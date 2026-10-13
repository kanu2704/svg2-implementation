"""Measurements from the masks TRASER was given, for the error analysis (tools/error_analysis.py).

Only on the frames TRASER reads (its ~1 fps sample, `sampled_idx` in each run's stats), so they describe the
same evidence the model had. Per object: size (share of the frame) and time on screen. Per pair of objects:
time both are on screen, the smallest gap between the two masks (share of the frame diagonal) and time
they touch. Masks are shrunk to at most --max_side pixels for the gaps (a 1080p frame -> 192 px: one pixel
is about 0.5% of the diagonal), sizes come from the full masks.

Runs where the masks are (Kaggle: the prepared items under BENCH, VidOR masks under the work folder); CPU only.
VidOR items whose SAM 2.1 masks are gone (a new Kaggle session) are measured from VidOR's own boxes instead,
which the masks were made from (sizes are then box sizes, gaps are gaps between boxes; "source": "boxes").
Writes one small file per video, results/traser_bench/diagnosis/mask_features/<dataset>/<video_id>.json, and
skips videos already done, so it can be stopped and restarted.

    python3 tools/mask_features.py --bench /kaggle/tmp/traser_bench --datasets pvsg svg2test vidor
"""
import argparse
import json
import math
import sys
import time
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))
import bench_data as B  # noqa: E402

RESULTS = REPO / "results" / "traser_bench"
OUT = RESULTS / "diagnosis" / "mask_features"
TOUCH = 0.01          # gap at or below 1% of the frame diagonal counts as touching


def distance_to(mask):
    """Distance (pixels) from every pixel to the nearest pixel of `mask` (0 on the mask)."""
    try:
        import cv2
        return cv2.distanceTransform((~mask).astype(np.uint8), cv2.DIST_L2, 5)
    except ImportError:
        from scipy.ndimage import distance_transform_edt
        return distance_transform_edt(~mask)


def video_features(masks, cols, gid_of_col, sampled, seconds_per_frame, max_side=192):
    """masks: TRASER's mask file (list over video frames of lists over columns of RLEs).
    cols: the mask columns TRASER was given. Returns {"objects": {...}, "pairs": {...}} keyed by human ids."""
    from pycocotools import mask as mu
    frames = [f for f in sampled if f < len(masks)]
    objects = {c: {"frames": 0, "area_sum": 0.0} for c in cols}
    pairs = {}
    for f in frames:
        row = masks[f]
        visible = []
        for c in cols:
            if c >= len(row):
                continue
            r = row[c]
            h, w = r["size"]
            a = float(mu.area(r)) / float(h * w)
            if a > 0:
                objects[c]["frames"] += 1
                objects[c]["area_sum"] += a
                visible.append(c)
        if len(visible) < 2:
            continue
        h, w = row[visible[0]]["size"]
        step = max(1, math.ceil(max(h, w) / max_side))
        small = {c: mu.decode(row[c])[::step, ::step].astype(bool) for c in visible}
        diag = math.hypot(*next(iter(small.values())).shape)
        dist = {c: distance_to(m) for c, m in small.items() if m.any()}
        for i, a in enumerate(visible):
            for b in visible[i + 1:]:
                p = pairs.setdefault((a, b), {"co_frames": 0, "touch_frames": 0, "gap": None})
                p["co_frames"] += 1
                if a in dist and small[b].any():
                    g = float(dist[a][small[b]].min()) / diag
                    p["gap"] = g if p["gap"] is None else min(p["gap"], g)
                    p["touch_frames"] += g <= TOUCH
    out_obj = {}
    for c, o in objects.items():
        out_obj[str(gid_of_col[c])] = {
            "area": round(o["area_sum"] / o["frames"], 5) if o["frames"] else 0.0,
            "visible_s": round(o["frames"] * seconds_per_frame, 2), "frames": o["frames"]}
    out_pairs = {}
    for (a, b), p in pairs.items():
        ga, gb = sorted((gid_of_col[a], gid_of_col[b]))
        out_pairs[f"{ga},{gb}"] = {"co_s": round(p["co_frames"] * seconds_per_frame, 2),
                                   "touch_s": round(p["touch_frames"] * seconds_per_frame, 2),
                                   "gap": None if p["gap"] is None else round(p["gap"], 4)}
    return {"objects": out_obj, "pairs": out_pairs, "frames_read": len(frames), "source": "masks"}


def box_gap(a, b):
    """Gap between two boxes (x0, y0, x1, y1), 0 when they overlap."""
    dx = max(0.0, max(a[0], b[0]) - min(a[2], b[2]))
    dy = max(0.0, max(a[1], b[1]) - min(a[3], b[3]))
    return math.hypot(dx, dy)


def vidor_box_features(anno, sampled, seconds_per_frame):
    """The same measurements from VidOR's boxes (human ids = VidOR's tids)."""
    w, h = float(anno.get("width") or 1), float(anno.get("height") or 1)
    diag = math.hypot(w, h)
    tids = [o["tid"] for o in anno["subject/objects"]]
    objects = {t: {"frames": 0, "area_sum": 0.0} for t in tids}
    pairs = {}
    frames = [f for f in sampled if f < len(anno["trajectories"])]
    for f in frames:
        boxes = {b["tid"]: (b["bbox"]["xmin"], b["bbox"]["ymin"], b["bbox"]["xmax"], b["bbox"]["ymax"])
                 for b in anno["trajectories"][f] if b["tid"] in objects}
        for t, bx in boxes.items():
            objects[t]["frames"] += 1
            objects[t]["area_sum"] += max(0.0, bx[2] - bx[0]) * max(0.0, bx[3] - bx[1]) / (w * h)
        vis = sorted(boxes)
        for i, a in enumerate(vis):
            for b in vis[i + 1:]:
                p = pairs.setdefault((a, b), {"co_frames": 0, "touch_frames": 0, "gap": None})
                g = box_gap(boxes[a], boxes[b]) / diag
                p["co_frames"] += 1
                p["touch_frames"] += g <= TOUCH
                p["gap"] = g if p["gap"] is None else min(p["gap"], g)
    return {"objects": {str(t): {"area": round(o["area_sum"] / o["frames"], 5) if o["frames"] else 0.0,
                                 "visible_s": round(o["frames"] * seconds_per_frame, 2), "frames": o["frames"]}
                        for t, o in objects.items()},
            "pairs": {f"{a},{b}": {"co_s": round(p["co_frames"] * seconds_per_frame, 2),
                                   "touch_s": round(p["touch_frames"] * seconds_per_frame, 2),
                                   "gap": None if p["gap"] is None else round(p["gap"], 4)}
                      for (a, b), p in pairs.items()},
            "frames_read": len(frames), "source": "boxes"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bench", required=True, help="folder with the prepared items (<dataset>/<video_id>/masks.json)")
    ap.add_argument("--work", default=None, help="writable folder where VidOR masks were made (default: --bench)")
    ap.add_argument("--results", default=str(RESULTS))
    ap.add_argument("--datasets", nargs="+", default=["pvsg", "svg2test", "vidor"])
    ap.add_argument("--videos", nargs="*", default=None, help="only these video ids")
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--max_side", type=int, default=192)
    args = ap.parse_args()
    t0 = time.time()
    for ds in args.datasets:
        preds = Path(args.results, ds, "preds")
        vids = sorted(p.name[:-len(".stats.json")] for p in preds.glob("*.stats.json"))
        if args.videos:
            vids = [v for v in vids if v in set(args.videos)]
        out_dir = Path(args.out, ds)
        out_dir.mkdir(parents=True, exist_ok=True)
        done = missing = 0
        for i, v in enumerate(vids, 1):
            target = out_dir / f"{v}.json"
            if target.exists():
                done += 1
                continue
            mpath = B.masks_path(args.bench, ds, v, args.work)
            anno = B.item_dir(args.bench, B.base_dataset(ds), v) / "vidor_anno.json"
            if not mpath.exists() and not (B.base_dataset(ds) == "vidor" and anno.exists()):
                missing += 1
                continue
            stats = json.load(open(preds / f"{v}.stats.json"))
            spf = stats["duration_s"] / max(1, stats["sampled_frames"])
            if mpath.exists():
                gt = json.load(open(Path(args.results, ds, "gt", f"{v}.json")))
                gid_of_col = {o["col"]: o["gt_id"] for o in gt["objects"]}
                cols = [c for c in stats["mask_columns"] if c in gid_of_col]
                feats = video_features(json.load(open(mpath)), cols, gid_of_col, stats["sampled_idx"], spf, args.max_side)
            else:
                feats = vidor_box_features(json.load(open(anno)), stats["sampled_idx"], spf)
            tmp = target.with_suffix(".part")
            tmp.write_text(json.dumps(feats))
            tmp.replace(target)
            done += 1
            if i % 25 == 0 or i == len(vids):
                print(f"{time.strftime('%H:%M:%S')} {ds}: {i}/{len(vids)} videos ({time.time() - t0:.0f} s)", flush=True)
        print(f"{ds}: {done} of {len(vids)} videos measured"
              + (f", {missing} without masks on this machine (prepare them first)" if missing else ""), flush=True)


if __name__ == "__main__":
    main()
