# Fine-tuning TRASER's language model: SFT and GRPO (`tools/finetune/`)

Notebook: `notebooks/traser_finetune.ipynb` (run after `traser_pairs.ipynb`, whose input sequences of the test videos it reuses).

Only the language model (Qwen2.5-VL-3B's decoder inside TRASER) is trained, with LoRA, on top of TRASER's weights.
The vision encoder and resamplers stay frozen: each video's input sequence is computed once
(`tools/interp/encode_stage.py`) and saved. Trained on the PVSG training split, tested on VidOR, SVG2test (not
trained on) and the PVSG test split.

| step | file | what it does | output |
|---|---|---|---|
| target | `common.py` | the human labels in TRASER's answer format (object names, `[s, "word", o, [[i, j]]]` with frame-index times); the GRPO reward (triplet F1 + 0.5 x pair F1, word match by stemming or the judge's cache) | |
| SFT | `sft.py` | cross-entropy on the human answer's tokens, LoRA r 16, 2 epochs; LoRA folded in at the end | model folder, `logs/sft.jsonl` |
| GRPO | `grpo.py` | 4 sampled answers per video, advantage = (reward - group mean) / group std, policy gradient + KL to the starting model (LoRA off) | model folder, `logs/grpo.jsonl` |
| test | `generate.py` | greedy answers on the test videos from the saved input sequences | `results/traser_bench/finetune/<model>/<dataset>/preds/` |
| scores | `score.py` | TRASER vs the fine-tuned models on the same videos (bench_eval's scores + pair recall), training curves | `results/traser_bench/finetune/FINETUNE.md` |

`encode_stage.py --videos_file` encodes a given list of videos (the training videos have no TRASER answer to pick a
sample from).
