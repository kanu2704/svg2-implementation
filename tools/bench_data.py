"""Benchmark data for regenerating the TRASER row of the SVG2 paper's Table 2 (PVSG, VidOR, SVG2test).

Every test video becomes one folder ``<bench>/<dataset>/<video_id>/`` with
  - ``masks.json``: TRASER's mask input (frames x objects, COCO RLE), one column per human object
  - ``gt.json``:    the human labels in one common format (below)
and the video itself is referenced by path (``gt["video"]``). ``gt.json`` is also copied to
``<results>/<dataset>/gt/`` so the evaluation can run later without the big data.

gt.json:
  {"dataset", "video_id", "video", "fps", "n_frames",
   "objects":   [{"col": mask column, "gt_id": human id, "name": human label}],
   "relations": [{"subj": gt_id or -1, "pred": str, "obj": gt_id or -1, "spans": [[t0, t1), ...]}],
   "time_unit": "seconds" | "index"}

Time: spans are half-open intervals. PVSG and VidOR give frame numbers, converted to seconds.
SVG2test gives indices into the 1-fps-sampled video, the same unit TRASER answers in, so it stays
in that unit ("index"): an inclusive [s, e] becomes [s, e + 1).

Masks (PVSG, VidOR): TRASER only reads the frames it samples (about 1 per second, at most 128), so
only those frames get real masks; every other frame holds an empty RLE. The sampled frames are
computed with TRASER's own function on the same video, so they are exactly the frames it reads.

Sources:
  PVSG     val split (62 videos: VidOR, Epic-Kitchens, Ego4D parts), Hugging Face Jingkang/PVSG.
           Masks: PNG per frame, pixel value = object id.
  VidOR    validation split (835 videos), Hugging Face shangxd/vidor. Labels are boxes; like the paper
           (Sec. 4.3) we turn them into masks with SAM 2 (box prompt on each sampled frame).
  SVG2test 100 videos (67 VIPSeg + 33 SA-V), Hugging Face UWGZQ/Synthetic_Visual_Genome2
           (data/SVG2_test + masks/SVG2_test). Videos: VIPSeg frames re-encoded at 6 fps and 720p
           (docs/DATA.md); SA-V mp4s from Meta's download links.
"""
import glob
import io
import json
import os
import subprocess
import sys
import zipfile
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))
sys.path.insert(0, str(REPO / "third_party/SVG2/traser"))

SVG2_REPO = "UWGZQ/Synthetic_Visual_Genome2"
VIDOR_REPO = "shangxd/vidor"


# ----------------------------------------------------------------------------- shared helpers
def rle(mask):
    from pycocotools import mask as mu
    r = mu.encode(np.asfortranarray(mask.astype(np.uint8)))
    return {"size": [int(r["size"][0]), int(r["size"][1])], "counts": r["counts"].decode()}


def traser_frames(video):
    """(sampled frame indices, number of frames, fps) exactly as TRASER's decode_video computes them."""
    import inference as T
    from decord import VideoReader
    vr = VideoReader(str(video))
    n, fps = len(vr), vr.get_avg_fps()
    return [int(i) for i in T._frame_indices(n, n / fps)], n, fps


def write_item(bench, results, gt, masks):
    d = Path(bench, gt["dataset"], gt["video_id"])
    d.mkdir(parents=True, exist_ok=True)
    with open(d / "masks.json", "w") as f:
        json.dump(masks, f)
    for path in (d / "gt.json", Path(results, gt["dataset"], "gt", f"{gt['video_id']}.json")):
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(gt, f, indent=1)
    return d


def item_ready(bench, dataset, video_id):
    d = Path(bench, dataset, video_id)
    return (d / "masks.json").exists() and (d / "gt.json").exists()


def load_gt(bench, dataset, video_id):
    return json.load(open(Path(bench, dataset, video_id, "gt.json")))


def clean_label(s):
    return str(s).replace("_", " ").strip()


# ----------------------------------------------------------------------------- PVSG
def pvsg_val_ids(anno):
    return [v for source in anno["split"] for v in anno["split"][source].get("val", [])]


def prepare_pvsg(pvsg_root, anno, video_id, bench, results):
    """One PVSG val video -> bench item. The mp4 and mask PNGs must be extracted already
    (pvsg_data.extract_videos)."""
    from PIL import Image
    import pvsg_data
    source = pvsg_data.video_source(anno, video_id)
    data = next(d for d in anno["data"] if d["video_id"] == video_id)
    video = Path(pvsg_root, source, "videos", f"{video_id}.mp4")
    pngs = sorted(Path(pvsg_root, source, "masks", video_id).glob("*.png"))
    sampled, n_frames, video_fps = traser_frames(video)
    fps = float(data["meta"].get("fps") or 5)

    objects = sorted(data["objects"], key=lambda o: o["object_id"])
    first = np.array(Image.open(pngs[0]))
    h, w = first.shape[:2]
    empty = rle(np.zeros((h, w), np.uint8))
    masks = [[empty] * len(objects) for _ in range(n_frames)]
    for f in sampled:
        if f >= len(pngs):
            continue
        m = np.array(Image.open(pngs[f]))
        if m.ndim == 3:
            m = m[..., 0]
        masks[f] = [rle(m == o["object_id"]) if (m == o["object_id"]).any() else empty for o in objects]

    rels = [{"subj": s, "pred": clean_label(p), "obj": o,
             "spans": [[a / fps, (b + 1) / fps] for a, b in spans]}
            for s, o, p, spans in data["relations"]]
    gt = {"dataset": "pvsg", "video_id": video_id, "source": source, "video": str(video), "fps": fps,
          "n_frames": n_frames, "video_fps": video_fps, "mask_pngs": len(pngs), "time_unit": "seconds",
          "objects": [{"col": k, "gt_id": o["object_id"], "name": clean_label(o["category"]),
                       "is_thing": o.get("is_thing")} for k, o in enumerate(objects)],
          "relations": rels}
    return write_item(bench, results, gt, masks)


# ----------------------------------------------------------------------------- VidOR
def download_vidor(root, token=None):
    """Validation videos + annotations from the Hugging Face mirror; returns {"videos": dir, "anno": dir}."""
    from huggingface_hub import hf_hub_download, list_repo_files
    files = list_repo_files(VIDOR_REPO, repo_type="dataset", token=token)
    print("files in", VIDOR_REPO, ":", files)
    val = [f for f in files if "val" in f.lower() and f.endswith(".zip")]
    vid_zip = [f for f in val if "video" in f.lower()]
    ann_zip = [f for f in val if "video" not in f.lower()]          # the annotation zip
    if not vid_zip or not ann_zip:
        raise FileNotFoundError(f"could not find validation video/annotation zips among {files}")
    out = {}
    for kind, name in (("videos", vid_zip[0]), ("anno", ann_zip[0])):
        target = Path(root, kind)
        if not target.exists() or not any(target.rglob("*")):
            local = hf_hub_download(VIDOR_REPO, name, repo_type="dataset", token=token,
                                    local_dir=os.path.join(root, "zips"))
            print("unzipping", name)
            with zipfile.ZipFile(local) as z:
                z.extractall(target)
            os.remove(local)
        out[kind] = str(target)
    return out


def vidor_index(vidor):
    """{video_id: (annotation json path, mp4 path)} for every validation video found."""
    mp4 = {Path(p).stem: p for p in glob.glob(os.path.join(vidor["videos"], "**", "*.mp4"), recursive=True)}
    ann = {Path(p).stem: p for p in glob.glob(os.path.join(vidor["anno"], "**", "*.json"), recursive=True)}
    return {v: (ann[v], mp4[v]) for v in sorted(ann) if v in mp4}


class BoxToMask:
    """SAM 2.1 (hiera-large) image predictor: box prompts -> masks. Loaded once, on first use."""
    def __init__(self, model_id="facebook/sam2.1-hiera-large"):
        import torch
        from sam2.sam2_image_predictor import SAM2ImagePredictor
        self.torch = torch
        self.predictor = SAM2ImagePredictor.from_pretrained(model_id, device="cuda")

    def __call__(self, image_rgb, boxes):
        torch = self.torch
        with torch.inference_mode(), torch.autocast("cuda", dtype=torch.float16):
            self.predictor.set_image(image_rgb)
            masks, _, _ = self.predictor.predict(box=np.asarray(boxes, dtype=np.float32), multimask_output=False)
        h, w = image_rgb.shape[:2]
        return np.asarray(masks).reshape(len(boxes), -1, h, w)[:, 0] > 0


def prepare_vidor(ann_path, video, bench, results, box_to_mask):
    from decord import VideoReader
    a = json.load(open(ann_path))
    video_id = str(a.get("video_id") or Path(ann_path).stem)
    sampled, n_frames, video_fps = traser_frames(video)
    fps = float(a.get("fps") or video_fps)
    objects = sorted(a["subject/objects"], key=lambda o: o["tid"])
    col = {o["tid"]: k for k, o in enumerate(objects)}
    vr = VideoReader(str(video))
    h, w = vr[0].shape[:2]
    empty = rle(np.zeros((h, w), np.uint8))
    masks = [[empty] * len(objects) for _ in range(n_frames)]
    frames = vr.get_batch(sampled).asnumpy()
    for f, img in zip(sampled, frames):
        boxes = a["trajectories"][f] if f < len(a["trajectories"]) else []
        boxes = [b for b in boxes if b["tid"] in col]
        if not boxes:
            continue
        sx, sy = w / float(a.get("width") or w), h / float(a.get("height") or h)
        xyxy = [[b["bbox"]["xmin"] * sx, b["bbox"]["ymin"] * sy, b["bbox"]["xmax"] * sx, b["bbox"]["ymax"] * sy]
                for b in boxes]
        row = list(masks[f])
        for b, m in zip(boxes, box_to_mask(img, xyxy)):
            row[col[b["tid"]]] = rle(m)
        masks[f] = row

    rels = [{"subj": r["subject_tid"], "pred": clean_label(r["predicate"]), "obj": r["object_tid"],
             "spans": [[r["begin_fid"] / fps, r["end_fid"] / fps]]}           # VidOR's end_fid is exclusive
            for r in a["relation_instances"]]
    gt = {"dataset": "vidor", "video_id": video_id, "video": str(video), "fps": fps, "n_frames": n_frames,
          "video_fps": video_fps, "ann_frames": a.get("frame_count"), "time_unit": "seconds",
          "objects": [{"col": k, "gt_id": o["tid"], "name": clean_label(o["category"])} for k, o in enumerate(objects)],
          "relations": rels}
    return write_item(bench, results, gt, masks)


# ----------------------------------------------------------------------------- SVG2test
def download_svg2test(root, token=None):
    from huggingface_hub import snapshot_download
    snapshot_download(SVG2_REPO, repo_type="dataset", local_dir=root, token=token,
                      allow_patterns=["data/SVG2_test/*", "masks/SVG2_test/*"])
    return root


def svg2test_rows(root):
    """{video_id: {"split": "sav"|"vipseg", "objects": [...], "relationships": [...]}}"""
    import pyarrow.parquet as pq
    rows = {}
    for split in ("sav", "vipseg"):
        for p in sorted(glob.glob(os.path.join(root, "data/SVG2_test", split, "*.parquet"))):
            t = pq.read_table(p).to_pylist()
            for r in t:
                parse = lambda x: json.loads(x) if isinstance(x, str) and x else (x or [])  # noqa: E731
                rows[r["video_id"]] = {"split": split, "objects": parse(r["objects"]),
                                       "relationships": parse(r["relationships"])}
    return rows


def svg2test_masks(root):
    """{video_id: masks (frames x objects RLE)}: the same unpacking as their prepare_svg2.convert_masks."""
    import pyarrow.parquet as pq
    out = {}
    for split in ("sav", "vipseg"):
        for p in sorted(glob.glob(os.path.join(root, "masks/SVG2_test", split, "*.parquet"))):
            for batch in pq.ParquetFile(p).iter_batches(batch_size=4):
                for r in batch.to_pylist():
                    n_obj, n_fr = int(r["num_objects"]), int(r["num_frames"])
                    h, w = int(r["mask_height"]), int(r["mask_width"])
                    c = r["counts"]
                    out[r["video_id"]] = [[{"size": [h, w], "counts": c[f * n_obj + o]} for o in range(n_obj)]
                                          for f in range(n_fr)]
    return out


def vipseg_to_mp4(frames_dir, out_mp4, fps=6, height=720):
    """docs/DATA.md: VIPSeg frames (720p) re-encoded per video at 6 fps."""
    out_mp4 = Path(out_mp4)
    if out_mp4.exists():
        return out_mp4
    out_mp4.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["ffmpeg", "-loglevel", "error", "-y", "-framerate", str(fps), "-pattern_type", "glob",
           "-i", os.path.join(str(frames_dir), "*.jpg"),
           "-vf", f"scale=trunc(oh*a/2)*2:{height}", "-c:v", "libx264", "-pix_fmt", "yuv420p", str(out_mp4)]
    subprocess.run(cmd, check=True)
    return out_mp4


def extract_vipseg_frames(archive, video_ids, out_dir):
    """Copy only the needed videos' frames (imgs/<video>/*.jpg) out of the VIPSeg download.
    The download may be a zip or a tar (.tar, .tar.gz, ...); anything else raises a clear error."""
    import tarfile
    wanted = set(video_ids)
    already = {v for v in wanted if any(Path(out_dir, v).glob("*.jpg"))}
    if already == wanted:                       # extracted in an earlier run of this session
        return already
    found = set()

    def keep(name, read):
        parts = name.split("/")
        if len(parts) >= 3 and parts[-3] == "imgs" and parts[-2] in wanted and parts[-1].endswith(".jpg"):
            target = Path(out_dir, parts[-2], parts[-1])
            if not target.exists():
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(read())
            found.add(parts[-2])

    if zipfile.is_zipfile(archive):
        with zipfile.ZipFile(archive) as z:
            for m in z.infolist():
                keep(m.filename, lambda m=m: z.read(m))
    elif tarfile.is_tarfile(archive):
        with tarfile.open(archive, "r:*") as t:
            for m in t:
                if m.isfile():
                    keep(m.name, lambda m=m: t.extractfile(m).read())
    else:
        head = open(archive, "rb").read(300)
        size = os.path.getsize(archive)
        if head.lstrip().startswith(b"<"):
            raise RuntimeError(f"the VIPSeg download is a web page ({size} bytes), not the dataset: Google Drive "
                               "refused (download limit). Delete it and download VIPSeg by hand (see the notebook).")
        raise RuntimeError(f"unknown archive type for {archive} ({size} bytes), first bytes: {head[:16]!r}")
    return found


def sav_links(links_file):
    """Meta's SA-V download list: lines '<file_name>\\t<url>' -> {file_name: url}."""
    links = {}
    for line in open(links_file):
        parts = line.strip().split()
        if len(parts) >= 2 and parts[0].endswith(".tar"):
            links[parts[0]] = parts[-1]
    return links


def fetch_sav_videos(links, video_ids, out_dir, fps=24):
    """Get the SA-V videos SVG2test uses, streaming Meta's tar files (nothing else is written to disk).

    SA-V's validation/test parts (sav_val.tar, sav_test.tar, ...) store each video as JPEG frames
    (<split>/JPEGImages_24fps/<video_id>/*.jpg); those are tried first and re-encoded to a 24 fps mp4.
    The training parts (sav_000.tar, ...) hold mp4s; sav_XXXYYY would be in sav_XXX.tar, tried last."""
    import re
    import tarfile
    import urllib.request
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    frames_root = out_dir / "_frames"
    need = {v for v in video_ids if not (out_dir / f"{v}.mp4").exists()}
    other = sorted(n for n in links if not re.fullmatch(r"sav_\d{3}\.tar", n))
    train = sorted({f"sav_{int(v.split('_')[1]) // 1000:03d}.tar" for v in need} & set(links))
    for shard in other + train:
        if not need:
            break
        print(f"streaming {shard} for {len(need)} videos ...", flush=True)
        got_frames = set()
        with urllib.request.urlopen(links[shard]) as resp, tarfile.open(fileobj=resp, mode="r|*") as tar:
            for m in tar:
                if not m.isfile():
                    continue
                parts = m.name.split("/")
                stem = Path(m.name).stem
                if m.name.endswith(".mp4") and stem in need:
                    (out_dir / f"{stem}.mp4").write_bytes(tar.extractfile(m).read())
                    need.discard(stem)
                    print("  got", stem, "(mp4)", flush=True)
                elif (m.name.endswith(".jpg") and len(parts) >= 3 and parts[-2] in need
                      and "JPEGImages_24fps" in parts):
                    target = frames_root / parts[-2] / parts[-1]
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(tar.extractfile(m).read())
                    got_frames.add(parts[-2])
        for v in sorted(got_frames):
            cmd = ["ffmpeg", "-loglevel", "error", "-y", "-framerate", str(fps), "-pattern_type", "glob",
                   "-i", str(frames_root / v / "*.jpg"), "-c:v", "libx264", "-pix_fmt", "yuv420p",
                   str(out_dir / f"{v}.mp4")]
            subprocess.run(cmd, check=True)
            need.discard(v)
            print("  got", v, f"({len(list((frames_root / v).glob('*.jpg')))} frames)", flush=True)
        print(f"  after {shard}: {len(need)} still missing", flush=True)
    return need


def prepare_svg2test(video_id, row, masks, video, bench, results):
    objects = []
    for o in row["objects"]:
        key = next(k for k in o if k.startswith("object_"))
        objects.append({"col": int(key.split("_")[1]), "gt_id": int(key.split("_")[1]), "name": clean_label(o[key])})
    objects.sort(key=lambda o: o["col"])
    n_cols = len(masks[0]) if masks else 0
    bad = [o["col"] for o in objects if o["col"] >= n_cols]
    rels = [{"subj": r[0], "pred": clean_label(r[1]), "obj": r[2],
             "spans": [[float(a), float(b) + 1] for a, b in r[3]]}
            for r in row["relationships"]]
    sampled, n_frames, video_fps = traser_frames(video)
    gt = {"dataset": "svg2test", "video_id": video_id, "source": row["split"], "video": str(video),
          "fps": video_fps, "n_frames": n_frames, "mask_frames": len(masks), "time_unit": "index",
          "objects_without_mask_column": bad,
          "objects": [o for o in objects if o["col"] < n_cols], "relations": rels}
    return write_item(bench, results, gt, masks)
