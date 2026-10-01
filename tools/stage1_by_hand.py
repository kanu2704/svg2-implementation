"""Learn SVG2 stage 1 ("segment everything") by doing it by hand on ONE frame.

SAM2 is used only as the oracle "point in -> mask out". Everything around it - the point
grid, the quality filters, duplicate removal, small-region cleanup and the 90% filter - is
written out here step by step, with a picture and numbers saved for every step. At the end
the official stage-1 code (svg2_pipeline.AutomaticMaskGenerator with the paper's Table 7
settings, including the zoomed crops) runs on the same frame for comparison.

Paper: §3.1 Phase 1 (p.5), Appendix A.1 + Table 7 (p.20).
Code it mirrors: pipeline/svg2_pipeline.py stage1_generate_masks / select_max_non_overlapping,
and sam2/automatic_mask_generator.py.

    python tools/stage1_by_hand.py                       # sav_000001.mp4, frame 0
    python tools/stage1_by_hand.py --frame 240 --grid 32

Writes notes/stage1/frame<idx>/*.png and notes/stage1/frame<idx>/README.md
"""
import argparse
import colorsys
import os
import sys
import time

import cv2
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import torch

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "third_party/SVG2/pipeline"))
import svg2_pipeline as P  # noqa: E402  (their stage-1 code, imported for the comparison at the end)

# Table 7 values (paper p.20) = pipeline/examples/run_full.yaml
PRED_IOU_THRESH = 0.75
STABILITY_THRESH = 0.85
STABILITY_OFFSET = 1.0
BOX_NMS_THRESH = 0.7
MIN_REGION_AREA = 200
MAX_OVERLAP_RATIO = 0.9


# ----------------------------------------------------------------------------- drawing
def colours(n, seed=0):
    rng = np.random.default_rng(seed)
    hues = (np.arange(n) * 0.618034 + rng.random()) % 1.0
    return [np.array(colorsys.hsv_to_rgb(h, 0.8, 1.0)) for h in hues]


def overlay(frame, masks, alpha=0.55, numbers=True):
    img = frame.astype(np.float32) / 255
    cols = colours(len(masks))
    for m, c in zip(masks, cols):
        img[m] = (1 - alpha) * img[m] + alpha * c
    img = (img * 255).astype(np.uint8)
    if numbers:
        for k, m in enumerate(masks):
            ys, xs = np.nonzero(m)
            if len(xs):
                cv2.putText(img, str(k), (int(xs.mean()), int(ys.mean())), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 0), 2)
                cv2.putText(img, str(k), (int(xs.mean()), int(ys.mean())), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
    return img


def save_panels(path, panels, titles, cols=4, suptitle=None, size=3.0):
    rows = int(np.ceil(len(panels) / cols))
    h, w = panels[0].shape[:2]
    fig, axes = plt.subplots(rows, cols, figsize=(cols * size * w / max(h, w) * 1.4, rows * size * h / max(h, w) * 1.4))
    axes = np.atleast_1d(axes).ravel()
    for ax in axes:
        ax.axis("off")
    for ax, p, t in zip(axes, panels, titles):
        ax.imshow(p)
        ax.set_title(t, fontsize=8)
    if suptitle:
        fig.suptitle(suptitle, fontsize=10)
    fig.tight_layout()
    fig.savefig(path, dpi=80)
    plt.close(fig)


# ----------------------------------------------------------------------------- our own versions of the filters
def mask_box(m):
    ys, xs = np.nonzero(m)
    return (xs.min(), ys.min(), xs.max(), ys.max()) if len(xs) else (0, 0, 0, 0)


def box_iou(a, b):
    ix = max(0, min(a[2], b[2]) - max(a[0], b[0]) + 1)
    iy = max(0, min(a[3], b[3]) - max(a[1], b[1]) + 1)
    inter = ix * iy
    area = lambda r: (r[2] - r[0] + 1) * (r[3] - r[1] + 1)
    return inter / (area(a) + area(b) - inter)


def nms(masks, scores, thresh):
    """Greedy non-maximum suppression on mask bounding boxes: best score first; drop any later
    mask whose box has IoU > thresh with an already-kept box. Returns kept indices + who killed whom."""
    order = np.argsort(-np.asarray(scores))
    boxes = [mask_box(m) for m in masks]
    kept, killed_by = [], {}
    for i in order:
        hit = next((k for k in kept if box_iou(boxes[i], boxes[k]) > thresh), None)
        if hit is None:
            kept.append(i)
        else:
            killed_by[i] = hit
    return kept, killed_by


def remove_small_regions(mask, min_area):
    """Fill holes and delete islands smaller than min_area pixels (as SAM's post-processing does)."""
    changed = False
    for mode in ("holes", "islands"):
        work = (~mask if mode == "holes" else mask).astype(np.uint8)
        n, labels, stats, _ = cv2.connectedComponentsWithStats(work, 8)
        small = [i for i in range(1, n) if stats[i, cv2.CC_STAT_AREA] < min_area]
        if small:
            changed = True
            if mode == "holes":
                mask = mask | np.isin(labels, small)
            else:
                mask = mask & ~np.isin(labels, small)
    return mask, changed


def max_non_overlapping(masks, ratio):
    """The paper's 90% filter (p.20): biggest first; keep a mask only if < ratio of it is
    already covered by the masks kept before it."""
    order = np.argsort([-int(m.sum()) for m in masks])
    union = np.zeros_like(masks[0], dtype=bool)
    kept, covered_frac = [], {}
    for i in order:
        area = int(masks[i].sum())
        frac = int((union & masks[i]).sum()) / area
        covered_frac[i] = frac
        if frac < ratio:
            kept.append(i)
            union |= masks[i]
    return kept, covered_frac, union


# ----------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", default="third_party/SVG2/pipeline/examples/sav_000001.mp4")
    ap.add_argument("--frame", type=int, default=0)
    ap.add_argument("--grid", type=int, default=32, help="points per side of the full-frame grid (paper: 32)")
    ap.add_argument("--model", default=P.DEFAULT_SAM2_MODEL_ID)
    ap.add_argument("--skip_official", action="store_true")
    args = ap.parse_args()
    out = f"notes/stage1/frame{args.frame}"
    os.makedirs(out, exist_ok=True)
    R = [f"# Stage 1 by hand: `{os.path.basename(args.video)}`, frame {args.frame}", ""]
    dev = "cuda" if torch.cuda.is_available() else "cpu"

    # ---- STEP 0: the input -------------------------------------------------------------
    cap = cv2.VideoCapture(args.video)
    n_frames, fps = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)), cap.get(cv2.CAP_PROP_FPS)
    cap.set(cv2.CAP_PROP_POS_FRAMES, args.frame)
    ok, bgr = cap.read()
    if not ok:
        raise SystemExit(f"cannot read frame {args.frame}")
    frame = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    H, W = frame.shape[:2]
    cv2.imwrite(f"{out}/step0_frame.png", bgr)
    R += ["## Step 0: the input", "",
          f"The video has {n_frames} frames at {fps:.0f} fps ({n_frames / fps:.1f} s). The real pipeline runs stage 1 "
          f"on every 20th frame ({len(range(0, n_frames, 20))} frames); here we do one of them. "
          f"The frame is a {W}×{H} RGB image: that is all SAM2 gets, no labels, no boxes.", "",
          "![frame](step0_frame.png)", ""]

    # ---- STEP 1: the point grid ---------------------------------------------------------
    grid = P.make_point_grid(args.grid)                 # their function: normalised (x, y) in [0, 1]
    points = grid * np.array([W, H])                    # SAM2 scales the grid by the image size
    vis = frame.copy()
    for x, y in points:
        cv2.circle(vis, (int(min(x, W - 1)), int(min(y, H - 1))), 2, (255, 0, 0), -1)
    cv2.imwrite(f"{out}/step1_grid.png", cv2.cvtColor(vis, cv2.COLOR_RGB2BGR))
    R += ["## Step 1: put a grid of points on the frame", "",
          f"{args.grid}×{args.grid} = **{len(points)} points**, one every {W / (args.grid - 1):.0f} px across and "
          f"{H / (args.grid - 1):.0f} px down. Each red dot is one *point* = one pixel where we will ask SAM2 "
          f"\"what is here?\". (Their `make_point_grid` uses `linspace(0, 1)`, so the outer points sit exactly on "
          f"the image border; SAM2's own default grid starts half a step inside.)", "", "![grid](step1_grid.png)", ""]

    # ---- load SAM2 as an image predictor -------------------------------------------------
    from sam2.build_sam import build_sam2_hf
    from sam2.sam2_image_predictor import SAM2ImagePredictor
    t0 = time.time()
    predictor = SAM2ImagePredictor(build_sam2_hf(args.model, device=dev))
    with torch.inference_mode():
        predictor.set_image(frame)                      # runs the image encoder ONCE for this frame
    R += [f"SAM2 (`{args.model}`) loaded; the image encoder ran once on the frame ({time.time() - t0:.1f} s). "
          "Every question below reuses that encoding: asking about a point is cheap.", ""]

    # ---- STEP 2: ask about six single points --------------------------------------------
    demo = np.linspace(0, len(points) - 1, 8).astype(int)[1:-1]
    panels, titles = [], []
    for i in demo:
        x, y = points[i]
        with torch.inference_mode():
            m, score, _ = predictor.predict(point_coords=np.array([[x, y]]), point_labels=np.array([1]),
                                            multimask_output=False)
        m = m[0].astype(bool)
        p = overlay(frame, [m], numbers=False)
        cv2.circle(p, (int(min(x, W - 1)), int(min(y, H - 1))), 7, (255, 0, 0), -1)
        cv2.circle(p, (int(min(x, W - 1)), int(min(y, H - 1))), 7, (255, 255, 255), 2)
        panels.append(p)
        titles.append(f"point #{i} at ({x:.0f},{y:.0f})\nmask = {int(m.sum())} px, SAM2's own IoU guess = {score[0]:.2f}")
    save_panels(f"{out}/step2_one_point_one_mask.png", panels, titles, cols=3,
                suptitle="One question each: the red dot is the point, the coloured area is SAM2's answer (the mask)")
    R += ["## Step 2: one point in → one mask out", "",
          "Six of the grid points, asked one at a time. A single pixel (red dot) returns the *whole* object under "
          "it. The number in each title is SAM2's guess of how good its own mask is (\"predicted IoU\").", "",
          "![one point one mask](step2_one_point_one_mask.png)", ""]

    # ---- STEP 3: ask about every grid point ----------------------------------------------
    t0 = time.time()
    all_masks, iou_pred, stability = [], [], []
    with torch.inference_mode():
        for s in range(0, len(points), 64):          # points_per_batch = 64 (Table 7)
            pts = torch.as_tensor(points[s:s + 64], dtype=torch.float32, device=dev)
            in_pts = predictor._transforms.transform_coords(pts, normalize=True, orig_hw=(H, W))
            labels = torch.ones(len(pts), dtype=torch.int, device=dev)
            logits, ious, _ = predictor._predict(in_pts[:, None, :], labels[:, None],
                                                 multimask_output=False, return_logits=True)
            logits = logits[:, 0].float()             # (B, H, W) un-thresholded mask scores
            # stability score: the mask cut at +1 vs at -1, IoU of the two (step 5)
            strict = (logits > STABILITY_OFFSET).sum((1, 2)).float()
            loose = (logits > -STABILITY_OFFSET).sum((1, 2)).float()
            stability += (strict / loose.clamp(min=1)).tolist()
            iou_pred += ious[:, 0].float().tolist()
            all_masks += list((logits > 0).cpu().numpy())
    iou_pred, stability = np.array(iou_pred), np.array(stability)
    areas = np.array([int(m.sum()) for m in all_masks])
    sample = np.random.default_rng(0).choice(len(all_masks), 12, replace=False)
    save_panels(f"{out}/step3_all_answers_sample.png", [overlay(frame, [all_masks[i]], numbers=False) for i in sample],
                [f"point #{i}: {areas[i]} px, IoU guess {iou_pred[i]:.2f}" for i in sample], cols=4,
                suptitle=f"12 random answers out of {len(all_masks)}: note how many are the same object")
    R += ["## Step 3: ask about every point", "",
          f"All {len(points)} points, in batches of 64: **{len(all_masks)} masks** in {time.time() - t0:.1f} s. "
          f"Most are repeats: big regions get hit by dozens of points. Mask sizes: median {int(np.median(areas))} px, "
          f"smallest {areas.min()} px, largest {areas.max()} px (frame = {H * W} px).", "",
          "![sample of answers](step3_all_answers_sample.png)", ""]

    # ---- STEP 4: filter A, SAM2's own confidence (pred_iou_thresh 0.75) ------------------
    keep = np.where(iou_pred > PRED_IOU_THRESH)[0]
    worst = np.argsort(iou_pred)[:8]
    save_panels(f"{out}/step4_rejected_low_confidence.png", [overlay(frame, [all_masks[i]], numbers=False) for i in worst],
                [f"IoU guess {iou_pred[i]:.2f} → removed" for i in worst], cols=4,
                suptitle="The 8 answers SAM2 itself trusted least")
    R += ["## Step 4: drop answers SAM2 itself doubts (`pred_iou_thresh = 0.75`)", "",
          f"{len(all_masks)} → **{len(keep)}** masks ({len(all_masks) - len(keep)} removed with predicted IoU ≤ 0.75). "
          "These are typically points on edges, shadows or textures where \"the object here\" is ambiguous.", "",
          "![low confidence](step4_rejected_low_confidence.png)", ""]

    # ---- STEP 5: filter B, stability (stability_score_thresh 0.85) ----------------------
    stable = keep[stability[keep] >= STABILITY_THRESH]
    unstable = keep[stability[keep] < STABILITY_THRESH]
    show = unstable[np.argsort(stability[unstable])[:8]] if len(unstable) else []
    if len(show):
        save_panels(f"{out}/step5_rejected_unstable.png", [overlay(frame, [all_masks[i]], numbers=False) for i in show],
                    [f"stability {stability[i]:.2f} → removed" for i in show], cols=4,
                    suptitle="Least stable masks: their outline moves a lot when the cut-off changes")
    R += ["## Step 5: drop unstable masks (`stability_score_thresh = 0.85`)", "",
          "SAM2 outputs a score per pixel; the mask is \"score > 0\". Cut it once strictly (> +1) and once loosely "
          "(> −1): a clean object gives almost the same shape both times (IoU near 1), a vague blob does not.", "",
          f"{len(keep)} → **{len(stable)}** masks ({len(unstable)} unstable removed).", ""]
    if len(show):
        R += ["![unstable](step5_rejected_unstable.png)", ""]

    # ---- STEP 6: duplicates, box NMS (box_nms_thresh 0.7) --------------------------------
    cand = [all_masks[i] for i in stable]
    kept_local, killed_by = nms(cand, iou_pred[stable], BOX_NMS_THRESH)
    groups = {}
    for loser, winner in killed_by.items():
        groups.setdefault(winner, []).append(loser)
    big = max(groups, key=lambda k: len(groups[k])) if groups else None
    if big is not None:
        members = [big] + groups[big][:7]
        save_panels(f"{out}/step6_one_duplicate_group.png", [overlay(frame, [cand[i]], numbers=False) for i in members],
                    ["kept (best IoU guess)"] + ["duplicate → removed"] * (len(members) - 1), cols=4,
                    suptitle=f"One group of duplicates: {len(groups[big]) + 1} answers for the same thing, 1 kept")
    nms_masks = [cand[i] for i in kept_local]
    nms_scores = [iou_pred[stable][i] for i in kept_local]
    R += ["## Step 6: remove duplicates (NMS, `box_nms_thresh = 0.7`)", "",
          "Sort by SAM2's confidence; walk down the list; delete a mask if its bounding box overlaps an already kept "
          "box with IoU > 0.7.", "",
          f"{len(cand)} → **{len(nms_masks)}** masks. The biggest duplicate group had "
          f"{len(groups[big]) + 1 if big is not None else 0} copies of one object.", ""]
    if big is not None:
        R += ["![duplicates](step6_one_duplicate_group.png)", ""]

    # ---- STEP 7: clean small islands and holes (min_mask_region_area 200) ----------------
    cleaned, n_changed = [], 0
    for m in nms_masks:
        m2, changed = remove_small_regions(m, MIN_REGION_AREA)
        n_changed += changed
        if m2.sum() > 0:
            cleaned.append(m2)
    R += ["## Step 7: tidy each mask (`min_mask_region_area = 200`)", "",
          f"Fill holes and delete stray specks smaller than 200 px inside each mask: {n_changed} of {len(nms_masks)} "
          f"masks were touched, {len(cleaned)} remain. (SAM2 then re-runs duplicate removal; skipped here.)", ""]

    # ---- STEP 8: the 90% filter (paper p.20) ---------------------------------------------
    kept90, covered, union = max_non_overlapping(cleaned, MAX_OVERLAP_RATIO)
    dropped90 = [i for i in range(len(cleaned)) if i not in kept90]
    final = [cleaned[i] for i in kept90]
    # sanity check against THEIR implementation of the same rule
    theirs = P.select_max_non_overlapping(cleaned, MAX_OVERLAP_RATIO)
    cv2.imwrite(f"{out}/step8_final_ours.png", cv2.cvtColor(overlay(frame, final), cv2.COLOR_RGB2BGR))
    if dropped90:
        save_panels(f"{out}/step8_dropped_by_90pct.png",
                    [overlay(frame, [cleaned[i]], numbers=False) for i in dropped90[:8]],
                    [f"{covered[i]:.0%} already covered → removed" for i in dropped90[:8]], cols=4,
                    suptitle="Masks removed by the 90% rule: mostly parts inside bigger kept masks")
    R += ["## Step 8: the 90% filter (paper p.20)", "",
          "Biggest first; keep a mask only if less than 90% of it is already covered by the masks kept before it.", "",
          f"{len(cleaned)} → **{len(final)} masks** = our stage-1 result for this frame "
          f"(their `select_max_non_overlapping` gives {len(theirs)}: {'✓ same' if len(theirs) == len(final) else '✗ differs'}). "
          f"Together they cover {union.mean():.0%} of the frame.", "",
          "![final](step8_final_ours.png)", ""]
    if dropped90:
        R += ["![dropped by 90%](step8_dropped_by_90pct.png)", ""]
    R += ["Summary of the funnel:", "", "| step | masks |", "|---|---|",
          f"| 3. one answer per point | {len(all_masks)} |", f"| 4. confident (pred IoU > 0.75) | {len(keep)} |",
          f"| 5. stable (≥ 0.85) | {len(stable)} |", f"| 6. after duplicate removal | {len(nms_masks)} |",
          f"| 7. after tidying | {len(cleaned)} |", f"| 8. after the 90% filter | **{len(final)}** |", ""]

    # ---- STEP 9: the official stage 1 on the same frame ----------------------------------
    if not args.skip_official:
        del predictor
        torch.cuda.empty_cache()
        t0 = time.time()
        gen = P.AutomaticMaskGenerator(P.MaskGenConfig(model_id=args.model), dev)   # Table 7, incl. 2 crop layers
        official_raw = gen.generate(frame)
        official = P.select_max_non_overlapping(official_raw, MAX_OVERLAP_RATIO)
        dt = time.time() - t0

        def best_iou(m, pool):
            return max((float((m & q).sum()) / float((m | q).sum()) for q in pool), default=0.0)
        new_from_crops = [m for m in official if best_iou(m, final) < 0.5]
        cv2.imwrite(f"{out}/step9_final_official.png", cv2.cvtColor(overlay(frame, official), cv2.COLOR_RGB2BGR))
        if new_from_crops:
            cv2.imwrite(f"{out}/step9_only_found_with_zoom.png",
                        cv2.cvtColor(overlay(frame, new_from_crops), cv2.COLOR_RGB2BGR))
        a_ours = sorted(int(m.sum()) for m in final)
        a_off = sorted(int(m.sum()) for m in official)
        R += ["## Step 9: the official stage 1 (with zoomed crops) on the same frame", "",
              f"`svg2_pipeline.AutomaticMaskGenerator` with Table 7 settings (32×32 grid on the frame + 16×16 on 4 "
              f"crops + 4×4 on 16 crops, plus one mask-refinement step `use_m2m`), then the 90% filter: "
              f"{len(official_raw)} → **{len(official)} masks** in {dt:.1f} s.", "",
              "| | ours (full frame only) | official (with crops) |", "|---|---|---|",
              f"| masks | {len(final)} | {len(official)} |",
              f"| smallest mask (px) | {a_ours[0] if a_ours else '-'} | {a_off[0] if a_off else '-'} |",
              f"| median mask (px) | {int(np.median(a_ours)) if a_ours else '-'} | {int(np.median(a_off)) if a_off else '-'} |",
              "", f"**{len(new_from_crops)} official masks have no match (IoU ≥ 0.5) in ours**: these are what "
              "zooming in found.", "", "![official](step9_final_official.png)", ""]
        if new_from_crops:
            R += ["![only with zoom](step9_only_found_with_zoom.png)", ""]

    with open(f"{out}/README.md", "w") as f:
        f.write("\n".join(R) + "\n")
    print("\n".join(R))
    print(f"\nwrote {out}/README.md and its images")


if __name__ == "__main__":
    main()
