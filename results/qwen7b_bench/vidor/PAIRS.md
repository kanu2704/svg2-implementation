# vidor: which object pairs Qwen-7B talks about (10 random videos, seed 0)

The same 10 videos as TRASER's page ([`results/traser_bench/vidor/PAIRS.md`](../../traser_bench/vidor/PAIRS.md)), with the answers of Qwen2.5-VL-7B-Instruct (not fine-tuned) in TRASER's pipeline (`../README.md`).

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

**Total over these videos:** 150 human pairs, 55 Qwen-7B pairs; 45 in both, 71 missed, 32 reversed, 2 with an object not given, 10 only Qwen-7B.

| video | source | masks given to Qwen-7B | objects right | relations right | triplets right | human pairs | Qwen-7B pairs | pairs in both | missed by Qwen-7B | reversed | object not given | only Qwen-7B |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [13624759154](#13624759154) | - | 4/5 | 3/5 | 1/19 | 1/19 | 12 | 6 | 6 | 0 | 6 | 0 | 0 |
| [3829541530](#3829541530) | - | 2/2 | 2/2 | 0/2 | 0/2 | 2 | 1 | 1 | 0 | 1 | 0 | 0 |
| [4146348376](#4146348376) | - | 5/5 | 3/5 | 0/3 | 0/3 | 2 | 4 | 1 | 0 | 1 | 0 | 3 |
| [4674481985](#4674481985) | - | 4/6 | 4/6 | 0/17 | 0/17 | 13 | 6 | 6 | 0 | 5 | 2 | 0 |
| [4822859674](#4822859674) | - | 10/10 | 4/10 | 0/70 | 0/70 | 45 | 9 | 7 | 34 | 4 | 0 | 2 |
| [4925211209](#4925211209) | - | 2/2 | 1/2 | 0/3 | 0/3 | 2 | 1 | 1 | 0 | 1 | 0 | 0 |
| [5421648216](#5421648216) | - | 3/3 | 3/3 | 0/15 | 0/15 | 6 | 6 | 6 | 0 | 0 | 0 | 0 |
| [5658916668](#5658916668) | - | 9/9 | 9/9 | 3/34 | 3/34 | 21 | 6 | 3 | 15 | 3 | 0 | 3 |
| [8563398032](#8563398032) | - | 6/6 | 2/6 | 2/30 | 0/30 | 25 | 10 | 9 | 10 | 6 | 0 | 1 |
| [9217939684](#9217939684) | - | 6/6 | 2/6 | 0/48 | 0/48 | 22 | 6 | 5 | 12 | 5 | 0 | 1 |

## 13624759154

11.05 s video; humans: 5 objects, 19 relations on 12 pairs; Qwen-7B: 6 relations on 6 pairs.

**Masks given to Qwen-7B:** 4 of 5 objects (0 after the first 40, 1 with no mask on the frames Qwen-7B reads)

**Pairs:** 6 in both, 0 missed by Qwen-7B, 6 reversed, 0 with an object Qwen-7B was not given, 0 only Qwen-7B

**Objects: 3/5 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | adult | yes (object 1) | Person A | hypernym/hyponym | ✓ |
| 1 | adult | yes (object 2) | Person B | hypernym/hyponym | ✓ |
| 2 | adult | yes (object 3) | Person C | hypernym/hyponym | ✓ |
| 3 | table | yes (object 4) | Cards | mismatch | ✗ |
| 4 | screen/monitor | no: no mask on the frames Qwen-7B reads | - (never shown to Qwen-7B) | - | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| adult #0 → adult #1 | ✓ | ✓ | watch [0-4.04571s, 7.75775-8.42508s, 10.6773-11.0527s]; in front of [0-11.011s] | interacts with [0-9.04091s] | ✓ Qwen-7B has this pair | ✓ ✗ | ✓ ✗ |
| adult #0 → adult #2 | ✓ | ✓ | in front of [0-11.011s] | interacts with [0-9.04091s] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| adult #0 → table #3 | ✓ | ✗ (table #3 named wrong) | next to [0-11.011s] | moves cards [0-9.04091s] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| adult #1 → adult #0 | ✓ | ✓ | watch [0.75075-7.63262s, 8.5085-11.0527s]; speak to [1.08442-10.7607s]; in front of [0-11.011s] | - | ↔ Qwen-7B has it reversed | - - - | - - - |
| adult #1 → adult #2 | ✓ | ✓ | watch [8.13312-8.59192s]; point to [8.21654-8.55021s]; next to [0-11.011s] | interacts with [0-9.04091s] | ✓ Qwen-7B has this pair | ✗ ✗ ✗ | ✗ ✗ ✗ |
| adult #1 → table #3 | ✓ | ✗ (table #3 named wrong) | next to [0-11.011s] | moves cards [0-9.04091s] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| adult #2 → adult #0 | ✓ | ✓ | in front of [0-11.011s] | - | ↔ Qwen-7B has it reversed | - | - |
| adult #2 → adult #1 | ✓ | ✓ | watch [9.75975-10.2185s]; next to [0-11.011s] | - | ↔ Qwen-7B has it reversed | - - | - - |
| adult #2 → table #3 | ✓ | ✗ (table #3 named wrong) | lean on [2.96129-11.0527s]; next to [0-11.011s] | moves cards [0-9.04091s] | ✓ Qwen-7B has this pair | ✗ ✗ | ✗ ✗ |
| table #3 → adult #0 | ✓ | ✗ (table #3 named wrong) | next to [0-11.011s] | - | ↔ Qwen-7B has it reversed | - | - |
| table #3 → adult #1 | ✓ | ✗ (table #3 named wrong) | next to [0-11.011s] | - | ↔ Qwen-7B has it reversed | - | - |
| table #3 → adult #2 | ✓ | ✗ (table #3 named wrong) | next to [0-11.011s] | - | ↔ Qwen-7B has it reversed | - | - |


## 3829541530

5.81 s video; humans: 2 objects, 2 relations on 2 pairs; Qwen-7B: 1 relations on 1 pairs.

**Masks given to Qwen-7B:** 2 of 2 objects

**Pairs:** 1 in both, 0 missed by Qwen-7B, 1 reversed, 0 with an object Qwen-7B was not given, 0 only Qwen-7B

**Objects: 2/2 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | adult | yes (object 1) | person | hypernym/hyponym | ✓ |
| 1 | adult | yes (object 2) | person | hypernym/hyponym | ✓ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| adult #0 → adult #1 | ✓ | ✓ | in front of [1.1011-5.77243s] | standing next to [0-5.81s] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| adult #1 → adult #0 | ✓ | ✓ | in front of [1.1011-5.77243s] | - | ↔ Qwen-7B has it reversed | - | - |


## 4146348376

52.89 s video; humans: 5 objects, 3 relations on 2 pairs; Qwen-7B: 4 relations on 4 pairs.

**Masks given to Qwen-7B:** 5 of 5 objects

**Pairs:** 1 in both, 0 missed by Qwen-7B, 1 reversed, 0 with an object Qwen-7B was not given, 3 only Qwen-7B

**Objects: 3/5 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | bird | yes (object 1) | seagull | hypernym/hyponym | ✓ |
| 1 | adult | yes (object 2) | man | hypernym/hyponym | ✓ |
| 2 | adult | yes (object 3) | shell | mismatch | ✗ |
| 3 | table | yes (object 4) | table | identical | ✓ |
| 4 | table | yes (object 5) | plants | mismatch | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| adult #1 → table #3 | ✓ | ✓ | lean on [1.66833-8.77543s, 11.7784-32.2656s, 37.1705-39.039s]; next to [2.002-8.77543s, 12.012-32.2656s, 37.1705-39.0056s] | writing [7.9834-32.9315s] | ✓ Qwen-7B has this pair | ✗ ✗ | ✗ ✗ |
| table #3 → adult #1 | ✓ | ✓ | in front of [2.002-8.77543s, 12.012-32.2656s, 37.1705-39.0056s] | - | ↔ Qwen-7B has it reversed | - | - |
| bird #0 → table #3 | ✓ | ✓ | - | near [0-56.8817s] | + only Qwen-7B | - | - |
| adult #2 → table #3 | ✓ | ✗ (adult #2 named wrong) | - | on [0-56.8817s] | + only Qwen-7B | - | - |
| table #4 → table #3 | ✓ | ✗ (table #4 named wrong) | - | on [31.9336-40.9149s] | + only Qwen-7B | - | - |


## 4674481985

24.49 s video; humans: 6 objects, 17 relations on 13 pairs; Qwen-7B: 6 relations on 6 pairs.

**Masks given to Qwen-7B:** 4 of 6 objects (0 after the first 40, 2 with no mask on the frames Qwen-7B reads)

**Pairs:** 6 in both, 0 missed by Qwen-7B, 5 reversed, 2 with an object Qwen-7B was not given, 0 only Qwen-7B

**Objects: 4/6 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | adult | yes (object 1) | person | hypernym/hyponym | ✓ |
| 1 | adult | yes (object 2) | person | hypernym/hyponym | ✓ |
| 2 | adult | yes (object 3) | person | hypernym/hyponym | ✓ |
| 3 | adult | no: no mask on the frames Qwen-7B reads | - (never shown to Qwen-7B) | - | ✗ |
| 4 | adult | no: no mask on the frames Qwen-7B reads | - (never shown to Qwen-7B) | - | ✗ |
| 5 | adult | yes (object 4) | person | hypernym/hyponym | ✓ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| adult #0 → adult #1 | ✓ | ✓ | next to [0-6.4064s] | near [0-25.5104s] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| adult #0 → adult #2 | ✓ | ✓ | in front of [0.467133-2.5025s] | near [0-25.5104s] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| adult #0 → adult #5 | ✓ | ✓ | behind [0-11.011s]; away [8.008-11.011s] | near [0-25.5104s] | ✓ Qwen-7B has this pair | ✗ ✗ | ✗ ✗ |
| adult #1 → adult #0 | ✓ | ✓ | watch [2.33567-3.03637s]; next to [0-6.4064s] | - | ↔ Qwen-7B has it reversed | - - | - - |
| adult #1 → adult #2 | ✓ | ✓ | watch [0.467133-2.002s]; in front of [0.467133-2.5025s] | near [0-25.5104s] | ✓ Qwen-7B has this pair | ✗ ✗ | ✗ ✗ |
| adult #1 → adult #5 | ✓ | ✓ | behind [0-6.4064s] | near [0-25.5104s] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| adult #2 → adult #1 | ✓ | ✓ | watch [0.467133-2.5025s]; in front of [0.467133-2.5025s] | - | ↔ Qwen-7B has it reversed | - - | - - |
| adult #2 → adult #5 | ✓ | ✓ | behind [0.467133-2.5025s] | near [0-25.5104s] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| adult #3 → adult #1 | ✗ (adult #3 not given) | ✗ (adult #3 not given) | watch [0.767433-0.967633s] | - | ⊘ an object was not given to Qwen-7B (40-object cap / no mask on its frames) | - | - |
| adult #4 → adult #0 | ✗ (adult #4 not given) | ✗ (adult #4 not given) | watch [0.6006-1.03437s] | - | ⊘ an object was not given to Qwen-7B (40-object cap / no mask on its frames) | - | - |
| adult #5 → adult #0 | ✓ | ✓ | behind [0-11.011s] | - | ↔ Qwen-7B has it reversed | - | - |
| adult #5 → adult #1 | ✓ | ✓ | behind [0-6.4064s] | - | ↔ Qwen-7B has it reversed | - | - |
| adult #5 → adult #2 | ✓ | ✓ | in front of [0.467133-2.5025s] | - | ↔ Qwen-7B has it reversed | - | - |


## 4822859674

35.91 s video; humans: 10 objects, 70 relations on 45 pairs; Qwen-7B: 9 relations on 9 pairs.

**Masks given to Qwen-7B:** 10 of 10 objects

**Pairs:** 7 in both, 34 missed by Qwen-7B, 4 reversed, 0 with an object Qwen-7B was not given, 2 only Qwen-7B

**Objects: 4/10 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | baby | yes (object 1) | baby | identical | ✓ |
| 1 | baby | yes (object 2) | adult | mismatch | ✗ |
| 2 | adult | yes (object 3) | dog | mismatch | ✗ |
| 3 | child | yes (object 4) | chair | mismatch | ✗ |
| 4 | chair | yes (object 5) | rocking chair | hypernym/hyponym | ✓ |
| 5 | table | yes (object 6) | table | identical | ✓ |
| 6 | sofa | yes (object 7) | couch | synonym | ✓ |
| 7 | adult | yes (object 8) | hand | mismatch | ✗ |
| 8 | sofa | yes (object 9) | person | mismatch | ✗ |
| 9 | adult | yes (object 10) | object | mismatch | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| baby #0 → baby #1 | ✓ | ✗ (baby #1 named wrong) | watch [18.5602-19.2275s]; in front of [10.5522-20.9793s] | near [-] | ✓ Qwen-7B has this pair | ✗ ✗ | ✗ ✗ |
| baby #0 → adult #2 | ✓ | ✗ (adult #2 named wrong) | in front of [0-25.7757s] | near [-] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| baby #0 → sofa #6 | ✓ | ✓ | in front of [12.304-14.1391s] | - | ✗ Qwen-7B missed this pair | - | - |
| baby #0 → adult #9 | ✓ | ✗ (adult #9 named wrong) | watch [0-5.88087s, 10.2602-13.8055s]; in front of [0-5.88087s, 10.2602-13.8055s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| baby #1 → baby #0 | ✓ | ✗ (baby #1 named wrong) | watch [10.5522-13.3467s, 16.5999-17.2672s]; next to [10.5522-14.9733s]; away [12.012-15.015s]; behind [14.014-19.019s] | - | ↔ Qwen-7B has it reversed | - - - - | - - - - |
| baby #1 → adult #2 | ✓ | ✗ (baby #1 named wrong, adult #2 named wrong) | in front of [10.5522-33.742s]; away [32.032-33.742s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| baby #1 → child #3 | ✓ | ✗ (baby #1 named wrong, child #3 named wrong) | away [32.032-35.035s] | near [-] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| baby #1 → chair #4 | ✓ | ✗ (baby #1 named wrong) | away [32.032-35.035s] | near [-] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| baby #1 → table #5 | ✓ | ✗ (baby #1 named wrong) | towards [14.014-17.017s]; away [32.032-35.035s] | near [-] | ✓ Qwen-7B has this pair | ✗ ✗ | ✗ ✗ |
| baby #1 → sofa #6 | ✓ | ✗ (baby #1 named wrong) | in front of [12.304-14.1391s]; towards [12.304-14.1391s] | near [-] | ✓ Qwen-7B has this pair | ✗ ✗ | ✗ ✗ |
| baby #1 → adult #7 | ✓ | ✗ (baby #1 named wrong, adult #7 named wrong) | away [32.032-35.035s] | near [-] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| baby #1 → adult #9 | ✓ | ✗ (baby #1 named wrong, adult #9 named wrong) | watch [31.8235-35.9109s]; in front of [10.5522-13.8055s, 32.032-35.9109s]; away [12.012-13.8055s]; towards [32.032-35.035s] | - | ✗ Qwen-7B missed this pair | - - - - | - - - - |
| adult #2 → baby #0 | ✓ | ✗ (adult #2 named wrong) | watch [0-6.33967s]; behind [0-19.019s]; towards [10.01-13.013s]; away [12.012-15.015s] | - | ↔ Qwen-7B has it reversed | - - - - | - - - - |
| adult #2 → baby #1 | ✓ | ✗ (adult #2 named wrong, baby #1 named wrong) | lift [12.8045-13.9723s, 18.9773-20.1034s, 24.8582-25.4004s, 29.6963-30.8225s]; watch [14.723-27.4024s, 29.029-32.9079s]; towards [10.5522-12.9713s]; behind [12.012-33.742s] | - | ✗ Qwen-7B missed this pair | - - - - | - - - - |
| adult #2 → sofa #6 | ✓ | ✗ (adult #2 named wrong) | in front of [12.304-14.1391s]; away [12.304-14.1391s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| adult #2 → adult #9 | ✓ | ✗ (adult #2 named wrong, adult #9 named wrong) | in front of [0-5.88087s, 10.2602-13.8055s, 32.032-33.742s]; towards [12.012-13.8055s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| child #3 → chair #4 | ✓ | ✗ (child #3 named wrong) | lean on [28.1531-35.9109s]; above [28.1531-35.8692s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| child #3 → table #5 | ✓ | ✗ (child #3 named wrong) | next to [28.1114-35.8692s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #3 → adult #7 | ✓ | ✗ (child #3 named wrong, adult #7 named wrong) | watch [32.9913-33.325s, 35.6189-35.9109s]; next to [31.1978-35.8692s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| child #3 → sofa #8 | ✓ | ✗ (child #3 named wrong, sofa #8 named wrong) | next to [34.034-35.9109s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #3 → adult #9 | ✓ | ✗ (child #3 named wrong, adult #9 named wrong) | in front of [32.032-35.9109s] | - | ✗ Qwen-7B missed this pair | - | - |
| chair #4 → child #3 | ✓ | ✗ (child #3 named wrong) | beneath [28.1531-35.8692s] | - | ✗ Qwen-7B missed this pair | - | - |
| chair #4 → adult #7 | ✓ | ✗ (adult #7 named wrong) | next to [31.1978-35.8692s] | - | ✗ Qwen-7B missed this pair | - | - |
| chair #4 → sofa #8 | ✓ | ✗ (sofa #8 named wrong) | next to [34.034-35.9109s] | - | ✗ Qwen-7B missed this pair | - | - |
| chair #4 → adult #9 | ✓ | ✗ (adult #9 named wrong) | in front of [32.032-35.9109s] | - | ✗ Qwen-7B missed this pair | - | - |
| table #5 → baby #1 | ✓ | ✗ (baby #1 named wrong) | behind [10.5522-12.2205s] | - | ↔ Qwen-7B has it reversed | - | - |
| table #5 → child #3 | ✓ | ✗ (child #3 named wrong) | in front of [30.03-35.9109s] | - | ✗ Qwen-7B missed this pair | - | - |
| table #5 → chair #4 | ✓ | ✓ | in front of [28.1531-35.8692s] | - | ✗ Qwen-7B missed this pair | - | - |
| table #5 → adult #7 | ✓ | ✗ (adult #7 named wrong) | in front of [31.1978-35.8692s] | - | ✗ Qwen-7B missed this pair | - | - |
| table #5 → sofa #8 | ✓ | ✗ (sofa #8 named wrong) | in front of [34.034-35.9109s] | - | ✗ Qwen-7B missed this pair | - | - |
| table #5 → adult #9 | ✓ | ✗ (adult #9 named wrong) | in front of [10.2602-12.2205s, 32.032-35.9109s] | - | ✗ Qwen-7B missed this pair | - | - |
| sofa #6 → baby #0 | ✓ | ✓ | behind [12.304-14.1391s] | - | ✗ Qwen-7B missed this pair | - | - |
| sofa #6 → baby #1 | ✓ | ✗ (baby #1 named wrong) | behind [12.304-14.1391s] | - | ↔ Qwen-7B has it reversed | - | - |
| sofa #6 → adult #2 | ✓ | ✗ (adult #2 named wrong) | behind [12.304-14.1391s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #7 → child #3 | ✓ | ✗ (adult #7 named wrong, child #3 named wrong) | next to [31.1978-35.8692s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #7 → chair #4 | ✓ | ✗ (adult #7 named wrong) | next to [31.1978-35.8692s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #7 → sofa #8 | ✓ | ✗ (adult #7 named wrong, sofa #8 named wrong) | lean on [33.7837-35.9109s]; above [34.034-35.9109s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| sofa #8 → child #3 | ✓ | ✗ (sofa #8 named wrong, child #3 named wrong) | next to [34.034-35.9109s] | - | ✗ Qwen-7B missed this pair | - | - |
| sofa #8 → chair #4 | ✓ | ✗ (sofa #8 named wrong) | next to [34.034-35.9109s] | - | ✗ Qwen-7B missed this pair | - | - |
| sofa #8 → adult #7 | ✓ | ✗ (sofa #8 named wrong, adult #7 named wrong) | beneath [34.034-35.9109s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #9 → baby #0 | ✓ | ✗ (adult #9 named wrong) | in front of [0-5.88087s, 10.2602-13.8055s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #9 → baby #1 | ✓ | ✗ (adult #9 named wrong, baby #1 named wrong) | watch [35.2852-35.9109s]; hold hand of [10.5522-12.7627s]; next to [10.5522-13.8055s]; in front of [32.032-35.9109s] | - | ✗ Qwen-7B missed this pair | - - - - | - - - - |
| adult #9 → adult #2 | ✓ | ✗ (adult #9 named wrong, adult #2 named wrong) | in front of [0-5.88087s, 10.2602-13.8055s, 32.032-33.742s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #9 → child #3 | ✓ | ✗ (adult #9 named wrong, child #3 named wrong) | behind [32.032-35.9109s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #9 → chair #4 | ✓ | ✗ (adult #9 named wrong) | behind [32.032-35.9109s] | - | ✗ Qwen-7B missed this pair | - | - |
| baby #1 → sofa #8 | ✓ | ✗ (baby #1 named wrong, sofa #8 named wrong) | - | near [-] | + only Qwen-7B | - | - |
| adult #7 → adult #9 | ✓ | ✗ (adult #7 named wrong, adult #9 named wrong) | - | holding [-] | + only Qwen-7B | - | - |


## 4925211209

32.0 s video; humans: 2 objects, 3 relations on 2 pairs; Qwen-7B: 1 relations on 1 pairs.

**Masks given to Qwen-7B:** 2 of 2 objects

**Pairs:** 1 in both, 0 missed by Qwen-7B, 1 reversed, 0 with an object Qwen-7B was not given, 0 only Qwen-7B

**Objects: 1/2 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | bus/truck | yes (object 1) | bucket | mismatch | ✗ |
| 1 | adult | yes (object 2) | worker | hypernym/hyponym | ✓ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| bus/truck #0 → adult #1 | ✓ | ✗ (bus/truck #0 named wrong) | inside [14-17s] | elevating [0-33s] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| adult #1 → bus/truck #0 | ✓ | ✗ (bus/truck #0 named wrong) | lean on [0-3.875s]; inside [0-17.75s] | - | ↔ Qwen-7B has it reversed | - - | - - |


## 5421648216

43.04 s video; humans: 3 objects, 15 relations on 6 pairs; Qwen-7B: 6 relations on 6 pairs.

**Masks given to Qwen-7B:** 3 of 3 objects

**Pairs:** 6 in both, 0 missed by Qwen-7B, 0 reversed, 0 with an object Qwen-7B was not given, 0 only Qwen-7B

**Objects: 3/3 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | sheep/goat | yes (object 1) | sheep1 | hypernym/hyponym | ✓ |
| 1 | sheep/goat | yes (object 2) | sheep2 | identical | ✓ |
| 2 | sheep/goat | yes (object 3) | sheep3 | identical | ✓ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| sheep/goat #0 → sheep/goat #1 | ✓ | ✓ | behind [0-3.003s, 8.008-10.2436s, 20.02-25.025s, 28.028-33.033s]; towards [0-3.003s]; in front of [2.002-9.009s]; next to [24.024-29.029s, 32.032-43.043s] | behind [0-45.0419s] | ✓ Qwen-7B has this pair | ✗ ✗ ✗ ✗ | ✗ ✗ ✗ ✗ |
| sheep/goat #0 → sheep/goat #2 | ✓ | ✓ | watch [23.4234-23.9239s]; towards [0-3.003s]; in front of [4.004-5.63897s, 20.02-23.9239s, 38.038-43.043s] | behind [0-45.0419s] | ✓ Qwen-7B has this pair | ✗ ✗ ✗ | ✗ ✗ ✗ |
| sheep/goat #1 → sheep/goat #0 | ✓ | ✓ | in front of [0-3.003s, 24.024-37.037s]; next to [2.002-10.2436s, 20.02-25.025s, 36.036-43.043s] | behind [0-45.0419s] | ✓ Qwen-7B has this pair | ✗ ✗ | ✗ ✗ |
| sheep/goat #1 → sheep/goat #2 | ✓ | ✓ | watch [4.23757-5.47213s, 34.8682-39.8064s]; in front of [4.004-5.63897s, 20.02-23.9239s, 40.04-43.043s] | behind [0-45.0419s] | ✓ Qwen-7B has this pair | ✗ ✗ | ✗ ✗ |
| sheep/goat #2 → sheep/goat #0 | ✓ | ✓ | watch [3.8038-5.63897s, 21.4881-23.9239s, 38.8388-41.5081s]; in front of [0-5.63897s, 19.3527-23.9239s, 34.8682-43.0096s] | behind [0-45.0419s] | ✓ Qwen-7B has this pair | ✗ ✗ | ✗ ✗ |
| sheep/goat #2 → sheep/goat #1 | ✓ | ✓ | in front of [0-5.63897s, 34.8682-43.0096s]; behind [20.02-23.9239s] | behind [0-45.0419s] | ✓ Qwen-7B has this pair | ✗ ✗ | ✗ ✗ |


## 5658916668

22.02 s video; humans: 9 objects, 34 relations on 21 pairs; Qwen-7B: 6 relations on 6 pairs.

**Masks given to Qwen-7B:** 9 of 9 objects

**Pairs:** 3 in both, 15 missed by Qwen-7B, 3 reversed, 0 with an object Qwen-7B was not given, 3 only Qwen-7B

**Objects: 9/9 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | adult | yes (object 1) | people | hypernym/hyponym | ✓ |
| 1 | adult | yes (object 2) | person with red snowboard | hypernym/hyponym | ✓ |
| 2 | adult | yes (object 3) | people | hypernym/hyponym | ✓ |
| 3 | adult | yes (object 4) | people | hypernym/hyponym | ✓ |
| 4 | snowboard | yes (object 5) | red snowboard | hypernym/hyponym | ✓ |
| 5 | adult | yes (object 6) | person with yellow snowboard | hypernym/hyponym | ✓ |
| 6 | adult | yes (object 7) | person falling | hypernym/hyponym | ✓ |
| 7 | snowboard | yes (object 8) | yellow snowboard | hypernym/hyponym | ✓ |
| 8 | adult | yes (object 9) | man standing | hypernym/hyponym | ✓ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| adult #0 → adult #1 | ✓ | ✓ | next to [0.6006-8.04137s]; away [0.6006-4.97163s] | near [0-9.00818s] | ✓ Qwen-7B has this pair | ✓ ✗ | ✓ ✗ |
| adult #0 → adult #2 | ✓ | ✓ | next to [0-8.04137s]; towards [0-3.003s] | near [0-9.00818s] | ✓ Qwen-7B has this pair | ✓ ✗ | ✓ ✗ |
| adult #0 → adult #3 | ✓ | ✓ | next to [0-8.04137s] | near [0-9.00818s] | ✓ Qwen-7B has this pair | ✓ | ✓ |
| adult #1 → adult #0 | ✓ | ✓ | next to [0.6006-8.04137s] | - | ↔ Qwen-7B has it reversed | - | - |
| adult #1 → adult #2 | ✓ | ✓ | next to [0.6006-8.97563s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #2 → adult #0 | ✓ | ✓ | next to [0-8.04137s]; towards [0-5.005s] | - | ↔ Qwen-7B has it reversed | - - | - - |
| adult #2 → adult #1 | ✓ | ✓ | next to [0.6006-8.97563s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #2 → adult #3 | ✓ | ✓ | next to [0-8.97563s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #2 → adult #6 | ✓ | ✓ | away [4.004-9.54287s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #3 → adult #0 | ✓ | ✓ | next to [0-8.04137s]; towards [0-5.005s] | - | ↔ Qwen-7B has it reversed | - - | - - |
| adult #3 → adult #2 | ✓ | ✓ | next to [0-8.97563s] | - | ✗ Qwen-7B missed this pair | - | - |
| snowboard #4 → adult #5 | ✓ | ✓ | next to [8.47513-10.3437s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #5 → snowboard #4 | ✓ | ✓ | next to [8.47513-10.3437s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #5 → adult #6 | ✓ | ✓ | next to [8.3083-9.87653s]; towards [8.3083-9.87653s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| adult #6 → adult #0 | ✓ | ✓ | towards [0-5.005s]; away [4.004-8.04137s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| adult #6 → adult #1 | ✓ | ✓ | away [4.004-9.009s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #6 → adult #2 | ✓ | ✓ | away [4.004-9.54287s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #6 → adult #3 | ✓ | ✓ | next to [0-8.97563s]; away [4.004-8.97563s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| adult #6 → adult #5 | ✓ | ✓ | next to [8.3083-9.87653s]; away [8.3083-9.87653s] | - | ✗ Qwen-7B missed this pair | - - | - - |
| adult #6 → snowboard #7 | ✓ | ✓ | ride [9.04237-9.87653s, 12.7127-13.3133s]; above [12.7127-14.9816s]; away [12.7127-14.9816s]; next to [14.014-21.4214s] | - | ✗ Qwen-7B missed this pair | - - - - | - - - - |
| snowboard #7 → adult #6 | ✓ | ✓ | beneath [12.7127-14.9816s]; away [12.7127-14.9816s]; next to [14.014-21.4214s] | - | ✗ Qwen-7B missed this pair | - - - | - - - |
| adult #1 → snowboard #4 | ✓ | ✓ | - | holding [0-9.00818s] | + only Qwen-7B | - | - |
| adult #5 → snowboard #7 | ✓ | ✓ | - | standing near [8.00727-13.0118s, 16.0145-25.0227s] | + only Qwen-7B | - | - |
| adult #6 → adult #8 | ✓ | ✓ | - | falling [12.0109-17.0155s] | + only Qwen-7B | - | - |


## 8563398032

81.6 s video; humans: 6 objects, 30 relations on 25 pairs; Qwen-7B: 12 relations on 10 pairs.

**Masks given to Qwen-7B:** 6 of 6 objects

**Pairs:** 9 in both, 10 missed by Qwen-7B, 6 reversed, 0 with an object Qwen-7B was not given, 1 only Qwen-7B

**Objects: 2/6 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | adult | yes (object 1) | man | hypernym/hyponym | ✓ |
| 1 | adult | yes (object 2) | man | hypernym/hyponym | ✓ |
| 2 | cup | yes (object 3) | table | mismatch | ✗ |
| 3 | table | yes (object 4) | chair | mismatch | ✗ |
| 4 | chair | yes (object 5) | cup | mismatch | ✗ |
| 5 | adult | yes (object 6) | leg | mismatch | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| adult #0 → adult #1 | ✓ | ✓ | speak to [54.44-60.24s]; watch [55.36-63.72s]; next to [0-59s, 60-81.6s]; in front of [58-61s] | speaking to [0-84.5854s]; across from [0-84.5854s] | ✓ Qwen-7B has this pair | ✗ ✗ ✗ ✗ | ✗ ✗ ✗ ✗ |
| adult #0 → cup #2 | ✓ | ✗ (cup #2 named wrong) | next to [0-81.6s] | sitting at [0-84.5854s] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| adult #0 → table #3 | ✓ | ✗ (table #3 named wrong) | next to [0-81.6s] | next to [0-84.5854s] | ✓ Qwen-7B has this pair | ✓ | ✗ |
| adult #0 → chair #4 | ✓ | ✗ (chair #4 named wrong) | in front of [0-81.6s] | holding [0-84.5854s] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| adult #0 → adult #5 | ✓ | ✗ (adult #5 named wrong) | in front of [1.36-81.56s] | gesturing with [0-84.5854s] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| adult #1 → adult #0 | ✓ | ✓ | watch [55.68-56.04s, 57.76-58.12s]; next to [0-81.6s] | speaking to [0-84.5854s]; across from [0-84.5854s] | ✓ Qwen-7B has this pair | ✗ ✗ | ✗ ✗ |
| adult #1 → table #3 | ✓ | ✗ (table #3 named wrong) | lean on [0-1.92s, 3.12-32.12s, 39.88-54.36s, 62.92-63.72s, 65.4-81.6s]; next to [0-81.6s] | next to [0-84.5854s] | ✓ Qwen-7B has this pair | ✗ ✓ | ✗ ✗ |
| adult #1 → chair #4 | ✓ | ✗ (chair #4 named wrong) | in front of [0-81.6s] | holding [0-84.5854s] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| adult #1 → adult #5 | ✓ | ✗ (adult #5 named wrong) | in front of [1.36-81.56s] | gesturing with [0-84.5854s] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| cup #2 → adult #0 | ✓ | ✗ (cup #2 named wrong) | in front of [0-81.6s] | - | ↔ Qwen-7B has it reversed | - | - |
| cup #2 → adult #1 | ✓ | ✗ (cup #2 named wrong) | in front of [58-61s] | - | ↔ Qwen-7B has it reversed | - | - |
| cup #2 → table #3 | ✓ | ✗ (cup #2 named wrong, table #3 named wrong) | above [0-81.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| cup #2 → chair #4 | ✓ | ✗ (cup #2 named wrong, chair #4 named wrong) | in front of [0-81.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| cup #2 → adult #5 | ✓ | ✗ (cup #2 named wrong, adult #5 named wrong) | in front of [1.36-81.56s] | - | ✗ Qwen-7B missed this pair | - | - |
| table #3 → adult #0 | ✓ | ✗ (table #3 named wrong) | in front of [0-81.6s] | - | ↔ Qwen-7B has it reversed | - | - |
| table #3 → adult #1 | ✓ | ✗ (table #3 named wrong) | in front of [0-81.6s] | - | ↔ Qwen-7B has it reversed | - | - |
| table #3 → cup #2 | ✓ | ✗ (table #3 named wrong, cup #2 named wrong) | beneath [0-81.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| table #3 → chair #4 | ✓ | ✗ (table #3 named wrong, chair #4 named wrong) | in front of [0-81.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| table #3 → adult #5 | ✓ | ✗ (table #3 named wrong, adult #5 named wrong) | in front of [1.36-81.56s] | - | ✗ Qwen-7B missed this pair | - | - |
| chair #4 → table #3 | ✓ | ✗ (chair #4 named wrong, table #3 named wrong) | next to [0-81.6s] | - | ✗ Qwen-7B missed this pair | - | - |
| chair #4 → adult #5 | ✓ | ✗ (chair #4 named wrong, adult #5 named wrong) | next to [1.36-81.56s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #5 → adult #0 | ✓ | ✗ (adult #5 named wrong) | in front of [1.36-81.56s] | - | ↔ Qwen-7B has it reversed | - | - |
| adult #5 → adult #1 | ✓ | ✗ (adult #5 named wrong) | in front of [1.36-81.56s] | - | ↔ Qwen-7B has it reversed | - | - |
| adult #5 → table #3 | ✓ | ✗ (adult #5 named wrong, table #3 named wrong) | next to [1.36-81.56s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #5 → chair #4 | ✓ | ✗ (adult #5 named wrong, chair #4 named wrong) | next to [1.36-26.96s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #1 → cup #2 | ✓ | ✗ (cup #2 named wrong) | - | sitting at [0-84.5854s] | + only Qwen-7B | - | - |


## 9217939684

69.17 s video; humans: 6 objects, 48 relations on 22 pairs; Qwen-7B: 6 relations on 6 pairs.

**Masks given to Qwen-7B:** 6 of 6 objects

**Pairs:** 5 in both, 12 missed by Qwen-7B, 5 reversed, 0 with an object Qwen-7B was not given, 1 only Qwen-7B

**Objects: 2/6 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | baby | yes (object 1) | child | hypernym/hyponym | ✓ |
| 1 | adult | yes (object 2) | woman | hypernym/hyponym | ✓ |
| 2 | adult | yes (object 3) | child2 | mismatch | ✗ |
| 3 | child | yes (object 4) | teddy bear | mismatch | ✗ |
| 4 | toy | yes (object 5) | pillow | mismatch | ✗ |
| 5 | toy | yes (object 6) | bed | mismatch | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| baby #0 → adult #1 | ✓ | ✓ | watch [14.0833-14.6667s, 38.875-40.0417s]; in front of [14.0833-27.625s, 38.625-44.9583s, 62.7917-68.9583s]; towards [38.625-40.9583s] | - | ↔ Qwen-7B has it reversed | - - - | - - - |
| baby #0 → adult #2 | ✓ | ✗ (adult #2 named wrong) | watch [0-1.16667s]; hug [0.916667-1.875s]; in front of [0-12s, 30.2917-36.4167s, 58-61s]; next to [53.3333-58.9583s] | playing with [0-73.1799s] | ✓ Qwen-7B has this pair | ✗ ✗ ✗ ✗ | ✗ ✗ ✗ ✗ |
| baby #0 → child #3 | ✓ | ✗ (child #3 named wrong) | watch [61.1667-62.9167s]; in front of [12.375-29.9583s, 36.6667-52.9583s, 61.1667-68.9583s]; away [50-52.9583s]; towards [61.1667-62.9583s] | - | ✗ Qwen-7B missed this pair | - - - - | - - - - |
| baby #0 → toy #4 | ✓ | ✗ (toy #4 named wrong) | next to [0-8.45833s, 30-37.7917s, 46.375-50.5417s, 52.8333-61.875s] | near [0-73.1799s] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| baby #0 → toy #5 | ✓ | ✗ (toy #5 named wrong) | next to [12.125-30.4167s, 36-53s, 61.0417-68.9583s]; away [48-51s]; towards [61.0417-62.9583s] | - | ✗ Qwen-7B missed this pair | - - - | - - - |
| adult #1 → baby #0 | ✓ | ✓ | watch [14.0833-16.9583s, 20.3333-27.625s, 38.875-45.0833s, 62.7917-66.6667s, 67.3333-69.1667s]; hold [16.9167-20.0833s, 22.25-24.1667s]; in front of [14.0833-16.9583s, 38.625-42.9583s, 64-69s]; behind [16-27.625s, 42-45s]; next to [62.7917-64.9583s] | watching [0-73.1799s] | ✓ Qwen-7B has this pair | ✗ ✗ ✗ ✗ ✗ | ✗ ✗ ✗ ✗ ✗ |
| adult #1 → child #3 | ✓ | ✗ (child #3 named wrong) | next to [14.0833-27.625s, 38.625-44.9583s, 62.7917-68.9583s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #1 → toy #5 | ✓ | ✗ (toy #5 named wrong) | next to [14.0833-27.625s, 38.625-44.9583s, 62.7917-68.9583s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #2 → baby #0 | ✓ | ✗ (adult #2 named wrong) | watch [0-1.04167s, 2.20833-11.4583s, 31-35.8333s, 55.125-58s]; hug [1.375-2.70833s]; hold [2.66667-8.75s]; lift [3.91667-4.66667s]; in front of [0-5s]; behind [4-12s, 34-36.4167s, 53.3333-58.9583s]; next to [30.2917-34.9583s, 58-61s] | - | ↔ Qwen-7B has it reversed | - - - - - - - | - - - - - - - |
| adult #2 → toy #4 | ✓ | ✗ (adult #2 named wrong, toy #4 named wrong) | next to [0-8.45833s, 30.2917-36.4167s, 53.3333-60.9583s] | near [0-73.1799s] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| child #3 → baby #0 | ✓ | ✗ (child #3 named wrong) | watch [12.5417-14.7083s, 18.0417-19.3333s, 20.375-29.9583s, 36.6667-37.4583s, 39.125-48s, 50-52.7083s, 61.4167-68.875s]; in front of [12.375-14.9583s, 36.6667-38.9583s, 61.1667-64.9583s]; next to [14-17s, 18-29.9583s, 38-47s, 64-69s]; behind [16-19s, 46-52.9583s] | - | ✗ Qwen-7B missed this pair | - - - - | - - - - |
| child #3 → adult #1 | ✓ | ✗ (child #3 named wrong) | next to [14.0833-27.625s, 38.625-44.9583s, 62.7917-68.9583s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #3 → toy #4 | ✓ | ✗ (child #3 named wrong, toy #4 named wrong) | next to [46.375-50.5417s] | - | ✗ Qwen-7B missed this pair | - | - |
| child #3 → toy #5 | ✓ | ✗ (child #3 named wrong, toy #5 named wrong) | next to [12.375-29.9583s, 36.6667-52.9583s, 61.1667-68.9583s] | on [0-73.1799s] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| toy #4 → baby #0 | ✓ | ✗ (toy #4 named wrong) | next to [0-8.45833s, 36-37.7917s, 46.375-50.5417s, 60-61.875s]; behind [30-37s, 52.8333-60.9583s] | - | ↔ Qwen-7B has it reversed | - - | - - |
| toy #4 → adult #2 | ✓ | ✗ (toy #4 named wrong, adult #2 named wrong) | next to [0-8.45833s, 30.2917-36.4167s, 53.3333-60.9583s] | - | ↔ Qwen-7B has it reversed | - | - |
| toy #4 → child #3 | ✓ | ✗ (toy #4 named wrong, child #3 named wrong) | next to [46.375-50.5417s] | - | ✗ Qwen-7B missed this pair | - | - |
| toy #4 → toy #5 | ✓ | ✗ (toy #4 named wrong, toy #5 named wrong) | next to [36-37.7917s, 46.375-50.5417s] | - | ✗ Qwen-7B missed this pair | - | - |
| toy #5 → baby #0 | ✓ | ✗ (toy #5 named wrong) | next to [12.125-20.9583s, 22-30.4167s, 36-49s, 64-69s]; behind [20-23s, 48-53s]; in front of [61.0417-64.9583s] | - | ✗ Qwen-7B missed this pair | - - - | - - - |
| toy #5 → adult #1 | ✓ | ✗ (toy #5 named wrong) | next to [14.0833-27.625s, 38.625-44.9583s, 62.7917-68.9583s] | - | ✗ Qwen-7B missed this pair | - | - |
| toy #5 → child #3 | ✓ | ✗ (toy #5 named wrong, child #3 named wrong) | behind [12.375-29.9583s, 36.6667-52.9583s, 61.1667-68.9583s] | - | ↔ Qwen-7B has it reversed | - | - |
| toy #5 → toy #4 | ✓ | ✗ (toy #5 named wrong, toy #4 named wrong) | next to [36-37.7917s, 46.375-50.5417s] | - | ✗ Qwen-7B missed this pair | - | - |
| adult #2 → child #3 | ✓ | ✗ (adult #2 named wrong, child #3 named wrong) | - | playing with [0-73.1799s] | + only Qwen-7B | - | - |

