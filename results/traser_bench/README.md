# TRASER on PVSG, VidOR and SVG2test: regenerating Table 2

Released checkpoint `UWGZQ/TRASER`, official inference settings (1 fps, at most 128 frames, at most 40 objects, greedy), float16 on Kaggle T4s. Lenient semantic criterion, temporal IoU > 0.5; scores over the videos with a prediction (see Coverage); judge: Kimi K3 (NVIDIA NIM) instead of the paper's GPT-4o-mini.

| | Triplet pvsg | Triplet vidor | Triplet svg2test | Relation pvsg | Relation vidor | Relation svg2test | Object pvsg | Object vidor | Object svg2test |
|---|---|---|---|---|---|---|---|---|---|
| TRASER, paper | 16.1 | 22.9 | 16.7 | 16.9 | 25.0 | 18.7 | 72.7 | 91.4 | 79.0 |
| **TRASER, ours** | 10.2 | – | – | 13.6 | – | – | 60.1 | – | – |

## Coverage

| | test videos | prepared | predicted | failed | answers not valid JSON (salvaged) |
|---|---|---|---|---|---|
| pvsg | 62 | 62 | 62 | 0 | 14 |

## Other settings (same predictions)

| setting | Triplet pvsg | Triplet vidor | Triplet svg2test | Relation pvsg | Relation vidor | Relation svg2test | Object pvsg | Object vidor | Object svg2test |
|---|---|---|---|---|---|---|---|---|---|
| lenient, tIoU 0.5 (main) | 10.2 | – | – | 13.6 | – | – | 60.1 | – | – |
| lenient, tIoU 0.1 | 15.5 | – | – | 20.5 | – | – | 60.1 | – | – |
| strict, tIoU 0.5 | 1.2 | – | – | 9.5 | – | – | 26.9 | – | – |
| strict, tIoU 0.1 | 1.7 | – | – | 12.9 | – | – | 26.9 | – | – |
| lenient, tIoU 0.5, per-video average | 11.0 | – | – | 15.3 | – | – | 66.0 | – | – |
| lenient, relation ignoring time | – | – | – | 26.3 | – | – | – | – | – |

## Judge answers (lenient = everything but mismatch)

- **pvsg**: object: mismatch 347, identical 345, hypernym/hyponym 226, semantic overlap 167, synonym 32; relation: mismatch 544, identical 360, hypernym/hyponym 121, semantic overlap 94, synonym 8

## How it is scored

See the docstring of `tools/bench_eval.py`. Differences from the paper that we know of:
- judge: Kimi K3 with our prompt (the paper's GPT-4o-mini prompt is not released);
- float16 on a T4 instead of bfloat16 on an A100 (greedy decoding can change a few tokens);
- VidOR masks: SAM 2.1 from VidOR's boxes on the frames TRASER reads (the paper also used SAM 2, details not given);
- videos longer than 128 s are read at fewer than 1 frame per second (released code caps at 128 frames);
- pooled over all human items (the per-video average is also shown).
