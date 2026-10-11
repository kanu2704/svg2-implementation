"""How different are the SAM 2.1 and SAM 3 masks of the same VidOR videos, and does TRASER see a difference?

For every video that has both masks.json (SAM 2.1) and masks_sam3.json (SAM 3), on the frames TRASER reads:
  - mask IoU per object and frame (both made from the same VidOR box);
  - the image patches TRASER picks for each object (its token selection: patches at least half covered by
    the mask), and how many of them are the same: Jaccard = shared / either. Same patches = same input.
Writes results/traser_bench/vidor_sam3/MASKS.md and masks_compare.json (README.md shows the summary).

    python3 tools/mask_compare.py --bench <bench> --work <work> [--videos v1 v2 ...]
"""
import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))
import bench_data as B  # noqa: E402

RESULTS = REPO / "results" / "traser_bench"


def mask_iou(a, b):
    from pycocotools import mask as mu
    ma, mb = mu.decode(a).astype(bool), mu.decode(b).astype(bool)
    union = np.logical_or(ma, mb).sum()
    return None if union == 0 else float(np.logical_and(ma, mb).sum() / union)


def compare_video(bench, work, video_id, stats, select=None):
    """Per-video numbers. stats: TRASER's stats for this video (sampled frames, token grid, columns)."""
    if select is None:
        from run_traser import select_object_tokens as select
    m2 = json.load(open(B.masks_path(bench, "vidor", video_id, work)))
    m3 = json.load(open(B.masks_path(bench, "vidor_sam3", video_id, work)))
    sampled = stats["sampled_idx"]
    cols = sorted(range(len(m2[0])))[:stats.get("max_objects", 40)]
    ious = [mask_iou(m2[f][c], m3[f][c]) for f in sampled if f < len(m2) for c in cols]
    ious = [x for x in ious if x is not None]
    grid = tuple(stats["grid_thw"])
    kept2, idx2 = select(m2, cols, sampled, grid)
    kept3, idx3 = select(m3, cols, sampled, grid)
    s2 = {c: set(i.tolist()) for c, i in zip(kept2, idx2)}
    s3 = {c: set(i.tolist()) for c, i in zip(kept3, idx3)}
    jac = [len(s2[c] & s3[c]) / max(len(s2[c] | s3[c]), 1) for c in s2 if c in s3]
    return {"video": video_id, "objects": len(cols), "mask_pairs": len(ious),
            "mean_iou": round(float(np.mean(ious)), 3) if ious else None,
            "iou_ge_0.9": round(float(np.mean([x >= 0.9 for x in ious])), 3) if ious else None,
            "iou_lt_0.5": round(float(np.mean([x < 0.5 for x in ious])), 3) if ious else None,
            "objects_given_sam2": len(kept2), "objects_given_sam3": len(kept3),
            "given_only_one": sorted(set(kept2) ^ set(kept3)),
            "mean_patch_jaccard": round(float(np.mean(jac)), 3) if jac else None,
            "objects_same_patches": sum(j == 1.0 for j in jac), "objects_compared": len(jac),
            "_ious": ious, "_jac": jac}


def summarize(rows):
    ious = [x for r in rows for x in r["_ious"]]
    jac = [x for r in rows for x in r["_jac"]]
    return {"videos": len(rows), "mask_pairs": len(ious),
            "mean_iou": round(float(np.mean(ious)), 3) if ious else None,
            "median_iou": round(float(np.median(ious)), 3) if ious else None,
            "iou_ge_0.9": round(float(np.mean([x >= 0.9 for x in ious])), 3) if ious else None,
            "iou_lt_0.5": round(float(np.mean([x < 0.5 for x in ious])), 3) if ious else None,
            "objects_compared": len(jac), "mean_patch_jaccard": round(float(np.mean(jac)), 3) if jac else None,
            "objects_same_patches": round(float(np.mean([j == 1.0 for j in jac])), 3) if jac else None,
            "objects_given_differently": sum(len(r["given_only_one"]) for r in rows)}


def write(rows, out=RESULTS / "vidor_sam3"):
    out.mkdir(parents=True, exist_ok=True)
    summary = summarize(rows)
    clean = [{k: v for k, v in r.items() if not k.startswith("_")} for r in rows]
    json.dump({"summary": summary, "videos": clean}, open(out / "masks_compare.json", "w"), indent=1)
    pct = lambda x: "-" if x is None else f"{100 * x:.1f}%"  # noqa: E731
    L = ["# VidOR masks: SAM 2.1 vs SAM 3 (same videos, same VidOR boxes)", "",
         "Both models get the same box of each object on each frame TRASER reads and return one mask. "
         "**Mask IoU** compares the two masks; **patches** compares what TRASER actually reads: for each object, "
         "the image patches (28×28 pixels after resizing) at least half covered by its mask. Same patches = "
         "identical input for that object. Made by `tools/mask_compare.py`.", "",
         f"**{summary['videos']} videos, {summary['mask_pairs']} masks compared:** mean IoU {summary['mean_iou']}, "
         f"median {summary['median_iou']}; IoU ≥ 0.9 for {pct(summary['iou_ge_0.9'])}, < 0.5 for "
         f"{pct(summary['iou_lt_0.5'])}. **Patches:** {summary['objects_compared']} objects, mean overlap "
         f"(Jaccard) {summary['mean_patch_jaccard']}, exactly the same patches for {pct(summary['objects_same_patches'])}; "
         f"objects given to TRASER with one model but not the other: {summary['objects_given_differently']}.", "",
         "| video | objects | masks compared | mean IoU | IoU ≥ 0.9 | IoU < 0.5 | patch overlap | same patches |",
         "|---|---|---|---|---|---|---|---|"]
    for r in clean:
        L.append(f"| {r['video']} | {r['objects']} | {r['mask_pairs']} | {r['mean_iou']} | {pct(r['iou_ge_0.9'])} | "
                 f"{pct(r['iou_lt_0.5'])} | {r['mean_patch_jaccard']} | {r['objects_same_patches']}/{r['objects_compared']} |")
    (out / "MASKS.md").write_text("\n".join(L) + "\n")
    return summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bench", required=True)
    ap.add_argument("--work", default=None)
    ap.add_argument("--videos", nargs="*", default=None, help="default: every video with both mask files")
    ap.add_argument("--results", default=str(RESULTS))
    args = ap.parse_args()
    work = args.work or args.bench
    videos = args.videos or sorted(p.parent.name for p in Path(work, "vidor").glob(f"*/{B.masks_name('vidor_sam3')}"))
    rows = []
    for i, v in enumerate(videos, 1):
        st = Path(args.results, "vidor", "preds", f"{v}.stats.json")
        if not st.exists() or not B.masks_path(args.bench, "vidor_sam3", v, work).exists():
            print(f"{v}: skipped (needs the SAM 2.1 run's stats and both mask files)")
            continue
        t0 = time.time()
        rows.append(compare_video(args.bench, work, v, json.load(open(st))))
        r = rows[-1]
        print(f"{time.strftime('%H:%M:%S')} {i}/{len(videos)} {v}: mean IoU {r['mean_iou']}, patch overlap "
              f"{r['mean_patch_jaccard']} ({time.time() - t0:.0f} s)", flush=True)
    if rows:
        s = write(rows, Path(args.results, "vidor_sam3"))
        print(json.dumps(s, indent=1))


if __name__ == "__main__":
    main()
