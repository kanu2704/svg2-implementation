# pvsg: which object pairs Qwen-7B talks about (10 random videos, seed 0)

The same 10 videos as TRASER's page ([`results/traser_bench/pvsg/PAIRS.md`](../../traser_bench/pvsg/PAIRS.md)), with the answers of Qwen2.5-VL-7B-Instruct (not fine-tuned) in TRASER's pipeline (`../README.md`).

Qwen-7B is given the human objects (masks) and writes its own list of relations; it is not told which pairs to describe. Each row is one ordered pair (subject → object) that the humans or Qwen-7B mention.

- **✓ Qwen-7B has this pair**: Qwen-7B wrote at least one relation for the same two objects, same direction
- **✗ Qwen-7B missed this pair**: humans annotated it, Qwen-7B said nothing about these two objects
- **↔ reversed**: Qwen-7B only has the other direction (object → subject); scored as missed
- **⊘ object not given**: one of the two objects was not among the (at most 40) objects Qwen-7B received, so it could not answer; scored as missed in the main score (README.md also shows a score that leaves these out)
- **mask given to Qwen-7B?** (objects table): yes, with the number Qwen-7B calls it ("object k"); or no, because the run gives only the first 40 objects by number, or because the object has no mask on the frames Qwen-7B reads (about 1 per second)
- **+ only Qwen-7B**: Qwen-7B describes a pair the humans did not annotate (ignored by the scores)
- **both masks given?**: ✓ if Qwen-7B got the masks of both objects of the pair in its input (the camera always counts as given), ✗ and which object was missing otherwise
- **both objects named right?**: ✓ if Qwen-7B's labels for both objects are right (lenient: not a mismatch), ✗ and which one is wrong (named wrong, or not given so never named)
- **relation right?**, one mark per human relation of the pair: ✓ same two objects, relation word right and tIoU > 0.5; ✗ not; - Qwen-7B wrote nothing for this pair; ? the judge has not compared the words yet. The object names do not matter here (paper's definition)
- **triplet right?**, one mark per human relation: ✓ only if the relation is right AND both objects are named right

**Total over these videos:** 129 human pairs, 136 Qwen-7B pairs; 3 in both, 119 missed, 2 reversed, 5 with an object not given, 133 only Qwen-7B.

| video | source | masks given to Qwen-7B | objects right | relations right | triplets right | human pairs | Qwen-7B pairs | pairs in both | missed by Qwen-7B | reversed | object not given | only Qwen-7B |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [0018_4748191834](#0018_4748191834) | vidor | 13/14 | 0/14 | 0/17 | 0/17 | 15 | 0 | 0 | 15 | 0 | 0 | 0 |
| [1000_6828150903](#1000_6828150903) | vidor | 15/15 | 0/15 | 0/13 | 0/13 | 11 | 10 | 0 | 10 | 1 | 0 | 10 |
| [1011_4633647136](#1011_4633647136) | vidor | 14/14 | 2/14 | 0/20 | 0/20 | 15 | 19 | 2 | 12 | 1 | 0 | 17 |
| [1012_4024008346](#1012_4024008346) | vidor | 11/11 | 4/11 | 0/8 | 0/8 | 8 | 9 | 0 | 8 | 0 | 0 | 9 |
| [1015_4698622422](#1015_4698622422) | vidor | 13/13 | 3/13 | 0/15 | 0/15 | 9 | 14 | 0 | 9 | 0 | 0 | 14 |
| [1021_4278168115](#1021_4278168115) | vidor | 11/11 | 5/11 | 0/21 | 0/21 | 19 | 7 | 0 | 19 | 0 | 0 | 7 |
| [1025_4615486172](#1025_4615486172) | vidor | 27/27 | 4/27 | 0/24 | 0/24 | 23 | 29 | 1 | 22 | 0 | 0 | 28 |
| [P03_06](#p03_06) | epic_kitchen | 39/65 | 2/65 | 0/20 | 0/20 | 16 | 20 | 0 | 11 | 0 | 5 | 20 |
| [P14_06](#p14_06) | epic_kitchen | 34/34 | 2/34 | 0/10 | 0/10 | 7 | 0 | 0 | 7 | 0 | 0 | 0 |
| [P28_19](#p28_19) | epic_kitchen | 27/28 | 0/28 | 0/10 | 0/10 | 6 | 28 | 0 | 6 | 0 | 0 | 28 |

## 0018_4748191834

33.2 s video; humans: 14 objects, 17 relations on 15 pairs; Qwen-7B: 0 relations on 0 pairs.

**Masks given to Qwen-7B:** 13 of 14 objects (0 after the first 40, 1 with no mask on the frames Qwen-7B reads)

**Pairs:** 0 in both, 15 missed by Qwen-7B, 0 reversed, 0 with an object Qwen-7B was not given, 0 only Qwen-7B

**Objects: 0/14 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | ground | no: no mask on the frames Qwen-7B reads | - (never shown to Qwen-7B) | - | ✗ |
| 2 | floor | yes (object 1) | cake | mismatch | ✗ |
| 3 | wall | yes (object 2) | child | mismatch | ✗ |
| 4 | cookie | yes (object 3) | woman | mismatch | ✗ |
| 5 | door | yes (object 4) | table | mismatch | ✗ |
| 6 | adult | yes (object 5) | chair | mismatch | ✗ |
| 7 | child | yes (object 6) | candle | mismatch | ✗ |
| 8 | table | yes (object 7) | hand | mismatch | ✗ |
| 9 | chair | yes (object 8) | mouth | mismatch | ✗ |
| 10 | candle | yes (object 9) | face | mismatch | ✗ |
| 11 | cake | yes (object 10) | light | mismatch | ✗ |
| 12 | camera | yes (object 11) | room | mismatch | ✗ |
| 13 | adult | yes (object 12) | floor | mismatch | ✗ |
| 14 | chair | yes (object 13) | window | mismatch | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| adult #6 → child #7 | ✓ | ✗ (adult #6 named wrong, child #7 named wrong) | touching [9-22.6s]; hugging [7.6-22.6s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| adult #6 → table #8 | ✓ | ✗ (adult #6 named wrong, table #8 named wrong) | beside [9-33.4s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #6 → candle #10 | ✓ | ✗ (adult #6 named wrong, candle #10 named wrong) | touching [25.8-27s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #7 → adult #6 | ✓ | ✗ (child #7 named wrong, adult #6 named wrong) | looking at [6.8-8.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #7 → chair #9 | ✓ | ✗ (child #7 named wrong, chair #9 named wrong) | sitting on [0-33.4s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #7 → candle #10 | ✓ | ✗ (child #7 named wrong, candle #10 named wrong) | blowing [22.4-26s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #7 → cake #11 | ✓ | ✗ (child #7 named wrong, cake #11 named wrong) | in front of [0-33.4s]; looking at [8.4-32s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| candle #10 → cake #11 | ✓ | ✗ (candle #10 named wrong, cake #11 named wrong) | on [0-33.4s] | - | ✗ Qwen-7B missed this pair | - | - |
| cake #11 → table #8 | ✓ | ✗ (cake #11 named wrong, table #8 named wrong) | on [0-33.4s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #13 → floor #2 | ✓ | ✗ (adult #13 named wrong, floor #2 named wrong) | walking on [9.6-19s, 31.4-33.2s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #13 → wall #3 | ✓ | ✗ (adult #13 named wrong, wall #3 named wrong) | in front of [0-9.2s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #13 → table #8 | ✓ | ✗ (adult #13 named wrong, table #8 named wrong) | beside [11-32s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #13 → candle #10 | ✓ | ✗ (adult #13 named wrong, candle #10 named wrong) | touching [20-21s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #13 → cake #11 | ✓ | ✗ (adult #13 named wrong, cake #11 named wrong) | touching [21-22.4s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #13 → camera #12 | ✓ | ✗ (adult #13 named wrong, camera #12 named wrong) | holding [0-32.2s] | - | ✗ Qwen-7B missed this pair | - | - |


## 1000_6828150903

68.0 s video; humans: 15 objects, 13 relations on 11 pairs; Qwen-7B: 10 relations on 10 pairs.

**Masks given to Qwen-7B:** 15 of 15 objects

**Pairs:** 0 in both, 10 missed by Qwen-7B, 1 reversed, 0 with an object Qwen-7B was not given, 10 only Qwen-7B

**Objects: 0/15 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | rock | yes (object 1) | flower | mismatch | ✗ |
| 2 | floor | yes (object 2) | woman | mismatch | ✗ |
| 3 | ceiling | yes (object 3) | child | mismatch | ✗ |
| 4 | wall | yes (object 4) | door | mismatch | ✗ |
| 5 | door | yes (object 5) | room | mismatch | ✗ |
| 6 | shelf | yes (object 6) | window | mismatch | ✗ |
| 7 | window | yes (object 7) | table | mismatch | ✗ |
| 8 | adult | yes (object 8) | chair | mismatch | ✗ |
| 9 | baby | yes (object 9) | toy | mismatch | ✗ |
| 10 | dog | yes (object 10) | statue | mismatch | ✗ |
| 11 | toy | yes (object 11) | mantle | mismatch | ✗ |
| 12 | door | yes (object 12) | statue | mismatch | ✗ |
| 13 | door | yes (object 13) | statue | mismatch | ✗ |
| 14 | door | yes (object 14) | statue | mismatch | ✗ |
| 15 | door | yes (object 15) | statue | mismatch | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| adult #8 → rock #1 | ✓ | ✗ (adult #8 named wrong, rock #1 named wrong) | in front of [16.4-68s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #8 → floor #2 | ✓ | ✗ (adult #8 named wrong, floor #2 named wrong) | walking on [0-16.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #8 → wall #4 | ✓ | ✗ (adult #8 named wrong, wall #4 named wrong) | beside [16.4-68s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #8 → door #5 | ✓ | ✗ (adult #8 named wrong, door #5 named wrong) | beside [0-5.2s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #8 → window #7 | ✓ | ✗ (adult #8 named wrong, window #7 named wrong) | beside [11.6-13.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #8 → baby #9 | ✓ | ✗ (adult #8 named wrong, baby #9 named wrong) | holding [0-68s]; hugging [0-68s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| adult #8 → toy #11 | ✓ | ✗ (adult #8 named wrong, toy #11 named wrong) | grabbing [16.8-18s]; holding [18-45.6s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| adult #8 → door #12 | ✓ | ✗ (adult #8 named wrong, door #12 named wrong) | beside [5.2-9.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #8 → door #14 | ✓ | ✗ (adult #8 named wrong, door #14 named wrong) | beside [10.2-11.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| baby #9 → toy #11 | ✓ | ✗ (baby #9 named wrong, toy #11 named wrong) | holding [45.6-68s] | - | ✗ Qwen-7B missed this pair | - | - |
| dog #10 → floor #2 | ✓ | ✗ (dog #10 named wrong, floor #2 named wrong) | jumping over [19-21.4s] | - | ↔ Qwen-7B has it reversed | - | - |
| rock #1 → floor #2 | ✓ | ✗ (rock #1 named wrong, floor #2 named wrong) | - | held by [-] | + only Qwen-7B | - | - |
| floor #2 → ceiling #3 | ✓ | ✗ (floor #2 named wrong, ceiling #3 named wrong) | - | carrying [-] | + only Qwen-7B | - | - |
| floor #2 → door #5 | ✓ | ✗ (floor #2 named wrong, door #5 named wrong) | - | standing in [-] | + only Qwen-7B | - | - |
| floor #2 → dog #10 | ✓ | ✗ (floor #2 named wrong, dog #10 named wrong) | - | holding [-] | + only Qwen-7B | - | - |
| floor #2 → toy #11 | ✓ | ✗ (floor #2 named wrong, toy #11 named wrong) | - | holding [-] | + only Qwen-7B | - | - |
| floor #2 → door #12 | ✓ | ✗ (floor #2 named wrong, door #12 named wrong) | - | holding [-] | + only Qwen-7B | - | - |
| floor #2 → door #13 | ✓ | ✗ (floor #2 named wrong, door #13 named wrong) | - | holding [-] | + only Qwen-7B | - | - |
| floor #2 → door #14 | ✓ | ✗ (floor #2 named wrong, door #14 named wrong) | - | holding [-] | + only Qwen-7B | - | - |
| floor #2 → door #15 | ✓ | ✗ (floor #2 named wrong, door #15 named wrong) | - | holding [-] | + only Qwen-7B | - | - |
| ceiling #3 → rock #1 | ✓ | ✗ (ceiling #3 named wrong, rock #1 named wrong) | - | playing with [-] | + only Qwen-7B | - | - |


## 1011_4633647136

53.6 s video; humans: 14 objects, 20 relations on 15 pairs; Qwen-7B: 19 relations on 19 pairs.

**Masks given to Qwen-7B:** 14 of 14 objects

**Pairs:** 2 in both, 12 missed by Qwen-7B, 1 reversed, 0 with an object Qwen-7B was not given, 17 only Qwen-7B

**Objects: 2/14 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | ground | yes (object 1) | table | mismatch | ✗ |
| 2 | wall | yes (object 2) | cake | mismatch | ✗ |
| 3 | door | yes (object 3) | woman | mismatch | ✗ |
| 4 | adult | yes (object 4) | child | hypernym/hyponym | ✓ |
| 5 | child | yes (object 5) | man | semantic overlap | ✓ |
| 6 | table | yes (object 6) | chair | mismatch | ✗ |
| 7 | chair | yes (object 7) | glass | mismatch | ✗ |
| 8 | candle | yes (object 8) | plate | mismatch | ✗ |
| 9 | cake | yes (object 9) | napkin | mismatch | ✗ |
| 10 | adult | yes (object 10) | fork | mismatch | ✗ |
| 11 | chair | yes (object 11) | spoon | mismatch | ✗ |
| 12 | adult | yes (object 12) | bottle | mismatch | ✗ |
| 13 | chair | yes (object 13) | door | mismatch | ✗ |
| 14 | chair | yes (object 14) | painting | mismatch | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| adult #4 → child #5 | ✓ | ✓ | holding [30.6-53.6s]; picking [27.8-30.2s]; guiding [42.4-44.4s] | - | ✗ Qwen-7B missed this pair | - - - | - - - |
| adult #4 → table #6 | ✓ | ✗ (table #6 named wrong) | beside [0-53.6s] | sitting on [-] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| adult #4 → candle #8 | ✓ | ✗ (candle #8 named wrong) | holding [40.2-48.4s]; blowing [42.4-43.4s]; carrying [40.2-42.4s] | - | ✗ Qwen-7B missed this pair | - - - | - - - |
| child #5 → table #6 | ✓ | ✗ (table #6 named wrong) | beside [0-53.6s] | standing behind [-] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| child #5 → chair #7 | ✓ | ✗ (chair #7 named wrong) | sitting on [0-28.8s]; standing on [30-53.6s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| candle #8 → cake #9 | ✓ | ✗ (candle #8 named wrong, cake #9 named wrong) | on [0-40.6s, 47.4-53.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| cake #9 → table #6 | ✓ | ✗ (cake #9 named wrong, table #6 named wrong) | on [0-53.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #10 → ground #1 | ✓ | ✗ (adult #10 named wrong, ground #1 named wrong) | walking on [8.6-9.8s, 45-49.4s] | - | ↔ Qwen-7B has it reversed | - | - |
| adult #10 → adult #4 | ✓ | ✗ (adult #10 named wrong) | beside [8.4-45.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #10 → table #6 | ✓ | ✗ (adult #10 named wrong, table #6 named wrong) | beside [6.2-49.2s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #10 → cake #9 | ✓ | ✗ (adult #10 named wrong, cake #9 named wrong) | touching [30.6-33.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #10 → chair #11 | ✓ | ✗ (adult #10 named wrong, chair #11 named wrong) | holding [7.6-29.4s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #12 → table #6 | ✓ | ✗ (adult #12 named wrong, table #6 named wrong) | beside [0-53.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #12 → candle #8 | ✓ | ✗ (adult #12 named wrong, candle #8 named wrong) | lighting [0-4s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #12 → cake #9 | ✓ | ✗ (adult #12 named wrong, cake #9 named wrong) | touching [30-33.4s] | - | ✗ Qwen-7B missed this pair | - | - |
| ground #1 → wall #2 | ✓ | ✗ (ground #1 named wrong, wall #2 named wrong) | - | with [-] | + only Qwen-7B | - | - |
| ground #1 → door #3 | ✓ | ✗ (ground #1 named wrong, door #3 named wrong) | - | with [-] | + only Qwen-7B | - | - |
| ground #1 → adult #4 | ✓ | ✗ (ground #1 named wrong) | - | with [-] | + only Qwen-7B | - | - |
| ground #1 → child #5 | ✓ | ✗ (ground #1 named wrong) | - | with [-] | + only Qwen-7B | - | - |
| ground #1 → table #6 | ✓ | ✗ (ground #1 named wrong, table #6 named wrong) | - | with [-] | + only Qwen-7B | - | - |
| ground #1 → chair #7 | ✓ | ✗ (ground #1 named wrong, chair #7 named wrong) | - | with [-] | + only Qwen-7B | - | - |
| ground #1 → candle #8 | ✓ | ✗ (ground #1 named wrong, candle #8 named wrong) | - | with [-] | + only Qwen-7B | - | - |
| ground #1 → cake #9 | ✓ | ✗ (ground #1 named wrong, cake #9 named wrong) | - | with [-] | + only Qwen-7B | - | - |
| ground #1 → adult #10 | ✓ | ✗ (ground #1 named wrong, adult #10 named wrong) | - | with [-] | + only Qwen-7B | - | - |
| ground #1 → chair #11 | ✓ | ✗ (ground #1 named wrong, chair #11 named wrong) | - | with [-] | + only Qwen-7B | - | - |
| ground #1 → adult #12 | ✓ | ✗ (ground #1 named wrong, adult #12 named wrong) | - | with [-] | + only Qwen-7B | - | - |
| ground #1 → chair #13 | ✓ | ✗ (ground #1 named wrong, chair #13 named wrong) | - | with [-] | + only Qwen-7B | - | - |
| ground #1 → chair #14 | ✓ | ✗ (ground #1 named wrong, chair #14 named wrong) | - | with [-] | + only Qwen-7B | - | - |
| door #3 → ground #1 | ✓ | ✗ (door #3 named wrong, ground #1 named wrong) | - | standing near [-] | + only Qwen-7B | - | - |
| door #3 → adult #4 | ✓ | ✗ (door #3 named wrong) | - | standing behind [-] | + only Qwen-7B | - | - |
| door #3 → child #5 | ✓ | ✗ (door #3 named wrong) | - | clapping hands with [-] | + only Qwen-7B | - | - |
| child #5 → ground #1 | ✓ | ✗ (ground #1 named wrong) | - | standing near [-] | + only Qwen-7B | - | - |


## 1012_4024008346

19.6 s video; humans: 11 objects, 8 relations on 8 pairs; Qwen-7B: 9 relations on 9 pairs.

**Masks given to Qwen-7B:** 11 of 11 objects

**Pairs:** 0 in both, 8 missed by Qwen-7B, 0 reversed, 0 with an object Qwen-7B was not given, 9 only Qwen-7B

**Objects: 4/11 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | floor | yes (object 1) | ball | mismatch | ✗ |
| 2 | wall | yes (object 2) | child | mismatch | ✗ |
| 3 | carpet | yes (object 3) | walker | mismatch | ✗ |
| 4 | fence | yes (object 4) | balloon | mismatch | ✗ |
| 5 | adult | yes (object 5) | adult | identical | ✓ |
| 6 | child | yes (object 6) | couch | mismatch | ✗ |
| 7 | sofa | yes (object 7) | wall | mismatch | ✗ |
| 8 | ballon | yes (object 8) | balloon | identical | ✓ |
| 9 | carpet | yes (object 9) | door | mismatch | ✗ |
| 10 | adult | yes (object 10) | woman | hypernym/hyponym | ✓ |
| 11 | ballon | yes (object 11) | balloon | identical | ✓ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| adult #5 → floor #1 | ✓ | ✗ (floor #1 named wrong) | on [0-19.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #5 → ballon #11 | ✓ | ✓ | playing with [4.4-5s, 13.4-16s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #6 → floor #1 | ✓ | ✗ (child #6 named wrong, floor #1 named wrong) | on [0-19.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #6 → ballon #8 | ✓ | ✗ (child #6 named wrong) | holding [0-19.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #6 → ballon #11 | ✓ | ✗ (child #6 named wrong) | playing with [0-0.8s, 6-13s] | - | ✗ Qwen-7B missed this pair | - | - |
| sofa #7 → floor #1 | ✓ | ✗ (sofa #7 named wrong, floor #1 named wrong) | on [0-19.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #10 → sofa #7 | ✓ | ✗ (sofa #7 named wrong) | sitting on [0-19.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| ballon #11 → floor #1 | ✓ | ✗ (floor #1 named wrong) | on [0-19.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| wall #2 → floor #1 | ✓ | ✗ (wall #2 named wrong, floor #1 named wrong) | - | plays with [0-20.58s] | + only Qwen-7B | - | - |
| wall #2 → fence #4 | ✓ | ✗ (wall #2 named wrong, fence #4 named wrong) | - | holds [0-20.58s] | + only Qwen-7B | - | - |
| wall #2 → child #6 | ✓ | ✗ (wall #2 named wrong, child #6 named wrong) | - | stands near [0-20.58s] | + only Qwen-7B | - | - |
| wall #2 → sofa #7 | ✓ | ✗ (wall #2 named wrong, sofa #7 named wrong) | - | stands near [0-20.58s] | + only Qwen-7B | - | - |
| wall #2 → ballon #8 | ✓ | ✗ (wall #2 named wrong) | - | stands near [0-20.58s] | + only Qwen-7B | - | - |
| wall #2 → carpet #9 | ✓ | ✗ (wall #2 named wrong, carpet #9 named wrong) | - | stands near [0-20.58s] | + only Qwen-7B | - | - |
| wall #2 → adult #10 | ✓ | ✗ (wall #2 named wrong) | - | stands near [0-20.58s] | + only Qwen-7B | - | - |
| wall #2 → ballon #11 | ✓ | ✗ (wall #2 named wrong) | - | stands near [0-20.58s] | + only Qwen-7B | - | - |
| adult #5 → wall #2 | ✓ | ✗ (wall #2 named wrong) | - | observes [0-20.58s] | + only Qwen-7B | - | - |


## 1015_4698622422

42.0 s video; humans: 13 objects, 15 relations on 9 pairs; Qwen-7B: 14 relations on 14 pairs.

**Masks given to Qwen-7B:** 13 of 13 objects

**Pairs:** 0 in both, 9 missed by Qwen-7B, 0 reversed, 0 with an object Qwen-7B was not given, 14 only Qwen-7B

**Objects: 3/13 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | tree | yes (object 1) | child | mismatch | ✗ |
| 2 | grass | yes (object 2) | racket | mismatch | ✗ |
| 3 | adult | yes (object 3) | ball | mismatch | ✗ |
| 4 | child | yes (object 4) | car | mismatch | ✗ |
| 5 | table | yes (object 5) | car | mismatch | ✗ |
| 6 | hat | yes (object 6) | car | mismatch | ✗ |
| 7 | bat | yes (object 7) | car | mismatch | ✗ |
| 8 | ball | yes (object 8) | car | mismatch | ✗ |
| 9 | car | yes (object 9) | car | identical | ✓ |
| 10 | adult | yes (object 10) | car | mismatch | ✗ |
| 11 | child | yes (object 11) | car | mismatch | ✗ |
| 12 | car | yes (object 12) | car | identical | ✓ |
| 13 | car | yes (object 13) | car | identical | ✓ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| adult #3 → grass #2 | ✓ | ✗ (adult #3 named wrong, grass #2 named wrong) | standing on [18.8-19.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #4 → grass #2 | ✓ | ✗ (child #4 named wrong, grass #2 named wrong) | on [0-41.8s]; walking on [0-10.4s]; squatting on [19-41.8s] | - | ✗ Qwen-7B missed this pair | - - - | - - - |
| child #4 → bat #7 | ✓ | ✗ (child #4 named wrong, bat #7 named wrong) | holding [0-36.2s]; throwing [36-36.6s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| child #4 → ball #8 | ✓ | ✗ (child #4 named wrong, ball #8 named wrong) | hitting [10.4-12.6s, 20.6-21.8s, 23.6-24.6s, 26.6-27.6s, 29-29.8s, 33.4-34.4s]; chasing [12.6-39.2s]; kicking [36.2-39.2s]; playing with [6.6-40.2s] | - | ✗ Qwen-7B missed this pair | - - - - | - - - - |
| ball #8 → grass #2 | ✓ | ✗ (ball #8 named wrong, grass #2 named wrong) | on [0-41.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #10 → grass #2 | ✓ | ✗ (adult #10 named wrong, grass #2 named wrong) | standing on [40-41.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #10 → child #4 | ✓ | ✗ (adult #10 named wrong, child #4 named wrong) | pulling [40.6-41.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #10 → hat #6 | ✓ | ✗ (adult #10 named wrong, hat #6 named wrong) | holding [40-41.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #11 → adult #3 | ✓ | ✗ (child #11 named wrong, adult #3 named wrong) | in front of [19-19.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| tree #1 → grass #2 | ✓ | ✗ (tree #1 named wrong, grass #2 named wrong) | - | plays with [-] | + only Qwen-7B | - | - |
| tree #1 → adult #3 | ✓ | ✗ (tree #1 named wrong, adult #3 named wrong) | - | kicks [-] | + only Qwen-7B | - | - |
| grass #2 → tree #1 | ✓ | ✗ (grass #2 named wrong, tree #1 named wrong) | - | held by [-] | + only Qwen-7B | - | - |
| adult #3 → tree #1 | ✓ | ✗ (adult #3 named wrong, tree #1 named wrong) | - | in front of [-] | + only Qwen-7B | - | - |
| child #4 → tree #1 | ✓ | ✗ (child #4 named wrong, tree #1 named wrong) | - | behind [-] | + only Qwen-7B | - | - |
| table #5 → tree #1 | ✓ | ✗ (table #5 named wrong, tree #1 named wrong) | - | behind [-] | + only Qwen-7B | - | - |
| hat #6 → tree #1 | ✓ | ✗ (hat #6 named wrong, tree #1 named wrong) | - | behind [-] | + only Qwen-7B | - | - |
| bat #7 → tree #1 | ✓ | ✗ (bat #7 named wrong, tree #1 named wrong) | - | behind [-] | + only Qwen-7B | - | - |
| ball #8 → tree #1 | ✓ | ✗ (ball #8 named wrong, tree #1 named wrong) | - | behind [-] | + only Qwen-7B | - | - |
| car #9 → tree #1 | ✓ | ✗ (tree #1 named wrong) | - | behind [-] | + only Qwen-7B | - | - |
| adult #10 → tree #1 | ✓ | ✗ (adult #10 named wrong, tree #1 named wrong) | - | behind [-] | + only Qwen-7B | - | - |
| child #11 → tree #1 | ✓ | ✗ (child #11 named wrong, tree #1 named wrong) | - | behind [-] | + only Qwen-7B | - | - |
| car #12 → tree #1 | ✓ | ✗ (tree #1 named wrong) | - | behind [-] | + only Qwen-7B | - | - |
| car #13 → tree #1 | ✓ | ✗ (tree #1 named wrong) | - | behind [-] | + only Qwen-7B | - | - |


## 1021_4278168115

79.8 s video; humans: 11 objects, 21 relations on 19 pairs; Qwen-7B: 8 relations on 7 pairs.

**Masks given to Qwen-7B:** 11 of 11 objects

**Pairs:** 0 in both, 19 missed by Qwen-7B, 0 reversed, 0 with an object Qwen-7B was not given, 7 only Qwen-7B

**Objects: 5/11 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | tree | yes (object 1) | child | mismatch | ✗ |
| 2 | floor | yes (object 2) | christmas tree | mismatch | ✗ |
| 3 | gift | yes (object 3) | present | synonym | ✓ |
| 4 | curtain | yes (object 4) | book | mismatch | ✗ |
| 5 | book | yes (object 5) | toy | mismatch | ✗ |
| 6 | adult | yes (object 6) | parent | hypernym/hyponym | ✓ |
| 7 | child | yes (object 7) | floor | mismatch | ✗ |
| 8 | box | yes (object 8) | book | mismatch | ✗ |
| 9 | book | yes (object 9) | book | identical | ✓ |
| 10 | book | yes (object 10) | book | identical | ✓ |
| 11 | book | yes (object 11) | book | identical | ✓ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| tree #1 → floor #2 | ✓ | ✗ (tree #1 named wrong, floor #2 named wrong) | on [0-79.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| gift #3 → floor #2 | ✓ | ✗ (floor #2 named wrong) | on [31-79.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| book #5 → floor #2 | ✓ | ✗ (book #5 named wrong, floor #2 named wrong) | on [42.8-43.4s, 50.6-79.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #6 → floor #2 | ✓ | ✗ (floor #2 named wrong) | sitting on [0-79.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #6 → gift #3 | ✓ | ✓ | holding [0-3s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #6 → book #5 | ✓ | ✗ (book #5 named wrong) | touching [49.4-52s]; holding [49-51.2s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| adult #6 → box #8 | ✓ | ✗ (box #8 named wrong) | opening [33.4-42.4s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #7 → floor #2 | ✓ | ✗ (child #7 named wrong, floor #2 named wrong) | on [0-79.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #7 → gift #3 | ✓ | ✗ (child #7 named wrong) | opening [3.6-31s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #7 → book #5 | ✓ | ✗ (child #7 named wrong, book #5 named wrong) | holding [43.2-48.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #7 → adult #6 | ✓ | ✗ (child #7 named wrong) | in front of [0-79.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #7 → box #8 | ✓ | ✗ (child #7 named wrong, box #8 named wrong) | holding [31-33.2s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #7 → book #9 | ✓ | ✗ (child #7 named wrong) | touching [66.2-71.2s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #7 → book #10 | ✓ | ✗ (child #7 named wrong) | holding [50-54s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #7 → book #11 | ✓ | ✗ (child #7 named wrong) | touching [78.2-79.8s]; holding [54.6-65.4s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| box #8 → floor #2 | ✓ | ✗ (box #8 named wrong, floor #2 named wrong) | on [42.4-79.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| book #9 → floor #2 | ✓ | ✗ (floor #2 named wrong) | on [42.8-79.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| book #10 → floor #2 | ✓ | ✗ (floor #2 named wrong) | on [42.8-50s, 54-79.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| book #11 → floor #2 | ✓ | ✗ (floor #2 named wrong) | on [42.8-54.6s, 65.4-79.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| tree #1 → gift #3 | ✓ | ✗ (tree #1 named wrong) | - | playing with [0-80.7975s]; opening [0-80.7975s] | + only Qwen-7B | - | - |
| tree #1 → curtain #4 | ✓ | ✗ (tree #1 named wrong, curtain #4 named wrong) | - | reading [39.9-80.7975s] | + only Qwen-7B | - | - |
| tree #1 → adult #6 | ✓ | ✗ (tree #1 named wrong) | - | receiving help from [0-80.7975s] | + only Qwen-7B | - | - |
| tree #1 → box #8 | ✓ | ✗ (tree #1 named wrong, box #8 named wrong) | - | holding [39.9-80.7975s] | + only Qwen-7B | - | - |
| tree #1 → book #9 | ✓ | ✗ (tree #1 named wrong) | - | holding [39.9-80.7975s] | + only Qwen-7B | - | - |
| tree #1 → book #10 | ✓ | ✗ (tree #1 named wrong) | - | holding [39.9-80.7975s] | + only Qwen-7B | - | - |
| tree #1 → book #11 | ✓ | ✗ (tree #1 named wrong) | - | holding [39.9-80.7975s] | + only Qwen-7B | - | - |


## 1025_4615486172

90.0 s video; humans: 27 objects, 24 relations on 23 pairs; Qwen-7B: 29 relations on 29 pairs.

**Masks given to Qwen-7B:** 27 of 27 objects

**Pairs:** 1 in both, 22 missed by Qwen-7B, 0 reversed, 0 with an object Qwen-7B was not given, 28 only Qwen-7B

**Objects: 4/27 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | rock | yes (object 1) | woman | mismatch | ✗ |
| 2 | floor | yes (object 2) | baby | mismatch | ✗ |
| 3 | ceiling | yes (object 3) | birthday cake | mismatch | ✗ |
| 4 | wall | yes (object 4) | balloons | mismatch | ✗ |
| 5 | door | yes (object 5) | table | mismatch | ✗ |
| 6 | curtain | yes (object 6) | chair | mismatch | ✗ |
| 7 | shelf | yes (object 7) | high chair | mismatch | ✗ |
| 8 | window | yes (object 8) | candles | mismatch | ✗ |
| 9 | adult | yes (object 9) | cup | mismatch | ✗ |
| 10 | child | yes (object 10) | phone | mismatch | ✗ |
| 11 | table | yes (object 11) | man | mismatch | ✗ |
| 12 | chair | yes (object 12) | balloon | mismatch | ✗ |
| 13 | candle | yes (object 13) | balloon | mismatch | ✗ |
| 14 | cake | yes (object 14) | balloon | mismatch | ✗ |
| 15 | cellphone | yes (object 15) | balloon | mismatch | ✗ |
| 16 | ballon | yes (object 16) | balloon | identical | ✓ |
| 17 | chair | yes (object 17) | balloon | mismatch | ✗ |
| 18 | ballon | yes (object 18) | balloon | identical | ✓ |
| 19 | adult | yes (object 19) | balloon | mismatch | ✗ |
| 20 | chair | yes (object 20) | balloon | mismatch | ✗ |
| 21 | ballon | yes (object 21) | balloon | identical | ✓ |
| 22 | adult | yes (object 22) | balloon | mismatch | ✗ |
| 23 | chair | yes (object 23) | balloon | mismatch | ✗ |
| 24 | ballon | yes (object 24) | balloon | identical | ✓ |
| 25 | adult | yes (object 25) | balloon | mismatch | ✗ |
| 26 | chair | yes (object 26) | balloon | mismatch | ✗ |
| 27 | chair | yes (object 27) | balloon | mismatch | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| adult #9 → door #5 | ✓ | ✗ (adult #9 named wrong, door #5 named wrong) | entering [3.4-6.2s] | is on [0-90s] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| adult #9 → cake #14 | ✓ | ✗ (adult #9 named wrong, cake #14 named wrong) | holding [2.2-29.2s, 76.8-90s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #10 → cake #14 | ✓ | ✗ (child #10 named wrong, cake #14 named wrong) | touching [75.4-77s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #10 → chair #27 | ✓ | ✗ (child #10 named wrong, chair #27 named wrong) | beside [5.2-90s] | - | ✗ Qwen-7B missed this pair | - | - |
| chair #12 → ballon #16 | ✓ | ✗ (chair #12 named wrong) | in front of [4.2-90s] | - | ✗ Qwen-7B missed this pair | - | - |
| chair #12 → ballon #18 | ✓ | ✗ (chair #12 named wrong) | in front of [4.2-90s] | - | ✗ Qwen-7B missed this pair | - | - |
| candle #13 → cake #14 | ✓ | ✗ (candle #13 named wrong, cake #14 named wrong) | on [2.8-90s] | - | ✗ Qwen-7B missed this pair | - | - |
| cake #14 → table #11 | ✓ | ✗ (cake #14 named wrong, table #11 named wrong) | on [27.6-86.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| ballon #16 → wall #4 | ✓ | ✗ (wall #4 named wrong) | on [4.2-90s] | - | ✗ Qwen-7B missed this pair | - | - |
| ballon #16 → ballon #18 | ✓ | ✓ | next to [4.2-90s] | - | ✗ Qwen-7B missed this pair | - | - |
| chair #17 → chair #12 | ✓ | ✗ (chair #17 named wrong, chair #12 named wrong) | next to [4.2-90s] | - | ✗ Qwen-7B missed this pair | - | - |
| ballon #18 → wall #4 | ✓ | ✗ (wall #4 named wrong) | on [4.2-90s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #19 → child #10 | ✓ | ✗ (adult #19 named wrong, child #10 named wrong) | holding [12.8-90s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #19 → chair #12 | ✓ | ✗ (adult #19 named wrong, chair #12 named wrong) | picking [31.6-35.4s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #19 → candle #13 | ✓ | ✗ (adult #19 named wrong, candle #13 named wrong) | blowing [58.8-61.4s] | - | ✗ Qwen-7B missed this pair | - | - |
| chair #20 → chair #17 | ✓ | ✗ (chair #20 named wrong, chair #17 named wrong) | beside [4-90s] | - | ✗ Qwen-7B missed this pair | - | - |
| ballon #21 → ceiling #3 | ✓ | ✗ (ceiling #3 named wrong) | on [13.4-20s] | - | ✗ Qwen-7B missed this pair | - | - |
| ballon #21 → table #11 | ✓ | ✗ (table #11 named wrong) | over [0-90s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #22 → floor #2 | ✓ | ✗ (adult #22 named wrong, floor #2 named wrong) | squatting on [50.4-90s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #22 → child #10 | ✓ | ✗ (adult #22 named wrong, child #10 named wrong) | looking at [62-83s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #22 → chair #12 | ✓ | ✗ (adult #22 named wrong, chair #12 named wrong) | in front of [49.8-90s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #22 → candle #13 | ✓ | ✗ (adult #22 named wrong, candle #13 named wrong) | blowing [58.8-61.4s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #22 → adult #19 | ✓ | ✗ (adult #22 named wrong, adult #19 named wrong) | hugging [50.4-81.2s]; next to [49.2-90s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| rock #1 → floor #2 | ✓ | ✗ (rock #1 named wrong, floor #2 named wrong) | - | interacts with [0-90s] | + only Qwen-7B | - | - |
| rock #1 → door #5 | ✓ | ✗ (rock #1 named wrong, door #5 named wrong) | - | sits next to [0-90s] | + only Qwen-7B | - | - |
| floor #2 → rock #1 | ✓ | ✗ (floor #2 named wrong, rock #1 named wrong) | - | is held by [0-90s] | + only Qwen-7B | - | - |
| floor #2 → child #10 | ✓ | ✗ (floor #2 named wrong, child #10 named wrong) | - | wears [0-90s] | + only Qwen-7B | - | - |
| ceiling #3 → door #5 | ✓ | ✗ (ceiling #3 named wrong, door #5 named wrong) | - | is on [0-90s] | + only Qwen-7B | - | - |
| wall #4 → door #5 | ✓ | ✗ (wall #4 named wrong, door #5 named wrong) | - | floats above [0-90s] | + only Qwen-7B | - | - |
| door #5 → curtain #6 | ✓ | ✗ (door #5 named wrong, curtain #6 named wrong) | - | has [0-90s] | + only Qwen-7B | - | - |
| door #5 → shelf #7 | ✓ | ✗ (door #5 named wrong, shelf #7 named wrong) | - | has [0-90s] | + only Qwen-7B | - | - |
| curtain #6 → door #5 | ✓ | ✗ (curtain #6 named wrong, door #5 named wrong) | - | is behind [0-90s] | + only Qwen-7B | - | - |
| window #8 → ceiling #3 | ✓ | ✗ (window #8 named wrong, ceiling #3 named wrong) | - | are on [0-90s] | + only Qwen-7B | - | - |
| child #10 → rock #1 | ✓ | ✗ (child #10 named wrong, rock #1 named wrong) | - | is used by [0-90s] | + only Qwen-7B | - | - |
| table #11 → door #5 | ✓ | ✗ (table #11 named wrong, door #5 named wrong) | - | stands behind [0-90s] | + only Qwen-7B | - | - |
| chair #12 → door #5 | ✓ | ✗ (chair #12 named wrong, door #5 named wrong) | - | floats above [0-90s] | + only Qwen-7B | - | - |
| candle #13 → door #5 | ✓ | ✗ (candle #13 named wrong, door #5 named wrong) | - | floats above [0-90s] | + only Qwen-7B | - | - |
| cake #14 → door #5 | ✓ | ✗ (cake #14 named wrong, door #5 named wrong) | - | floats above [0-90s] | + only Qwen-7B | - | - |
| cellphone #15 → door #5 | ✓ | ✗ (cellphone #15 named wrong, door #5 named wrong) | - | floats above [0-90s] | + only Qwen-7B | - | - |
| ballon #16 → door #5 | ✓ | ✗ (door #5 named wrong) | - | floats above [0-90s] | + only Qwen-7B | - | - |
| chair #17 → door #5 | ✓ | ✗ (chair #17 named wrong, door #5 named wrong) | - | floats above [0-90s] | + only Qwen-7B | - | - |
| ballon #18 → door #5 | ✓ | ✗ (door #5 named wrong) | - | floats above [0-90s] | + only Qwen-7B | - | - |
| adult #19 → door #5 | ✓ | ✗ (adult #19 named wrong, door #5 named wrong) | - | floats above [0-90s] | + only Qwen-7B | - | - |
| chair #20 → door #5 | ✓ | ✗ (chair #20 named wrong, door #5 named wrong) | - | floats above [0-90s] | + only Qwen-7B | - | - |
| ballon #21 → door #5 | ✓ | ✗ (door #5 named wrong) | - | floats above [0-90s] | + only Qwen-7B | - | - |
| adult #22 → door #5 | ✓ | ✗ (adult #22 named wrong, door #5 named wrong) | - | floats above [0-90s] | + only Qwen-7B | - | - |
| chair #23 → door #5 | ✓ | ✗ (chair #23 named wrong, door #5 named wrong) | - | floats above [0-90s] | + only Qwen-7B | - | - |
| ballon #24 → door #5 | ✓ | ✗ (door #5 named wrong) | - | floats above [0-90s] | + only Qwen-7B | - | - |
| adult #25 → door #5 | ✓ | ✗ (adult #25 named wrong, door #5 named wrong) | - | floats above [0-90s] | + only Qwen-7B | - | - |
| chair #26 → door #5 | ✓ | ✗ (chair #26 named wrong, door #5 named wrong) | - | floats above [0-90s] | + only Qwen-7B | - | - |
| chair #27 → door #5 | ✓ | ✗ (chair #27 named wrong, door #5 named wrong) | - | floats above [0-90s] | + only Qwen-7B | - | - |


## P03_06

109.2 s video; humans: 65 objects, 20 relations on 16 pairs; Qwen-7B: 20 relations on 20 pairs.

**Masks given to Qwen-7B:** 39 of 65 objects (25 after the first 40, 1 with no mask on the frames Qwen-7B reads)

**Pairs:** 0 in both, 11 missed by Qwen-7B, 0 reversed, 5 with an object Qwen-7B was not given, 20 only Qwen-7B

**Objects: 2/65 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | floor | yes (object 1) | spatula | mismatch | ✗ |
| 2 | wall | yes (object 2) | pot | mismatch | ✗ |
| 3 | cloth | yes (object 3) | stove | mismatch | ✗ |
| 4 | mat | yes (object 4) | kitchen counter | mismatch | ✗ |
| 5 | countertop | yes (object 5) | cutting board | mismatch | ✗ |
| 6 | grain | yes (object 6) | knife | mismatch | ✗ |
| 7 | simmering | yes (object 7) | plate | mismatch | ✗ |
| 8 | rack | yes (object 8) | sink | mismatch | ✗ |
| 9 | spatula | yes (object 9) | drawer | mismatch | ✗ |
| 10 | chopstick | no: no mask on the frames Qwen-7B reads | - (never shown to Qwen-7B) | - | ✗ |
| 11 | teapot | yes (object 10) | utensils | hypernym/hyponym | ✓ |
| 12 | pot | yes (object 11) | spoon | mismatch | ✗ |
| 13 | board | yes (object 12) | food | mismatch | ✗ |
| 14 | cover | yes (object 13) | hand | mismatch | ✗ |
| 15 | brush | yes (object 14) | kitchen sink | mismatch | ✗ |
| 16 | rag | yes (object 15) | water | mismatch | ✗ |
| 17 | dustbin | yes (object 16) | bowl | mismatch | ✗ |
| 18 | washer | yes (object 17) | spatula | mismatch | ✗ |
| 19 | drawer | yes (object 18) | pot lid | mismatch | ✗ |
| 20 | oven | yes (object 19) | spatula | mismatch | ✗ |
| 21 | stove | yes (object 20) | pot | mismatch | ✗ |
| 22 | sponge | yes (object 21) | stove | mismatch | ✗ |
| 23 | cabinet | yes (object 22) | kitchen counter | mismatch | ✗ |
| 24 | door | yes (object 23) | cutting board | mismatch | ✗ |
| 25 | glass | yes (object 24) | knife | mismatch | ✗ |
| 26 | spoon | yes (object 25) | plate | mismatch | ✗ |
| 27 | towel | yes (object 26) | sink | mismatch | ✗ |
| 28 | basket | yes (object 27) | drawer | semantic overlap | ✓ |
| 29 | adult | yes (object 28) | utensils | mismatch | ✗ |
| 30 | sink | yes (object 29) | spoon | mismatch | ✗ |
| 31 | faucet | yes (object 30) | food | mismatch | ✗ |
| 32 | table | yes (object 31) | hand | mismatch | ✗ |
| 33 | knife | yes (object 32) | kitchen sink | mismatch | ✗ |
| 34 | fork | yes (object 33) | bowl | mismatch | ✗ |
| 35 | plate | yes (object 34) | spatula | mismatch | ✗ |
| 36 | bowl | yes (object 35) | pot lid | mismatch | ✗ |
| 37 | bottle | yes (object 36) | spatula | mismatch | ✗ |
| 38 | box | yes (object 37) | pot | mismatch | ✗ |
| 39 | mat | yes (object 38) | stove | mismatch | ✗ |
| 40 | grain | yes (object 39) | kitchen counter | mismatch | ✗ |
| 41 | simmering | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 42 | rack | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 43 | pot | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 44 | cover | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 45 | oven | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 46 | cabinet | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 47 | glass | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 48 | spoon | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 49 | basket | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 50 | knife | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 51 | plate | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 52 | bowl | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 53 | bottle | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 54 | cup | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 55 | paper | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 56 | grain | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 57 | simmering | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 58 | pot | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 59 | basket | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 60 | knife | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 61 | plate | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 62 | bottle | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 63 | pot | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 64 | plate | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 65 | plate | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| rag #16 → oven #20 | ✓ | ✗ (rag #16 named wrong, oven #20 named wrong) | hanging from [0-109.2s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #29 → grain #6 | ✓ | ✗ (adult #29 named wrong, grain #6 named wrong) | stirring [28.2-35.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #29 → simmering #7 | ✓ | ✗ (adult #29 named wrong, simmering #7 named wrong) | stirring [3.8-42.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #29 → spatula #9 | ✓ | ✗ (adult #29 named wrong, spatula #9 named wrong) | holding [2.8-9s, 66-69s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #29 → pot #12 | ✓ | ✗ (adult #29 named wrong, pot #12 named wrong) | touching [3.4-8.8s]; holding [69.4-99.6s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| adult #29 → drawer #19 | ✓ | ✗ (adult #29 named wrong, drawer #19 named wrong) | opening [24.6-26.6s, 101-101.8s]; pulling [25.2-26.4s, 101-102.4s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| adult #29 → stove #21 | ✓ | ✗ (adult #29 named wrong, stove #21 named wrong) | touching [9.2-10s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #29 → glass #25 | ✓ | ✗ (adult #29 named wrong, glass #25 named wrong) | holding [13.4-13.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #29 → spoon #26 | ✓ | ✗ (adult #29 named wrong, spoon #26 named wrong) | holding [26.4-97.2s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #29 → knife #33 | ✓ | ✗ (adult #29 named wrong, knife #33 named wrong) | holding [102.2-109.2s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #29 → fork #34 | ✓ | ✗ (adult #29 named wrong, fork #34 named wrong) | holding [103-109.2s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #29 → pot #43 | ✗ (pot #43 not given) | ✗ (adult #29 named wrong, pot #43 not given) | touching [10.2-12.6s]; holding [20.8-23.2s, 28-62.8s] | - | ⊘ an object was not given to Qwen-7B (40-object cap / no mask on its frames) | - - | - - |
| adult #29 → cover #44 | ✗ (cover #44 not given) | ✗ (adult #29 named wrong, cover #44 not given) | holding [10.2-12.2s] | - | ⊘ an object was not given to Qwen-7B (40-object cap / no mask on its frames) | - | - |
| adult #29 → cabinet #46 | ✗ (cabinet #46 not given) | ✗ (adult #29 named wrong, cabinet #46 not given) | opening [14.2-15s] | - | ⊘ an object was not given to Qwen-7B (40-object cap / no mask on its frames) | - | - |
| adult #29 → plate #64 | ✗ (plate #64 not given) | ✗ (adult #29 named wrong, plate #64 not given) | holding [15-19.6s] | - | ⊘ an object was not given to Qwen-7B (40-object cap / no mask on its frames) | - | - |
| adult #29 → plate #65 | ✗ (plate #65 not given) | ✗ (adult #29 named wrong, plate #65 not given) | holding [15.4-19.4s]; touching [63-64.8s] | - | ⊘ an object was not given to Qwen-7B (40-object cap / no mask on its frames) | - - | - - |
| floor #1 → stove #21 | ✓ | ✗ (floor #1 named wrong, stove #21 named wrong) | - | on top of [0-5.00917s] | + only Qwen-7B | - | - |
| floor #1 → sponge #22 | ✓ | ✗ (floor #1 named wrong, sponge #22 named wrong) | - | in [0-5.00917s] | + only Qwen-7B | - | - |
| floor #1 → cabinet #23 | ✓ | ✗ (floor #1 named wrong, cabinet #23 named wrong) | - | in [0-5.00917s] | + only Qwen-7B | - | - |
| floor #1 → door #24 | ✓ | ✗ (floor #1 named wrong, door #24 named wrong) | - | in [0-5.00917s] | + only Qwen-7B | - | - |
| floor #1 → glass #25 | ✓ | ✗ (floor #1 named wrong, glass #25 named wrong) | - | in [0-5.00917s] | + only Qwen-7B | - | - |
| floor #1 → spoon #26 | ✓ | ✗ (floor #1 named wrong, spoon #26 named wrong) | - | in [0-5.00917s] | + only Qwen-7B | - | - |
| floor #1 → towel #27 | ✓ | ✗ (floor #1 named wrong, towel #27 named wrong) | - | in [0-5.00917s] | + only Qwen-7B | - | - |
| floor #1 → basket #28 | ✓ | ✗ (floor #1 named wrong) | - | in [0-5.00917s] | + only Qwen-7B | - | - |
| floor #1 → adult #29 | ✓ | ✗ (floor #1 named wrong, adult #29 named wrong) | - | in [0-5.00917s] | + only Qwen-7B | - | - |
| floor #1 → sink #30 | ✓ | ✗ (floor #1 named wrong, sink #30 named wrong) | - | in [0-5.00917s] | + only Qwen-7B | - | - |
| floor #1 → faucet #31 | ✓ | ✗ (floor #1 named wrong, faucet #31 named wrong) | - | in [0-5.00917s] | + only Qwen-7B | - | - |
| floor #1 → table #32 | ✓ | ✗ (floor #1 named wrong, table #32 named wrong) | - | in [0-5.00917s] | + only Qwen-7B | - | - |
| floor #1 → knife #33 | ✓ | ✗ (floor #1 named wrong, knife #33 named wrong) | - | in [0-5.00917s] | + only Qwen-7B | - | - |
| floor #1 → fork #34 | ✓ | ✗ (floor #1 named wrong, fork #34 named wrong) | - | in [0-5.00917s] | + only Qwen-7B | - | - |
| floor #1 → plate #35 | ✓ | ✗ (floor #1 named wrong, plate #35 named wrong) | - | in [0-5.00917s] | + only Qwen-7B | - | - |
| floor #1 → bowl #36 | ✓ | ✗ (floor #1 named wrong, bowl #36 named wrong) | - | in [0-5.00917s] | + only Qwen-7B | - | - |
| floor #1 → bottle #37 | ✓ | ✗ (floor #1 named wrong, bottle #37 named wrong) | - | in [0-5.00917s] | + only Qwen-7B | - | - |
| floor #1 → box #38 | ✓ | ✗ (floor #1 named wrong, box #38 named wrong) | - | in [0-5.00917s] | + only Qwen-7B | - | - |
| floor #1 → mat #39 | ✓ | ✗ (floor #1 named wrong, mat #39 named wrong) | - | in [0-5.00917s] | + only Qwen-7B | - | - |
| floor #1 → grain #40 | ✓ | ✗ (floor #1 named wrong, grain #40 named wrong) | - | in [0-5.00917s] | + only Qwen-7B | - | - |


## P14_06

64.6 s video; humans: 34 objects, 10 relations on 7 pairs; Qwen-7B: 0 relations on 0 pairs (answer cut off at the token limit, read up to there).

**Masks given to Qwen-7B:** 34 of 34 objects

**Pairs:** 0 in both, 7 missed by Qwen-7B, 0 reversed, 0 with an object Qwen-7B was not given, 0 only Qwen-7B

**Objects: 2/34 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | floor | yes (object 1) | box | mismatch | ✗ |
| 2 | wall | yes (object 2) | cereal bowl | mismatch | ✗ |
| 3 | countertop | yes (object 3) | sink | semantic overlap | ✓ |
| 4 | grain | yes (object 4) | kitchen counter | mismatch | ✗ |
| 5 | beverage | yes (object 5) | milk carton | semantic overlap | ✓ |
| 6 | rack | yes (object 6) | scissors | mismatch | ✗ |
| 7 | cover | yes (object 7) | dishes | mismatch | ✗ |
| 8 | carpet | yes (object 8) | cereal | mismatch | ✗ |
| 9 | dustbin | yes (object 9) | - (Qwen-7B wrote no label) | - | ✗ |
| 10 | stairs | yes (object 10) | - (Qwen-7B wrote no label) | - | ✗ |
| 11 | sponge | yes (object 11) | - (Qwen-7B wrote no label) | - | ✗ |
| 12 | shelf | yes (object 12) | - (Qwen-7B wrote no label) | - | ✗ |
| 13 | window | yes (object 13) | - (Qwen-7B wrote no label) | - | ✗ |
| 14 | cabinet | yes (object 14) | - (Qwen-7B wrote no label) | - | ✗ |
| 15 | door | yes (object 15) | - (Qwen-7B wrote no label) | - | ✗ |
| 16 | fridge | yes (object 16) | - (Qwen-7B wrote no label) | - | ✗ |
| 17 | spoon | yes (object 17) | - (Qwen-7B wrote no label) | - | ✗ |
| 18 | scissor | yes (object 18) | - (Qwen-7B wrote no label) | - | ✗ |
| 19 | adult | yes (object 19) | - (Qwen-7B wrote no label) | - | ✗ |
| 20 | sink | yes (object 20) | - (Qwen-7B wrote no label) | - | ✗ |
| 21 | faucet | yes (object 21) | - (Qwen-7B wrote no label) | - | ✗ |
| 22 | table | yes (object 22) | - (Qwen-7B wrote no label) | - | ✗ |
| 23 | knife | yes (object 23) | - (Qwen-7B wrote no label) | - | ✗ |
| 24 | plate | yes (object 24) | - (Qwen-7B wrote no label) | - | ✗ |
| 25 | bowl | yes (object 25) | - (Qwen-7B wrote no label) | - | ✗ |
| 26 | cup | yes (object 26) | - (Qwen-7B wrote no label) | - | ✗ |
| 27 | paper | yes (object 27) | - (Qwen-7B wrote no label) | - | ✗ |
| 28 | box | yes (object 28) | - (Qwen-7B wrote no label) | - | ✗ |
| 29 | beverage | yes (object 29) | - (Qwen-7B wrote no label) | - | ✗ |
| 30 | cabinet | yes (object 30) | - (Qwen-7B wrote no label) | - | ✗ |
| 31 | door | yes (object 31) | - (Qwen-7B wrote no label) | - | ✗ |
| 32 | plate | yes (object 32) | - (Qwen-7B wrote no label) | - | ✗ |
| 33 | bowl | yes (object 33) | - (Qwen-7B wrote no label) | - | ✗ |
| 34 | bowl | yes (object 34) | - (Qwen-7B wrote no label) | - | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| beverage #5 → table #22 | ✓ | ✗ (table #22 named wrong) | on [17.8-19.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #19 → beverage #5 | ✓ | ✗ (adult #19 named wrong) | holding [13.2-40.8s]; opening [17.8-19.8s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| adult #19 → fridge #16 | ✓ | ✗ (adult #19 named wrong, fridge #16 named wrong) | opening [10.4-12s, 35.8-38.2s]; closing [13.8-15.2s, 41.6-43s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| adult #19 → spoon #17 | ✓ | ✗ (adult #19 named wrong, spoon #17 named wrong) | holding [60.2-64.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #19 → box #28 | ✓ | ✗ (adult #19 named wrong, box #28 named wrong) | holding [45.6-57.4s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #19 → bowl #33 | ✓ | ✗ (adult #19 named wrong, bowl #33 named wrong) | holding [4.2-9s]; touching [21-21.6s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| bowl #33 → table #22 | ✓ | ✗ (bowl #33 named wrong, table #22 named wrong) | on [9-64.6s] | - | ✗ Qwen-7B missed this pair | - | - |


## P28_19

90.0 s video; humans: 28 objects, 10 relations on 6 pairs; Qwen-7B: 28 relations on 28 pairs.

**Masks given to Qwen-7B:** 27 of 28 objects (0 after the first 40, 1 with no mask on the frames Qwen-7B reads)

**Pairs:** 0 in both, 6 missed by Qwen-7B, 0 reversed, 0 with an object Qwen-7B was not given, 28 only Qwen-7B

**Objects: 0/28 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 1 | floor | yes (object 1) | hand | mismatch | ✗ |
| 2 | wall | yes (object 2) | knife | mismatch | ✗ |
| 3 | egg | yes (object 3) | chopping board | mismatch | ✗ |
| 4 | others | yes (object 4) | countertop | mismatch | ✗ |
| 5 | countertop | yes (object 5) | package | mismatch | ✗ |
| 6 | spatula | yes (object 6) | spices | mismatch | ✗ |
| 7 | board | yes (object 7) | stove | mismatch | ✗ |
| 8 | rag | yes (object 8) | pan | mismatch | ✗ |
| 9 | dustbin | yes (object 9) | oil bottle | mismatch | ✗ |
| 10 | oven | yes (object 10) | plate | mismatch | ✗ |
| 11 | stove | yes (object 11) | tortilla | mismatch | ✗ |
| 12 | pan | yes (object 12) | box | mismatch | ✗ |
| 13 | window | yes (object 13) | tomato | mismatch | ✗ |
| 14 | cabinet | yes (object 14) | onion | mismatch | ✗ |
| 15 | door | yes (object 15) | pepper | mismatch | ✗ |
| 16 | adult | yes (object 16) | spatula | mismatch | ✗ |
| 17 | sink | yes (object 17) | spoon | mismatch | ✗ |
| 18 | knife | yes (object 18) | sink | mismatch | ✗ |
| 19 | plate | yes (object 19) | kitchen towel | mismatch | ✗ |
| 20 | bottle | yes (object 20) | cabinet | mismatch | ✗ |
| 21 | bag | yes (object 21) | drawer | mismatch | ✗ |
| 22 | box | yes (object 22) | spices | mismatch | ✗ |
| 23 | countertop | yes (object 23) | bowl | mismatch | ✗ |
| 24 | window | no: no mask on the frames Qwen-7B reads | - (never shown to Qwen-7B) | - | ✗ |
| 25 | cabinet | yes (object 24) | spatula | mismatch | ✗ |
| 26 | vegetable | yes (object 25) | spices | mismatch | ✗ |
| 27 | bag | yes (object 26) | spatula | mismatch | ✗ |
| 28 | box | yes (object 27) | spices | mismatch | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| adult #16 → stove #11 | ✓ | ✗ (adult #16 named wrong, stove #11 named wrong) | touching [60.4-70.8s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #16 → pan #12 | ✓ | ✗ (adult #16 named wrong, pan #12 named wrong) | swinging [71.2-79.4s]; holding [82.6-83.8s]; over [84.2-88s] | - | ✗ Qwen-7B missed this pair | - - - | - - - |
| adult #16 → knife #18 | ✓ | ✗ (adult #16 named wrong, knife #18 named wrong) | holding [1.4-43.2s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #16 → bottle #20 | ✓ | ✗ (adult #16 named wrong, bottle #20 named wrong) | holding [43-52.4s]; opening [45-46.2s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| adult #16 → box #22 | ✓ | ✗ (adult #16 named wrong, box #22 named wrong) | holding [53.2-59.2s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #16 → vegetable #26 | ✓ | ✗ (adult #16 named wrong, vegetable #26 named wrong) | holding [1.4-42s]; cutting [2.8-39.6s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| floor #1 → wall #2 | ✓ | ✗ (floor #1 named wrong, wall #2 named wrong) | - | is using [0-93s] | + only Qwen-7B | - | - |
| wall #2 → egg #3 | ✓ | ✗ (wall #2 named wrong, egg #3 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |
| egg #3 → others #4 | ✓ | ✗ (egg #3 named wrong, others #4 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |
| others #4 → countertop #5 | ✓ | ✗ (others #4 named wrong, countertop #5 named wrong) | - | is near [0-93s] | + only Qwen-7B | - | - |
| countertop #5 → spatula #6 | ✓ | ✗ (countertop #5 named wrong, spatula #6 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |
| spatula #6 → board #7 | ✓ | ✗ (spatula #6 named wrong, board #7 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |
| board #7 → rag #8 | ✓ | ✗ (board #7 named wrong, rag #8 named wrong) | - | has pan on it [0-93s] | + only Qwen-7B | - | - |
| rag #8 → board #7 | ✓ | ✗ (rag #8 named wrong, board #7 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |
| rag #8 → dustbin #9 | ✓ | ✗ (rag #8 named wrong, dustbin #9 named wrong) | - | is near [0-93s] | + only Qwen-7B | - | - |
| dustbin #9 → board #7 | ✓ | ✗ (dustbin #9 named wrong, board #7 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |
| oven #10 → others #4 | ✓ | ✗ (oven #10 named wrong, others #4 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |
| stove #11 → oven #10 | ✓ | ✗ (stove #11 named wrong, oven #10 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |
| pan #12 → others #4 | ✓ | ✗ (pan #12 named wrong, others #4 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |
| window #13 → egg #3 | ✓ | ✗ (window #13 named wrong, egg #3 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |
| cabinet #14 → egg #3 | ✓ | ✗ (cabinet #14 named wrong, egg #3 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |
| door #15 → egg #3 | ✓ | ✗ (door #15 named wrong, egg #3 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |
| adult #16 → others #4 | ✓ | ✗ (adult #16 named wrong, others #4 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |
| sink #17 → others #4 | ✓ | ✗ (sink #17 named wrong, others #4 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |
| knife #18 → plate #19 | ✓ | ✗ (knife #18 named wrong, plate #19 named wrong) | - | is near [0-93s] | + only Qwen-7B | - | - |
| plate #19 → bottle #20 | ✓ | ✗ (plate #19 named wrong, bottle #20 named wrong) | - | is hanging on [0-93s] | + only Qwen-7B | - | - |
| bottle #20 → others #4 | ✓ | ✗ (bottle #20 named wrong, others #4 named wrong) | - | is under [0-93s] | + only Qwen-7B | - | - |
| bag #21 → others #4 | ✓ | ✗ (bag #21 named wrong, others #4 named wrong) | - | is under [0-93s] | + only Qwen-7B | - | - |
| box #22 → others #4 | ✓ | ✗ (box #22 named wrong, others #4 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |
| countertop #23 → others #4 | ✓ | ✗ (countertop #23 named wrong, others #4 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |
| cabinet #25 → others #4 | ✓ | ✗ (cabinet #25 named wrong, others #4 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |
| vegetable #26 → others #4 | ✓ | ✗ (vegetable #26 named wrong, others #4 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |
| bag #27 → others #4 | ✓ | ✗ (bag #27 named wrong, others #4 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |
| box #28 → others #4 | ✓ | ✗ (box #28 named wrong, others #4 named wrong) | - | is on [0-93s] | + only Qwen-7B | - | - |

