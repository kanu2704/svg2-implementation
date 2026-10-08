# svg2test: which object pairs TRASER talks about (10 random videos, seed 0)

TRASER is given the human objects (masks) and writes its own list of relations; it is not told which pairs to describe. Each row is one ordered pair (subject → object) that the humans or TRASER mention.

- **✓ TRASER has this pair**: TRASER wrote at least one relation for the same two objects, same direction
- **✗ TRASER missed this pair**: humans annotated it, TRASER said nothing about these two objects
- **↔ reversed**: TRASER only has the other direction (object → subject); scored as missed
- **⊘ object not given**: one of the two objects was not among the (at most 40) objects TRASER received, so it could not answer; scored as missed, as in the paper's setup
- **+ only TRASER**: TRASER describes a pair the humans did not annotate (ignored by the scores)
- last column, one mark per human relation of the pair: ✓ word right and tIoU > 0.5, ✗ not, ? the judge has not compared the words yet

**Total over these videos:** 280 human pairs, 535 TRASER pairs; 123 in both, 103 missed, 30 reversed, 24 with an object not given, 412 only TRASER.

| video | human pairs | TRASER pairs | pairs in both | missed by TRASER | reversed | object not given | only TRASER |
|---|---|---|---|---|---|---|---|
| [1086_iywqpda7d8k](#1086_iywqpda7d8k) | 16 | 18 | 8 | 4 | 4 | 0 | 10 |
| [1638_MhoaeR88gm4](#1638_mhoaer88gm4) | 10 | 34 | 0 | 7 | 0 | 3 | 34 |
| [1757_0jsMPnghnck](#1757_0jsmpnghnck) | 28 | 44 | 23 | 0 | 5 | 0 | 21 |
| [2225_6acPX_00M9Q](#2225_6acpx_00m9q) | 27 | 47 | 12 | 13 | 2 | 0 | 35 |
| [226_n7YpGfnTqoY](#226_n7ypgfntqoy) | 43 | 46 | 30 | 10 | 3 | 0 | 16 |
| [241_oEkly9vzEGQ](#241_oekly9vzegq) | 27 | 39 | 9 | 15 | 3 | 0 | 30 |
| [285_EP_blwEf2K8](#285_ep_blwef2k8) | 42 | 127 | 6 | 15 | 0 | 21 | 121 |
| [308_7WhzIsqPQW8](#308_7whzisqpqw8) | 36 | 57 | 7 | 26 | 3 | 0 | 50 |
| [670_JboU-y2LdkU](#670_jbou-y2ldku) | 31 | 76 | 21 | 5 | 5 | 0 | 55 |
| [754_TYUV8DYWe8k](#754_tyuv8dywe8k) | 20 | 47 | 7 | 8 | 5 | 0 | 40 |

## 1086_iywqpda7d8k

20.17 s video; humans: 9 objects, 19 relations on 16 pairs; TRASER: 22 relations on 18 pairs.

**Pairs:** 8 in both, 4 missed by TRASER, 4 reversed, 0 with an object TRASER was not given, 10 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 0 | trees | foliage |
| 1 | trees | forest |
| 2 | waterfall | waterfall |
| 3 | plants | bush |
| 4 | trees | tree |
| 5 | trees | forest |
| 6 | sky | clouds |
| 7 | tree | leaves |
| 8 | cliffside | cliff |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| trees #0 → waterfall #2 | in front of [0-21] | in front of [0-20]; below [0-20] | ✓ TRASER has this pair | ✓ |
| trees #0 → sky #6 | below [0-21] | - | ✗ TRASER missed this pair | - |
| trees #1 → sky #6 | below [0-21] | - | ↔ TRASER has it reversed | - |
| waterfall #2 → trees #1 | flows down past [0-21]; in front of [0-21] | flows past [0-20]; in front of [0-20] | ✓ TRASER has this pair | ? ✓ |
| waterfall #2 → sky #6 | below [0-21] | - | ↔ TRASER has it reversed | - |
| waterfall #2 → cliffside #8 | flows down past [17-21]; in front of [17-21] | flows past [18-20] | ✓ TRASER has this pair | ? ? |
| plants #3 → trees #1 | in front of [0-21]; below [0-21] | in front of [0-20] | ✓ TRASER has this pair | ✓ ? |
| plants #3 → waterfall #2 | in front of [0-21] | in front of [0-20]; below [0-20] | ✓ TRASER has this pair | ✓ |
| plants #3 → sky #6 | below [0-21] | - | ✗ TRASER missed this pair | - |
| plants #3 → cliffside #8 | in front of [17-21] | - | ✗ TRASER missed this pair | - |
| trees #4 → waterfall #2 | above [0-21] | behind [0-20] | ✓ TRASER has this pair | ? |
| trees #4 → sky #6 | below [0-21] | - | ✗ TRASER missed this pair | - |
| trees #5 → waterfall #2 | above [0-21] | - | ↔ TRASER has it reversed | - |
| trees #5 → sky #6 | below [0-21] | - | ↔ TRASER has it reversed | - |
| tree #7 → waterfall #2 | in front of [0-11] | in front of [0-12]; below [0-12] | ✓ TRASER has this pair | ✓ |
| cliffside #8 → sky #6 | below [17-21] | below [18-20] | ✓ TRASER has this pair | ✗ |
| trees #0 → trees #1 | - | in front of [0-20] | + only TRASER | - |
| waterfall #2 → trees #0 | - | flows past [0-20] | + only TRASER | - |
| waterfall #2 → plants #3 | - | flows past [0-20] | + only TRASER | - |
| waterfall #2 → trees #5 | - | in front of [0-20] | + only TRASER | - |
| trees #4 → trees #1 | - | in front of [0-20] | + only TRASER | - |
| sky #6 → trees #1 | - | above [0-20] | + only TRASER | - |
| sky #6 → waterfall #2 | - | above [0-20] | + only TRASER | - |
| sky #6 → trees #5 | - | above [0-20] | + only TRASER | - |
| tree #7 → trees #1 | - | in front of [0-12] | + only TRASER | - |
| cliffside #8 → trees #1 | - | in front of [18-20] | + only TRASER | - |


## 1638_MhoaeR88gm4

7.5 s video; humans: 63 objects, 10 relations on 10 pairs; TRASER: 49 relations on 34 pairs.

**Pairs:** 0 in both, 7 missed by TRASER, 0 reversed, 3 with an object TRASER was not given, 34 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 0 | chair | chair |
| 1 | chair | chair |
| 2 | chair | chair |
| 3 | chair | signboard |
| 4 | chair | chair |
| 5 | chair | chair |
| 6 | chair | chair |
| 7 | chair | chair |
| 8 | chair | chair |
| 9 | chair | chair |
| 10 | chair | chair |
| 11 | chair | chair |
| 12 | chair | chair |
| 13 | chair | chair |
| 14 | floor | chair |
| 15 | table | chair |
| 16 | table | chair |
| 17 | table | chair |
| 18 | table | chair |
| 19 | window | signboard |
| 20 | window | window |
| 21 | ceiling | ceiling |
| 22 | towel | chair |
| 23 | towel | chair |
| 24 | towel | chair |
| 25 | towel | chair |
| 26 | window | vent (uncertain) |
| 27 | towel | chair |
| 28 | towel | chair |
| 29 | towel | chair |
| 30 | towel | chair |
| 31 | towel | chair |
| 32 | towel | chair |
| 33 | towel | chair |
| 34 | towel | chair |
| 35 | towel | chair |
| 36 | window | wall panel |
| 37 | exit sign | signboard |
| 38 | counter | signboard |
| 39 | counter | wooden panel |
| 40 | pillar | - (not given to TRASER) |
| 41 | decoration item | - (not given to TRASER) |
| 42 | counter | - (not given to TRASER) |
| 43 | decoration item | - (not given to TRASER) |
| 44 | window | - (not given to TRASER) |
| 45 | window | - (not given to TRASER) |
| 46 | pillar | - (not given to TRASER) |
| 47 | pillar | - (not given to TRASER) |
| 48 | pillar | - (not given to TRASER) |
| 49 | pillar | - (not given to TRASER) |
| 50 | towel | - (not given to TRASER) |
| 51 | logo | - (not given to TRASER) |
| 52 | counter door | - (not given to TRASER) |
| 53 | box | - (not given to TRASER) |
| 54 | box | - (not given to TRASER) |
| 55 | box | - (not given to TRASER) |
| 56 | chair | - (not given to TRASER) |
| 57 | chair | - (not given to TRASER) |
| 58 | poster or logo | - (not given to TRASER) |
| 59 | poster or logo | - (not given to TRASER) |
| 60 | decoration item | - (not given to TRASER) |
| 61 | decoration item | - (not given to TRASER) |
| 62 | poster or logo | - (not given to TRASER) |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| towel #27 → chair #7 | on [4-8] | - | ✗ TRASER missed this pair | - |
| towel #28 → chair #8 | on [4-8] | - | ✗ TRASER missed this pair | - |
| towel #29 → chair #9 | on [5-8] | - | ✗ TRASER missed this pair | - |
| towel #30 → chair #10 | on [5-8] | - | ✗ TRASER missed this pair | - |
| towel #31 → chair #11 | on [3-8] | - | ✗ TRASER missed this pair | - |
| towel #32 → chair #11 | on [2-8] | - | ✗ TRASER missed this pair | - |
| towel #33 → chair #13 | on [0.5-8] | - | ✗ TRASER missed this pair | - |
| box #53 → counter #39 | on [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| box #54 → counter #39 | on [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| box #55 → counter #39 | on [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| chair #0 → ceiling #21 | - | below [5-6] | + only TRASER | - |
| chair #0 → counter #39 | - | in front of [0-4] | + only TRASER | - |
| chair #1 → ceiling #21 | - | below [5-6] | + only TRASER | - |
| chair #1 → counter #39 | - | in front of [0-4] | + only TRASER | - |
| chair #3 → counter #39 | - | above [0-3] | + only TRASER | - |
| chair #5 → ceiling #21 | - | below [5-6] | + only TRASER | - |
| chair #5 → counter #39 | - | in front of [0-5] | + only TRASER | - |
| chair #6 → ceiling #21 | - | below [5-6] | + only TRASER | - |
| chair #6 → counter #39 | - | in front of [0-5] | + only TRASER | - |
| chair #11 → ceiling #21 | - | below [5-8]; below [5-8] | + only TRASER | - |
| chair #12 → ceiling #21 | - | below [5-8]; below [5-8] | + only TRASER | - |
| chair #13 → ceiling #21 | - | below [5-8]; below [5-8] | + only TRASER | - |
| floor #14 → ceiling #21 | - | below [5-8]; below [5-8] | + only TRASER | - |
| floor #14 → counter #39 | - | in front of [0-8] | + only TRASER | - |
| table #17 → ceiling #21 | - | below [5-8]; below [5-8] | + only TRASER | - |
| table #17 → counter #39 | - | in front of [0-8] | + only TRASER | - |
| table #18 → ceiling #21 | - | below [5-8]; below [5-8] | + only TRASER | - |
| window #19 → ceiling #21 | - | below [5-8] | + only TRASER | - |
| window #19 → counter #39 | - | above [0-8] | + only TRASER | - |
| window #20 → ceiling #21 | - | below [5-8] | + only TRASER | - |
| window #20 → counter #39 | - | above [0-8] | + only TRASER | - |
| towel #27 → ceiling #21 | - | below [5-8]; below [5-8] | + only TRASER | - |
| towel #28 → ceiling #21 | - | below [5-8]; below [5-8] | + only TRASER | - |
| towel #29 → ceiling #21 | - | below [5-8]; below [5-8] | + only TRASER | - |
| towel #30 → ceiling #21 | - | below [5-8]; below [5-8] | + only TRASER | - |
| towel #31 → ceiling #21 | - | below [5-8]; below [5-8] | + only TRASER | - |
| towel #32 → ceiling #21 | - | below [5-8]; below [5-8] | + only TRASER | - |
| towel #33 → ceiling #21 | - | below [5-8]; below [5-8] | + only TRASER | - |
| towel #34 → ceiling #21 | - | below [5-8]; below [5-8] | + only TRASER | - |
| towel #35 → ceiling #21 | - | below [5-8]; below [5-8] | + only TRASER | - |
| window #36 → ceiling #21 | - | below [5-8] | + only TRASER | - |
| exit sign #37 → ceiling #21 | - | below [5-8] | + only TRASER | - |
| counter #38 → counter #39 | - | above [0-4] | + only TRASER | - |
| counter #39 → ceiling #21 | - | below [5-8] | + only TRASER | - |


## 1757_0jsMPnghnck

7.33 s video; humans: 23 objects, 28 relations on 28 pairs; TRASER: 44 relations on 44 pairs.

**Pairs:** 23 in both, 0 missed by TRASER, 5 reversed, 0 with an object TRASER was not given, 21 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 0 | sky | sky |
| 1 | ground | terrain |
| 2 | road | road |
| 3 | building | building |
| 4 | house | house |
| 5 | house | building |
| 6 | house | building |
| 7 | house | tree |
| 8 | house | tree |
| 9 | house | tree |
| 10 | sand | golf hole |
| 11 | swimming pool | swimming pool |
| 12 | tree | tree |
| 13 | tree | tree |
| 14 | tree | tree |
| 15 | tree | tree |
| 16 | tree | tree |
| 17 | tree | tree |
| 18 | tree | tree |
| 19 | tree | tree |
| 20 | tree | tree |
| 21 | tree | house |
| 22 | tree | tree |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| sky #0 → ground #1 | above [0-8] | above [0-8] | ✓ TRASER has this pair | ✓ |
| road #2 → ground #1 | on [0-5] | on [0-3] | ✓ TRASER has this pair | ✓ |
| building #3 → ground #1 | on [0-5] | on [0-3] | ✓ TRASER has this pair | ✓ |
| house #4 → ground #1 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| house #5 → ground #1 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| house #6 → ground #1 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| house #7 → ground #1 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| house #8 → ground #1 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| house #9 → ground #1 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| sand #10 → ground #1 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| swimming pool #11 → ground #1 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| swimming pool #11 → house #5 | next to [0-8] | near [0-8] | ✓ TRASER has this pair | ✓ |
| tree #12 → ground #1 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| tree #12 → swimming pool #11 | next to [0-8] | - | ↔ TRASER has it reversed | - |
| tree #13 → ground #1 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| tree #13 → swimming pool #11 | next to [0-8] | - | ↔ TRASER has it reversed | - |
| tree #14 → ground #1 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| tree #14 → swimming pool #11 | next to [0-8] | - | ↔ TRASER has it reversed | - |
| tree #15 → ground #1 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| tree #15 → swimming pool #11 | next to [0-8] | - | ↔ TRASER has it reversed | - |
| tree #16 → ground #1 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| tree #16 → swimming pool #11 | next to [0-8] | - | ↔ TRASER has it reversed | - |
| tree #17 → ground #1 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| tree #18 → ground #1 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| tree #19 → ground #1 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| tree #20 → ground #1 | on [4.5-7] | on [0-5] | ✓ TRASER has this pair | ✗ |
| tree #21 → ground #1 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| tree #22 → ground #1 | on [0-4] | on [0-3] | ✓ TRASER has this pair | ✓ |
| road #2 → tree #22 | - | near [0-3] | + only TRASER | - |
| building #3 → road #2 | - | near [0-3] | + only TRASER | - |
| building #3 → tree #22 | - | near [0-3] | + only TRASER | - |
| sand #10 → swimming pool #11 | - | near [0-8] | + only TRASER | - |
| swimming pool #11 → sky #0 | - | near [0-8] | + only TRASER | - |
| swimming pool #11 → house #4 | - | near [0-8] | + only TRASER | - |
| swimming pool #11 → house #6 | - | near [0-8] | + only TRASER | - |
| swimming pool #11 → house #7 | - | near [0-8] | + only TRASER | - |
| swimming pool #11 → house #8 | - | near [0-8] | + only TRASER | - |
| swimming pool #11 → house #9 | - | near [0-8] | + only TRASER | - |
| swimming pool #11 → tree #12 | - | near [0-8] | + only TRASER | - |
| swimming pool #11 → tree #13 | - | near [0-8] | + only TRASER | - |
| swimming pool #11 → tree #14 | - | near [0-8] | + only TRASER | - |
| swimming pool #11 → tree #15 | - | near [0-8] | + only TRASER | - |
| swimming pool #11 → tree #16 | - | near [0-8] | + only TRASER | - |
| swimming pool #11 → tree #17 | - | near [0-8] | + only TRASER | - |
| swimming pool #11 → tree #18 | - | near [0-8] | + only TRASER | - |
| swimming pool #11 → tree #19 | - | near [0-8] | + only TRASER | - |
| swimming pool #11 → tree #20 | - | near [0-5] | + only TRASER | - |
| swimming pool #11 → tree #21 | - | near [0-8] | + only TRASER | - |
| swimming pool #11 → tree #22 | - | near [0-3] | + only TRASER | - |


## 2225_6acPX_00M9Q

15.0 s video; humans: 19 objects, 38 relations on 27 pairs; TRASER: 49 relations on 47 pairs.

**Pairs:** 12 in both, 13 missed by TRASER, 2 reversed, 0 with an object TRASER was not given, 35 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 0 | rail signal | traffic light |
| 1 | warning sign board | signboard |
| 2 | mountains | mountain |
| 3 | ground | snow |
| 4 | sky | sky |
| 5 | mountain | mountain |
| 6 | train | train |
| 7 | ground | snow |
| 8 | barrier wall | snow |
| 9 | snow | smoke |
| 10 | ground | snow |
| 11 | roof | snow |
| 12 | sign board | signboard |
| 13 | sign board | signboard |
| 14 | sign board | signboard |
| 15 | light | traffic light |
| 16 | light | traffic light |
| 17 | light | headlight |
| 18 | window | window |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| rail signal #0 → ground #3 | on [0-16] | above [0-15] | ✓ TRASER has this pair | ✓ |
| rail signal #0 → train #6 | in front of [0-11] | in front of [0-15] | ✓ TRASER has this pair | ✓ |
| rail signal #0 → barrier wall #8 | in front of [0-15] | - | ✗ TRASER missed this pair | - |
| warning sign board #1 → rail signal #0 | below [4-13] | - | ✗ TRASER missed this pair | - |
| warning sign board #1 → ground #3 | on [4-13] | above [4-11] | ✓ TRASER has this pair | ✓ |
| warning sign board #1 → barrier wall #8 | attached to [3.5-13.5] | - | ✗ TRASER missed this pair | - |
| mountains #2 → ground #3 | above [0-15] | - | ↔ TRASER has it reversed | - |
| sky #4 → mountains #2 | above [4-15] | above [4-15] | ✓ TRASER has this pair | ✓ |
| train #6 → rail signal #0 | approaches [0-10]; passes [9-16] | moving past [0-15] | ✓ TRASER has this pair | ? ? |
| train #6 → mountains #2 | in front of [0-15] | traveling through [0-15]; in front of [0-15] | ✓ TRASER has this pair | ✓ |
| train #6 → ground #3 | on [0-15] | moving on [0-15]; on [0-15] | ✓ TRASER has this pair | ✓ |
| train #6 → sky #4 | below [3.5-16] | - | ↔ TRASER has it reversed | - |
| train #6 → barrier wall #8 | moves past [0-15] | - | ✗ TRASER missed this pair | - |
| train #6 → snow #9 | clears [0-15]; moves through [0-16] | moving past [0-15] | ✓ TRASER has this pair | ? ? |
| barrier wall #8 → ground #3 | on [0-15] | - | ✗ TRASER missed this pair | - |
| snow #9 → ground #3 | on [0-16]; covers [0-15] | above [0-15] | ✓ TRASER has this pair | ✓ ? |
| snow #9 → train #6 | in front of [0-15]; moves away from [0-16] | in front of [0-15] | ✓ TRASER has this pair | ✓ ? |
| sign board #12 → rail signal #0 | on [0-15]; attached to [0-15] | - | ✗ TRASER missed this pair | - - |
| sign board #12 → sign board #13 | above [0-15] | - | ✗ TRASER missed this pair | - |
| sign board #13 → rail signal #0 | on [0-15]; attached to [0-15] | - | ✗ TRASER missed this pair | - - |
| sign board #13 → sign board #14 | above [0-15] | - | ✗ TRASER missed this pair | - |
| sign board #14 → rail signal #0 | on [0-15]; attached to [0-15] | - | ✗ TRASER missed this pair | - - |
| light #15 → rail signal #0 | on [0-15]; attached to [0-15] | - | ✗ TRASER missed this pair | - - |
| light #16 → rail signal #0 | on [4-15]; attached to [0-15] | - | ✗ TRASER missed this pair | - - |
| light #16 → light #15 | above [3.5-16] | - | ✗ TRASER missed this pair | - |
| light #17 → train #6 | on [0-14]; attached to [0-14] | on [0-2, 10-15] | ✓ TRASER has this pair | ✗ ? |
| window #18 → train #6 | on [0-14]; attached to [0-14] | on [0-2, 10-15] | ✓ TRASER has this pair | ✗ ? |
| rail signal #0 → mountains #2 | - | in front of [0-15] | + only TRASER | - |
| warning sign board #1 → mountains #2 | - | in front of [4-11] | + only TRASER | - |
| warning sign board #1 → train #6 | - | in front of [4-11] | + only TRASER | - |
| ground #3 → mountains #2 | - | below [0-15] | + only TRASER | - |
| sky #4 → train #6 | - | above [4-15] | + only TRASER | - |
| train #6 → warning sign board #1 | - | moving past [4-11] | + only TRASER | - |
| train #6 → sign board #12 | - | moving past [0-2] | + only TRASER | - |
| train #6 → sign board #13 | - | moving past [0-2] | + only TRASER | - |
| train #6 → sign board #14 | - | moving past [0-2, 10-12] | + only TRASER | - |
| train #6 → light #15 | - | moving past [0-15] | + only TRASER | - |
| train #6 → light #16 | - | moving past [0-15] | + only TRASER | - |
| train #6 → light #17 | - | moving past [0-2, 10-15] | + only TRASER | - |
| train #6 → window #18 | - | moving past [0-2, 10-15] | + only TRASER | - |
| ground #7 → mountains #2 | - | below [0-2, 4-8] | + only TRASER | - |
| barrier wall #8 → mountains #2 | - | below [0-15] | + only TRASER | - |
| ground #10 → mountains #2 | - | below [4-15] | + only TRASER | - |
| roof #11 → mountains #2 | - | below [0-2] | + only TRASER | - |
| sign board #12 → mountains #2 | - | in front of [0-2] | + only TRASER | - |
| sign board #12 → ground #3 | - | above [0-2] | + only TRASER | - |
| sign board #12 → train #6 | - | in front of [0-2] | + only TRASER | - |
| sign board #13 → mountains #2 | - | in front of [0-2] | + only TRASER | - |
| sign board #13 → ground #3 | - | above [0-2] | + only TRASER | - |
| sign board #13 → train #6 | - | in front of [0-2] | + only TRASER | - |
| sign board #14 → mountains #2 | - | in front of [0-2, 10-12] | + only TRASER | - |
| sign board #14 → ground #3 | - | above [0-2, 10-12] | + only TRASER | - |
| sign board #14 → train #6 | - | in front of [0-2, 10-12] | + only TRASER | - |
| light #15 → mountains #2 | - | in front of [0-15] | + only TRASER | - |
| light #15 → ground #3 | - | above [0-15] | + only TRASER | - |
| light #15 → train #6 | - | in front of [0-15] | + only TRASER | - |
| light #16 → mountains #2 | - | in front of [0-15] | + only TRASER | - |
| light #16 → ground #3 | - | above [0-15] | + only TRASER | - |
| light #16 → train #6 | - | in front of [0-15] | + only TRASER | - |
| light #17 → ground #3 | - | above [0-2, 10-15] | + only TRASER | - |
| window #18 → ground #3 | - | above [0-2, 10-15] | + only TRASER | - |
| window #18 → light #17 | - | above [0-2, 10-15] | + only TRASER | - |


## 226_n7YpGfnTqoY

6.33 s video; humans: 20 objects, 51 relations on 43 pairs; TRASER: 51 relations on 46 pairs.

**Pairs:** 30 in both, 10 missed by TRASER, 3 reversed, 0 with an object TRASER was not given, 16 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 0 | car | car |
| 1 | road | road |
| 2 | grass | grass |
| 3 | sidewalk | curb |
| 4 | road | lane separator |
| 5 | license plate | license plate |
| 6 | windshield | windshield |
| 7 | headlight | headlight |
| 8 | headlight | headlight |
| 9 | grill | grille |
| 10 | driver | rearview mirror |
| 11 | bonnet | car hood |
| 12 | car logo | emblem |
| 13 | fog light | vent |
| 14 | fog light | vent |
| 15 | front bumper | bumper |
| 16 | wiper | windshield wiper |
| 17 | cooling system | vent |
| 18 | side mirror | rearview mirror |
| 19 | tree | pole |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| car #0 → road #1 | on [0-7]; moving along [0-7]; traveling on [0-7] | moving on [0-6]; driving along [0-6]; on [0-6] | ✓ TRASER has this pair | ✓ ? ? |
| car #0 → grass #2 | in front of [0-7]; moving past [0-7] | passing [0-6]; in front of [0-6] | ✓ TRASER has this pair | ✓ ? |
| car #0 → sidewalk #3 | in front of [0-7]; moving past [0-7] | passing [0-6]; in front of [0-6] | ✓ TRASER has this pair | ✓ ? |
| car #0 → license plate #5 | has attached [0-7] | has [5-6] | ✓ TRASER has this pair | ? |
| car #0 → headlight #7 | has attached [0-7] | has [0-6] | ✓ TRASER has this pair | ? |
| car #0 → headlight #8 | has attached [0-7] | has [0-6] | ✓ TRASER has this pair | ? |
| car #0 → grill #9 | has attached [0-7] | has [0-6] | ✓ TRASER has this pair | ? |
| car #0 → bonnet #11 | has attached [0-7] | has [0-6] | ✓ TRASER has this pair | ? |
| car #0 → car logo #12 | has attached [0-7] | has [0-6] | ✓ TRASER has this pair | ? |
| car #0 → fog light #13 | has attached [0-7] | has [0-6] | ✓ TRASER has this pair | ? |
| car #0 → fog light #14 | has attached [0-7] | has [0-6] | ✓ TRASER has this pair | ? |
| car #0 → front bumper #15 | has attached [0-7] | has [0-6] | ✓ TRASER has this pair | ? |
| car #0 → wiper #16 | has attached [0-7] | has [0-6] | ✓ TRASER has this pair | ? |
| car #0 → side mirror #18 | has attached [0-7] | has [0-6] | ✓ TRASER has this pair | ? |
| car #0 → tree #19 | moving past [1.5-7]; in front of [2-7] | passing [0-6]; in front of [0-6] | ✓ TRASER has this pair | ? ✓ |
| road #1 → sidewalk #3 | beside [0-7]; beside [0-7] | - | ↔ TRASER has it reversed | - - |
| sidewalk #3 → grass #2 | beside [0-7] | - | ↔ TRASER has it reversed | - |
| road #4 → road #1 | beside [6-7] | on [5-6] | ✓ TRASER has this pair | ? |
| license plate #5 → car #0 | on [4-7] | on [5-6] | ✓ TRASER has this pair | ✗ |
| license plate #5 → grill #9 | below [4-7] | - | ✗ TRASER missed this pair | - |
| license plate #5 → front bumper #15 | on [4-7] | - | ✗ TRASER missed this pair | - |
| windshield #6 → car #0 | on [0-7] | on [0-6] | ✓ TRASER has this pair | ✓ |
| headlight #7 → car #0 | on [0-7] | on [0-6] | ✓ TRASER has this pair | ✓ |
| headlight #7 → fog light #13 | above [0-7] | - | ✗ TRASER missed this pair | - |
| headlight #8 → car #0 | on [0-7] | on [0-6] | ✓ TRASER has this pair | ✓ |
| headlight #8 → fog light #14 | above [0-7] | - | ✗ TRASER missed this pair | - |
| grill #9 → car #0 | on [0-7] | on [0-6] | ✓ TRASER has this pair | ✓ |
| grill #9 → front bumper #15 | above [0-7] | - | ↔ TRASER has it reversed | - |
| driver #10 → car #0 | driving [0-7]; inside [0-7] | on [0-6] | ✓ TRASER has this pair | ? ? |
| driver #10 → windshield #6 | behind [0-7] | - | ✗ TRASER missed this pair | - |
| bonnet #11 → car #0 | on [0-7] | on [0-6] | ✓ TRASER has this pair | ✓ |
| bonnet #11 → front bumper #15 | above [0-7] | - | ✗ TRASER missed this pair | - |
| car logo #12 → grill #9 | attached to [0-7]; on [0-7] | above [0-6] | ✓ TRASER has this pair | ? ✓ |
| fog light #13 → car #0 | on [0-7] | on [0-6] | ✓ TRASER has this pair | ✓ |
| fog light #13 → headlight #7 | below [0-7] | - | ✗ TRASER missed this pair | - |
| fog light #14 → car #0 | on [0-7] | on [0-6] | ✓ TRASER has this pair | ✓ |
| fog light #14 → grill #9 | below [0-7] | below [0-6] | ✓ TRASER has this pair | ✓ |
| front bumper #15 → car #0 | on [0-7] | on [0-6] | ✓ TRASER has this pair | ✓ |
| wiper #16 → car #0 | on [0-7] | on [0-6] | ✓ TRASER has this pair | ✓ |
| wiper #16 → windshield #6 | below [0-7] | - | ✗ TRASER missed this pair | - |
| side mirror #18 → car #0 | on [0-7] | on [0-6] | ✓ TRASER has this pair | ✓ |
| tree #19 → grass #2 | on [2-7] | - | ✗ TRASER missed this pair | - |
| tree #19 → sidewalk #3 | behind [2-7] | - | ✗ TRASER missed this pair | - |
| car #0 → windshield #6 | - | has [0-6] | + only TRASER | - |
| car #0 → driver #10 | - | has [0-6] | + only TRASER | - |
| car #0 → cooling system #17 | - | has [0-6] | + only TRASER | - |
| grass #2 → sidewalk #3 | - | adjacent to [0-6] | + only TRASER | - |
| sidewalk #3 → road #1 | - | adjacent to [0-6] | + only TRASER | - |
| headlight #7 → front bumper #15 | - | above [0-6] | + only TRASER | - |
| headlight #8 → front bumper #15 | - | above [0-6] | + only TRASER | - |
| grill #9 → bonnet #11 | - | below [0-6] | + only TRASER | - |
| driver #10 → grill #9 | - | above [0-6] | + only TRASER | - |
| car logo #12 → car #0 | - | on [0-6] | + only TRASER | - |
| fog light #13 → grill #9 | - | below [0-6] | + only TRASER | - |
| front bumper #15 → grill #9 | - | below [0-6] | + only TRASER | - |
| wiper #16 → grill #9 | - | above [0-6] | + only TRASER | - |
| cooling system #17 → car #0 | - | on [0-6] | + only TRASER | - |
| cooling system #17 → grill #9 | - | below [0-6] | + only TRASER | - |
| side mirror #18 → grill #9 | - | above [0-6] | + only TRASER | - |


## 241_oEkly9vzEGQ

12.67 s video; humans: 26 objects, 31 relations on 27 pairs; TRASER: 41 relations on 39 pairs.

**Pairs:** 9 in both, 15 missed by TRASER, 3 reversed, 0 with an object TRASER was not given, 30 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 0 | person | person |
| 1 | bench | bench |
| 2 | ground | person |
| 3 | fountain | fountain |
| 4 | street | car |
| 5 | building | pole (uncertain) |
| 6 | building | tree |
| 7 | building | wall |
| 8 | car | car |
| 9 | car | car |
| 10 | car | car |
| 11 | tree | tree |
| 12 | garagecan | flowerpot |
| 13 | building | building |
| 14 | parking sign | car |
| 15 | bag | handbag |
| 16 | hair | hair |
| 17 | coat | jacket |
| 18 | shoes | high heel shoe |
| 19 | tree | tree |
| 20 | tree | tree |
| 21 | bush | bush |
| 22 | bush | trash can (uncertain) |
| 23 | bush | bush |
| 24 | plant | plant |
| 25 | plant | potted plant |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| person #0 → bench #1 | in front of [0-13] | in front of [0-14] | ✓ TRASER has this pair | ✓ |
| person #0 → ground #2 | on [0-13]; walking across [0-13] | - | ✗ TRASER missed this pair | - - |
| person #0 → fountain #3 | behind [0-13]; beside [0-13]; approaching [0-13] | looking at [0-14]; approaching [0-14]; near [0-14] | ✓ TRASER has this pair | ? ? ✓ |
| person #0 → building #7 | in front of [0-13] | in front of [0-14] | ✓ TRASER has this pair | ✓ |
| person #0 → bag #15 | carrying [0-13] | carrying [0-14] | ✓ TRASER has this pair | ✓ |
| person #0 → coat #17 | wearing [0-13] | wearing [0-14] | ✓ TRASER has this pair | ✓ |
| person #0 → shoes #18 | wearing [0-13] | wearing [0-14] | ✓ TRASER has this pair | ✓ |
| bench #1 → ground #2 | on [0-13] | - | ✗ TRASER missed this pair | - |
| bench #1 → fountain #3 | behind [0-13]; beside [0-13] | - | ✗ TRASER missed this pair | - - |
| bench #1 → building #7 | in front of [0-13] | in front of [0-14] | ✓ TRASER has this pair | ✓ |
| fountain #3 → ground #2 | on [0-13] | - | ✗ TRASER missed this pair | - |
| fountain #3 → building #13 | in front of [4-13] | in front of [4-14] | ✓ TRASER has this pair | ✓ |
| car #9 → ground #2 | on [0-13] | - | ✗ TRASER missed this pair | - |
| car #9 → fountain #3 | behind [0-13] | - | ↔ TRASER has it reversed | - |
| car #9 → building #13 | in front of [0-13] | in front of [4-14] | ✓ TRASER has this pair | ✓ |
| car #10 → ground #2 | on [0-13] | - | ✗ TRASER missed this pair | - |
| car #10 → fountain #3 | behind [0-13] | - | ↔ TRASER has it reversed | - |
| tree #11 → ground #2 | on [0-13] | - | ✗ TRASER missed this pair | - |
| tree #11 → fountain #3 | behind [0-13] | - | ↔ TRASER has it reversed | - |
| garagecan #12 → ground #2 | on [0-13] | - | ✗ TRASER missed this pair | - |
| garagecan #12 → fountain #3 | behind [0-13] | - | ✗ TRASER missed this pair | - |
| bag #15 → shoes #18 | above [0-13] | - | ✗ TRASER missed this pair | - |
| hair #16 → bag #15 | above [0-13] | - | ✗ TRASER missed this pair | - |
| hair #16 → coat #17 | above [0-13] | - | ✗ TRASER missed this pair | - |
| coat #17 → shoes #18 | above [0-13] | - | ✗ TRASER missed this pair | - |
| plant #24 → ground #2 | on [5-13] | - | ✗ TRASER missed this pair | - |
| plant #25 → ground #2 | on [10-13] | - | ✗ TRASER missed this pair | - |
| person #0 → tree #11 | - | in front of [0-14] | + only TRASER | - |
| person #0 → building #13 | - | in front of [4-14] | + only TRASER | - |
| bench #1 → tree #11 | - | in front of [0-14] | + only TRASER | - |
| bench #1 → building #13 | - | in front of [4-14] | + only TRASER | - |
| fountain #3 → car #9 | - | in front of [0-14] | + only TRASER | - |
| fountain #3 → car #10 | - | in front of [0-14] | + only TRASER | - |
| fountain #3 → tree #11 | - | in front of [0-14] | + only TRASER | - |
| fountain #3 → parking sign #14 | - | in front of [4-14] | + only TRASER | - |
| street #4 → building #7 | - | in front of [0-14] | + only TRASER | - |
| building #6 → building #7 | - | in front of [0-4] | + only TRASER | - |
| car #8 → building #7 | - | in front of [0-7] | + only TRASER | - |
| car #9 → bench #1 | - | behind [0-14] | + only TRASER | - |
| car #10 → bench #1 | - | behind [0-14] | + only TRASER | - |
| car #10 → building #13 | - | in front of [4-14] | + only TRASER | - |
| garagecan #12 → tree #11 | - | in front of [0-14] | + only TRASER | - |
| garagecan #12 → building #13 | - | in front of [4-14] | + only TRASER | - |
| parking sign #14 → bench #1 | - | behind [4-14] | + only TRASER | - |
| parking sign #14 → building #13 | - | in front of [4-14] | + only TRASER | - |
| bag #15 → person #0 | - | overlapping [0-14] | + only TRASER | - |
| hair #16 → person #0 | - | overlapping [0-14] | + only TRASER | - |
| coat #17 → person #0 | - | overlapping [0-14] | + only TRASER | - |
| shoes #18 → person #0 | - | below [0-14] | + only TRASER | - |
| shoes #18 → bench #1 | - | in front of [0-14] | + only TRASER | - |
| shoes #18 → fountain #3 | - | near [0-14] | + only TRASER | - |
| tree #19 → building #7 | - | in front of [0-14] | + only TRASER | - |
| tree #20 → building #7 | - | in front of [0-14] | + only TRASER | - |
| bush #21 → building #7 | - | in front of [0-14] | + only TRASER | - |
| bush #23 → building #13 | - | in front of [4-14] | + only TRASER | - |
| plant #24 → building #13 | - | in front of [4-14] | + only TRASER | - |
| plant #25 → building #13 | - | in front of [4-14] | + only TRASER | - |


## 285_EP_blwEf2K8

7.5 s video; humans: 58 objects, 50 relations on 42 pairs; TRASER: 127 relations on 127 pairs.

**Pairs:** 6 in both, 15 missed by TRASER, 0 reversed, 21 with an object TRASER was not given, 121 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 0 | boat | raft |
| 1 | bucket | person |
| 2 | bucket | person |
| 3 | bucket | life jacket (uncertain) |
| 4 | person | person |
| 5 | person | person |
| 6 | person | person |
| 7 | person | person |
| 8 | pool | raft |
| 9 | person | person |
| 10 | person | person |
| 11 | bucket | person |
| 12 | bucket | life jacket (uncertain) |
| 13 | wall | wall |
| 14 | wall | pillar |
| 15 | wall | pillar |
| 16 | floor | wall |
| 17 | swim ring | signboard |
| 18 | wall | brick wall |
| 19 | grass | pole (uncertain) |
| 20 | person | person |
| 21 | person | person |
| 22 | window | window |
| 23 | storage reel | ladder |
| 24 | floatation device | pillar |
| 25 | poolside step | ladder |
| 26 | door | window |
| 27 | window | window |
| 28 | chair | vent (uncertain) |
| 29 | door | door |
| 30 | shelf | vent (uncertain) |
| 31 | poolside step | fan |
| 32 | fan | fan |
| 33 | storage reel center | ladder |
| 34 | wheel | ladder |
| 35 | wheel | ladder |
| 36 | tyre | person |
| 37 | tyre | person |
| 38 | tyre | trash can (uncertain) |
| 39 | tyre | trash can (uncertain) |
| 40 | head | - (not given to TRASER) |
| 41 | head | - (not given to TRASER) |
| 42 | head | - (not given to TRASER) |
| 43 | head | - (not given to TRASER) |
| 44 | head | - (not given to TRASER) |
| 45 | head | - (not given to TRASER) |
| 46 | head | - (not given to TRASER) |
| 47 | life jacket | - (not given to TRASER) |
| 48 | life jacket | - (not given to TRASER) |
| 49 | life jacket | - (not given to TRASER) |
| 50 | life jacket | - (not given to TRASER) |
| 51 | life jacket | - (not given to TRASER) |
| 52 | life jacket | - (not given to TRASER) |
| 53 | life jacket | - (not given to TRASER) |
| 54 | shirt | - (not given to TRASER) |
| 55 | shirt | - (not given to TRASER) |
| 56 | shirt | - (not given to TRASER) |
| 57 | short | - (not given to TRASER) |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| boat #0 → pool #8 | moving on [0-8]; in [0-8] | - | ✗ TRASER missed this pair | - - |
| boat #0 → wall #13 | in front of [0-8] | in front of [0-9] | ✓ TRASER has this pair | ✓ |
| bucket #1 → boat #0 | in [0-8] | inside [0-9] | ✓ TRASER has this pair | ? |
| bucket #3 → boat #0 | in [3-5, 6-8] | - | ✗ TRASER missed this pair | - |
| person #4 → boat #0 | aboard [0-8]; in [0-8] | inside [0-9] | ✓ TRASER has this pair | ? ? |
| person #4 → bucket #1 | holding [0-8] | - | ✗ TRASER missed this pair | - |
| person #4 → life jacket #48 | wearing [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| person #5 → boat #0 | aboard [0-8]; in [0-8] | inside [0-9] | ✓ TRASER has this pair | ? ? |
| person #5 → bucket #2 | splashing with [1-3]; holding [0-8] | - | ✗ TRASER missed this pair | - - |
| person #5 → life jacket #49 | wearing [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| person #6 → boat #0 | aboard [0-8]; in [0-8] | inside [0-9] | ✓ TRASER has this pair | ? ? |
| person #6 → bucket #3 | holding [0-8]; splashing with [4.5-7] | - | ✗ TRASER missed this pair | - - |
| person #6 → life jacket #51 | wearing [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| person #7 → boat #0 | aboard [0-8]; in [0-8] | inside [0-9] | ✓ TRASER has this pair | ? ? |
| person #7 → life jacket #50 | wearing [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| person #9 → bucket #11 | holding [0-1, 2-8]; splashing with [2-5] | - | ✗ TRASER missed this pair | - - |
| person #9 → life jacket #53 | wearing [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| person #10 → life jacket #52 | wearing [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| swim ring #17 → wall #13 | on [0-8] | - | ✗ TRASER missed this pair | - |
| storage reel #23 → window #22 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| poolside step #25 → pool #8 | beside [0-8] | - | ✗ TRASER missed this pair | - |
| chair #28 → floor #16 | on [0-5] | - | ✗ TRASER missed this pair | - |
| poolside step #31 → pool #8 | beside [2-8] | - | ✗ TRASER missed this pair | - |
| fan #32 → floor #16 | on [3-8] | - | ✗ TRASER missed this pair | - |
| storage reel center #33 → storage reel #23 | on [0-8] | - | ✗ TRASER missed this pair | - |
| wheel #34 → storage reel #23 | on [0-8] | - | ✗ TRASER missed this pair | - |
| wheel #35 → storage reel #23 | on [0-8] | - | ✗ TRASER missed this pair | - |
| head #40 → person #4 | on [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| head #41 → person #5 | on [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| head #42 → person #9 | on [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| head #43 → person #10 | on [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| head #44 → person #6 | on [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| head #45 → person #7 | on [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| life jacket #48 → person #4 | on [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| life jacket #49 → person #5 | on [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| life jacket #50 → person #7 | on [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| life jacket #51 → person #6 | on [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| life jacket #52 → person #10 | on [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| life jacket #53 → person #9 | on [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| shirt #54 → person #4 | on [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| shirt #55 → person #7 | on [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| shirt #56 → person #6 | on [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| boat #0 → wall #14 | - | in front of [0-9] | + only TRASER | - |
| boat #0 → wall #15 | - | in front of [0-9] | + only TRASER | - |
| boat #0 → floor #16 | - | in front of [0-9] | + only TRASER | - |
| boat #0 → window #22 | - | in front of [0-9] | + only TRASER | - |
| boat #0 → storage reel #23 | - | in front of [0-9] | + only TRASER | - |
| boat #0 → floatation device #24 | - | in front of [0-9] | + only TRASER | - |
| boat #0 → door #29 | - | in front of [4-9] | + only TRASER | - |
| boat #0 → poolside step #31 | - | in front of [3-9] | + only TRASER | - |
| boat #0 → fan #32 | - | in front of [4-9] | + only TRASER | - |
| bucket #1 → wall #13 | - | in front of [0-9] | + only TRASER | - |
| bucket #1 → swim ring #17 | - | in front of [0-9] | + only TRASER | - |
| bucket #1 → wall #18 | - | in front of [0-2] | + only TRASER | - |
| bucket #1 → window #22 | - | in front of [0-9] | + only TRASER | - |
| bucket #1 → storage reel #23 | - | in front of [0-9] | + only TRASER | - |
| bucket #1 → door #29 | - | in front of [4-9] | + only TRASER | - |
| bucket #1 → poolside step #31 | - | in front of [3-9] | + only TRASER | - |
| bucket #1 → fan #32 | - | in front of [4-9] | + only TRASER | - |
| bucket #2 → boat #0 | - | inside [0-9] | + only TRASER | - |
| bucket #2 → wall #13 | - | in front of [0-9] | + only TRASER | - |
| bucket #2 → swim ring #17 | - | in front of [0-9] | + only TRASER | - |
| bucket #2 → wall #18 | - | in front of [0-2] | + only TRASER | - |
| bucket #2 → window #22 | - | in front of [0-9] | + only TRASER | - |
| bucket #2 → storage reel #23 | - | in front of [0-9] | + only TRASER | - |
| bucket #2 → door #29 | - | in front of [4-9] | + only TRASER | - |
| bucket #2 → poolside step #31 | - | in front of [3-9] | + only TRASER | - |
| bucket #2 → fan #32 | - | in front of [4-9] | + only TRASER | - |
| person #4 → wall #13 | - | in front of [0-9] | + only TRASER | - |
| person #4 → swim ring #17 | - | in front of [0-9] | + only TRASER | - |
| person #4 → wall #18 | - | in front of [0-2] | + only TRASER | - |
| person #4 → window #22 | - | in front of [0-9] | + only TRASER | - |
| person #4 → storage reel #23 | - | in front of [0-9] | + only TRASER | - |
| person #4 → door #29 | - | in front of [4-9] | + only TRASER | - |
| person #4 → poolside step #31 | - | in front of [3-9] | + only TRASER | - |
| person #4 → fan #32 | - | in front of [4-9] | + only TRASER | - |
| person #5 → wall #13 | - | in front of [0-9] | + only TRASER | - |
| person #5 → swim ring #17 | - | in front of [0-9] | + only TRASER | - |
| person #5 → wall #18 | - | in front of [0-2] | + only TRASER | - |
| person #5 → window #22 | - | in front of [0-9] | + only TRASER | - |
| person #5 → storage reel #23 | - | in front of [0-9] | + only TRASER | - |
| person #5 → door #29 | - | in front of [4-9] | + only TRASER | - |
| person #5 → poolside step #31 | - | in front of [3-9] | + only TRASER | - |
| person #5 → fan #32 | - | in front of [4-9] | + only TRASER | - |
| person #6 → wall #13 | - | in front of [0-9] | + only TRASER | - |
| person #6 → swim ring #17 | - | in front of [0-9] | + only TRASER | - |
| person #6 → wall #18 | - | in front of [0-2] | + only TRASER | - |
| person #6 → window #22 | - | in front of [0-9] | + only TRASER | - |
| person #6 → storage reel #23 | - | in front of [0-9] | + only TRASER | - |
| person #6 → door #29 | - | in front of [4-9] | + only TRASER | - |
| person #6 → poolside step #31 | - | in front of [3-9] | + only TRASER | - |
| person #6 → fan #32 | - | in front of [4-9] | + only TRASER | - |
| person #7 → wall #13 | - | in front of [0-9] | + only TRASER | - |
| person #7 → swim ring #17 | - | in front of [0-9] | + only TRASER | - |
| person #7 → wall #18 | - | in front of [0-2] | + only TRASER | - |
| person #7 → window #22 | - | in front of [0-9] | + only TRASER | - |
| person #7 → storage reel #23 | - | in front of [0-9] | + only TRASER | - |
| person #7 → door #29 | - | in front of [4-9] | + only TRASER | - |
| person #7 → poolside step #31 | - | in front of [3-9] | + only TRASER | - |
| person #7 → fan #32 | - | in front of [4-9] | + only TRASER | - |
| person #9 → boat #0 | - | inside [0-9] | + only TRASER | - |
| person #9 → wall #13 | - | in front of [0-9] | + only TRASER | - |
| person #9 → swim ring #17 | - | in front of [0-9] | + only TRASER | - |
| person #9 → wall #18 | - | in front of [0-2] | + only TRASER | - |
| person #9 → window #22 | - | in front of [0-9] | + only TRASER | - |
| person #9 → storage reel #23 | - | in front of [0-9] | + only TRASER | - |
| person #9 → door #29 | - | in front of [4-9] | + only TRASER | - |
| person #9 → poolside step #31 | - | in front of [3-9] | + only TRASER | - |
| person #9 → fan #32 | - | in front of [4-9] | + only TRASER | - |
| person #10 → boat #0 | - | inside [0-9] | + only TRASER | - |
| person #10 → wall #13 | - | in front of [0-9] | + only TRASER | - |
| person #10 → swim ring #17 | - | in front of [0-9] | + only TRASER | - |
| person #10 → wall #18 | - | in front of [0-2] | + only TRASER | - |
| person #10 → window #22 | - | in front of [0-9] | + only TRASER | - |
| person #10 → storage reel #23 | - | in front of [0-9] | + only TRASER | - |
| person #10 → door #29 | - | in front of [4-9] | + only TRASER | - |
| person #10 → poolside step #31 | - | in front of [3-9] | + only TRASER | - |
| person #10 → fan #32 | - | in front of [4-9] | + only TRASER | - |
| bucket #11 → boat #0 | - | inside [0-9] | + only TRASER | - |
| bucket #11 → wall #13 | - | in front of [0-9] | + only TRASER | - |
| bucket #11 → swim ring #17 | - | in front of [0-9] | + only TRASER | - |
| bucket #11 → wall #18 | - | in front of [0-2] | + only TRASER | - |
| bucket #11 → window #22 | - | in front of [0-9] | + only TRASER | - |
| bucket #11 → storage reel #23 | - | in front of [0-9] | + only TRASER | - |
| bucket #11 → door #29 | - | in front of [4-9] | + only TRASER | - |
| bucket #11 → poolside step #31 | - | in front of [3-9] | + only TRASER | - |
| bucket #11 → fan #32 | - | in front of [4-9] | + only TRASER | - |
| person #20 → boat #0 | - | inside [0-2] | + only TRASER | - |
| person #20 → wall #13 | - | in front of [0-2] | + only TRASER | - |
| person #20 → swim ring #17 | - | in front of [0-2] | + only TRASER | - |
| person #20 → wall #18 | - | in front of [0-2] | + only TRASER | - |
| person #20 → window #22 | - | in front of [0-2] | + only TRASER | - |
| person #20 → storage reel #23 | - | in front of [0-2] | + only TRASER | - |
| person #20 → door #29 | - | in front of [-] | + only TRASER | - |
| person #20 → poolside step #31 | - | in front of [-] | + only TRASER | - |
| person #20 → fan #32 | - | in front of [-] | + only TRASER | - |
| person #21 → boat #0 | - | inside [0-2] | + only TRASER | - |
| person #21 → wall #13 | - | in front of [0-2] | + only TRASER | - |
| person #21 → swim ring #17 | - | in front of [0-2] | + only TRASER | - |
| person #21 → wall #18 | - | in front of [0-2] | + only TRASER | - |
| person #21 → window #22 | - | in front of [0-2] | + only TRASER | - |
| person #21 → storage reel #23 | - | in front of [0-2] | + only TRASER | - |
| person #21 → door #29 | - | in front of [-] | + only TRASER | - |
| person #21 → poolside step #31 | - | in front of [-] | + only TRASER | - |
| person #21 → fan #32 | - | in front of [-] | + only TRASER | - |
| tyre #36 → boat #0 | - | inside [0-9] | + only TRASER | - |
| tyre #36 → wall #13 | - | in front of [0-9] | + only TRASER | - |
| tyre #36 → swim ring #17 | - | in front of [0-9] | + only TRASER | - |
| tyre #36 → wall #18 | - | in front of [0-2] | + only TRASER | - |
| tyre #36 → window #22 | - | in front of [0-9] | + only TRASER | - |
| tyre #36 → storage reel #23 | - | in front of [0-9] | + only TRASER | - |
| tyre #36 → door #29 | - | in front of [4-9] | + only TRASER | - |
| tyre #36 → poolside step #31 | - | in front of [3-9] | + only TRASER | - |
| tyre #36 → fan #32 | - | in front of [4-9] | + only TRASER | - |
| tyre #37 → boat #0 | - | inside [0-9] | + only TRASER | - |
| tyre #37 → wall #13 | - | in front of [0-9] | + only TRASER | - |
| tyre #37 → swim ring #17 | - | in front of [0-9] | + only TRASER | - |
| tyre #37 → wall #18 | - | in front of [0-2] | + only TRASER | - |
| tyre #37 → window #22 | - | in front of [0-9] | + only TRASER | - |
| tyre #37 → storage reel #23 | - | in front of [0-9] | + only TRASER | - |
| tyre #37 → door #29 | - | in front of [4-9] | + only TRASER | - |
| tyre #37 → poolside step #31 | - | in front of [3-9] | + only TRASER | - |
| tyre #37 → fan #32 | - | in front of [4-9] | + only TRASER | - |


## 308_7WhzIsqPQW8

22.67 s video; humans: 42 objects, 41 relations on 36 pairs; TRASER: 163 relations on 57 pairs.

**Pairs:** 7 in both, 26 missed by TRASER, 3 reversed, 0 with an object TRASER was not given, 50 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 0 | referee | person |
| 1 | dancer | person |
| 2 | dancer | person |
| 3 | dance floor | dancer |
| 4 | trash can | banner |
| 5 | background floor | stage |
| 6 | country logo | signboard |
| 7 | country logo | signboard |
| 8 | country logo | signboard |
| 9 | country logo | signboard |
| 10 | flower vase | signboard |
| 11 | country logo | signboard |
| 12 | flower vase | flower arrangement |
| 13 | country logo | signboard |
| 14 | flower vase | flower arrangement |
| 15 | bottle water | bottle |
| 16 | flower vase | flower arrangement |
| 17 | logo | television set |
| 18 | flower vase | flower arrangement |
| 19 | flower vase | flower arrangement |
| 20 | flower vase | flower arrangement |
| 21 | bottle | bottle |
| 22 | cup | tablecloth |
| 23 | paper | tablecloth |
| 24 | paper | tablecloth |
| 25 | bottle water | chair |
| 26 | bottle water | bottle |
| 27 | table | banner |
| 28 | face | person |
| 29 | hair | hair |
| 30 | skirt | skirt |
| 31 | hand | handbag |
| 32 | hand | handbag |
| 33 | leg | legs (uncertain) |
| 34 | leg | legs (uncertain) |
| 35 | shirt | dress |
| 36 | head | person |
| 37 | jacket | suit jacket |
| 38 | shirt | suit jacket |
| 39 | trouser | trousers |
| 40 | head | - (not given to TRASER) |
| 41 | shoes | - (not given to TRASER) |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| referee #0 → dancer #1 | in front of [0-23] | - | ↔ TRASER has it reversed | - |
| referee #0 → dancer #2 | in front of [0-23] | - | ↔ TRASER has it reversed | - |
| referee #0 → dance floor #3 | on [0-23] | - | ✗ TRASER missed this pair | - |
| referee #0 → jacket #37 | wears [0-23] | - | ✗ TRASER missed this pair | - |
| dancer #1 → dancer #2 | dances with [0-23]; moves with [0-23]; performs routine with [0-23]; overlapping [13.5-20.5] | dancing with [0-24]; moving with [0-24]; performing dance routine with [0-24] | ✓ TRASER has this pair | ? ? ? ? |
| dancer #1 → dance floor #3 | on [0-23] | - | ✗ TRASER missed this pair | - |
| dancer #1 → table #27 | in front of [0-23] | in front of [0-24] | ✓ TRASER has this pair | ✓ |
| dancer #1 → skirt #30 | wears [0-23] | wearing [0-24] | ✓ TRASER has this pair | ? |
| dancer #1 → shirt #35 | wears [0-23] | wearing [0-24] | ✓ TRASER has this pair | ? |
| dancer #2 → dancer #1 | follows [19-23]; holds [12-19]; approaches [0-12] | - | ↔ TRASER has it reversed | - - - |
| dancer #2 → dance floor #3 | on [0-23] | - | ✗ TRASER missed this pair | - |
| dancer #2 → table #27 | in front of [0-23] | in front of [0-24] | ✓ TRASER has this pair | ✓ |
| dancer #2 → shirt #38 | wears [0-23] | wearing [0-24] | ✓ TRASER has this pair | ? |
| dancer #2 → trouser #39 | wears [0-23] | wearing [0-24] | ✓ TRASER has this pair | ? |
| dance floor #3 → table #27 | in front of [0-23] | - | ✗ TRASER missed this pair | - |
| trash can #4 → background floor #5 | on [0-12, 21-23] | - | ✗ TRASER missed this pair | - |
| country logo #6 → table #27 | on [0-23] | - | ✗ TRASER missed this pair | - |
| country logo #7 → table #27 | on [0-23] | - | ✗ TRASER missed this pair | - |
| country logo #8 → table #27 | on [0-23] | - | ✗ TRASER missed this pair | - |
| country logo #9 → table #27 | on [0-23] | - | ✗ TRASER missed this pair | - |
| flower vase #10 → table #27 | on [0-23] | - | ✗ TRASER missed this pair | - |
| country logo #11 → table #27 | on [0-23] | - | ✗ TRASER missed this pair | - |
| flower vase #12 → table #27 | on [0-23] | - | ✗ TRASER missed this pair | - |
| country logo #13 → table #27 | on [0-23] | - | ✗ TRASER missed this pair | - |
| flower vase #14 → table #27 | on [0-23] | - | ✗ TRASER missed this pair | - |
| flower vase #16 → table #27 | on [0-15, 20-23] | - | ✗ TRASER missed this pair | - |
| flower vase #18 → table #27 | on [0-23] | - | ✗ TRASER missed this pair | - |
| flower vase #19 → table #27 | on [0-23] | - | ✗ TRASER missed this pair | - |
| flower vase #20 → table #27 | on [0-23] | - | ✗ TRASER missed this pair | - |
| bottle #21 → table #27 | on [0-23] | - | ✗ TRASER missed this pair | - |
| cup #22 → table #27 | on [8-23] | - | ✗ TRASER missed this pair | - |
| paper #23 → table #27 | on [0-23] | - | ✗ TRASER missed this pair | - |
| paper #24 → table #27 | on [0-23] | - | ✗ TRASER missed this pair | - |
| bottle water #25 → table #27 | on [0-23] | - | ✗ TRASER missed this pair | - |
| bottle water #26 → table #27 | on [0-23] | - | ✗ TRASER missed this pair | - |
| table #27 → background floor #5 | on [0-23] | - | ✗ TRASER missed this pair | - |
| dancer #1 → referee #0 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #1 → trash can #4 | - | in front of [0-12, 22-24]; in front of [0-12, 22-24]; in front of [0-12, 22-24] | + only TRASER | - |
| dancer #1 → background floor #5 | - | in front of [0-24] | + only TRASER | - |
| dancer #1 → country logo #6 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #1 → country logo #7 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #1 → country logo #8 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #1 → country logo #9 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #1 → flower vase #10 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #1 → country logo #11 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #1 → flower vase #12 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #1 → country logo #13 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #1 → flower vase #14 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #1 → bottle water #15 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #1 → flower vase #16 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #1 → logo #17 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #1 → flower vase #18 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #1 → flower vase #19 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #1 → flower vase #20 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #1 → cup #22 | - | in front of [0-24] | + only TRASER | - |
| dancer #1 → paper #23 | - | in front of [0-24] | + only TRASER | - |
| dancer #1 → paper #24 | - | in front of [0-24] | + only TRASER | - |
| dancer #1 → bottle water #25 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #1 → face #28 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #1 → hand #31 | - | carrying [0-24] | + only TRASER | - |
| dancer #1 → hand #32 | - | carrying [0-24] | + only TRASER | - |
| dancer #1 → head #36 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #2 → referee #0 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #2 → trash can #4 | - | in front of [0-12, 22-24]; in front of [0-12, 22-24]; in front of [0-12, 22-24] | + only TRASER | - |
| dancer #2 → background floor #5 | - | in front of [0-24] | + only TRASER | - |
| dancer #2 → country logo #6 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #2 → country logo #7 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #2 → country logo #8 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #2 → country logo #9 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #2 → flower vase #10 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #2 → country logo #11 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #2 → flower vase #12 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #2 → country logo #13 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #2 → flower vase #14 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #2 → bottle water #15 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #2 → flower vase #16 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #2 → logo #17 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #2 → flower vase #18 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #2 → flower vase #19 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #2 → flower vase #20 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #2 → cup #22 | - | in front of [0-24] | + only TRASER | - |
| dancer #2 → paper #23 | - | in front of [0-24] | + only TRASER | - |
| dancer #2 → paper #24 | - | in front of [0-24] | + only TRASER | - |
| dancer #2 → bottle water #25 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #2 → face #28 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| dancer #2 → head #36 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |


## 670_JboU-y2LdkU

7.5 s video; humans: 24 objects, 33 relations on 31 pairs; TRASER: 86 relations on 76 pairs.

**Pairs:** 21 in both, 5 missed by TRASER, 5 reversed, 0 with an object TRASER was not given, 55 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 0 | grass | lawn |
| 1 | bush | bush |
| 2 | tree | bush |
| 3 | tree | bush |
| 4 | tree | bush |
| 5 | tree | bush |
| 6 | tree | tree |
| 7 | tree | car |
| 8 | tree | bush |
| 9 | tree | plant |
| 10 | car | car |
| 11 | tree | bush |
| 12 | person | person |
| 13 | person | person |
| 14 | person | child |
| 15 | person | person |
| 16 | person | person |
| 17 | person | person |
| 18 | person | person |
| 19 | forest | tree |
| 20 | wheel | wheel |
| 21 | headlight | car |
| 22 | headlight | wheel |
| 23 | windshield | car window |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| grass #0 → forest #19 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| bush #1 → grass #0 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| bush #1 → car #10 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| tree #3 → grass #0 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| tree #4 → grass #0 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| tree #5 → grass #0 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| tree #6 → grass #0 | on [0-8] | - | ✗ TRASER missed this pair | - |
| tree #8 → grass #0 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| car #10 → grass #0 | on [0-8]; parked on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ ? |
| car #10 → forest #19 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| car #10 → wheel #20 | has [0-2.5, 4.5-6.5] | - | ↔ TRASER has it reversed | - |
| car #10 → headlight #21 | has [0-4, 6-8] | - | ✗ TRASER missed this pair | - |
| car #10 → headlight #22 | has [3.5-5.5, 6.5-8] | - | ↔ TRASER has it reversed | - |
| car #10 → windshield #23 | has [0-6, 6.5-8] | - | ↔ TRASER has it reversed | - |
| person #12 → grass #0 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| person #12 → forest #19 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| person #13 → grass #0 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| person #13 → car #10 | moves away from [0-8] | - | ✗ TRASER missed this pair | - |
| person #13 → forest #19 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| person #14 → grass #0 | on [0-4, 5-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| person #15 → grass #0 | on [0-4, 6-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| person #16 → grass #0 | on [0-4, 6-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| person #17 → grass #0 | on [0-4, 7-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| person #18 → grass #0 | on [0-8] | on [0-8] | ✓ TRASER has this pair | ✓ |
| person #18 → forest #19 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| wheel #20 → car #10 | attached to [0-2, 5-6]; under [0-2, 5-6] | below [0-8] | ✓ TRASER has this pair | ? ? |
| headlight #21 → car #10 | attached to [0-4, 6-8] | - | ✗ TRASER missed this pair | - |
| headlight #21 → windshield #23 | in front of [0-4, 7-8] | - | ↔ TRASER has it reversed | - |
| headlight #22 → car #10 | attached to [0-2, 4-5, 6-8] | below [0-8] | ✓ TRASER has this pair | ? |
| headlight #22 → windshield #23 | in front of [0-2, 4-5, 7-8] | - | ↔ TRASER has it reversed | - |
| windshield #23 → car #10 | attached to [0-5, 7-8] | above [0-8] | ✓ TRASER has this pair | ? |
| bush #1 → tree #6 | - | in front of [0-8] | + only TRASER | - |
| bush #1 → tree #7 | - | in front of [0-8] | + only TRASER | - |
| bush #1 → tree #9 | - | in front of [0-8] | + only TRASER | - |
| bush #1 → person #12 | - | in front of [0-8]; in front of [0-8] | + only TRASER | - |
| bush #1 → person #13 | - | in front of [0-8]; in front of [0-8] | + only TRASER | - |
| bush #1 → person #14 | - | in front of [0-8]; in front of [0-8]; in front of [0-8] | + only TRASER | - |
| bush #1 → person #15 | - | in front of [0-8]; in front of [0-8] | + only TRASER | - |
| bush #1 → person #16 | - | in front of [0-8]; in front of [0-8] | + only TRASER | - |
| bush #1 → person #17 | - | in front of [0-8]; in front of [0-8] | + only TRASER | - |
| bush #1 → person #18 | - | in front of [0-8]; in front of [0-8]; in front of [0-8] | + only TRASER | - |
| bush #1 → forest #19 | - | in front of [0-8] | + only TRASER | - |
| bush #1 → headlight #21 | - | in front of [0-8]; in front of [0-8] | + only TRASER | - |
| tree #2 → grass #0 | - | on [0-4] | + only TRASER | - |
| tree #7 → grass #0 | - | on [0-8] | + only TRASER | - |
| tree #7 → tree #6 | - | in front of [0-8] | + only TRASER | - |
| tree #7 → forest #19 | - | in front of [0-8] | + only TRASER | - |
| tree #9 → grass #0 | - | on [0-8] | + only TRASER | - |
| tree #9 → tree #6 | - | in front of [0-8] | + only TRASER | - |
| tree #9 → forest #19 | - | in front of [0-8] | + only TRASER | - |
| car #10 → tree #6 | - | in front of [0-8] | + only TRASER | - |
| tree #11 → grass #0 | - | on [0-8] | + only TRASER | - |
| person #12 → tree #6 | - | in front of [0-8] | + only TRASER | - |
| person #13 → tree #6 | - | in front of [0-8] | + only TRASER | - |
| person #14 → tree #6 | - | in front of [0-8] | + only TRASER | - |
| person #14 → forest #19 | - | in front of [0-8] | + only TRASER | - |
| person #15 → tree #6 | - | in front of [0-8] | + only TRASER | - |
| person #15 → forest #19 | - | in front of [0-8] | + only TRASER | - |
| person #16 → tree #6 | - | in front of [0-8] | + only TRASER | - |
| person #16 → forest #19 | - | in front of [0-8] | + only TRASER | - |
| person #17 → tree #6 | - | in front of [0-8] | + only TRASER | - |
| person #17 → forest #19 | - | in front of [0-8] | + only TRASER | - |
| person #18 → tree #6 | - | in front of [0-8] | + only TRASER | - |
| person #18 → tree #7 | - | approaches [0-8] | + only TRASER | - |
| person #18 → tree #9 | - | approaches [0-8] | + only TRASER | - |
| person #18 → car #10 | - | moves away from [0-8] | + only TRASER | - |
| person #18 → person #14 | - | approaches [0-8] | + only TRASER | - |
| person #18 → person #15 | - | approaches [0-8] | + only TRASER | - |
| person #18 → person #16 | - | approaches [0-8] | + only TRASER | - |
| person #18 → person #17 | - | approaches [0-8] | + only TRASER | - |
| person #18 → wheel #20 | - | approaches [0-8] | + only TRASER | - |
| person #18 → headlight #21 | - | approaches [0-8] | + only TRASER | - |
| person #18 → headlight #22 | - | approaches [0-8] | + only TRASER | - |
| person #18 → windshield #23 | - | approaches [0-8] | + only TRASER | - |
| wheel #20 → grass #0 | - | on [0-8] | + only TRASER | - |
| wheel #20 → tree #7 | - | below [0-8] | + only TRASER | - |
| headlight #21 → grass #0 | - | on [0-8] | + only TRASER | - |
| headlight #21 → tree #6 | - | in front of [0-8] | + only TRASER | - |
| headlight #21 → forest #19 | - | in front of [0-8] | + only TRASER | - |
| headlight #22 → grass #0 | - | on [0-8] | + only TRASER | - |
| headlight #22 → tree #7 | - | below [0-8] | + only TRASER | - |
| windshield #23 → grass #0 | - | above [0-8] | + only TRASER | - |
| windshield #23 → tree #7 | - | above [0-8] | + only TRASER | - |
| windshield #23 → wheel #20 | - | above [0-8] | + only TRASER | - |
| windshield #23 → headlight #21 | - | above [0-8] | + only TRASER | - |
| windshield #23 → headlight #22 | - | above [0-8] | + only TRASER | - |


## 754_TYUV8DYWe8k

22.67 s video; humans: 28 objects, 26 relations on 20 pairs; TRASER: 47 relations on 47 pairs.

**Pairs:** 7 in both, 8 missed by TRASER, 5 reversed, 0 with an object TRASER was not given, 40 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 0 | building | truck |
| 1 | tree | tree |
| 2 | tree | tree |
| 3 | tree | tree |
| 4 | building | barn |
| 5 | tree | tree |
| 6 | grass | grass |
| 7 | sky | clouds |
| 8 | dirt | soil |
| 9 | grass | hill |
| 10 | hand | hand |
| 11 | bush | plant |
| 12 | fence post | tree |
| 13 | stick | pole |
| 14 | fence post | tree |
| 15 | stick | pole |
| 16 | stick | pole |
| 17 | stick | pole |
| 18 | stick | pole |
| 19 | stick | plant |
| 20 | storage | truck |
| 21 | storage | truck |
| 22 | storage | truck |
| 23 | stick | pole |
| 24 | stick | pole |
| 25 | side of house | tree |
| 26 | side of house | tree |
| 27 | roof | tree |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| building #0 → grass #6 | behind [0-23] | on [0-23] | ✓ TRASER has this pair | ? |
| building #0 → sky #7 | beneath [0-23] | - | ✗ TRASER missed this pair | - |
| tree #1 → grass #6 | behind [0-23] | on [0-23] | ✓ TRASER has this pair | ? |
| tree #1 → sky #7 | beneath [0-23] | - | ✗ TRASER missed this pair | - |
| tree #2 → grass #6 | behind [0-23] | on [0-23] | ✓ TRASER has this pair | ? |
| tree #2 → sky #7 | beneath [0-23] | - | ✗ TRASER missed this pair | - |
| tree #3 → grass #6 | behind [0-23] | on [0-23] | ✓ TRASER has this pair | ? |
| tree #3 → sky #7 | beneath [0-23] | - | ✗ TRASER missed this pair | - |
| building #4 → grass #6 | behind [0-23] | on [0-23] | ✓ TRASER has this pair | ? |
| building #4 → sky #7 | beneath [0-23] | - | ✗ TRASER missed this pair | - |
| grass #6 → sky #7 | in front of [0-23] | - | ↔ TRASER has it reversed | - |
| grass #6 → dirt #8 | above [0-23] | - | ↔ TRASER has it reversed | - |
| dirt #8 → grass #6 | in front of [0-23] | in front of [0-23] | ✓ TRASER has this pair | ✓ |
| hand #10 → dirt #8 | above [0-1] | touching [0-1] | ✓ TRASER has this pair | ? |
| storage #20 → building #0 | attached to [0-23]; near [0-23] | - | ↔ TRASER has it reversed | - - |
| storage #21 → building #0 | attached to [0-23]; near [0-23] | - | ↔ TRASER has it reversed | - - |
| storage #22 → building #0 | attached to [0-23]; near [0-23] | - | ↔ TRASER has it reversed | - - |
| side of house #25 → building #4 | attached to [0-23]; on [0-23] | - | ✗ TRASER missed this pair | - - |
| side of house #26 → building #4 | attached to [0-23]; on [0-23] | - | ✗ TRASER missed this pair | - - |
| roof #27 → building #4 | mounted on [0-23]; on [0-23] | - | ✗ TRASER missed this pair | - - |
| building #0 → building #4 | - | moving left relative to [0-23] | + only TRASER | - |
| building #0 → storage #20 | - | moving with [0-23] | + only TRASER | - |
| building #0 → storage #21 | - | moving with [0-23] | + only TRASER | - |
| building #0 → storage #22 | - | moving with [0-23] | + only TRASER | - |
| building #4 → grass #9 | - | in front of [0-23] | + only TRASER | - |
| tree #5 → grass #6 | - | on [0-23] | + only TRASER | - |
| grass #6 → grass #9 | - | in front of [0-23] | + only TRASER | - |
| sky #7 → grass #6 | - | above [0-23] | + only TRASER | - |
| sky #7 → dirt #8 | - | above [0-23] | + only TRASER | - |
| sky #7 → grass #9 | - | above [0-23] | + only TRASER | - |
| dirt #8 → grass #9 | - | in front of [0-23] | + only TRASER | - |
| bush #11 → grass #6 | - | on [0-23] | + only TRASER | - |
| bush #11 → grass #9 | - | in front of [0-23] | + only TRASER | - |
| fence post #12 → grass #6 | - | on [21-23] | + only TRASER | - |
| stick #13 → grass #6 | - | on [0-23] | + only TRASER | - |
| stick #13 → grass #9 | - | in front of [0-23] | + only TRASER | - |
| fence post #14 → grass #6 | - | on [0-23] | + only TRASER | - |
| stick #15 → grass #6 | - | on [0-23] | + only TRASER | - |
| stick #15 → grass #9 | - | in front of [0-23] | + only TRASER | - |
| stick #16 → grass #6 | - | on [0-23] | + only TRASER | - |
| stick #16 → grass #9 | - | in front of [0-23] | + only TRASER | - |
| stick #17 → grass #6 | - | on [0-23] | + only TRASER | - |
| stick #17 → grass #9 | - | in front of [0-23] | + only TRASER | - |
| stick #18 → grass #6 | - | on [0-23] | + only TRASER | - |
| stick #18 → grass #9 | - | in front of [0-23] | + only TRASER | - |
| stick #19 → grass #6 | - | on [0-23] | + only TRASER | - |
| stick #19 → grass #9 | - | in front of [0-23] | + only TRASER | - |
| storage #20 → building #4 | - | moving left relative to [0-23] | + only TRASER | - |
| storage #20 → grass #6 | - | on [0-23] | + only TRASER | - |
| storage #21 → building #4 | - | moving left relative to [0-23] | + only TRASER | - |
| storage #21 → grass #6 | - | on [0-23] | + only TRASER | - |
| storage #22 → building #4 | - | moving left relative to [0-23] | + only TRASER | - |
| storage #22 → grass #6 | - | on [0-23] | + only TRASER | - |
| stick #23 → grass #6 | - | on [0-23] | + only TRASER | - |
| stick #23 → grass #9 | - | in front of [0-23] | + only TRASER | - |
| stick #24 → grass #6 | - | on [0-23] | + only TRASER | - |
| stick #24 → grass #9 | - | in front of [0-23] | + only TRASER | - |
| side of house #25 → grass #6 | - | on [0-23] | + only TRASER | - |
| side of house #26 → grass #6 | - | on [0-23] | + only TRASER | - |
| roof #27 → grass #6 | - | on [0-23] | + only TRASER | - |

