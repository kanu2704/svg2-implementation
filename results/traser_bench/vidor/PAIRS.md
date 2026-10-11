# vidor: which object pairs TRASER talks about (10 random videos, seed 0)

TRASER is given the human objects (masks) and writes its own list of relations; it is not told which pairs to describe. Each row is one ordered pair (subject → object) that the humans or TRASER mention.

- **✓ TRASER has this pair**: TRASER wrote at least one relation for the same two objects, same direction
- **✗ TRASER missed this pair**: humans annotated it, TRASER said nothing about these two objects
- **↔ reversed**: TRASER only has the other direction (object → subject); scored as missed
- **⊘ object not given**: one of the two objects was not among the (at most 40) objects TRASER received, so it could not answer; scored as missed in the main score (README.md also shows a score that leaves these out)
- **mask given to TRASER?** (objects table): yes, with the number TRASER calls it ("object k"); or no, because the run gives only the first 40 objects by number, or because the object has no mask on the frames TRASER reads (about 1 per second)
- **+ only TRASER**: TRASER describes a pair the humans did not annotate (ignored by the scores)
- **both masks given?**: ✓ if TRASER got the masks of both objects of the pair in its input (the camera always counts as given), ✗ and which object was missing otherwise
- **both objects named right?**: ✓ if TRASER's labels for both objects are right (lenient: not a mismatch), ✗ and which one is wrong (named wrong, or not given so never named)
- **relation right?**, one mark per human relation of the pair: ✓ same two objects, relation word right and tIoU > 0.5; ✗ not; - TRASER wrote nothing for this pair; ? the judge has not compared the words yet. The object names do not matter here (paper's definition)
- **triplet right?**, one mark per human relation: ✓ only if the relation is right AND both objects are named right

**Total over these videos:** 150 human pairs, 84 TRASER pairs; 60 in both, 42 missed, 46 reversed, 2 with an object not given, 24 only TRASER.

| video | source | masks given to TRASER | objects right | relations right | triplets right | human pairs | TRASER pairs | pairs in both | missed by TRASER | reversed | object not given | only TRASER |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [13624759154](#13624759154) | - | 4/5 | 4/5 | 4/22 | 4/22 | 12 | 6 | 6 | 0 | 6 | 0 | 0 |
| [3829541530](#3829541530) | - | 2/2 | 2/2 | 1/2 | 1/2 | 2 | 1 | 1 | 0 | 1 | 0 | 0 |
| [4146348376](#4146348376) | - | 5/5 | 4/5 | 0/9 | 0/9 | 2 | 11 | 1 | 0 | 1 | 0 | 10 |
| [4674481985](#4674481985) | - | 4/6 | 4/6 | 1/17 | 1/17 | 13 | 6 | 6 | 0 | 5 | 2 | 0 |
| [4822859674](#4822859674) | - | 10/10 | 8/10 | 4/85 | 4/85 | 45 | 16 | 12 | 24 | 9 | 0 | 4 |
| [4925211209](#4925211209) | - | 2/2 | 1/2 | 0/3 | 0/3 | 2 | 1 | 1 | 0 | 1 | 0 | 0 |
| [5421648216](#5421648216) | - | 3/3 | 3/3 | 0/32 | 0/32 | 6 | 3 | 3 | 0 | 3 | 0 | 0 |
| [5658916668](#5658916668) | - | 9/9 | 8/9 | 0/35 | 0/35 | 21 | 15 | 6 | 12 | 3 | 0 | 9 |
| [8563398032](#8563398032) | - | 6/6 | 6/6 | 3/36 | 3/36 | 25 | 12 | 12 | 6 | 7 | 0 | 0 |
| [9217939684](#9217939684) | - | 6/6 | 5/6 | 0/112 | 0/112 | 22 | 13 | 12 | 0 | 10 | 0 | 1 |

## 13624759154

11.05 s video; humans: 5 objects, 22 relations on 12 pairs; TRASER: 12 relations on 6 pairs.

**Masks given to TRASER:** 4 of 5 objects (0 after the first 40, 1 with no mask on the frames TRASER reads)

**Pairs:** 6 in both, 0 missed by TRASER, 6 reversed, 0 with an object TRASER was not given, 0 only TRASER

**Objects: 4/5 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | adult | yes (object 1) | person | hypernym/hyponym | ✓ |
| 1 | adult | yes (object 2) | person | hypernym/hyponym | ✓ |
| 2 | adult | yes (object 3) | child | hypernym/hyponym | ✓ |
| 3 | table | yes (object 4) | table | identical | ✓ |
| 4 | screen/monitor | no: no mask on the frames TRASER reads | - (never shown to TRASER) | - | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| adult #0 → adult #1 | ✓ | ✓ | watch [0-4.04571s]; watch [7.75775-8.42508s]; watch [10.6773-11.0527s]; in front of [0-11.011s] | collaborating with [0-11.05s] | ✓ TRASER has this pair | ✗ ✗ ✗ ✗ | ✗ ✗ ✗ ✗ |
| adult #0 → adult #2 | ✓ | ✓ | in front of [0-11.011s] | collaborating with [0-11.05s] | ✓ TRASER has this pair | ✗ | ✗ |
| adult #0 → table #3 | ✓ | ✓ | next to [0-11.011s] | touching [0-11.05s]; looking at [0-11.05s]; working on [0-11.05s] | ✓ TRASER has this pair | ✓ | ✓ |
| adult #1 → adult #0 | ✓ | ✓ | watch [0.75075-7.63262s]; watch [8.5085-11.0527s]; speak to [1.08442-10.7607s]; in front of [0-11.011s] | - | ↔ TRASER has it reversed | - - - - | - - - - |
| adult #1 → adult #2 | ✓ | ✓ | watch [8.13312-8.59192s]; point to [8.21654-8.55021s]; next to [0-11.011s] | collaborating with [0-11.05s] | ✓ TRASER has this pair | ✗ ✗ ✗ | ✗ ✗ ✗ |
| adult #1 → table #3 | ✓ | ✓ | next to [0-11.011s] | touching [0-11.05s]; looking at [0-11.05s]; working on [0-11.05s] | ✓ TRASER has this pair | ✓ | ✓ |
| adult #2 → adult #0 | ✓ | ✓ | in front of [0-11.011s] | - | ↔ TRASER has it reversed | - | - |
| adult #2 → adult #1 | ✓ | ✓ | watch [9.75975-10.2185s]; next to [0-11.011s] | - | ↔ TRASER has it reversed | - - | - - |
| adult #2 → table #3 | ✓ | ✓ | lean on [2.96129-11.0527s]; next to [0-11.011s] | touching [0-11.05s]; looking at [0-11.05s]; working on [0-11.05s] | ✓ TRASER has this pair | ✓ ✓ | ✓ ✓ |
| table #3 → adult #0 | ✓ | ✓ | next to [0-11.011s] | - | ↔ TRASER has it reversed | - | - |
| table #3 → adult #1 | ✓ | ✓ | next to [0-11.011s] | - | ↔ TRASER has it reversed | - | - |
| table #3 → adult #2 | ✓ | ✓ | next to [0-11.011s] | - | ↔ TRASER has it reversed | - | - |


## 3829541530

5.81 s video; humans: 2 objects, 2 relations on 2 pairs; TRASER: 3 relations on 1 pairs.

**Masks given to TRASER:** 2 of 2 objects

**Pairs:** 1 in both, 0 missed by TRASER, 1 reversed, 0 with an object TRASER was not given, 0 only TRASER

**Objects: 2/2 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | adult | yes (object 1) | person | hypernym/hyponym | ✓ |
| 1 | adult | yes (object 2) | person | hypernym/hyponym | ✓ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| adult #0 → adult #1 | ✓ | ✓ | in front of [1.1011-5.77243s] | approaches [0-3.87333s]; moves away from [3.87333-6.77833s]; in front of [0-6.77833s] | ✓ TRASER has this pair | ✓ | ✓ |
| adult #1 → adult #0 | ✓ | ✓ | in front of [1.1011-5.77243s] | - | ↔ TRASER has it reversed | - | - |


## 4146348376

52.89 s video; humans: 5 objects, 9 relations on 2 pairs; TRASER: 15 relations on 11 pairs.

**Masks given to TRASER:** 5 of 5 objects

**Pairs:** 1 in both, 0 missed by TRASER, 1 reversed, 0 with an object TRASER was not given, 10 only TRASER

**Objects: 4/5 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | bird | yes (object 1) | bird | identical | ✓ |
| 1 | adult | yes (object 2) | person | hypernym/hyponym | ✓ |
| 2 | adult | yes (object 3) | person | hypernym/hyponym | ✓ |
| 3 | table | yes (object 4) | table | identical | ✓ |
| 4 | table | yes (object 5) | bowl | mismatch | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| adult #1 → table #3 | ✓ | ✓ | lean on [1.66833-8.77543s]; lean on [11.7784-32.2656s]; lean on [37.1705-39.039s]; next to [2.002-8.77543s]; next to [12.012-32.2656s]; next to [37.1705-39.0056s] | behind [0-10.9772s, 11.9751-27.9419s, 29.9377-31.9336s, 37.9211-40.9149s] | ✓ TRASER has this pair | ✗ ✗ ✗ ✗ ✗ ✗ | ✗ ✗ ✗ ✗ ✗ ✗ |
| table #3 → adult #1 | ✓ | ✓ | in front of [2.002-8.77543s]; in front of [12.012-32.2656s]; in front of [37.1705-39.0056s] | - | ↔ TRASER has it reversed | - - - | - - - |
| bird #0 → adult #1 | ✓ | ✓ | - | approaching [8.98132-10.9772s]; moving away from [9.97925-11.9751s]; in front of [0-3.9917s, 8.98132-10.9772s, 11.9751-12.973s, 13.9709-16.9647s, 17.9626-27.9419s, 29.9377-31.9336s] | + only TRASER | - | - |
| bird #0 → adult #2 | ✓ | ✓ | - | approaching [8.98132-10.9772s]; in front of [8.98132-10.9772s] | + only TRASER | - | - |
| bird #0 → table #3 | ✓ | ✓ | - | behind [0-3.9917s, 8.98132-10.9772s, 11.9751-12.973s, 13.9709-16.9647s, 17.9626-27.9419s, 29.9377-31.9336s, 37.9211-53.8879s] | + only TRASER | - | - |
| adult #1 → bird #0 | ✓ | ✓ | - | looking at [0-3.9917s, 8.98132-10.9772s, 11.9751-12.973s, 13.9709-16.9647s, 17.9626-27.9419s, 29.9377-31.9336s]; feeding [13.9709-16.9647s, 17.9626-27.9419s, 29.9377-31.9336s] | + only TRASER | - | - |
| adult #1 → table #4 | ✓ | ✗ (table #4 named wrong) | - | looking at [31.9336-33.9294s] | + only TRASER | - | - |
| adult #2 → bird #0 | ✓ | ✓ | - | looking at [8.98132-10.9772s] | + only TRASER | - | - |
| adult #2 → table #3 | ✓ | ✓ | - | behind [8.98132-10.9772s] | + only TRASER | - | - |
| table #4 → adult #1 | ✓ | ✗ (table #4 named wrong) | - | in front of [31.9336-33.9294s] | + only TRASER | - | - |
| table #4 → adult #2 | ✓ | ✗ (table #4 named wrong) | - | in front of [31.9336-33.9294s] | + only TRASER | - | - |
| table #4 → table #3 | ✓ | ✗ (table #4 named wrong) | - | on [31.9336-33.9294s] | + only TRASER | - | - |


## 4674481985

24.49 s video; humans: 6 objects, 17 relations on 13 pairs; TRASER: 11 relations on 6 pairs.

**Masks given to TRASER:** 4 of 6 objects (0 after the first 40, 2 with no mask on the frames TRASER reads)

**Pairs:** 6 in both, 0 missed by TRASER, 5 reversed, 2 with an object TRASER was not given, 0 only TRASER

**Objects: 4/6 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | adult | yes (object 1) | person | hypernym/hyponym | ✓ |
| 1 | adult | yes (object 2) | person | hypernym/hyponym | ✓ |
| 2 | adult | yes (object 3) | person | hypernym/hyponym | ✓ |
| 3 | adult | no: no mask on the frames TRASER reads | - (never shown to TRASER) | - | ✗ |
| 4 | adult | no: no mask on the frames TRASER reads | - (never shown to TRASER) | - | ✗ |
| 5 | adult | yes (object 4) | person | hypernym/hyponym | ✓ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| adult #0 → adult #1 | ✓ | ✓ | next to [0-6.4064s] | approaches [0-6.1225s]; moves away from [6.1225-9.18375s]; in front of [0-9.18375s] | ✓ TRASER has this pair | ✗ | ✗ |
| adult #0 → adult #2 | ✓ | ✓ | in front of [0.467133-2.5025s] | approaches [0-4.08167s]; in front of [0-4.08167s] | ✓ TRASER has this pair | ✗ | ✗ |
| adult #0 → adult #5 | ✓ | ✓ | behind [0-11.011s]; away [8.008-11.011s] | approaches [0-7.14292s]; moves away from [7.14292-10.2042s]; in front of [0-10.2042s] | ✓ TRASER has this pair | ✗ ✓ | ✗ ✓ |
| adult #1 → adult #0 | ✓ | ✓ | watch [2.33567-3.03637s]; next to [0-6.4064s] | - | ↔ TRASER has it reversed | - - | - - |
| adult #1 → adult #2 | ✓ | ✓ | watch [0.467133-2.002s]; in front of [0.467133-2.5025s] | in front of [0-4.08167s] | ✓ TRASER has this pair | ✗ ✗ | ✗ ✗ |
| adult #1 → adult #5 | ✓ | ✓ | behind [0-6.4064s] | in front of [0-9.18375s] | ✓ TRASER has this pair | ✗ | ✗ |
| adult #2 → adult #1 | ✓ | ✓ | watch [0.467133-2.5025s]; in front of [0.467133-2.5025s] | - | ↔ TRASER has it reversed | - - | - - |
| adult #2 → adult #5 | ✓ | ✓ | behind [0.467133-2.5025s] | in front of [0-4.08167s] | ✓ TRASER has this pair | ✗ | ✗ |
| adult #3 → adult #1 | ✗ (adult #3 not given) | ✗ (adult #3 not given) | watch [0.767433-0.967633s] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - | - |
| adult #4 → adult #0 | ✗ (adult #4 not given) | ✗ (adult #4 not given) | watch [0.6006-1.03437s] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - | - |
| adult #5 → adult #0 | ✓ | ✓ | behind [0-11.011s] | - | ↔ TRASER has it reversed | - | - |
| adult #5 → adult #1 | ✓ | ✓ | behind [0-6.4064s] | - | ↔ TRASER has it reversed | - | - |
| adult #5 → adult #2 | ✓ | ✓ | in front of [0.467133-2.5025s] | - | ↔ TRASER has it reversed | - | - |


## 4822859674

35.91 s video; humans: 10 objects, 85 relations on 45 pairs; TRASER: 16 relations on 16 pairs.

**Masks given to TRASER:** 10 of 10 objects

**Pairs:** 12 in both, 24 missed by TRASER, 9 reversed, 0 with an object TRASER was not given, 4 only TRASER

**Objects: 8/10 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | baby | yes (object 1) | child | hypernym/hyponym | ✓ |
| 1 | baby | yes (object 2) | child | hypernym/hyponym | ✓ |
| 2 | adult | yes (object 3) | person | hypernym/hyponym | ✓ |
| 3 | child | yes (object 4) | child | identical | ✓ |
| 4 | chair | yes (object 5) | chair | identical | ✓ |
| 5 | table | yes (object 6) | table | identical | ✓ |
| 6 | sofa | yes (object 7) | sofa | identical | ✓ |
| 7 | adult | yes (object 8) | chair | mismatch | ✗ |
| 8 | sofa | yes (object 9) | couch | synonym | ✓ |
| 9 | adult | yes (object 10) | arm (uncertain) | mismatch | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| baby #0 → baby #1 | ✓ | ✓ | watch [18.5602-19.2275s]; in front of [10.5522-20.9793s] | - | ✗ TRASER missed this pair | - - | - - |
| baby #0 → adult #2 | ✓ | ✓ | in front of [0-25.7757s] | in front of [0-27.93s] | ✓ TRASER has this pair | ✓ | ✓ |
| baby #0 → sofa #6 | ✓ | ✓ | in front of [12.304-14.1391s] | in front of [11.97-14.9625s] | ✓ TRASER has this pair | ✓ | ✓ |
| baby #0 → adult #9 | ✓ | ✗ (adult #9 named wrong) | watch [0-5.88087s]; watch [10.2602-13.8055s]; in front of [0-5.88087s]; in front of [10.2602-13.8055s] | - | ✗ TRASER missed this pair | - - - - | - - - - |
| baby #1 → baby #0 | ✓ | ✓ | watch [10.5522-13.3467s]; watch [16.5999-17.2672s]; next to [10.5522-14.9733s]; away [12.012-15.015s]; behind [14.014-19.019s] | - | ✗ TRASER missed this pair | - - - - - | - - - - - |
| baby #1 → adult #2 | ✓ | ✓ | in front of [10.5522-33.742s]; away [32.032-33.742s] | in front of [9.975-34.9125s] | ✓ TRASER has this pair | ✓ ✗ | ✓ ✗ |
| baby #1 → child #3 | ✓ | ✓ | away [32.032-35.035s] | - | ✗ TRASER missed this pair | - | - |
| baby #1 → chair #4 | ✓ | ✓ | away [32.032-35.035s] | in front of [30.9225-34.9125s] | ✓ TRASER has this pair | ✗ | ✗ |
| baby #1 → table #5 | ✓ | ✓ | towards [14.014-17.017s]; away [32.032-35.035s] | in front of [9.975-34.9125s] | ✓ TRASER has this pair | ✗ ✗ | ✗ ✗ |
| baby #1 → sofa #6 | ✓ | ✓ | in front of [12.304-14.1391s]; towards [12.304-14.1391s] | in front of [11.97-14.9625s] | ✓ TRASER has this pair | ✓ ✗ | ✓ ✗ |
| baby #1 → adult #7 | ✓ | ✗ (adult #7 named wrong) | away [32.032-35.035s] | in front of [31.92-34.9125s] | ✓ TRASER has this pair | ✗ | ✗ |
| baby #1 → adult #9 | ✓ | ✗ (adult #9 named wrong) | watch [31.8235-35.9109s]; in front of [10.5522-13.8055s]; in front of [32.032-35.9109s]; away [12.012-13.8055s]; towards [32.032-35.035s] | - | ✗ TRASER missed this pair | - - - - - | - - - - - |
| adult #2 → baby #0 | ✓ | ✓ | watch [0-6.33967s]; behind [0-19.019s]; towards [10.01-13.013s]; away [12.012-15.015s] | - | ↔ TRASER has it reversed | - - - - | - - - - |
| adult #2 → baby #1 | ✓ | ✓ | lift [12.8045-13.9723s]; lift [18.9773-20.1034s]; lift [24.8582-25.4004s]; lift [29.6963-30.8225s]; watch [14.723-27.4024s]; watch [29.029-32.9079s]; towards [10.5522-12.9713s]; behind [12.012-33.742s] | - | ↔ TRASER has it reversed | - - - - - - - - | - - - - - - - - |
| adult #2 → sofa #6 | ✓ | ✓ | in front of [12.304-14.1391s]; away [12.304-14.1391s] | - | ✗ TRASER missed this pair | - - | - - |
| adult #2 → adult #9 | ✓ | ✗ (adult #9 named wrong) | in front of [0-5.88087s]; in front of [10.2602-13.8055s]; in front of [32.032-33.742s]; towards [12.012-13.8055s] | - | ✗ TRASER missed this pair | - - - - | - - - - |
| child #3 → chair #4 | ✓ | ✓ | lean on [28.1531-35.9109s]; above [28.1531-35.8692s] | on [31.92-34.9125s] | ✓ TRASER has this pair | ✗ ✗ | ✗ ✗ |
| child #3 → table #5 | ✓ | ✓ | next to [28.1114-35.8692s] | - | ✗ TRASER missed this pair | - | - |
| child #3 → adult #7 | ✓ | ✗ (adult #7 named wrong) | watch [32.9913-33.325s]; watch [35.6189-35.9109s]; next to [31.1978-35.8692s] | - | ✗ TRASER missed this pair | - - - | - - - |
| child #3 → sofa #8 | ✓ | ✓ | next to [34.034-35.9109s] | in front of [32.9175-34.9125s] | ✓ TRASER has this pair | ✗ | ✗ |
| child #3 → adult #9 | ✓ | ✗ (adult #9 named wrong) | in front of [32.032-35.9109s] | - | ✗ TRASER missed this pair | - | - |
| chair #4 → child #3 | ✓ | ✓ | beneath [28.1531-35.8692s] | - | ↔ TRASER has it reversed | - | - |
| chair #4 → adult #7 | ✓ | ✗ (adult #7 named wrong) | next to [31.1978-35.8692s] | - | ✗ TRASER missed this pair | - | - |
| chair #4 → sofa #8 | ✓ | ✓ | next to [34.034-35.9109s] | in front of [32.9175-34.9125s] | ✓ TRASER has this pair | ✗ | ✗ |
| chair #4 → adult #9 | ✓ | ✗ (adult #9 named wrong) | in front of [32.032-35.9109s] | - | ✗ TRASER missed this pair | - | - |
| table #5 → baby #1 | ✓ | ✓ | behind [10.5522-12.2205s] | - | ↔ TRASER has it reversed | - | - |
| table #5 → child #3 | ✓ | ✓ | in front of [30.03-35.9109s] | - | ✗ TRASER missed this pair | - | - |
| table #5 → chair #4 | ✓ | ✓ | in front of [28.1531-35.8692s] | - | ✗ TRASER missed this pair | - | - |
| table #5 → adult #7 | ✓ | ✗ (adult #7 named wrong) | in front of [31.1978-35.8692s] | - | ✗ TRASER missed this pair | - | - |
| table #5 → sofa #8 | ✓ | ✓ | in front of [34.034-35.9109s] | in front of [32.9175-34.9125s] | ✓ TRASER has this pair | ✗ | ✗ |
| table #5 → adult #9 | ✓ | ✗ (adult #9 named wrong) | in front of [10.2602-12.2205s]; in front of [32.032-35.9109s] | - | ✗ TRASER missed this pair | - - | - - |
| sofa #6 → baby #0 | ✓ | ✓ | behind [12.304-14.1391s] | - | ↔ TRASER has it reversed | - | - |
| sofa #6 → baby #1 | ✓ | ✓ | behind [12.304-14.1391s] | - | ↔ TRASER has it reversed | - | - |
| sofa #6 → adult #2 | ✓ | ✓ | behind [12.304-14.1391s] | - | ✗ TRASER missed this pair | - | - |
| adult #7 → child #3 | ✓ | ✗ (adult #7 named wrong) | next to [31.1978-35.8692s] | - | ✗ TRASER missed this pair | - | - |
| adult #7 → chair #4 | ✓ | ✗ (adult #7 named wrong) | next to [31.1978-35.8692s] | - | ✗ TRASER missed this pair | - | - |
| adult #7 → sofa #8 | ✓ | ✗ (adult #7 named wrong) | lean on [33.7837-35.9109s]; above [34.034-35.9109s] | in front of [32.9175-34.9125s] | ✓ TRASER has this pair | ✗ ✗ | ✗ ✗ |
| sofa #8 → child #3 | ✓ | ✓ | next to [34.034-35.9109s] | - | ↔ TRASER has it reversed | - | - |
| sofa #8 → chair #4 | ✓ | ✓ | next to [34.034-35.9109s] | - | ↔ TRASER has it reversed | - | - |
| sofa #8 → adult #7 | ✓ | ✗ (adult #7 named wrong) | beneath [34.034-35.9109s] | - | ↔ TRASER has it reversed | - | - |
| adult #9 → baby #0 | ✓ | ✗ (adult #9 named wrong) | in front of [0-5.88087s]; in front of [10.2602-13.8055s] | - | ✗ TRASER missed this pair | - - | - - |
| adult #9 → baby #1 | ✓ | ✗ (adult #9 named wrong) | watch [35.2852-35.9109s]; hold hand of [10.5522-12.7627s]; next to [10.5522-13.8055s]; in front of [32.032-35.9109s] | - | ✗ TRASER missed this pair | - - - - | - - - - |
| adult #9 → adult #2 | ✓ | ✗ (adult #9 named wrong) | in front of [0-5.88087s]; in front of [10.2602-13.8055s]; in front of [32.032-33.742s] | - | ✗ TRASER missed this pair | - - - | - - - |
| adult #9 → child #3 | ✓ | ✗ (adult #9 named wrong) | behind [32.032-35.9109s] | - | ✗ TRASER missed this pair | - | - |
| adult #9 → chair #4 | ✓ | ✗ (adult #9 named wrong) | behind [32.032-35.9109s] | - | ✗ TRASER missed this pair | - | - |
| baby #0 → table #5 | ✓ | ✓ | - | in front of [0-27.93s] | + only TRASER | - | - |
| baby #0 → sofa #8 | ✓ | ✓ | - | in front of [32.9175-34.9125s] | + only TRASER | - | - |
| baby #1 → sofa #8 | ✓ | ✓ | - | in front of [32.9175-34.9125s] | + only TRASER | - | - |
| table #5 → sofa #6 | ✓ | ✓ | - | in front of [11.97-14.9625s] | + only TRASER | - | - |


## 4925211209

32.0 s video; humans: 2 objects, 3 relations on 2 pairs; TRASER: 3 relations on 1 pairs.

**Masks given to TRASER:** 2 of 2 objects

**Pairs:** 1 in both, 0 missed by TRASER, 1 reversed, 0 with an object TRASER was not given, 0 only TRASER

**Objects: 1/2 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | bus/truck | yes (object 1) | crane | mismatch | ✗ |
| 1 | adult | yes (object 2) | person | hypernym/hyponym | ✓ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| bus/truck #0 → adult #1 | ✓ | ✗ (bus/truck #0 named wrong) | inside [14-17s] | - | ↔ TRASER has it reversed | - | - |
| adult #1 → bus/truck #0 | ✓ | ✗ (bus/truck #0 named wrong) | lean on [0-3.875s]; inside [0-17.75s] | holding [0-14s]; moving up relative to [0-14s]; on [0-14s] | ✓ TRASER has this pair | ✗ ✗ | ✗ ✗ |


## 5421648216

43.04 s video; humans: 3 objects, 32 relations on 6 pairs; TRASER: 9 relations on 3 pairs.

**Masks given to TRASER:** 3 of 3 objects

**Pairs:** 3 in both, 0 missed by TRASER, 3 reversed, 0 with an object TRASER was not given, 0 only TRASER

**Objects: 3/3 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | sheep/goat | yes (object 1) | sheep | identical | ✓ |
| 1 | sheep/goat | yes (object 2) | sheep | identical | ✓ |
| 2 | sheep/goat | yes (object 3) | sheep | identical | ✓ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| sheep/goat #0 → sheep/goat #1 | ✓ | ✓ | behind [0-3.003s]; behind [8.008-10.2436s]; behind [20.02-25.025s]; behind [28.028-33.033s]; towards [0-3.003s]; in front of [2.002-9.009s]; next to [24.024-29.029s]; next to [32.032-43.043s] | approaches [0-7.00651s]; passes [7.00651-9.00837s]; moves away from [9.00837-12.0112s]; follows [24.0223-36.0335s]; near [0-12.0112s, 20.0186-42.0391s]; overlapping [0-12.0112s, 20.0186-42.0391s]; in front of [24.0223-36.0335s] | ✓ TRASER has this pair | ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ | ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ |
| sheep/goat #0 → sheep/goat #2 | ✓ | ✓ | watch [23.4234-23.9239s]; towards [0-3.003s]; in front of [4.004-5.63897s]; in front of [20.02-23.9239s]; in front of [38.038-43.043s] | near [0-6.00558s, 12.0112-13.0121s, 16.0149-17.0158s, 18.0167-22.0205s, 36.0335-42.0391s] | ✓ TRASER has this pair | ✗ ✗ ✗ ✗ ✗ | ✗ ✗ ✗ ✗ ✗ |
| sheep/goat #1 → sheep/goat #0 | ✓ | ✓ | in front of [0-3.003s]; in front of [24.024-37.037s]; next to [2.002-10.2436s]; next to [20.02-25.025s]; next to [36.036-43.043s] | - | ↔ TRASER has it reversed | - - - - - | - - - - - |
| sheep/goat #1 → sheep/goat #2 | ✓ | ✓ | watch [4.23757-5.47213s]; watch [34.8682-39.8064s]; in front of [4.004-5.63897s]; in front of [20.02-23.9239s]; in front of [40.04-43.043s] | near [0-6.00558s, 12.0112-13.0121s, 16.0149-17.0158s, 18.0167-22.0205s, 36.0335-42.0391s] | ✓ TRASER has this pair | ✗ ✗ ✗ ✗ ✗ | ✗ ✗ ✗ ✗ ✗ |
| sheep/goat #2 → sheep/goat #0 | ✓ | ✓ | watch [3.8038-5.63897s]; watch [21.4881-23.9239s]; watch [38.8388-41.5081s]; in front of [0-5.63897s]; in front of [19.3527-23.9239s]; in front of [34.8682-43.0096s] | - | ↔ TRASER has it reversed | - - - - - - | - - - - - - |
| sheep/goat #2 → sheep/goat #1 | ✓ | ✓ | in front of [0-5.63897s]; in front of [34.8682-43.0096s]; behind [20.02-23.9239s] | - | ↔ TRASER has it reversed | - - - | - - - |


## 5658916668

22.02 s video; humans: 9 objects, 35 relations on 21 pairs; TRASER: 18 relations on 15 pairs.

**Masks given to TRASER:** 9 of 9 objects

**Pairs:** 6 in both, 12 missed by TRASER, 3 reversed, 0 with an object TRASER was not given, 9 only TRASER

**Objects: 8/9 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | adult | yes (object 1) | person | hypernym/hyponym | ✓ |
| 1 | adult | yes (object 2) | skateboard | mismatch | ✗ |
| 2 | adult | yes (object 3) | person | hypernym/hyponym | ✓ |
| 3 | adult | yes (object 4) | person | hypernym/hyponym | ✓ |
| 4 | snowboard | yes (object 5) | skateboard | semantic overlap | ✓ |
| 5 | adult | yes (object 6) | person | hypernym/hyponym | ✓ |
| 6 | adult | yes (object 7) | person | hypernym/hyponym | ✓ |
| 7 | snowboard | yes (object 8) | skateboard | semantic overlap | ✓ |
| 8 | adult | yes (object 9) | person | hypernym/hyponym | ✓ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| adult #0 → adult #1 | ✓ | ✗ (adult #1 named wrong) | next to [0.6006-8.04137s]; away [0.6006-4.97163s] | - | ✗ TRASER missed this pair | - - | - - |
| adult #0 → adult #2 | ✓ | ✓ | next to [0-8.04137s]; towards [0-3.003s] | - | ✗ TRASER missed this pair | - - | - - |
| adult #0 → adult #3 | ✓ | ✓ | next to [0-8.04137s] | - | ✗ TRASER missed this pair | - | - |
| adult #1 → adult #0 | ✓ | ✗ (adult #1 named wrong) | next to [0.6006-8.04137s] | - | ✗ TRASER missed this pair | - | - |
| adult #1 → adult #2 | ✓ | ✗ (adult #1 named wrong) | next to [0.6006-8.97563s] | - | ✗ TRASER missed this pair | - | - |
| adult #2 → adult #0 | ✓ | ✓ | next to [0-8.04137s]; towards [0-5.005s] | - | ✗ TRASER missed this pair | - - | - - |
| adult #2 → adult #1 | ✓ | ✗ (adult #1 named wrong) | next to [0.6006-8.97563s] | - | ✗ TRASER missed this pair | - | - |
| adult #2 → adult #3 | ✓ | ✓ | next to [0-8.97563s] | - | ✗ TRASER missed this pair | - | - |
| adult #2 → adult #6 | ✓ | ✓ | away [4.004-9.54287s] | - | ↔ TRASER has it reversed | - | - |
| adult #3 → adult #0 | ✓ | ✓ | next to [0-8.04137s]; towards [0-5.005s] | - | ✗ TRASER missed this pair | - - | - - |
| adult #3 → adult #2 | ✓ | ✓ | next to [0-8.97563s] | - | ✗ TRASER missed this pair | - | - |
| snowboard #4 → adult #5 | ✓ | ✓ | next to [8.47513-10.3437s] | - | ✗ TRASER missed this pair | - | - |
| adult #5 → snowboard #4 | ✓ | ✓ | next to [8.47513-10.3437s] | - | ✗ TRASER missed this pair | - | - |
| adult #5 → adult #6 | ✓ | ✓ | next to [8.3083-9.87653s]; towards [8.3083-9.87653s] | - | ↔ TRASER has it reversed | - - | - - |
| adult #6 → adult #0 | ✓ | ✓ | towards [0-5.005s]; away [4.004-8.04137s] | in front of [0-2.00182s, 3.00273-11.01s] | ✓ TRASER has this pair | ✗ ✗ | ✗ ✗ |
| adult #6 → adult #1 | ✓ | ✗ (adult #1 named wrong) | away [4.004-9.009s] | in front of [0-2.00182s, 3.00273-11.01s] | ✓ TRASER has this pair | ✗ | ✗ |
| adult #6 → adult #2 | ✓ | ✓ | away [4.004-9.54287s] | in front of [0-2.00182s, 3.00273-11.01s] | ✓ TRASER has this pair | ✗ | ✗ |
| adult #6 → adult #3 | ✓ | ✓ | next to [0-8.97563s]; away [4.004-8.97563s] | in front of [0-2.00182s, 3.00273-11.01s] | ✓ TRASER has this pair | ✗ ✗ | ✗ ✗ |
| adult #6 → adult #5 | ✓ | ✓ | next to [8.3083-9.87653s]; away [8.3083-9.87653s] | in front of [0-2.00182s, 3.00273-11.01s] | ✓ TRASER has this pair | ✗ ✗ | ✗ ✗ |
| adult #6 → snowboard #7 | ✓ | ✓ | ride [9.04237-9.87653s]; ride [12.7127-13.3133s]; above [12.7127-14.9816s]; away [12.7127-14.9816s]; next to [14.014-21.4214s] | rides [0-2.00182s, 3.00273-11.01s, 12.0109-22.02s]; moves with [0-2.00182s, 3.00273-11.01s, 12.0109-22.02s]; performs trick with [12.0109-22.02s]; on [0-2.00182s, 3.00273-11.01s, 12.0109-22.02s] | ✓ TRASER has this pair | ✗ ✗ ✗ ✗ ✗ | ✗ ✗ ✗ ✗ ✗ |
| snowboard #7 → adult #6 | ✓ | ✓ | beneath [12.7127-14.9816s]; away [12.7127-14.9816s]; next to [14.014-21.4214s] | - | ↔ TRASER has it reversed | - - - | - - - |
| adult #6 → snowboard #4 | ✓ | ✓ | - | in front of [0-2.00182s, 3.00273-11.01s] | + only TRASER | - | - |
| snowboard #7 → adult #0 | ✓ | ✓ | - | in front of [0-2.00182s, 3.00273-11.01s] | + only TRASER | - | - |
| snowboard #7 → adult #1 | ✓ | ✗ (adult #1 named wrong) | - | in front of [0-2.00182s, 3.00273-11.01s] | + only TRASER | - | - |
| snowboard #7 → adult #2 | ✓ | ✓ | - | in front of [0-2.00182s, 3.00273-11.01s] | + only TRASER | - | - |
| snowboard #7 → adult #3 | ✓ | ✓ | - | in front of [0-2.00182s, 3.00273-11.01s] | + only TRASER | - | - |
| snowboard #7 → snowboard #4 | ✓ | ✓ | - | in front of [0-2.00182s, 3.00273-11.01s] | + only TRASER | - | - |
| snowboard #7 → adult #5 | ✓ | ✓ | - | in front of [0-2.00182s, 3.00273-11.01s] | + only TRASER | - | - |
| adult #8 → adult #6 | ✓ | ✓ | - | in front of [10.0091-11.01s] | + only TRASER | - | - |
| adult #8 → snowboard #7 | ✓ | ✓ | - | in front of [10.0091-11.01s] | + only TRASER | - | - |


## 8563398032

81.6 s video; humans: 6 objects, 36 relations on 25 pairs; TRASER: 15 relations on 12 pairs.

**Masks given to TRASER:** 6 of 6 objects

**Pairs:** 12 in both, 6 missed by TRASER, 7 reversed, 0 with an object TRASER was not given, 0 only TRASER

**Objects: 6/6 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | adult | yes (object 1) | person | hypernym/hyponym | ✓ |
| 1 | adult | yes (object 2) | person | hypernym/hyponym | ✓ |
| 2 | cup | yes (object 3) | cup | identical | ✓ |
| 3 | table | yes (object 4) | tablecloth | semantic overlap | ✓ |
| 4 | chair | yes (object 5) | chair | identical | ✓ |
| 5 | adult | yes (object 6) | person | hypernym/hyponym | ✓ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| adult #0 → adult #1 | ✓ | ✓ | speak to [54.44-60.24s]; watch [55.36-63.72s]; next to [0-59s]; next to [60-81.6s]; in front of [58-61s] | looking at [0-81.6s]; talking with [0-81.6s]; next to [0-81.6s] | ✓ TRASER has this pair | ✗ ✗ ✓ ✗ ✗ | ✗ ✗ ✓ ✗ ✗ |
| adult #0 → cup #2 | ✓ | ✓ | next to [0-81.6s] | - | ↔ TRASER has it reversed | - | - |
| adult #0 → table #3 | ✓ | ✓ | next to [0-81.6s] | behind [0-81.6s] | ✓ TRASER has this pair | ✗ | ✗ |
| adult #0 → chair #4 | ✓ | ✓ | in front of [0-81.6s] | sitting on [0-81.6s] | ✓ TRASER has this pair | ✗ | ✗ |
| adult #0 → adult #5 | ✓ | ✓ | in front of [1.36-81.56s] | - | ✗ TRASER missed this pair | - | - |
| adult #1 → adult #0 | ✓ | ✓ | watch [55.68-56.04s]; watch [57.76-58.12s]; next to [0-81.6s] | looking at [0-81.6s] | ✓ TRASER has this pair | ✗ ✗ ✗ | ✗ ✗ ✗ |
| adult #1 → table #3 | ✓ | ✓ | lean on [0-1.92s]; lean on [3.12-32.12s]; lean on [39.88-54.36s]; lean on [62.92-63.72s]; lean on [65.4-81.6s]; next to [0-81.6s] | behind [0-81.6s] | ✓ TRASER has this pair | ✗ ✗ ✗ ✗ ✗ ✗ | ✗ ✗ ✗ ✗ ✗ ✗ |
| adult #1 → chair #4 | ✓ | ✓ | in front of [0-81.6s] | sitting on [0-81.6s] | ✓ TRASER has this pair | ✗ | ✗ |
| adult #1 → adult #5 | ✓ | ✓ | in front of [1.36-81.56s] | - | ✗ TRASER missed this pair | - | - |
| cup #2 → adult #0 | ✓ | ✓ | in front of [0-81.6s] | in front of [0-81.6s] | ✓ TRASER has this pair | ✓ | ✓ |
| cup #2 → adult #1 | ✓ | ✓ | in front of [58-61s] | in front of [0-81.6s] | ✓ TRASER has this pair | ✗ | ✗ |
| cup #2 → table #3 | ✓ | ✓ | above [0-81.6s] | on [0-81.6s] | ✓ TRASER has this pair | ✓ | ✓ |
| cup #2 → chair #4 | ✓ | ✓ | in front of [0-81.6s] | - | ✗ TRASER missed this pair | - | - |
| cup #2 → adult #5 | ✓ | ✓ | in front of [1.36-81.56s] | - | ✗ TRASER missed this pair | - | - |
| table #3 → adult #0 | ✓ | ✓ | in front of [0-81.6s] | - | ↔ TRASER has it reversed | - | - |
| table #3 → adult #1 | ✓ | ✓ | in front of [0-81.6s] | - | ↔ TRASER has it reversed | - | - |
| table #3 → cup #2 | ✓ | ✓ | beneath [0-81.6s] | - | ↔ TRASER has it reversed | - | - |
| table #3 → chair #4 | ✓ | ✓ | in front of [0-81.6s] | - | ↔ TRASER has it reversed | - | - |
| table #3 → adult #5 | ✓ | ✓ | in front of [1.36-81.56s] | - | ↔ TRASER has it reversed | - | - |
| chair #4 → table #3 | ✓ | ✓ | next to [0-81.6s] | behind [0-81.6s] | ✓ TRASER has this pair | ✗ | ✗ |
| chair #4 → adult #5 | ✓ | ✓ | next to [1.36-81.56s] | - | ↔ TRASER has it reversed | - | - |
| adult #5 → adult #0 | ✓ | ✓ | in front of [1.36-81.56s] | - | ✗ TRASER missed this pair | - | - |
| adult #5 → adult #1 | ✓ | ✓ | in front of [1.36-81.56s] | - | ✗ TRASER missed this pair | - | - |
| adult #5 → table #3 | ✓ | ✓ | next to [1.36-81.56s] | behind [0-81.6s] | ✓ TRASER has this pair | ✗ | ✗ |
| adult #5 → chair #4 | ✓ | ✓ | next to [1.36-26.96s] | sitting on [0-81.6s]; on [0-81.6s] | ✓ TRASER has this pair | ✗ | ✗ |


## 9217939684

69.17 s video; humans: 6 objects, 112 relations on 22 pairs; TRASER: 20 relations on 13 pairs.

**Masks given to TRASER:** 6 of 6 objects

**Pairs:** 12 in both, 0 missed by TRASER, 10 reversed, 0 with an object TRASER was not given, 1 only TRASER

**Objects: 5/6 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | baby | yes (object 1) | child | hypernym/hyponym | ✓ |
| 1 | adult | yes (object 2) | person | hypernym/hyponym | ✓ |
| 2 | adult | yes (object 3) | person | hypernym/hyponym | ✓ |
| 3 | child | yes (object 4) | child | identical | ✓ |
| 4 | toy | yes (object 5) | toy | identical | ✓ |
| 5 | toy | yes (object 6) | pillow | mismatch | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| baby #0 → adult #1 | ✓ | ✓ | watch [14.0833-14.6667s]; watch [38.875-40.0417s]; in front of [14.0833-27.625s]; in front of [38.625-44.9583s]; in front of [62.7917-68.9583s]; towards [38.625-40.9583s] | approaches [12.0296-18.0443s]; moves away from [18.0443-29.0714s]; in front of [12.0296-29.0714s, 38.0936-47.1158s, 62.1528-69.17s] | ✓ TRASER has this pair | ✗ ✗ ✗ ✗ ✗ ✗ | ✗ ✗ ✗ ✗ ✗ ✗ |
| baby #0 → adult #2 | ✓ | ✓ | watch [0-1.16667s]; hug [0.916667-1.875s]; in front of [0-12s]; in front of [30.2917-36.4167s]; in front of [58-61s]; next to [53.3333-58.9583s] | approaches [0-10.0246s]; moves away from [10.0246-12.0296s]; in front of [0-12.0296s, 31.0764-37.0912s, 53.1306-62.1528s] | ✓ TRASER has this pair | ✗ ✗ ✗ ✗ ✗ ✗ | ✗ ✗ ✗ ✗ ✗ ✗ |
| baby #0 → child #3 | ✓ | ✓ | watch [61.1667-62.9167s]; in front of [12.375-29.9583s]; in front of [36.6667-52.9583s]; in front of [61.1667-68.9583s]; away [50-52.9583s]; towards [61.1667-62.9583s] | approaches [12.0296-18.0443s]; moves away from [18.0443-29.0714s]; in front of [12.0296-29.0714s, 38.0936-47.1158s, 48.1183-54.133s, 62.1528-69.17s] | ✓ TRASER has this pair | ✗ ✗ ✗ ✗ ✗ ✗ | ✗ ✗ ✗ ✗ ✗ ✗ |
| baby #0 → toy #4 | ✓ | ✓ | next to [0-8.45833s]; next to [30-37.7917s]; next to [46.375-50.5417s]; next to [52.8333-61.875s] | approaches [31.0764-37.0912s]; moves away from [37.0912-41.101s] | ✓ TRASER has this pair | ✗ ✗ ✗ ✗ | ✗ ✗ ✗ ✗ |
| baby #0 → toy #5 | ✓ | ✗ (toy #5 named wrong) | next to [12.125-30.4167s]; next to [36-53s]; next to [61.0417-68.9583s]; away [48-51s]; towards [61.0417-62.9583s] | in front of [12.0296-29.0714s, 38.0936-47.1158s, 48.1183-54.133s, 62.1528-69.17s] | ✓ TRASER has this pair | ✗ ✗ ✗ ✗ ✗ | ✗ ✗ ✗ ✗ ✗ |
| adult #1 → baby #0 | ✓ | ✓ | watch [14.0833-16.9583s]; watch [20.3333-27.625s]; watch [38.875-45.0833s]; watch [62.7917-66.6667s]; watch [67.3333-69.1667s]; hold [16.9167-20.0833s]; hold [22.25-24.1667s]; in front of [14.0833-16.9583s]; in front of [38.625-42.9583s]; in front of [64-69s]; behind [16-27.625s]; behind [42-45s]; next to [62.7917-64.9583s] | - | ↔ TRASER has it reversed | - - - - - - - - - - - - - | - - - - - - - - - - - - - |
| adult #1 → child #3 | ✓ | ✓ | next to [14.0833-27.625s]; next to [38.625-44.9583s]; next to [62.7917-68.9583s] | - | ↔ TRASER has it reversed | - - - | - - - |
| adult #1 → toy #5 | ✓ | ✗ (toy #5 named wrong) | next to [14.0833-27.625s]; next to [38.625-44.9583s]; next to [62.7917-68.9583s] | - | ↔ TRASER has it reversed | - - - | - - - |
| adult #2 → baby #0 | ✓ | ✓ | watch [0-1.04167s]; watch [2.20833-11.4583s]; watch [31-35.8333s]; watch [55.125-58s]; hug [1.375-2.70833s]; hold [2.66667-8.75s]; lift [3.91667-4.66667s]; in front of [0-5s]; behind [4-12s]; behind [34-36.4167s]; behind [53.3333-58.9583s]; next to [30.2917-34.9583s]; next to [58-61s] | - | ↔ TRASER has it reversed | - - - - - - - - - - - - - | - - - - - - - - - - - - - |
| adult #2 → toy #4 | ✓ | ✓ | next to [0-8.45833s]; next to [30.2917-36.4167s]; next to [53.3333-60.9583s] | - | ↔ TRASER has it reversed | - - - | - - - |
| child #3 → baby #0 | ✓ | ✓ | watch [12.5417-14.7083s]; watch [18.0417-19.3333s]; watch [20.375-29.9583s]; watch [36.6667-37.4583s]; watch [39.125-48s]; watch [50-52.7083s]; watch [61.4167-68.875s]; in front of [12.375-14.9583s]; in front of [36.6667-38.9583s]; in front of [61.1667-64.9583s]; next to [14-17s]; next to [18-29.9583s]; next to [38-47s]; next to [64-69s]; behind [16-19s]; behind [46-52.9583s] | - | ↔ TRASER has it reversed | - - - - - - - - - - - - - - - - | - - - - - - - - - - - - - - - - |
| child #3 → adult #1 | ✓ | ✓ | next to [14.0833-27.625s]; next to [38.625-44.9583s]; next to [62.7917-68.9583s] | in front of [12.0296-29.0714s, 38.0936-47.1158s, 62.1528-69.17s] | ✓ TRASER has this pair | ✗ ✗ ✗ | ✗ ✗ ✗ |
| child #3 → toy #4 | ✓ | ✓ | next to [46.375-50.5417s] | - | ↔ TRASER has it reversed | - | - |
| child #3 → toy #5 | ✓ | ✗ (toy #5 named wrong) | next to [12.375-29.9583s]; next to [36.6667-52.9583s]; next to [61.1667-68.9583s] | in front of [12.0296-29.0714s, 38.0936-47.1158s, 48.1183-54.133s, 62.1528-69.17s] | ✓ TRASER has this pair | ✗ ✗ ✗ | ✗ ✗ ✗ |
| toy #4 → baby #0 | ✓ | ✓ | next to [0-8.45833s]; next to [36-37.7917s]; next to [46.375-50.5417s]; next to [60-61.875s]; behind [30-37s]; behind [52.8333-60.9583s] | - | ↔ TRASER has it reversed | - - - - - - | - - - - - - |
| toy #4 → adult #2 | ✓ | ✓ | next to [0-8.45833s]; next to [30.2917-36.4167s]; next to [53.3333-60.9583s] | in front of [0-12.0296s, 31.0764-37.0912s, 53.1306-62.1528s] | ✓ TRASER has this pair | ✗ ✗ ✗ | ✗ ✗ ✗ |
| toy #4 → child #3 | ✓ | ✓ | next to [46.375-50.5417s] | in front of [12.0296-29.0714s, 38.0936-47.1158s, 48.1183-54.133s, 62.1528-69.17s] | ✓ TRASER has this pair | ✗ | ✗ |
| toy #4 → toy #5 | ✓ | ✗ (toy #5 named wrong) | next to [36-37.7917s]; next to [46.375-50.5417s] | in front of [12.0296-29.0714s, 38.0936-47.1158s, 48.1183-54.133s, 62.1528-69.17s] | ✓ TRASER has this pair | ✗ ✗ | ✗ ✗ |
| toy #5 → baby #0 | ✓ | ✗ (toy #5 named wrong) | next to [12.125-20.9583s]; next to [22-30.4167s]; next to [36-49s]; next to [64-69s]; behind [20-23s]; behind [48-53s]; in front of [61.0417-64.9583s] | - | ↔ TRASER has it reversed | - - - - - - - | - - - - - - - |
| toy #5 → adult #1 | ✓ | ✗ (toy #5 named wrong) | next to [14.0833-27.625s]; next to [38.625-44.9583s]; next to [62.7917-68.9583s] | in front of [12.0296-29.0714s, 38.0936-47.1158s, 62.1528-69.17s] | ✓ TRASER has this pair | ✗ ✗ ✗ | ✗ ✗ ✗ |
| toy #5 → child #3 | ✓ | ✗ (toy #5 named wrong) | behind [12.375-29.9583s]; behind [36.6667-52.9583s]; behind [61.1667-68.9583s] | in front of [12.0296-29.0714s, 38.0936-47.1158s, 48.1183-54.133s, 62.1528-69.17s] | ✓ TRASER has this pair | ✗ ✗ ✗ | ✗ ✗ ✗ |
| toy #5 → toy #4 | ✓ | ✗ (toy #5 named wrong) | next to [36-37.7917s]; next to [46.375-50.5417s] | - | ↔ TRASER has it reversed | - - | - - |
| toy #4 → adult #1 | ✓ | ✓ | - | in front of [12.0296-29.0714s, 38.0936-47.1158s, 62.1528-69.17s] | + only TRASER | - | - |

