# Phase 2: Hugging Face vendored code vs GitHub release

Model repo `UWGZQ/TRASER` vs `third_party/SVG2/traser` (GitHub commit pinned in setup_kaggle.sh).

| HF file | GitHub file | identical? | lines only in HF | lines only in GitHub |
|---|---|---|---|---|
| `modeling_traser.py` | `third_party/SVG2/traser/traser_train/train/modeling_traser.py` | no | 16 | 27 |
| `resampler_utils/token_selection.py` | `third_party/SVG2/traser/traser_train/train/token_selection.py` | no | 21 | 36 |
| `resampler_utils/token_arrangement.py` | `third_party/SVG2/traser/traser_train/train/token_arrangement.py` | no | 187 | 184 |
| `inference.py` | `third_party/SVG2/traser/inference.py` | no | 199 | 257 |

## `modeling_traser.py` vs `third_party/SVG2/traser/traser_train/train/modeling_traser.py`

```diff
--- github:third_party/SVG2/traser/traser_train/train/modeling_traser.py
+++ hf:modeling_traser.py
@@ -1,13 +1,14 @@
+import torch
+import torch.nn as nn
+from typing import List, Tuple, Optional, Any, Dict
 from dataclasses import dataclass
-from typing import Any, List, Optional, Tuple
 
-import torch
+from transformers import Qwen2_5_VLForConditionalGeneration
 from transformers.modeling_outputs import ModelOutput
+from transformers.models.qwen2_5_vl.configuration_qwen2_5_vl import Qwen2_5_VLConfig
+from transformers.models.idefics2.modeling_idefics2 import Idefics2PerceiverResampler
 from transformers.models.idefics2.configuration_idefics2 import Idefics2PerceiverConfig
-from transformers.models.idefics2.modeling_idefics2 import Idefics2PerceiverResampler
-from transformers.models.qwen2_5_vl.configuration_qwen2_5_vl import Qwen2_5_VLConfig
-from transformers.models.qwen2_5_vl.modeling_qwen2_5_vl import Qwen2_5_VLForConditionalGeneration
+from transformers.utils import ModelOutput
 from transformers.processing_utils import Unpack
-
 
 @dataclass
@@ -20,22 +21,12 @@
     rope_deltas: Optional[torch.LongTensor] = None
 
-
 class TRASER(Qwen2_5_VLForConditionalGeneration):
-    """Qwen2.5-VL extended with two Perceiver Resamplers for trajectory-aligned tokens.
-
-    - Temporal-Window Resampler (TWR, `perceiver_resampler`): compresses one object's
-      visual tokens inside each temporal window into a fixed number of latents.
-    - Object-Trajectory Resampler (OTR, `second_perceiver_resampler`): compresses all
-      of one object's visual tokens across the whole video into a global summary.
-    """
-
     def __init__(self, config: Qwen2_5_VLConfig, **kwargs):
         super().__init__(config)
-        # Store resampler hyperparameters passed via from_pretrained(**kwargs) on the
-        # config so that they are serialized with the checkpoint.
+        # Update config with kwargs if provided (fallback mechanism)
         for k, v in kwargs.items():
             if not hasattr(config, k):
                 setattr(config, k, v)
-
+        
         self.config = config
         self._build_perceiver(dtype=config.torch_dtype, attn_impl=config._attn_implementation)
@@ -43,10 +34,10 @@
 
     def _build_perceiver(self, dtype: torch.dtype, attn_impl: str) -> None:
-        hidden_size = int(getattr(self.config, "hidden_size", 2048))
-        n_latents = int(getattr(self.config, "temporal_resampler_n_latents", 32))
+        h = int(getattr(self.config, "hidden_size", 2048))
+        n_latents = int(getattr(self.config, "temporal_resampler_n_latents", 64))
         depth = int(getattr(self.config, "resampler_depth", 3))
 
         perceiver_cfg = Idefics2PerceiverConfig(
-            hidden_size=hidden_size,
+            hidden_size=h,
             resampler_n_latents=n_latents,
             resampler_depth=depth,
@@ -55,10 +46,10 @@
         )
         self.perceiver_resampler = Idefics2PerceiverResampler(perceiver_cfg)
-
+        
         if getattr(self.config, "object_resampler", True):
             second_n_latents = int(getattr(self.config, "object_resampler_n_latents", 32))
 
             second_perceiver_cfg = Idefics2PerceiverConfig(
-                hidden_size=hidden_size,
+                hidden_size=h,
                 resampler_n_latents=second_n_latents,
                 resampler_depth=depth,
@@ -127,7 +118,6 @@
 
         if rope_deltas is not None:
-            self.model.rope_deltas = rope_deltas  # [B, 1]
+            self.model.rope_deltas = rope_deltas 
 
-        # Prefill: the caller provides the rearranged embeddings and position ids directly.
         is_prefill = (inputs_embeds is not None) and (
             past_key_values is None or (hasattr(past_key_values, "get_seq_length") and past_key_values.get_seq_length() == 0)
@@ -148,5 +138,4 @@
             )
         else:
-            # Decode: 1D positions continued from the prefill via rope_deltas.
             inputs_embeds = self.model.get_input_embeddings()(input_ids)
             batch_size, seq_length, _ = inputs_embeds.shape
@@ -179,5 +168,5 @@
         loss = None
         if labels is not None:
-            loss = self.loss_function(logits=logits, labels=labels, vocab_size=logits.size(-1))
+            loss = self.loss_function(logits=logits, labels=labels, vocab_size=self.config.vocab_size)
 
         return TRASEROutput(
```

## `resampler_utils/token_selection.py` vs `third_party/SVG2/traser/traser_train/train/token_selection.py`

```diff
--- github:third_party/SVG2/traser/traser_train/train/token_selection.py
+++ hf:resampler_utils/token_selection.py
@@ -1,34 +1,22 @@
-from typing import Literal, Tuple
-
 import torch
 import torch.nn.functional as F
-
+from typing import Literal, Optional, Tuple
 
 @torch.no_grad()
 def select_tokens(
-    obj_masks: torch.Tensor,                 # (O, N, H_rz, W_rz) or (N, H_rz, W_rz)
-    grid_thw: Tuple[int, int, int],          # (T, H, W) patch grid *after* temporal merging, *before* spatial merging
+    obj_masks: torch.Tensor,                
+    grid_thw: Tuple[int,int,int],           
     *,
     patch_size: int = 14,
-    spatial_merge_size: int = 2,             # m
-    temporal_patch_size: int = 2,            # g
-    coverage_thresh: float = 0.5,
-    time_reduce: Literal["mean", "max", "min"] = "max",  # reduction across the g frames merged into one grid
+    spatial_merge_size: int = 2,             
+    temporal_patch_size: int = 2,         
+    coverage_thresh: float = 0.7,
+    time_reduce: Literal["mean","max","all"] = "max", 
     device: str | torch.device = "cpu",
-    retry_step: float = 0.2,
-    retry_times: int = 2,
-    ensure_at_least_one: bool = True,
+    retry_step: float = 0.1,                 
+    retry_times: int = 1, 
+    ensure_at_least_one: bool = True,        
     dtype: torch.dtype = torch.float32,
 ):
-    """Select the visual tokens covered by each object's segmentation masks.
-
-    Returns:
-        union_idx:      (K,)          selected token indices, union over all objects
-        per_obj_idx:    List[(Ki,)]   selected token indices for each object
-        per_obj_cover:  (O, T, Hm, Wm) coverage map for each object
-
-    Constraints: N == T * g, and H_rz / W_rz must be divisible by (m * patch_size)
-    (guaranteed by the video preprocessing).
-    """
     if obj_masks.dim() == 3:
         obj_masks = obj_masks.unsqueeze(0)
@@ -36,23 +24,22 @@
     T, H, W = grid_thw
     m, g = spatial_merge_size, temporal_patch_size
-    if N != T * g:
+    if N != T*g:
         if N < T * g:
-            pad = T * g - N
-            last = obj_masks[:, -1:, :, :].repeat(1, pad, 1, 1)
+            pad = T*g - N
+            last = obj_masks[:,-1:,:,:].repeat(1, pad, 1, 1)
             obj_masks = torch.cat([obj_masks, last], dim=1)
-            N = T * g
+            N = T * g 
         else:
             obj_masks = obj_masks[:, :T * g, :, :]
-            N = T * g
+            N = T * g 
     Hm, Wm = H // m, W // m
     pix_h, pix_w = m * patch_size, m * patch_size
-    assert H_rz % pix_h == 0 and W_rz % pix_w == 0, "resized height/width must be divisible by spatial_merge_size * patch_size"
+    assert H_rz % pix_h == 0 and W_rz % pix_w == 0, "resized // (28×28)"
 
     M = obj_masks.to(device=device, dtype=dtype).clamp(0, 1)
 
-    # Per-grid coverage: fraction of each (m*patch_size)^2 cell covered by the mask.
-    M_flat = M.view(O * N, 1, H_rz, W_rz)
-    cov_hw = F.avg_pool2d(M_flat, kernel_size=(pix_h, pix_w), stride=(pix_h, pix_w))
-    cov_hw = cov_hw.view(O, N, Hm, Wm)
+    M_flat = M.view(O*N, 1, H_rz, W_rz)
+    cov_hw = F.avg_pool2d(M_flat, kernel_size=(pix_h, pix_w), stride=(pix_h, pix_w))  # (O*N,1,Hm,Wm)
+    cov_hw = cov_hw.view(O, N, Hm, Wm) 
 
     cov_hw = cov_hw.view(O, T, g, Hm, Wm)
@@ -61,13 +48,12 @@
     elif time_reduce == "max":
         cov_thw = cov_hw.max(dim=2).values
-    elif time_reduce == "min":
+    elif time_reduce == "all":
         cov_thw = cov_hw.min(dim=2).values
     else:
-        raise ValueError("time_reduce must be one of {'mean', 'max', 'min'}")
+        raise ValueError("time_reduce ∈ {'mean','max','all'}")
 
     per_obj_idx = []
     per_t = Hm * Wm
     for o in range(O):
-        # Threshold the coverage map; if nothing passes, relax the threshold a few times.
         nz = torch.empty(0, 3, dtype=torch.long, device=device)
         tried = 0
@@ -83,5 +69,4 @@
         if nz.numel() == 0:
             if ensure_at_least_one:
-                # Fall back to the single best-covered token.
                 flat = cov_thw[o].reshape(-1)
                 arg = torch.argmax(flat)
```

## `resampler_utils/token_arrangement.py` vs `third_party/SVG2/traser/traser_train/train/token_arrangement.py`

```diff
--- github:third_party/SVG2/traser/traser_train/train/token_arrangement.py
+++ hf:resampler_utils/token_arrangement.py
@@ -1,19 +1,18 @@
-from typing import List, Optional
-
 import torch
+import torch.nn.functional as F
+from typing import List, Optional, Tuple
+import math
 
 
 def rearrange_token(
     model,
-    input_ids: torch.LongTensor,           # [B, L]
-    attention_mask: torch.LongTensor,      # [B, L]
-    pixel_values: Optional[torch.FloatTensor],         # unused, kept for API compatibility
-    image_grid_thw: Optional[torch.LongTensor],        # unused, kept for API compatibility
-    pixel_values_videos: Optional[torch.FloatTensor],
-    video_grid_thw: Optional[torch.LongTensor],
-    second_per_grid_ts: Optional[torch.Tensor],
-
-    # Per-sample list of objects; each object is a 1D LongTensor of indices into that
-    # sample's video-token stream (relative indices, not absolute sequence positions).
+    input_ids: torch.LongTensor,          
+    attention_mask: torch.LongTensor,      
+    pixel_values: Optional[torch.FloatTensor],            
+    image_grid_thw: Optional[torch.LongTensor],           
+    pixel_values_videos: Optional[torch.FloatTensor],    
+    video_grid_thw: Optional[torch.LongTensor],           
+    second_per_grid_ts: Optional[torch.Tensor],           
+
     obj_token_indices_per_sample: List[List[torch.Tensor]],
 
@@ -21,40 +20,16 @@
     obj_traj_end_id: Optional[int] = None,
 
-    # "Object k: " label token ids: List[sample][object] -> 1D LongTensor
     text_token_ids_per_sample: Optional[List[List[torch.Tensor]]] = None,
 
-    # Timestamp token ids per temporal window: List[sample] -> List[window] -> 1D LongTensor
-    timestamp_token_ids_per_batch=None,
-    # Number of grids per temporal window: List[sample] -> int
-    grids_per_temporal_window_per_batch=None,
+    timestamp_token_ids_per_batch=None,  
+    grids_per_temporal_window_per_batch=None,  
 
     labels: Optional[torch.LongTensor] = None,
     IGNORE_ID: int = -100,
 
-    use_resampler: bool = True,
+    use_resampler: bool = True,             
     use_second_resampler: bool = True,
-    add_timestamp_token: bool = True,
+    add_timestamp_token: bool = True,       
 ):
-    """Rearrange a Qwen2.5-VL input sequence into trajectory-aligned object blocks.
-
-    The original contiguous video-token span is replaced by one block per object:
-
-        <obj_traj_start> Object k: <|vision_start|>
-            [OTR latents]                      (global object summary)
-            <t0 - t1 sec> [TWR latents]        (one group per non-empty temporal window)
-            <t1 - t2 sec> [TWR latents]
-            ...
-        <|vision_end|> <obj_traj_end>
-
-    Returns:
-        new_inputs_embeds:  [B, Lmax, D]   (grad flows to the token embedding, the visual
-                                            encoder, and the resamplers)
-        new_position_ids:   [3, B, Lmax]   (int32, 1D-linear positions replicated over the 3 RoPE dims)
-        new_attention_mask: [B, Lmax]
-        rope_deltas:        [B, 1] (long)
-        cache_position:     [Lmax] (int32)
-        new_input_ids:      [B, Lmax] (long)
-        new_labels:         [B, Lmax] or None (long)
-    """
     dev = input_ids.device
     B, L = input_ids.shape
@@ -62,10 +37,14 @@
 
     assert text_token_ids_per_sample is not None and len(text_token_ids_per_sample) == B, \
-        "rearrange_token requires text_token_ids_per_sample with length B."
-    assert grids_per_temporal_window_per_batch is not None and len(grids_per_temporal_window_per_batch) == B, \
-        "grids_per_temporal_window_per_batch is required."
+        "mode3_traj_and_text requires text_token_ids_per_sample with length B."
+
     if add_timestamp_token:
         assert timestamp_token_ids_per_batch is not None and len(timestamp_token_ids_per_batch) == B, \
             "add_timestamp_token=True requires timestamp_token_ids_per_batch with length B."
+        assert grids_per_temporal_window_per_batch is not None and len(grids_per_temporal_window_per_batch) == B, \
+            "add_timestamp_token=True requires grids_per_temporal_window_per_batch with length B."
+    else:
+        assert grids_per_temporal_window_per_batch is not None and len(grids_per_temporal_window_per_batch) == B, \
+            "grids_per_temporal_window_per_batch is required."
 
     tok_embed = model.get_input_embeddings()
@@ -73,15 +52,15 @@
     vs_id = getattr(model.config, "vision_start_token_id", None)
     ve_id = getattr(model.config, "vision_end_token_id", None)
-    pad_id = 151643  # Qwen2.5-VL <|endoftext|>
-
-    # ---- (0) Temporal window metadata ----
+    pad_id = 151643  
+
+    # ---- (0+) temporal window meta ----
     assert video_grid_thw is not None, "video_grid_thw is required for temporal windowing"
     assert video_grid_thw.shape[0] == B and video_grid_thw.shape[1] == 3, \
         f"video_grid_thw should be ({B},3), got {video_grid_thw.shape}"
 
-    grid_area_batch: List[int] = []  # spatial tokens per temporal grid, after 2x2 spatial merging
+    grid_area_batch: List[int] = []  
     temporal_window_size_batch = grids_per_temporal_window_per_batch
 
-    # ---- (1) Compute visual features (with grad) ----
+    # ---- (0) Compute visual features (with grad) ----
     video_embeds = None
     if pixel_values_videos is not None:
@@ -89,10 +68,8 @@
             pixel_values_videos.type(model.model.visual.dtype), video_grid_thw
         )
-        if hasattr(_vid, "pooler_output"):  # transformers >= 5 wraps the features in a ModelOutput
-            _vid = _vid.pooler_output
-        video_embeds = torch.cat(_vid, dim=0) if isinstance(_vid, (list, tuple)) else _vid  # [N_vid, D]
+        video_embeds = torch.cat(_vid, dim=0) if isinstance(_vid, (list, tuple)) else _vid 
         del pixel_values_videos, _vid
 
-    # ---- (2) Resampler handles ----
+    # ---- (0.1) Resamplers ----
     resampler = None
     resampler_num_latents = None
@@ -110,10 +87,13 @@
             second_resampler_num_latents = int(second_resampler.n_latents)
 
-    # ---- (3) Move to CPU for sequence planning (no autograd graph) ----
+    # ---- (1) Position ids preparation ----
+    position_ids_full = None
+
+    # ---- (2) Move to CPU for sequence planning ----
     attn_cpu = attention_mask.to(cpu, dtype=torch.bool)
     ids_cpu = input_ids.to(cpu)
+    pid_cpu = None
     lbls_cpu = labels.to(cpu) if labels is not None else None
 
-    # Effective lengths and video-token positions in the original sequence.
     eff_lens: List[int] = []
     vid_idx_list: List[torch.Tensor] = []
@@ -134,5 +114,4 @@
             vid_idx_list.append(torch.empty(0, dtype=torch.long))
 
-    # Row offsets of each sample's video tokens inside the concatenated video_embeds.
     vid_counts = [int(v.numel()) for v in vid_idx_list]
     vid_offsets: List[int] = [0] * B
@@ -142,7 +121,6 @@
         running += vid_counts[b]
 
-    # ---- (4) Length planning ----
+    # ---- (3) Length planning ----
     def _object_block_len(b: int, obj_i: int, sel_latent_len: int, rel_temporal_window_idx: torch.Tensor) -> int:
-        """Total sequence length of one object block."""
         add = 0
 
@@ -150,5 +128,6 @@
             add += 1
 
-        add += int(text_token_ids_per_sample[b][obj_i].numel())
+        tlen = int(text_token_ids_per_sample[b][obj_i].numel())
+        add += tlen
 
         if vs_id is not None:
@@ -166,4 +145,5 @@
         add += int(sel_latent_len)
 
+        # VE
         if ve_id is not None:
             add += 1
@@ -188,5 +168,87 @@
             continue
 
-        # Span [v_s, v_e] of the original video segment, including <|vision_start|>/<|vision_end|>.
+        v_s = int(vid_idx[0].item())
+        v_e = int(vid_idx[-1].item())
+
+        has_vs = (vs_id is not None and v_s - 1 >= 0 and ids_b[v_s - 1].item() == vs_id)
+        has_ve = (ve_id is not None and v_e + 1 < L_eff and ids_b[v_e + 1].item() == ve_id)
+        if has_vs:
+            v_s -= 1
+        if has_ve:
+            v_e += 1
+
+        prefix_len = v_s
+        suffix_len = L_eff - (v_e + 1)
+
+        sel_lists = obj_token_indices_per_sample[b]
+        Nv = int(vid_idx.numel())
+
+        cur_total = 0
+        for i, rel in enumerate(sel_lists):
+            rel = rel.to(cpu, dtype=torch.long)
+            sel_len = int(rel.numel())
+
+            tokens_per_window = int(grid_area_batch[b] * int(temporal_window_size_batch[b]))
+            rel_temporal_window_idx = rel // tokens_per_window if (tokens_per_window > 0) else torch.zeros_like(rel)
+            nonempty_windows = int(rel_temporal_window_idx.unique().numel())
+
+            if use_second_resampler and second_resampler_num_latents is not None:
+                sel_len = int(second_resampler_num_latents) + int(resampler_num_latents) * nonempty_windows
+            else:
+                sel_len = int(resampler_num_latents) * nonempty_windows
+
+            cur_total += _object_block_len(b, i, sel_len, rel_temporal_window_idx)
+
+        L_new_each.append(prefix_len + cur_total + suffix_len)
+
+    Lmax = max(L_new_each) if len(L_new_each) > 0 else 0
+
+    # ---- (4) Allocate new sequence tensors on CPU and fill per-sample ----
+    new_input_ids_cpu = torch.full((B, Lmax), pad_id, dtype=torch.long, device=cpu)
+    new_attention_mask_cpu = torch.zeros((B, Lmax), dtype=torch.bool, device=cpu)
+    new_position_ids_cpu = torch.zeros((3, B, Lmax), dtype=torch.int32, device=cpu)
+    new_labels_cpu = None
+    if labels is not None:
+        new_labels_cpu = torch.full((B, Lmax), IGNORE_ID, dtype=torch.long, device=cpu)
+
+    rows_for_video: List[torch.Tensor] = [torch.empty(0, dtype=torch.long) for _ in range(B)]
+
+    batched_obj_rows: List[torch.Tensor] = []  
+    batched_obj_pos: List[torch.Tensor] = []   
+    batched_obj_bids: List[int] = []
+    batched_obj_lens: List[int] = []        
+
+    batched_second_rows: List[torch.Tensor] = []
+    batched_second_pos: List[torch.Tensor] = []
+    batched_second_bids: List[int] = []
+    batched_second_oids: List[int] = []
+
+    def _text_pos_block(start_scalar: int, length: int, dtype=torch.int32) -> torch.Tensor:
+        """Create 1D-linear positions replicated across 3 RoPE dims."""
+        if length <= 0:
+            return torch.empty(3, 0, dtype=dtype, device=cpu)
+        ar = torch.arange(start_scalar, start_scalar + length, device=cpu, dtype=dtype)
+        return torch.stack([ar, ar, ar], dim=0)
+
+    for b in range(B):
+        L_eff = eff_lens[b]
+        if L_eff == 0:
+            continue
+
+        ids_b = ids_cpu[b, :L_eff]
+        msk_b = attn_cpu[b, :L_eff]
+        labs_b = lbls_cpu[b, :L_eff] if lbls_cpu is not None else None
+        vid_idx = vid_idx_list[b]
+
+        dst = 0
+
+        if vid_idx.numel() == 0:
+            new_input_ids_cpu[b, :L_eff] = ids_b
+            new_attention_mask_cpu[b, :L_eff] = msk_b
+            if new_labels_cpu is not None and labs_b is not None:
+                new_labels_cpu[b, :L_eff] = labs_b
+            new_position_ids_cpu[:, b, :L_eff] = _text_pos_block(0, L_eff, dtype=torch.int32)
+            continue
+
         v_s = int(vid_idx[0].item())
         v_e = int(vid_idx[-1].item())
@@ -201,86 +263,4 @@
         suffix_len = L_eff - (v_e + 1)
 
-        sel_lists = obj_token_indices_per_sample[b]
-
-        cur_total = 0
-        for i, rel in enumerate(sel_lists):
-            rel = rel.to(cpu, dtype=torch.long)
-
-            tokens_per_window = int(grid_area_batch[b] * int(temporal_window_size_batch[b]))
-            rel_temporal_window_idx = rel // tokens_per_window if (tokens_per_window > 0) else torch.zeros_like(rel)
-            nonempty_windows = int(rel_temporal_window_idx.unique().numel())
-
-            # Each object contributes a fixed number of latents:
-            # OTR (global summary) + TWR (one group per non-empty temporal window).
-            if use_second_resampler and second_resampler_num_latents is not None:
-                sel_len = int(second_resampler_num_latents) + int(resampler_num_latents) * nonempty_windows
-            else:
-                sel_len = int(resampler_num_latents) * nonempty_windows
-
-            cur_total += _object_block_len(b, i, sel_len, rel_temporal_window_idx)
-
-        L_new_each.append(prefix_len + cur_total + suffix_len)
-
-    Lmax = max(L_new_each) if len(L_new_each) > 0 else 0
-
-    # ---- (5) Allocate new sequence tensors on CPU and fill per sample ----
-    new_input_ids_cpu = torch.full((B, Lmax), pad_id, dtype=torch.long, device=cpu)
-    new_attention_mask_cpu = torch.zeros((B, Lmax), dtype=attn_cpu.dtype, device=cpu)
-    new_position_ids_cpu = torch.zeros((3, B, Lmax), dtype=torch.int32, device=cpu)
-    new_labels_cpu = None
-    if labels is not None:
-        new_labels_cpu = torch.full((B, Lmax), IGNORE_ID, dtype=torch.long, device=cpu)
-
-    # Per-object plan for the batched resampler forwards.
-    batched_obj_rows: List[torch.Tensor] = []   # rows into video_embeds for one (object, window)
-    batched_obj_pos: List[torch.Tensor] = []    # destination positions in the new sequence
-    batched_obj_bids: List[int] = []            # sample index
-    batched_obj_lens: List[int] = []            # number of input rows (before resampling)
-
-    batched_second_rows: List[torch.Tensor] = []
-    batched_second_pos: List[torch.Tensor] = []
-    batched_second_bids: List[int] = []
-
-    def _text_pos_block(start_scalar: int, length: int, dtype=torch.int32) -> torch.Tensor:
-        """1D-linear positions replicated across the 3 RoPE dims: [[i..], [i..], [i..]]."""
-        if length <= 0:
-            return torch.empty(3, 0, dtype=dtype, device=cpu)
-        ar = torch.arange(start_scalar, start_scalar + length, device=cpu, dtype=dtype)
-        return torch.stack([ar, ar, ar], dim=0)
-
-    for b in range(B):
-        L_eff = eff_lens[b]
-        if L_eff == 0:
-            continue
-
-        ids_b = ids_cpu[b, :L_eff]
-        msk_b = attn_cpu[b, :L_eff]
-        labs_b = lbls_cpu[b, :L_eff] if lbls_cpu is not None else None
-        vid_idx = vid_idx_list[b]
-
-        dst = 0  # write cursor into the new_* tensors
-
-        if vid_idx.numel() == 0:
-            # No video segment: copy the sample as-is.
-            new_input_ids_cpu[b, :L_eff] = ids_b
-            new_attention_mask_cpu[b, :L_eff] = msk_b
-            if new_labels_cpu is not None and labs_b is not None:
-                new_labels_cpu[b, :L_eff] = labs_b
-            new_position_ids_cpu[:, b, :L_eff] = _text_pos_block(0, L_eff, dtype=torch.int32)
-            continue
-
-        v_s = int(vid_idx[0].item())
-        v_e = int(vid_idx[-1].item())
-        has_vs = (vs_id is not None and v_s - 1 >= 0 and ids_b[v_s - 1].item() == vs_id)
-        has_ve = (ve_id is not None and v_e + 1 < L_eff and ids_b[v_e + 1].item() == ve_id)
-        if has_vs:
-            v_s -= 1
-        if has_ve:
-            v_e += 1
-
-        prefix_len = v_s
-        suffix_len = L_eff - (v_e + 1)
-
-        # Prefix before the video segment.
         if prefix_len > 0:
             new_input_ids_cpu[b, dst:dst + prefix_len] = ids_b[:prefix_len]
@@ -292,4 +272,8 @@
 
         Nv = int(vid_idx.numel())
+        pos2rank = torch.full((L_eff,), -1, dtype=torch.long, device=cpu)
+        if Nv > 0:
+            pos2rank[vid_idx] = torch.arange(Nv, dtype=torch.long, device=cpu)
+
         vid_offset = int(vid_offsets[b])
 
@@ -300,5 +284,7 @@
                 rel.clamp_(0, Nv - 1)
 
-            # (a) <obj_traj_start>
+            g = vid_idx.index_select(0, rel) if (Nv > 0 and rel.numel() > 0) else torch.empty(0, dtype=torch.long, device=cpu)
+
+            # (1) <obj_traj_start> (optional)
             if obj_traj_start_id is not None:
                 new_input_ids_cpu[b, dst] = int(obj_traj_start_id)
@@ -309,5 +295,5 @@
                 dst += 1
 
-            # (b) "Object k: " label tokens
+            # (2) text tokens (required)
             txt_ids = text_token_ids_per_sample[b][i].to(cpu, dtype=torch.long)
             k = int(txt_ids.numel())
@@ -320,5 +306,5 @@
                 dst += k
 
-            # (c) <|vision_start|>
+            # (3) <VS> (optional)
             if vs_id is not None:
                 new_input_ids_cpu[b, dst] = int(vs_id)
@@ -329,30 +315,44 @@
                 dst += 1
 
-            # (d) resampled visual tokens
-            if rel.numel() > 0:
+            # (4) video tokens
+            if g.numel() > 0:
                 tokens_per_window = int(grid_area_batch[b] * int(temporal_window_size_batch[b]))
                 rel_temporal_window_idx = rel // tokens_per_window if (tokens_per_window > 0) else torch.zeros_like(rel)
+
                 W_eff = int(rel_temporal_window_idx.max().item()) + 1 if rel_temporal_window_idx.numel() > 0 else 0
 
-                # OTR: reserve slots for the global object summary.
+                all_rows_list = []
+                for w in range(W_eff):
+                    m_w = (rel_temporal_window_idx == w)
+                    if not torch.any(m_w):
... (truncated)
```

## `inference.py` vs `third_party/SVG2/traser/inference.py`

```diff
--- github:third_party/SVG2/traser/inference.py
+++ hf:inference.py
@@ -1,269 +1,211 @@
 #!/usr/bin/env python3
-"""Run TRASER on a video + its object mask trajectories and print the scene graph.
-
-The preprocessing mirrors training (``traser_train/data/data_qwen.py``) exactly — the
-same frame sampling, the same video processor limits, the same mask -> token selection,
-and the same trajectory-aligned token arrangement — so inference sees sequences of the
-same shape the model was trained on.
-
-    python traser/inference.py --video clip.mp4 --masks clip_rle.json
-
-Weights come from the Hub (``UWGZQ/TRASER``) unless ``--model`` points at a local
-directory. ``--masks`` is the per-frame, per-object COCO RLE JSON produced by
-``traser/data/prepare_svg2.py`` or by the SVG2 annotation pipeline
-(``pipeline/svg2_pipeline.py``, whose ``stage6_scene_graph.json`` can be converted with
-``--from_scene_graph``). Progress goes to stderr; stdout is the scene graph only.
+# -*- coding: utf-8 -*-
 """
-
+Inference example for Qwen2.5-VL TRASER model.
+Usage:
+    python inference.py \
+        --model_path . \
+        --video_path /path/to/video.mp4 \
+        --mask_path /path/to/mask.json \
+        --structured_json_dir /path/to/struct_dir \
+        --out_dir ./output
+"""
+
+import os
+import json
 import argparse
-import json
+import random
+import torch
+import numpy as np
+from transformers import AutoProcessor, AutoTokenizer
+
+# Import Custom Model
+from modeling_traser import TRASER
+
+# Import Utils
+from qwen_vl_vsg_utils.src.qwen_vl_utils import process_vision_info
+from resampler_utils.token_selection import select_tokens
+from resampler_utils.token_arrangement import rearrange_token
+from pycocotools import mask as maskUtils
 import math
-import os
-import sys
-from pathlib import Path
-
-import numpy as np
-import torch
 import torch.nn.functional as F
-from pycocotools import mask as maskUtils
-from transformers import AutoProcessor, AutoTokenizer
-
-sys.path.insert(0, str(Path(__file__).resolve().parent))
-
-from traser_train.train.modeling_traser import TRASER
-from traser_train.train.token_arrangement import rearrange_token
-from traser_train.train.token_selection import select_tokens
-
-DEFAULT_MODEL = "UWGZQ/TRASER"
-BASE_MODEL = "Qwen/Qwen2.5-VL-3B-Instruct"
-
-# Qwen2.5-VL vision constants (traser_train/train/trainer_insert.py).
-PATCH_SIZE = 14
-SPATIAL_MERGE_SIZE = 2
-TEMPORAL_PATCH_SIZE = 2
-OBJECT_LABEL_TEMPLATE = "Object {i}: "
-
-# Video sampling, identical to DataArguments' defaults used for training.
-BASE_INTERVAL = 1           # seconds between sampled frames
-VIDEO_MIN_FRAMES = 4
-VIDEO_MAX_FRAMES = 128
-VIDEO_MAX_FRAME_PIXELS = 768 * 28 * 28
-VIDEO_MIN_FRAME_PIXELS = 64 * 28 * 28
-
-SYSTEM_MESSAGE = "You are a helpful assistant."
-CHAT_TEMPLATE = (
-    "{% for message in messages %}"
-    "{{'<|im_start|>' + message['role'] + '\n' + message['content'] + '<|im_end|>' + '\n'}}"
-    "{% endfor %}"
-    "{% if add_generation_prompt %}{{ '<|im_start|>assistant\n' }}{% endif %}"
-)
-
-PROMPTS = {
-    "scene_graph": "Output the Video Scene Graph from the video and object trajectories:\n<video>\n",
-    "relationships": "List all objects and their relationships from the video and object trajectories:\n<video>\n",
-    "attributes": "List all objects and their attributes from the video and object trajectories:\n<video>\n",
-    "objects": "List all objects from the video and object trajectories:\n<video>\n",
-}
-
-
-# --------------------------------------------------------------------------- video
-def decode_video(path, video_processor):
-    """Sample ~1 frame/second and preprocess, exactly as the training dataset does."""
-    try:
-        from decord import VideoReader
-        vr = VideoReader(path, num_threads=4)
-        total_frames, avg_fps = len(vr), vr.get_avg_fps()
-        frame_idx = _frame_indices(total_frames, total_frames / avg_fps)
-        video = vr.get_batch(frame_idx).asnumpy()
-    except Exception as exc:  # noqa: BLE001 - fall back like the training loader
-        print(f"[traser] decord failed ({exc}); falling back to torchcodec", file=sys.stderr)
-        from torchcodec.decoders import VideoDecoder
-        decoder = VideoDecoder(path, device="cpu")
-        total_frames = decoder.metadata.num_frames
-        avg_fps = decoder.metadata.average_fps
-        frame_idx = _frame_indices(total_frames, total_frames / avg_fps)
-        video = decoder.get_frames_at(indices=frame_idx.tolist()).data.cpu().numpy()
-
-    video_length = total_frames / avg_fps
-    fps = len(frame_idx) / video_length
-
-    import copy as _copy
-    proc = _copy.deepcopy(video_processor)
-    proc.max_pixels = VIDEO_MAX_FRAME_PIXELS
-    proc.min_pixels = VIDEO_MIN_FRAME_PIXELS
-    proc.size["longest_edge"] = proc.max_pixels
-    proc.size["shortest_edge"] = proc.min_pixels
-    out = proc.preprocess(videos=video, return_tensors="pt")
-    second_per_grid_ts = [video_processor.temporal_patch_size / fps] * len(out["video_grid_thw"])
-    return (out["pixel_values_videos"], out["video_grid_thw"][0],
-            frame_idx.tolist(), second_per_grid_ts)
-
-
-def _frame_indices(total_frames, video_length):
-    target = min(max(round(video_length / BASE_INTERVAL), VIDEO_MIN_FRAMES), VIDEO_MAX_FRAMES)
-    return np.unique(np.linspace(0, total_frames - 1, target, dtype=int))
-
-
-# --------------------------------------------------------------------------- masks
-def build_obj_masks(mask_data, obj_ids, sampled_idx, h_rz, w_rz):
-    """(O, N, h_rz, w_rz) binary masks; also returns the ids whose masks are non-empty."""
-    masks = torch.zeros((len(obj_ids), len(sampled_idx), h_rz, w_rz), dtype=torch.float32)
-    for o_idx, oid in enumerate(obj_ids):
-        for n_idx, f_idx in enumerate(sampled_idx):
-            if not (0 <= f_idx < len(mask_data)):
-                continue
-            frame = mask_data[f_idx]
-            if not frame or not (0 <= oid < len(frame)):
-                continue
-            rle = frame[oid]
-            if not rle:
-                continue
-            # Absent objects are stored as all-zero RLEs; skip them without decoding. Some
-            # released placeholders encode a run shorter than size[0] * size[1], and
-            # pycocotools then leaves the rest of its output buffer uninitialised, so
-            # decoding them returns garbage instead of zeros. area() only reads run lengths.
-            if maskUtils.area({"size": rle["size"], "counts": rle["counts"]}) == 0:
-                continue
-            m = maskUtils.decode({"size": rle["size"], "counts": rle["counts"]})
-            if m.ndim == 3:
-                m = m[:, :, 0]
-            m_t = torch.from_numpy(m.astype(np.uint8))[None, None].float()
-            masks[o_idx, n_idx] = (F.interpolate(m_t, size=(h_rz, w_rz), mode="nearest")[0, 0] > 0.5).float()
-
-    keep = (masks.view(len(obj_ids), -1).sum(dim=1) > 0).nonzero(as_tuple=False).squeeze(1).tolist()
-    if not keep:
-        raise SystemExit("None of the requested objects has a mask on the sampled frames.")
-    return masks[keep], [obj_ids[i] for i in keep]
-
-
-def masks_from_scene_graph(path):
-    """Convert a pipeline ``stage6_scene_graph.json`` into the per-frame RLE mask list."""
-    sg = json.load(open(path))
-    objects = sg["objects"]
-    n_frames = sg["total_frames"]
-    empty = {"size": [sg["height"], sg["width"]], "counts": maskUtils.encode(
-        np.asfortranarray(np.zeros((sg["height"], sg["width"]), dtype=np.uint8)))["counts"].decode()}
-    out = [[dict(empty) for _ in objects] for _ in range(n_frames)]
-    for o_idx, obj in enumerate(objects):
-        # trajectory["masks"] is already dense and self-indexed: position i IS video frame
-        # i, null/falsy where the object is absent. trajectory["frames"] is only the sparse
-        # list of frame indices where masks[i] is non-empty (derived from it in the
-        # pipeline's stage5_structure) -- it must not be zipped against masks.
-        for f_idx, rle in enumerate(obj["trajectory"]["masks"]):
-            if rle and 0 <= f_idx < n_frames:
-                out[f_idx][o_idx] = {"size": rle["size"], "counts": rle["counts"]}
-    return out
-
-
-# --------------------------------------------------------------------------- prompt
-def build_prompt_ids(tokenizer, prompt, n_video_tokens):
-    tok = tokenizer
-    saved = getattr(tok, "chat_template", None)
-    tok.chat_template = CHAT_TEMPLATE
-    try:
-        content = prompt.replace(
-            "<video>", "<|vision_start|>" + "<|video_pad|>" * n_video_tokens + "<|vision_end|>"
+
+def set_seed(seed: int):
+    random.seed(seed)
+    np.random.seed(seed)
+    torch.manual_seed(seed)
+    torch.cuda.manual_seed_all(seed)
+
+
+def load_mask_data(mask_json_path):
+    with open(mask_json_path, "r") as f:
+        return json.load(f)
+
+def has_any_mask(mask_data, obj_id):
+    for frame in mask_data:
+        if not frame or obj_id >= len(frame): continue
+        if frame[obj_id] and frame[obj_id].get("counts"): return True
+    return False
+
+def build_obj_masks_tensor(mask_data, obj_ids, sampled_idx, H_rz, W_rz, device):
+    O, N = len(obj_ids), len(sampled_idx)
+    obj_masks = torch.zeros((O, N, H_rz, W_rz), dtype=torch.float32, device=device)
+    for o_i, oid in enumerate(obj_ids):
+        for n_idx, fidx in enumerate(sampled_idx):
+            if fidx < len(mask_data):
+                frame_objs = mask_data[fidx]
+                if frame_objs and oid < len(frame_objs):
+                    rle = frame_objs[oid]
+                    if rle:
+                        m = maskUtils.decode({"size": rle["size"], "counts": rle["counts"]})
+                        if m.ndim == 3: m = m[:, :, 0]
+                        m_t = torch.from_numpy(m.astype(np.uint8)).unsqueeze(0).unsqueeze(0).float().to(device)
+                        m_rz = F.interpolate(m_t, size=(H_rz, W_rz), mode="nearest")[0, 0]
+                        obj_masks[o_i, n_idx] = (m_rz > 0.5).float()
+    
+    keep_idx = (obj_masks.view(O, -1).sum(dim=1) > 0).nonzero(as_tuple=False).squeeze(1).tolist()
+    if len(keep_idx) < O: obj_masks = obj_masks[keep_idx]
+    return obj_masks, keep_idx
+
+def run_single_video(model, processor, video_path, mask_path, out_dir, device, args):
+    mask_data = load_mask_data(mask_path)
+    all_ids = range(min(len(mask_data[0]),args.max_objects))
+    eligible = [oid for oid in all_ids if has_any_mask(mask_data, oid)]
+    
+    if len(eligible) > args.max_objects:
+        random.shuffle(eligible)
+        selected_obj_ids = sorted(eligible[:args.max_objects])
+    else:
+        selected_obj_ids = sorted(eligible)
+
+    messages = [
+        {"role": "system", "content": "You are a helpful assistant."},
+        {"role": "user", "content": [
+            {"type": "text", "text": "Output the video Scene Graph from the video and object trajectories:\n"},
+            {"type": "video", "video": video_path}
+        ]}
+    ]
+    
+    prompt_text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
+    image_inputs, video_inputs, fps, selected_frame_idx = process_vision_info(messages, return_video_kwargs=True)
+    
+    proc_inputs = processor(
+        text=[prompt_text], images=image_inputs, videos=video_inputs, padding=True, return_tensors="pt", fps=1
+    ).to(device)
+
+    video_grid_thw = proc_inputs["video_grid_thw"]
+    if isinstance(video_grid_thw, list): video_grid_thw = torch.stack([x.to(device) for x in video_grid_thw])
+    else: video_grid_thw = video_grid_thw.to(device)
+    
+    T_grid = int(video_grid_thw[0, 0].item())
+    H_patch, W_patch = int(video_grid_thw[0, 1].item()), int(video_grid_thw[0, 2].item())
+    
+    # Calculate mask resize dimensions
+    patch_size = 14
+    H_rz, W_rz = H_patch * patch_size, W_patch * patch_size
+
+    # Build Masks
+    sampled_idx = selected_frame_idx[0]
+    obj_masks, keep_idx = build_obj_masks_tensor(mask_data, selected_obj_ids, sampled_idx, H_rz, W_rz, device)
+    selected_obj_ids = [selected_obj_ids[i] for i in keep_idx]
+
+    # Select Tokens
+    per_union_idx, per_obj_idx, _ = select_tokens(
+        obj_masks=obj_masks,
+        grid_thw=(T_grid, H_patch, W_patch),
+        patch_size=patch_size,
+        device=device
+    )
+
+    # Prepare Input
+    per_obj_idx_batch = [per_obj_idx]
+    
+    # Prepare text labels
+    text_token_ids_per_sample = []
+    label_template = "Object {i}: "
+    additional_texts = [label_template.format(i=(k + 1)) for k in range(len(per_obj_idx))]
+    enc = processor.tokenizer(additional_texts, add_special_tokens=False)["input_ids"]
+    text_token_ids_per_sample.append([torch.tensor(x, dtype=torch.long) for x in enc])
+
+    # Prepare timestamps
+    sec_per_window = torch.arange(0, T_grid) * 2.0 
+    temporal_window_length = 4.0
+    grids_per_window = int(temporal_window_length / 2.0) 
+    
+    timestamp_token_ids_per_batch = []
+    grids_per_window_batch = []
+    
+    temporal_text_list = []
+    num_windows = math.ceil(len(sec_per_window) / grids_per_window)
+    for w_id in range(num_windows):
+        s, e = w_id * temporal_window_length, (w_id + 1) * temporal_window_length
+        temporal_text_list.append(f"<{int(s)} - {int(e)} sec>")
+    
+    enc_ts = processor.tokenizer(temporal_text_list, add_special_tokens=False)["input_ids"]
+    timestamp_token_ids_per_batch.append([torch.tensor(x) for x in enc_ts])
+    grids_per_window_batch.append(grids_per_window)
+
+    # Rearrange and Generate
+    with torch.no_grad():
+        new_emb, new_pid, new_mask, rope_deltas, cache_pos, _, _ = rearrange_token(
+            model=model,
+            input_ids=proc_inputs["input_ids"],
+            attention_mask=proc_inputs["attention_mask"],
+            pixel_values_videos=proc_inputs["pixel_values_videos"],
+            video_grid_thw=video_grid_thw,
+            image_grid_thw=None, pixel_values=None, second_per_grid_ts=None,
+            obj_token_indices_per_sample=per_obj_idx_batch,
+            obj_traj_start_id=args.obj_traj_start_id,
+            obj_traj_end_id=args.obj_traj_end_id,
+            text_token_ids_per_sample=text_token_ids_per_sample,
+            timestamp_token_ids_per_batch=timestamp_token_ids_per_batch,
+            grids_per_temporal_window_per_batch=grids_per_window_batch,
         )
-        ids = list(tok.apply_chat_template(
-            [{"role": "system", "content": SYSTEM_MESSAGE}], return_dict=False))
-        ids += list(tok.apply_chat_template(
-            [{"role": "user", "content": content}], add_generation_prompt=True, return_dict=False))
-    finally:
-        tok.chat_template = saved
-    return torch.tensor([ids], dtype=torch.long)
-
-
-# --------------------------------------------------------------------------- main
+        
+        gen_out = model.generate(
+            inputs_embeds=new_emb,
+            position_ids=new_pid,
+            attention_mask=new_mask.long(),
+            rope_deltas=rope_deltas,
+            max_new_tokens=8192,
+            do_sample=True,
+            top_p=0.9,
+            temperature=1e-6,
+            repetition_penalty=1.05
+        )
+
+    decoded = processor.tokenizer.decode(gen_out[0], skip_special_tokens=True)
+    print(f"Generated Output:\n{decoded}")
+    
+    if out_dir:
+        with open(os.path.join(out_dir, "output.txt"), "w") as f:
+            f.write(decoded)
+
 def main():
-    ap = argparse.ArgumentParser(description=__doc__,
-                                 formatter_class=argparse.RawDescriptionHelpFormatter)
-    ap.add_argument("--video", required=True, help="Input video file.")
-    ap.add_argument("--masks", required=True,
-                    help="Per-frame, per-object COCO RLE JSON, or a pipeline "
-                         "stage6_scene_graph.json with --from_scene_graph.")
-    ap.add_argument("--from_scene_graph", action="store_true",
-                    help="Read --masks as a pipeline stage-6 scene graph instead of an RLE list.")
-    ap.add_argument("--model", default=DEFAULT_MODEL, help="Hub id or local checkpoint directory.")
-    ap.add_argument("--task", default="scene_graph", choices=sorted(PROMPTS),
-                    help="Which of the four training prompts to use.")
-    ap.add_argument("--objects", type=int, nargs="*", default=None,
-                    help="Object ids (columns of the mask JSON) to describe. Default: all.")
-    ap.add_argument("--max_objects", type=int, default=40,
-                    help="Cap on the number of objects, matching the released training data.")
-    ap.add_argument("--coverage_thresh", type=float, default=0.5)
-    ap.add_argument("--time_reduce", default="max", choices=["mean", "max", "min"])
-    ap.add_argument("--temporal_window_length", type=int, default=4, help="Seconds per window.")
-    ap.add_argument("--max_new_tokens", type=int, default=8192)
-    ap.add_argument("--output", default=None, help="Write the generated scene graph here.")
-    args = ap.parse_args()
-
+    parser = argparse.ArgumentParser()
+    parser.add_argument("--model_path", type=str, required=True, help="Path to model or HF repo")
+    parser.add_argument("--video_path", type=str, required=True)
+    parser.add_argument("--mask_path", type=str, required=True)
+    parser.add_argument("--out_dir", type=str, default="./output")
+    parser.add_argument("--max_objects", type=int, default=40)
+    parser.add_argument("--obj_traj_start_id", type=int, default=151665)
+    parser.add_argument("--obj_traj_end_id", type=int, default=151666)
+    args = parser.parse_args()
+
+    set_seed(42)
     device = "cuda" if torch.cuda.is_available() else "cpu"
-    model = TRASER.from_pretrained(args.model, torch_dtype=torch.bfloat16).to(device).eval()
-    processor = AutoProcessor.from_pretrained(BASE_MODEL)
-    tokenizer = AutoTokenizer.from_pretrained(args.model, use_fast=False)
+    
+    if args.out_dir:
+        os.makedirs(args.out_dir, exist_ok=True)
+    
+    # Load Model (Using the separate class)
+    # Note: If trust_remote_code=True works, you can use AutoModel.
... (truncated)
```

## `config.json`

```json
{
 "architectures": [
  "Qwen2_5_VLForConditionalGeneration_Insert"
 ],
 "attention_dropout": 0.0,
 "bos_token_id": 151643,
 "eos_token_id": 151645,
 "hidden_act": "silu",
 "hidden_size": 2048,
 "image_token_id": 151655,
 "initializer_range": 0.02,
 "intermediate_size": 11008,
 "max_position_embeddings": 128000,
 "max_window_layers": 70,
 "model_type": "qwen2_5_vl",
 "num_attention_heads": 16,
 "num_hidden_layers": 36,
 "num_key_value_heads": 2,
 "obj_traj_end_id": 151666,
 "obj_traj_start_id": 151665,
 "resampler_depth": 3,
 "temporal_resampler_n_latents": 32,
 "rms_norm_eps": 1e-06,
 "rope_theta": 1000000.0,
 "object_resampler_n_latents": 32,
 "sliding_window": 32768,
 "torch_dtype": "bfloat16",
 "transformers_version": "4.54.0",
 "object_resampler": true,
 "use_cache": false,
 "use_resampler": true,
 "use_sliding_window": false,
 "video_token_id": 151656,
 "vision_end_token_id": 151653,
 "vision_start_token_id": 151652,
 "vision_token_id": 151654,
 "vocab_size": 151667,
 "vision_config (keys)": [
  "depth",
  "fullatt_block_indexes",
  "hidden_act",
  "hidden_size",
  "in_channels",
  "in_chans",
  "initializer_range",
  "intermediate_size",
  "model_type",
  "num_heads",
  "out_hidden_size",
  "patch_size",
  "spatial_merge_size",
  "spatial_patch_size",
  "temporal_patch_size",
  "tokens_per_second",
  "torch_dtype",
  "window_size"
 ]
}
```

## `generation_config.json`

```json
{
 "bos_token_id": 151643,
 "do_sample": true,
 "eos_token_id": [
  151645,
  151643
 ],
 "pad_token_id": 151643,
 "repetition_penalty": 1.05,
 "resampler_depth": 3,
 "temporal_resampler_n_latents": 32,
 "object_resampler_n_latents": 32,
 "temperature": 1e-06,
 "transformers_version": "4.54.0",
 "object_resampler": true,
 "use_resampler": true
}
```
