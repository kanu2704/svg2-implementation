# TRASER on PVSG, VidOR and SVG2test: regenerating Table 2

Released checkpoint `UWGZQ/TRASER`, official inference settings (1 fps, at most 128 frames, at most 40 objects, greedy), float16 on Kaggle T4s. Lenient semantic criterion, temporal IoU > 0.5; scores over the videos with a prediction (see Coverage); judge: Kimi K3 (NVIDIA NIM) instead of the paper's GPT-4o-mini.

| | Triplet pvsg | Triplet vidor | Triplet svg2test | Relation pvsg | Relation vidor | Relation svg2test | Object pvsg | Object vidor | Object svg2test |
|---|---|---|---|---|---|---|---|---|---|
| TRASER, paper | 16.1 | 22.9 | 16.7 | 16.9 | 25.0 | 18.7 | 72.7 | 91.4 | 79.0 |
| **TRASER, ours** | 14.3 | – | – | 17.4 | – | – | 73.1 | – | – |

## Coverage

| | test videos | prepared | predicted | failed | answers not valid JSON (salvaged) |
|---|---|---|---|---|---|
| pvsg | 62 | 62 | 44 | 9 | 5 |

## Other settings (same predictions)

| setting | Triplet pvsg | Triplet vidor | Triplet svg2test | Relation pvsg | Relation vidor | Relation svg2test | Object pvsg | Object vidor | Object svg2test |
|---|---|---|---|---|---|---|---|---|---|
| lenient, tIoU 0.5 (main) | 14.3 | – | – | 17.4 | – | – | 73.1 | – | – |
| lenient, tIoU 0.1 | 21.3 | – | – | 25.3 | – | – | 73.1 | – | – |
| strict, tIoU 0.5 | 1.8 | – | – | 12.4 | – | – | 33.3 | – | – |
| strict, tIoU 0.1 | 2.4 | – | – | 16.4 | – | – | 33.3 | – | – |
| lenient, tIoU 0.5, per-video average | 15.0 | – | – | 19.0 | – | – | 73.0 | – | – |
| lenient, relation ignoring time | – | – | – | 31.1 | – | – | – | – | – |

## Judge answers (lenient = everything but mismatch)

- **pvsg**: object: identical 223, hypernym/hyponym 161, mismatch 150, semantic overlap 88, synonym 18; relation: mismatch 366, identical 150, not judged 106, hypernym/hyponym 77, semantic overlap 40, synonym 5

## How it is scored

See the docstring of `tools/bench_eval.py`. Differences from the paper that we know of:
- judge: Kimi K3 with our prompt (the paper's GPT-4o-mini prompt is not released);
- float16 on a T4 instead of bfloat16 on an A100 (greedy decoding can change a few tokens);
- VidOR masks: SAM 2.1 from VidOR's boxes on the frames TRASER reads (the paper also used SAM 2, details not given);
- videos longer than 128 s are read at fewer than 1 frame per second (released code caps at 128 frames);
- pooled over all human items (the per-video average is also shown).
