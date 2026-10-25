# Table 2 with TRASER's language model replaced by an untrained Qwen2.5-VL-7B

TRASER's pipeline (same frames, same masks, same token selection and trajectory-aligned arrangement, same window labels, same prompt) with **Qwen2.5-VL-7B-Instruct, not fine-tuned** as vision encoder and language model. TRASER's two trained resamplers only fit its own 3B model, so each is replaced by plain averaging to the same 32 tokens per object and per window (nothing learned); TRASER's own trained special tokens are left out. TRASER learned its answer format in training, so the prompt adds a description of that JSON format (as the paper's baselines got a JSON template). Code: `tools/run_traser.py` (`load_qwen`), `tools/bench_run.py --lm qwen7b`, this page `tools/qwen_bench_report.py`.

Lenient semantic criterion, temporal IoU > 0.5, scored by `tools/bench_eval.py` exactly as TRASER's answers; TRASER's numbers are on the same videos as Qwen's.

| | Triplet pvsg | Triplet vidor | Triplet svg2test | Relation pvsg | Relation vidor | Relation svg2test | Object pvsg | Object vidor | Object svg2test |
|---|---|---|---|---|---|---|---|---|---|
| TRASER, paper | 16.1 | 22.9 | 16.7 | 16.9 | 25.0 | 18.7 | 72.7 | 91.4 | 79.0 |
| Qwen2.5-VL-3B (no fine-tuning), paper | 0.1 | 0.2 | 0.2 | 0.1 | 0.4 | 0.3 | 10.4 | 45.0 | 24.2 |
| **TRASER (released weights), ours** | 10.3 | 11.2 | 21.2 | 13.9 | 13.0 | 27.1 | 62.2 | 86.2 | 58.4 |
| **Qwen2.5-VL-7B-Instruct in TRASER's pipeline (not fine-tuned), ours** | 0.0 | 1.5 | 0.9 | 0.0 | 2.0 | 2.2 | 13.9 | 66.7 | 11.8 |

## Coverage

| dataset | model | videos | answers that are valid JSON | answer tokens (mean) | relation word right at any time | unjudged words |
|---|---|---|---|---|---|---|
| pvsg | TRASER (released weights), ours | 62 | 51 | 2769 | 27.7 | 0 |
| pvsg | Qwen2.5-VL-7B-Instruct in TRASER's pipeline (not fine-tuned), ours | 62 | 42 | 2490 | 1.1 | 0 |
| vidor | TRASER (released weights), ours | 835 | 835 | 499 | 22.2 | 0 |
| vidor | Qwen2.5-VL-7B-Instruct in TRASER's pipeline (not fine-tuned), ours | 835 | 812 | 580 | 5.4 | 0 |
| svg2test | TRASER (released weights), ours | 100 | 96 | 2693 | 29.9 | 0 |
| svg2test | Qwen2.5-VL-7B-Instruct in TRASER's pipeline (not fine-tuned), ours | 100 | 86 | 2500 | 2.6 | 0 |

*Unjudged words count as wrong (`--ask` or another judge fills them in). Qwen sometimes leaves an object unnamed ("object 3"): such a name was judged a mismatch.* Judge: 9581 words Kimi K3 never judged were judged by claude (NVIDIA retired Kimi K3 on 15 Oct 2026). Check on words Kimi K3 judged: of 100 it accepted, claude also accepts 79; of 100 it rejected, claude also rejects 98.
