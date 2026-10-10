# pvsg: which object pairs TRASER talks about (10 random videos, seed 0)

TRASER is given the human objects (masks) and writes its own list of relations; it is not told which pairs to describe. Each row is one ordered pair (subject → object) that the humans or TRASER mention.

- **✓ TRASER has this pair**: TRASER wrote at least one relation for the same two objects, same direction
- **✗ TRASER missed this pair**: humans annotated it, TRASER said nothing about these two objects
- **↔ reversed**: TRASER only has the other direction (object → subject); scored as missed
- **⊘ object not given**: one of the two objects was not among the (at most 40) objects TRASER received, so it could not answer; scored as missed in the main score (README.md also shows a score that leaves these out)
- **mask given to TRASER?** (objects table): yes, with the number TRASER calls it ("object k"); or no, because the run gives only the first 40 objects by number, or because the object has no mask on the frames TRASER reads (about 1 per second)
- **+ only TRASER**: TRASER describes a pair the humans did not annotate (ignored by the scores)
- last column, one mark per human relation of the pair: ✓ word right and tIoU > 0.5, ✗ not, ? the judge has not compared the words yet

**Total over these videos:** 129 human pairs, 230 TRASER pairs; 60 in both, 60 missed, 4 reversed, 5 with an object not given, 170 only TRASER.

| video | source | masks given to TRASER | objects right | relations right | triplets right | human pairs | TRASER pairs | pairs in both | missed by TRASER | reversed | object not given | only TRASER |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [0018_4748191834](#0018_4748191834) | vidor | 13/14 | 10/14 | 4/17 | 4/17 | 15 | 26 | 5 | 9 | 1 | 0 | 21 |
| [1000_6828150903](#1000_6828150903) | vidor | 15/15 | 10/15 | 4/13 | 3/13 | 11 | 32 | 11 | 0 | 0 | 0 | 21 |
| [1011_4633647136](#1011_4633647136) | vidor | 14/14 | 12/14 | 0/20 | 0/20 | 15 | 16 | 6 | 9 | 0 | 0 | 10 |
| [1012_4024008346](#1012_4024008346) | vidor | 11/11 | 10/11 | 5/8 | 4/8 | 8 | 26 | 6 | 1 | 1 | 0 | 20 |
| [1015_4698622422](#1015_4698622422) | vidor | 13/13 | 10/13 | 3/15 | 3/15 | 9 | 13 | 2 | 6 | 1 | 0 | 11 |
| [1021_4278168115](#1021_4278168115) | vidor | 11/11 | 11/11 | 9/21 | 9/21 | 19 | 32 | 14 | 5 | 0 | 0 | 18 |
| [1025_4615486172](#1025_4615486172) | vidor | 27/27 | 21/27 | 0/24 | 0/24 | 23 | 25 | 3 | 19 | 1 | 0 | 22 |
| [P03_06](#p03_06) | epic_kitchen | 39/65 | 19/65 | 2/20 | 0/20 | 16 | 23 | 8 | 3 | 0 | 5 | 15 |
| [P14_06](#p14_06) | epic_kitchen | 34/34 | 24/34 | 0/10 | 0/10 | 7 | 29 | 0 | 7 | 0 | 0 | 29 |
| [P28_19](#p28_19) | epic_kitchen | 27/28 | 17/28 | 3/10 | 0/10 | 6 | 8 | 5 | 1 | 0 | 0 | 3 |

## 0018_4748191834

33.2 s video; humans: 14 objects, 17 relations on 15 pairs; TRASER: 29 relations on 26 pairs.

**Masks given to TRASER:** 13 of 14 objects (0 after the first 40, 1 with no mask on the frames TRASER reads)

**Pairs:** 5 in both, 9 missed by TRASER, 1 reversed, 0 with an object TRASER was not given, 21 only TRASER

**Objects: 10/14 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | ground | no: no mask on the frames TRASER reads | - (never shown to TRASER) | - | ✗ |
| 2 | floor | yes (object 1) | table | mismatch | ✗ |
| 3 | wall | yes (object 2) | wall | identical | ✓ |
| 4 | cookie | yes (object 3) | cake slice | semantic overlap | ✓ |
| 5 | door | yes (object 4) | cabinet door | hypernym/hyponym | ✓ |
| 6 | adult | yes (object 5) | person | hypernym/hyponym | ✓ |
| 7 | child | yes (object 6) | child | identical | ✓ |
| 8 | table | yes (object 7) | tablecloth | semantic overlap | ✓ |
| 9 | chair | yes (object 8) | chair backrest | hypernym/hyponym | ✓ |
| 10 | candle | yes (object 9) | candle | identical | ✓ |
| 11 | cake | yes (object 10) | cake | identical | ✓ |
| 12 | camera | yes (object 11) | knife | mismatch | ✗ |
| 13 | adult | yes (object 12) | shirt | mismatch | ✗ |
| 14 | chair | yes (object 13) | chair | identical | ✓ |

**Relations, pair by pair**

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

**Masks given to TRASER:** 15 of 15 objects

**Pairs:** 11 in both, 0 missed by TRASER, 0 reversed, 0 with an object TRASER was not given, 21 only TRASER

**Objects: 10/15 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | rock | yes (object 1) | fireplace | mismatch | ✗ |
| 2 | floor | yes (object 2) | baseboard | semantic overlap | ✓ |
| 3 | ceiling | yes (object 3) | curtain | mismatch | ✗ |
| 4 | wall | yes (object 4) | curtain | mismatch | ✗ |
| 5 | door | yes (object 5) | door frame | semantic overlap | ✓ |
| 6 | shelf | yes (object 6) | table | semantic overlap | ✓ |
| 7 | window | yes (object 7) | window | identical | ✓ |
| 8 | adult | yes (object 8) | person | hypernym/hyponym | ✓ |
| 9 | baby | yes (object 9) | child | hypernym/hyponym | ✓ |
| 10 | dog | yes (object 10) | plush toy | mismatch | ✗ |
| 11 | toy | yes (object 11) | toy | identical | ✓ |
| 12 | door | yes (object 12) | door | identical | ✓ |
| 13 | door | yes (object 13) | curtain | mismatch | ✗ |
| 14 | door | yes (object 14) | window | semantic overlap | ✓ |
| 15 | door | yes (object 15) | door | identical | ✓ |

**Relations, pair by pair**

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


## 1011_4633647136

53.6 s video; humans: 14 objects, 20 relations on 15 pairs; TRASER: 356 relations on 16 pairs (answer cut off at the token limit, read up to there).

**Masks given to TRASER:** 14 of 14 objects

**Pairs:** 6 in both, 9 missed by TRASER, 0 reversed, 0 with an object TRASER was not given, 10 only TRASER

**Objects: 12/14 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | ground | yes (object 1) | floor | synonym | ✓ |
| 2 | wall | yes (object 2) | painting | mismatch | ✗ |
| 3 | door | yes (object 3) | door | identical | ✓ |
| 4 | adult | yes (object 4) | person | hypernym/hyponym | ✓ |
| 5 | child | yes (object 5) | child | identical | ✓ |
| 6 | table | yes (object 6) | tablecloth | semantic overlap | ✓ |
| 7 | chair | yes (object 7) | chair | identical | ✓ |
| 8 | candle | yes (object 8) | bow | mismatch | ✗ |
| 9 | cake | yes (object 9) | cake | identical | ✓ |
| 10 | adult | yes (object 10) | person | hypernym/hyponym | ✓ |
| 11 | chair | yes (object 11) | chair | identical | ✓ |
| 12 | adult | yes (object 12) | person | hypernym/hyponym | ✓ |
| 13 | chair | yes (object 13) | chair | identical | ✓ |
| 14 | chair | yes (object 14) | chair | identical | ✓ |

**Relations, pair by pair**

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

**Masks given to TRASER:** 11 of 11 objects

**Pairs:** 6 in both, 1 missed by TRASER, 1 reversed, 0 with an object TRASER was not given, 20 only TRASER

**Objects: 10/11 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | floor | yes (object 1) | floor | identical | ✓ |
| 2 | wall | yes (object 2) | wall | identical | ✓ |
| 3 | carpet | yes (object 3) | doormat | hypernym/hyponym | ✓ |
| 4 | fence | yes (object 4) | gate | semantic overlap | ✓ |
| 5 | adult | yes (object 5) | child | hypernym/hyponym | ✓ |
| 6 | child | yes (object 6) | child | identical | ✓ |
| 7 | sofa | yes (object 7) | sofa | identical | ✓ |
| 8 | ballon | yes (object 8) | balloon | identical | ✓ |
| 9 | carpet | yes (object 9) | baseboard | semantic overlap | ✓ |
| 10 | adult | yes (object 10) | person | hypernym/hyponym | ✓ |
| 11 | ballon | yes (object 11) | ball | mismatch | ✗ |

**Relations, pair by pair**

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

**Masks given to TRASER:** 13 of 13 objects

**Pairs:** 2 in both, 6 missed by TRASER, 1 reversed, 0 with an object TRASER was not given, 11 only TRASER

**Objects: 10/13 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | tree | yes (object 1) | pole | mismatch | ✗ |
| 2 | grass | yes (object 2) | tennis ball | mismatch | ✗ |
| 3 | adult | yes (object 3) | person | hypernym/hyponym | ✓ |
| 4 | child | yes (object 4) | child | identical | ✓ |
| 5 | table | yes (object 5) | bench | semantic overlap | ✓ |
| 6 | hat | yes (object 6) | hand | mismatch | ✗ |
| 7 | bat | yes (object 7) | tennis racket | semantic overlap | ✓ |
| 8 | ball | yes (object 8) | soccer ball | hypernym/hyponym | ✓ |
| 9 | car | yes (object 9) | car | identical | ✓ |
| 10 | adult | yes (object 10) | person | hypernym/hyponym | ✓ |
| 11 | child | yes (object 11) | person | hypernym/hyponym | ✓ |
| 12 | car | yes (object 12) | car | identical | ✓ |
| 13 | car | yes (object 13) | car | identical | ✓ |

**Relations, pair by pair**

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

**Masks given to TRASER:** 11 of 11 objects

**Pairs:** 14 in both, 5 missed by TRASER, 0 reversed, 0 with an object TRASER was not given, 18 only TRASER

**Objects: 11/11 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | tree | yes (object 1) | Christmas tree | hypernym/hyponym | ✓ |
| 2 | floor | yes (object 2) | rug | semantic overlap | ✓ |
| 3 | gift | yes (object 3) | gift wrap | semantic overlap | ✓ |
| 4 | curtain | yes (object 4) | curtain | identical | ✓ |
| 5 | book | yes (object 5) | book | identical | ✓ |
| 6 | adult | yes (object 6) | person | hypernym/hyponym | ✓ |
| 7 | child | yes (object 7) | child | identical | ✓ |
| 8 | box | yes (object 8) | box | identical | ✓ |
| 9 | book | yes (object 9) | book | identical | ✓ |
| 10 | book | yes (object 10) | book | identical | ✓ |
| 11 | book | yes (object 11) | book | identical | ✓ |

**Relations, pair by pair**

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


## 1025_4615486172

90.0 s video; humans: 27 objects, 24 relations on 23 pairs; TRASER: 320 relations on 25 pairs (answer cut off at the token limit, read up to there).

**Masks given to TRASER:** 27 of 27 objects

**Pairs:** 3 in both, 19 missed by TRASER, 1 reversed, 0 with an object TRASER was not given, 22 only TRASER

**Objects: 21/27 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | rock | yes (object 1) | chair | mismatch | ✗ |
| 2 | floor | yes (object 2) | chair leg (uncertain) | mismatch | ✗ |
| 3 | ceiling | yes (object 3) | ceiling fan | semantic overlap | ✓ |
| 4 | wall | yes (object 4) | wall | identical | ✓ |
| 5 | door | yes (object 5) | door | identical | ✓ |
| 6 | curtain | yes (object 6) | door frame (uncertain) | mismatch | ✗ |
| 7 | shelf | yes (object 7) | bookshelf | hypernym/hyponym | ✓ |
| 8 | window | yes (object 8) | curtain | semantic overlap | ✓ |
| 9 | adult | yes (object 9) | person | hypernym/hyponym | ✓ |
| 10 | child | yes (object 10) | child | identical | ✓ |
| 11 | table | yes (object 11) | tablecloth | semantic overlap | ✓ |
| 12 | chair | yes (object 12) | table | mismatch | ✗ |
| 13 | candle | yes (object 13) | cake | semantic overlap | ✓ |
| 14 | cake | yes (object 14) | cake | identical | ✓ |
| 15 | cellphone | yes (object 15) | cell phone | identical | ✓ |
| 16 | ballon | yes (object 16) | balloon | identical | ✓ |
| 17 | chair | yes (object 17) | chair | identical | ✓ |
| 18 | ballon | yes (object 18) | balloon | identical | ✓ |
| 19 | adult | yes (object 19) | person | hypernym/hyponym | ✓ |
| 20 | chair | yes (object 20) | chair | identical | ✓ |
| 21 | ballon | yes (object 21) | balloon | identical | ✓ |
| 22 | adult | yes (object 22) | person | hypernym/hyponym | ✓ |
| 23 | chair | yes (object 23) | chair | identical | ✓ |
| 24 | ballon | yes (object 24) | chair | mismatch | ✗ |
| 25 | adult | yes (object 25) | person | hypernym/hyponym | ✓ |
| 26 | chair | yes (object 26) | chair | identical | ✓ |
| 27 | chair | yes (object 27) | person | mismatch | ✗ |

**Relations, pair by pair**

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| adult #9 → door #5 | entering [3.4-6.2s] | - | ✗ TRASER missed this pair | - |
| adult #9 → cake #14 | holding [2.2-29.2s, 76.8-90s] | - | ✗ TRASER missed this pair | - |
| child #10 → cake #14 | touching [75.4-77s] | - | ✗ TRASER missed this pair | - |
| child #10 → chair #27 | beside [5.2-90s] | - | ✗ TRASER missed this pair | - |
| chair #12 → ballon #16 | in front of [4.2-90s] | - | ✗ TRASER missed this pair | - |
| chair #12 → ballon #18 | in front of [4.2-90s] | - | ✗ TRASER missed this pair | - |
| candle #13 → cake #14 | on [2.8-90s] | - | ✗ TRASER missed this pair | - |
| cake #14 → table #11 | on [27.6-86.8s] | - | ✗ TRASER missed this pair | - |
| ballon #16 → wall #4 | on [4.2-90s] | - | ✗ TRASER missed this pair | - |
| ballon #16 → ballon #18 | next to [4.2-90s] | - | ✗ TRASER missed this pair | - |
| chair #17 → chair #12 | next to [4.2-90s] | - | ✗ TRASER missed this pair | - |
| ballon #18 → wall #4 | on [4.2-90s] | - | ✗ TRASER missed this pair | - |
| adult #19 → child #10 | holding [12.8-90s] | photographing [73-90s]; looking at [15-22s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s] | ✓ TRASER has this pair | ✗ |
| adult #19 → chair #12 | picking [31.6-35.4s] | photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s] | ✓ TRASER has this pair | ✗ |
| adult #19 → candle #13 | blowing [58.8-61.4s] | photographing [73-90s]; looking at [22-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s] | ✓ TRASER has this pair | ✗ |
| chair #20 → chair #17 | beside [4-90s] | - | ✗ TRASER missed this pair | - |
| ballon #21 → ceiling #3 | on [13.4-20s] | - | ✗ TRASER missed this pair | - |
| ballon #21 → table #11 | over [0-90s] | - | ✗ TRASER missed this pair | - |
| adult #22 → floor #2 | squatting on [50.4-90s] | - | ✗ TRASER missed this pair | - |
| adult #22 → child #10 | looking at [62-83s] | - | ✗ TRASER missed this pair | - |
| adult #22 → chair #12 | in front of [49.8-90s] | - | ✗ TRASER missed this pair | - |
| adult #22 → candle #13 | blowing [58.8-61.4s] | - | ✗ TRASER missed this pair | - |
| adult #22 → adult #19 | hugging [50.4-81.2s]; next to [49.2-90s] | - | ↔ TRASER has it reversed | - - |
| adult #19 → rock #1 | - | sitting on [77-90s]; photographing [77-90s]; photographing [77-90s]; photographing [77-90s]; photographing [77-90s]; photographing [77-90s]; photographing [77-90s]; photographing [77-90s]; photographing [77-90s]; photographing [77-90s] | + only TRASER | - |
| adult #19 → floor #2 | - | photographing [0-1s]; photographing [0-1s]; photographing [0-1s]; photographing [0-1s]; photographing [0-1s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s]; photographing [2-3s] | + only TRASER | - |
| adult #19 → ceiling #3 | - | photographing [11-15s]; photographing [11-15s]; photographing [11-15s]; photographing [11-15s] | + only TRASER | - |
| adult #19 → wall #4 | - | photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s] | + only TRASER | - |
| adult #19 → door #5 | - | photographing [11-15s]; photographing [11-15s]; photographing [11-15s]; photographing [11-15s] | + only TRASER | - |
| adult #19 → shelf #7 | - | photographing [11-15s]; photographing [11-15s]; photographing [11-15s]; photographing [11-15s]; photographing [11-15s] | + only TRASER | - |
| adult #19 → window #8 | - | photographing [11-15s]; photographing [11-15s]; photographing [11-15s]; photographing [11-15s] | + only TRASER | - |
| adult #19 → adult #9 | - | photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s] | + only TRASER | - |
| adult #19 → table #11 | - | photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s] | + only TRASER | - |
| adult #19 → cake #14 | - | photographing [73-90s]; looking at [22-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s] | + only TRASER | - |
| adult #19 → cellphone #15 | - | holding [73-90s]; looking at [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s] | + only TRASER | - |
| adult #19 → ballon #16 | - | photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s] | + only TRASER | - |
| adult #19 → chair #17 | - | sitting on [15-22s]; photographing [15-22s]; photographing [15-22s]; photographing [15-22s]; photographing [15-22s]; photographing [15-22s]; photographing [22-23s] | + only TRASER | - |
| adult #19 → ballon #18 | - | photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s] | + only TRASER | - |
| adult #19 → chair #20 | - | sitting on [11-15s]; photographing [11-15s]; photographing [11-15s]; photographing [15-22s]; photographing [15-22s]; photographing [15-22s]; photographing [15-22s]; photographing [22-23s] | + only TRASER | - |
| adult #19 → ballon #21 | - | photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s] | + only TRASER | - |
| adult #19 → adult #22 | - | photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s]; photographing [73-90s] | + only TRASER | - |
| adult #19 → chair #23 | - | sitting on [15-22s]; photographing [15-22s]; photographing [15-22s]; photographing [15-22s]; photographing [15-22s]; photographing [15-22s]; photographing [15-22s]; photographing [22-23s]; photographing [15-22s] | + only TRASER | - |
| adult #19 → ballon #24 | - | photographing [15-22s]; photographing [15-22s]; photographing [22-23s]; photographing [22-23s]; photographing [22-23s]; photographing [22-23s]; photographing [22-23s]; photographing [22-23s]; photographing [22-23s]; photographing [22-23s]; photographing [22-23s]; photographing [22-23s]; photographing [22-23s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s]; photographing [22-23s]; photographing [26-27s] | + only TRASER | - |
| adult #19 → adult #25 | - | photographing [11-15s]; photographing [11-15s]; photographing [11-15s]; photographing [11-15s]; photographing [11-15s]; photographing [11-15s]; photographing [11-15s]; photographing [11-15s] | + only TRASER | - |
| adult #19 → chair #26 | - | sitting on [15-22s]; photographing [15-22s]; photographing [15-22s]; photographing [15-22s]; photographing [15-22s]; photographing [15-22s]; photographing [15-22s]; photographing [15-22s]; photographing [22-23s]; photographing [15-22s] | + only TRASER | - |
| adult #19 → chair #27 | - | photographing [11-15s]; photographing [11-15s]; photographing [11-15s]; photographing [11-15s]; photographing [11-15s]; photographing [11-15s]; photographing [11-15s]; photographing [11-15s]; photographing [11-15s] | + only TRASER | - |


## P03_06

109.2 s video; humans: 65 objects, 20 relations on 16 pairs; TRASER: 276 relations on 23 pairs (answer cut off at the token limit, read up to there).

**Masks given to TRASER:** 39 of 65 objects (25 after the first 40, 1 with no mask on the frames TRASER reads)

**Pairs:** 8 in both, 3 missed by TRASER, 0 reversed, 5 with an object TRASER was not given, 15 only TRASER

**Objects: 19/65 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | floor | yes (object 1) | stove burner | mismatch | ✗ |
| 2 | wall | yes (object 2) | wall | identical | ✓ |
| 3 | cloth | yes (object 3) | handle (uncertain) | mismatch | ✗ |
| 4 | mat | yes (object 4) | chopping board | mismatch | ✗ |
| 5 | countertop | yes (object 5) | stove top | semantic overlap | ✓ |
| 6 | grain | yes (object 6) | spatula | mismatch | ✗ |
| 7 | simmering | yes (object 7) | pot | mismatch | ✗ |
| 8 | rack | yes (object 8) | countertop | semantic overlap | ✓ |
| 9 | spatula | yes (object 9) | spatula | identical | ✓ |
| 10 | chopstick | no: no mask on the frames TRASER reads | - (never shown to TRASER) | - | ✗ |
| 11 | teapot | yes (object 10) | kettle | synonym | ✓ |
| 12 | pot | yes (object 11) | pot | identical | ✓ |
| 13 | board | yes (object 12) | chopping board | hypernym/hyponym | ✓ |
| 14 | cover | yes (object 13) | stove burner | mismatch | ✗ |
| 15 | brush | yes (object 14) | bottle | mismatch | ✗ |
| 16 | rag | yes (object 15) | handle (uncertain) | mismatch | ✗ |
| 17 | dustbin | yes (object 16) | spoon | mismatch | ✗ |
| 18 | washer | yes (object 17) | handle (uncertain) | semantic overlap | ✓ |
| 19 | drawer | yes (object 18) | handle (uncertain) | mismatch | ✗ |
| 20 | oven | yes (object 19) | stove burner | semantic overlap | ✓ |
| 21 | stove | yes (object 20) | stove burner | hypernym/hyponym | ✓ |
| 22 | sponge | yes (object 21) | cup | mismatch | ✗ |
| 23 | cabinet | yes (object 22) | stove burner | mismatch | ✗ |
| 24 | door | yes (object 23) | wall | mismatch | ✗ |
| 25 | glass | yes (object 24) | glass cup | hypernym/hyponym | ✓ |
| 26 | spoon | yes (object 25) | spoon | identical | ✓ |
| 27 | towel | yes (object 26) | handle (uncertain) | mismatch | ✗ |
| 28 | basket | yes (object 27) | pot | mismatch | ✗ |
| 29 | adult | yes (object 28) | hand | mismatch | ✗ |
| 30 | sink | yes (object 29) | sink | identical | ✓ |
| 31 | faucet | yes (object 30) | faucet | identical | ✓ |
| 32 | table | yes (object 31) | handle (uncertain) | mismatch | ✗ |
| 33 | knife | yes (object 32) | knife | identical | ✓ |
| 34 | fork | yes (object 33) | handle (uncertain) | mismatch | ✗ |
| 35 | plate | yes (object 34) | lid (uncertain) | semantic overlap | ✓ |
| 36 | bowl | yes (object 35) | bowl | identical | ✓ |
| 37 | bottle | yes (object 36) | cup | semantic overlap | ✓ |
| 38 | box | yes (object 37) | handle (uncertain) | mismatch | ✗ |
| 39 | mat | yes (object 38) | chopping board | mismatch | ✗ |
| 40 | grain | yes (object 39) | rice | hypernym/hyponym | ✓ |
| 41 | simmering | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 42 | rack | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 43 | pot | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 44 | cover | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 45 | oven | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 46 | cabinet | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 47 | glass | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 48 | spoon | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 49 | basket | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 50 | knife | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 51 | plate | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 52 | bowl | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 53 | bottle | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 54 | cup | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 55 | paper | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 56 | grain | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 57 | simmering | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 58 | pot | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 59 | basket | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 60 | knife | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 61 | plate | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 62 | bottle | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 63 | pot | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 64 | plate | no: after the first 40 | - (never shown to TRASER) | - | ✗ |
| 65 | plate | no: after the first 40 | - (never shown to TRASER) | - | ✗ |

**Relations, pair by pair**

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| rag #16 → oven #20 | hanging from [0-109.2s] | - | ✗ TRASER missed this pair | - |
| adult #29 → grain #6 | stirring [28.2-35.6s] | holding [30.055-65.1193s] | ✓ TRASER has this pair | ✗ |
| adult #29 → simmering #7 | stirring [3.8-42.8s] | stirring [30.055-65.1193s]; pouring into [71.1303-92.1688s] | ✓ TRASER has this pair | ✗ |
| adult #29 → spatula #9 | holding [2.8-9s, 66-69s] | holding [28.0514-31.0569s] | ✓ TRASER has this pair | ✗ |
| adult #29 → pot #12 | touching [3.4-8.8s]; holding [69.4-99.6s] | holding [71.1303-92.1688s] | ✓ TRASER has this pair | ✗ ✓ |
| adult #29 → drawer #19 | opening [24.6-26.6s, 101-101.8s]; pulling [25.2-26.4s, 101-102.4s] | - | ✗ TRASER missed this pair | - - |
| adult #29 → stove #21 | touching [9.2-10s] | holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s] | ✓ TRASER has this pair | ✗ |
| adult #29 → glass #25 | holding [13.4-13.8s] | holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s] | ✓ TRASER has this pair | ✗ |
| adult #29 → spoon #26 | holding [26.4-97.2s] | holding [30.055-65.1193s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s] | ✓ TRASER has this pair | ✗ |
| adult #29 → knife #33 | holding [102.2-109.2s] | holding [66.1211-71.1303s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s] | ✓ TRASER has this pair | ✓ |
| adult #29 → fork #34 | holding [103-109.2s] | - | ✗ TRASER missed this pair | - |
| adult #29 → pot #43 | touching [10.2-12.6s]; holding [20.8-23.2s, 28-62.8s] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - - |
| adult #29 → cover #44 | holding [10.2-12.2s] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| adult #29 → cabinet #46 | opening [14.2-15s] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| adult #29 → plate #64 | holding [15-19.6s] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| adult #29 → plate #65 | holding [15.4-19.4s]; touching [63-64.8s] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - - |
| adult #29 → floor #1 | - | holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s] | + only TRASER | - |
| adult #29 → mat #4 | - | holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s] | + only TRASER | - |
| adult #29 → teapot #11 | - | holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s] | + only TRASER | - |
| adult #29 → board #13 | - | holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s] | + only TRASER | - |
| adult #29 → cover #14 | - | holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s] | + only TRASER | - |
| adult #29 → brush #15 | - | holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s] | + only TRASER | - |
| adult #29 → dustbin #17 | - | holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s] | + only TRASER | - |
| adult #29 → oven #20 | - | holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s] | + only TRASER | - |
| adult #29 → sponge #22 | - | holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s] | + only TRASER | - |
| adult #29 → sink #30 | - | holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s] | + only TRASER | - |
| adult #29 → faucet #31 | - | holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s] | + only TRASER | - |
| adult #29 → bowl #36 | - | holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s] | + only TRASER | - |
| adult #29 → bottle #37 | - | holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s] | + only TRASER | - |
| adult #29 → mat #39 | - | holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s] | + only TRASER | - |
| adult #29 → grain #40 | - | holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s]; holding [104.191-109.2s] | + only TRASER | - |


## P14_06

64.6 s video; humans: 34 objects, 10 relations on 7 pairs; TRASER: 203 relations on 29 pairs (answer cut off at the token limit, read up to there).

**Masks given to TRASER:** 34 of 34 objects

**Pairs:** 0 in both, 7 missed by TRASER, 0 reversed, 0 with an object TRASER was not given, 29 only TRASER

**Objects: 24/34 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | floor | yes (object 1) | person | mismatch | ✗ |
| 2 | wall | yes (object 2) | wall | identical | ✓ |
| 3 | countertop | yes (object 3) | countertop | identical | ✓ |
| 4 | grain | yes (object 4) | bowl | mismatch | ✗ |
| 5 | beverage | yes (object 5) | box | mismatch | ✗ |
| 6 | rack | yes (object 6) | dish rack | hypernym/hyponym | ✓ |
| 7 | cover | yes (object 7) | plate (uncertain) | semantic overlap | ✓ |
| 8 | carpet | yes (object 8) | doormat | hypernym/hyponym | ✓ |
| 9 | dustbin | yes (object 9) | plastic bag | mismatch | ✗ |
| 10 | stairs | yes (object 10) | drawer front (uncertain) | mismatch | ✗ |
| 11 | sponge | yes (object 11) | sponge | identical | ✓ |
| 12 | shelf | yes (object 12) | shelf | identical | ✓ |
| 13 | window | yes (object 13) | pipe (uncertain) | mismatch | ✗ |
| 14 | cabinet | yes (object 14) | sink | mismatch | ✗ |
| 15 | door | yes (object 15) | cabinet door | hypernym/hyponym | ✓ |
| 16 | fridge | yes (object 16) | refrigerator | synonym | ✓ |
| 17 | spoon | yes (object 17) | knife | mismatch | ✗ |
| 18 | scissor | yes (object 18) | scissors | identical | ✓ |
| 19 | adult | yes (object 19) | arm | mismatch | ✗ |
| 20 | sink | yes (object 20) | sink | identical | ✓ |
| 21 | faucet | yes (object 21) | faucet | identical | ✓ |
| 22 | table | yes (object 22) | countertop | semantic overlap | ✓ |
| 23 | knife | yes (object 23) | knife | identical | ✓ |
| 24 | plate | yes (object 24) | plate | identical | ✓ |
| 25 | bowl | yes (object 25) | plate | semantic overlap | ✓ |
| 26 | cup | yes (object 26) | cup | identical | ✓ |
| 27 | paper | yes (object 27) | paper (uncertain) | identical | ✓ |
| 28 | box | yes (object 28) | box | identical | ✓ |
| 29 | beverage | yes (object 29) | bowl | mismatch | ✗ |
| 30 | cabinet | yes (object 30) | cabinet door | semantic overlap | ✓ |
| 31 | door | yes (object 31) | cabinet door | hypernym/hyponym | ✓ |
| 32 | plate | yes (object 32) | plate | identical | ✓ |
| 33 | bowl | yes (object 33) | bowl | identical | ✓ |
| 34 | bowl | yes (object 34) | plate | semantic overlap | ✓ |

**Relations, pair by pair**

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| beverage #5 → table #22 | on [17.8-19.6s] | - | ✗ TRASER missed this pair | - |
| adult #19 → beverage #5 | holding [13.2-40.8s]; opening [17.8-19.8s] | - | ✗ TRASER missed this pair | - - |
| adult #19 → fridge #16 | opening [10.4-12s, 35.8-38.2s]; closing [13.8-15.2s, 41.6-43s] | - | ✗ TRASER missed this pair | - - |
| adult #19 → spoon #17 | holding [60.2-64.6s] | - | ✗ TRASER missed this pair | - |
| adult #19 → box #28 | holding [45.6-57.4s] | - | ✗ TRASER missed this pair | - |
| adult #19 → bowl #33 | holding [4.2-9s]; touching [21-21.6s] | - | ✗ TRASER missed this pair | - - |
| bowl #33 → table #22 | on [9-64.6s] | - | ✗ TRASER missed this pair | - |
| floor #1 → floor #1 | - | placing [61.6185-63.6062s] | + only TRASER | - |
| floor #1 → wall #2 | - | placing [61.6185-63.6062s]; in front of [0-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s] | + only TRASER | - |
| floor #1 → grain #4 | - | holding [57.6431-61.6185s]; placing [57.6431-61.6185s]; in front of [57.6431-63.6062s]; in front of [57.6431-63.6062s]; in front of [57.6431-63.6062s]; in front of [57.6431-63.6062s]; in front of [57.6431-63.6062s]; in front of [57.6431-63.6062s] | + only TRASER | - |
| floor #1 → beverage #5 | - | holding [17.8892-36.7723s]; placing [35.7785-37.7662s]; in front of [17.8892-36.7723s]; in front of [17.8892-36.7723s]; in front of [17.8892-36.7723s]; in front of [17.8892-36.7723s]; in front of [17.8892-36.7723s]; in front of [17.8892-36.7723s] | + only TRASER | - |
| floor #1 → rack #6 | - | in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s] | + only TRASER | - |
| floor #1 → carpet #8 | - | in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s] | + only TRASER | - |
| floor #1 → dustbin #9 | - | in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s] | + only TRASER | - |
| floor #1 → sponge #11 | - | placing [61.6185-63.6062s]; placing [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s] | + only TRASER | - |
| floor #1 → shelf #12 | - | placing [61.6185-63.6062s]; in front of [3.97538-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s] | + only TRASER | - |
| floor #1 → cabinet #14 | - | in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s] | + only TRASER | - |
| floor #1 → door #15 | - | placing [61.6185-63.6062s]; in front of [0-3.97538s, 5.96308-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s] | + only TRASER | - |
| floor #1 → fridge #16 | - | placing [61.6185-63.6062s]; in front of [0-3.97538s, 5.96308-15.9015s, 16.8954-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-15.9015s, 16.8954-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s] | + only TRASER | - |
| floor #1 → spoon #17 | - | placing [61.6185-63.6062s]; placing [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s] | + only TRASER | - |
| floor #1 → scissor #18 | - | placing [61.6185-63.6062s]; in front of [5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s] | + only TRASER | - |
| floor #1 → adult #19 | - | in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s] | + only TRASER | - |
| floor #1 → sink #20 | - | in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s] | + only TRASER | - |
| floor #1 → faucet #21 | - | placing [61.6185-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [0-3.97538s, 5.96308-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s] | + only TRASER | - |
| floor #1 → table #22 | - | in front of [0-3.97538s, 5.96308-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s] | + only TRASER | - |
| floor #1 → knife #23 | - | placing [61.6185-63.6062s]; placing [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s] | + only TRASER | - |
| floor #1 → plate #24 | - | placing [61.6185-63.6062s]; placing [61.6185-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [61.6185-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s] | + only TRASER | - |
| floor #1 → bowl #25 | - | placing [61.6185-63.6062s]; placing [61.6185-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [61.6185-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s] | + only TRASER | - |
| floor #1 → cup #26 | - | placing [61.6185-63.6062s]; placing [61.6185-63.6062s]; packing groceries into [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s] | + only TRASER | - |
| floor #1 → box #28 | - | holding [46.7108-57.6431s]; placing [57.6431-61.6185s]; packing groceries into [46.7108-57.6431s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s] | + only TRASER | - |
| floor #1 → beverage #29 | - | holding [46.7108-57.6431s]; placing [46.7108-57.6431s]; in front of [46.7108-57.6431s]; in front of [46.7108-57.6431s]; in front of [46.7108-57.6431s]; in front of [46.7108-57.6431s]; in front of [46.7108-57.6431s]; in front of [46.7108-57.6431s]; in front of [46.7108-57.6431s]; in front of [46.7108-57.6431s]; in front of [46.7108-57.6431s]; in front of [46.7108-57.6431s] | + only TRASER | - |
| floor #1 → cabinet #30 | - | placing [61.6185-63.6062s]; in front of [7.95077-11.9262s, 32.7969-35.7785s, 61.6185-63.6062s]; in front of [7.95077-11.9262s, 32.7969-35.7785s, 61.6185-63.6062s]; in front of [7.95077-11.9262s, 32.7969-35.7785s, 61.6185-63.6062s]; in front of [7.95077-11.9262s, 32.7969-35.7785s, 61.6185-63.6062s] | + only TRASER | - |
| floor #1 → door #31 | - | placing [61.6185-63.6062s]; in front of [0-3.97538s, 5.96308-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s] | + only TRASER | - |
| floor #1 → plate #32 | - | placing [61.6185-63.6062s]; placing [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s] | + only TRASER | - |
| floor #1 → bowl #33 | - | in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [61.6185-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [61.6185-63.6062s]; in front of [0-3.97538s, 5.96308-7.95077s, 15.9015-35.7785s, 39.7538-45.7169s, 46.7108-57.6431s, 58.6369-63.6062s]; in front of [61.6185-63.6062s] | + only TRASER | - |
| floor #1 → bowl #34 | - | placing [61.6185-63.6062s]; placing [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s]; in front of [61.6185-63.6062s] | + only TRASER | - |


## P28_19

90.0 s video; humans: 28 objects, 10 relations on 6 pairs; TRASER: 18 relations on 8 pairs.

**Masks given to TRASER:** 27 of 28 objects (0 after the first 40, 1 with no mask on the frames TRASER reads)

**Pairs:** 5 in both, 1 missed by TRASER, 0 reversed, 0 with an object TRASER was not given, 3 only TRASER

**Objects: 17/28 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | floor | yes (object 1) | chopping board | mismatch | ✗ |
| 2 | wall | yes (object 2) | countertop | mismatch | ✗ |
| 3 | egg | yes (object 3) | tomato | mismatch | ✗ |
| 4 | others | yes (object 4) | tortilla (uncertain) | hypernym/hyponym | ✓ |
| 5 | countertop | yes (object 5) | countertop | identical | ✓ |
| 6 | spatula | yes (object 6) | spatula | identical | ✓ |
| 7 | board | yes (object 7) | chopping board | hypernym/hyponym | ✓ |
| 8 | rag | yes (object 8) | chair | mismatch | ✗ |
| 9 | dustbin | yes (object 9) | pot | mismatch | ✗ |
| 10 | oven | yes (object 10) | cabinet door | mismatch | ✗ |
| 11 | stove | yes (object 11) | stove top | hypernym/hyponym | ✓ |
| 12 | pan | yes (object 12) | frying pan | hypernym/hyponym | ✓ |
| 13 | window | yes (object 13) | tray | mismatch | ✗ |
| 14 | cabinet | yes (object 14) | drawer front | semantic overlap | ✓ |
| 15 | door | yes (object 15) | cabinet door | hypernym/hyponym | ✓ |
| 16 | adult | yes (object 16) | arm | mismatch | ✗ |
| 17 | sink | yes (object 17) | sink | identical | ✓ |
| 18 | knife | yes (object 18) | spoon | semantic overlap | ✓ |
| 19 | plate | yes (object 19) | tray | semantic overlap | ✓ |
| 20 | bottle | yes (object 20) | bottle | identical | ✓ |
| 21 | bag | yes (object 21) | aluminum foil | mismatch | ✗ |
| 22 | box | yes (object 22) | box | identical | ✓ |
| 23 | countertop | yes (object 23) | countertop | identical | ✓ |
| 24 | window | no: no mask on the frames TRASER reads | - (never shown to TRASER) | - | ✗ |
| 25 | cabinet | yes (object 24) | cabinet door | semantic overlap | ✓ |
| 26 | vegetable | yes (object 25) | onions | hypernym/hyponym | ✓ |
| 27 | bag | yes (object 26) | napkin | mismatch | ✗ |
| 28 | box | yes (object 27) | bag | semantic overlap | ✓ |

**Relations, pair by pair**

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| adult #16 → stove #11 | touching [60.4-70.8s] | - | ✗ TRASER missed this pair | - |
| adult #16 → pan #12 | swinging [71.2-79.4s]; holding [82.6-83.8s]; over [84.2-88s] | pouring into [45-51s]; holding [45-51s, 72-89s]; stirring [72-89s]; cooking with [72-89s]; transferring to [45-51s]; adding to [45-51s]; serving onto [72-89s] | ✓ TRASER has this pair | ✗ ✗ ✗ |
| adult #16 → knife #18 | holding [1.4-43.2s] | holding [41-43s] | ✓ TRASER has this pair | ✗ |
| adult #16 → bottle #20 | holding [43-52.4s]; opening [45-46.2s] | holding [44-51s]; holding [44-51s] | ✓ TRASER has this pair | ✓ ✗ |
| adult #16 → box #22 | holding [53.2-59.2s] | holding [52-57s]; holding [52-57s] | ✓ TRASER has this pair | ✓ |
| adult #16 → vegetable #26 | holding [1.4-42s]; cutting [2.8-39.6s] | cutting [3-43s]; preparing food [3-43s] | ✓ TRASER has this pair | ✗ ✓ |
| adult #16 → spatula #6 | - | holding [41-43s] | + only TRASER | - |
| adult #16 → window #13 | - | holding [52-57s] | + only TRASER | - |
| adult #16 → box #28 | - | holding [89-91s]; holding [89-91s] | + only TRASER | - |

