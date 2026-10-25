# Experiment 2b, every word judged by nvidia/nemotron-3.5-super-vl-120b-a12b

As `results/traser_bench/interp/PAIRS_LENIENT.md` (read it for what the columns mean), with every verdict from nvidia/nemotron-3.5-super-vl-120b-a12b alone (`tools/rejudge.py`). Lenient: anything but a mismatch.

## svg2test: 99 videos, 2519 human pairs

### Relation word, TRASER's 1st choice

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) |
|---|---|---|---|---|---|---|---|
| fresh | all human pairs (2519) | 1338 (53%) | 898 (36%) | 1035 (41%) | 597 / 157 | 430 / 127 | 0 |
| fresh | missed (1534) | 708 (46%) | 423 (28%) | 464 (30%) | 378 / 93 | 315 / 71 | 0 |
| fresh | written (985) | 630 (64%) | 475 (48%) | 571 (58%) | 219 / 64 | 115 / 56 | 0 |
| after its own answer | missed (1449) | 598 (41%) | 377 (26%) | 413 (29%) | 279 / 58 | 243 / 58 | 0 |

### Relation word, any of its top 5

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) |
|---|---|---|---|---|---|---|---|
| fresh | all human pairs (2519) | 2103 (83%) | 1775 (70%) | 1895 (75%) | 449 / 121 | 319 / 111 | 0 |
| fresh | missed (1534) | 1244 (81%) | 1012 (66%) | 1065 (69%) | 302 / 70 | 249 / 70 | 0 |
| fresh | written (985) | 859 (87%) | 763 (77%) | 830 (84%) | 147 / 51 | 70 / 41 | 0 |
| after its own answer | missed (1449) | 1119 (77%) | 979 (68%) | 948 (65%) | 187 / 47 | 206 / 35 | 0 |

### Object, TRASER's 1st choice

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) | same object, exact (real video) |
|---|---|---|---|---|---|---|---|---|
| fresh | all human pairs (2519) | 1382 (55%) | 806 (32%) | 976 (39%) | 737 / 161 | 580 / 174 | 0 | 1202 (48%) |
| fresh | missed (1534) | 716 (47%) | 394 (26%) | 473 (31%) | 421 / 99 | 337 / 94 | 0 | 578 (38%) |
| fresh | written (985) | 666 (68%) | 412 (42%) | 503 (51%) | 316 / 62 | 243 / 80 | 0 | 624 (63%) |
| after its own answer | missed (1449) | 677 (47%) | 471 (33%) | 485 (33%) | 279 / 73 | 254 / 62 | 0 | 544 (38%) |

### Object, any of its top 5

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) | same object, exact (real video) |
|---|---|---|---|---|---|---|---|---|
| fresh | all human pairs (2519) | 2209 (88%) | 1730 (69%) | 1904 (76%) | 538 / 59 | 367 / 62 | 0 | 2056 (82%) |
| fresh | missed (1534) | 1279 (83%) | 933 (61%) | 1032 (67%) | 383 / 37 | 289 / 42 | 0 | 1163 (76%) |
| fresh | written (985) | 930 (94%) | 797 (81%) | 872 (89%) | 155 / 22 | 78 / 20 | 0 | 893 (91%) |
| after its own answer | missed (1449) | 1167 (81%) | 974 (67%) | 1016 (70%) | 242 / 49 | 194 / 43 | 0 | 1046 (72%) |

## pvsg: 62 videos, 739 human pairs

### Relation word, TRASER's 1st choice

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) |
|---|---|---|---|---|---|---|---|
| fresh | all human pairs (739) | 399 (54%) | 309 (42%) | 337 (46%) | 112 / 22 | 91 / 29 | 0 |
| fresh | missed (476) | 220 (46%) | 172 (36%) | 165 (35%) | 64 / 16 | 71 / 16 | 0 |
| fresh | written (263) | 179 (68%) | 137 (52%) | 172 (65%) | 48 / 6 | 20 / 13 | 0 |
| after its own answer | missed (355) | 101 (28%) | 81 (23%) | 84 (24%) | 32 / 12 | 27 / 10 | 0 |

### Relation word, any of its top 5

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) |
|---|---|---|---|---|---|---|---|
| fresh | all human pairs (739) | 592 (80%) | 545 (74%) | 531 (72%) | 76 / 29 | 80 / 19 | 0 |
| fresh | missed (476) | 355 (75%) | 323 (68%) | 298 (63%) | 52 / 20 | 70 / 13 | 0 |
| fresh | written (263) | 237 (90%) | 222 (84%) | 233 (89%) | 24 / 9 | 10 / 6 | 0 |
| after its own answer | missed (355) | 235 (66%) | 206 (58%) | 193 (54%) | 42 / 13 | 47 / 5 | 0 |

### Object, TRASER's 1st choice

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) | same object, exact (real video) |
|---|---|---|---|---|---|---|---|---|
| fresh | all human pairs (739) | 400 (54%) | 261 (35%) | 293 (40%) | 178 / 39 | 145 / 38 | 0 | 306 (41%) |
| fresh | missed (476) | 217 (46%) | 136 (29%) | 147 (31%) | 109 / 28 | 100 / 30 | 0 | 138 (29%) |
| fresh | written (263) | 183 (70%) | 125 (48%) | 146 (56%) | 69 / 11 | 45 / 8 | 0 | 168 (64%) |
| after its own answer | missed (355) | 169 (48%) | 119 (34%) | 125 (35%) | 62 / 12 | 53 / 9 | 0 | 108 (30%) |

### Object, any of its top 5

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) | same object, exact (real video) |
|---|---|---|---|---|---|---|---|---|
| fresh | all human pairs (739) | 643 (87%) | 550 (74%) | 574 (78%) | 116 / 23 | 88 / 19 | 0 | 543 (73%) |
| fresh | missed (476) | 400 (84%) | 332 (70%) | 340 (71%) | 84 / 16 | 70 / 10 | 0 | 306 (64%) |
| fresh | written (263) | 243 (92%) | 218 (83%) | 234 (89%) | 32 / 7 | 18 / 9 | 0 | 237 (90%) |
| after its own answer | missed (355) | 297 (84%) | 270 (76%) | 272 (77%) | 38 / 11 | 34 / 9 | 0 | 237 (67%) |

## vidor: 835 videos, 11157 human pairs

### Relation word, TRASER's 1st choice

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) |
|---|---|---|---|---|---|---|---|
| fresh | all human pairs (11157) | 2469 (22%) | 1828 (16%) | 2243 (20%) | 1352 / 711 | 1046 / 820 | 0 |
| fresh | missed (6528) | 1118 (17%) | 870 (13%) | 1060 (16%) | 611 / 363 | 495 / 437 | 0 |
| fresh | written (4629) | 1351 (29%) | 958 (21%) | 1183 (26%) | 741 / 348 | 551 / 383 | 0 |
| after its own answer | missed (6528) | 2857 (44%) | 2473 (38%) | 2471 (38%) | 971 / 587 | 909 / 523 | 0 |

### Relation word, any of its top 5

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) |
|---|---|---|---|---|---|---|---|
| fresh | all human pairs (11157) | 5410 (48%) | 4954 (44%) | 6046 (54%) | 1574 / 1118 | 991 / 1627 | 0 |
| fresh | missed (6528) | 2699 (41%) | 2528 (39%) | 3054 (47%) | 870 / 699 | 620 / 975 | 0 |
| fresh | written (4629) | 2711 (59%) | 2426 (52%) | 2992 (65%) | 704 / 419 | 371 / 652 | 0 |
| after its own answer | missed (6528) | 6013 (92%) | 5902 (90%) | 5836 (89%) | 216 / 105 | 253 / 76 | 0 |

### Object, TRASER's 1st choice

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) | same object, exact (real video) |
|---|---|---|---|---|---|---|---|---|
| fresh | all human pairs (11157) | 6988 (63%) | 6603 (59%) | 6417 (58%) | 1478 / 1093 | 1427 / 856 | 0 | 4201 (38%) |
| fresh | missed (6528) | 3672 (56%) | 3608 (55%) | 3391 (52%) | 802 / 738 | 842 / 561 | 0 | 1943 (30%) |
| fresh | written (4629) | 3316 (72%) | 2995 (65%) | 3026 (65%) | 676 / 355 | 585 / 295 | 0 | 2258 (49%) |
| after its own answer | missed (6528) | 3835 (59%) | 3706 (57%) | 3643 (56%) | 527 / 398 | 475 / 283 | 0 | 2026 (31%) |

### Object, any of its top 5

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) | same object, exact (real video) |
|---|---|---|---|---|---|---|---|---|
| fresh | all human pairs (11157) | 10834 (97%) | 10803 (97%) | 10839 (97%) | 166 / 135 | 139 / 144 | 0 | 9838 (88%) |
| fresh | missed (6528) | 6264 (96%) | 6254 (96%) | 6273 (96%) | 116 / 106 | 105 / 114 | 0 | 5503 (84%) |
| fresh | written (4629) | 4570 (99%) | 4549 (98%) | 4566 (99%) | 50 / 29 | 34 / 30 | 0 | 4335 (94%) |
| after its own answer | missed (6528) | 6281 (96%) | 6304 (97%) | 6283 (96%) | 75 / 98 | 78 / 80 | 0 | 5561 (85%) |

