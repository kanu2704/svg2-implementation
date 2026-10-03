"""Option A on PVSG: the full SVG2 pipeline from the raw video, resumable, one video after another.

    python3 tools/pvsg_pipeline.py --pvsg_root /kaggle/tmp/pvsg --out /kaggle/working/pvsg_runs --videos ID1 ID2

Stages 1-4 are their Pipeline (SAM2 masks, SAM2 tracking, cleanup, DAM), stages 5-6 their stage functions
with NVIDIA NIM models (same prompts and schemas as theirs), stage 7 is ours: map the open-vocabulary
names and predicates to PVSG's classes and write the result in PVSG's format.

Changes for PVSG's 5-fps videos (their thresholds count frames, not seconds):
  * stage 1 on every 5th frame (1 per second) instead of every 20th;
  * every stage-1 frame is a re-discovery check (adaptive_sample_rate off), i.e. one check per second;
  * DAM describes every tracked object (their default: only the 40 largest);
  * stage 6 sees 1 frame per second, capped at --max_rel_frames.

Speed options (--fast = all four; off by default, so the default run is their code as is):
  * --fp16: T4s have no bfloat16 hardware, so their bfloat16 autocast (SAM2 stages 1-2) runs on slow
    paths; run it in float16 instead (T4 tensor cores). Slightly different numerics.
  * --no_offload: keep SAM2's video frames and tracking memory on the GPU (their default copies them
    to CPU RAM and back every frame). Fine for short videos; more GPU memory.
  * --points_per_batch 256: stage 1 sends 256 grid points through SAM2 at once instead of 64
    (same masks, better use of the GPU).
  * --overlap: while the GPU starts SAM2 on the next video, stages 5-7 (internet calls, no GPU) of
    the previous video run in a background thread.

Every stage's artifact is written to <out>/<video_id>/; a rerun skips the stages already done.
Progress: <out>/<video_id>/status.json. The NIM key comes from $NVIDIA_API_KEY or /root/.svg2_keys.
"""
import argparse
import json
import logging
import os
import re
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "third_party/SVG2/pipeline"))
sys.path.insert(0, str(REPO / "tools"))
import svg2_pipeline as P  # noqa: E402
import pvsg_data  # noqa: E402

log = logging.getLogger("pvsg")
NIM_URL = "https://integrate.api.nvidia.com/v1"
THINK_OFF = {"chat_template_kwargs": {"enable_thinking": False}}


# ----------------------------------------------------------------------------- NIM calls
def nim_client(timeout):
    from openai import OpenAI
    if not os.environ.get("NVIDIA_API_KEY") and os.path.exists("/root/.svg2_keys"):
        for line in open("/root/.svg2_keys"):
            k, _, v = line.strip().partition("=")
            if k and v:
                os.environ.setdefault(k, v)
    if not os.environ.get("NVIDIA_API_KEY"):
        raise SystemExit("NVIDIA_API_KEY not set (environment or /root/.svg2_keys)")
    return OpenAI(base_url=NIM_URL, api_key=os.environ["NVIDIA_API_KEY"], timeout=timeout)


def extract_json(text):
    """Some models wrap the JSON in thoughts or ``` fences: take the first {...} that parses."""
    if not text:
        return None
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.S)
    for m in re.finditer(r"\{", text):
        depth = 0
        for j in range(m.start(), len(text)):
            depth += {"{": 1, "}": -1}.get(text[j], 0)
            if depth == 0:
                try:
                    return json.loads(text[m.start():j + 1])
                except json.JSONDecodeError:
                    break
    return None


def ask(client, model, messages, settings, schema=None, max_tokens=4096, tries=2):
    """Strict JSON schema -> JSON mode -> plain text, like their extractors; every attempt is logged."""
    formats = ([("json_schema", {"type": "json_schema", "json_schema": schema})] if schema else []) + \
              [("json_object", {"type": "json_object"}), ("plain", None)]
    last = None
    for attempt in range(tries):
        for name, fmt in formats:
            kw = dict(model=model, messages=messages, max_tokens=max_tokens, **settings)
            if fmt:
                kw["response_format"] = fmt
            t0 = time.time()
            try:
                resp = client.chat.completions.create(**kw)
                if not getattr(resp, "choices", None):   # NIM sometimes answers 200 with no choices
                    raise RuntimeError(f"empty reply from the server: {str(resp)[:300]}")
                raw = resp.choices[0].message.content or ""
                parsed = extract_json(raw)
                if parsed is not None:
                    log.info("    %s: ok via %s in %.0f s", model, name, time.time() - t0)
                    return parsed
                last = f"{name}: no JSON in reply ({raw[:100]!r})"
            except Exception as e:  # noqa: BLE001
                last = f"{name}: {type(e).__name__}: {str(e)[:200]}"
            log.warning("    %s attempt %d (%s) failed after %.0f s: %s", model, attempt + 1, name, time.time() - t0, last)
    raise RuntimeError(last)


class NimStructurer:
    """Stands in for their SceneGraphStructurer: same prompt, schema and validation."""
    def __init__(self, client, model, progress):
        self.client, self.model, self.progress = client, model, progress

    def structure(self, description):
        msgs = [{"role": "system", "content": P.STRUCTURE_SYSTEM_PROMPT},
                {"role": "user", "content": P.build_structure_prompt(description)}]
        schema = {"name": "scene_graph", "schema": P.SCENE_GRAPH_SCHEMA, "strict": True}
        settings = dict(temperature=0.6, top_p=0.95, extra_body=THINK_OFF) if "nemotron" in self.model else dict(temperature=0.6)
        record = P._validate_scene_graph(ask(self.client, self.model, msgs, settings, schema, max_tokens=2048))
        self.progress.tick()
        return record


class NimExtractor:
    """Stands in for their RelationshipExtractor: same system prompts and schemas, one call per kind."""
    def __init__(self, client, model, max_tokens, progress):
        self.client, self.model, self.max_tokens, self.progress = client, model, max_tokens, progress

    def extract(self, user_content, kind):
        for item in user_content:                    # NIM rejects OpenAI's image "detail" field
            if item["type"] == "image_url":
                item["image_url"].pop("detail", None)
        sys_prompt, schema = {"temporal": (P.TEMPORAL_RELATION_SYS_PROMPT, P.TEMPORAL_RELATION_SCHEMA),
                              "spatial": (P.SPATIAL_RELATION_SYS_PROMPT, P.SPATIAL_RELATION_SCHEMA)}[kind]
        msgs = [{"role": "system", "content": sys_prompt}, {"role": "user", "content": user_content}]
        rels = ask(self.client, self.model, msgs, dict(temperature=0.6), schema, self.max_tokens,
                   tries=1).get("relationships", [])          # stage 6 retries with fewer/smaller frames instead
        self.progress.tick()
        return rels


MAP_PROMPT = """You map free-text labels from an automatic video annotator onto a fixed vocabulary.
For every object name, give the single closest class from OBJECT_CLASSES, or "none" if no class fits.
For every relation predicate, give the single closest predicate from PREDICATES, or "none" if none fits.
Match meaning, not spelling ("young person" -> "child" or "adult" as appropriate; "positioned on" -> "on").
Answer only with JSON: {"objects": {"<name>": "<class>"}, "predicates": {"<predicate>": "<predicate>"}}.

OBJECT_CLASSES: %s
PREDICATES: %s
OBJECT NAMES: %s
RELATION PREDICATES: %s"""


# ----------------------------------------------------------------------------- one video
def make_cfg(video_path, out, args):
    cfg = P.PipelineConfig()
    cfg.io.video_path, cfg.io.output_dir = str(video_path), str(out)
    cfg.runtime.device = "cuda"
    cfg.mask_gen.frame_sample_rate = args.stage1_every
    cfg.tracking.adaptive_sample_rate = False
    cfg.caption.max_objects = cfg.tracking.max_objects
    cfg.relationship.max_frames = args.max_rel_frames
    cfg.mask_gen.points_per_batch = args.points_per_batch
    cfg.tracking.offload_to_cpu = not args.no_offload
    return cfg


def use_fp16_autocast():
    """Their stages 1-2 run under torch.autocast("cuda", dtype=torch.bfloat16). On GPUs without
    bfloat16 hardware (compute capability < 8, e.g. T4) swap that for float16."""
    import torch
    if not torch.cuda.is_available() or torch.cuda.get_device_capability()[0] >= 8:
        return False
    original = torch.autocast

    class Float16Autocast(original):
        def __init__(self, device_type, dtype=None, *a, **k):
            if device_type == "cuda" and dtype == torch.bfloat16:
                dtype = torch.float16
            super().__init__(device_type, dtype, *a, **k)

    torch.autocast = Float16Autocast
    return True


def set_status(vdir, **kw):
    path = Path(vdir) / "status.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    st = json.load(open(path)) if path.exists() else {}
    st.update(kw, updated=time.strftime("%H:%M:%S"))
    json.dump(st, open(path, "w"), indent=1)


class Progress(logging.Handler):
    """Live progress for the bars in pvsg_run.ipynb: writes step / done / total into status.json.

    Stages 1, 2 and 4 are their code, so we read their own log lines ("frame 5: 91 -> 54 masks",
    "object 3: ...") and count the frames SAM2 tracking yields; stages 5-7 count our API calls."""
    def __init__(self):
        super().__init__(level=logging.INFO)
        self.vdir, self.step, self.done, self.total, self.t = None, None, 0, 0, 0.0

    def set(self, step, done, total, force=True):
        self.step, self.done, self.total = step, done, total
        if self.vdir and (force or time.time() - self.t > 5 or done >= total):
            self.t = time.time()
            set_status(self.vdir, step=step, done=done, total=total)

    def tick(self):
        self.set(self.step, self.done + 1, self.total, force=False)

    def emit(self, record):
        msg = record.getMessage()
        m = re.match(r"Stage 1: generating masks on (\d+) / \d+ frames", msg)
        if m:
            self.set("SAM2 masks: frames", 0, int(m[1]))
        elif re.match(r"\s+frame \d+: \d+ -> \d+ masks", msg):
            self.tick()
        elif msg.startswith("Stage 2 pass 1 complete"):
            self.set("SAM2 tracking, pass 2 of 2: frames", 0, self.total)
        elif re.match(r"Stage 4: describing (\d+) objects", msg):
            self.set("DAM: objects described", 0, int(re.match(r"Stage 4: describing (\d+)", msg)[1]))
        elif re.match(r"\s+object \d+: ", msg) and (self.step or "").startswith("DAM"):
            self.tick()


PROGRESS = Progress()
_their_propagate = P.VideoTracker.propagate


def _propagate_with_progress(self, state, start_frame, max_frames):
    """Their VideoTracker.propagate, unchanged, plus a frame counter for the progress bar."""
    total = state.get("num_frames", 0) if isinstance(state, dict) else 0
    if not (PROGRESS.step or "").startswith("SAM2 tracking"):
        PROGRESS.set("SAM2 tracking, pass 1 of 2: frames", 0, total)
    for frame_idx, tracked in _their_propagate(self, state, start_frame, max_frames):
        PROGRESS.set(PROGRESS.step, frame_idx + 1, total or PROGRESS.total, force=False)
        yield frame_idx, tracked


P.VideoTracker.propagate = _propagate_with_progress


def to_frames(span, sampled, total):
    """Stage-6 span over sampled frames [a, b] -> PVSG frames [sampled[a], frame before sampled[b+1]]."""
    a, b = max(0, int(span[0])), min(len(sampled) - 1, int(span[1]))
    if a > b:
        return None
    end = sampled[b + 1] - 1 if b + 1 < len(sampled) else total - 1
    return [sampled[a], end]


def stage7_align(graph, anno, client, model, video_id):
    """Ours: map names/predicates to PVSG classes and write PVSG's relation format."""
    names = sorted({o["name"] for o in graph["objects"]})
    rels = graph["relationships"]
    preds = sorted({r[1] for r in rels["temporal"] + rels["spatial"] if isinstance(r, list) and len(r) >= 4})
    classes = anno["objects"]["thing"] + anno["objects"]["stuff"]
    prompt = MAP_PROMPT % (json.dumps(classes), json.dumps(anno["relations"]), json.dumps(names), json.dumps(preds))
    mapping = ask(client, model, [{"role": "user", "content": prompt}], dict(temperature=0.2), max_tokens=4096)
    obj_map = {k: (v if v in classes else "none") for k, v in mapping.get("objects", {}).items()}
    pred_map = {k: (v if v in anno["relations"] else "none") for k, v in mapping.get("predicates", {}).items()}

    sampled, total = rels["sampled_frame_indices"], graph["total_frames"]
    ids = {o["object_id"] for o in graph["objects"]}
    open_rels, pvsg_rels = [], {}
    for kind in ("temporal", "spatial"):
        for r in rels[kind]:
            if not (isinstance(r, list) and len(r) >= 4 and isinstance(r[3], list)):
                continue
            frames = [f for f in (to_frames(s, sampled, total) for s in r[3] if isinstance(s, list) and len(s) == 2) if f]
            p = pred_map.get(r[1], "none")
            open_rels.append({"subject": r[0], "predicate": r[1], "object": r[2], "frames": frames,
                              "kind": kind, "pvsg_predicate": p})
            if p != "none" and r[0] in ids and r[2] in ids and r[0] != r[2] and frames:
                pvsg_rels.setdefault((r[0], r[2], p), []).extend(frames)
    return {
        "video_id": video_id,
        "meta": {"height": graph["height"], "width": graph["width"], "num_frames": total},
        "objects": [{"object_id": o["object_id"], "name": o["name"], "category": obj_map.get(o["name"], "none"),
                     "is_thing": obj_map.get(o["name"]) in anno["objects"]["thing"], "attributes": o["attributes"]}
                    for o in graph["objects"]],
        "relations": [[s, o, p, sorted(fr)] for (s, o, p), fr in pvsg_rels.items()],
        "relations_open": open_rels,
        "name_map": obj_map, "predicate_map": pred_map,
    }


def video_paths(video_id, args, anno):
    source = pvsg_data.video_source(anno, video_id)
    video = Path(args.pvsg_root, source, "videos", f"{video_id}.mp4")
    return video, make_cfg(video, args.out, args), Path(args.out, video_id)


def timings_of(vdir):
    p = Path(vdir) / "status.json"
    return json.load(open(p)).get("seconds", {}) if p.exists() else {}


def run_gpu_stages(video_id, args, anno):
    """Stages 1-4 (SAM2, cleanup, DAM): their Pipeline, one stage at a time (resumable)."""
    video, cfg, vdir = video_paths(video_id, args, anno)
    vdir.mkdir(parents=True, exist_ok=True)
    set_status(vdir, video=video_id, state="running", started=time.strftime("%Y-%m-%d %H:%M"))
    PROGRESS.vdir, PROGRESS.step = vdir, None
    timings = timings_of(vdir)
    for k in range(1, 5):
        if P.artifact_path(cfg, k).exists():
            continue
        set_status(vdir, stage=f"{k} {P.STAGE_NAMES[k - 1]}")
        PROGRESS.set({1: "SAM2: loading model", 2: "SAM2 tracking: loading video", 3: "cleanup",
                      4: "DAM: loading model"}[k], 0, 1)
        t0 = time.time()
        cfg.start_stage, cfg.end_stage = k, k
        P.Pipeline(cfg).run()
        timings[str(k)] = round(time.time() - t0)
        set_status(vdir, seconds=timings)
    PROGRESS.vdir = None


def run_api_stages(video_id, args, anno, client):
    """Stages 5-7: internet calls only (no GPU), so they can overlap with the next video's SAM2."""
    video, cfg, vdir = video_paths(video_id, args, anno)
    progress = Progress()
    progress.vdir = vdir
    timings = timings_of(vdir)
    if not P.artifact_path(cfg, 5).exists():
        set_status(vdir, stage="5 structure")
        t0 = time.time()
        descs = P.read_json(P.artifact_path(cfg, 4))
        progress.set("names (NIM): objects", 0, len(descs["objects"]))
        scene = P.stage5_structure(cfg, descs, P.read_json(P.artifact_path(cfg, 3)),
                                   NimStructurer(client, args.stage5_model, progress))
        P.write_json(P.artifact_path(cfg, 5), scene)
        timings["5"] = round(time.time() - t0)
        set_status(vdir, seconds=timings)
    if not P.artifact_path(cfg, 6).exists():
        set_status(vdir, stage="6 relationships")
        t0 = time.time()
        frames, fps, _, _ = P.read_video_frames(str(video))
        scene = P.read_json(P.artifact_path(cfg, 5))
        graph, last = None, None
        # Kimi K3 on NIM returned empty replies for 16 full-size frames in one request (it handled 5):
        # retry with fewer and smaller frames. The frames actually used are saved in the artifact.
        for n_frames, width in stage6_attempts(args.max_rel_frames):
            cfg.relationship.max_frames = n_frames
            progress.set(f"relations (NIM, {n_frames} frames @ {width}px): calls", 0, 2)
            try:
                with smaller_frames(width):
                    graph = P.stage6_relationships(cfg, scene, frames, fps,
                                                   NimExtractor(client, args.stage6_model,
                                                                cfg.relationship.max_completion_tokens, progress))
                graph["relationships"]["frames_sent"] = {"max_frames": n_frames, "width": width}
                break
            except RuntimeError as e:
                last = e
                log.warning("stage 6 with %d frames at %d px failed (%s); trying fewer/smaller", n_frames, width, e)
        if graph is None:
            raise RuntimeError(f"stage 6 failed with every frame setting: {last}")
        P.write_json(P.artifact_path(cfg, 6), graph)
        timings["6"] = round(time.time() - t0)
        set_status(vdir, seconds=timings)
    out7 = vdir / "pvsg_format.json"
    if not out7.exists():
        set_status(vdir, stage="7 align to PVSG")
        t0 = time.time()
        progress.set("map to PVSG (NIM): calls", 0, 1)
        aligned = stage7_align(P.read_json(P.artifact_path(cfg, 6)), anno, client, args.map_model, video_id)
        progress.tick()
        aligned["settings"] = {k: getattr(args, k) for k in (
            "stage1_every", "max_rel_frames", "stage5_model", "stage6_model", "map_model",
            "fp16", "no_offload", "points_per_batch", "overlap")}
        json.dump(aligned, open(out7, "w"), indent=1)
        timings["7"] = round(time.time() - t0)
    set_status(vdir, state="done", stage="finished", seconds=timings, step="finished", done=1, total=1)


def stage6_attempts(max_frames):
    """(frames per request, image width) to try, best first."""
    out = []
    for n, w in ((max_frames, 640), (16, 512), (8, 512), (5, 448)):
        n = min(n, max_frames)
        if (n, w) not in out:
            out.append((n, w))
    return out


class smaller_frames:
    """Temporarily make their stage-6 JPEG encoder downscale frames to `width` pixels wide."""
    def __init__(self, width):
        self.width = width

    def __enter__(self):
        import cv2
        self.original = P._encode_frame_data_url
        width = self.width

        def encode(frame_rgb, quality=90):
            h, w = frame_rgb.shape[:2]
            if w > width:
                frame_rgb = cv2.resize(frame_rgb, (width, round(h * width / w)), interpolation=cv2.INTER_AREA)
            return self.original(frame_rgb, quality=85)
        P._encode_frame_data_url = encode

    def __exit__(self, *exc):
        P._encode_frame_data_url = self.original
        return False


def failed(video_id, args, e):
    log.error("%s failed: %s\n%s", video_id, e, traceback.format_exc())
    set_status(Path(args.out, video_id), state="failed", error=f"{type(e).__name__}: {str(e)[:300]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pvsg_root", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--videos", nargs="+", required=True)
    ap.add_argument("--stage1_every", type=int, default=5, help="stage-1 mask generation every N frames (5 = 1/s at 5 fps)")
    ap.add_argument("--max_rel_frames", type=int, default=40)
    ap.add_argument("--stage5_model", default="nvidia/nemotron-3.5-lightning-30b-a3b")
    ap.add_argument("--stage6_model", default="moonshotai/kimi-k3")
    ap.add_argument("--map_model", default="moonshotai/kimi-k3")
    ap.add_argument("--timeout", type=float, default=240)
    ap.add_argument("--fast", action="store_true", help="= --fp16 --no_offload --points_per_batch 256 --overlap")
    ap.add_argument("--fp16", action="store_true", help="SAM2 in float16 instead of bfloat16 (T4 has no bf16 hardware)")
    ap.add_argument("--no_offload", action="store_true", help="keep SAM2 tracking state on the GPU")
    ap.add_argument("--points_per_batch", type=int, default=64, help="stage-1 grid points per SAM2 batch (theirs: 64)")
    ap.add_argument("--overlap", action="store_true", help="run stages 5-7 of a video while the GPU starts the next one")
    args = ap.parse_args()
    if args.fast:
        args.fp16 = args.no_offload = args.overlap = True
        args.points_per_batch = max(args.points_per_batch, 256)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(name)s | %(message)s", stream=sys.stdout)
    logging.getLogger("svg2").addHandler(PROGRESS)

    if args.fp16:
        log.info("float16 autocast for SAM2: %s", "on" if use_fp16_autocast() else "not needed on this GPU")
    log.info("settings: points_per_batch=%d, offload_to_cpu=%s, overlap=%s",
             args.points_per_batch, not args.no_offload, args.overlap)

    anno = pvsg_data.load_anno(args.pvsg_root)
    client = nim_client(args.timeout)
    api = ThreadPoolExecutor(max_workers=1) if args.overlap else None
    pending = []

    def api_stages(v):
        try:
            run_api_stages(v, args, anno, client)
        except Exception as e:  # noqa: BLE001 - keep going with the next video
            failed(v, args, e)

    for v in args.videos:
        log.info("########## %s ##########", v)
        try:
            run_gpu_stages(v, args, anno)
        except Exception as e:  # noqa: BLE001 - keep going with the next video
            failed(v, args, e)
            continue
        if api:
            pending.append(api.submit(api_stages, v))
        else:
            api_stages(v)
    for f in pending:
        f.result()


if __name__ == "__main__":
    main()
