# Experiment 2b under the lenient judge

Every human pair whose two objects TRASER received (`pairs_stage.py --phases e2all`), checked with the benchmark's judge (Kimi K3, lenient: anything but a mismatch). **Relation**: TRASER's 1st choice / any of its top 5 words for the pair is accepted for one of the human words. **Object**: given the subject and the human word, the object it picks first / any of its top 5 is the human object or an object whose human name the judge accepts for it. Inputs: the real video, another video's input in its place, the video blanked. Context: *fresh* (no earlier relation) or *after its own answer* (its relation list re-opened; missed pairs only). *only real / only another*: pairs right with the real video but not the other input / the other way round. *unjudged*: combinations the judge was never asked, counted as wrong (`python3 tools/interp/judge_pairs.py` asks it).

**Judge.** 5729 words Kimi K3 never judged were judged by claude (NVIDIA retired Kimi K3 on 15 Oct 2026). Check on words Kimi K3 judged: of 100 it accepted, claude also accepts 79; of 100 it rejected, claude also rejects 98. Kimi K3's own verdicts always come first.

## svg2test: 99 videos, 2519 human pairs

### Relation word, TRASER's 1st choice

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) |
|---|---|---|---|---|---|---|---|
| fresh | all human pairs (2519) | 1558 (62%) | 1162 (46%) | 1288 (51%) | 561 / 165 | 411 / 141 | 0 |
| fresh | missed (1534) | 862 (56%) | 594 (39%) | 642 (42%) | 366 / 98 | 307 / 87 | 0 |
| fresh | written (985) | 696 (71%) | 568 (58%) | 646 (66%) | 195 / 67 | 104 / 54 | 0 |
| after its own answer | missed (1449) | 774 (53%) | 586 (40%) | 677 (47%) | 284 / 96 | 202 / 105 | 0 |

### Relation word, any of its top 5

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) |
|---|---|---|---|---|---|---|---|
| fresh | all human pairs (2519) | 2206 (88%) | 1973 (78%) | 2080 (83%) | 356 / 123 | 238 / 112 | 0 |
| fresh | missed (1534) | 1324 (86%) | 1161 (76%) | 1211 (79%) | 236 / 73 | 183 / 70 | 0 |
| fresh | written (985) | 882 (90%) | 812 (82%) | 869 (88%) | 120 / 50 | 55 / 42 | 0 |
| after its own answer | missed (1449) | 1233 (85%) | 1171 (81%) | 1184 (82%) | 90 / 28 | 77 / 28 | 0 |

### Object, TRASER's 1st choice

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) | same object, exact (real video) |
|---|---|---|---|---|---|---|---|---|
| fresh | all human pairs (2519) | 1374 (55%) | 789 (31%) | 974 (39%) | 737 / 152 | 569 / 169 | 1009 | 1202 (48%) |
| fresh | missed (1534) | 713 (46%) | 370 (24%) | 468 (31%) | 430 / 87 | 340 / 95 | 723 | 578 (38%) |
| fresh | written (985) | 661 (67%) | 419 (43%) | 506 (51%) | 307 / 65 | 229 / 74 | 286 | 624 (63%) |
| after its own answer | missed (1449) | 662 (46%) | 454 (31%) | 477 (33%) | 275 / 67 | 248 / 63 | 679 | 544 (38%) |

### Object, any of its top 5

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) | same object, exact (real video) |
|---|---|---|---|---|---|---|---|---|
| fresh | all human pairs (2519) | 2186 (87%) | 1683 (67%) | 1869 (74%) | 560 / 57 | 376 / 59 | 329 | 2056 (82%) |
| fresh | missed (1534) | 1260 (82%) | 893 (58%) | 999 (65%) | 401 / 34 | 302 / 41 | 270 | 1163 (76%) |
| fresh | written (985) | 926 (94%) | 790 (80%) | 870 (88%) | 159 / 23 | 74 / 18 | 59 | 893 (91%) |
| after its own answer | missed (1449) | 1161 (80%) | 942 (65%) | 992 (68%) | 261 / 42 | 211 / 42 | 284 | 1046 (72%) |

### Check the judge: relation words, most frequent

| human | TRASER | times | judge (Kimi K3) |
|---|---|---|---|
| on | on | 2339 | identical (right) |
| on | above | 2028 | semantic overlap (right) |
| on | in front of | 1960 | mismatch (wrong) |
| in front of | in front of | 1846 | identical (right) |
| on | attached to | 1570 | semantic overlap (right) |
| above | above | 1016 | identical (right) |
| on | below | 949 | mismatch (wrong) |
| in front of | below | 812 | mismatch (wrong) |
| in front of | above | 795 | mismatch (wrong) |
| in front of | approaches | 773 | mismatch (wrong) |
| in front of | on | 771 | mismatch (wrong) |
| on | behind | 762 | mismatch (wrong) |
| in front of | attached to | 708 | mismatch (wrong) |
| on | approaches | 704 | mismatch (wrong, by moonshotai/kimi-k3 (other order)) |
| on | overlapping | 637 | semantic overlap (right) |
| on | inside | 635 | mismatch (wrong) |
| above | in front of | 617 | mismatch (wrong) |
| on | near | 576 | mismatch (wrong, by claude) |
| in front of | behind | 534 | mismatch (wrong) |
| above | on | 508 | semantic overlap (right) |
| above | attached to | 485 | mismatch (wrong) |
| on | mounted on | 482 | hypernym/hyponym (right) |
| in front of | approaching | 411 | mismatch (wrong) |
| attached to | attached to | 407 | identical (right) |
| below | below | 402 | identical (right) |

4229 different combinations, 0 not judged yet; all of them in `judge_check_*.csv`.

### Check the judge: objects (another object than the human one), most frequent

| human | TRASER | times | judge (Kimi K3) |
|---|---|---|---|
| wall | wall | 696 | identical (right) |
| person | person | 448 | identical (right) |
| floor | wall | 269 | mismatch (wrong) |
| wall | person | 256 | mismatch (wrong) |
| sky | trees | 229 | not judged yet |
| ground | treadmill | 207 | mismatch (wrong) |
| wall | door | 194 | mismatch (wrong, by moonshotai/kimi-k3 (other order)) |
| building | building | 148 | identical (right) |
| person | wall | 147 | mismatch (wrong, by moonshotai/kimi-k3 (other order)) |
| ceiling | tv | 132 | not judged yet |
| table | paper | 130 | not judged yet |
| floor | stick | 126 | not judged yet |
| sky | tree | 125 | mismatch (wrong) |
| table | background floor | 124 | not judged yet |
| road | building | 121 | not judged yet |
| trees | rock | 117 | not judged yet |
| ground | wall | 114 | not judged yet |
| ground | person | 111 | mismatch (wrong) |
| player | player | 110 | identical (right) |
| ceiling | wall | 109 | mismatch (wrong, by moonshotai/kimi-k3 (other order)) |
| t-shirt | t-shirt | 108 | identical (right) |
| barrier wall | player | 107 | not judged yet |
| sky | building | 106 | mismatch (wrong) |
| road | sidewalk | 104 | not judged yet |
| grass | tree | 103 | not judged yet |

5758 different combinations, 5272 not judged yet; all of them in `judge_check_*.csv`.

## pvsg: 62 videos, 739 human pairs

### Relation word, TRASER's 1st choice

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) |
|---|---|---|---|---|---|---|---|
| fresh | all human pairs (739) | 449 (61%) | 376 (51%) | 410 (55%) | 103 / 30 | 88 / 49 | 0 |
| fresh | missed (476) | 256 (54%) | 222 (47%) | 221 (46%) | 57 / 23 | 71 / 36 | 0 |
| fresh | written (263) | 193 (73%) | 154 (59%) | 189 (72%) | 46 / 7 | 17 / 13 | 0 |
| after its own answer | missed (355) | 123 (35%) | 110 (31%) | 115 (32%) | 26 / 13 | 21 / 13 | 0 |

### Relation word, any of its top 5

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) |
|---|---|---|---|---|---|---|---|
| fresh | all human pairs (739) | 634 (86%) | 608 (82%) | 583 (79%) | 61 / 35 | 78 / 27 | 0 |
| fresh | missed (476) | 388 (82%) | 371 (78%) | 344 (72%) | 44 / 27 | 66 / 22 | 0 |
| fresh | written (263) | 246 (94%) | 237 (90%) | 239 (91%) | 17 / 8 | 12 / 5 | 0 |
| after its own answer | missed (355) | 250 (70%) | 220 (62%) | 225 (63%) | 41 / 11 | 34 / 9 | 0 |

### Object, TRASER's 1st choice

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) | same object, exact (real video) |
|---|---|---|---|---|---|---|---|---|
| fresh | all human pairs (739) | 416 (56%) | 291 (39%) | 318 (43%) | 167 / 42 | 139 / 41 | 208 | 306 (41%) |
| fresh | missed (476) | 232 (49%) | 160 (34%) | 168 (35%) | 103 / 31 | 98 / 34 | 158 | 138 (29%) |
| fresh | written (263) | 184 (70%) | 131 (50%) | 150 (57%) | 64 / 11 | 41 / 7 | 50 | 168 (64%) |
| after its own answer | missed (355) | 178 (50%) | 134 (38%) | 135 (38%) | 61 / 17 | 55 / 12 | 101 | 108 (30%) |

### Object, any of its top 5

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) | same object, exact (real video) |
|---|---|---|---|---|---|---|---|---|
| fresh | all human pairs (739) | 659 (89%) | 570 (77%) | 589 (80%) | 105 / 16 | 89 / 19 | 78 | 543 (73%) |
| fresh | missed (476) | 414 (87%) | 349 (73%) | 354 (74%) | 74 / 9 | 71 / 11 | 60 | 306 (64%) |
| fresh | written (263) | 245 (93%) | 221 (84%) | 235 (89%) | 31 / 7 | 18 / 8 | 18 | 237 (90%) |
| after its own answer | missed (355) | 304 (86%) | 281 (79%) | 291 (82%) | 34 / 11 | 22 / 9 | 46 | 237 (67%) |

### Check the judge: relation words, most frequent

| human | TRASER | times | judge (Kimi K3) |
|---|---|---|---|
| holding | holding | 603 | identical (right) |
| holding | hold | 509 | identical (right) |
| holding | touching | 461 | semantic overlap (right) |
| on | on | 444 | identical (right) |
| on | above | 325 | semantic overlap (right) |
| on | approaches | 308 | mismatch (wrong, by moonshotai/kimi-k3 (other order)) |
| on | attached to | 255 | semantic overlap (right) |
| holding | in front of | 230 | mismatch (wrong) |
| on | in front of | 220 | mismatch (wrong) |
| holding | carrying | 209 | hypernym/hyponym (right) |
| holding | above | 195 | mismatch (wrong, by moonshotai/kimi-k3 (other order)) |
| holding | approaches | 189 | mismatch (wrong) |
| holding | manipulates | 187 | semantic overlap (right, by claude) |
| holding | wearing | 184 | mismatch (wrong) |
| on | moves away from | 175 | mismatch (wrong, by claude) |
| holding | near | 157 | mismatch (wrong) |
| on | in | 154 | semantic overlap (right, by moonshotai/kimi-k3 (other order)) |
| in front of | in front of | 148 | identical (right) |
| on | inside | 134 | mismatch (wrong) |
| holding | placing | 128 | semantic overlap (right) |
| touching | holding | 123 | hypernym/hyponym (right) |
| touching | touching | 115 | identical (right) |
| in front of | approaches | 114 | mismatch (wrong) |
| holding | on | 111 | mismatch (wrong) |
| holding | below | 106 | mismatch (wrong) |

1483 different combinations, 0 not judged yet; all of them in `judge_check_*.csv`.

### Check the judge: objects (another object than the human one), most frequent

| human | TRASER | times | judge (Kimi K3) |
|---|---|---|---|
| card | card | 588 | identical (right) |
| grass | adult | 248 | not judged yet |
| adult | adult | 234 | identical (right) |
| child | child | 192 | identical (right) |
| ball | adult | 155 | not judged yet |
| child | adult | 152 | hypernym/hyponym (right, by moonshotai/kimi-k3 (other order)) |
| table | card | 139 | not judged yet |
| table | chair | 133 | mismatch (wrong) |
| child | cake | 117 | mismatch (wrong, by claude) |
| ball | helmet | 106 | not judged yet |
| floor | chair | 100 | mismatch (wrong) |
| card | box | 100 | not judged yet |
| table | wall | 95 | mismatch (wrong, by moonshotai/kimi-k3 (other order)) |
| chair | chair | 90 | identical (right) |
| table | cake | 88 | mismatch (wrong, by moonshotai/kimi-k3 (other order)) |
| table | adult | 87 | mismatch (wrong, by claude) |
| floor | table | 87 | mismatch (wrong) |
| ball | ball | 82 | identical (right) |
| fruit | fruit | 81 | identical (right) |
| candle | cake | 78 | semantic overlap (right) |
| table | child | 75 | mismatch (wrong, by claude) |
| chair | adult | 73 | mismatch (wrong, by moonshotai/kimi-k3 (other order)) |
| wall | child | 72 | not judged yet |
| grass | tree | 71 | not judged yet |
| floor | wall | 68 | mismatch (wrong) |

1529 different combinations, 1180 not judged yet; all of them in `judge_check_*.csv`.

## vidor: 835 videos, 11157 human pairs

### Relation word, TRASER's 1st choice

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) |
|---|---|---|---|---|---|---|---|
| fresh | all human pairs (11157) | 3265 (29%) | 2763 (25%) | 3656 (33%) | 1565 / 1063 | 1076 / 1467 | 0 |
| fresh | missed (6528) | 1543 (24%) | 1392 (21%) | 1722 (26%) | 740 / 589 | 572 / 751 | 0 |
| fresh | written (4629) | 1722 (37%) | 1371 (30%) | 1934 (42%) | 825 / 474 | 504 / 716 | 0 |
| after its own answer | missed (6528) | 3405 (52%) | 3227 (49%) | 3559 (55%) | 775 / 597 | 528 / 682 | 0 |

### Relation word, any of its top 5

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) |
|---|---|---|---|---|---|---|---|
| fresh | all human pairs (11157) | 7080 (63%) | 7197 (65%) | 8077 (72%) | 1441 / 1558 | 909 / 1906 | 0 |
| fresh | missed (6528) | 3739 (57%) | 3922 (60%) | 4296 (66%) | 841 / 1024 | 640 / 1197 | 0 |
| fresh | written (4629) | 3341 (72%) | 3275 (71%) | 3781 (82%) | 600 / 534 | 269 / 709 | 0 |
| after its own answer | missed (6528) | 6113 (94%) | 6031 (92%) | 6016 (92%) | 135 / 53 | 139 / 42 | 0 |

### Object, TRASER's 1st choice

*Objects on 832 of 835 videos so far (the rest were made before the run saved them).*

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) | same object, exact (real video) |
|---|---|---|---|---|---|---|---|---|
| fresh | all human pairs (11157) | 7264 (65%) | 6873 (62%) | 6644 (60%) | 1404 / 1013 | 1416 / 796 | 63 | 4201 (38%) |
| fresh | missed (6528) | 3882 (59%) | 3780 (58%) | 3543 (54%) | 767 / 665 | 840 / 501 | 44 | 1943 (30%) |
| fresh | written (4629) | 3382 (73%) | 3093 (67%) | 3101 (67%) | 637 / 348 | 576 / 295 | 19 | 2258 (49%) |
| after its own answer | missed (6528) | 4043 (62%) | 3922 (60%) | 3861 (59%) | 478 / 357 | 440 / 258 | 20 | 2026 (31%) |

### Object, any of its top 5

*Objects on 832 of 835 videos so far (the rest were made before the run saved them).*

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) | same object, exact (real video) |
|---|---|---|---|---|---|---|---|---|
| fresh | all human pairs (11157) | 10862 (97%) | 10844 (97%) | 10882 (98%) | 145 / 127 | 120 / 140 | 12 | 9838 (88%) |
| fresh | missed (6528) | 6289 (96%) | 6282 (96%) | 6307 (97%) | 104 / 97 | 92 / 110 | 7 | 5503 (84%) |
| fresh | written (4629) | 4573 (99%) | 4562 (99%) | 4575 (99%) | 41 / 30 | 28 / 30 | 5 | 4335 (94%) |
| after its own answer | missed (6528) | 6296 (96%) | 6327 (97%) | 6316 (97%) | 65 / 96 | 59 / 79 | 9 | 5561 (85%) |

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

1803 different combinations, 0 not judged yet; all of them in `judge_check_*.csv`.

### Check the judge: objects (another object than the human one), most frequent

| human | TRASER | times | judge (Kimi K3) |
|---|---|---|---|
| adult | adult | 44378 | identical (right) |
| child | child | 9920 | identical (right) |
| child | adult | 6540 | hypernym/hyponym (right, by moonshotai/kimi-k3 (other order)) |
| adult | child | 6173 | hypernym/hyponym (right) |
| adult | chair | 3074 | mismatch (wrong) |
| adult | table | 2441 | mismatch (wrong, by claude) |
| adult | car | 2335 | mismatch (wrong) |
| chair | adult | 1961 | mismatch (wrong, by moonshotai/kimi-k3 (other order)) |
| child | toy | 1893 | mismatch (wrong) |
| child | table | 1843 | mismatch (wrong, by claude) |
| toy | toy | 1786 | identical (right) |
| child | sofa | 1739 | mismatch (wrong, by moonshotai/kimi-k3 (other order)) |
| adult | cup | 1727 | mismatch (wrong, by claude) |
| guitar | adult | 1613 | mismatch (wrong, by claude) |
| adult | guitar | 1586 | mismatch (wrong, by claude) |
| camera | adult | 1454 | mismatch (wrong, by claude) |
| baby | adult | 1432 | mismatch (wrong, by moonshotai/kimi-k3 (other order)) |
| ball/sports ball | child | 1415 | mismatch (wrong, by claude) |
| cup | adult | 1372 | mismatch (wrong, by claude) |
| toy | child | 1340 | mismatch (wrong, by moonshotai/kimi-k3 (other order)) |
| adult | bicycle | 1326 | mismatch (wrong, by claude) |
| adult | baby | 1244 | mismatch (wrong) |
| sheep/goat | sheep/goat | 1244 | identical (right) |
| table | adult | 1232 | mismatch (wrong, by claude) |
| adult | bottle | 1183 | mismatch (wrong, by claude) |

898 different combinations, 68 not judged yet; all of them in `judge_check_*.csv`.
