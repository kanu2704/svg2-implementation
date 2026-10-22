# Experiment 2b under the lenient judge

Every human pair whose two objects TRASER received (`pairs_stage.py --phases e2all`), checked with the benchmark's judge (Kimi K3, lenient: anything but a mismatch). **Relation**: TRASER's 1st choice / any of its top 5 words for the pair is accepted for one of the human words. **Object**: given the subject and the human word, the object it picks first / any of its top 5 is the human object or an object whose human name the judge accepts for it. Inputs: the real video, another video's input in its place, the video blanked. Context: *fresh* (no earlier relation) or *after its own answer* (its relation list re-opened; missed pairs only). *only real / only another*: pairs right with the real video but not the other input / the other way round. *unjudged*: combinations the judge was never asked, counted as wrong (`python3 tools/interp/judge_pairs.py` asks it).

**Judge.** 2627 words Kimi K3 never judged were judged by claude (NVIDIA retired Kimi K3 on 15 Oct 2026). Check on words Kimi K3 judged: of 100 it accepted, claude also accepts 79; of 100 it rejected, claude also rejects 98. Kimi K3's own verdicts always come first.

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

*Objects on 646 of 835 videos so far (the rest were made before the run saved them).*

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) | same object, exact (real video) |
|---|---|---|---|---|---|---|---|---|
| fresh | all human pairs (8852) | 5742 (65%) | 5397 (61%) | 5239 (59%) | 1155 / 810 | 1151 / 648 | 0 | 3291 (37%) |
| fresh | missed (5168) | 3061 (59%) | 2963 (57%) | 2780 (54%) | 628 / 530 | 686 / 405 | 0 | 1495 (29%) |
| fresh | written (3684) | 2681 (73%) | 2434 (66%) | 2459 (67%) | 527 / 280 | 465 / 243 | 0 | 1796 (49%) |
| after its own answer | missed (5168) | 3202 (62%) | 3086 (60%) | 3058 (59%) | 378 / 262 | 340 / 196 | 0 | 1563 (30%) |

### Object, any of its top 5

*Objects on 646 of 835 videos so far (the rest were made before the run saved them).*

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) | same object, exact (real video) |
|---|---|---|---|---|---|---|---|---|
| fresh | all human pairs (8852) | 8623 (97%) | 8631 (98%) | 8650 (98%) | 91 / 99 | 82 / 109 | 0 | 7821 (88%) |
| fresh | missed (5168) | 4981 (96%) | 4993 (97%) | 5004 (97%) | 66 / 78 | 64 / 87 | 0 | 4365 (84%) |
| fresh | written (3684) | 3642 (99%) | 3638 (99%) | 3646 (99%) | 25 / 21 | 18 / 22 | 0 | 3456 (94%) |
| after its own answer | missed (5168) | 4985 (96%) | 5016 (97%) | 5004 (97%) | 49 / 80 | 45 / 64 | 0 | 4414 (85%) |

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
| adult | adult | 34608 | identical (right) |
| child | child | 7945 | identical (right) |
| child | adult | 5557 | hypernym/hyponym (right, by moonshotai/kimi-k3 (other order)) |
| adult | child | 5296 | hypernym/hyponym (right) |
| adult | chair | 2592 | mismatch (wrong) |
| adult | table | 2122 | mismatch (wrong, by claude) |
| child | table | 1660 | mismatch (wrong, by claude) |
| chair | adult | 1619 | mismatch (wrong, by moonshotai/kimi-k3 (other order)) |
| guitar | adult | 1517 | mismatch (wrong, by claude) |
| adult | car | 1496 | mismatch (wrong) |
| child | toy | 1432 | mismatch (wrong) |
| toy | toy | 1391 | identical (right) |
| child | sofa | 1353 | mismatch (wrong, by moonshotai/kimi-k3 (other order)) |
| adult | guitar | 1347 | mismatch (wrong, by claude) |
| camera | adult | 1314 | mismatch (wrong, by claude) |
| adult | cup | 1271 | mismatch (wrong, by claude) |
| sheep/goat | sheep/goat | 1244 | identical (right) |
| baby | adult | 1071 | mismatch (wrong, by moonshotai/kimi-k3 (other order)) |
| cup | adult | 1052 | mismatch (wrong, by claude) |
| toy | child | 1038 | mismatch (wrong, by moonshotai/kimi-k3 (other order)) |
| table | adult | 1036 | mismatch (wrong, by claude) |
| adult | bottle | 1024 | mismatch (wrong, by claude) |
| dog | dog | 1019 | identical (right) |
| chair | chair | 1016 | identical (right) |
| ball/sports ball | adult | 1010 | mismatch (wrong, by claude) |

816 different combinations, 0 not judged yet; all of them in `judge_check_*.csv`.
