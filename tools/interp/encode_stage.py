"""Interpretability, stage 1 (GPU, the TRASER checkpoint): for every selected video, what TRASER's language model
reads, and the representations before it.

Per video, into --work (big files, kept on the machine):
    <video>.embeds.pt    the language model's input sequence [L, 2048] (exactly what produced the answers)
    <video>.layout.json  where every object / OTR / window / label sits in it (common.parse_layout), the mask
                         columns, the frames read, and geometry from the masks (sizes, motion, gaps, touching)
    <video>.feats.npz    per object: vision tokens after the encoder+merger (mean over the object's tokens),
                         the same per 4-second window, OTR latents (mean of 32), TWR latents per window (mean of 32)

VidOR items whose SAM 2.1 masks are missing get them here (SAM 2.1 from VidOR's boxes, as in the runs).

    CUDA_VISIBLE_DEVICES=0 python3 tools/interp/encode_stage.py --bench /kaggle/tmp/traser_bench \
        --work /kaggle/tmp/interp_work --shard 0 --nshards 2
"""
import argparse
import json
import math
import sys
import time
import traceback
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent))
import bench_data as B  # noqa: E402
import mask_features as MF  # noqa: E402
from interp import common as C  # noqa: E402


def log(msg, tag=""):
    print(f"{time.strftime('%H:%M:%S')} {tag}{msg}", flush=True)


def motion(masks, cols, gid_of_col, sampled, seconds_per_frame):
    """Per object: how fast its box centre moves (share of the frame diagonal per second, frames TRASER reads)
    and how much its size changes (std / mean of the box area)."""
    from pycocotools import mask as mu
    frames = [f for f in sampled if f < len(masks)]
    out = {}
    for c in cols:
        centres, areas = [], []
        for f in frames:
            row = masks[f]
            if c >= len(row) or mu.area(row[c]) == 0:
                centres.append(None)
                continue
            x, y, w, h = mu.toBbox(row[c]).tolist()
            H, W = row[c]["size"]
            centres.append((x + w / 2, y + h / 2, math.hypot(H, W)))
            areas.append(w * h)
        steps = [math.hypot(b[0] - a[0], b[1] - a[1]) / a[2] for a, b in zip(centres, centres[1:]) if a and b]
        out[str(gid_of_col[c])] = {
            "speed": round(float(np.mean(steps)) / seconds_per_frame, 5) if steps else None,
            "size_change": round(float(np.std(areas) / np.mean(areas)), 4) if len(areas) > 1 and np.mean(areas) > 0 else None}
    return out


def features(embeds, layout, capture, n_windows):
    """Mean vectors per object (and per object x window) at the stages before the language model."""
    import torch
    ve, per_obj, tpw = capture["video_embeds"], capture["per_obj_idx"], capture["tokens_per_window"]
    E = embeds[0].float().cpu()
    n, D = len(layout["objects"]), E.shape[-1]
    vis_obj = np.zeros((n, D), np.float32)
    vis_win = np.zeros((n, n_windows, D), np.float32)
    otr = np.zeros((n, D), np.float32)
    twr_win = np.zeros((n, n_windows, D), np.float32)
    win_mask = np.zeros((n, n_windows), bool)
    for i, (o, idx) in enumerate(zip(layout["objects"], per_obj)):
        idx = idx.long()
        vis_obj[i] = ve[idx].mean(0).numpy()
        w_of = idx // tpw
        for w in torch.unique(w_of).tolist():
            if w < n_windows:
                vis_win[i, w] = ve[idx[w_of == w]].mean(0).numpy()
        otr[i] = E[o["otr"][0]:o["otr"][1]].mean(0).numpy()
        for win in o["windows"]:
            if win["w"] < n_windows:
                twr_win[i, win["w"]] = E[win["twr"][0]:win["twr"][1]].mean(0).numpy()
                win_mask[i, win["w"]] = True
    f16 = lambda a: a.astype(np.float16)  # noqa: E731
    return {"vis_obj": f16(vis_obj), "vis_win": f16(vis_win), "otr": f16(otr), "twr_win": f16(twr_win), "win_mask": win_mask}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bench", required=True, help="prepared items (<dataset>/<video>/video.mp4, gt.json, masks)")
    ap.add_argument("--masks_work", default=None, help="where VidOR masks were made (default: --bench)")
    ap.add_argument("--work", required=True, help="where the big per-video files go")
    ap.add_argument("--results", default=str(C.RESULTS))
    ap.add_argument("--datasets", nargs="+", default=C.DATASETS)
    ap.add_argument("--n", type=json.loads, default={}, help='videos per dataset, e.g. \'{"vidor": 50}\' (default: common.DEFAULT_N)')
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--shard", type=int, default=0)
    ap.add_argument("--nshards", type=int, default=1)
    ap.add_argument("--model", default=None, help="TRASER checkpoint folder or Hub id")
    ap.add_argument("--base_model", default=None)
    ap.add_argument("--dtype", default="float16", help="float16 = what produced the answers on the T4s")
    ap.add_argument("--sam2_ckpt", default=None)
    args = ap.parse_args()
    args.masks_work = args.masks_work or args.bench
    tag = f"[encode {args.shard + 1}/{args.nshards}] "

    todo = []
    for ds in args.datasets:
        vids = C.select_videos(ds, args.n.get(ds), args.seed, args.results)
        for v in C.shard(vids, args.shard, args.nshards):
            if not C.work_paths(args.work, ds, v)["feats"].exists():
                todo.append((ds, v))
    log(f"{len(todo)} videos to encode", tag)
    if not todo:
        return 0
    import torch
    from run_traser import encode, load_model
    model = processor = tokenizer = box_to_mask = None
    done = failed = skipped = 0
    t_all = time.time()
    for i, (ds, v) in enumerate(todo, 1):
        p = C.work_paths(args.work, ds, v)
        item = B.item_dir(args.bench, ds, v)
        try:
            if not (item / "gt.json").exists() or not B.item_video(args.bench, B.load_gt(args.bench, ds, v)).exists():
                skipped += 1
                log(f"{ds}/{v}: not prepared on this machine, skipped", tag)
                continue
            mpath = B.masks_path(args.bench, ds, v, args.masks_work)
            if not mpath.exists():
                if ds == "vidor" and (item / "vidor_anno.json").exists():
                    if box_to_mask is None:
                        log("loading SAM 2.1 for the missing VidOR masks ...", tag)
                        box_to_mask = B.BoxToMask(checkpoint=args.sam2_ckpt)
                    B.make_vidor_masks(args.bench, v, box_to_mask, out=args.masks_work)
                    mpath = B.masks_path(args.bench, ds, v, args.masks_work)
                else:
                    skipped += 1
                    log(f"{ds}/{v}: no masks on this machine, skipped", tag)
                    continue
            if model is None:
                log("loading TRASER ...", tag)
                model, processor, tokenizer = load_model(args.model, dtype=args.dtype, base_model=args.base_model)
                cfg = model.config
                ids_cfg = dict(start_id=int(cfg.obj_traj_start_id), end_id=int(cfg.obj_traj_end_id),
                               video_id=int(cfg.video_token_id), vs_id=int(cfg.vision_start_token_id),
                               ve_id=int(cfg.vision_end_token_id), n_otr=int(model.second_perceiver_resampler.n_latents),
                               n_twr=int(model.perceiver_resampler.n_latents))
            t0 = time.time()
            gt = B.load_gt(args.bench, ds, v)
            masks = json.load(open(mpath))
            capture = {}
            emb, _, am, _, stats = encode(model, processor, tokenizer, str(B.item_video(args.bench, gt)), masks,
                                          objects=[o["col"] for o in gt["objects"]], max_objects=40, capture=capture)
            if not stats["linear_positions"] or not bool(am.all()) or not stats["embeds_finite"]:
                raise RuntimeError("input sequence is not plain positions 0..L-1 / has inf or NaN")
            layout = C.parse_layout(capture["input_ids"].tolist(), decode=lambda x: tokenizer.decode(x), **ids_cfg)
            saved = C.read_json(Path(args.results, ds, "preds", f"{v}.stats.json"), {})
            n_windows = len(stats["window_labels"])
            gid_of_col = {o["col"]: o["gt_id"] for o in gt["objects"]}
            cols = stats["mask_columns"]
            spf = stats["duration_s"] / max(1, stats["sampled_frames"])
            geo = MF.video_features(masks, cols, gid_of_col, stats["sampled_idx"], spf)
            layout.update(
                dataset=ds, video=v, mask_columns=cols, gt_ids=[gid_of_col[c] for c in cols], n_windows=n_windows,
                window_labels=stats["window_labels"], duration_s=stats["duration_s"], sampled_frames=stats["sampled_frames"],
                tokens_per_object=stats["tokens_per_object"], seconds_per_frame=spf,
                same_objects_as_answer=saved.get("mask_columns") == cols, answer_vision_dtype=saved.get("vision_dtype"),
                geometry={"objects": geo["objects"], "pairs": geo["pairs"],
                          "motion": motion(masks, cols, gid_of_col, stats["sampled_idx"], spf)},
                encode_s=round(time.time() - t0, 1), gpu=torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu")
            feats = features(emb, layout, capture, n_windows)
            p["embeds"].parent.mkdir(parents=True, exist_ok=True)
            tmp = p["embeds"].with_suffix(".part")
            torch.save(emb[0].detach().to(torch.float16).cpu().contiguous(), tmp)
            tmp.replace(p["embeds"])
            C.write_json(p["layout"], layout)
            tmpf = p["feats"].with_name(p["feats"].name + ".part.npz")
            np.savez_compressed(tmpf, **feats)
            tmpf.replace(p["feats"])
            done += 1
            log(f"{ds}/{v} encoded ({i}/{len(todo)}): {len(layout['objects'])} objects, {layout['L']} tokens, "
                f"{time.time() - t0:.0f} s" + ("" if layout["same_objects_as_answer"] else " (!! objects differ from the saved run)"), tag)
            del emb, capture
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
        except Exception as e:  # noqa: BLE001
            failed += 1
            log(f"{ds}/{v} FAILED: {type(e).__name__}: {str(e)[:300]}\n{traceback.format_exc()[-1200:]}", tag)
    log(f"finished: {done} encoded, {skipped} not prepared here, {failed} failed ({(time.time() - t_all) / 60:.1f} min)", tag)
    return 0


if __name__ == "__main__":
    sys.exit(main())
