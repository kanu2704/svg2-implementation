# What is done and what is still needed (TRASER)

Updated 21 Oct 2026, 16:10. ✅ done · ⏳ running · ⬜ to do (who does it)

## 1. Benchmark: the paper's Table 2 for TRASER (`README.md`)
- ✅ PVSG (62), SVG2test (100), VidOR (835) scored: lenient, tIoU > 0.5; VidOR with occurrences merged

## 2. Where TRASER loses points (`diagnosis/ERRORS.md`)
- ✅ all three datasets

## 3. Interpretability report (`interp/REPORT.md`: probes, forced answers, interventions, patching, attention)
- ✅ PVSG (25 videos) + VidOR (60)
- ⬜ SVG2test (40): needs SVG2test prepared on the server (Meta's SA-V links file)
- ⬜ optional: attention on the long PVSG videos (did not fit the T4s; fits the A6000)

## 4. Pair experiment, experiments 1-5 (`interp/PAIRS.md`)
- ✅ PVSG (62) + VidOR (300 sample)
- ⬜ SVG2test: needs the SA-V links file

## 5. Experiment 2 on every human pair (`PAIRS.md` 2b, `PAIRS_LENIENT.md`)
- ✅ PVSG: 62 videos, 739 pairs (without the objects it picks)
- ⏳ VidOR: 124 / 835 videos (running, 1 copy)
- ⬜ restart with the new code (you, server): saves the objects it picks + 3 copies; PVSG and the VidOR videos done so far are redone
- ⬜ SVG2test (100): put the SA-V links file at `/media/nas_mount/kanupriya/sav_links.txt`, then start `full_pairs_run.py` again

## 6. Lenient judge (Kimi K3) on experiment 2b (`interp/PAIRS_LENIENT.md`, `judge_check_*.csv`)
- ✅ relation word tables, PVSG (1st choice + top 5), partly judged
- ⬜ judge the ~1,700 word combinations not judged yet (you, Mac: `tools/interp/judge_pairs.py` with your NVIDIA key)
- ⬜ object tables (1st choice + top 5): after the restarted run
- ⬜ judge the object names: `judge_pairs.py` again after the run
- ⬜ check the judge's verdicts by eye (you: `judge_check_relations.csv`, `judge_check_objects.csv`)
- ⬜ VidOR and SVG2test tables: after their runs (Claude regenerates the page)

## 7. Fine-tuning (`finetune/FINETUNE.md`)
- ✅ SFT + GRPO trained on PVSG, tested on PVSG (62) + VidOR (300)
- ⬜ judge the 833-883 relation words the fine-tuned models used that were never judged (`score.py --ask`, NVIDIA key): until then their lenient scores are too low
- ⬜ SVG2test test: needs SVG2test prepared
- ✅ full SFT training log back in `logs/sft.jsonl` (steps 1-79 of 86; the last 7 steps were lost when the server swapped the file)

## 8. Write-up
- ⬜ one-page summary for the supervisor: interpretability + pair experiment + fine-tuning (Claude)

## 9. Housekeeping
- ⬜ delete the GitHub token that was pasted in the chat on 20 Oct, if not done yet (you, github.com)
- ⬜ after the last run: close the tmux sessions on the server (`tmux kill-session -t full`, `-t overnight`)
