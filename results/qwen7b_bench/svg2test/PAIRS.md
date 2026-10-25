# svg2test: which object pairs Qwen-7B talks about (10 random videos, seed 0)

The same 10 videos as TRASER's page ([`results/traser_bench/svg2test/PAIRS.md`](../../traser_bench/svg2test/PAIRS.md)), with the answers of Qwen2.5-VL-7B-Instruct (not fine-tuned) in TRASER's pipeline (`../README.md`).

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

**Total over these videos:** 285 human pairs, 166 Qwen-7B pairs; 29 in both, 220 missed, 24 reversed, 12 with an object not given, 137 only Qwen-7B.

| video | source | masks given to Qwen-7B | objects right | relations right | triplets right | human pairs | Qwen-7B pairs | pairs in both | missed by Qwen-7B | reversed | object not given | only Qwen-7B |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [1190_UmpN6eLjN8w](#1190_umpn6eljn8w) | vipseg | 18/18 | 0/18 | 0/44 | 0/44 | 40 | 6 | 5 | 30 | 5 | 0 | 1 |
| [339_j2gELsuQ3Cg](#339_j2gelsuq3cg) | vipseg | 14/14 | 4/14 | 0/20 | 0/20 | 17 | 3 | 1 | 16 | 0 | 0 | 2 |
| [465_nbJ_SLWUDxk](#465_nbj_slwudxk) | vipseg | 39/39 | 0/39 | 0/24 | 0/24 | 21 | 39 | 6 | 10 | 5 | 0 | 33 |
| [700_zkhPzSZcRtQ](#700_zkhpzszcrtq) | vipseg | 24/24 | 1/24 | 0/41 | 0/41 | 39 | 3 | 2 | 37 | 0 | 0 | 1 |
| [722__ajUvCkhVcI](#722__ajuvckhvci) | vipseg | 18/18 | 2/18 | 1/39 | 1/39 | 32 | 3 | 2 | 30 | 0 | 0 | 1 |
| [744_1X6KvqPjk6I](#744_1x6kvqpjk6i) | vipseg | 32/32 | 0/32 | 0/26 | 0/26 | 23 | 0 | 0 | 23 | 0 | 0 | 0 |
| [888_BS3hab7EtAg](#888_bs3hab7etag) | vipseg | 26/26 | 3/26 | 7/39 | 2/39 | 36 | 68 | 8 | 16 | 12 | 0 | 60 |
| [914_f4HgijyAEYs](#914_f4hgijyaeys) | vipseg | 19/19 | 2/19 | 2/21 | 1/21 | 19 | 4 | 3 | 15 | 1 | 0 | 1 |
| [976_U19VojbI0h4](#976_u19vojbi0h4) | vipseg | 40/65 | 12/65 | 0/36 | 0/36 | 32 | 40 | 2 | 17 | 1 | 12 | 38 |
| [sav_053005](#sav_053005) | sav | 29/29 | 7/29 | 0/29 | 0/29 | 26 | 0 | 0 | 26 | 0 | 0 | 0 |

## 1190_UmpN6eLjN8w

10.17 s video; humans: 18 objects, 44 relations on 40 pairs; Qwen-7B: 6 relations on 6 pairs.

**Masks given to Qwen-7B:** 18 of 18 objects

**Pairs:** 5 in both, 30 missed by Qwen-7B, 5 reversed, 0 with an object Qwen-7B was not given, 1 only Qwen-7B

**Objects: 0/18 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | plane | yes (object 1) | - (Qwen-7B wrote no label) | - | ✗ |
| 1 | person | yes (object 2) | - (Qwen-7B wrote no label) | - | ✗ |
| 2 | person | yes (object 3) | - (Qwen-7B wrote no label) | - | ✗ |
| 3 | ocean | yes (object 4) | - (Qwen-7B wrote no label) | - | ✗ |
| 4 | person | yes (object 5) | - (Qwen-7B wrote no label) | - | ✗ |
| 5 | sky | yes (object 6) | - (Qwen-7B wrote no label) | - | ✗ |
| 6 | hair | yes (object 7) | - (Qwen-7B wrote no label) | - | ✗ |
| 7 | face | yes (object 8) | - (Qwen-7B wrote no label) | - | ✗ |
| 8 | cap | yes (object 9) | - (Qwen-7B wrote no label) | - | ✗ |
| 9 | neck | yes (object 10) | - (Qwen-7B wrote no label) | - | ✗ |
| 10 | hair | yes (object 11) | - (Qwen-7B wrote no label) | - | ✗ |
| 11 | shirt | yes (object 12) | - (Qwen-7B wrote no label) | - | ✗ |
| 12 | wing | yes (object 13) | - (Qwen-7B wrote no label) | - | ✗ |
| 13 | wing | yes (object 14) | - (Qwen-7B wrote no label) | - | ✗ |
| 14 | tyres | yes (object 15) | - (Qwen-7B wrote no label) | - | ✗ |
| 15 | tyres | yes (object 16) | - (Qwen-7B wrote no label) | - | ✗ |
| 16 | nose | yes (object 17) | - (Qwen-7B wrote no label) | - | ✗ |
| 17 | hair | yes (object 18) | - (Qwen-7B wrote no label) | - | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| plane #0 → person #1 | ✓ | ✗ (plane #0 named wrong, person #1 named wrong) | above [0-11]; approaches [0-11] | - | ✗ Qwen-7B missed this pair | - - | - - |
| plane #0 → person #2 | ✓ | ✗ (plane #0 named wrong, person #2 named wrong) | approaches [0-3, 6-8]; above [0-3, 6-8] | - | ✗ Qwen-7B missed this pair | - - | - - |
| plane #0 → ocean #3 | ✓ | ✗ (plane #0 named wrong, ocean #3 named wrong) | above [0-11] | - | ✗ Qwen-7B missed this pair | - | - |
| plane #0 → person #4 | ✓ | ✗ (plane #0 named wrong, person #4 named wrong) | approaches [3-11]; above [2.5-11] | - | ✗ Qwen-7B missed this pair | - - | - - |
| plane #0 → sky #5 | ✓ | ✗ (plane #0 named wrong, sky #5 named wrong) | moves across [0-11]; in front of [0-11] | - | ✗ Qwen-7B missed this pair | - - | - - |
| plane #0 → wing #12 | ✓ | ✗ (plane #0 named wrong, wing #12 named wrong) | has [0-11] | above [0-13] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| plane #0 → wing #13 | ✓ | ✗ (plane #0 named wrong, wing #13 named wrong) | has [0-11] | above [0-13] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| plane #0 → tyres #14 | ✓ | ✗ (plane #0 named wrong, tyres #14 named wrong) | has [0-11] | above [0-13] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| plane #0 → tyres #15 | ✓ | ✗ (plane #0 named wrong, tyres #15 named wrong) | has [0-11] | above [0-13] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| plane #0 → nose #16 | ✓ | ✗ (plane #0 named wrong, nose #16 named wrong) | has [0-11] | above [0-13] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| person #1 → plane #0 | ✓ | ✗ (person #1 named wrong, plane #0 named wrong) | looking at [2.5-5, 6.5-10] | - | ✗ Qwen-7B missed this pair | - | - |
| person #1 → ocean #3 | ✓ | ✗ (person #1 named wrong, ocean #3 named wrong) | in front of [0-11] | - | ✗ Qwen-7B missed this pair | - | - |
| person #1 → sky #5 | ✓ | ✗ (person #1 named wrong, sky #5 named wrong) | in front of [0-11] | - | ✗ Qwen-7B missed this pair | - | - |
| person #1 → hair #6 | ✓ | ✗ (person #1 named wrong, hair #6 named wrong) | has [0-11] | - | ✗ Qwen-7B missed this pair | - | - |
| person #1 → face #7 | ✓ | ✗ (person #1 named wrong, face #7 named wrong) | has [0-11] | - | ✗ Qwen-7B missed this pair | - | - |
| person #2 → plane #0 | ✓ | ✗ (person #2 named wrong, plane #0 named wrong) | looking at [0-3, 6-8] | - | ✗ Qwen-7B missed this pair | - | - |
| person #2 → ocean #3 | ✓ | ✗ (person #2 named wrong, ocean #3 named wrong) | in front of [0-3, 6-8] | - | ✗ Qwen-7B missed this pair | - | - |
| person #2 → sky #5 | ✓ | ✗ (person #2 named wrong, sky #5 named wrong) | in front of [0-3, 6-8] | - | ✗ Qwen-7B missed this pair | - | - |
| person #2 → cap #8 | ✓ | ✗ (person #2 named wrong, cap #8 named wrong) | wears [0-2, 6-8] | - | ✗ Qwen-7B missed this pair | - | - |
| person #2 → shirt #11 | ✓ | ✗ (person #2 named wrong, shirt #11 named wrong) | wears [0-3, 6-8] | - | ✗ Qwen-7B missed this pair | - | - |
| ocean #3 → sky #5 | ✓ | ✗ (ocean #3 named wrong, sky #5 named wrong) | in front of [0-11] | - | ✗ Qwen-7B missed this pair | - | - |
| person #4 → plane #0 | ✓ | ✗ (person #4 named wrong, plane #0 named wrong) | looking at [3-11] | - | ✗ Qwen-7B missed this pair | - | - |
| person #4 → ocean #3 | ✓ | ✗ (person #4 named wrong, ocean #3 named wrong) | in front of [3-11] | - | ✗ Qwen-7B missed this pair | - | - |
| person #4 → sky #5 | ✓ | ✗ (person #4 named wrong, sky #5 named wrong) | in front of [3-11] | - | ✗ Qwen-7B missed this pair | - | - |
| sky #5 → ocean #3 | ✓ | ✗ (sky #5 named wrong, ocean #3 named wrong) | above [0-11] | - | ✗ Qwen-7B missed this pair | - | - |
| hair #6 → person #1 | ✓ | ✗ (hair #6 named wrong, person #1 named wrong) | on [0-11] | - | ✗ Qwen-7B missed this pair | - | - |
| hair #6 → face #7 | ✓ | ✗ (hair #6 named wrong, face #7 named wrong) | above [0-11] | - | ✗ Qwen-7B missed this pair | - | - |
| face #7 → person #1 | ✓ | ✗ (face #7 named wrong, person #1 named wrong) | on [0-11] | - | ✗ Qwen-7B missed this pair | - | - |
| cap #8 → person #2 | ✓ | ✗ (cap #8 named wrong, person #2 named wrong) | on [0-2, 6-7] | - | ✗ Qwen-7B missed this pair | - | - |
| neck #9 → person #2 | ✓ | ✗ (neck #9 named wrong, person #2 named wrong) | on [0-2, 6-8] | - | ✗ Qwen-7B missed this pair | - | - |
| hair #10 → person #2 | ✓ | ✗ (hair #10 named wrong, person #2 named wrong) | on [0-2.5, 6-8] | - | ✗ Qwen-7B missed this pair | - | - |
| shirt #11 → person #2 | ✓ | ✗ (shirt #11 named wrong, person #2 named wrong) | on [0-2, 6-7] | - | ✗ Qwen-7B missed this pair | - | - |
| wing #12 → plane #0 | ✓ | ✗ (wing #12 named wrong, plane #0 named wrong) | on [0-11] | - | ↔ Qwen-7B has it reversed | - | - |
| wing #13 → plane #0 | ✓ | ✗ (wing #13 named wrong, plane #0 named wrong) | on [0-11] | - | ↔ Qwen-7B has it reversed | - | - |
| tyres #14 → plane #0 | ✓ | ✗ (tyres #14 named wrong, plane #0 named wrong) | on [0-11] | - | ↔ Qwen-7B has it reversed | - | - |
| tyres #14 → wing #12 | ✓ | ✗ (tyres #14 named wrong, wing #12 named wrong) | below [0-11] | - | ✗ Qwen-7B missed this pair | - | - |
| tyres #15 → plane #0 | ✓ | ✗ (tyres #15 named wrong, plane #0 named wrong) | on [0-11] | - | ↔ Qwen-7B has it reversed | - | - |
| tyres #15 → wing #12 | ✓ | ✗ (tyres #15 named wrong, wing #12 named wrong) | below [0-11] | - | ✗ Qwen-7B missed this pair | - | - |
| nose #16 → plane #0 | ✓ | ✗ (nose #16 named wrong, plane #0 named wrong) | on [0-11] | - | ↔ Qwen-7B has it reversed | - | - |
| hair #17 → person #4 | ✓ | ✗ (hair #17 named wrong, person #4 named wrong) | on [3-11] | - | ✗ Qwen-7B missed this pair | - | - |
| plane #0 → hair #17 | ✓ | ✗ (plane #0 named wrong, hair #17 named wrong) | - | above [0-13] | + only Qwen-7B | - | - |


## 339_j2gELsuQ3Cg

5.0 s video; humans: 14 objects, 20 relations on 17 pairs; Qwen-7B: 3 relations on 3 pairs.

**Masks given to Qwen-7B:** 14 of 14 objects

**Pairs:** 1 in both, 16 missed by Qwen-7B, 0 reversed, 0 with an object Qwen-7B was not given, 2 only Qwen-7B

**Objects: 4/14 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | woman | hypernym/hyponym | ✓ |
| 1 | clothes | yes (object 2) | clothes rack | mismatch | ✗ |
| 2 | clothes | yes (object 3) | shirt | hypernym/hyponym | ✓ |
| 3 | clothes | yes (object 4) | shirt | hypernym/hyponym | ✓ |
| 4 | closet | yes (object 5) | shirt | mismatch | ✗ |
| 5 | closet divider | yes (object 6) | shirt | mismatch | ✗ |
| 6 | closet divider | yes (object 7) | shirt | mismatch | ✗ |
| 7 | closet shelf | yes (object 8) | shirt | mismatch | ✗ |
| 8 | hair | yes (object 9) | shirt | mismatch | ✗ |
| 9 | face | yes (object 10) | shirt | mismatch | ✗ |
| 10 | hand | yes (object 11) | shirt | mismatch | ✗ |
| 11 | shoulder | yes (object 12) | shirt | mismatch | ✗ |
| 12 | shirt | yes (object 13) | shirt | identical | ✓ |
| 13 | plywood | yes (object 14) | shirt | mismatch | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| person #0 → clothes #1 | ✓ | ✗ (clothes #1 named wrong) | looks at [0-6]; touches [0-3]; moves leftward [2-5] | - | ✗ Qwen-7B missed this pair | - - - | - - - |
| person #0 → closet #4 | ✓ | ✗ (closet #4 named wrong) | in front of [0-5]; browses [0-6] | - | ✗ Qwen-7B missed this pair | - - | - - |
| person #0 → shirt #12 | ✓ | ✓ | wears [0-5] | talks to [0-9] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| clothes #1 → person #0 | ✓ | ✗ (clothes #1 named wrong) | behind [0-6] | - | ✗ Qwen-7B missed this pair | - | - |
| clothes #1 → closet #4 | ✓ | ✗ (clothes #1 named wrong, closet #4 named wrong) | in [0-6] | - | ✗ Qwen-7B missed this pair | - | - |
| clothes #2 → person #0 | ✓ | ✓ | behind [0-5.5] | - | ✗ Qwen-7B missed this pair | - | - |
| clothes #3 → person #0 | ✓ | ✓ | behind [0-5] | - | ✗ Qwen-7B missed this pair | - | - |
| closet divider #5 → person #0 | ✓ | ✗ (closet divider #5 named wrong) | behind [1.5-3.5] | - | ✗ Qwen-7B missed this pair | - | - |
| closet divider #6 → person #0 | ✓ | ✗ (closet divider #6 named wrong) | behind [0-5] | - | ✗ Qwen-7B missed this pair | - | - |
| closet shelf #7 → closet divider #6 | ✓ | ✗ (closet shelf #7 named wrong, closet divider #6 named wrong) | below [0-5] | - | ✗ Qwen-7B missed this pair | - | - |
| hair #8 → closet #4 | ✓ | ✗ (hair #8 named wrong, closet #4 named wrong) | in front of [0-6] | - | ✗ Qwen-7B missed this pair | - | - |
| face #9 → closet #4 | ✓ | ✗ (face #9 named wrong, closet #4 named wrong) | in front of [0-5] | - | ✗ Qwen-7B missed this pair | - | - |
| hand #10 → clothes #1 | ✓ | ✗ (hand #10 named wrong, clothes #1 named wrong) | in front of [0-5] | - | ✗ Qwen-7B missed this pair | - | - |
| hand #10 → closet #4 | ✓ | ✗ (hand #10 named wrong, closet #4 named wrong) | in front of [0-2.5, 3-5] | - | ✗ Qwen-7B missed this pair | - | - |
| hand #10 → face #9 | ✓ | ✗ (hand #10 named wrong, face #9 named wrong) | below [0-2.5, 4.5-6] | - | ✗ Qwen-7B missed this pair | - | - |
| shoulder #11 → face #9 | ✓ | ✗ (shoulder #11 named wrong, face #9 named wrong) | below [0-5] | - | ✗ Qwen-7B missed this pair | - | - |
| shirt #12 → face #9 | ✓ | ✗ (face #9 named wrong) | below [0-5] | - | ✗ Qwen-7B missed this pair | - | - |
| person #0 → hand #10 | ✓ | ✗ (hand #10 named wrong) | - | selects [0-9] | + only Qwen-7B | - | - |
| person #0 → shoulder #11 | ✓ | ✗ (shoulder #11 named wrong) | - | moves [4-9] | + only Qwen-7B | - | - |


## 465_nbJ_SLWUDxk

7.5 s video; humans: 39 objects, 24 relations on 21 pairs; Qwen-7B: 39 relations on 39 pairs.

**Masks given to Qwen-7B:** 39 of 39 objects

**Pairs:** 6 in both, 10 missed by Qwen-7B, 5 reversed, 0 with an object Qwen-7B was not given, 33 only Qwen-7B

**Objects: 0/39 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | - (Qwen-7B wrote no label) | - | ✗ |
| 1 | person | yes (object 2) | - (Qwen-7B wrote no label) | - | ✗ |
| 2 | person | yes (object 3) | - (Qwen-7B wrote no label) | - | ✗ |
| 3 | person | yes (object 4) | - (Qwen-7B wrote no label) | - | ✗ |
| 4 | person | yes (object 5) | - (Qwen-7B wrote no label) | - | ✗ |
| 5 | person | yes (object 6) | - (Qwen-7B wrote no label) | - | ✗ |
| 6 | person | yes (object 7) | - (Qwen-7B wrote no label) | - | ✗ |
| 7 | person | yes (object 8) | - (Qwen-7B wrote no label) | - | ✗ |
| 8 | person | yes (object 9) | - (Qwen-7B wrote no label) | - | ✗ |
| 9 | person | yes (object 10) | - (Qwen-7B wrote no label) | - | ✗ |
| 10 | person | yes (object 11) | - (Qwen-7B wrote no label) | - | ✗ |
| 11 | person | yes (object 12) | - (Qwen-7B wrote no label) | - | ✗ |
| 12 | person | yes (object 13) | - (Qwen-7B wrote no label) | - | ✗ |
| 13 | person | yes (object 14) | - (Qwen-7B wrote no label) | - | ✗ |
| 14 | person | yes (object 15) | - (Qwen-7B wrote no label) | - | ✗ |
| 15 | person | yes (object 16) | - (Qwen-7B wrote no label) | - | ✗ |
| 16 | person | yes (object 17) | - (Qwen-7B wrote no label) | - | ✗ |
| 17 | person | yes (object 18) | - (Qwen-7B wrote no label) | - | ✗ |
| 18 | person | yes (object 19) | - (Qwen-7B wrote no label) | - | ✗ |
| 19 | person | yes (object 20) | - (Qwen-7B wrote no label) | - | ✗ |
| 20 | person | yes (object 21) | - (Qwen-7B wrote no label) | - | ✗ |
| 21 | person | yes (object 22) | - (Qwen-7B wrote no label) | - | ✗ |
| 22 | person | yes (object 23) | - (Qwen-7B wrote no label) | - | ✗ |
| 23 | person | yes (object 24) | - (Qwen-7B wrote no label) | - | ✗ |
| 24 | person | yes (object 25) | - (Qwen-7B wrote no label) | - | ✗ |
| 25 | person | yes (object 26) | - (Qwen-7B wrote no label) | - | ✗ |
| 26 | person | yes (object 27) | - (Qwen-7B wrote no label) | - | ✗ |
| 27 | person | yes (object 28) | - (Qwen-7B wrote no label) | - | ✗ |
| 28 | person | yes (object 29) | - (Qwen-7B wrote no label) | - | ✗ |
| 29 | ground | yes (object 30) | - (Qwen-7B wrote no label) | - | ✗ |
| 30 | buildings | yes (object 31) | - (Qwen-7B wrote no label) | - | ✗ |
| 31 | sky | yes (object 32) | - (Qwen-7B wrote no label) | - | ✗ |
| 32 | river | yes (object 33) | - (Qwen-7B wrote no label) | - | ✗ |
| 33 | light | yes (object 34) | - (Qwen-7B wrote no label) | - | ✗ |
| 34 | light | yes (object 35) | - (Qwen-7B wrote no label) | - | ✗ |
| 35 | saxophone | yes (object 36) | - (Qwen-7B wrote no label) | - | ✗ |
| 36 | shoes | yes (object 37) | - (Qwen-7B wrote no label) | - | ✗ |
| 37 | hat | yes (object 38) | - (Qwen-7B wrote no label) | - | ✗ |
| 38 | suit | yes (object 39) | - (Qwen-7B wrote no label) | - | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| person #0 → person #1 | ✓ | ✗ (person #0 named wrong, person #1 named wrong) | performs for [0-8]; approaches [0-5] | - | ↔ Qwen-7B has it reversed | - - | - - |
| person #0 → person #7 | ✓ | ✗ (person #0 named wrong, person #7 named wrong) | in front of [0-8] | plays saxophone with [0-9] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| person #0 → ground #29 | ✓ | ✗ (person #0 named wrong, ground #29 named wrong) | on [0-8] | - | ↔ Qwen-7B has it reversed | - | - |
| person #0 → buildings #30 | ✓ | ✗ (person #0 named wrong, buildings #30 named wrong) | in front of [0-8] | - | ↔ Qwen-7B has it reversed | - | - |
| person #0 → hat #37 | ✓ | ✗ (person #0 named wrong, hat #37 named wrong) | wears [0-8] | - | ↔ Qwen-7B has it reversed | - | - |
| person #0 → suit #38 | ✓ | ✗ (person #0 named wrong, suit #38 named wrong) | wears [0-8] | - | ↔ Qwen-7B has it reversed | - | - |
| person #1 → person #0 | ✓ | ✗ (person #1 named wrong, person #0 named wrong) | in front of [0-8]; looks at [5-8] | dances next to [0-9] | ✓ Qwen-7B has this pair | ✗ ✗ | ✗ ✗ |
| person #1 → person #2 | ✓ | ✗ (person #1 named wrong, person #2 named wrong) | dances with [0-8]; in front of [0-8] | - | ✗ Qwen-7B missed this pair | - - | - - |
| person #1 → ground #29 | ✓ | ✗ (person #1 named wrong, ground #29 named wrong) | on [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| person #1 → buildings #30 | ✓ | ✗ (person #1 named wrong, buildings #30 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| person #2 → ground #29 | ✓ | ✗ (person #2 named wrong, ground #29 named wrong) | on [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| person #2 → buildings #30 | ✓ | ✗ (person #2 named wrong, buildings #30 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| person #2 → shoes #36 | ✓ | ✗ (person #2 named wrong, shoes #36 named wrong) | wears [0-6] | - | ✗ Qwen-7B missed this pair | - | - |
| person #24 → person #0 | ✓ | ✗ (person #24 named wrong, person #0 named wrong) | looks at [0-8] | claps along with [0-9] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| sky #31 → buildings #30 | ✓ | ✗ (sky #31 named wrong, buildings #30 named wrong) | above [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| river #32 → person #0 | ✓ | ✗ (river #32 named wrong, person #0 named wrong) | behind [0-8] | claps along with [0-9] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| light #33 → ground #29 | ✓ | ✗ (light #33 named wrong, ground #29 named wrong) | above [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| light #34 → ground #29 | ✓ | ✗ (light #34 named wrong, ground #29 named wrong) | above [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| shoes #36 → person #2 | ✓ | ✗ (shoes #36 named wrong, person #2 named wrong) | on [0-6.5] | - | ✗ Qwen-7B missed this pair | - | - |
| hat #37 → person #0 | ✓ | ✗ (hat #37 named wrong, person #0 named wrong) | on [0-8] | claps along with [0-9] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| suit #38 → person #0 | ✓ | ✗ (suit #38 named wrong, person #0 named wrong) | on [0-8] | claps along with [0-9] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| person #2 → person #0 | ✓ | ✗ (person #2 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #3 → person #0 | ✓ | ✗ (person #3 named wrong, person #0 named wrong) | - | stands still behind [0-9] | + only Qwen-7B | - | - |
| person #4 → person #0 | ✓ | ✗ (person #4 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #5 → person #0 | ✓ | ✗ (person #5 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #6 → person #0 | ✓ | ✗ (person #6 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #7 → person #0 | ✓ | ✗ (person #7 named wrong, person #0 named wrong) | - | plays saxophone with [0-9] | + only Qwen-7B | - | - |
| person #8 → person #0 | ✓ | ✗ (person #8 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #9 → person #0 | ✓ | ✗ (person #9 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #10 → person #0 | ✓ | ✗ (person #10 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #11 → person #7 | ✓ | ✗ (person #11 named wrong, person #7 named wrong) | - | plays saxophone with [0-9] | + only Qwen-7B | - | - |
| person #12 → person #0 | ✓ | ✗ (person #12 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #13 → person #0 | ✓ | ✗ (person #13 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #14 → person #0 | ✓ | ✗ (person #14 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #15 → person #0 | ✓ | ✗ (person #15 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #16 → person #0 | ✓ | ✗ (person #16 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #17 → person #0 | ✓ | ✗ (person #17 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #18 → person #0 | ✓ | ✗ (person #18 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #19 → person #0 | ✓ | ✗ (person #19 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #20 → person #0 | ✓ | ✗ (person #20 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #21 → person #0 | ✓ | ✗ (person #21 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #22 → person #0 | ✓ | ✗ (person #22 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #23 → person #0 | ✓ | ✗ (person #23 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #25 → person #0 | ✓ | ✗ (person #25 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #26 → person #0 | ✓ | ✗ (person #26 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #27 → person #0 | ✓ | ✗ (person #27 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| person #28 → person #0 | ✓ | ✗ (person #28 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| ground #29 → person #0 | ✓ | ✗ (ground #29 named wrong, person #0 named wrong) | - | plays saxophone with [0-9] | + only Qwen-7B | - | - |
| buildings #30 → person #0 | ✓ | ✗ (buildings #30 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| sky #31 → person #0 | ✓ | ✗ (sky #31 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| light #33 → person #0 | ✓ | ✗ (light #33 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| light #34 → person #0 | ✓ | ✗ (light #34 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| saxophone #35 → person #0 | ✓ | ✗ (saxophone #35 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |
| shoes #36 → person #0 | ✓ | ✗ (shoes #36 named wrong, person #0 named wrong) | - | claps along with [0-9] | + only Qwen-7B | - | - |


## 700_zkhPzSZcRtQ

22.67 s video; humans: 24 objects, 41 relations on 39 pairs; Qwen-7B: 3 relations on 3 pairs.

**Masks given to Qwen-7B:** 24 of 24 objects

**Pairs:** 2 in both, 37 missed by Qwen-7B, 0 reversed, 0 with an object Qwen-7B was not given, 1 only Qwen-7B

**Objects: 1/24 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | mat | yes (object 1) | mat | identical | ✓ |
| 1 | mat | yes (object 2) | man | mismatch | ✗ |
| 2 | floor | yes (object 3) | bat | mismatch | ✗ |
| 3 | pole | yes (object 4) | cart | mismatch | ✗ |
| 4 | man | yes (object 5) | baseball field | mismatch | ✗ |
| 5 | bat | yes (object 6) | - (Qwen-7B wrote no label) | - | ✗ |
| 6 | wall | yes (object 7) | - (Qwen-7B wrote no label) | - | ✗ |
| 7 | ball cart | yes (object 8) | - (Qwen-7B wrote no label) | - | ✗ |
| 8 | stripe or mat | yes (object 9) | - (Qwen-7B wrote no label) | - | ✗ |
| 9 | stripe | yes (object 10) | - (Qwen-7B wrote no label) | - | ✗ |
| 10 | stripe | yes (object 11) | - (Qwen-7B wrote no label) | - | ✗ |
| 11 | wall poster | yes (object 12) | - (Qwen-7B wrote no label) | - | ✗ |
| 12 | wall poster | yes (object 13) | - (Qwen-7B wrote no label) | - | ✗ |
| 13 | wall poster | yes (object 14) | - (Qwen-7B wrote no label) | - | ✗ |
| 14 | wall poster | yes (object 15) | - (Qwen-7B wrote no label) | - | ✗ |
| 15 | strip | yes (object 16) | - (Qwen-7B wrote no label) | - | ✗ |
| 16 | posters | yes (object 17) | - (Qwen-7B wrote no label) | - | ✗ |
| 17 | shoe | yes (object 18) | - (Qwen-7B wrote no label) | - | ✗ |
| 18 | shoe | yes (object 19) | - (Qwen-7B wrote no label) | - | ✗ |
| 19 | hat | yes (object 20) | - (Qwen-7B wrote no label) | - | ✗ |
| 20 | hoodie | yes (object 21) | - (Qwen-7B wrote no label) | - | ✗ |
| 21 | pants | yes (object 22) | - (Qwen-7B wrote no label) | - | ✗ |
| 22 | ball cart | yes (object 23) | - (Qwen-7B wrote no label) | - | ✗ |
| 23 | poster | yes (object 24) | - (Qwen-7B wrote no label) | - | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| mat #0 → floor #2 | ✓ | ✗ (floor #2 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| mat #0 → wall #6 | ✓ | ✗ (wall #6 named wrong) | in front of [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| mat #1 → mat #0 | ✓ | ✗ (mat #1 named wrong) | behind [0-23] | standing on [0-25] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| mat #1 → floor #2 | ✓ | ✗ (mat #1 named wrong, floor #2 named wrong) | on [0-23] | holding [0-25] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| pole #3 → floor #2 | ✓ | ✗ (pole #3 named wrong, floor #2 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| pole #3 → wall #6 | ✓ | ✗ (pole #3 named wrong, wall #6 named wrong) | in front of [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| man #4 → mat #0 | ✓ | ✗ (man #4 named wrong) | approaching [18-21]; moving away from [20-23] | - | ✗ Qwen-7B missed this pair | - - | - - |
| man #4 → floor #2 | ✓ | ✗ (man #4 named wrong, floor #2 named wrong) | on [0-23]; walking on [18-23] | - | ✗ Qwen-7B missed this pair | - - | - - |
| man #4 → bat #5 | ✓ | ✗ (man #4 named wrong, bat #5 named wrong) | holding [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| man #4 → wall #6 | ✓ | ✗ (man #4 named wrong, wall #6 named wrong) | in front of [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| man #4 → ball cart #7 | ✓ | ✗ (man #4 named wrong, ball cart #7 named wrong) | in front of [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| man #4 → shoe #17 | ✓ | ✗ (man #4 named wrong, shoe #17 named wrong) | wearing [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| man #4 → shoe #18 | ✓ | ✗ (man #4 named wrong, shoe #18 named wrong) | wearing [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| man #4 → hat #19 | ✓ | ✗ (man #4 named wrong, hat #19 named wrong) | wearing [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| man #4 → hoodie #20 | ✓ | ✗ (man #4 named wrong, hoodie #20 named wrong) | wearing [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| man #4 → pants #21 | ✓ | ✗ (man #4 named wrong, pants #21 named wrong) | wearing [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| bat #5 → floor #2 | ✓ | ✗ (bat #5 named wrong, floor #2 named wrong) | above [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| bat #5 → wall #6 | ✓ | ✗ (bat #5 named wrong, wall #6 named wrong) | in front of [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| ball cart #7 → floor #2 | ✓ | ✗ (ball cart #7 named wrong, floor #2 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| ball cart #7 → wall #6 | ✓ | ✗ (ball cart #7 named wrong, wall #6 named wrong) | in front of [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| stripe or mat #8 → floor #2 | ✓ | ✗ (stripe or mat #8 named wrong, floor #2 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| stripe #9 → floor #2 | ✓ | ✗ (stripe #9 named wrong, floor #2 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| stripe #10 → floor #2 | ✓ | ✗ (stripe #10 named wrong, floor #2 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| wall poster #11 → wall #6 | ✓ | ✗ (wall poster #11 named wrong, wall #6 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| wall poster #12 → wall #6 | ✓ | ✗ (wall poster #12 named wrong, wall #6 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| wall poster #13 → wall #6 | ✓ | ✗ (wall poster #13 named wrong, wall #6 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| wall poster #14 → wall #6 | ✓ | ✗ (wall poster #14 named wrong, wall #6 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| posters #16 → wall #6 | ✓ | ✗ (posters #16 named wrong, wall #6 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| shoe #17 → floor #2 | ✓ | ✗ (shoe #17 named wrong, floor #2 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| shoe #18 → floor #2 | ✓ | ✗ (shoe #18 named wrong, floor #2 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| hat #19 → man #4 | ✓ | ✗ (hat #19 named wrong, man #4 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| hat #19 → hoodie #20 | ✓ | ✗ (hat #19 named wrong, hoodie #20 named wrong) | above [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| hoodie #20 → man #4 | ✓ | ✗ (hoodie #20 named wrong, man #4 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| hoodie #20 → pants #21 | ✓ | ✗ (hoodie #20 named wrong, pants #21 named wrong) | above [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| pants #21 → man #4 | ✓ | ✗ (pants #21 named wrong, man #4 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| pants #21 → shoe #17 | ✓ | ✗ (pants #21 named wrong, shoe #17 named wrong) | above [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| pants #21 → shoe #18 | ✓ | ✗ (pants #21 named wrong, shoe #18 named wrong) | above [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| poster #23 → wall #6 | ✓ | ✗ (poster #23 named wrong, wall #6 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| poster #23 → ball cart #7 | ✓ | ✗ (poster #23 named wrong, ball cart #7 named wrong) | above [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| pole #3 → mat #0 | ✓ | ✗ (pole #3 named wrong) | - | in background [0-25] | + only Qwen-7B | - | - |


## 722__ajUvCkhVcI

22.67 s video; humans: 18 objects, 39 relations on 32 pairs; Qwen-7B: 3 relations on 3 pairs.

**Masks given to Qwen-7B:** 18 of 18 objects

**Pairs:** 2 in both, 30 missed by Qwen-7B, 0 reversed, 0 with an object Qwen-7B was not given, 1 only Qwen-7B

**Objects: 2/18 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | baby | yes (object 1) | child | hypernym/hyponym | ✓ |
| 1 | baby | yes (object 2) | boy | semantic overlap | ✓ |
| 2 | baby | yes (object 3) | woman | mismatch | ✗ |
| 3 | ball pit | yes (object 4) | ball | mismatch | ✗ |
| 4 | side of a cage | yes (object 5) | - (Qwen-7B wrote no label) | - | ✗ |
| 5 | side of a cage | yes (object 6) | - (Qwen-7B wrote no label) | - | ✗ |
| 6 | rope | yes (object 7) | - (Qwen-7B wrote no label) | - | ✗ |
| 7 | rope | yes (object 8) | - (Qwen-7B wrote no label) | - | ✗ |
| 8 | shirt | yes (object 9) | - (Qwen-7B wrote no label) | - | ✗ |
| 9 | head | yes (object 10) | - (Qwen-7B wrote no label) | - | ✗ |
| 10 | short | yes (object 11) | - (Qwen-7B wrote no label) | - | ✗ |
| 11 | shirt | yes (object 12) | - (Qwen-7B wrote no label) | - | ✗ |
| 12 | top | yes (object 13) | - (Qwen-7B wrote no label) | - | ✗ |
| 13 | skirt | yes (object 14) | - (Qwen-7B wrote no label) | - | ✗ |
| 14 | trouser | yes (object 15) | - (Qwen-7B wrote no label) | - | ✗ |
| 15 | legs | yes (object 16) | - (Qwen-7B wrote no label) | - | ✗ |
| 16 | legs | yes (object 17) | - (Qwen-7B wrote no label) | - | ✗ |
| 17 | legs | yes (object 18) | - (Qwen-7B wrote no label) | - | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| baby #0 → baby #1 | ✓ | ✓ | looking at [8-11]; in front of [0-23] | near [0-25] | ✓ Qwen-7B has this pair | ✗ ✓ | ✗ ✓ |
| baby #0 → baby #2 | ✓ | ✗ (baby #2 named wrong) | looking at [13-23] | near [0-25] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| baby #0 → ball pit #3 | ✓ | ✗ (ball pit #3 named wrong) | inside [0-23]; playing with [0-23] | - | ✗ Qwen-7B missed this pair | - - | - - |
| baby #0 → side of a cage #4 | ✓ | ✗ (side of a cage #4 named wrong) | in front of [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| baby #0 → side of a cage #5 | ✓ | ✗ (side of a cage #5 named wrong) | in front of [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| baby #0 → shirt #8 | ✓ | ✗ (shirt #8 named wrong) | wearing [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| baby #0 → short #10 | ✓ | ✗ (short #10 named wrong) | wearing [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| baby #1 → ball pit #3 | ✓ | ✗ (ball pit #3 named wrong) | inside [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| baby #1 → side of a cage #4 | ✓ | ✗ (side of a cage #4 named wrong) | in front of [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| baby #1 → side of a cage #5 | ✓ | ✗ (side of a cage #5 named wrong) | holding [8-23]; approaching [1-9]; climbing [8.5-23]; looking at [8-23]; in front of [0-23] | - | ✗ Qwen-7B missed this pair | - - - - - | - - - - - |
| baby #1 → shirt #11 | ✓ | ✗ (shirt #11 named wrong) | wearing [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| baby #1 → trouser #14 | ✓ | ✗ (trouser #14 named wrong) | wearing [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| baby #2 → ball pit #3 | ✓ | ✗ (baby #2 named wrong, ball pit #3 named wrong) | inside [10-19]; playing with [12-20] | - | ✗ Qwen-7B missed this pair | - - | - - |
| baby #2 → side of a cage #4 | ✓ | ✗ (baby #2 named wrong, side of a cage #4 named wrong) | approaching [12-18] | - | ✗ Qwen-7B missed this pair | - | - |
| baby #2 → top #12 | ✓ | ✗ (baby #2 named wrong, top #12 named wrong) | wearing [12-21] | - | ✗ Qwen-7B missed this pair | - | - |
| baby #2 → skirt #13 | ✓ | ✗ (baby #2 named wrong, skirt #13 named wrong) | wearing [12-23] | - | ✗ Qwen-7B missed this pair | - | - |
| rope #6 → baby #0 | ✓ | ✗ (rope #6 named wrong) | in front of [0-9] | - | ✗ Qwen-7B missed this pair | - | - |
| rope #6 → ball pit #3 | ✓ | ✗ (rope #6 named wrong, ball pit #3 named wrong) | in front of [0-9] | - | ✗ Qwen-7B missed this pair | - | - |
| rope #7 → baby #0 | ✓ | ✗ (rope #7 named wrong) | in front of [0-11] | - | ✗ Qwen-7B missed this pair | - | - |
| rope #7 → baby #1 | ✓ | ✗ (rope #7 named wrong) | in front of [0-11.5] | - | ✗ Qwen-7B missed this pair | - | - |
| rope #7 → ball pit #3 | ✓ | ✗ (rope #7 named wrong, ball pit #3 named wrong) | in front of [0-11] | - | ✗ Qwen-7B missed this pair | - | - |
| shirt #8 → baby #0 | ✓ | ✗ (shirt #8 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| head #9 → shirt #8 | ✓ | ✗ (head #9 named wrong, shirt #8 named wrong) | above [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| head #9 → short #10 | ✓ | ✗ (head #9 named wrong, short #10 named wrong) | above [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| short #10 → baby #0 | ✓ | ✗ (short #10 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| short #10 → shirt #8 | ✓ | ✗ (short #10 named wrong, shirt #8 named wrong) | below [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| shirt #11 → baby #1 | ✓ | ✗ (shirt #11 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| shirt #11 → trouser #14 | ✓ | ✗ (shirt #11 named wrong, trouser #14 named wrong) | above [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| top #12 → baby #2 | ✓ | ✗ (top #12 named wrong, baby #2 named wrong) | on [13-21] | - | ✗ Qwen-7B missed this pair | - | - |
| skirt #13 → baby #2 | ✓ | ✗ (skirt #13 named wrong, baby #2 named wrong) | on [12-23] | - | ✗ Qwen-7B missed this pair | - | - |
| skirt #13 → top #12 | ✓ | ✗ (skirt #13 named wrong, top #12 named wrong) | below [12.5-22] | - | ✗ Qwen-7B missed this pair | - | - |
| trouser #14 → baby #1 | ✓ | ✗ (trouser #14 named wrong) | on [0-23] | - | ✗ Qwen-7B missed this pair | - | - |
| baby #1 → baby #2 | ✓ | ✗ (baby #2 named wrong) | - | near [0-25] | + only Qwen-7B | - | - |


## 744_1X6KvqPjk6I

7.5 s video; humans: 32 objects, 26 relations on 23 pairs; Qwen-7B: 0 relations on 0 pairs (answer cut off at the token limit, read up to there).

**Masks given to Qwen-7B:** 32 of 32 objects

**Pairs:** 0 in both, 23 missed by Qwen-7B, 0 reversed, 0 with an object Qwen-7B was not given, 0 only Qwen-7B

**Objects: 0/32 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | dog | yes (object 1) | - (Qwen-7B wrote no label) | - | ✗ |
| 1 | tree | yes (object 2) | - (Qwen-7B wrote no label) | - | ✗ |
| 2 | plant | yes (object 3) | - (Qwen-7B wrote no label) | - | ✗ |
| 3 | fence | yes (object 4) | - (Qwen-7B wrote no label) | - | ✗ |
| 4 | grass | yes (object 5) | - (Qwen-7B wrote no label) | - | ✗ |
| 5 | plants, soil | yes (object 6) | - (Qwen-7B wrote no label) | - | ✗ |
| 6 | plant | yes (object 7) | - (Qwen-7B wrote no label) | - | ✗ |
| 7 | person | yes (object 8) | - (Qwen-7B wrote no label) | - | ✗ |
| 8 | person | yes (object 9) | - (Qwen-7B wrote no label) | - | ✗ |
| 9 | hat | yes (object 10) | - (Qwen-7B wrote no label) | - | ✗ |
| 10 | hair | yes (object 11) | - (Qwen-7B wrote no label) | - | ✗ |
| 11 | tail | yes (object 12) | - (Qwen-7B wrote no label) | - | ✗ |
| 12 | dog leg | yes (object 13) | - (Qwen-7B wrote no label) | - | ✗ |
| 13 | dog leg | yes (object 14) | - (Qwen-7B wrote no label) | - | ✗ |
| 14 | dog leg | yes (object 15) | - (Qwen-7B wrote no label) | - | ✗ |
| 15 | head | yes (object 16) | - (Qwen-7B wrote no label) | - | ✗ |
| 16 | barricade | yes (object 17) | - (Qwen-7B wrote no label) | - | ✗ |
| 17 | barricade | yes (object 18) | - (Qwen-7B wrote no label) | - | ✗ |
| 18 | stone | yes (object 19) | - (Qwen-7B wrote no label) | - | ✗ |
| 19 | gardening glove | yes (object 20) | - (Qwen-7B wrote no label) | - | ✗ |
| 20 | fence | yes (object 21) | - (Qwen-7B wrote no label) | - | ✗ |
| 21 | pillar | yes (object 22) | - (Qwen-7B wrote no label) | - | ✗ |
| 22 | fence | yes (object 23) | - (Qwen-7B wrote no label) | - | ✗ |
| 23 | fence | yes (object 24) | - (Qwen-7B wrote no label) | - | ✗ |
| 24 | pillar | yes (object 25) | - (Qwen-7B wrote no label) | - | ✗ |
| 25 | fence | yes (object 26) | - (Qwen-7B wrote no label) | - | ✗ |
| 26 | wall | yes (object 27) | - (Qwen-7B wrote no label) | - | ✗ |
| 27 | wall | yes (object 28) | - (Qwen-7B wrote no label) | - | ✗ |
| 28 | pillar | yes (object 29) | - (Qwen-7B wrote no label) | - | ✗ |
| 29 | pillar | yes (object 30) | - (Qwen-7B wrote no label) | - | ✗ |
| 30 | fence | yes (object 31) | - (Qwen-7B wrote no label) | - | ✗ |
| 31 | trouser | yes (object 32) | - (Qwen-7B wrote no label) | - | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| dog #0 → grass #4 | ✓ | ✗ (dog #0 named wrong, grass #4 named wrong) | looking at [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| dog #0 → barricade #17 | ✓ | ✗ (dog #0 named wrong, barricade #17 named wrong) | behind [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| dog #0 → wall #27 | ✓ | ✗ (dog #0 named wrong, wall #27 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| grass #4 → barricade #17 | ✓ | ✗ (grass #4 named wrong, barricade #17 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| plants, soil #5 → person #7 | ✓ | ✗ (plants, soil #5 named wrong, person #7 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| plants, soil #5 → barricade #17 | ✓ | ✗ (plants, soil #5 named wrong, barricade #17 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| person #7 → plants, soil #5 | ✓ | ✗ (person #7 named wrong, plants, soil #5 named wrong) | pulling [0-8]; looking at [0-8]; weeding [0-8]; holding [0-8] | - | ✗ Qwen-7B missed this pair | - - - - | - - - - |
| person #7 → hat #9 | ✓ | ✗ (person #7 named wrong, hat #9 named wrong) | wearing [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| person #7 → barricade #17 | ✓ | ✗ (person #7 named wrong, barricade #17 named wrong) | behind [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| person #7 → wall #27 | ✓ | ✗ (person #7 named wrong, wall #27 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| person #7 → trouser #31 | ✓ | ✗ (person #7 named wrong, trouser #31 named wrong) | wearing [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| hat #9 → person #7 | ✓ | ✗ (hat #9 named wrong, person #7 named wrong) | on [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| hair #10 → person #7 | ✓ | ✗ (hair #10 named wrong, person #7 named wrong) | on [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| hair #10 → hat #9 | ✓ | ✗ (hair #10 named wrong, hat #9 named wrong) | below [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| tail #11 → dog #0 | ✓ | ✗ (tail #11 named wrong, dog #0 named wrong) | part of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| dog leg #12 → dog #0 | ✓ | ✗ (dog leg #12 named wrong, dog #0 named wrong) | part of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| dog leg #13 → dog #0 | ✓ | ✗ (dog leg #13 named wrong, dog #0 named wrong) | part of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| dog leg #14 → dog #0 | ✓ | ✗ (dog leg #14 named wrong, dog #0 named wrong) | part of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| head #15 → dog #0 | ✓ | ✗ (head #15 named wrong, dog #0 named wrong) | part of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| barricade #16 → person #7 | ✓ | ✗ (barricade #16 named wrong, person #7 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| stone #18 → barricade #16 | ✓ | ✗ (stone #18 named wrong, barricade #16 named wrong) | on [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| gardening glove #19 → barricade #17 | ✓ | ✗ (gardening glove #19 named wrong, barricade #17 named wrong) | on [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| trouser #31 → person #7 | ✓ | ✗ (trouser #31 named wrong, person #7 named wrong) | on [0-8] | - | ✗ Qwen-7B missed this pair | - | - |


## 888_BS3hab7EtAg

7.5 s video; humans: 26 objects, 39 relations on 36 pairs; Qwen-7B: 75 relations on 68 pairs.

**Masks given to Qwen-7B:** 26 of 26 objects

**Pairs:** 8 in both, 16 missed by Qwen-7B, 12 reversed, 0 with an object Qwen-7B was not given, 60 only Qwen-7B

**Objects: 3/26 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | barricade | yes (object 1) | tiger | mismatch | ✗ |
| 1 | trunk | yes (object 2) | cow | mismatch | ✗ |
| 2 | building | yes (object 3) | tree | mismatch | ✗ |
| 3 | trees | yes (object 4) | fence | mismatch | ✗ |
| 4 | trees | yes (object 5) | grass | mismatch | ✗ |
| 5 | trees | yes (object 6) | bush | semantic overlap | ✓ |
| 6 | grass | yes (object 7) | dirt | mismatch | ✗ |
| 7 | grass | yes (object 8) | water | mismatch | ✗ |
| 8 | grass | yes (object 9) | people | mismatch | ✗ |
| 9 | people | yes (object 10) | building | mismatch | ✗ |
| 10 | tiger | yes (object 11) | tiger2 | identical | ✓ |
| 11 | cow | yes (object 12) | cow2 | identical | ✓ |
| 12 | trunk | yes (object 13) | tree2 | mismatch | ✗ |
| 13 | trunk | yes (object 14) | fence2 | mismatch | ✗ |
| 14 | trunk | yes (object 15) | grass2 | mismatch | ✗ |
| 15 | trunk | yes (object 16) | bush2 | mismatch | ✗ |
| 16 | trunk | yes (object 17) | dirt2 | mismatch | ✗ |
| 17 | trunk | yes (object 18) | water2 | mismatch | ✗ |
| 18 | trunk | yes (object 19) | people2 | mismatch | ✗ |
| 19 | trunk | yes (object 20) | building2 | mismatch | ✗ |
| 20 | trunk | yes (object 21) | tiger3 | mismatch | ✗ |
| 21 | legs | yes (object 22) | cow3 | mismatch | ✗ |
| 22 | legs | yes (object 23) | tree3 | mismatch | ✗ |
| 23 | tail | yes (object 24) | fence3 | mismatch | ✗ |
| 24 | tiger head | yes (object 25) | grass3 | mismatch | ✗ |
| 25 | ram head | yes (object 26) | bush3 | mismatch | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| trees #3 → barricade #0 | ✓ | ✗ (trees #3 named wrong, barricade #0 named wrong) | in front of [0-8] | - | ↔ Qwen-7B has it reversed | - | - |
| trees #3 → people #9 | ✓ | ✗ (trees #3 named wrong, people #9 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| trees #4 → barricade #0 | ✓ | ✗ (trees #4 named wrong, barricade #0 named wrong) | in front of [0-8] | - | ↔ Qwen-7B has it reversed | - | - |
| trees #4 → people #9 | ✓ | ✗ (trees #4 named wrong, people #9 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| trees #5 → barricade #0 | ✓ | ✗ (barricade #0 named wrong) | in front of [0-8] | - | ↔ Qwen-7B has it reversed | - | - |
| trees #5 → people #9 | ✓ | ✗ (people #9 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| grass #7 → grass #6 | ✓ | ✗ (grass #7 named wrong, grass #6 named wrong) | on [0-5] | - | ✗ Qwen-7B missed this pair | - | - |
| grass #8 → grass #6 | ✓ | ✗ (grass #8 named wrong, grass #6 named wrong) | on [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| people #9 → barricade #0 | ✓ | ✗ (people #9 named wrong, barricade #0 named wrong) | behind [0-8] | - | ↔ Qwen-7B has it reversed | - | - |
| tiger #10 → barricade #0 | ✓ | ✗ (barricade #0 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| tiger #10 → trees #3 | ✓ | ✗ (trees #3 named wrong) | in front of [0-8] | stands near [0-9] | ✓ Qwen-7B has this pair | ✓ | ✗ |
| tiger #10 → trees #4 | ✓ | ✗ (trees #4 named wrong) | in front of [0-8] | stands near [0-9] | ✓ Qwen-7B has this pair | ✓ | ✗ |
| tiger #10 → trees #5 | ✓ | ✓ | in front of [0-8] | stands near [0-9] | ✓ Qwen-7B has this pair | ✓ | ✓ |
| tiger #10 → grass #6 | ✓ | ✗ (grass #6 named wrong) | on [0-8] | stands near [0-9] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| tiger #10 → people #9 | ✓ | ✗ (people #9 named wrong) | in front of [0-8] | stands near [0-9] | ✓ Qwen-7B has this pair | ✓ | ✗ |
| tiger #10 → cow #11 | ✓ | ✓ | looking at [0-8]; approaching [0-8] | walks near [0-9]; runs past [0-9] | ✓ Qwen-7B has this pair | ✗ ✓ | ✗ ✓ |
| tiger #10 → trunk #14 | ✓ | ✗ (trunk #14 named wrong) | in front of [0-8] | stands near [0-9] | ✓ Qwen-7B has this pair | ✓ | ✗ |
| tiger #10 → trunk #17 | ✓ | ✗ (trunk #17 named wrong) | in front of [0-8] | stands near [0-9] | ✓ Qwen-7B has this pair | ✓ | ✗ |
| cow #11 → barricade #0 | ✓ | ✗ (barricade #0 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| cow #11 → trees #3 | ✓ | ✗ (trees #3 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| cow #11 → trees #4 | ✓ | ✗ (trees #4 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| cow #11 → trees #5 | ✓ | ✓ | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| cow #11 → grass #6 | ✓ | ✗ (grass #6 named wrong) | on [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| cow #11 → people #9 | ✓ | ✗ (people #9 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| cow #11 → tiger #10 | ✓ | ✓ | looking at [2-8]; moving away from [2-5]; approaching [5-8] | - | ↔ Qwen-7B has it reversed | - - - | - - - |
| cow #11 → trunk #14 | ✓ | ✗ (trunk #14 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| cow #11 → trunk #17 | ✓ | ✗ (trunk #17 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| trunk #14 → barricade #0 | ✓ | ✗ (trunk #14 named wrong, barricade #0 named wrong) | in front of [0-8] | - | ↔ Qwen-7B has it reversed | - | - |
| trunk #16 → barricade #0 | ✓ | ✗ (trunk #16 named wrong, barricade #0 named wrong) | in front of [0-8] | - | ↔ Qwen-7B has it reversed | - | - |
| trunk #17 → barricade #0 | ✓ | ✗ (trunk #17 named wrong, barricade #0 named wrong) | in front of [0-8] | - | ↔ Qwen-7B has it reversed | - | - |
| trunk #18 → barricade #0 | ✓ | ✗ (trunk #18 named wrong, barricade #0 named wrong) | in front of [0-8] | - | ↔ Qwen-7B has it reversed | - | - |
| legs #21 → cow #11 | ✓ | ✗ (legs #21 named wrong) | under [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| legs #22 → tiger #10 | ✓ | ✗ (legs #22 named wrong) | under [0-8] | - | ↔ Qwen-7B has it reversed | - | - |
| tail #23 → tiger #10 | ✓ | ✗ (tail #23 named wrong) | attached to [0-8] | - | ↔ Qwen-7B has it reversed | - | - |
| tiger head #24 → tiger #10 | ✓ | ✗ (tiger head #24 named wrong) | attached to [0-8] | - | ↔ Qwen-7B has it reversed | - | - |
| ram head #25 → cow #11 | ✓ | ✗ (ram head #25 named wrong) | attached to [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| barricade #0 → trunk #1 | ✓ | ✗ (barricade #0 named wrong, trunk #1 named wrong) | - | walks near [0-9]; runs past [0-9] | + only Qwen-7B | - | - |
| barricade #0 → building #2 | ✓ | ✗ (barricade #0 named wrong, building #2 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → trees #3 | ✓ | ✗ (barricade #0 named wrong, trees #3 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → trees #4 | ✓ | ✗ (barricade #0 named wrong, trees #4 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → trees #5 | ✓ | ✗ (barricade #0 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → grass #6 | ✓ | ✗ (barricade #0 named wrong, grass #6 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → grass #7 | ✓ | ✗ (barricade #0 named wrong, grass #7 named wrong) | - | stands in [0-9]; stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → grass #8 | ✓ | ✗ (barricade #0 named wrong, grass #8 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → people #9 | ✓ | ✗ (barricade #0 named wrong, people #9 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → trunk #12 | ✓ | ✗ (barricade #0 named wrong, trunk #12 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → trunk #13 | ✓ | ✗ (barricade #0 named wrong, trunk #13 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → trunk #14 | ✓ | ✗ (barricade #0 named wrong, trunk #14 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → trunk #15 | ✓ | ✗ (barricade #0 named wrong, trunk #15 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → trunk #16 | ✓ | ✗ (barricade #0 named wrong, trunk #16 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → trunk #17 | ✓ | ✗ (barricade #0 named wrong, trunk #17 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → trunk #18 | ✓ | ✗ (barricade #0 named wrong, trunk #18 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → trunk #19 | ✓ | ✗ (barricade #0 named wrong, trunk #19 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → trunk #20 | ✓ | ✗ (barricade #0 named wrong, trunk #20 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → legs #21 | ✓ | ✗ (barricade #0 named wrong, legs #21 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → legs #22 | ✓ | ✗ (barricade #0 named wrong, legs #22 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → tail #23 | ✓ | ✗ (barricade #0 named wrong, tail #23 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → tiger head #24 | ✓ | ✗ (barricade #0 named wrong, tiger head #24 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| barricade #0 → ram head #25 | ✓ | ✗ (barricade #0 named wrong, ram head #25 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| tiger #10 → building #2 | ✓ | ✗ (building #2 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| tiger #10 → grass #7 | ✓ | ✗ (grass #7 named wrong) | - | stands in [0-9]; stands near [0-9] | + only Qwen-7B | - | - |
| tiger #10 → grass #8 | ✓ | ✗ (grass #8 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| tiger #10 → trunk #12 | ✓ | ✗ (trunk #12 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| tiger #10 → trunk #13 | ✓ | ✗ (trunk #13 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| tiger #10 → trunk #15 | ✓ | ✗ (trunk #15 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| tiger #10 → trunk #16 | ✓ | ✗ (trunk #16 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| tiger #10 → trunk #18 | ✓ | ✗ (trunk #18 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| tiger #10 → trunk #19 | ✓ | ✗ (trunk #19 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| tiger #10 → trunk #20 | ✓ | ✗ (trunk #20 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| tiger #10 → legs #21 | ✓ | ✗ (legs #21 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| tiger #10 → legs #22 | ✓ | ✗ (legs #22 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| tiger #10 → tail #23 | ✓ | ✗ (tail #23 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| tiger #10 → tiger head #24 | ✓ | ✗ (tiger head #24 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| tiger #10 → ram head #25 | ✓ | ✗ (ram head #25 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → building #2 | ✓ | ✗ (trunk #20 named wrong, building #2 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → trees #3 | ✓ | ✗ (trunk #20 named wrong, trees #3 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → trees #4 | ✓ | ✗ (trunk #20 named wrong, trees #4 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → trees #5 | ✓ | ✗ (trunk #20 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → grass #6 | ✓ | ✗ (trunk #20 named wrong, grass #6 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → grass #7 | ✓ | ✗ (trunk #20 named wrong, grass #7 named wrong) | - | stands in [0-9]; stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → grass #8 | ✓ | ✗ (trunk #20 named wrong, grass #8 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → people #9 | ✓ | ✗ (trunk #20 named wrong, people #9 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → trunk #12 | ✓ | ✗ (trunk #20 named wrong, trunk #12 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → trunk #13 | ✓ | ✗ (trunk #20 named wrong, trunk #13 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → trunk #14 | ✓ | ✗ (trunk #20 named wrong, trunk #14 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → trunk #15 | ✓ | ✗ (trunk #20 named wrong, trunk #15 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → trunk #16 | ✓ | ✗ (trunk #20 named wrong, trunk #16 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → trunk #17 | ✓ | ✗ (trunk #20 named wrong, trunk #17 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → trunk #18 | ✓ | ✗ (trunk #20 named wrong, trunk #18 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → trunk #19 | ✓ | ✗ (trunk #20 named wrong, trunk #19 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → trunk #20 | ✓ | ✗ (trunk #20 named wrong, trunk #20 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → legs #21 | ✓ | ✗ (trunk #20 named wrong, legs #21 named wrong) | - | walks near [0-9]; runs past [0-9]; stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → legs #22 | ✓ | ✗ (trunk #20 named wrong, legs #22 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → tail #23 | ✓ | ✗ (trunk #20 named wrong, tail #23 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → tiger head #24 | ✓ | ✗ (trunk #20 named wrong, tiger head #24 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |
| trunk #20 → ram head #25 | ✓ | ✗ (trunk #20 named wrong, ram head #25 named wrong) | - | stands near [0-9] | + only Qwen-7B | - | - |


## 914_f4HgijyAEYs

7.5 s video; humans: 19 objects, 21 relations on 19 pairs; Qwen-7B: 5 relations on 4 pairs.

**Masks given to Qwen-7B:** 19 of 19 objects

**Pairs:** 3 in both, 15 missed by Qwen-7B, 1 reversed, 0 with an object Qwen-7B was not given, 1 only Qwen-7B

**Objects: 2/19 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | girl | hypernym/hyponym | ✓ |
| 1 | cotton candy | yes (object 2) | cotton_candy | identical | ✓ |
| 2 | seat | yes (object 3) | carousel | mismatch | ✗ |
| 3 | ride | yes (object 4) | ground | mismatch | ✗ |
| 4 | landing | yes (object 5) | background | mismatch | ✗ |
| 5 | building | yes (object 6) | - (Qwen-7B wrote no label) | - | ✗ |
| 6 | circus | yes (object 7) | - (Qwen-7B wrote no label) | - | ✗ |
| 7 | circus | yes (object 8) | - (Qwen-7B wrote no label) | - | ✗ |
| 8 | circus | yes (object 9) | - (Qwen-7B wrote no label) | - | ✗ |
| 9 | sky | yes (object 10) | - (Qwen-7B wrote no label) | - | ✗ |
| 10 | seat | yes (object 11) | - (Qwen-7B wrote no label) | - | ✗ |
| 11 | ground | yes (object 12) | - (Qwen-7B wrote no label) | - | ✗ |
| 12 | light | yes (object 13) | - (Qwen-7B wrote no label) | - | ✗ |
| 13 | light | yes (object 14) | - (Qwen-7B wrote no label) | - | ✗ |
| 14 | glasses | yes (object 15) | - (Qwen-7B wrote no label) | - | ✗ |
| 15 | hair | yes (object 16) | - (Qwen-7B wrote no label) | - | ✗ |
| 16 | jacket | yes (object 17) | - (Qwen-7B wrote no label) | - | ✗ |
| 17 | hand | yes (object 18) | - (Qwen-7B wrote no label) | - | ✗ |
| 18 | hand | yes (object 19) | - (Qwen-7B wrote no label) | - | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| person #0 → cotton candy #1 | ✓ | ✓ | holding [0-8]; eating [0-3]; snacking on [0-3] | eating [0-9]; holding [0-9] | ✓ Qwen-7B has this pair | ✓ ✗ ✗ | ✓ ✗ ✗ |
| person #0 → ride #3 | ✓ | ✗ (ride #3 named wrong) | in front of [0-8] | standing_on [0-9] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| person #0 → landing #4 | ✓ | ✗ (landing #4 named wrong) | in front of [0-8] | in_front_of [0-9] | ✓ Qwen-7B has this pair | ✓ | ✗ |
| person #0 → building #5 | ✓ | ✗ (building #5 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| person #0 → sky #9 | ✓ | ✗ (sky #9 named wrong) | under [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| person #0 → glasses #14 | ✓ | ✗ (glasses #14 named wrong) | wearing [0-4, 5-8] | - | ✗ Qwen-7B missed this pair | - | - |
| person #0 → jacket #16 | ✓ | ✗ (jacket #16 named wrong) | wearing [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| cotton candy #1 → person #0 | ✓ | ✓ | in front of [0-8] | - | ↔ Qwen-7B has it reversed | - | - |
| cotton candy #1 → ride #3 | ✓ | ✗ (ride #3 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| cotton candy #1 → building #5 | ✓ | ✗ (building #5 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| cotton candy #1 → sky #9 | ✓ | ✗ (sky #9 named wrong) | below [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| cotton candy #1 → light #12 | ✓ | ✗ (light #12 named wrong) | above [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| cotton candy #1 → light #13 | ✓ | ✗ (light #13 named wrong) | above [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| seat #2 → ride #3 | ✓ | ✗ (seat #2 named wrong, ride #3 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| light #12 → ride #3 | ✓ | ✗ (light #12 named wrong, ride #3 named wrong) | on [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| light #13 → ride #3 | ✓ | ✗ (light #13 named wrong, ride #3 named wrong) | on [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| glasses #14 → person #0 | ✓ | ✗ (glasses #14 named wrong) | on [0-4, 5-8] | - | ✗ Qwen-7B missed this pair | - | - |
| hair #15 → person #0 | ✓ | ✗ (hair #15 named wrong) | on [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| jacket #16 → person #0 | ✓ | ✗ (jacket #16 named wrong) | on [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| cotton candy #1 → seat #2 | ✓ | ✗ (seat #2 named wrong) | - | spinning [0-9] | + only Qwen-7B | - | - |


## 976_U19VojbI0h4

7.5 s video; humans: 65 objects, 36 relations on 32 pairs; Qwen-7B: 40 relations on 40 pairs.

**Masks given to Qwen-7B:** 40 of 65 objects (25 after the first 40, 0 with no mask on the frames Qwen-7B reads)

**Pairs:** 2 in both, 17 missed by Qwen-7B, 1 reversed, 12 with an object Qwen-7B was not given, 38 only Qwen-7B

**Objects: 12/65 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | ground | yes (object 1) | floor | synonym | ✓ |
| 1 | painting | yes (object 2) | door | mismatch | ✗ |
| 2 | plant | yes (object 3) | painting | mismatch | ✗ |
| 3 | decoration | yes (object 4) | cabinet | mismatch | ✗ |
| 4 | fireplace | yes (object 5) | fireplace | identical | ✓ |
| 5 | cabinet | yes (object 6) | table | mismatch | ✗ |
| 6 | door | yes (object 7) | wall | mismatch | ✗ |
| 7 | wall | yes (object 8) | rug | mismatch | ✗ |
| 8 | door | yes (object 9) | door | identical | ✓ |
| 9 | lamp | yes (object 10) | lamp | identical | ✓ |
| 10 | table | yes (object 11) | plant | mismatch | ✗ |
| 11 | interior | yes (object 12) | shelf | semantic overlap | ✓ |
| 12 | shelf | yes (object 13) | wall | mismatch | ✗ |
| 13 | interior | yes (object 14) | vase | mismatch | ✗ |
| 14 | ceiling fan | yes (object 15) | ceiling | semantic overlap | ✓ |
| 15 | ceiling and upper wall | yes (object 16) | ceiling light | mismatch | ✗ |
| 16 | closet | yes (object 17) | door | mismatch | ✗ |
| 17 | outlet | yes (object 18) | door | mismatch | ✗ |
| 18 | table | yes (object 19) | coffee table | hypernym/hyponym | ✓ |
| 19 | rug | yes (object 20) | rug | identical | ✓ |
| 20 | vase | yes (object 21) | plant | mismatch | ✗ |
| 21 | doorway | yes (object 22) | door | semantic overlap | ✓ |
| 22 | wall | yes (object 23) | painting | mismatch | ✗ |
| 23 | wall | yes (object 24) | shelf | mismatch | ✗ |
| 24 | wall | yes (object 25) | lamp | mismatch | ✗ |
| 25 | lamp shade | yes (object 26) | plant | mismatch | ✗ |
| 26 | lamp base | yes (object 27) | shelf | mismatch | ✗ |
| 27 | throw pillow | yes (object 28) | coffee table | mismatch | ✗ |
| 28 | couch | yes (object 29) | plant | mismatch | ✗ |
| 29 | cup | yes (object 30) | rug | mismatch | ✗ |
| 30 | leaves | yes (object 31) | plant | mismatch | ✗ |
| 31 | fireplace | yes (object 32) | fireplace | identical | ✓ |
| 32 | fireplace face | yes (object 33) | ceiling | mismatch | ✗ |
| 33 | ceiling area | yes (object 34) | ceiling light | mismatch | ✗ |
| 34 | fireplace frame | yes (object 35) | door | mismatch | ✗ |
| 35 | flower vase | yes (object 36) | painting | mismatch | ✗ |
| 36 | vase | yes (object 37) | shelf | mismatch | ✗ |
| 37 | home decor | yes (object 38) | lamp | hypernym/hyponym | ✓ |
| 38 | home decor | yes (object 39) | plant | semantic overlap | ✓ |
| 39 | socket | yes (object 40) | vase | mismatch | ✗ |
| 40 | flower | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 41 | vase stand | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 42 | tray | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 43 | fan | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 44 | cupboard handle | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 45 | cupboard handle | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 46 | flower vase | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 47 | flower stand | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 48 | vase | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 49 | home decor | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 50 | glass | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 51 | fireplace | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 52 | door | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 53 | ground | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 54 | door | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 55 | shelf | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 56 | shelf | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 57 | shelf | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 58 | household item | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 59 | wall | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 60 | light | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 61 | door frame | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 62 | top of a cupboard | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 63 | door of cupboard | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |
| 64 | door of cupboard | no: after the first 40 | - (never shown to Qwen-7B) | - | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| painting #1 → fireplace #4 | ✓ | ✗ (painting #1 named wrong) | above [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| painting #1 → wall #22 | ✓ | ✗ (painting #1 named wrong, wall #22 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| painting #1 → fireplace face #32 | ✓ | ✗ (painting #1 named wrong, fireplace face #32 named wrong) | on [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| plant #2 → fireplace #4 | ✓ | ✗ (plant #2 named wrong) | above [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| plant #2 → wall #22 | ✓ | ✗ (plant #2 named wrong, wall #22 named wrong) | in front of [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| plant #2 → fireplace face #32 | ✓ | ✗ (plant #2 named wrong, fireplace face #32 named wrong) | on [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| plant #2 → flower vase #46 | ✗ (flower vase #46 not given) | ✗ (plant #2 named wrong, flower vase #46 not given) | in [0-8] | - | ⊘ an object was not given to Qwen-7B (40-object cap / no mask on its frames) | - | - |
| decoration #3 → wall #22 | ✓ | ✗ (decoration #3 named wrong, wall #22 named wrong) | in front of [0-5.5] | - | ✗ Qwen-7B missed this pair | - | - |
| decoration #3 → fireplace face #32 | ✓ | ✗ (decoration #3 named wrong, fireplace face #32 named wrong) | on [0-5.5] | - | ✗ Qwen-7B missed this pair | - | - |
| fireplace #4 → wall #22 | ✓ | ✗ (wall #22 named wrong) | in [0-8]; against [0-8] | - | ✗ Qwen-7B missed this pair | - - | - - |
| cabinet #5 → ground #0 | ✓ | ✗ (cabinet #5 named wrong) | on [0-4] | - | ✗ Qwen-7B missed this pair | - | - |
| door #6 → closet #16 | ✓ | ✗ (door #6 named wrong, closet #16 named wrong) | attached to [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| door #6 → wall #59 | ✗ (wall #59 not given) | ✗ (door #6 named wrong, wall #59 not given) | in [0-8] | - | ⊘ an object was not given to Qwen-7B (40-object cap / no mask on its frames) | - | - |
| door #6 → door frame #61 | ✗ (door frame #61 not given) | ✗ (door #6 named wrong, door frame #61 not given) | inside [0-8]; attached to [0-8] | - | ⊘ an object was not given to Qwen-7B (40-object cap / no mask on its frames) | - - | - - |
| door #8 → wall #7 | ✓ | ✗ (wall #7 named wrong) | inside [0-8] | - | ↔ Qwen-7B has it reversed | - | - |
| lamp #9 → table #10 | ✓ | ✗ (table #10 named wrong) | on [0-1] | on top of [0-9] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| closet #16 → door #54 | ✗ (door #54 not given) | ✗ (closet #16 named wrong, door #54 not given) | behind [0-8] | - | ⊘ an object was not given to Qwen-7B (40-object cap / no mask on its frames) | - | - |
| table #18 → ground #0 | ✓ | ✓ | on [0-7] | - | ✗ Qwen-7B missed this pair | - | - |
| rug #19 → ground #0 | ✓ | ✓ | on [0-2] | - | ✗ Qwen-7B missed this pair | - | - |
| vase #20 → table #18 | ✓ | ✗ (vase #20 named wrong) | on [0-2] | - | ✗ Qwen-7B missed this pair | - | - |
| doorway #21 → fireplace frame #34 | ✓ | ✗ (fireplace frame #34 named wrong) | in [0-8]; in [0-8] | - | ✗ Qwen-7B missed this pair | - - | - - |
| fireplace #31 → wall #22 | ✓ | ✗ (wall #22 named wrong) | in [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| fireplace #31 → fireplace face #32 | ✓ | ✗ (fireplace face #32 named wrong) | under [0-8] | behind [0-9] | ✓ Qwen-7B has this pair | ✗ | ✗ |
| fireplace face #32 → wall #22 | ✓ | ✗ (fireplace face #32 named wrong, wall #22 named wrong) | against [0-8] | - | ✗ Qwen-7B missed this pair | - | - |
| flower vase #46 → flower stand #47 | ✗ (flower vase #46, flower stand #47 not given) | ✗ (flower vase #46 not given, flower stand #47 not given) | on [0-8] | - | ⊘ an object was not given to Qwen-7B (40-object cap / no mask on its frames) | - | - |
| door #52 → doorway #21 | ✗ (door #52 not given) | ✗ (door #52 not given) | inside [0-8] | - | ⊘ an object was not given to Qwen-7B (40-object cap / no mask on its frames) | - | - |
| ground #53 → doorway #21 | ✗ (ground #53 not given) | ✗ (ground #53 not given) | inside [0-8] | - | ⊘ an object was not given to Qwen-7B (40-object cap / no mask on its frames) | - | - |
| door #54 → wall #59 | ✗ (door #54, wall #59 not given) | ✗ (door #54 not given, wall #59 not given) | in [0-8] | - | ⊘ an object was not given to Qwen-7B (40-object cap / no mask on its frames) | - | - |
| door #54 → door frame #61 | ✗ (door #54, door frame #61 not given) | ✗ (door #54 not given, door frame #61 not given) | attached to [0-8]; inside [0-8] | - | ⊘ an object was not given to Qwen-7B (40-object cap / no mask on its frames) | - - | - - |
| shelf #55 → closet #16 | ✗ (shelf #55 not given) | ✗ (shelf #55 not given, closet #16 named wrong) | in [0-8] | - | ⊘ an object was not given to Qwen-7B (40-object cap / no mask on its frames) | - | - |
| shelf #56 → closet #16 | ✗ (shelf #56 not given) | ✗ (shelf #56 not given, closet #16 named wrong) | in [0-8] | - | ⊘ an object was not given to Qwen-7B (40-object cap / no mask on its frames) | - | - |
| shelf #57 → closet #16 | ✗ (shelf #57 not given) | ✗ (shelf #57 not given, closet #16 named wrong) | in [0-8] | - | ⊘ an object was not given to Qwen-7B (40-object cap / no mask on its frames) | - | - |
| ground #0 → painting #1 | ✓ | ✗ (painting #1 named wrong) | - | in front of [0-9] | + only Qwen-7B | - | - |
| painting #1 → plant #2 | ✓ | ✗ (painting #1 named wrong, plant #2 named wrong) | - | above [0-9] | + only Qwen-7B | - | - |
| plant #2 → decoration #3 | ✓ | ✗ (plant #2 named wrong, decoration #3 named wrong) | - | on top of [0-9] | + only Qwen-7B | - | - |
| decoration #3 → fireplace #4 | ✓ | ✗ (decoration #3 named wrong) | - | in front of [0-9] | + only Qwen-7B | - | - |
| fireplace #4 → cabinet #5 | ✓ | ✗ (cabinet #5 named wrong) | - | on top of [0-9] | + only Qwen-7B | - | - |
| cabinet #5 → door #6 | ✓ | ✗ (cabinet #5 named wrong, door #6 named wrong) | - | next to [0-9] | + only Qwen-7B | - | - |
| door #6 → wall #7 | ✓ | ✗ (door #6 named wrong, wall #7 named wrong) | - | behind [0-9] | + only Qwen-7B | - | - |
| wall #7 → door #8 | ✓ | ✗ (wall #7 named wrong) | - | in front of [0-9] | + only Qwen-7B | - | - |
| door #8 → lamp #9 | ✓ | ✓ | - | next to [0-9] | + only Qwen-7B | - | - |
| table #10 → interior #11 | ✓ | ✗ (table #10 named wrong) | - | on top of [0-9] | + only Qwen-7B | - | - |
| interior #11 → shelf #12 | ✓ | ✗ (shelf #12 named wrong) | - | next to [0-9] | + only Qwen-7B | - | - |
| shelf #12 → interior #13 | ✓ | ✗ (shelf #12 named wrong, interior #13 named wrong) | - | behind [0-9] | + only Qwen-7B | - | - |
| interior #13 → ceiling fan #14 | ✓ | ✗ (interior #13 named wrong) | - | on top of [0-9] | + only Qwen-7B | - | - |
| ceiling fan #14 → ceiling and upper wall #15 | ✓ | ✗ (ceiling and upper wall #15 named wrong) | - | above [0-9] | + only Qwen-7B | - | - |
| ceiling and upper wall #15 → closet #16 | ✓ | ✗ (ceiling and upper wall #15 named wrong, closet #16 named wrong) | - | next to [0-9] | + only Qwen-7B | - | - |
| closet #16 → outlet #17 | ✓ | ✗ (closet #16 named wrong, outlet #17 named wrong) | - | behind [0-9] | + only Qwen-7B | - | - |
| outlet #17 → table #18 | ✓ | ✗ (outlet #17 named wrong) | - | next to [0-9] | + only Qwen-7B | - | - |
| table #18 → rug #19 | ✓ | ✓ | - | on top of [0-9] | + only Qwen-7B | - | - |
| rug #19 → vase #20 | ✓ | ✗ (vase #20 named wrong) | - | next to [0-9] | + only Qwen-7B | - | - |
| vase #20 → doorway #21 | ✓ | ✗ (vase #20 named wrong) | - | on top of [0-9] | + only Qwen-7B | - | - |
| doorway #21 → wall #22 | ✓ | ✗ (wall #22 named wrong) | - | behind [0-9] | + only Qwen-7B | - | - |
| wall #22 → wall #23 | ✓ | ✗ (wall #22 named wrong, wall #23 named wrong) | - | on top of [0-9] | + only Qwen-7B | - | - |
| wall #23 → wall #24 | ✓ | ✗ (wall #23 named wrong, wall #24 named wrong) | - | next to [0-9] | + only Qwen-7B | - | - |
| wall #24 → lamp shade #25 | ✓ | ✗ (wall #24 named wrong, lamp shade #25 named wrong) | - | on top of [0-9] | + only Qwen-7B | - | - |
| lamp shade #25 → lamp base #26 | ✓ | ✗ (lamp shade #25 named wrong, lamp base #26 named wrong) | - | next to [0-9] | + only Qwen-7B | - | - |
| lamp base #26 → throw pillow #27 | ✓ | ✗ (lamp base #26 named wrong, throw pillow #27 named wrong) | - | on top of [0-9] | + only Qwen-7B | - | - |
| throw pillow #27 → couch #28 | ✓ | ✗ (throw pillow #27 named wrong, couch #28 named wrong) | - | next to [0-9] | + only Qwen-7B | - | - |
| couch #28 → cup #29 | ✓ | ✗ (couch #28 named wrong, cup #29 named wrong) | - | on top of [0-9] | + only Qwen-7B | - | - |
| cup #29 → leaves #30 | ✓ | ✗ (cup #29 named wrong, leaves #30 named wrong) | - | next to [0-9] | + only Qwen-7B | - | - |
| leaves #30 → fireplace #31 | ✓ | ✗ (leaves #30 named wrong) | - | on top of [0-9] | + only Qwen-7B | - | - |
| fireplace face #32 → ceiling area #33 | ✓ | ✗ (fireplace face #32 named wrong, ceiling area #33 named wrong) | - | above [0-9] | + only Qwen-7B | - | - |
| ceiling area #33 → fireplace frame #34 | ✓ | ✗ (ceiling area #33 named wrong, fireplace frame #34 named wrong) | - | next to [0-9] | + only Qwen-7B | - | - |
| fireplace frame #34 → flower vase #35 | ✓ | ✗ (fireplace frame #34 named wrong, flower vase #35 named wrong) | - | behind [0-9] | + only Qwen-7B | - | - |
| flower vase #35 → vase #36 | ✓ | ✗ (flower vase #35 named wrong, vase #36 named wrong) | - | on top of [0-9] | + only Qwen-7B | - | - |
| vase #36 → home decor #37 | ✓ | ✗ (vase #36 named wrong) | - | next to [0-9] | + only Qwen-7B | - | - |
| home decor #37 → home decor #38 | ✓ | ✓ | - | on top of [0-9] | + only Qwen-7B | - | - |
| home decor #38 → socket #39 | ✓ | ✗ (socket #39 named wrong) | - | next to [0-9] | + only Qwen-7B | - | - |
| socket #39 → ground #0 | ✓ | ✗ (socket #39 named wrong) | - | on top of [0-9] | + only Qwen-7B | - | - |


## sav_053005

18.71 s video; humans: 29 objects, 29 relations on 26 pairs; Qwen-7B: 0 relations on 0 pairs (answer cut off at the token limit, read up to there).

**Masks given to Qwen-7B:** 29 of 29 objects

**Pairs:** 0 in both, 26 missed by Qwen-7B, 0 reversed, 0 with an object Qwen-7B was not given, 0 only Qwen-7B

**Objects: 7/29 right**

| id | human label | mask given to Qwen-7B? | Qwen-7B label | verdict | right (lenient) |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | woman | hypernym/hyponym | ✓ |
| 1 | carpet | yes (object 2) | floor | semantic overlap | ✓ |
| 2 | sofa | yes (object 3) | chair | semantic overlap | ✓ |
| 3 | table | yes (object 4) | couch | mismatch | ✗ |
| 4 | curtain | yes (object 5) | window | semantic overlap | ✓ |
| 5 | windows | yes (object 6) | chandelier | mismatch | ✗ |
| 6 | lights | yes (object 7) | lamp | hypernym/hyponym | ✓ |
| 7 | chair | yes (object 8) | door | mismatch | ✗ |
| 8 | wall panel | yes (object 9) | pillow | mismatch | ✗ |
| 9 | floor | yes (object 10) | wall | mismatch | ✗ |
| 10 | pillars | yes (object 11) | curtain | mismatch | ✗ |
| 11 | fountain | yes (object 12) | hotel lobby | mismatch | ✗ |
| 12 | desk | yes (object 13) | hotel reception desk | hypernym/hyponym | ✓ |
| 13 | sofa | yes (object 14) | hotel sign | mismatch | ✗ |
| 14 | lights | yes (object 15) | hotel entrance | mismatch | ✗ |
| 15 | background | yes (object 16) | hotel elevator | mismatch | ✗ |
| 16 | screen | yes (object 17) | hotel lobby carpet | mismatch | ✗ |
| 17 | chandelier lights | yes (object 18) | hotel seating area | mismatch | ✗ |
| 18 | door | yes (object 19) | hotel receptionist | mismatch | ✗ |
| 19 | oerson | yes (object 20) | hotel guest | hypernym/hyponym | ✓ |
| 20 | pillar | yes (object 21) | hotel security guard | mismatch | ✗ |
| 21 | reflected lights | yes (object 22) | hotel staff | mismatch | ✗ |
| 22 | bag | yes (object 23) | hotel decoration | mismatch | ✗ |
| 23 | head | yes (object 24) | hotel lighting | mismatch | ✗ |
| 24 | legs | yes (object 25) | hotel reception desk chair | mismatch | ✗ |
| 25 | entrance | yes (object 26) | hotel reception desk table | mismatch | ✗ |
| 26 | balcony | yes (object 27) | hotel reception desk lamp | mismatch | ✗ |
| 27 | bench | yes (object 28) | hotel reception desk phone | mismatch | ✗ |
| 28 | sign | yes (object 29) | hotel reception desk computer | mismatch | ✗ |

**Relations, pair by pair**

| pair (subject → object) | both masks given? | both objects named right? | human said | Qwen-7B said | pair | relation right? (lenient, tIoU > 0.5) | triplet right? |
|---|---|---|---|---|---|---|---|
| person #0 → carpet #1 | ✓ | ✓ | moves on [0-9, 11-19]; on [0-9, 11-19] | - | ✗ Qwen-7B missed this pair | - - | - - |
| person #0 → table #3 | ✓ | ✗ (table #3 named wrong) | in front of [0-9, 11-19] | - | ✗ Qwen-7B missed this pair | - | - |
| person #0 → curtain #4 | ✓ | ✓ | in front of [0-9, 11-19] | - | ✗ Qwen-7B missed this pair | - | - |
| person #0 → windows #5 | ✓ | ✗ (windows #5 named wrong) | in front of [0-9, 11-19] | - | ✗ Qwen-7B missed this pair | - | - |
| person #0 → chair #7 | ✓ | ✗ (chair #7 named wrong) | in front of [0-9, 11-19] | - | ✗ Qwen-7B missed this pair | - | - |
| person #0 → wall panel #8 | ✓ | ✗ (wall panel #8 named wrong) | in front of [0-9, 11-19] | - | ✗ Qwen-7B missed this pair | - | - |
| person #0 → bag #22 | ✓ | ✗ (bag #22 named wrong) | poses with [0-9, 11-19]; carries [0-9, 11-19] | - | ✗ Qwen-7B missed this pair | - - | - - |
| carpet #1 → floor #9 | ✓ | ✗ (floor #9 named wrong) | on [0-5, 9-10, 11-12] | - | ✗ Qwen-7B missed this pair | - | - |
| sofa #2 → carpet #1 | ✓ | ✓ | on [0-8, 12-15, 18-19] | - | ✗ Qwen-7B missed this pair | - | - |
| table #3 → carpet #1 | ✓ | ✗ (table #3 named wrong) | on [0-9, 11-19] | - | ✗ Qwen-7B missed this pair | - | - |
| table #3 → chair #7 | ✓ | ✗ (table #3 named wrong, chair #7 named wrong) | in front of [0-9, 11-19] | - | ✗ Qwen-7B missed this pair | - | - |
| curtain #4 → windows #5 | ✓ | ✗ (windows #5 named wrong) | in front of [0-9, 11-19] | - | ✗ Qwen-7B missed this pair | - | - |
| chair #7 → carpet #1 | ✓ | ✗ (chair #7 named wrong) | on [0-9, 11-19] | - | ✗ Qwen-7B missed this pair | - | - |
| wall panel #8 → curtain #4 | ✓ | ✗ (wall panel #8 named wrong) | below [0-9, 11-19] | - | ✗ Qwen-7B missed this pair | - | - |
| pillars #10 → floor #9 | ✓ | ✗ (pillars #10 named wrong, floor #9 named wrong) | on [9-11] | - | ✗ Qwen-7B missed this pair | - | - |
| fountain #11 → floor #9 | ✓ | ✗ (fountain #11 named wrong, floor #9 named wrong) | on [10-12] | - | ✗ Qwen-7B missed this pair | - | - |
| desk #12 → floor #9 | ✓ | ✗ (floor #9 named wrong) | on [9-10] | - | ✗ Qwen-7B missed this pair | - | - |
| desk #12 → pillar #20 | ✓ | ✗ (pillar #20 named wrong) | in front of [8.5-10.5] | - | ✗ Qwen-7B missed this pair | - | - |
| sofa #13 → carpet #1 | ✓ | ✗ (sofa #13 named wrong) | on [9-10] | - | ✗ Qwen-7B missed this pair | - | - |
| lights #14 → desk #12 | ✓ | ✗ (lights #14 named wrong) | above [8.5-10.5] | - | ✗ Qwen-7B missed this pair | - | - |
| door #18 → floor #9 | ✓ | ✗ (door #18 named wrong, floor #9 named wrong) | above [8.5-11] | - | ✗ Qwen-7B missed this pair | - | - |
| bag #22 → person #0 | ✓ | ✗ (bag #22 named wrong) | moves with [0-9, 11-19]; near [0-9, 11-19] | - | ✗ Qwen-7B missed this pair | - - | - - |
| head #23 → legs #24 | ✓ | ✗ (head #23 named wrong, legs #24 named wrong) | above [0-9, 11-19] | - | ✗ Qwen-7B missed this pair | - | - |
| legs #24 → carpet #1 | ✓ | ✗ (legs #24 named wrong) | on [0-9, 11-19] | - | ✗ Qwen-7B missed this pair | - | - |
| entrance #25 → floor #9 | ✓ | ✗ (entrance #25 named wrong, floor #9 named wrong) | above [9-11] | - | ✗ Qwen-7B missed this pair | - | - |
| bench #27 → floor #9 | ✓ | ✗ (bench #27 named wrong, floor #9 named wrong) | on [9.5-12] | - | ✗ Qwen-7B missed this pair | - | - |

