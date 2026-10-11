"""VidOR masks made by SAM 3 instead of SAM 2.1, for the mask-model comparison (result dataset vidor_sam3).

Same as the SAM 2.1 step (tools/bench_data.make_vidor_masks): VidOR's box of each object on each frame TRASER
reads -> one mask, from the box prompt. Only the model differs: facebook/sam3 through transformers' Sam3Tracker
(needs transformers >= 5, so this runs in its own environment, and access to the gated facebook/sam3 on
Hugging Face). Writes <work>/vidor/<video_id>/masks_sam3.json next to the SAM 2.1 masks.json.

    CUDA_VISIBLE_DEVICES=0 /tmp/venv_sam3/bin/python tools/sam3_masks.py --bench <bench> --work <work> \
        --videos v1 v2 ... --gpu_name gpu0
    /tmp/venv_sam3/bin/python tools/sam3_masks.py --bench <bench> --work <work> --videos v1 --check
"""
import argparse
import json
import os
import sys
import time
import traceback
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))
import bench_data as B  # noqa: E402

NAME = "masks_sam3.json"


def check(args, box_to_mask):
    """One frame of the first video: SAM 3's masks for its boxes, next to SAM 2.1's if they exist."""
    import numpy as np
    from decord import VideoReader
    from pycocotools import mask as mu
    v = args.videos[0]
    d = B.item_dir(args.bench, "vidor", v)
    a = json.load(open(d / "vidor_anno.json"))
    sampled, _, _ = B.traser_frames(d / "video.mp4")
    vr = VideoReader(str(d / "video.mp4"))
    h, w = vr[0].shape[:2]
    sx, sy = w / float(a.get("width") or w), h / float(a.get("height") or h)
    f = next(f for f in sampled if f < len(a["trajectories"]) and a["trajectories"][f])
    boxes = a["trajectories"][f]
    xyxy = [[b["bbox"]["xmin"] * sx, b["bbox"]["ymin"] * sy, b["bbox"]["xmax"] * sx, b["bbox"]["ymax"] * sy] for b in boxes]
    t0 = time.time()
    masks = box_to_mask(vr[f].asnumpy(), xyxy)
    print(f"{v} frame {f}: {len(boxes)} boxes -> masks {masks.shape} in {time.time() - t0:.1f} s")
    sam2 = B.item_dir(args.work, "vidor", v) / "masks.json"
    sam2 = json.load(open(sam2)) if sam2.exists() else None
    objects = sorted(a["subject/objects"], key=lambda o: o["tid"])
    col = {o["tid"]: k for k, o in enumerate(objects)}
    for b, box, m in zip(boxes, xyxy, masks):
        x0, y0, x1, y1 = (int(round(c)) for c in box)
        inside = m[max(y0, 0):y1, max(x0, 0):x1].sum() / max(m.sum(), 1)
        line = (f"  object {b['tid']}: box {x1 - x0}x{y1 - y0}, mask {int(m.sum())} pixels "
                f"({m.sum() / max((x1 - x0) * (y1 - y0), 1):.0%} of the box), {inside:.0%} inside the box")
        if sam2 is not None:
            m2 = mu.decode(sam2[f][col[b["tid"]]]).astype(bool)
            line += f", IoU with SAM 2.1: {np.logical_and(m, m2).sum() / max(np.logical_or(m, m2).sum(), 1):.2f}"
        print(line)
    ok = all(m.any() for m in masks)
    print("CHECK OK" if ok else "CHECK FAILED: an empty mask")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bench", required=True)
    ap.add_argument("--work", default=None, help="writable folder for the masks (default: --bench)")
    ap.add_argument("--videos", nargs="+", required=True)
    ap.add_argument("--model", default="facebook/sam3")
    ap.add_argument("--dtype", default="float32")
    ap.add_argument("--runs", default="/kaggle/working/traser_bench_runs")
    ap.add_argument("--gpu_name", default="gpu0")
    ap.add_argument("--name", default="vidor_sam3masks", help="progress file name prefix")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    args.work = args.work or args.bench

    def log(msg):
        print(f"{time.strftime('%H:%M:%S')} [{args.gpu_name}] {msg}", flush=True)

    todo = [v for v in args.videos if not B.item_dir(args.work, "vidor", v).joinpath(NAME).exists()]
    status_path = Path(args.runs, f"{args.name}_{args.gpu_name}.json")
    os.makedirs(args.runs, exist_ok=True)
    status = {"total": len(args.videos), "done": len(args.videos) - len(todo), "failed": [], "current": None,
              "state": "loading SAM 3", "stage_since": time.time(), "video_since": None, "attempt": 1,
              "recent": [], "avg_min": None, "started": time.strftime("%H:%M:%S")}

    def save_status(**kw):
        if "state" in kw and kw["state"] != status.get("state"):
            kw.setdefault("stage_since", time.time())
        status.update(kw, updated=time.strftime("%H:%M:%S"))
        tmp = status_path.with_suffix(".tmp")
        tmp.write_text(json.dumps(status, indent=1))
        tmp.replace(status_path)

    if not args.check:
        save_status()
        log(f"SAM 3 masks: {len(todo)} videos to do, {status['done']} done before")
        if not todo:
            save_status(state="finished")
            return 0
    t0 = time.time()
    box_to_mask = B.Sam3BoxToMask(args.model, dtype=args.dtype)
    log(f"SAM 3 loaded in {time.time() - t0:.0f} s ({args.dtype})")
    if args.check:
        return check(args, box_to_mask)
    for i, v in enumerate(todo, 1):
        save_status(current=f"vidor/{v}", video_since=time.time(), state="SAM 3 masks")
        t1 = time.time()
        try:
            B.make_vidor_masks(args.bench, v, box_to_mask, out=args.work, name=NAME)
            mins = round((time.time() - t1) / 60, 2)
            status["done"] += 1
            status["recent"] = (status["recent"] + [{"video": f"vidor/{v}", "min": mins, "tokens": None,
                                                     "objects": None}])[-5:]
            status["avg_min"] = round(sum(r["min"] for r in status["recent"]) / len(status["recent"]), 2)
            log(f"vidor/{v} masks done in {time.time() - t1:.0f} s ({i}/{len(todo)})")
        except Exception as e:  # noqa: BLE001
            status["failed"].append(f"vidor/{v}")
            log(f"vidor/{v} FAILED: {type(e).__name__}: {str(e)[:300]}\n{traceback.format_exc()[-800:]}")
    save_status(current=None, state="finished")
    log(f"finished: {status['done']} of {status['total']} done, failed: {status['failed'] or 'none'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
