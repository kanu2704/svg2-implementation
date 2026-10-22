# Experiment 2b under the lenient judge

Every human pair whose two objects TRASER received (`pairs_stage.py --phases e2all`), checked with the benchmark's judge (Kimi K3, lenient: anything but a mismatch). **Relation**: TRASER's 1st choice / any of its top 5 words for the pair is accepted for one of the human words. **Object**: given the subject and the human word, the object it picks first / any of its top 5 is the human object or an object whose human name the judge accepts for it. Inputs: the real video, another video's input in its place, the video blanked. Context: *fresh* (no earlier relation) or *after its own answer* (its relation list re-opened; missed pairs only). *only real / only another*: pairs right with the real video but not the other input / the other way round. *unjudged*: combinations the judge was never asked, counted as wrong (`python3 tools/interp/judge_pairs.py` asks it).

## pvsg: 62 videos, 739 human pairs

### Relation word, TRASER's 1st choice

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) |
|---|---|---|---|---|---|---|---|
| fresh | all human pairs (739) | 429 (58%) | 364 (49%) | 388 (53%) | 99 / 34 | 82 / 41 | 192 |
| fresh | missed (476) | 243 (51%) | 215 (45%) | 206 (43%) | 53 / 25 | 65 / 28 | 159 |
| fresh | written (263) | 186 (71%) | 149 (57%) | 182 (69%) | 46 / 9 | 17 / 13 | 33 |
| after its own answer | missed (355) | 100 (28%) | 87 (25%) | 87 (25%) | 25 / 12 | 22 / 9 | 164 |

### Relation word, any of its top 5

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) |
|---|---|---|---|---|---|---|---|
| fresh | all human pairs (739) | 599 (81%) | 559 (76%) | 553 (75%) | 69 / 29 | 77 / 31 | 116 |
| fresh | missed (476) | 359 (75%) | 335 (70%) | 318 (67%) | 44 / 20 | 65 / 24 | 100 |
| fresh | written (263) | 240 (91%) | 224 (85%) | 235 (89%) | 25 / 9 | 12 / 7 | 16 |
| after its own answer | missed (355) | 236 (66%) | 212 (60%) | 217 (61%) | 36 / 12 | 30 / 11 | 119 |

### Object, TRASER's 1st choice

*Not available yet: these results were made before the run saved the objects it picks (re-run `pairs_stage.py --phases e2all`; old files are redone automatically).*

### Object, any of its top 5

*Not available yet: these results were made before the run saved the objects it picks (re-run `pairs_stage.py --phases e2all`; old files are redone automatically).*

### Check the judge: relation words, most frequent

| human | TRASER | times | judge (Kimi K3) |
|---|---|---|---|
| holding | holding | 603 | identical (right) |
| holding | hold | 509 | identical (right) |
| holding | touching | 461 | semantic overlap (right) |
| on | on | 444 | identical (right) |
| on | above | 325 | semantic overlap (right) |
| on | approaches | 308 | not judged yet |
| on | attached to | 255 | semantic overlap (right) |
| holding | in front of | 230 | mismatch (wrong) |
| on | in front of | 220 | mismatch (wrong) |
| holding | carrying | 209 | hypernym/hyponym (right) |
| holding | above | 195 | not judged yet |
| holding | approaches | 189 | mismatch (wrong) |
| holding | manipulates | 187 | not judged yet |
| holding | wearing | 184 | mismatch (wrong) |
| on | moves away from | 175 | not judged yet |
| holding | near | 157 | mismatch (wrong) |
| on | in | 154 | not judged yet |
| in front of | in front of | 148 | identical (right) |
| on | inside | 134 | mismatch (wrong) |
| holding | placing | 128 | semantic overlap (right) |
| touching | holding | 123 | hypernym/hyponym (right) |
| touching | touching | 115 | identical (right) |
| in front of | approaches | 114 | mismatch (wrong) |
| holding | on | 111 | mismatch (wrong) |
| holding | below | 106 | mismatch (wrong) |

1483 different combinations, 1150 not judged yet; all of them in `judge_check_*.csv`.

## vidor: 835 videos, 11157 human pairs

### Relation word, TRASER's 1st choice

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) |
|---|---|---|---|---|---|---|---|
| fresh | all human pairs (11157) | 3263 (29%) | 2761 (25%) | 3651 (33%) | 1563 / 1061 | 1078 / 1466 | 277 |
| fresh | missed (6528) | 1542 (24%) | 1392 (21%) | 1719 (26%) | 739 / 589 | 573 / 750 | 178 |
| fresh | written (4629) | 1721 (37%) | 1369 (30%) | 1932 (42%) | 824 / 472 | 505 / 716 | 99 |
| after its own answer | missed (6528) | 3403 (52%) | 3227 (49%) | 3558 (55%) | 774 / 598 | 528 / 683 | 79 |

### Relation word, any of its top 5

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) |
|---|---|---|---|---|---|---|---|
| fresh | all human pairs (11157) | 7072 (63%) | 7191 (64%) | 8061 (72%) | 1441 / 1560 | 920 / 1909 | 835 |
| fresh | missed (6528) | 3736 (57%) | 3916 (60%) | 4288 (66%) | 845 / 1025 | 647 / 1199 | 590 |
| fresh | written (4629) | 3336 (72%) | 3275 (71%) | 3773 (82%) | 596 / 535 | 273 / 710 | 245 |
| after its own answer | missed (6528) | 6111 (94%) | 6028 (92%) | 6013 (92%) | 136 / 53 | 140 / 42 | 72 |

### Object, TRASER's 1st choice

*Objects on 646 of 835 videos so far (the rest were made before the run saved them).*

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) | same object, exact (real video) |
|---|---|---|---|---|---|---|---|---|
| fresh | all human pairs (8852) | 5546 (63%) | 5180 (59%) | 5072 (57%) | 1218 / 852 | 1148 / 674 | 2802 | 3291 (37%) |
| fresh | missed (5168) | 2914 (56%) | 2831 (55%) | 2673 (52%) | 654 / 571 | 676 / 435 | 1902 | 1495 (29%) |
| fresh | written (3684) | 2632 (71%) | 2349 (64%) | 2399 (65%) | 564 / 281 | 472 / 239 | 900 | 1796 (49%) |
| after its own answer | missed (5168) | 3048 (59%) | 2917 (56%) | 2892 (56%) | 420 / 289 | 372 / 216 | 1756 | 1563 (30%) |

### Object, any of its top 5

*Objects on 646 of 835 videos so far (the rest were made before the run saved them).*

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) | same object, exact (real video) |
|---|---|---|---|---|---|---|---|---|
| fresh | all human pairs (8852) | 8603 (97%) | 8603 (97%) | 8627 (97%) | 107 / 107 | 90 / 114 | 249 | 7821 (88%) |
| fresh | missed (5168) | 4962 (96%) | 4976 (96%) | 4986 (96%) | 75 / 89 | 71 / 95 | 206 | 4365 (84%) |
| fresh | written (3684) | 3641 (99%) | 3627 (98%) | 3641 (99%) | 32 / 18 | 19 / 19 | 43 | 3456 (94%) |
| after its own answer | missed (5168) | 4975 (96%) | 5003 (97%) | 4981 (96%) | 56 / 84 | 61 / 67 | 192 | 4414 (85%) |

### Check the judge: relation words, most frequent

| human | TRASER | times | judge (Kimi K3) |
|---|---|---|---|
| next to | in front of | 14215 | mismatch (wrong) |
| in front of | in front of | 13874 | identical (right) |
| in front of | approaches | 10476 | mismatch (wrong) |
| next to | approaches | 10339 | mismatch (wrong) |
| next to | near | 9615 | hypernym/hyponym (right) |
| next to | overlapping | 8198 | mismatch (wrong) |
| in front of | near | 7778 | hypernym/hyponym (right) |
| next to | above | 7238 | mismatch (wrong) |
| in front of | overlapping | 7218 | semantic overlap (right) |
| next to | behind | 6748 | mismatch (wrong) |
| next to | next to | 6548 | identical (right) |
| next to | holding | 6490 | mismatch (wrong) |
| in front of | moves away from | 5983 | mismatch (wrong) |
| in front of | approaching | 5970 | mismatch (wrong) |
| behind | in front of | 5939 | mismatch (wrong) |
| next to | moves away from | 5562 | mismatch (wrong) |
| in front of | above | 5520 | mismatch (wrong) |
| in front of | behind | 5484 | mismatch (wrong) |
| next to | touching | 5334 | semantic overlap (right) |
| next to | approaching | 5238 | mismatch (wrong) |
| in front of | holding | 4490 | mismatch (wrong) |
| next to | below | 4364 | mismatch (wrong) |
| in front of | next to | 4340 | semantic overlap (right) |
| behind | approaches | 4333 | mismatch (wrong) |
| watch | in front of | 4282 | mismatch (wrong) |

1803 different combinations, 893 not judged yet; all of them in `judge_check_*.csv`.

### Check the judge: objects (another object than the human one), most frequent

| human | TRASER | times | judge (Kimi K3) |
|---|---|---|---|
| adult | adult | 34608 | identical (right) |
| child | child | 7945 | identical (right) |
| child | adult | 5557 | not judged yet |
| adult | child | 5296 | hypernym/hyponym (right) |
| adult | chair | 2592 | mismatch (wrong) |
| adult | table | 2122 | not judged yet |
| child | table | 1660 | not judged yet |
| chair | adult | 1619 | not judged yet |
| guitar | adult | 1517 | not judged yet |
| adult | car | 1496 | mismatch (wrong) |
| child | toy | 1432 | mismatch (wrong) |
| toy | toy | 1391 | identical (right) |
| child | sofa | 1353 | not judged yet |
| adult | guitar | 1347 | not judged yet |
| camera | adult | 1314 | not judged yet |
| adult | cup | 1271 | not judged yet |
| sheep/goat | sheep/goat | 1244 | identical (right) |
| baby | adult | 1071 | not judged yet |
| cup | adult | 1052 | not judged yet |
| toy | child | 1038 | not judged yet |
| table | adult | 1036 | not judged yet |
| adult | bottle | 1024 | not judged yet |
| dog | dog | 1019 | identical (right) |
| chair | chair | 1016 | identical (right) |
| ball/sports ball | adult | 1010 | not judged yet |

816 different combinations, 690 not judged yet; all of them in `judge_check_*.csv`.
