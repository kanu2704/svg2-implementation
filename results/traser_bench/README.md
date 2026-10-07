# TRASER on PVSG, VidOR and SVG2test: regenerating Table 2

Released checkpoint `UWGZQ/TRASER`, official inference settings (1 fps, at most 128 frames, at most 40 objects, greedy), float16 on Kaggle T4s. Lenient semantic criterion, temporal IoU > 0.5; scores over the videos with a prediction (see Coverage); judge: Kimi K3 (NVIDIA NIM) instead of the paper's GPT-4o-mini.

| | Triplet pvsg | Triplet vidor | Triplet svg2test | Relation pvsg | Relation vidor | Relation svg2test | Object pvsg | Object vidor | Object svg2test |
|---|---|---|---|---|---|---|---|---|---|
| TRASER, paper | 16.1 | 22.9 | 16.7 | 16.9 | 25.0 | 18.7 | 72.7 | 91.4 | 79.0 |
| **TRASER, ours** | 13.1 | – | – | 16.8 | – | – | 69.4 | – | – |

## Coverage

| | test videos | prepared | predicted | failed | answers not valid JSON (salvaged) |
|---|---|---|---|---|---|
| pvsg | 62 | 62 | 51 | 9 | 6 |

## Other settings (same predictions)

| setting | Triplet pvsg | Triplet vidor | Triplet svg2test | Relation pvsg | Relation vidor | Relation svg2test | Object pvsg | Object vidor | Object svg2test |
|---|---|---|---|---|---|---|---|---|---|
| lenient, tIoU 0.5 (main) | 13.1 | – | – | 16.8 | – | – | 69.4 | – | – |
| lenient, tIoU 0.1 | 19.7 | – | – | 25.1 | – | – | 69.4 | – | – |
| strict, tIoU 0.5 | 1.6 | – | – | 11.5 | – | – | 32.3 | – | – |
| strict, tIoU 0.1 | 2.1 | – | – | 15.6 | – | – | 32.3 | – | – |
| lenient, tIoU 0.5, per-video average | 13.3 | – | – | 17.8 | – | – | 70.5 | – | – |
| lenient, relation ignoring time | – | – | – | 31.7 | – | – | – | – | – |

## Judge answers (lenient = everything but mismatch)

- **pvsg**: object: identical 274, mismatch 217, hypernym/hyponym 174, semantic overlap 115, synonym 26; relation: mismatch 484, identical 165, hypernym/hyponym 89, semantic overlap 57, synonym 8

## How it is scored

See the docstring of `tools/bench_eval.py`. Differences from the paper that we know of:
- judge: Kimi K3 with our prompt (the paper's GPT-4o-mini prompt is not released);
- float16 on a T4 instead of bfloat16 on an A100 (greedy decoding can change a few tokens);
- VidOR masks: SAM 2.1 from VidOR's boxes on the frames TRASER reads (the paper also used SAM 2, details not given);
- videos longer than 128 s are read at fewer than 1 frame per second (released code caps at 128 frames);
- pooled over all human items (the per-video average is also shown).
