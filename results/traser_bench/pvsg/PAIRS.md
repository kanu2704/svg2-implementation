# pvsg: which object pairs TRASER talks about (10 random videos, seed 0)

TRASER is given the human objects (masks) and writes its own list of relations; it is not told which pairs to describe. Each row is one ordered pair (subject → object) that the humans or TRASER mention.

- **✓ TRASER has this pair**: TRASER wrote at least one relation for the same two objects, same direction
- **✗ TRASER missed this pair**: humans annotated it, TRASER said nothing about these two objects
- **↔ reversed**: TRASER only has the other direction (object → subject); scored as missed
- **+ only TRASER**: TRASER describes a pair the humans did not annotate (ignored by the scores)
- last column, one mark per human relation of the pair: ✓ word right and tIoU > 0.5, ✗ not, ? the judge has not compared the words yet

**Total over these videos:** 156 human pairs, 254 TRASER pairs; 60 in both, 90 missed, 6 reversed, 194 only TRASER.

| video | human pairs | TRASER pairs | pairs in both | missed by TRASER | reversed | only TRASER |
|---|---|---|---|---|---|---|
| [0018_4748191834](#0018_4748191834) | 15 | 26 | 5 | 9 | 1 | 21 |
| [1000_6828150903](#1000_6828150903) | 11 | 32 | 11 | 0 | 0 | 21 |
| [1005_4760962392](#1005_4760962392) | 19 | 12 | 5 | 12 | 2 | 7 |
| [1011_4633647136](#1011_4633647136) | 15 | 16 | 6 | 9 | 0 | 10 |
| [1012_4024008346](#1012_4024008346) | 8 | 26 | 6 | 1 | 1 | 20 |
| [1015_4698622422](#1015_4698622422) | 9 | 13 | 2 | 6 | 1 | 11 |
| [1021_4278168115](#1021_4278168115) | 19 | 32 | 14 | 5 | 0 | 18 |
| [1025_6244382586](#1025_6244382586) | 11 | 22 | 7 | 3 | 1 | 15 |
| [P09_07](#p09_07) | 8 | 58 | 4 | 4 | 0 | 54 |
| [d1d4a1b3-a651-4eb8-bb7f-8d66982854fa](#d1d4a1b3-a651-4eb8-bb7f-8d66982854fa) | 41 | 17 | 0 | 41 | 0 | 17 |

## 0018_4748191834

33.2 s video; humans: 14 objects, 17 relations on 15 pairs; TRASER: 29 relations on 26 pairs.

**Pairs:** 5 in both, 9 missed by TRASER, 1 reversed, 21 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 1 | ground | - (not given to TRASER) |
| 2 | floor | table |
| 3 | wall | wall |
| 4 | cookie | cake slice |
| 5 | door | cabinet door |
| 6 | adult | person |
| 7 | child | child |
| 8 | table | tablecloth |
| 9 | chair | chair backrest |
| 10 | candle | candle |
| 11 | cake | cake |
| 12 | camera | knife |
| 13 | adult | shirt |
| 14 | chair | chair |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| adult #6 → child #7 | touching [9-22.6s]; hugging [7.6-22.6s] | serving [10.0606-25.1515s]; serving cake to [10.0606-25.1515s] | ✓ TRASER has this pair | ✓ ✗ |
| adult #6 → table #8 | beside [9-33.4s] | - | ✗ TRASER missed this pair | - |
| adult #6 → candle #10 | touching [25.8-27s] | - | ✗ TRASER missed this pair | - |
| child #7 → adult #6 | looking at [6.8-8.6s] | next to [0-34.2061s] | ✓ TRASER has this pair | ✗ |
| child #7 → chair #9 | sitting on [0-33.4s] | - | ↔ TRASER has it reversed | - |
| child #7 → candle #10 | blowing [22.4-26s] | - | ✗ TRASER missed this pair | - |
| child #7 → cake #11 | in front of [0-33.4s]; looking at [8.4-32s] | looking at [0-25.1515s] | ✓ TRASER has this pair | ✗ ✓ |
| candle #10 → cake #11 | on [0-33.4s] | inserted in [0-34.2061s]; on [0-34.2061s] | ✓ TRASER has this pair | ✓ |
| cake #11 → table #8 | on [0-33.4s] | on [0-34.2061s] | ✓ TRASER has this pair | ✓ |
| adult #13 → floor #2 | walking on [9.6-19s, 31.4-33.2s] | - | ✗ TRASER missed this pair | - |
| adult #13 → wall #3 | in front of [0-9.2s] | - | ✗ TRASER missed this pair | - |
| adult #13 → table #8 | beside [11-32s] | - | ✗ TRASER missed this pair | - |
| adult #13 → candle #10 | touching [20-21s] | - | ✗ TRASER missed this pair | - |
| adult #13 → cake #11 | touching [21-22.4s] | - | ✗ TRASER missed this pair | - |
| adult #13 → camera #12 | holding [0-32.2s] | - | ✗ TRASER missed this pair | - |
| cookie #4 → wall #3 | - | in front of [0-25.1515s] | + only TRASER | - |
| cookie #4 → cake #11 | - | above [0-25.1515s] | + only TRASER | - |
| adult #6 → wall #3 | - | in front of [0-34.2061s] | + only TRASER | - |
| adult #6 → door #5 | - | in front of [0-25.1515s, 26.1576-27.1636s, 28.1697-34.2061s] | + only TRASER | - |
| adult #6 → cake #11 | - | cutting [10.0606-25.1515s]; looking at [10.0606-25.1515s] | + only TRASER | - |
| adult #6 → camera #12 | - | holding [10.0606-25.1515s] | + only TRASER | - |
| adult #6 → adult #13 | - | wearing [0-34.2061s] | + only TRASER | - |
| child #7 → wall #3 | - | in front of [0-34.2061s] | + only TRASER | - |
| child #7 → cookie #4 | - | holding [0-25.1515s] | + only TRASER | - |
| child #7 → door #5 | - | in front of [0-25.1515s, 26.1576-27.1636s, 28.1697-34.2061s] | + only TRASER | - |
| child #7 → chair #14 | - | sitting on [0-34.2061s] | + only TRASER | - |
| table #8 → wall #3 | - | in front of [0-34.2061s] | + only TRASER | - |
| chair #9 → child #7 | - | behind [0-34.2061s] | + only TRASER | - |
| cake #11 → wall #3 | - | in front of [0-34.2061s] | + only TRASER | - |
| cake #11 → door #5 | - | in front of [0-25.1515s, 26.1576-27.1636s, 28.1697-34.2061s] | + only TRASER | - |
| cake #11 → adult #6 | - | in front of [0-34.2061s] | + only TRASER | - |
| cake #11 → child #7 | - | in front of [0-34.2061s] | + only TRASER | - |
| cake #11 → chair #9 | - | in front of [0-34.2061s] | + only TRASER | - |
| cake #11 → chair #14 | - | in front of [0-34.2061s] | + only TRASER | - |
| camera #12 → cake #11 | - | above [10.0606-25.1515s] | + only TRASER | - |
| chair #14 → child #7 | - | behind [0-34.2061s] | + only TRASER | - |


## 1000_6828150903

68.0 s video; humans: 15 objects, 13 relations on 11 pairs; TRASER: 38 relations on 32 pairs.

**Pairs:** 11 in both, 0 missed by TRASER, 0 reversed, 21 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 1 | rock | fireplace |
| 2 | floor | baseboard |
| 3 | ceiling | curtain |
| 4 | wall | curtain |
| 5 | door | door frame |
| 6 | shelf | table |
| 7 | window | window |
| 8 | adult | person |
| 9 | baby | child |
| 10 | dog | plush toy |
| 11 | toy | toy |
| 12 | door | door |
| 13 | door | curtain |
| 14 | door | window |
| 15 | door | door |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| adult #8 → rock #1 | in front of [16.4-68s] | in front of [16-69s] | ✓ TRASER has this pair | ✓ |
| adult #8 → floor #2 | walking on [0-16.8s] | above [10-14s, 50-69s] | ✓ TRASER has this pair | ✗ |
| adult #8 → wall #4 | beside [16.4-68s] | in front of [0-69s] | ✓ TRASER has this pair | ✗ |
| adult #8 → door #5 | beside [0-5.2s] | in front of [0-9s] | ✓ TRASER has this pair | ✗ |
| adult #8 → window #7 | beside [11.6-13.6s] | in front of [10-14s] | ✓ TRASER has this pair | ✗ |
| adult #8 → baby #9 | holding [0-68s]; hugging [0-68s] | holding [0-69s]; carrying [0-69s]; playing with [16-69s]; looking at [16-69s]; playing with toy [16-69s] | ✓ TRASER has this pair | ✓ ✓ |
| adult #8 → toy #11 | grabbing [16.8-18s]; holding [18-45.6s] | holding [16-69s]; in front of [16-69s] | ✓ TRASER has this pair | ✗ ✓ |
| adult #8 → door #12 | beside [5.2-9.6s] | in front of [0-12s] | ✓ TRASER has this pair | ✗ |
| adult #8 → door #14 | beside [10.2-11.6s] | in front of [10-14s] | ✓ TRASER has this pair | ✗ |
| baby #9 → toy #11 | holding [45.6-68s] | looking at [16-69s]; in front of [16-69s] | ✓ TRASER has this pair | ✗ |
| dog #10 → floor #2 | jumping over [19-21.4s] | above [19-24s] | ✓ TRASER has this pair | ✗ |
| rock #1 → floor #2 | - | above [16-17s, 50-69s] | + only TRASER | - |
| door #5 → floor #2 | - | above [10-12s] | + only TRASER | - |
| shelf #6 → floor #2 | - | above [12-14s] | + only TRASER | - |
| window #7 → floor #2 | - | above [10-14s] | + only TRASER | - |
| adult #8 → shelf #6 | - | in front of [12-14s] | + only TRASER | - |
| adult #8 → dog #10 | - | in front of [19-24s] | + only TRASER | - |
| adult #8 → door #15 | - | in front of [16-69s] | + only TRASER | - |
| baby #9 → rock #1 | - | in front of [16-69s] | + only TRASER | - |
| baby #9 → floor #2 | - | above [10-14s, 50-69s] | + only TRASER | - |
| baby #9 → wall #4 | - | in front of [0-69s] | + only TRASER | - |
| baby #9 → door #5 | - | in front of [0-9s] | + only TRASER | - |
| baby #9 → shelf #6 | - | in front of [12-14s] | + only TRASER | - |
| baby #9 → window #7 | - | in front of [10-14s] | + only TRASER | - |
| baby #9 → dog #10 | - | in front of [19-24s] | + only TRASER | - |
| baby #9 → door #12 | - | in front of [0-12s] | + only TRASER | - |
| baby #9 → door #14 | - | in front of [10-14s] | + only TRASER | - |
| baby #9 → door #15 | - | in front of [16-69s] | + only TRASER | - |
| toy #11 → floor #2 | - | above [50-69s] | + only TRASER | - |
| door #12 → floor #2 | - | above [10-12s] | + only TRASER | - |
| door #14 → floor #2 | - | above [10-14s] | + only TRASER | - |
| door #15 → floor #2 | - | above [16-17s, 50-69s] | + only TRASER | - |


## 1005_4760962392

90.0 s video; humans: 17 objects, 20 relations on 19 pairs; TRASER: 14 relations on 12 pairs.

**Pairs:** 5 in both, 12 missed by TRASER, 2 reversed, 7 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 1 | ground | fabric |
| 2 | wall | wall |
| 3 | spoon | candle |
| 4 | adult | person |
| 5 | child | girl |
| 6 | table | tablecloth |
| 7 | knife | knife |
| 8 | candle | candle |
| 9 | plate | napkin |
| 10 | cake | cake |
| 11 | adult | person |
| 12 | child | child |
| 13 | knife | bowl |
| 14 | candle | candle |
| 15 | plate | plate |
| 16 | adult | person |
| 17 | child | child |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| adult #4 → wall #2 | in front of [0-90s] | - | ✗ TRASER missed this pair | - |
| adult #4 → spoon #3 | holding [86.6-90s] | - | ✗ TRASER missed this pair | - |
| adult #4 → knife #7 | holding [11.6-22.6s] | holding [0-17s, 41-46s] | ✓ TRASER has this pair | ✗ |
| adult #4 → cake #10 | looking at [5-8.2s]; cutting [36-75.2s] | cutting [0-17s, 41-46s]; preparing cake [0-90s] | ✓ TRASER has this pair | ✗ ✗ |
| adult #4 → knife #13 | holding [34-80.2s] | holding [28-38s] | ✓ TRASER has this pair | ✗ |
| adult #4 → plate #15 | holding [84.6-90s] | serving [84-90s] | ✓ TRASER has this pair | ✗ |
| adult #4 → child #17 | holding [0-5.2s] | serving [66-72s] | ✓ TRASER has this pair | ✗ |
| child #5 → adult #4 | beside [0-90s] | - | ↔ TRASER has it reversed | - |
| child #5 → child #17 | beside [0-14.2s] | - | ✗ TRASER missed this pair | - |
| candle #8 → cake #10 | on [0-23.2s] | - | ✗ TRASER missed this pair | - |
| cake #10 → table #6 | on [0-90s] | - | ✗ TRASER missed this pair | - |
| child #12 → adult #4 | beside [0-90s] | - | ↔ TRASER has it reversed | - |
| child #12 → child #17 | beside [0-20.2s] | - | ✗ TRASER missed this pair | - |
| candle #14 → cake #10 | on [0-23.2s] | - | ✗ TRASER missed this pair | - |
| adult #16 → candle #8 | picking [23-26.2s] | - | ✗ TRASER missed this pair | - |
| adult #16 → candle #14 | picking [23-26.2s] | - | ✗ TRASER missed this pair | - |
| child #17 → table #6 | beside [39-90s] | - | ✗ TRASER missed this pair | - |
| child #17 → candle #8 | blowing [5.4-9.2s] | - | ✗ TRASER missed this pair | - |
| child #17 → plate #9 | holding [39.6-90s] | - | ✗ TRASER missed this pair | - |
| adult #4 → child #5 | - | serving [55-64s] | + only TRASER | - |
| adult #4 → child #12 | - | serving [28-38s] | + only TRASER | - |
| child #5 → cake #10 | - | looking at [55-64s] | + only TRASER | - |
| child #12 → cake #10 | - | looking at [28-38s] | + only TRASER | - |
| child #12 → knife #13 | - | eating from [28-38s] | + only TRASER | - |
| child #17 → cake #10 | - | looking at [0-17s, 41-46s]; looking at [66-72s] | + only TRASER | - |
| child #17 → plate #15 | - | looking at [84-90s] | + only TRASER | - |


## 1011_4633647136

53.6 s video; humans: 14 objects, 20 relations on 15 pairs; TRASER: 356 relations on 16 pairs (answer cut off at the token limit, read up to there).

**Pairs:** 6 in both, 9 missed by TRASER, 0 reversed, 10 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 1 | ground | floor |
| 2 | wall | painting |
| 3 | door | door |
| 4 | adult | person |
| 5 | child | child |
| 6 | table | tablecloth |
| 7 | chair | chair |
| 8 | candle | bow |
| 9 | cake | cake |
| 10 | adult | person |
| 11 | chair | chair |
| 12 | adult | person |
| 13 | chair | chair |
| 14 | chair | chair |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| adult #4 → child #5 | holding [30.6-53.6s]; picking [27.8-30.2s]; guiding [42.4-44.4s] | holding [0-53.6s]; looking at [0-53.6s] | ✓ TRASER has this pair | ✗ ✗ ✗ |
| adult #4 → table #6 | beside [0-53.6s] | - | ✗ TRASER missed this pair | - |
| adult #4 → candle #8 | holding [40.2-48.4s]; blowing [42.4-43.4s]; carrying [40.2-42.4s] | - | ✗ TRASER missed this pair | - - - |
| child #5 → table #6 | beside [0-53.6s] | - | ✗ TRASER missed this pair | - |
| child #5 → chair #7 | sitting on [0-28.8s]; standing on [30-53.6s] | - | ✗ TRASER missed this pair | - - |
| candle #8 → cake #9 | on [0-40.6s, 47.4-53.6s] | - | ✗ TRASER missed this pair | - |
| cake #9 → table #6 | on [0-53.6s] | - | ✗ TRASER missed this pair | - |
| adult #10 → ground #1 | walking on [8.6-9.8s, 45-49.4s] | approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s] | ✓ TRASER has this pair | ✗ |
| adult #10 → adult #4 | beside [8.4-45.8s] | approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s] | ✓ TRASER has this pair | ✗ |
| adult #10 → table #6 | beside [6.2-49.2s] | approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s] | ✓ TRASER has this pair | ✗ |
| adult #10 → cake #9 | touching [30.6-33.8s] | approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s] | ✓ TRASER has this pair | ✗ |
| adult #10 → chair #11 | holding [7.6-29.4s] | approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s] | ✓ TRASER has this pair | ✗ |
| adult #12 → table #6 | beside [0-53.6s] | - | ✗ TRASER missed this pair | - |
| adult #12 → candle #8 | lighting [0-4s] | - | ✗ TRASER missed this pair | - |
| adult #12 → cake #9 | touching [30-33.4s] | - | ✗ TRASER missed this pair | - |
| child #5 → cake #9 | - | looking at [0-53.6s] | + only TRASER | - |
| adult #10 → wall #2 | - | approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s] | + only TRASER | - |
| adult #10 → door #3 | - | approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s] | + only TRASER | - |
| adult #10 → child #5 | - | approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s] | + only TRASER | - |
| adult #10 → chair #7 | - | approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s] | + only TRASER | - |
| adult #10 → candle #8 | - | approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s] | + only TRASER | - |
| adult #10 → adult #12 | - | approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s] | + only TRASER | - |
| adult #10 → chair #13 | - | approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s] | + only TRASER | - |
| adult #10 → chair #14 | - | approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s]; approaching [5.95556-10.9185s]; moving away from [44.6667-50.6222s] | + only TRASER | - |
| adult #12 → child #5 | - | holding [0-53.6s]; looking at [0-53.6s] | + only TRASER | - |


## 1012_4024008346

19.6 s video; humans: 11 objects, 8 relations on 8 pairs; TRASER: 31 relations on 26 pairs.

**Pairs:** 6 in both, 1 missed by TRASER, 1 reversed, 20 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 1 | floor | floor |
| 2 | wall | wall |
| 3 | carpet | doormat |
| 4 | fence | gate |
| 5 | adult | child |
| 6 | child | child |
| 7 | sofa | sofa |
| 8 | ballon | balloon |
| 9 | carpet | baseboard |
| 10 | adult | person |
| 11 | ballon | ball |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| adult #5 → floor #1 | on [0-19.6s] | on [0-8.82s, 11.76-16.66s] | ✓ TRASER has this pair | ✓ |
| adult #5 → ballon #11 | playing with [4.4-5s, 13.4-16s] | - | ✗ TRASER missed this pair | - |
| child #6 → floor #1 | on [0-19.6s] | on [0-19.6s] | ✓ TRASER has this pair | ✓ |
| child #6 → ballon #8 | holding [0-19.6s] | holding [0-19.6s]; carrying [0-19.6s]; playing with [0-19.6s] | ✓ TRASER has this pair | ✓ |
| child #6 → ballon #11 | playing with [0-0.8s, 6-13s] | approaching [9.8-12.74s]; moving away from [12.74-16.66s] | ✓ TRASER has this pair | ✗ |
| sofa #7 → floor #1 | on [0-19.6s] | on [0-12.74s, 15.68-19.6s] | ✓ TRASER has this pair | ✓ |
| adult #10 → sofa #7 | sitting on [0-19.6s] | - | ↔ TRASER has it reversed | - |
| ballon #11 → floor #1 | on [0-19.6s] | on [0-16.66s] | ✓ TRASER has this pair | ✓ |
| carpet #3 → floor #1 | - | on [0-19.6s] | + only TRASER | - |
| carpet #3 → wall #2 | - | in front of [0-19.6s] | + only TRASER | - |
| fence #4 → floor #1 | - | on [0-19.6s] | + only TRASER | - |
| fence #4 → wall #2 | - | in front of [0-19.6s] | + only TRASER | - |
| fence #4 → adult #10 | - | in front of [0-12.74s, 15.68-19.6s] | + only TRASER | - |
| child #6 → fence #4 | - | in front of [0-19.6s] | + only TRASER | - |
| child #6 → sofa #7 | - | moving away from [9.8-12.74s]; approaching [15.68-19.6s]; in front of [0-12.74s, 15.68-19.6s] | + only TRASER | - |
| child #6 → adult #10 | - | in front of [0-12.74s, 15.68-19.6s] | + only TRASER | - |
| sofa #7 → wall #2 | - | in front of [0-12.74s, 15.68-19.6s] | + only TRASER | - |
| sofa #7 → adult #10 | - | in front of [0-12.74s, 15.68-19.6s] | + only TRASER | - |
| ballon #8 → floor #1 | - | above [0-19.6s] | + only TRASER | - |
| ballon #8 → fence #4 | - | in front of [0-19.6s] | + only TRASER | - |
| ballon #8 → child #6 | - | in front of [0-19.6s] | + only TRASER | - |
| ballon #8 → sofa #7 | - | in front of [0-12.74s, 15.68-19.6s] | + only TRASER | - |
| ballon #8 → adult #10 | - | in front of [0-12.74s, 15.68-19.6s] | + only TRASER | - |
| carpet #9 → wall #2 | - | attached to [0-1.96s] | + only TRASER | - |
| ballon #11 → fence #4 | - | in front of [0-16.66s] | + only TRASER | - |
| ballon #11 → child #6 | - | in front of [0-16.66s] | + only TRASER | - |
| ballon #11 → sofa #7 | - | in front of [0-12.74s, 15.68-16.66s] | + only TRASER | - |
| ballon #11 → adult #10 | - | in front of [0-12.74s, 15.68-19.6s] | + only TRASER | - |


## 1015_4698622422

42.0 s video; humans: 13 objects, 15 relations on 9 pairs; TRASER: 18 relations on 13 pairs.

**Pairs:** 2 in both, 6 missed by TRASER, 1 reversed, 11 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 1 | tree | pole |
| 2 | grass | tennis ball |
| 3 | adult | person |
| 4 | child | child |
| 5 | table | bench |
| 6 | hat | hand |
| 7 | bat | tennis racket |
| 8 | ball | soccer ball |
| 9 | car | car |
| 10 | adult | person |
| 11 | child | person |
| 12 | car | car |
| 13 | car | car |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| adult #3 → grass #2 | standing on [18.8-19.8s] | - | ✗ TRASER missed this pair | - |
| child #4 → grass #2 | on [0-41.8s]; walking on [0-10.4s]; squatting on [19-41.8s] | - | ✗ TRASER missed this pair | - - - |
| child #4 → bat #7 | holding [0-36.2s]; throwing [36-36.6s] | holding [0-17s, 18-36s]; swinging [0-17s, 18-36s] | ✓ TRASER has this pair | ✓ ✗ |
| child #4 → ball #8 | hitting [10.4-12.6s, 20.6-21.8s, 23.6-24.6s, 26.6-27.6s, 29-29.8s, 33.4-34.4s]; chasing [12.6-39.2s]; kicking [36.2-39.2s]; playing with [6.6-40.2s] | hitting [10-13s, 24-26s, 31-33s]; approaching [23-25s, 30-32s]; moving away from [25-27s, 33-35s]; playing with [0-17s, 18-42s]; near [0-17s, 18-42s] | ✓ TRASER has this pair | ✗ ✓ ✗ ✓ |
| ball #8 → grass #2 | on [0-41.8s] | - | ✗ TRASER missed this pair | - |
| adult #10 → grass #2 | standing on [40-41.8s] | - | ✗ TRASER missed this pair | - |
| adult #10 → child #4 | pulling [40.6-41.8s] | - | ↔ TRASER has it reversed | - |
| adult #10 → hat #6 | holding [40-41.8s] | - | ✗ TRASER missed this pair | - |
| child #11 → adult #3 | in front of [19-19.8s] | - | ✗ TRASER missed this pair | - |
| child #4 → tree #1 | - | in front of [0-15s, 20-22s, 29-38s] | + only TRASER | - |
| child #4 → adult #3 | - | in front of [17-18s] | + only TRASER | - |
| child #4 → table #5 | - | in front of [12-15s] | + only TRASER | - |
| child #4 → car #9 | - | in front of [0-15s] | + only TRASER | - |
| child #4 → adult #10 | - | in front of [41-42s] | + only TRASER | - |
| child #4 → child #11 | - | in front of [17-18s] | + only TRASER | - |
| child #4 → car #12 | - | in front of [4-15s] | + only TRASER | - |
| child #4 → car #13 | - | in front of [6-15s] | + only TRASER | - |
| bat #7 → child #4 | - | in front of [0-17s, 18-36s] | + only TRASER | - |
| bat #7 → ball #8 | - | above [0-17s, 18-36s] | + only TRASER | - |
| ball #8 → child #4 | - | in front of [0-17s, 18-42s] | + only TRASER | - |


## 1021_4278168115

79.8 s video; humans: 11 objects, 21 relations on 19 pairs; TRASER: 40 relations on 32 pairs.

**Pairs:** 14 in both, 5 missed by TRASER, 0 reversed, 18 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 1 | tree | Christmas tree |
| 2 | floor | rug |
| 3 | gift | gift wrap |
| 4 | curtain | curtain |
| 5 | book | book |
| 6 | adult | person |
| 7 | child | child |
| 8 | box | box |
| 9 | book | book |
| 10 | book | book |
| 11 | book | book |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| tree #1 → floor #2 | on [0-79.8s] | - | ✗ TRASER missed this pair | - |
| gift #3 → floor #2 | on [31-79.8s] | on [2.9925-31.92s] | ✓ TRASER has this pair | ✗ |
| book #5 → floor #2 | on [42.8-43.4s, 50.6-79.8s] | on [41.895-80.7975s] | ✓ TRASER has this pair | ✓ |
| adult #6 → floor #2 | sitting on [0-79.8s] | on [0-80.7975s] | ✓ TRASER has this pair | ✓ |
| adult #6 → gift #3 | holding [0-3s] | - | ✗ TRASER missed this pair | - |
| adult #6 → book #5 | touching [49.4-52s]; holding [49-51.2s] | - | ✗ TRASER missed this pair | - - |
| adult #6 → box #8 | opening [33.4-42.4s] | - | ✗ TRASER missed this pair | - |
| child #7 → floor #2 | on [0-79.8s] | on [0-80.7975s] | ✓ TRASER has this pair | ✓ |
| child #7 → gift #3 | opening [3.6-31s] | holding [1.995-27.93s]; opening [1.995-27.93s]; looking at [1.995-27.93s] | ✓ TRASER has this pair | ✓ |
| child #7 → book #5 | holding [43.2-48.8s] | holding [41.895-51.87s]; looking at [41.895-51.87s] | ✓ TRASER has this pair | ✓ |
| child #7 → adult #6 | in front of [0-79.8s] | - | ✗ TRASER missed this pair | - |
| child #7 → box #8 | holding [31-33.2s] | holding [30.9225-41.895s]; opening [30.9225-41.895s]; looking at [30.9225-41.895s] | ✓ TRASER has this pair | ✗ |
| child #7 → book #9 | touching [66.2-71.2s] | holding [41.895-51.87s]; looking at [41.895-51.87s] | ✓ TRASER has this pair | ✗ |
| child #7 → book #10 | holding [50-54s] | holding [41.895-51.87s]; looking at [41.895-51.87s] | ✓ TRASER has this pair | ✗ |
| child #7 → book #11 | touching [78.2-79.8s]; holding [54.6-65.4s] | holding [51.87-65.835s]; looking at [51.87-65.835s] | ✓ TRASER has this pair | ✗ ✓ |
| box #8 → floor #2 | on [42.4-79.8s] | on [30.9225-41.895s] | ✓ TRASER has this pair | ✗ |
| book #9 → floor #2 | on [42.8-79.8s] | on [41.895-80.7975s] | ✓ TRASER has this pair | ✓ |
| book #10 → floor #2 | on [42.8-50s, 54-79.8s] | on [41.895-80.7975s] | ✓ TRASER has this pair | ✓ |
| book #11 → floor #2 | on [42.8-54.6s, 65.4-79.8s] | on [41.895-80.7975s] | ✓ TRASER has this pair | ✓ |
| tree #1 → curtain #4 | - | in front of [0-80.7975s] | + only TRASER | - |
| floor #2 → curtain #4 | - | in front of [0-80.7975s] | + only TRASER | - |
| gift #3 → tree #1 | - | in front of [2.9925-31.92s] | + only TRASER | - |
| gift #3 → curtain #4 | - | in front of [2.9925-31.92s] | + only TRASER | - |
| book #5 → tree #1 | - | in front of [41.895-80.7975s] | + only TRASER | - |
| book #5 → curtain #4 | - | in front of [41.895-80.7975s] | + only TRASER | - |
| adult #6 → tree #1 | - | in front of [0-80.7975s] | + only TRASER | - |
| adult #6 → curtain #4 | - | in front of [0-80.7975s] | + only TRASER | - |
| child #7 → tree #1 | - | in front of [0-80.7975s] | + only TRASER | - |
| child #7 → curtain #4 | - | in front of [0-80.7975s] | + only TRASER | - |
| box #8 → tree #1 | - | in front of [30.9225-41.895s] | + only TRASER | - |
| box #8 → curtain #4 | - | in front of [30.9225-41.895s] | + only TRASER | - |
| book #9 → tree #1 | - | in front of [41.895-80.7975s] | + only TRASER | - |
| book #9 → curtain #4 | - | in front of [41.895-80.7975s] | + only TRASER | - |
| book #10 → tree #1 | - | in front of [41.895-80.7975s] | + only TRASER | - |
| book #10 → curtain #4 | - | in front of [41.895-80.7975s] | + only TRASER | - |
| book #11 → tree #1 | - | in front of [41.895-80.7975s] | + only TRASER | - |
| book #11 → curtain #4 | - | in front of [41.895-80.7975s] | + only TRASER | - |


## 1025_6244382586

20.6 s video; humans: 11 objects, 12 relations on 11 pairs; TRASER: 28 relations on 22 pairs.

**Pairs:** 7 in both, 3 missed by TRASER, 1 reversed, 15 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 1 | ground | sand |
| 2 | ceiling | ceiling |
| 3 | wall | fence |
| 4 | adult | person |
| 5 | child | person |
| 6 | horse | horse |
| 7 | hat | helmet |
| 8 | box | box |
| 9 | child | person |
| 10 | horse | horse |
| 11 | hat | helmet |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| adult #4 → ground #1 | walking on [5-8s] | - | ✗ TRASER missed this pair | - |
| adult #4 → child #5 | looking at [5-8s]; guiding [0-20.6s] | - | ✗ TRASER missed this pair | - - |
| adult #4 → child #9 | guiding [0-20.6s] | - | ✗ TRASER missed this pair | - |
| child #5 → horse #6 | riding [0-20.6s] | riding [0-20.6s]; riding horse [0-20.6s] | ✓ TRASER has this pair | ✓ |
| child #5 → hat #7 | wearing [0-20.6s] | wearing [0-20.6s] | ✓ TRASER has this pair | ✓ |
| horse #6 → ground #1 | walking on [0-20.6s] | moving across [0-20.6s]; on [0-20.6s] | ✓ TRASER has this pair | ✓ |
| box #8 → ground #1 | on [0-5.2s] | on [0-5.88571s] | ✓ TRASER has this pair | ✓ |
| child #9 → child #5 | looking at [0-5.2s] | - | ↔ TRASER has it reversed | - |
| child #9 → horse #10 | riding [0-5.4s, 10.8-20.6s] | riding [0-20.6s]; riding horse [0-20.6s] | ✓ TRASER has this pair | ✓ |
| child #9 → hat #11 | wearing [0-5.4s, 10.8-20.6s] | wearing [0-20.6s] | ✓ TRASER has this pair | ✓ |
| horse #10 → ground #1 | walking on [0-5.4s, 10.8-20.6s] | moving across [0-20.6s]; on [0-20.6s] | ✓ TRASER has this pair | ✓ |
| ceiling #2 → ground #1 | - | above [0-20.6s] | + only TRASER | - |
| ceiling #2 → wall #3 | - | above [0-20.6s] | + only TRASER | - |
| child #5 → ground #1 | - | moving across [0-20.6s] | + only TRASER | - |
| child #5 → wall #3 | - | in front of [0-20.6s] | + only TRASER | - |
| child #5 → child #9 | - | moving with [0-20.6s]; next to [0-20.6s] | + only TRASER | - |
| horse #6 → wall #3 | - | in front of [0-20.6s] | + only TRASER | - |
| horse #6 → horse #10 | - | moving with [0-20.6s]; next to [0-20.6s] | + only TRASER | - |
| hat #7 → child #5 | - | on [0-20.6s] | + only TRASER | - |
| box #8 → wall #3 | - | in front of [0-5.88571s] | + only TRASER | - |
| box #8 → horse #6 | - | in front of [0-5.88571s] | + only TRASER | - |
| box #8 → horse #10 | - | in front of [0-5.88571s] | + only TRASER | - |
| child #9 → ground #1 | - | moving across [0-20.6s] | + only TRASER | - |
| child #9 → wall #3 | - | in front of [0-20.6s] | + only TRASER | - |
| horse #10 → wall #3 | - | in front of [0-20.6s] | + only TRASER | - |
| hat #11 → child #9 | - | on [0-20.6s] | + only TRASER | - |


## P09_07

55.2 s video; humans: 29 objects, 15 relations on 8 pairs; TRASER: 72 relations on 58 pairs.

**Pairs:** 4 in both, 4 missed by TRASER, 0 reversed, 54 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 1 | floor | hand |
| 2 | wall | wall |
| 3 | countertop | table |
| 4 | microwave | cabinet door |
| 5 | pot | bottle |
| 6 | cover | lid (uncertain) |
| 7 | stove | handle (uncertain) |
| 8 | shelf | bottle |
| 9 | cabinet | drawer |
| 10 | spoon | scissors |
| 11 | scissor | scissors |
| 12 | adult | hand |
| 13 | sink | bowl |
| 14 | knife | knife |
| 15 | bottle | cup |
| 16 | paper | paper (uncertain) |
| 17 | box | paper (uncertain) |
| 18 | cover | bowl |
| 19 | cabinet | drawer |
| 20 | spoon | lid (uncertain) |
| 21 | knife | knife |
| 22 | bottle | - (not given to TRASER) |
| 23 | powder | cup |
| 24 | cover | bowl |
| 25 | cabinet | shelf (uncertain) |
| 26 | spoon | - (not given to TRASER) |
| 27 | bottle | cup |
| 28 | cover | lid (uncertain) |
| 29 | bottle | lid (uncertain) |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| adult #12 → cover #6 | holding [4.2-5s, 48-52.6s] | - | ✗ TRASER missed this pair | - |
| adult #12 → cabinet #9 | opening [5.8-7s, 44.6-45.6s]; closing [30.6-31.8s, 46.4-47.2s] | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | ✓ TRASER has this pair | ✗ ✗ |
| adult #12 → bottle #15 | holding [1.6-5s, 48.6-53.4s]; opening [2.4-4.2s]; closing [48-52.6s] | holding [16.0582-27.0982s, 33.12-45.1636s]; holding [51.1855-55.2s]; preparing drink in [51.1855-55.2s] | ✓ TRASER has this pair | ✗ ✗ ✗ |
| adult #12 → cover #18 | holding [14.6-25.4s] | holding [16.0582-27.0982s] | ✓ TRASER has this pair | ✓ |
| adult #12 → spoon #20 | holding [16.4-25.2s] | - | ✗ TRASER missed this pair | - |
| adult #12 → bottle #27 | holding [7.6-9.8s, 12.4-30.2s]; opening [12.4-15.2s]; closing [25.6-27.6s] | holding [16.0582-27.0982s, 33.12-45.1636s]; pouring into [16.0582-27.0982s, 33.12-45.1636s]; holding [51.1855-55.2s]; preparing drink in [16.0582-27.0982s, 33.12-45.1636s] | ✓ TRASER has this pair | ✗ ✗ ✗ |
| adult #12 → cover #28 | holding [33.8-34.6s, 39.4-40.4s] | - | ✗ TRASER missed this pair | - |
| adult #12 → bottle #29 | holding [10.6-12.2s, 32.2-46.4s]; opening [32.4-34.6s]; closing [40.2-43.8s] | - | ✗ TRASER missed this pair | - - - |
| floor #1 → countertop #3 | - | above [0-2.00727s, 4.01455-11.04s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| spoon #10 → countertop #3 | - | on [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| spoon #10 → microwave #4 | - | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| spoon #10 → cabinet #9 | - | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| spoon #10 → cabinet #19 | - | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| scissor #11 → countertop #3 | - | on [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| scissor #11 → microwave #4 | - | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| scissor #11 → cabinet #9 | - | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| scissor #11 → cabinet #19 | - | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| adult #12 → wall #2 | - | in front of [0-2.00727s]; in front of [0-2.00727s] | + only TRASER | - |
| adult #12 → countertop #3 | - | above [0-55.2s] | + only TRASER | - |
| adult #12 → microwave #4 | - | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| adult #12 → pot #5 | - | in front of [0-2.00727s]; in front of [0-2.00727s] | + only TRASER | - |
| adult #12 → shelf #8 | - | in front of [0-2.00727s]; in front of [0-2.00727s] | + only TRASER | - |
| adult #12 → spoon #10 | - | holding [35.1273-45.1636s]; cutting [35.1273-45.1636s]; in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| adult #12 → scissor #11 | - | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s]; in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| adult #12 → sink #13 | - | in front of [0-2.00727s]; in front of [0-2.00727s] | + only TRASER | - |
| adult #12 → knife #14 | - | holding [51.1855-55.2s]; in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s]; in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| adult #12 → cabinet #19 | - | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| adult #12 → knife #21 | - | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| adult #12 → powder #23 | - | holding [16.0582-27.0982s] | + only TRASER | - |
| adult #12 → cover #24 | - | holding [16.0582-27.0982s] | + only TRASER | - |
| sink #13 → countertop #3 | - | on [0-2.00727s] | + only TRASER | - |
| sink #13 → microwave #4 | - | in front of [0-2.00727s] | + only TRASER | - |
| sink #13 → cabinet #9 | - | in front of [0-2.00727s] | + only TRASER | - |
| sink #13 → cabinet #19 | - | in front of [0-2.00727s] | + only TRASER | - |
| knife #14 → countertop #3 | - | on [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| knife #14 → microwave #4 | - | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| knife #14 → cabinet #9 | - | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| knife #14 → cabinet #19 | - | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| bottle #15 → countertop #3 | - | on [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| bottle #15 → microwave #4 | - | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| bottle #15 → cabinet #9 | - | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| bottle #15 → cabinet #19 | - | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| cover #18 → countertop #3 | - | on [16.0582-27.0982s] | + only TRASER | - |
| cover #18 → microwave #4 | - | in front of [16.0582-27.0982s] | + only TRASER | - |
| cover #18 → cabinet #9 | - | in front of [16.0582-27.0982s] | + only TRASER | - |
| cover #18 → cabinet #19 | - | in front of [16.0582-27.0982s] | + only TRASER | - |
| knife #21 → countertop #3 | - | on [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| knife #21 → microwave #4 | - | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| knife #21 → cabinet #9 | - | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| knife #21 → cabinet #19 | - | in front of [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s] | + only TRASER | - |
| powder #23 → countertop #3 | - | on [16.0582-27.0982s] | + only TRASER | - |
| powder #23 → microwave #4 | - | in front of [16.0582-27.0982s] | + only TRASER | - |
| powder #23 → cabinet #9 | - | in front of [16.0582-27.0982s] | + only TRASER | - |
| powder #23 → cabinet #19 | - | in front of [16.0582-27.0982s] | + only TRASER | - |
| cover #24 → countertop #3 | - | on [16.0582-27.0982s] | + only TRASER | - |
| cover #24 → microwave #4 | - | in front of [16.0582-27.0982s] | + only TRASER | - |
| cover #24 → cabinet #9 | - | in front of [16.0582-27.0982s] | + only TRASER | - |
| cover #24 → cabinet #19 | - | in front of [16.0582-27.0982s] | + only TRASER | - |
| bottle #27 → countertop #3 | - | on [16.0582-27.0982s, 33.12-45.1636s] | + only TRASER | - |
| bottle #27 → microwave #4 | - | in front of [16.0582-27.0982s, 33.12-45.1636s] | + only TRASER | - |
| bottle #27 → cabinet #9 | - | in front of [16.0582-27.0982s, 33.12-45.1636s] | + only TRASER | - |
| bottle #27 → cabinet #19 | - | in front of [16.0582-27.0982s, 33.12-45.1636s] | + only TRASER | - |


## d1d4a1b3-a651-4eb8-bb7f-8d66982854fa

183.8 s video; humans: 44 objects, 41 relations on 41 pairs; TRASER: 17 relations on 17 pairs.

**Pairs:** 0 in both, 41 missed by TRASER, 0 reversed, 17 only TRASER

<details><summary>objects (human label vs TRASER label)</summary>

| id | human label | TRASER label |
|---|---|---|
| 1 | wall | table |
| 2 | mat | hand |
| 3 | others | cell phone (uncertain) |
| 4 | card | playing card |
| 5 | adult | hand |
| 6 | table | hand |
| 7 | box | table |
| 8 | cellphone | hand |
| 9 | card | playing card |
| 10 | adult | hand |
| 11 | box | hand |
| 12 | cellphone | hand |
| 13 | card | playing card |
| 14 | card | playing card |
| 15 | card | hand |
| 16 | card | hand |
| 17 | card | hand |
| 18 | card | playing card |
| 19 | card | playing card |
| 20 | card | hand |
| 21 | card | hand |
| 22 | card | playing card |
| 23 | card | playing card |
| 24 | card | playing card |
| 25 | card | playing card |
| 26 | card | playing card |
| 27 | card | playing card |
| 28 | card | playing card |
| 29 | card | playing card |
| 30 | card | playing card |
| 31 | card | playing card |
| 32 | card | playing card |
| 33 | card | playing card |
| 34 | card | playing card |
| 35 | card | playing card |
| 36 | card | playing card |
| 37 | card | playing card |
| 38 | card | playing card |
| 39 | card | playing card |
| 40 | card | hand |
| 41 | card | - (not given to TRASER) |
| 42 | card | - (not given to TRASER) |
| 43 | card | - (not given to TRASER) |
| 44 | card | - (not given to TRASER) |

</details>

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| card #4 → table #6 | on [0-175.4s] | - | ✗ TRASER missed this pair | - |
| adult #5 → card #18 | holding [6.6-14.4s] | - | ✗ TRASER missed this pair | - |
| adult #5 → card #19 | holding [18.4-21.2s] | - | ✗ TRASER missed this pair | - |
| adult #5 → card #20 | holding [23.2-27.8s] | - | ✗ TRASER missed this pair | - |
| adult #5 → card #23 | picking [59.4-65.6s] | - | ✗ TRASER missed this pair | - |
| adult #5 → card #24 | holding [40.6-44s] | - | ✗ TRASER missed this pair | - |
| adult #5 → card #25 | holding [45.4-48.4s] | - | ✗ TRASER missed this pair | - |
| adult #5 → card #26 | holding [72.8-79.6s] | - | ✗ TRASER missed this pair | - |
| adult #5 → card #30 | holding [92-99s] | - | ✗ TRASER missed this pair | - |
| adult #5 → card #36 | holding [125-130.2s] | - | ✗ TRASER missed this pair | - |
| adult #5 → card #38 | holding [139.8-142.6s] | - | ✗ TRASER missed this pair | - |
| adult #5 → card #40 | holding [149-152s] | - | ✗ TRASER missed this pair | - |
| adult #5 → card #42 | holding [155.8-158.6s] | - | ✗ TRASER missed this pair | - |
| adult #5 → card #44 | holding [167.6-173.2s] | - | ✗ TRASER missed this pair | - |
| card #9 → table #6 | on [0-175.4s] | - | ✗ TRASER missed this pair | - |
| adult #10 → card #17 | holding [8.8-14.4s] | - | ✗ TRASER missed this pair | - |
| adult #10 → card #21 | holding [29-31s] | - | ✗ TRASER missed this pair | - |
| adult #10 → card #22 | holding [32.6-35.2s] | - | ✗ TRASER missed this pair | - |
| adult #10 → card #23 | holding [36-39.8s] | - | ✗ TRASER missed this pair | - |
| adult #10 → card #28 | holding [83.8-86.8s] | - | ✗ TRASER missed this pair | - |
| adult #10 → card #37 | holding [132.4-137.4s] | - | ✗ TRASER missed this pair | - |
| card #13 → table #6 | on [0-175.4s] | - | ✗ TRASER missed this pair | - |
| card #14 → table #6 | on [0-175.4s] | - | ✗ TRASER missed this pair | - |
| card #15 → table #6 | on [0-175.4s] | - | ✗ TRASER missed this pair | - |
| card #16 → table #6 | on [0-175.4s] | - | ✗ TRASER missed this pair | - |
| card #19 → card #13 | on [20.4-175.4s] | - | ✗ TRASER missed this pair | - |
| card #20 → table #6 | on [27.6-175.4s] | - | ✗ TRASER missed this pair | - |
| card #21 → table #6 | on [30.8-175.4s] | - | ✗ TRASER missed this pair | - |
| card #23 → table #6 | on [39.8-175.4s] | - | ✗ TRASER missed this pair | - |
| card #23 → card #25 | on [65-175.4s] | - | ✗ TRASER missed this pair | - |
| card #24 → card #4 | on [43.8-175.4s] | - | ✗ TRASER missed this pair | - |
| card #25 → card #22 | on [48.4-175.4s] | - | ✗ TRASER missed this pair | - |
| card #26 → card #20 | on [79.2-175.4s] | - | ✗ TRASER missed this pair | - |
| card #28 → card #9 | on [86.6-175.4s] | - | ✗ TRASER missed this pair | - |
| card #30 → card #26 | on [98.8-175.4s] | - | ✗ TRASER missed this pair | - |
| card #36 → card #30 | on [65-175.4s] | - | ✗ TRASER missed this pair | - |
| card #37 → card #35 | on [137.2-175.4s] | - | ✗ TRASER missed this pair | - |
| card #38 → card #36 | on [142.2-175.4s] | - | ✗ TRASER missed this pair | - |
| card #40 → card #38 | on [152-175.4s] | - | ✗ TRASER missed this pair | - |
| card #42 → card #40 | on [158.4-175.4s] | - | ✗ TRASER missed this pair | - |
| card #44 → card #21 | on [173-175.4s] | - | ✗ TRASER missed this pair | - |
| mat #2 → wall #1 | - | deals cards to [0-175.184s] | + only TRASER | - |
| mat #2 → card #4 | - | manipulates [0-2.87188s, 4.30781-18.6672s] | + only TRASER | - |
| mat #2 → card #13 | - | manipulates [18.6672-24.4109s] | + only TRASER | - |
| mat #2 → card #14 | - | manipulates [24.4109-31.5906s] | + only TRASER | - |
| mat #2 → card #19 | - | manipulates [31.5906-38.7703s] | + only TRASER | - |
| mat #2 → card #22 | - | manipulates [38.7703-45.95s] | + only TRASER | - |
| mat #2 → card #23 | - | manipulates [45.95-53.1297s] | + only TRASER | - |
| mat #2 → card #25 | - | manipulates [53.1297-60.3094s] | + only TRASER | - |
| mat #2 → card #26 | - | manipulates [60.3094-67.4891s] | + only TRASER | - |
| mat #2 → card #27 | - | manipulates [67.4891-74.6688s] | + only TRASER | - |
| mat #2 → card #28 | - | manipulates [74.6688-81.8484s] | + only TRASER | - |
| mat #2 → card #30 | - | manipulates [81.8484-89.0281s] | + only TRASER | - |
| mat #2 → card #31 | - | manipulates [160.825-168.005s] | + only TRASER | - |
| mat #2 → card #33 | - | manipulates [168.005-175.184s] | + only TRASER | - |
| mat #2 → card #34 | - | manipulates [89.0281-96.2078s] | + only TRASER | - |
| mat #2 → card #36 | - | manipulates [96.2078-103.388s] | + only TRASER | - |
| mat #2 → card #38 | - | manipulates [103.388-110.567s] | + only TRASER | - |

