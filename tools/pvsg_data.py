"""PVSG data: download from Hugging Face, choose videos, extract only those videos.

PVSG (Yang et al., CVPR 2023) is mirrored at https://huggingface.co/datasets/Jingkang/PVSG with the
layout of OpenPVSG's ``data_zip/`` folder: ``pvsg.json`` plus, per source, ``<source>_videos.zip`` and
``<source>_masks.zip``. The videos are already at 5 fps (one video frame = one PVSG frame) and every
frame has a mask PNG whose pixel value is the object id (``mask == 7`` is object 7).

We never unpack whole zips: ``extract_videos`` copies out only the chosen videos, as
``<root>/<source>/videos/<id>.mp4`` and ``<root>/<source>/masks/<id>/0000.png …`` (OpenPVSG's layout).
"""
import io
import json
import os
import zipfile
from pathlib import Path

REPO_ID = "Jingkang/PVSG"
SOURCES = {"vidor": "vidor", "epic_kitchen": "epic_kitchen", "ego4d": "ego4d"}   # pvsg.json split key -> zip prefix


def download(root, sources=("vidor",), token=None):
    """Download pvsg.json and the chosen sources' zips into <root>/data_zip. Returns {name: local path}."""
    from huggingface_hub import hf_hub_download, list_repo_files

    files = list_repo_files(REPO_ID, repo_type="dataset", token=token)
    wanted = {"pvsg.json"} | {f"{s}_{kind}.zip" for s in sources for kind in ("videos", "masks")}
    found = {}
    for f in files:
        if os.path.basename(f) in wanted:
            found[os.path.basename(f)] = hf_hub_download(REPO_ID, f, repo_type="dataset", token=token,
                                                         local_dir=os.path.join(root, "data_zip"))
    missing = wanted - set(found)
    if missing:
        raise FileNotFoundError(f"not in {REPO_ID}: {sorted(missing)}; files there: {files[:30]}")
    return found


def video_source(anno, video_id):
    for source, splits in anno["split"].items():
        for ids in splits.values():
            if video_id in ids:
                return source
    raise KeyError(video_id)


def choose_videos(anno, source="vidor", split="val", n=4, min_frames=50, order="shortest", skip=(), seed=0):
    """n videos of a split with at least min_frames frames, leaving out `skip` (already finished).
    order="shortest": shortest first (cheaper SAM2); order="random": a fixed random order (seed)."""
    import random
    data = {d["video_id"]: d for d in anno["data"]}
    ids = [v for v in anno["split"][source][split] if data[v]["meta"]["num_frames"] >= min_frames]
    ids.sort(key=lambda v: data[v]["meta"]["num_frames"])
    if order == "random":
        random.Random(seed).shuffle(ids)
    return [v for v in ids if v not in set(skip)][:n]


def _members_for(zf, video_id):
    return [m for m in zf.infolist() if video_id in m.filename and not m.is_dir()]


def extract_videos(root, zips, anno, video_ids):
    """Copy the chosen videos' mp4 and mask PNGs out of the zips. Returns {video_id: report}."""
    report = {}
    by_source = {}
    for v in video_ids:
        by_source.setdefault(video_source(anno, v), []).append(v)
    for source, vids in by_source.items():
        prefix = SOURCES[source]
        with zipfile.ZipFile(zips[f"{prefix}_videos.zip"]) as zv, zipfile.ZipFile(zips[f"{prefix}_masks.zip"]) as zm:
            for v in vids:
                vdir = Path(root, source, "videos"); vdir.mkdir(parents=True, exist_ok=True)
                mp4 = [m for m in _members_for(zv, v) if m.filename.endswith(".mp4")]
                if not mp4:
                    raise FileNotFoundError(f"{v}.mp4 not found in {prefix}_videos.zip")
                (vdir / f"{v}.mp4").write_bytes(zv.read(mp4[0]))

                mdir = Path(root, source, "masks", v); mdir.mkdir(parents=True, exist_ok=True)
                members = _members_for(zm, v)
                pngs = [m for m in members if m.filename.endswith(".png")]
                nested = [m for m in members if m.filename.endswith(".zip")]
                if pngs:
                    for m in pngs:
                        (mdir / os.path.basename(m.filename)).write_bytes(zm.read(m))
                elif nested:                     # some releases pack one zip per video
                    with zipfile.ZipFile(io.BytesIO(zm.read(nested[0]))) as inner:
                        for m in inner.infolist():
                            if m.filename.endswith(".png"):
                                (mdir / os.path.basename(m.filename)).write_bytes(inner.read(m))
                else:
                    raise FileNotFoundError(f"no masks for {v} in {prefix}_masks.zip")
                report[v] = {"source": source, "mp4": str(vdir / f"{v}.mp4"),
                             "mask_pngs": len(list(mdir.glob("*.png")))}
    return report


def check_video(root, anno, video_id):
    """Frame counts must agree: mp4 frames, mask PNGs and pvsg.json num_frames."""
    import cv2
    source = video_source(anno, video_id)
    meta = next(d for d in anno["data"] if d["video_id"] == video_id)["meta"]
    cap = cv2.VideoCapture(str(Path(root, source, "videos", f"{video_id}.mp4")))
    n_video, fps = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)), cap.get(cv2.CAP_PROP_FPS)
    cap.release()
    n_masks = len(list(Path(root, source, "masks", video_id).glob("*.png")))
    return {"video_frames": n_video, "video_fps": round(fps, 2), "mask_pngs": n_masks,
            "json_frames": meta["num_frames"], "ok": n_video == n_masks == meta["num_frames"]}


def load_anno(root):
    for p in (Path(root, "pvsg.json"), Path(root, "data_zip", "pvsg.json")):
        if p.exists():
            return json.load(open(p))
    raise FileNotFoundError("pvsg.json")
