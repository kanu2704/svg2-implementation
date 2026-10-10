# TRASER on PVSG, VidOR and SVG2test: regenerating Table 2

Released checkpoint `UWGZQ/TRASER`, official inference settings (1 fps, at most 128 frames, at most 40 objects, greedy), float16 on Kaggle T4s. Lenient semantic criterion, temporal IoU > 0.5; scores over the videos with a prediction (see Coverage); judge: Kimi K3 (NVIDIA NIM) instead of the paper's GPT-4o-mini.

| | Triplet pvsg | Triplet vidor | Triplet svg2test | Relation pvsg | Relation vidor | Relation svg2test | Object pvsg | Object vidor | Object svg2test |
|---|---|---|---|---|---|---|---|---|---|
| TRASER, paper | 16.1 | 22.9 | 16.7 | 16.9 | 25.0 | 18.7 | 72.7 | 91.4 | 79.0 |
| **TRASER, ours** | 10.3 | – | 21.2 | 13.9 | – | 27.1 | 62.2 | – | 58.4 |

## Coverage

| | test videos | prepared | predicted | failed | answers not valid JSON (salvaged) |
|---|---|---|---|---|---|
| pvsg | 62 | 62 | 62 | 0 | 11 |
| svg2test | 100 | 100 | 100 | 0 | 4 |

## pvsg by video source (lenient, tIoU > 0.5)

| source | videos | avg length | answers cut off | Triplet | Relation | Object |
|---|---|---|---|---|---|---|
| ego4d | 11 | 122 s | 3 | 1.0 | 3.1 | 53.7 |
| epic_kitchen | 11 | 97 s | 4 | 0.0 | 9.7 | 48.4 |
| vidor | 40 | 53 s | 4 | 15.7 | 18.3 | 76.4 |

## svg2test by video source (lenient, tIoU > 0.5)

| source | videos | avg length | answers cut off | Triplet | Relation | Object |
|---|---|---|---|---|---|---|
| sav | 33 | 17 s | 2 | 16.7 | 22.7 | 64.5 |
| vipseg | 67 | 12 s | 2 | 23.4 | 29.2 | 55.1 |

## Other settings (same predictions)

| setting | Triplet pvsg | Triplet vidor | Triplet svg2test | Relation pvsg | Relation vidor | Relation svg2test | Object pvsg | Object vidor | Object svg2test |
|---|---|---|---|---|---|---|---|---|---|
| lenient, tIoU 0.5 (main) | 10.3 | – | 21.2 | 13.9 | – | 27.1 | 62.2 | – | 58.4 |
| lenient, tIoU 0.1 | 15.6 | – | 23.2 | 21.2 | – | 29.8 | 62.2 | – | 58.4 |
| strict, tIoU 0.5 | 1.2 | – | 4.5 | 9.8 | – | 20.6 | 27.7 | – | 26.4 |
| strict, tIoU 0.1 | 1.7 | – | 4.7 | 13.3 | – | 22.1 | 27.7 | – | 26.4 |
| lenient, tIoU 0.5, only the objects TRASER was given (≤ 40) and relations between them | 10.5 | – | 22.8 | 14.2 | – | 29.1 | 68.4 | – | 67.7 |
| lenient, tIoU 0.5, per-video average | 11.1 | – | 21.9 | 15.5 | – | 27.6 | 67.7 | – | 63.7 |
| lenient, relation ignoring time | – | – | – | 27.7 | – | 29.9 | – | – | – |

## Judge answers (lenient = everything but mismatch)

- **pvsg**: object: mismatch 369, identical 355, hypernym/hyponym 236, semantic overlap 173, synonym 33; relation: mismatch 513, identical 225, hypernym/hyponym 102, semantic overlap 92, synonym 12
- **svg2test**: object: mismatch 890, identical 874, hypernym/hyponym 469, semantic overlap 454, synonym 133; relation: identical 803, mismatch 605, semantic overlap 157, hypernym/hyponym 130, synonym 57

## Notes on these predictions

- **pvsg**: 11 of 62 answers were cut off at the 8192-token limit (read up to the cut); 19 of 969 human relations (2.0%) involve an object TRASER was not given (40-object cap, or no mask on the sampled frames); vision encoder + resamplers in float32 for 5 of 62 videos, float16 for the rest (`pvsg/preds_fp16_vision/` has older float16 answers that were re-run).
- **svg2test**: 4 of 100 answers were cut off at the 8192-token limit (read up to the cut); 223 of 3187 human relations (7.0%) involve an object TRASER was not given (40-object cap, or no mask on the sampled frames); vision encoder + resamplers in float32 for all 100 videos (`svg2test/preds_fp16_vision/` has older float16 answers that were re-run).
- Video by video: `<dataset>/COMPARE.md`; pair by pair for 10 random videos: `<dataset>/PAIRS.md`.

## How it is scored

See the docstring of `tools/bench_eval.py`. Differences from the paper that we know of:
- judge: Kimi K3 with our prompt (the paper's GPT-4o-mini prompt is not released);
- language model in float16 on a T4 instead of bfloat16 on H100s (greedy decoding can change tokens on long answers);
- VidOR masks: SAM 2.1 from VidOR's boxes on the frames TRASER reads (the paper also used SAM 2, details not given);
- videos longer than 128 s are read at fewer than 1 frame per second (released code caps at 128 frames);
- pooled over all human items (the per-video average is also shown).
