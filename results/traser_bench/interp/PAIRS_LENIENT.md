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

## vidor: 124 videos, 1651 human pairs

### Relation word, TRASER's 1st choice

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) |
|---|---|---|---|---|---|---|---|
| fresh | all human pairs (1651) | 460 (28%) | 361 (22%) | 475 (29%) | 240 / 141 | 164 / 179 | 51 |
| fresh | missed (1009) | 210 (21%) | 171 (17%) | 204 (20%) | 118 / 79 | 90 / 84 | 36 |
| fresh | written (642) | 250 (39%) | 190 (30%) | 271 (42%) | 122 / 62 | 74 / 95 | 15 |
| after its own answer | missed (1009) | 504 (50%) | 465 (46%) | 525 (52%) | 128 / 89 | 83 / 104 | 14 |

### Relation word, any of its top 5

| context | pairs | real video | another video's input | video blanked | only real / only another | only real / only blanked | unjudged (real video) |
|---|---|---|---|---|---|---|---|
| fresh | all human pairs (1651) | 1024 (62%) | 1023 (62%) | 1154 (70%) | 224 / 223 | 139 / 269 | 163 |
| fresh | missed (1009) | 551 (55%) | 560 (56%) | 634 (63%) | 146 / 155 | 100 / 183 | 117 |
| fresh | written (642) | 473 (74%) | 463 (72%) | 520 (81%) | 78 / 68 | 39 / 86 | 46 |
| after its own answer | missed (1009) | 920 (91%) | 903 (89%) | 903 (89%) | 29 / 12 | 27 / 10 | 19 |

### Object, TRASER's 1st choice

*Not available yet: these results were made before the run saved the objects it picks (re-run `pairs_stage.py --phases e2all`; old files are redone automatically).*

### Object, any of its top 5

*Not available yet: these results were made before the run saved the objects it picks (re-run `pairs_stage.py --phases e2all`; old files are redone automatically).*

### Check the judge: relation words, most frequent

| human | TRASER | times | judge (Kimi K3) |
|---|---|---|---|
| next to | in front of | 2318 | mismatch (wrong) |
| in front of | in front of | 1954 | identical (right) |
| next to | approaches | 1617 | mismatch (wrong) |
| next to | near | 1582 | hypernym/hyponym (right) |
| in front of | approaches | 1486 | mismatch (wrong) |
| next to | overlapping | 1312 | mismatch (wrong) |
| next to | above | 1207 | mismatch (wrong) |
| in front of | near | 1176 | hypernym/hyponym (right) |
| next to | next to | 1064 | identical (right) |
| in front of | overlapping | 1028 | semantic overlap (right) |
| next to | behind | 997 | mismatch (wrong) |
| next to | holding | 997 | mismatch (wrong) |
| in front of | approaching | 834 | mismatch (wrong) |
| next to | approaching | 829 | mismatch (wrong) |
| in front of | moves away from | 827 | mismatch (wrong) |
| next to | moves away from | 820 | mismatch (wrong) |
| next to | touching | 797 | semantic overlap (right) |
| behind | in front of | 790 | mismatch (wrong) |
| in front of | behind | 751 | mismatch (wrong) |
| next to | below | 707 | mismatch (wrong) |
| in front of | above | 705 | mismatch (wrong) |
| watch | in front of | 660 | mismatch (wrong) |
| in front of | below | 628 | mismatch (wrong) |
| in front of | next to | 624 | semantic overlap (right) |
| away | in front of | 624 | mismatch (wrong) |

1122 different combinations, 397 not judged yet; all of them in `judge_check_*.csv`.
