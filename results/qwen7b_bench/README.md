# Table 2 with TRASER's language model replaced by an untrained Qwen2.5-VL-7B

TRASER's pipeline (same frames, same masks, same token selection and trajectory-aligned arrangement, same window labels, same prompt) with **Qwen2.5-VL-7B-Instruct, not fine-tuned** as vision encoder and language model. TRASER's two trained resamplers only fit its own 3B model, so each is replaced by plain averaging to the same 32 tokens per object and per window (nothing learned); TRASER's own trained special tokens are left out. TRASER learned its answer format in training, so the prompt adds a description of that JSON format (as the paper's baselines got a JSON template). Code: `tools/run_traser.py` (`load_qwen`), `tools/bench_run.py --lm qwen7b`, this page `tools/qwen_bench_report.py`.

Lenient semantic criterion, temporal IoU > 0.5, scored by `tools/bench_eval.py` exactly as TRASER's answers; TRASER's numbers are on the same videos as Qwen's.

| | Triplet pvsg | Relation pvsg | Object pvsg |
|---|---|---|---|
| TRASER, paper | 16.1 | 16.9 | 72.7 |
| Qwen2.5-VL-3B (no fine-tuning), paper | 0.1 | 0.1 | 10.4 |
| **TRASER (released weights), ours** | 10.3 | 13.9 | 62.2 |
| **Qwen2.5-VL-7B-Instruct in TRASER's pipeline (not fine-tuned), ours** | 0.0 | 0.0 | 7.6 |

## Coverage

| dataset | model | videos | answers that are valid JSON | answer tokens (mean) | relation word right at any time | unjudged words |
|---|---|---|---|---|---|---|
| pvsg | TRASER (released weights), ours | 62 | 51 | 2769 | 27.7 | 0 |
| pvsg | Qwen2.5-VL-7B-Instruct in TRASER's pipeline (not fine-tuned), ours | 62 | 42 | 2490 | 0.4 | 899 |

*Unjudged words count as wrong (`--ask` or another judge fills them in).* Judge: 5729 words Kimi K3 never judged were judged by claude (NVIDIA retired Kimi K3 on 15 Oct 2026). Check on words Kimi K3 judged: of 100 it accepted, claude also accepts 79; of 100 it rejected, claude also rejects 98.
