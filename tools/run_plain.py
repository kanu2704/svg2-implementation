"""TRASER's fine-tuned model used directly, without TRASER's pipeline: the released checkpoint loaded as a standard
Qwen2.5-VL-3B (its vision encoder and fine-tuned language model; the two resamplers are left out), the whole video
as ordinary video tokens (no object-token selection, no resamplers, no trajectory-aligned rearrangement), and the
objects given as text: each object's bounding box in each 4 s window, in TRASER's own label format

    Object 1: <0 - 4 sec> [x1, y1, x2, y2] <4 - 8 sec> [x1, y1, x2, y2] ...

after TRASER's own prompt. The boxes come from exactly the video cells TRASER selects for that object (its masks,
coverage 0.5; one cell = 28 x 28 pixels of the resized frame), so the same objects are given, under the same
numbers. The answer format is unchanged (TRASER's JSON), so it is scored exactly like TRASER's.

Used by tools/bench_run.py --lm traser_plain (load_plain, infer_plain).
"""
import time

import torch

import run_traser as RT
from run_traser import T


def load_plain(model_id=None, dtype="auto", device=None, base_model=None):
    """TRASER's weights in the stock Qwen2_5_VLForConditionalGeneration (the resampler weights are not used)."""
    from transformers import Qwen2_5_VLForConditionalGeneration
    device = device or ("cuda" if torch.cuda.is_available() else "cpu")
    torch_dtype = getattr(torch, RT.pick_dtype(dtype))
    RT.avoid_math_attention()
    model = Qwen2_5_VLForConditionalGeneration.from_pretrained(model_id or T.DEFAULT_MODEL,
                                                               torch_dtype=torch_dtype).to(device).eval()
    if torch_dtype == torch.float16:
        RT.vision_in_float32(model)          # as for TRASER on a T4: the vision encoder overflows in float16
    RT.chunk_vision(model)
    RT.last_logits_only(model)
    processor = T.AutoProcessor.from_pretrained(base_model or T.BASE_MODEL)
    tokenizer = T.AutoTokenizer.from_pretrained(model_id or T.DEFAULT_MODEL, use_fast=False)
    processor.tokenizer = tokenizer
    return model, processor, tokenizer


def window_boxes(token_idx, grid_thw, temporal_window_length=4):
    """One object's selected video cells (indices t * Hm * Wm + row * Wm + col, as select_tokens returns them) ->
    [(window, [x1, y1, x2, y2])] in pixels of the resized frame, one box per window the object is in."""
    t_grid, h_patch, w_patch = grid_thw
    hm, wm = h_patch // T.SPATIAL_MERGE_SIZE, w_patch // T.SPATIAL_MERGE_SIZE
    cell = T.PATCH_SIZE * T.SPATIAL_MERGE_SIZE
    grids_per_window = max(1, int(temporal_window_length / (T.TEMPORAL_PATCH_SIZE / T.BASE_INTERVAL)))
    per_window = {}
    for i in (token_idx.tolist() if hasattr(token_idx, "tolist") else token_idx):
        t, rem = divmod(int(i), hm * wm)
        r, c = divmod(rem, wm)
        w = t // grids_per_window
        b = per_window.setdefault(w, [c, r, c, r])
        b[0], b[1], b[2], b[3] = min(b[0], c), min(b[1], r), max(b[2], c), max(b[3], r)
    return [(w, [b[0] * cell, b[1] * cell, (b[2] + 1) * cell, (b[3] + 1) * cell]) for w, b in sorted(per_window.items())]


def trajectories_text(per_obj_boxes, width, height, temporal_window_length=4):
    """The objects as text, in TRASER's labels ("Object k: ", "<a - b sec>"), a box where the resampler tokens were."""
    lines = [f"Object trajectories: each object's bounding box [x1, y1, x2, y2] in pixels of the {width}x{height} "
             f"video frames, in each {temporal_window_length} s window it is visible in (time in seconds):"]
    for k, boxes in enumerate(per_obj_boxes, 1):
        parts = [f"<{w * temporal_window_length} - {(w + 1) * temporal_window_length} sec> [{b[0]}, {b[1]}, {b[2]}, {b[3]}]"
                 for w, b in boxes]
        lines.append(T.OBJECT_LABEL_TEMPLATE.format(i=k) + " ".join(parts))
    return "\n".join(lines) + "\n"


def infer_plain(model, processor, tokenizer, video, mask_data, objects=None, max_objects=40, task="scene_graph",
                coverage_thresh=0.5, time_reduce="max", temporal_window_length=4, max_new_tokens=8192, progress=None,
                prompt=None):
    """One video, plain: (text, stats) as run_traser.infer returns them; stats["mask_columns"][k - 1] is the mask
    column the model calls "object k"."""
    progress = progress or (lambda stage, **info: None)
    device = model.device
    stats = {"video": video, "task": task, "input": "plain video + boxes as text (no TRASER pipeline)",
             "dtype": str(model.lm_head.weight.dtype).replace("torch.", ""),
             "vision_dtype": str(model.model.visual.dtype).replace("torch.", ""), "max_objects": max_objects}

    progress("reading video frames")
    pixel_values_videos, video_grid_thw, sampled_idx, second_per_grid_ts = T.decode_video(video, processor.video_processor)
    t_grid, h_patch, w_patch = (int(x) for x in video_grid_thw)
    n_video_tokens = t_grid * h_patch * w_patch // T.SPATIAL_MERGE_SIZE ** 2
    from decord import VideoReader
    vr = VideoReader(video)
    duration = len(vr) / vr.get_avg_fps()
    height, width = h_patch * T.PATCH_SIZE, w_patch * T.PATCH_SIZE
    stats.update(duration_s=round(duration, 2), video_frames=len(vr), video_fps=round(vr.get_avg_fps(), 3),
                 sampled_frames=len(sampled_idx), sampled_idx=[int(i) for i in sampled_idx],
                 effective_fps=round(len(sampled_idx) / duration, 3), grid_thw=[t_grid, h_patch, w_patch],
                 raw_video_tokens=n_video_tokens, resized_hw=[height, width])
    del vr
    progress("video read", frames=len(sampled_idx), duration_s=stats["duration_s"], video_fps=stats["video_fps"])

    obj_ids = sorted(objects if objects is not None else range(len(mask_data[0])))[: max_objects]
    stats["objects_requested"] = len(objects) if objects is not None else len(mask_data[0])
    progress("building object boxes", objects=len(obj_ids))
    obj_ids, per_obj_idx = RT.select_object_tokens(mask_data, obj_ids, sampled_idx, (t_grid, h_patch, w_patch),
                                                   coverage_thresh, time_reduce, progress)
    boxes = [window_boxes(idx, (t_grid, h_patch, w_patch), temporal_window_length) for idx in per_obj_idx]
    traj = trajectories_text(boxes, width, height, temporal_window_length)
    text_in = (prompt or T.PROMPTS[task]) + traj
    input_ids = T.build_prompt_ids(tokenizer, text_in, n_video_tokens).to(device)
    stats.update(objects=len(obj_ids), mask_columns=[int(i) for i in obj_ids], boxes_per_object=[len(b) for b in boxes],
                 prompt_tokens=int(input_ids.shape[1]), trajectory_text_tokens=len(tokenizer(traj)["input_ids"]),
                 prompt=text_in.replace("<video>", f"<video: {n_video_tokens} tokens>"))

    if str(device).startswith("cuda"):
        torch.cuda.reset_peak_memory_stats()
    with torch.no_grad():
        progress("generating answer", tokens=0, input_tokens=int(input_ids.shape[1]))
        t2 = time.time()
        out = model.generate(input_ids=input_ids, attention_mask=torch.ones_like(input_ids),
                             pixel_values_videos=pixel_values_videos.to(device, dtype=model.model.visual.dtype),
                             video_grid_thw=torch.as_tensor(video_grid_thw).view(1, 3).to(device),
                             second_per_grid_ts=torch.tensor(second_per_grid_ts, device=device),
                             max_new_tokens=max_new_tokens, do_sample=False,
                             stopping_criteria=RT._token_counter(progress, t2))
        generated = out[:, input_ids.shape[1]:]
        stats.update(generate_s=round(time.time() - t2, 1), new_tokens=int(generated.shape[1]), engine="hf")
    if str(device).startswith("cuda"):
        stats["peak_gpu_gb"] = round(torch.cuda.max_memory_allocated() / 2**30, 2)
    text = tokenizer.decode(generated[0], skip_special_tokens=True)
    stats.update(RT.answer_stats(text))
    return text, stats
