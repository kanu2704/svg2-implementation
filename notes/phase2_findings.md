# Phase 2: running the released TRASER checkpoint

Run: `tools/run_traser.py` (official inference, fp16 instead of bf16) on the example video
`2401075277` shipped with the model, Kaggle 1× Tesla T4. Output:
`experiments/phase2/2401075277.json`, stats: `experiments/phase2/2401075277.json.stats.json`.

## It works on a T4 in fp16

| | value |
|---|---|
| model load | 63 s (8.2 GB of weights) |
| generation | 58 s for 864 new tokens |
| peak GPU memory | 9.1 GB |
| embeddings finite (no fp16 overflow) | yes |
| output | valid JSON: 9 objects, 18 relations |

## Against the authors' reference output (A100, bf16)

| | ours (T4, fp16) vs reference |
|---|---|
| object labels | identical, all 9 |
| attribute lists | 6 of 9 identical |
| relations | 18 vs 22; 15 identical |

The model is the same and decoding is greedy, so the difference is numeric (fp16 vs bf16,
T4 vs A100). Once one token differs, greedy decoding follows a different path: the
reference has `child approaches chair/table [22, 26]` and `moves away from … [27, 37]`;
ours has `approaches dog [22, 24]`, `moves away from dog [25, 37]` and drops four relations.
The README says another GPU "may change a few tokens"; here **7 of 22 relations changed**.
**Open question:** does that variance matter at the scale of the paper's metrics? Next run:
`--dtype bfloat16` on the same T4 isolates dtype from hardware.

## What the input looked like (stats)

| | value | plot hole |
|---|---|---|
| video | 38.1 s → 38 frames, effective fps 0.997 | P13 not triggered (< 128 s) |
| raw video tokens (what Qwen2.5-VL would read) | 7,429 (grid 19 × 34 × 46 patches) | |
| arranged tokens (what TRASER's LLM reads) | 2,641, i.e. 2.8× fewer | P11 |
| video tokens covered by **no** object, dropped | **53%** | P10, P32 |
| tokens per object | 1,512 / 1,071 / 482 / 280 / 86 / 79 / 74 / 47 / 23 | |
| labels with "(uncertain)" in the output | 2 of 9 | P26 |

Every object gets 32 OTR latents plus 32 TWR latents per window it appears in, whatever
its size: the 1,512 tokens of the largest object are squeezed into 32, while the
23 tokens of the smallest are *expanded* to 32 + 32 per window. The "compression" is
strong for large objects and an expansion for small ones.

## The code shipped with the checkpoint is not the GitHub code (`notes/phase2_hf_vs_github.md`)

- **`modeling_traser.py`**: functionally the same as GitHub (refactor, comments). The
  default `temporal_resampler_n_latents` is 64 in the HF file vs 32 on GitHub, but
  `config.json` sets 32, so no effect.
- **`token_selection.py`**: defaults differ: `coverage_thresh` **0.7** (GitHub and the
  paper's τ_eff: 0.5), fallback `retry_step 0.1 × 1` (GitHub: 0.2 × 2).
- **`token_arrangement.py`**: restructured, same block layout and 1D positions.
- **`inference.py` (standalone, on the Hub)**:
  - calls `select_tokens` **without** a threshold, so it runs at **τ = 0.7**;
  - samples frames through a vendored, modified `qwen_vl_utils.process_vision_info(fps=1)`,
    not the training data loader's `linspace(round(duration))` sampling;
  - hard-codes `temporal_window_length = 4.0`.

  So the two official inference paths feed the model differently, and the Hub path does
  not match training (τ = 0.5). It is not documented which path produced the paper's
  numbers.
- **`generation_config.json`**: `do_sample: true, temperature: 1e-6` (≈ greedy) and
  **`repetition_penalty: 1.05`**. A repetition penalty lowers the probability of every
  token already generated, and a scene graph is highly repetitive by nature (`"in front
  of"`, ids, brackets), so it may nudge predicates and numbers. Worth an ablation (1.0 vs 1.05).
- `config.json`: `vocab_size 151667` = Qwen's 151,665 tokens + `<obj_traj_start>` (151665)
  + `<obj_traj_end>` (151666); the embedding matrix was shrunk from 151,936 rows when the
  two tokens were added.
