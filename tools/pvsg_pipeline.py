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
                raw = client.chat.completions.create(**kw).choices[0].message.content or ""
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
    def __init__(self, client, model):
        self.client, self.model = client, model

    def structure(self, description):
        msgs = [{"role": "system", "content": P.STRUCTURE_SYSTEM_PROMPT},
                {"role": "user", "content": P.build_structure_prompt(description)}]
        schema = {"name": "scene_graph", "schema": P.SCENE_GRAPH_SCHEMA, "strict": True}
        settings = dict(temperature=0.6, top_p=0.95, extra_body=THINK_OFF) if "nemotron" in self.model else dict(temperature=0.6)
        return P._validate_scene_graph(ask(self.client, self.model, msgs, settings, schema, max_tokens=2048))


class NimExtractor:
    """Stands in for their RelationshipExtractor: same system prompts and schemas, one call per kind."""
    def __init__(self, client, model, max_tokens):
        self.client, self.model, self.max_tokens = client, model, max_tokens

    def extract(self, user_content, kind):
        for item in user_content:                    # NIM rejects OpenAI's image "detail" field
            if item["type"] == "image_url":
                item["image_url"].pop("detail", None)
        sys_prompt, schema = {"temporal": (P.TEMPORAL_RELATION_SYS_PROMPT, P.TEMPORAL_RELATION_SCHEMA),
                              "spatial": (P.SPATIAL_RELATION_SYS_PROMPT, P.SPATIAL_RELATION_SCHEMA)}[kind]
        msgs = [{"role": "system", "content": sys_prompt}, {"role": "user", "content": user_content}]
        return ask(self.client, self.model, msgs, dict(temperature=0.6), schema, self.max_tokens).get("relationships", [])


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
    return cfg


def set_status(vdir, **kw):
    path = Path(vdir) / "status.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    st = json.load(open(path)) if path.exists() else {}
    st.update(kw, updated=time.strftime("%H:%M:%S"))
    json.dump(st, open(path, "w"), indent=1)


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


def run_video(video_id, args, anno, client):
    source = pvsg_data.video_source(anno, video_id)
    video = Path(args.pvsg_root, source, "videos", f"{video_id}.mp4")
    cfg = make_cfg(video, args.out, args)
    vdir = Path(args.out, video_id)
    vdir.mkdir(parents=True, exist_ok=True)
    set_status(vdir, video=video_id, state="running", started=time.strftime("%Y-%m-%d %H:%M"))
    timings = json.load(open(vdir / "status.json")).get("seconds", {})

    def done(k):
        return P.artifact_path(cfg, k).exists()

    for k in range(1, 5):                          # their Pipeline, one stage at a time (resumable)
        if done(k):
            continue
        set_status(vdir, stage=f"{k} {P.STAGE_NAMES[k - 1]}")
        t0 = time.time()
        cfg.start_stage, cfg.end_stage = k, k
        P.Pipeline(cfg).run()
        timings[str(k)] = round(time.time() - t0)
        set_status(vdir, seconds=timings)

    frames = fps = None
    if not done(5):
        set_status(vdir, stage="5 structure")
        t0 = time.time()
        scene = P.stage5_structure(cfg, P.read_json(P.artifact_path(cfg, 4)), P.read_json(P.artifact_path(cfg, 3)),
                                   NimStructurer(client, args.stage5_model))
        P.write_json(P.artifact_path(cfg, 5), scene)
        timings["5"] = round(time.time() - t0)
        set_status(vdir, seconds=timings)
    if not done(6):
        set_status(vdir, stage="6 relationships")
        t0 = time.time()
        frames, fps, _, _ = P.read_video_frames(str(video))
        graph = P.stage6_relationships(cfg, P.read_json(P.artifact_path(cfg, 5)), frames, fps,
                                       NimExtractor(client, args.stage6_model, cfg.relationship.max_completion_tokens))
        P.write_json(P.artifact_path(cfg, 6), graph)
        timings["6"] = round(time.time() - t0)
        set_status(vdir, seconds=timings)
    out7 = vdir / "pvsg_format.json"
    if not out7.exists():
        set_status(vdir, stage="7 align to PVSG")
        t0 = time.time()
        aligned = stage7_align(P.read_json(P.artifact_path(cfg, 6)), anno, client, args.map_model, video_id)
        aligned["settings"] = {"stage1_every": args.stage1_every, "max_rel_frames": args.max_rel_frames,
                               "stage5_model": args.stage5_model, "stage6_model": args.stage6_model,
                               "map_model": args.map_model}
        json.dump(aligned, open(out7, "w"), indent=1)
        timings["7"] = round(time.time() - t0)
    set_status(vdir, state="done", stage="finished", seconds=timings)


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
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(name)s | %(message)s", stream=sys.stdout)

    anno = pvsg_data.load_anno(args.pvsg_root)
    client = nim_client(args.timeout)
    for v in args.videos:
        log.info("########## %s ##########", v)
        try:
            run_video(v, args, anno, client)
        except Exception as e:  # noqa: BLE001 - keep going with the next video
            log.error("%s failed: %s\n%s", v, e, traceback.format_exc())
            set_status(Path(args.out, v), state="failed", error=f"{type(e).__name__}: {str(e)[:300]}")


if __name__ == "__main__":
    main()
