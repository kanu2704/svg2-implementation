"""Phase 3: follow ONE training sample through TRASER, step by step, with the official code.

Uses their data loader (LazySupervisedDataset._get_item + the collator), their
select_tokens, their rearrange_token and their TRASER forward, exactly as one training
step does (traser_train/train/trainer_insert.py), but without the backward pass. Writes
notes/phase3_trace_<video>.md (what happened at every step, with numbers) and
notes/figs/phase3_selection_<video>.png (which visual tokens each object got).

Steps (plan Phase 3):
  3.1 frame sampling + Qwen preprocessing        3.4 trajectory-aligned arrangement
  3.2 prompt + labels                            3.5 the two resamplers (+ permutation test)
  3.3 mask -> token selection                    3.6 forward pass + loss (+ corrupted answers)

    python tools/trace_one_sample.py --ann data/traser/svg2_pvd.json --index 0
"""
import argparse
import colorsys
import copy
import json
import math
import os
import sys

import numpy as np
import torch

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "third_party/SVG2/traser"))
from transformers import AutoProcessor, AutoTokenizer  # noqa: E402

from traser_train.data.data_qwen import DataCollatorForSupervisedDataset, LazySupervisedDataset  # noqa: E402
from traser_train.train import trainer_insert as TI  # noqa: E402  (training constants)
from traser_train.train.argument import DataArguments  # noqa: E402
from traser_train.train.modeling_traser import TRASER  # noqa: E402
from traser_train.train.token_arrangement import rearrange_token  # noqa: E402
from traser_train.train.token_selection import select_tokens  # noqa: E402

BASE_MODEL = "Qwen/Qwen2.5-VL-3B-Instruct"
WINDOW_S = 4      # --temporal_window_length in train.sh
TRAIN_FPS = 1     # training_fps / base_interval


# ----------------------------------------------------------------------------- helpers
def make_dataset(ann_path, tokenizer):
    """Their dataset class, filled in the way its __init__ would (without the registry)."""
    data_args = DataArguments()
    data_args.max_pixels, data_args.min_pixels = 602112, 50176      # train.sh --max_pixels / --min_pixels
    data_args.processor = AutoProcessor.from_pretrained(BASE_MODEL)
    data_args.processor.video_processor.max_pixels = data_args.max_pixels
    data_args.processor.video_processor.min_pixels = data_args.min_pixels
    ds = LazySupervisedDataset.__new__(LazySupervisedDataset)
    ds.tokenizer, ds.data_args = tokenizer, data_args
    with open(ann_path) as f:
        ds.list_data_dict = json.load(f)
    for e in ds.list_data_dict:
        e.setdefault("data_path", "")
    return ds


def view_tokens(tok, ids, special_runs):
    """Decode ids to text, collapsing runs of the given token ids into '[N x name]'."""
    out, i, ids = [], 0, list(ids)
    while i < len(ids):
        if ids[i] in special_runs:
            j = i
            while j < len(ids) and ids[j] == ids[i]:
                j += 1
            out.append(f"[{j - i} × {special_runs[ids[i]]}]")
            i = j
        else:
            j = i
            while j < len(ids) and ids[j] not in special_runs:
                j += 1
            out.append(tok.decode(ids[i:j], skip_special_tokens=False))
            i = j
    return "".join(out)


def colours(n):
    return [colorsys.hsv_to_rgb(i / max(n, 1), 0.85, 1.0) for i in range(n)]


def arrange_like_trainer(model, tok, batch, device, dtype, coverage=0.5):
    """trainer_insert.TraserTrainer.compute_loss steps (1)-(4), verbatim in logic."""
    input_ids = batch["input_ids"].to(device)
    attention_mask = batch["attention_mask"].to(device)
    labels = batch["labels"].to(device)
    thw = batch["video_grid_thw"].to(device)
    T, H, W = (int(x) for x in thw[0])
    _, per_obj_idx, cover = select_tokens(
        obj_masks=batch["obj_masks"][0].cpu(), grid_thw=[T, H, W], patch_size=TI.PATCH_SIZE,
        spatial_merge_size=TI.SPATIAL_MERGE_SIZE, temporal_patch_size=TI.TEMPORAL_PATCH_SIZE,
        coverage_thresh=coverage, time_reduce="max", device="cpu")
    label_ids = [torch.tensor(x, dtype=torch.long) for x in
                 tok([TI.OBJECT_LABEL_TEMPLATE.format(i=k + 1) for k in range(len(per_obj_idx))],
                     add_special_tokens=False)["input_ids"]]
    gpw = int(WINDOW_S / (TI.TEMPORAL_PATCH_SIZE / TRAIN_FPS))
    windows = [f"<{int(w * WINDOW_S)} - {int(w * WINDOW_S + WINDOW_S)} sec>" for w in range(math.ceil(T / gpw))]
    ts_ids = [torch.tensor(x) for x in tok(windows, add_special_tokens=False)["input_ids"]]
    out = rearrange_token(
        model=model, input_ids=input_ids, attention_mask=attention_mask,
        pixel_values=None, image_grid_thw=None,
        pixel_values_videos=batch["pixel_values_videos"].to(device, dtype), video_grid_thw=thw,
        second_per_grid_ts=None, obj_token_indices_per_sample=[[i.to(device) for i in per_obj_idx]],
        obj_traj_start_id=int(model.config.obj_traj_start_id), obj_traj_end_id=int(model.config.obj_traj_end_id),
        use_resampler=True, use_second_resampler=True, text_token_ids_per_sample=[label_ids],
        timestamp_token_ids_per_batch=[ts_ids], grids_per_temporal_window_per_batch=[gpw], labels=labels)
    return out, per_obj_idx, cover, label_ids, ts_ids, windows, gpw


def forward_loss(model, arranged):
    emb, pid, mask, rope_deltas, cache_pos, _, new_labels = arranged
    with torch.no_grad():
        o = model(inputs_embeds=emb, position_ids=pid, attention_mask=mask, rope_deltas=rope_deltas,
                  cache_position=cache_pos, labels=new_labels, use_cache=False)
    return float(o.loss), int((new_labels != -100).sum())


def corrupt(entry, how):
    e = copy.deepcopy(entry)
    g = json.loads(e["conversations"][1]["value"])
    objs = g["objects"]
    if how == "names_rotated":       # each object gets the next object's name
        keys = [next(k for k in o if k.startswith("object_")) for o in objs]
        names = [o[k] for o, k in zip(objs, keys)]
        for o, k, n in zip(objs, keys, names[1:] + names[:1]):
            o[k] = n
    elif how == "spans_shifted_+4s":  # every relation happens 4 s later
        for r in g.get("relationships", []):
            r[3] = [[s + 4, t + 4] for s, t in r[3]]
    elif how == "subject_object_swapped":
        for r in g.get("relationships", []):
            r[0], r[2] = r[2], r[0]
    e["conversations"][1]["value"] = json.dumps(g, ensure_ascii=False)
    return e


# ----------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ann", default="data/traser/svg2_pvd.json")
    ap.add_argument("--index", type=int, default=0)
    ap.add_argument("--model", default="UWGZQ/TRASER")
    ap.add_argument("--dtype", default="float16", choices=["float16", "bfloat16", "float32"])
    args = ap.parse_args()
    dtype = getattr(torch, args.dtype)
    device = "cuda"

    tok = AutoTokenizer.from_pretrained(args.model, use_fast=False, model_max_length=128000)  # as train_qwen.py
    ds = make_dataset(args.ann, tok)
    entry = ds.list_data_dict[args.index]
    vid = os.path.splitext(os.path.basename(entry["video"]))[0]
    R = [f"# Phase 3 trace: training sample `{vid}`", "",
         "Every number below comes from the official code path of one training step "
         "(data loader → collator → `compute_loss` steps 1–4 → model forward), without the backward pass.", ""]

    # ---- 3.1 frames ------------------------------------------------------------------
    from decord import VideoReader
    vr = VideoReader(entry["video"])
    duration = len(vr) / vr.get_avg_fps()
    _, grid, frame_idx, _ = ds.process_video(entry["video"])
    T, Hp, Wp = (int(x) for x in grid)
    per_grid = (Hp // 2) * (Wp // 2)
    R += ["## 3.1 Frame sampling and preprocessing", "",
          f"- video: {duration:.1f} s, {len(vr)} frames at {vr.get_avg_fps():.2f} fps",
          f"- sampled {len(frame_idx)} frames (`round(duration)`, clamped to 4–128), effective fps "
          f"**{len(frame_idx) / duration:.3f}**; frame indices: {frame_idx[:8]}{' …' if len(frame_idx) > 8 else ''}",
          f"- resized frame: {Hp * 14} × {Wp * 14} px → grid (T, H, W) = ({T}, {Hp}, {Wp}) patches of 14 px",
          f"- one visual token = 2 frames × 28×28 px → {T} temporal grids × {Hp // 2}×{Wp // 2} = "
          f"**{T * per_grid} visual tokens** ({per_grid} per grid)", ""]

    # ---- 3.2 prompt + labels -----------------------------------------------------------
    item = ds._get_item(args.index)
    batch = DataCollatorForSupervisedDataset(tokenizer=tok)([item])
    ids = batch["input_ids"][0].tolist()
    labels = batch["labels"][0]
    vt = tok.convert_tokens_to_ids("<|video_pad|>")
    supervised = labels != -100
    R += ["## 3.2 Prompt and labels (data loader + collator)", "",
          f"- sequence length {len(ids)}; `<|video_pad|>` placeholders: {ids.count(vt)}; "
          f"supervised (label ≠ -100) tokens: **{int(supervised.sum())}** = the JSON answer + `<|im_end|>\\n`",
          f"- objects after dropping ones with no mask on any sampled frame: {item['obj_masks'].shape[0]} "
          f"(annotation had {len(entry['obj_list'])})", "", "Prompt as the model sees it:", "", "```",
          view_tokens(tok, ids[:ids.index(vt) + ids.count(vt) + 8], {vt: "<|video_pad|>"}), "```", "",
          "The answer it is trained to write (decoded labels, first 600 characters):", "", "```",
          tok.decode(labels[supervised].tolist())[:600], "```", ""]

    # ---- model ---------------------------------------------------------------------------
    model = TRASER.from_pretrained(args.model, torch_dtype=dtype).to(device).eval()
    with torch.no_grad():
        arranged, per_obj_idx, cover, label_ids, ts_ids, windows, gpw = arrange_like_trainer(model, tok, batch, device, dtype)
    emb, pid, amask, rope_deltas, cache_pos, new_ids, new_labels = arranged

    # ---- 3.3 token selection ---------------------------------------------------------------
    O = len(per_obj_idx)
    best_cov = cover.reshape(O, -1).max(dim=1).values
    fallback = [k + 1 for k in range(O) if best_cov[k] < 0.5]
    union = torch.unique(torch.cat(per_obj_idx))
    R += ["## 3.3 Mask → visual-token selection (Eq. 1–2, `select_tokens`)", "",
          "Coverage of a token = fraction of its 28×28-px square covered by the mask, max over its 2 frames; "
          "selected if ≥ 0.5.", "",
          "| object | label | tokens selected | temporal grids present (of %d) | best coverage | fallback used? |" % T,
          "|---|---|---|---|---|---|"]
    answer = json.loads(tok.decode(labels[supervised].tolist()).split("<|im_end|>")[0])
    names = [next(v for k, v in o.items() if k.startswith("object")) for o in answer["objects"]]
    for k in range(O):
        grids = torch.unique(per_obj_idx[k] // per_grid).numel()
        R.append(f"| {k + 1} | {names[k] if k < len(names) else '?'} | {per_obj_idx[k].numel()} | {grids} "
                 f"| {best_cov[k]:.2f} | {'yes' if (k + 1) in fallback else 'no'} |")
    R += ["", f"- tokens selected by ≥1 object: {union.numel()} of {T * per_grid}; "
              f"**dropped (belong to no object): {1 - union.numel() / (T * per_grid):.1%}**",
          f"- tokens claimed by more than one object: "
          f"{int((torch.bincount(torch.cat(per_obj_idx), minlength=T * per_grid) > 1).sum())}", ""]

    # figure: selected cells on 4 temporal grids
    import cv2
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    show = np.linspace(0, T - 1, min(4, T)).astype(int)
    frames = vr.get_batch([frame_idx[min(2 * t, len(frame_idx) - 1)] for t in show]).asnumpy()
    cols = colours(O)
    fig, axes = plt.subplots(1, len(show), figsize=(4.5 * len(show), 4))
    for ax, t, fr in zip(np.atleast_1d(axes), show, frames):
        img = cv2.resize(fr, (Wp * 14, Hp * 14)).astype(np.float32) / 255
        for k in range(O):
            cells = per_obj_idx[k][(per_obj_idx[k] // per_grid) == t] % per_grid
            for c in cells.tolist():
                r, q = divmod(c, Wp // 2)
                img[r * 28:(r + 1) * 28, q * 28:(q + 1) * 28] = 0.45 * img[r * 28:(r + 1) * 28, q * 28:(q + 1) * 28] + 0.55 * np.array(cols[k])
        ax.imshow(img)
        ax.set_xticks(np.arange(0, Wp * 14, 28) - 0.5, minor=True)
        ax.set_yticks(np.arange(0, Hp * 14, 28) - 0.5, minor=True)
        ax.grid(which="minor", color="white", linewidth=0.2)
        ax.tick_params(which="both", length=0, labelbottom=False, labelleft=False)
        ax.set_title(f"grid t={t} (≈ {2 * t}–{2 * t + 1} s)", fontsize=9)
    handles = [plt.Rectangle((0, 0), 1, 1, color=cols[k]) for k in range(O)]
    fig.legend(handles, [f"{k + 1}: {names[k] if k < len(names) else '?'}" for k in range(O)],
               loc="lower center", ncol=min(O, 8), fontsize=8)
    fig.suptitle(f"{vid}: visual tokens (28×28-px cells) selected for each object; uncoloured cells are dropped", fontsize=10)
    os.makedirs("notes/figs", exist_ok=True)
    fig_path = f"notes/figs/phase3_selection_{vid}.png"
    fig.savefig(fig_path, dpi=70, bbox_inches="tight")
    R += [f"![token selection](figs/{os.path.basename(fig_path)})", ""]

    # ---- 3.4 arrangement ------------------------------------------------------------------
    nid = new_ids[0].tolist()
    L_new = len(nid)
    s_id, e_id = int(model.config.obj_traj_start_id), int(model.config.obj_traj_end_id)
    text = view_tokens(tok, nid, {vt: "resampled vector"}).replace("<obj_traj_start>", "\n<obj_traj_start>")
    obj_part = text[text.find("<obj_traj_start>"):text.rfind("<obj_traj_end>") + len("<obj_traj_end>")]
    # Length formula (plan 3.4): per object 1 + label + 1 + 32 OTR + Σ_windows (timestamp + 32 TWR) + 1 + 1
    predicted = 0
    for k in range(O):
        wins = torch.unique(per_obj_idx[k] // (per_grid * gpw)).tolist()
        predicted += 1 + len(label_ids[k]) + 1 + 32 + sum(len(ts_ids[w]) + 32 for w in wins) + 1 + 1
    prefix_suffix = len(ids) - ids.count(vt) - 2
    same_rows = bool((pid[0] == pid[1]).all() and (pid[1] == pid[2]).all())
    is_arange = bool((pid[0, 0] == torch.arange(L_new, device=pid.device, dtype=pid.dtype)).all())
    R += ["## 3.4 Trajectory-aligned arrangement (`rearrange_token`)", "",
          f"- sequence: {len(ids)} tokens before → **{L_new} after** ({ids.count(vt)} video placeholders "
          f"replaced by {O} object blocks)",
          f"- length check: prefix+suffix {prefix_suffix} + predicted object blocks {predicted} = "
          f"{prefix_suffix + predicted} {'✓ matches' if prefix_suffix + predicted == L_new else '✗ differs'}",
          f"- position ids: the 3 M-RoPE rows identical? **{same_rows}**; equal to 0…L-1? **{is_arange}** "
          f"→ plain 1D positions, no (time, row, column) for visual tokens (P9)",
          f"- supervised tokens before {int(supervised.sum())} → after {int((new_labels != -100).sum())} "
          f"(arrangement must not touch the answer)",
          f"- window labels: {windows}", "", "The object blocks as the LLM reads them:", "", "```",
          obj_part[:4000] + (" …" if len(obj_part) > 4000 else ""), "```", ""]

    # ---- 3.5 resamplers --------------------------------------------------------------------
    otr, twr = model.second_perceiver_resampler, model.perceiver_resampler
    n_params = lambda m: sum(p.numel() for p in m.parameters())
    with torch.no_grad():
        ve = model.model.get_video_features(batch["pixel_values_videos"].to(device, dtype).type(model.model.visual.dtype),
                                            batch["video_grid_thw"].to(device))
        ve = torch.cat(ve, 0) if isinstance(ve, (list, tuple)) else ve
        big = int(np.argmax([i.numel() for i in per_obj_idx]))
        x = ve[per_obj_idx[big].to(device)].unsqueeze(0)
        m = torch.ones(x.shape[:2], dtype=torch.bool, device=device)
        y = otr(x, attention_mask=m)
        perm = torch.randperm(x.shape[1], device=device)
        y_perm = otr(x[:, perm], attention_mask=m)
        x_rev_time = x.flip(1)   # tokens are stored in time order: reverse time
        y_rev = otr(x_rev_time, attention_mask=m)
    rel = lambda a, b: float((a - b).abs().max() / b.abs().mean())

    def latent_sim(res):
        L = torch.nn.functional.normalize(res.latents.float(), dim=-1)
        s = L @ L.T
        off = s[~torch.eye(len(s), dtype=torch.bool, device=s.device)]
        return float(off.mean()), float(off.min())
    R += ["## 3.5 The two resamplers", "",
          f"- parameters: OTR (`second_perceiver_resampler`) {n_params(otr) / 1e6:.1f} M, "
          f"TWR (`perceiver_resampler`) {n_params(twr) / 1e6:.1f} M, together "
          f"{(n_params(otr) + n_params(twr)) / 1e6:.0f} M on top of {n_params(model) / 1e9 - (n_params(otr) + n_params(twr)) / 1e9:.2f} B",
          f"- latents: {otr.n_latents} (OTR) and {twr.n_latents} (TWR) vectors of size {otr.latents.shape[1]}",
          f"- **permutation test** on object {big + 1} ({x.shape[1]} tokens → {y.shape[1]}×{y.shape[2]}): "
          f"shuffling its tokens changes the OTR output by {rel(y_perm, y):.2e} (relative max abs diff); "
          f"reversing their time order: {rel(y_rev, y):.2e}. "
          f"≈ 0 (fp16 rounding) means the resampler cannot see token order (P8).",
          f"- learned latents, mean / min pairwise cosine similarity: OTR {latent_sim(otr)[0]:.3f} / {latent_sim(otr)[1]:.3f}, "
          f"TWR {latent_sim(twr)[0]:.3f} / {latent_sim(twr)[1]:.3f} (at initialisation all are 1.0: every latent = all ones; P21)", ""]

    # ---- 3.6 loss ----------------------------------------------------------------------------
    base_loss, n_sup = forward_loss(model, arranged)
    R += ["## 3.6 Forward pass and loss", "",
          f"- loss on the true answer: **{base_loss:.3f}** (mean cross-entropy over {n_sup} answer tokens; "
          f"perplexity {math.exp(base_loss):.2f})", "",
          "Corrupted answers (same video, same masks). A higher loss means the model *uses* that information:", "",
          "| answer | loss | Δ vs true |", "|---|---|---|", f"| true | {base_loss:.3f} | – |"]
    for how in ("names_rotated", "spans_shifted_+4s", "subject_object_swapped"):
        ds.list_data_dict[args.index] = corrupt(entry, how)
        b = DataCollatorForSupervisedDataset(tokenizer=tok)([ds._get_item(args.index)])
        with torch.no_grad():
            arr, *_ = arrange_like_trainer(model, tok, b, device, dtype)
        l, _ = forward_loss(model, arr)
        R.append(f"| {how} | {l:.3f} | {l - base_loss:+.3f} |")
        ds.list_data_dict[args.index] = entry
    R += ["", f"Peak GPU memory: {torch.cuda.max_memory_allocated() / 2**30:.1f} GB", ""]

    out = f"notes/phase3_trace_{vid}.md"
    with open(out, "w") as f:
        f.write("\n".join(R) + "\n")
    print("\n".join(R))
    print(f"\nwrote {out} and {fig_path}")


if __name__ == "__main__":
    main()
