# What is done and what is still needed (TRASER)

Updated 22 Oct 2026, 15:30. ✅ done · ⏳ running · ⬜ to do (who does it)

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
- ✅ PVSG: 62 videos, 739 pairs (relation words)
- ✅ VidOR: 835 videos, 11,157 pairs (relation words; the objects it picks on the 649 videos run after the restart)
- ⬜ objects for the 248 videos run before (62 PVSG + 186 VidOR): the objects-only step saved nothing; its log is needed (you, server)
- ⬜ SVG2test (100): put the SA-V links file at `/media/nas_mount/kanupriya/sav_links.txt`, then start `full_pairs_run.py` again

## 6. Lenient judge on experiment 2b (`interp/PAIRS_LENIENT.md`, `judge_check_*.csv`)
- ✅ every word judged: Kimi K3's saved verdicts first (also for the same two words in the other order, 195); the 2,627 it never judged by Claude in this chat with the benchmark's judge prompt (NVIDIA retired Kimi K3 on 15 Oct 2026). Blind check on 200 words Kimi K3 judged: Claude accepts 79 of its 100 accepted, rejects 98 of its 100 rejected
- ✅ relation word tables (1st choice + top 5): PVSG + VidOR
- ✅ object tables: VidOR (649 videos); PVSG after the objects-only step
- ⬜ check the judge's verdicts by eye (you: `judge_check_relations.csv`, `judge_check_objects.csv`)
- ⬜ SVG2test tables: after its run

## 7. Fine-tuning (`finetune/FINETUNE.md`)
- ✅ SFT + GRPO trained on PVSG, tested on PVSG (62) + VidOR (300)
- ⬜ judge the 833-883 relation words the fine-tuned models used that were never judged (`score.py --ask`, NVIDIA key): until then their lenient scores are too low
- ⬜ SVG2test test: needs SVG2test prepared
- ✅ full SFT training log back in `logs/sft.jsonl` (steps 1-79 of 86; the last 7 steps were lost when the server swapped the file)

## 10. Table 2 with an untrained Qwen2.5-VL-7B in TRASER's pipeline (`results/qwen7b_bench/README.md`)
- ✅ code: `tools/run_traser.py` (`load_qwen`: same frames, masks, token arrangement, prompt + JSON format; Qwen's own vision encoder and language model; the two trained resamplers replaced by plain averaging to 32 tokens), `tools/bench_run.py --lm qwen7b`, `tools/qwen_bench_report.py`, `notebooks/qwen7b_run.py`
- ⬜ run on the server (you): `notebooks/qwen7b_run.py` (PVSG, SVG2test, then VidOR; about a day)
- ⬜ judge the new words of Qwen's answers, then the table (Claude)

## 8. Write-up
- ⬜ one-page summary for the supervisor: interpretability + pair experiment + fine-tuning (Claude)

## 9. Housekeeping
- ⬜ delete the GitHub token that was pasted in the chat on 20 Oct, if not done yet (you, github.com)
- ⬜ after the last run: close the tmux sessions on the server (`tmux kill-session -t full`, `-t overnight`)
