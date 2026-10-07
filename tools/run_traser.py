"""Phase 2: run the released TRASER checkpoint on a video + its mask trajectories.

This is the official inference (third_party/SVG2/traser/inference.py), step for step,
using its own functions. Two things differ:
  1. --dtype: their script hard-codes bfloat16. T4 GPUs have no native bfloat16, so we
     default to float16 (bfloat16 still selectable on A100/H100-class GPUs).
  2. It records what we need for the plot-hole checks into <output>.stats.json: frame
     sampling and effective fps (P13), raw vs arranged sequence length (P11), tokens
     selected per object (P10), timing, peak GPU memory, whether the output parses as
     JSON, and how many labels contain "(uncertain)" (P26).

    python tools/run_traser.py --video traser/examples/example/2401075277.mp4 \
        --masks traser/examples/example/2401075277_rle.json --output experiments/phase2/2401075277.json

`load_model` + `infer` are also used by tools/bench_run.py to run many videos with one model load.
"""
import argparse
import json
import math
import os
import sys
import time

import torch

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "third_party/SVG2/traser"))
import inference as T  # noqa: E402  (their module: TRASER, select_tokens, rearrange_token, helpers, constants)


def pick_dtype(dtype="auto"):
    """bfloat16 (what the paper used) on GPUs that have it (compute capability >= 8), else float16."""
    if dtype != "auto":
        return dtype
    if torch.cuda.is_available() and torch.cuda.get_device_capability()[0] >= 8:
        return "bfloat16"
    return "float16"


def avoid_math_attention():
    """On GPUs without FlashAttention (T4 = compute capability 7.5), transformers calls SDPA with
    enable_gqa=True, which only the plain "math" kernel supports there: it builds the full
    heads x L x L attention table (3-7 GB for long inputs) and runs out of memory. Repeating the
    key/value heads instead (what transformers does when a mask is given) lets SDPA use its
    memory-efficient kernel. Same result, linear memory."""
    if torch.cuda.is_available() and torch.cuda.get_device_capability()[0] < 8:
        import transformers.integrations.sdpa_attention as sdpa
        sdpa.use_gqa_in_sdpa = lambda *args, **kwargs: False
        return True
    return False


def load_model(model_id=None, dtype="auto", device=None, base_model=None):
    """Model, processor and tokenizer, as in their main (load once, reuse for many videos).
    model_id / base_model may be local folders (offline use)."""
    device = device or ("cuda" if torch.cuda.is_available() else "cpu")
    torch_dtype = getattr(torch, pick_dtype(dtype))
    avoid_math_attention()
    model = T.TRASER.from_pretrained(model_id or T.DEFAULT_MODEL, torch_dtype=torch_dtype).to(device).eval()
    processor = T.AutoProcessor.from_pretrained(base_model or T.BASE_MODEL)
    tokenizer = T.AutoTokenizer.from_pretrained(model_id or T.DEFAULT_MODEL, use_fast=False)
    processor.tokenizer = tokenizer
    return model, processor, tokenizer


def _token_counter(progress, t0, every=25):
    """A stopping criterion that never stops: it only reports how many tokens have been generated."""
    from transformers import StoppingCriteria, StoppingCriteriaList

    class Count(StoppingCriteria):
        n = 0

        def __call__(self, input_ids, scores, **kwargs):
            self.n += 1
            if self.n % every == 0:
                progress("generating answer", tokens=self.n, tokens_per_s=round(self.n / (time.time() - t0), 1))
            return torch.zeros(input_ids.shape[0], dtype=torch.bool, device=input_ids.device)

    return StoppingCriteriaList([Count()])


def select_object_tokens(mask_data, obj_ids, sampled_idx, grid_thw, coverage_thresh=0.5, time_reduce="max",
                         progress=None):
    """Their build_obj_masks + select_tokens, one object at a time. Same result (both work per object:
    an object without any mask on the sampled frames is dropped, the others get their token indices), but
    the float32 mask table (objects x frames x height x width) is never held for all objects at once:
    for 40 objects on a long 1080p video that table and its copies need 15-25 GB of RAM, which killed
    two workers on Kaggle (30 GB). Returns (kept object ids, per-object token indices)."""
    t_grid, h_patch, w_patch = grid_thw
    kept, per_obj_idx = [], []
    for n, oid in enumerate(obj_ids, 1):
        try:
            masks, _ = T.build_obj_masks(mask_data, [oid], sampled_idx, h_patch * T.PATCH_SIZE, w_patch * T.PATCH_SIZE)
        except SystemExit:               # no mask on any sampled frame: dropped, as in build_obj_masks
            continue
        _, idx, _ = T.select_tokens(
            obj_masks=masks, grid_thw=(t_grid, h_patch, w_patch), patch_size=T.PATCH_SIZE,
            spatial_merge_size=T.SPATIAL_MERGE_SIZE, temporal_patch_size=T.TEMPORAL_PATCH_SIZE,
            coverage_thresh=coverage_thresh, time_reduce=time_reduce, device="cpu")
        kept.append(oid)
        per_obj_idx.append(idx[0])
        del masks
        if progress and n % 10 == 0:
            progress("building object masks", done=f"{n}/{len(obj_ids)}")
    if not kept:
        raise SystemExit("None of the requested objects has a mask on the sampled frames.")
    return kept, per_obj_idx


def infer(model, processor, tokenizer, video, mask_data, objects=None, max_objects=40, task="scene_graph",
          coverage_thresh=0.5, time_reduce="max", temporal_window_length=4, max_new_tokens=8192, progress=None):
    """One video: their preprocessing and generation step for step. Returns (text, stats).
    stats["mask_columns"][k - 1] is the mask column the model calls "object k".
    progress(stage, **info), if given, is called at every step and every 25 generated tokens (live status)."""
    progress = progress or (lambda stage, **info: None)
    device = model.device
    dtype = model.dtype
    stats = {"video": video, "task": task, "dtype": str(dtype).replace("torch.", "")}

    # ---- video: ~1 fps, 4..128 frames, Qwen resize ----
    progress("reading video frames")
    pixel_values_videos, video_grid_thw, sampled_idx, _ = T.decode_video(video, processor.video_processor)
    t_grid, h_patch, w_patch = (int(x) for x in video_grid_thw)
    n_video_tokens = t_grid * h_patch * w_patch // T.SPATIAL_MERGE_SIZE ** 2
    from decord import VideoReader
    vr = VideoReader(video)
    duration = len(vr) / vr.get_avg_fps()
    stats.update(duration_s=round(duration, 2), video_frames=len(vr), video_fps=round(vr.get_avg_fps(), 3),
                 sampled_frames=len(sampled_idx), sampled_idx=[int(i) for i in sampled_idx],
                 effective_fps=round(len(sampled_idx) / duration, 3),
                 grid_thw=[t_grid, h_patch, w_patch], raw_video_tokens=n_video_tokens,
                 resized_hw=[h_patch * T.PATCH_SIZE, w_patch * T.PATCH_SIZE])
    del vr
    progress("video read", frames=len(sampled_idx), duration_s=stats["duration_s"], video_fps=stats["video_fps"])

    # ---- masks -> per-object visual tokens ----
    obj_ids = objects if objects is not None else list(range(len(mask_data[0])))
    obj_ids = sorted(obj_ids)[: max_objects]
    stats["objects_requested"] = len(objects) if objects is not None else len(mask_data[0])
    progress("building object masks", objects=len(obj_ids))
    obj_ids, per_obj_idx = select_object_tokens(mask_data, obj_ids, sampled_idx, (t_grid, h_patch, w_patch),
                                                coverage_thresh, time_reduce, progress)
    selected = [int(i.numel()) for i in per_obj_idx]
    union = int(torch.unique(torch.cat(per_obj_idx)).numel()) if per_obj_idx else 0
    stats.update(objects=len(obj_ids), mask_columns=[int(i) for i in obj_ids], tokens_per_object=selected,
                 tokens_selected_union=union, tokens_dropped_fraction=round(1 - union / n_video_tokens, 3))

    # ---- prompt, "Object k: " labels, "<a - b sec>" window labels ----
    input_ids = T.build_prompt_ids(tokenizer, T.PROMPTS[task], n_video_tokens).to(device)
    attention_mask = torch.ones_like(input_ids)
    label_ids = tokenizer([T.OBJECT_LABEL_TEMPLATE.format(i=k + 1) for k in range(len(per_obj_idx))],
                          add_special_tokens=False)["input_ids"]
    seconds_per_grid = T.TEMPORAL_PATCH_SIZE / T.BASE_INTERVAL
    grids_per_window = int(temporal_window_length / seconds_per_grid)
    windows = [f"<{w * temporal_window_length} - {(w + 1) * temporal_window_length} sec>"
               for w in range(math.ceil(t_grid / grids_per_window))]
    window_ids = tokenizer(windows, add_special_tokens=False)["input_ids"]
    stats.update(window_labels=windows, prompt_tokens=int(input_ids.shape[1]))

    if str(device).startswith("cuda"):
        torch.cuda.reset_peak_memory_stats()
    with torch.no_grad():
        progress("encoding video + objects", objects=len(obj_ids), video_tokens=n_video_tokens)
        t1 = time.time()
        embeds, position_ids, mask, rope_deltas, _, _, _ = T.rearrange_token(
            model=model, input_ids=input_ids, attention_mask=attention_mask,
            pixel_values_videos=pixel_values_videos.to(device, dtype=dtype),
            video_grid_thw=video_grid_thw[None].to(device),
            image_grid_thw=None, pixel_values=None,
            second_per_grid_ts=None,
            obj_token_indices_per_sample=[[i.to(device) for i in per_obj_idx]],
            obj_traj_start_id=int(model.config.obj_traj_start_id),
            obj_traj_end_id=int(model.config.obj_traj_end_id),
            text_token_ids_per_sample=[[torch.tensor(x, dtype=torch.long) for x in label_ids]],
            timestamp_token_ids_per_batch=[[torch.tensor(x, dtype=torch.long) for x in window_ids]],
            grids_per_temporal_window_per_batch=[grids_per_window])
        stats.update(arranged_tokens=int(embeds.shape[1]), arrange_s=round(time.time() - t1, 1),
                     embeds_finite=bool(torch.isfinite(embeds).all()))
        progress("generating answer", tokens=0, input_tokens=int(embeds.shape[1]))
        t2 = time.time()
        generated = model.generate(inputs_embeds=embeds, position_ids=position_ids, attention_mask=mask.long(),
                                   rope_deltas=rope_deltas, max_new_tokens=max_new_tokens, do_sample=False,
                                   stopping_criteria=_token_counter(progress, t2))
        stats.update(generate_s=round(time.time() - t2, 1), new_tokens=int(generated.shape[1]))
    if str(device).startswith("cuda"):
        stats["peak_gpu_gb"] = round(torch.cuda.max_memory_allocated() / 2**30, 2)

    text = tokenizer.decode(generated[0], skip_special_tokens=True)
    try:
        graph = json.loads(text)
        stats.update(json_ok=True, out_objects=len(graph.get("objects", [])),
                     out_relationships=len(graph.get("relationships", [])),
                     out_uncertain_labels=sum("uncertain" in json.dumps(o) for o in graph.get("objects", [])))
    except json.JSONDecodeError as e:
        stats.update(json_ok=False, json_error=str(e)[:200])
    return text, stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", required=True)
    ap.add_argument("--masks", required=True)
    ap.add_argument("--from_scene_graph", action="store_true")
    ap.add_argument("--model", default=T.DEFAULT_MODEL)
    ap.add_argument("--task", default="scene_graph", choices=sorted(T.PROMPTS))
    ap.add_argument("--objects", type=int, nargs="*", default=None)
    ap.add_argument("--max_objects", type=int, default=40)
    ap.add_argument("--coverage_thresh", type=float, default=0.5)
    ap.add_argument("--time_reduce", default="max", choices=["mean", "max", "min"])
    ap.add_argument("--temporal_window_length", type=int, default=4)
    ap.add_argument("--max_new_tokens", type=int, default=8192)
    ap.add_argument("--dtype", default="auto", choices=["auto", "float16", "bfloat16", "float32"])
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    t0 = time.time()
    model, processor, tokenizer = load_model(args.model, args.dtype)
    load_s = round(time.time() - t0, 1)
    mask_data = T.masks_from_scene_graph(args.masks) if args.from_scene_graph else json.load(open(args.masks))
    text, stats = infer(model, processor, tokenizer, args.video, mask_data, objects=args.objects,
                        max_objects=args.max_objects, task=args.task, coverage_thresh=args.coverage_thresh,
                        time_reduce=args.time_reduce, temporal_window_length=args.temporal_window_length,
                        max_new_tokens=args.max_new_tokens)
    stats["load_s"] = load_s

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w") as f:
        f.write(text)
    with open(args.output + ".stats.json", "w") as f:
        json.dump(stats, f, indent=1)
    print(text)
    print(json.dumps(stats, indent=1), file=sys.stderr)


if __name__ == "__main__":
    main()
