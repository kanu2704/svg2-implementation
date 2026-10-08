# svg2test: which object pairs TRASER talks about (10 random videos, seed 0)

TRASER is given the human objects (masks) and writes its own list of relations; it is not told which pairs to describe. Each row is one ordered pair (subject → object) that the humans or TRASER mention.

- **✓ TRASER has this pair**: TRASER wrote at least one relation for the same two objects, same direction
- **✗ TRASER missed this pair**: humans annotated it, TRASER said nothing about these two objects
- **↔ reversed**: TRASER only has the other direction (object → subject); scored as missed
- **⊘ object not given**: one of the two objects was not among the (at most 40) objects TRASER received, so it could not answer; scored as missed, as in the paper's setup
- **+ only TRASER**: TRASER describes a pair the humans did not annotate (ignored by the scores)
- last column, one mark per human relation of the pair: ✓ word right and tIoU > 0.5, ✗ not, ? the judge has not compared the words yet

**Total over these videos:** 285 human pairs, 373 TRASER pairs; 94 in both, 166 missed, 13 reversed, 12 with an object not given, 279 only TRASER.

| video | source | objects right | relations right | triplets right | human pairs | TRASER pairs | pairs in both | missed by TRASER | reversed | object not given | only TRASER |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [1190_UmpN6eLjN8w](#1190_umpn6eljn8w) | vipseg | 6/18 | 7/44 | 3/44 | 40 | 26 | 7 | 31 | 2 | 0 | 19 |
| [339_j2gELsuQ3Cg](#339_j2gelsuq3cg) | vipseg | 7/14 | 0/20 | 0/20 | 17 | 14 | 3 | 14 | 0 | 0 | 11 |
| [465_nbJ_SLWUDxk](#465_nbj_slwudxk) | vipseg | 32/39 | 4/24 | 2/24 | 21 | 47 | 8 | 10 | 3 | 0 | 39 |
| [700_zkhPzSZcRtQ](#700_zkhpzszcrtq) | vipseg | 10/24 | 8/41 | 6/41 | 39 | 41 | 9 | 28 | 2 | 0 | 32 |
| [722__ajUvCkhVcI](#722__ajuvckhvci) | vipseg | 5/18 | 4/39 | 0/39 | 32 | 30 | 9 | 21 | 2 | 0 | 21 |
| [744_1X6KvqPjk6I](#744_1x6kvqpjk6i) | vipseg | 15/32 | 4/26 | 3/26 | 23 | 36 | 10 | 11 | 2 | 0 | 26 |
| [888_BS3hab7EtAg](#888_bs3hab7etag) | vipseg | 9/26 | 18/39 | 5/39 | 36 | 61 | 21 | 13 | 2 | 0 | 40 |
| [914_f4HgijyAEYs](#914_f4hgijyaeys) | vipseg | 7/19 | 8/21 | 5/21 | 19 | 41 | 9 | 10 | 0 | 0 | 32 |
| [976_U19VojbI0h4](#976_u19vojbi0h4) | vipseg | 21/65 | 7/36 | 2/36 | 32 | 43 | 9 | 11 | 0 | 12 | 34 |
| [sav_053005](#sav_053005) | sav | 12/29 | 6/29 | 4/29 | 26 | 34 | 9 | 17 | 0 | 0 | 25 |

## 1190_UmpN6eLjN8w

10.17 s video; humans: 18 objects, 44 relations on 40 pairs; TRASER: 28 relations on 26 pairs.

**Pairs:** 7 in both, 31 missed by TRASER, 2 reversed, 0 with an object TRASER was not given, 19 only TRASER

**Objects: 6/18 right**

| id | human label | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|
| 0 | plane | airplane | not judged yet | ? |
| 1 | person | person | identical | ✓ |
| 2 | person | hat (uncertain) | mismatch | ✗ |
| 3 | ocean | water | hypernym/hyponym | ✓ |
| 4 | person | person | identical | ✓ |
| 5 | sky | airplane | not judged yet | ? |
| 6 | hair | hair | identical | ✓ |
| 7 | face | person | hypernym/hyponym | ✓ |
| 8 | cap | hat (uncertain) | hypernym/hyponym | ✓ |
| 9 | neck | person | mismatch | ✗ |
| 10 | hair | person | mismatch | ✗ |
| 11 | shirt | hat (uncertain) | not judged yet | ? |
| 12 | wing | airplane | not judged yet | ? |
| 13 | wing | airplane | not judged yet | ? |
| 14 | tyres | airplane | not judged yet | ? |
| 15 | tyres | airplane | not judged yet | ? |
| 16 | nose | airplane | mismatch | ✗ |
| 17 | hair | person | mismatch | ✗ |

**Relations, pair by pair**

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| plane #0 → person #1 | above [0-11]; approaches [0-11] | above [0-11] | ✓ TRASER has this pair | ✓ ? |
| plane #0 → person #2 | approaches [0-3, 6-8]; above [0-3, 6-8] | - | ✗ TRASER missed this pair | - - |
| plane #0 → ocean #3 | above [0-11] | moving left relative to [0-11]; flying over [0-11]; above [0-11] | ✓ TRASER has this pair | ✓ |
| plane #0 → person #4 | approaches [3-11]; above [2.5-11] | above [0-1, 3-11] | ✓ TRASER has this pair | ? ✓ |
| plane #0 → sky #5 | moves across [0-11]; in front of [0-11] | - | ✗ TRASER missed this pair | - - |
| plane #0 → wing #12 | has [0-11] | - | ✗ TRASER missed this pair | - |
| plane #0 → wing #13 | has [0-11] | - | ✗ TRASER missed this pair | - |
| plane #0 → tyres #14 | has [0-11] | - | ✗ TRASER missed this pair | - |
| plane #0 → tyres #15 | has [0-11] | - | ✗ TRASER missed this pair | - |
| plane #0 → nose #16 | has [0-11] | - | ✗ TRASER missed this pair | - |
| person #1 → plane #0 | looking at [2.5-5, 6.5-10] | looking at [0-11] | ✓ TRASER has this pair | ✓ |
| person #1 → ocean #3 | in front of [0-11] | in front of [0-11] | ✓ TRASER has this pair | ✓ |
| person #1 → sky #5 | in front of [0-11] | - | ✗ TRASER missed this pair | - |
| person #1 → hair #6 | has [0-11] | - | ↔ TRASER has it reversed | - |
| person #1 → face #7 | has [0-11] | - | ✗ TRASER missed this pair | - |
| person #2 → plane #0 | looking at [0-3, 6-8] | - | ✗ TRASER missed this pair | - |
| person #2 → ocean #3 | in front of [0-3, 6-8] | - | ✗ TRASER missed this pair | - |
| person #2 → sky #5 | in front of [0-3, 6-8] | - | ✗ TRASER missed this pair | - |
| person #2 → cap #8 | wears [0-2, 6-8] | - | ✗ TRASER missed this pair | - |
| person #2 → shirt #11 | wears [0-3, 6-8] | - | ✗ TRASER missed this pair | - |
| ocean #3 → sky #5 | in front of [0-11] | - | ✗ TRASER missed this pair | - |
| person #4 → plane #0 | looking at [3-11] | - | ↔ TRASER has it reversed | - |
| person #4 → ocean #3 | in front of [3-11] | in front of [0-1, 3-11] | ✓ TRASER has this pair | ✓ |
| person #4 → sky #5 | in front of [3-11] | - | ✗ TRASER missed this pair | - |
| sky #5 → ocean #3 | above [0-11] | - | ✗ TRASER missed this pair | - |
| hair #6 → person #1 | on [0-11] | on [0-11] | ✓ TRASER has this pair | ✓ |
| hair #6 → face #7 | above [0-11] | - | ✗ TRASER missed this pair | - |
| face #7 → person #1 | on [0-11] | - | ✗ TRASER missed this pair | - |
| cap #8 → person #2 | on [0-2, 6-7] | - | ✗ TRASER missed this pair | - |
| neck #9 → person #2 | on [0-2, 6-8] | - | ✗ TRASER missed this pair | - |
| hair #10 → person #2 | on [0-2.5, 6-8] | - | ✗ TRASER missed this pair | - |
| shirt #11 → person #2 | on [0-2, 6-7] | - | ✗ TRASER missed this pair | - |
| wing #12 → plane #0 | on [0-11] | - | ✗ TRASER missed this pair | - |
| wing #13 → plane #0 | on [0-11] | - | ✗ TRASER missed this pair | - |
| tyres #14 → plane #0 | on [0-11] | - | ✗ TRASER missed this pair | - |
| tyres #14 → wing #12 | below [0-11] | - | ✗ TRASER missed this pair | - |
| tyres #15 → plane #0 | on [0-11] | - | ✗ TRASER missed this pair | - |
| tyres #15 → wing #12 | below [0-11] | - | ✗ TRASER missed this pair | - |
| nose #16 → plane #0 | on [0-11] | - | ✗ TRASER missed this pair | - |
| hair #17 → person #4 | on [3-11] | - | ✗ TRASER missed this pair | - |
| plane #0 → hair #6 | - | above [0-11] | + only TRASER | - |
| plane #0 → face #7 | - | above [0-11] | + only TRASER | - |
| plane #0 → neck #9 | - | above [0-1] | + only TRASER | - |
| plane #0 → hair #10 | - | above [0-1] | + only TRASER | - |
| plane #0 → hair #17 | - | above [0-1, 3-11] | + only TRASER | - |
| face #7 → ocean #3 | - | in front of [0-11] | + only TRASER | - |
| neck #9 → ocean #3 | - | in front of [0-1] | + only TRASER | - |
| hair #10 → ocean #3 | - | in front of [0-1] | + only TRASER | - |
| wing #12 → person #1 | - | above [0-11] | + only TRASER | - |
| wing #12 → ocean #3 | - | above [0-11] | + only TRASER | - |
| wing #13 → person #1 | - | above [0-11] | + only TRASER | - |
| wing #13 → ocean #3 | - | above [0-11] | + only TRASER | - |
| tyres #14 → person #1 | - | above [0-11] | + only TRASER | - |
| tyres #14 → ocean #3 | - | above [0-11] | + only TRASER | - |
| tyres #15 → person #1 | - | above [0-11] | + only TRASER | - |
| tyres #15 → ocean #3 | - | above [0-11] | + only TRASER | - |
| nose #16 → person #1 | - | above [0-11] | + only TRASER | - |
| nose #16 → ocean #3 | - | above [0-11] | + only TRASER | - |
| hair #17 → ocean #3 | - | in front of [0-1, 3-11] | + only TRASER | - |


## 339_j2gELsuQ3Cg

5.0 s video; humans: 14 objects, 20 relations on 17 pairs; TRASER: 19 relations on 14 pairs.

**Pairs:** 3 in both, 14 missed by TRASER, 0 reversed, 0 with an object TRASER was not given, 11 only TRASER

**Objects: 7/14 right**

| id | human label | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|
| 0 | person | person | identical | ✓ |
| 1 | clothes | garment (uncertain) | synonym | ✓ |
| 2 | clothes | garment (uncertain) | synonym | ✓ |
| 3 | clothes | garment (uncertain) | synonym | ✓ |
| 4 | closet | door frame (uncertain) | not judged yet | ? |
| 5 | closet divider | pole (uncertain) | not judged yet | ? |
| 6 | closet divider | door frame (uncertain) | not judged yet | ? |
| 7 | closet shelf | drawer (uncertain) | not judged yet | ? |
| 8 | hair | hair | identical | ✓ |
| 9 | face | person | hypernym/hyponym | ✓ |
| 10 | hand | arm | semantic overlap | ✓ |
| 11 | shoulder | tank top | not judged yet | ? |
| 12 | shirt | tank top | not judged yet | ? |
| 13 | plywood | fabric (uncertain) | not judged yet | ? |

**Relations, pair by pair**

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| person #0 → clothes #1 | looks at [0-6]; touches [0-3]; moves leftward [2-5] | - | ✗ TRASER missed this pair | - - - |
| person #0 → closet #4 | in front of [0-5]; browses [0-6] | - | ✗ TRASER missed this pair | - - |
| person #0 → shirt #12 | wears [0-5] | wearing [0-6]; in front of [0-6] | ✓ TRASER has this pair | ? |
| clothes #1 → person #0 | behind [0-6] | - | ✗ TRASER missed this pair | - |
| clothes #1 → closet #4 | in [0-6] | - | ✗ TRASER missed this pair | - |
| clothes #2 → person #0 | behind [0-5.5] | - | ✗ TRASER missed this pair | - |
| clothes #3 → person #0 | behind [0-5] | - | ✗ TRASER missed this pair | - |
| closet divider #5 → person #0 | behind [1.5-3.5] | - | ✗ TRASER missed this pair | - |
| closet divider #6 → person #0 | behind [0-5] | - | ✗ TRASER missed this pair | - |
| closet shelf #7 → closet divider #6 | below [0-5] | - | ✗ TRASER missed this pair | - |
| hair #8 → closet #4 | in front of [0-6] | - | ✗ TRASER missed this pair | - |
| face #9 → closet #4 | in front of [0-5] | - | ✗ TRASER missed this pair | - |
| hand #10 → clothes #1 | in front of [0-5] | - | ✗ TRASER missed this pair | - |
| hand #10 → closet #4 | in front of [0-2.5, 3-5] | - | ✗ TRASER missed this pair | - |
| hand #10 → face #9 | below [0-2.5, 4.5-6] | - | ✗ TRASER missed this pair | - |
| shoulder #11 → face #9 | below [0-5] | overlapping [0-6] | ✓ TRASER has this pair | ? |
| shirt #12 → face #9 | below [0-5] | overlapping [0-6] | ✓ TRASER has this pair | ? |
| person #0 → hair #8 | - | has [0-6]; in front of [0-6] | + only TRASER | - |
| person #0 → face #9 | - | looking at [0-6]; in front of [0-6] | + only TRASER | - |
| person #0 → hand #10 | - | has [0-6]; in front of [0-6] | + only TRASER | - |
| person #0 → shoulder #11 | - | wearing [0-6]; in front of [0-6] | + only TRASER | - |
| hair #8 → face #9 | - | overlapping [0-6] | + only TRASER | - |
| hair #8 → shoulder #11 | - | overlapping [0-6] | + only TRASER | - |
| hair #8 → shirt #12 | - | overlapping [0-6] | + only TRASER | - |
| hand #10 → hair #8 | - | overlapping [0-6] | + only TRASER | - |
| hand #10 → shoulder #11 | - | overlapping [0-6] | + only TRASER | - |
| hand #10 → shirt #12 | - | overlapping [0-6] | + only TRASER | - |
| shoulder #11 → shirt #12 | - | overlapping [0-6] | + only TRASER | - |


## 465_nbJ_SLWUDxk

7.5 s video; humans: 39 objects, 24 relations on 21 pairs; TRASER: 52 relations on 47 pairs.

**Pairs:** 8 in both, 10 missed by TRASER, 3 reversed, 0 with an object TRASER was not given, 39 only TRASER

**Objects: 32/39 right**

| id | human label | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|
| 0 | person | person | identical | ✓ |
| 1 | person | person | identical | ✓ |
| 2 | person | person | identical | ✓ |
| 3 | person | person | identical | ✓ |
| 4 | person | person | identical | ✓ |
| 5 | person | person | identical | ✓ |
| 6 | person | person | identical | ✓ |
| 7 | person | child | hypernym/hyponym | ✓ |
| 8 | person | person | identical | ✓ |
| 9 | person | child | hypernym/hyponym | ✓ |
| 10 | person | person | identical | ✓ |
| 11 | person | person | identical | ✓ |
| 12 | person | person | identical | ✓ |
| 13 | person | person | identical | ✓ |
| 14 | person | jersey (uncertain) | mismatch | ✗ |
| 15 | person | person | identical | ✓ |
| 16 | person | person | identical | ✓ |
| 17 | person | person | identical | ✓ |
| 18 | person | person | identical | ✓ |
| 19 | person | person | identical | ✓ |
| 20 | person | person | identical | ✓ |
| 21 | person | person | identical | ✓ |
| 22 | person | person | identical | ✓ |
| 23 | person | person | identical | ✓ |
| 24 | person | person | identical | ✓ |
| 25 | person | person | identical | ✓ |
| 26 | person | person | identical | ✓ |
| 27 | person | person | identical | ✓ |
| 28 | person | person | identical | ✓ |
| 29 | ground | person | mismatch | ✗ |
| 30 | buildings | hill | mismatch | ✗ |
| 31 | sky | streetlight | not judged yet | ? |
| 32 | river | boat | not judged yet | ? |
| 33 | light | streetlight | hypernym/hyponym | ✓ |
| 34 | light | streetlight | hypernym/hyponym | ✓ |
| 35 | saxophone | saxophone | identical | ✓ |
| 36 | shoes | roller skates | not judged yet | ? |
| 37 | hat | hat | identical | ✓ |
| 38 | suit | suit jacket | not judged yet | ? |

**Relations, pair by pair**

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| person #0 → person #1 | performs for [0-8]; approaches [0-5] | in front of [0-9] | ✓ TRASER has this pair | ? ? |
| person #0 → person #7 | in front of [0-8] | in front of [0-9] | ✓ TRASER has this pair | ✓ |
| person #0 → ground #29 | on [0-8] | - | ✗ TRASER missed this pair | - |
| person #0 → buildings #30 | in front of [0-8] | in front of [0-9] | ✓ TRASER has this pair | ✓ |
| person #0 → hat #37 | wears [0-8] | wearing [0-9] | ✓ TRASER has this pair | ? |
| person #0 → suit #38 | wears [0-8] | wearing [0-9] | ✓ TRASER has this pair | ? |
| person #1 → person #0 | in front of [0-8]; looks at [5-8] | - | ↔ TRASER has it reversed | - - |
| person #1 → person #2 | dances with [0-8]; in front of [0-8] | - | ✗ TRASER missed this pair | - - |
| person #1 → ground #29 | on [0-8] | - | ✗ TRASER missed this pair | - |
| person #1 → buildings #30 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| person #2 → ground #29 | on [0-8] | - | ✗ TRASER missed this pair | - |
| person #2 → buildings #30 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| person #2 → shoes #36 | wears [0-6] | - | ✗ TRASER missed this pair | - |
| person #24 → person #0 | looks at [0-8] | - | ↔ TRASER has it reversed | - |
| sky #31 → buildings #30 | above [0-8] | in front of [0-9] | ✓ TRASER has this pair | ? |
| river #32 → person #0 | behind [0-8] | - | ↔ TRASER has it reversed | - |
| light #33 → ground #29 | above [0-8] | - | ✗ TRASER missed this pair | - |
| light #34 → ground #29 | above [0-8] | - | ✗ TRASER missed this pair | - |
| shoes #36 → person #2 | on [0-6.5] | - | ✗ TRASER missed this pair | - |
| hat #37 → person #0 | on [0-8] | on [0-9] | ✓ TRASER has this pair | ✓ |
| suit #38 → person #0 | on [0-8] | on [0-9] | ✓ TRASER has this pair | ✓ |
| person #0 → person #2 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #3 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #4 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #5 | - | in front of [0-4] | + only TRASER | - |
| person #0 → person #6 | - | in front of [0-4] | + only TRASER | - |
| person #0 → person #8 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #9 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #10 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #11 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #12 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #13 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #15 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #16 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #17 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #18 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #19 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #20 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #21 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #22 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #23 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #24 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #25 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #26 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #27 | - | in front of [0-9] | + only TRASER | - |
| person #0 → person #28 | - | in front of [0-9] | + only TRASER | - |
| person #0 → sky #31 | - | in front of [0-9] | + only TRASER | - |
| person #0 → river #32 | - | in front of [0-9]; in front of [0-9] | + only TRASER | - |
| person #0 → light #33 | - | in front of [0-9] | + only TRASER | - |
| person #0 → light #34 | - | in front of [0-9] | + only TRASER | - |
| person #0 → saxophone #35 | - | holding [0-9]; playing [0-9]; looking at [0-9]; performing with [0-9] | + only TRASER | - |
| river #32 → buildings #30 | - | in front of [0-9] | + only TRASER | - |
| light #33 → buildings #30 | - | in front of [0-9] | + only TRASER | - |
| light #34 → buildings #30 | - | in front of [0-9] | + only TRASER | - |
| saxophone #35 → person #0 | - | in front of [0-9]; below [0-9] | + only TRASER | - |
| saxophone #35 → buildings #30 | - | in front of [0-9] | + only TRASER | - |
| saxophone #35 → river #32 | - | in front of [0-9] | + only TRASER | - |
| shoes #36 → person #0 | - | below [0-9] | + only TRASER | - |
| shoes #36 → saxophone #35 | - | below [0-9] | + only TRASER | - |
| hat #37 → suit #38 | - | above [0-9] | + only TRASER | - |


## 700_zkhPzSZcRtQ

22.67 s video; humans: 24 objects, 41 relations on 39 pairs; TRASER: 116 relations on 41 pairs.

**Pairs:** 9 in both, 28 missed by TRASER, 2 reversed, 0 with an object TRASER was not given, 32 only TRASER

**Objects: 10/24 right**

| id | human label | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|
| 0 | mat | mat | identical | ✓ |
| 1 | mat | crossbar (uncertain) | mismatch | ✗ |
| 2 | floor | person | mismatch | ✗ |
| 3 | pole | pole | identical | ✓ |
| 4 | man | person | hypernym/hyponym | ✓ |
| 5 | bat | handbag | not judged yet | ? |
| 6 | wall | net | not judged yet | ? |
| 7 | ball cart | shopping cart | semantic overlap | ✓ |
| 8 | stripe or mat | mat | not judged yet | ? |
| 9 | stripe | mat | not judged yet | ? |
| 10 | stripe | tape measure (uncertain) | not judged yet | ? |
| 11 | wall poster | vent (uncertain) | not judged yet | ? |
| 12 | wall poster | vent (uncertain) | not judged yet | ? |
| 13 | wall poster | vent (uncertain) | not judged yet | ? |
| 14 | wall poster | vent (uncertain) | not judged yet | ? |
| 15 | strip | tape measure | not judged yet | ? |
| 16 | posters | basketball backboard | not judged yet | ? |
| 17 | shoe | shoe | identical | ✓ |
| 18 | shoe | shoe | identical | ✓ |
| 19 | hat | baseball cap | hypernym/hyponym | ✓ |
| 20 | hoodie | jacket | hypernym/hyponym | ✓ |
| 21 | pants | trousers (uncertain) | synonym | ✓ |
| 22 | ball cart | shopping cart | semantic overlap | ✓ |
| 23 | poster | banner | not judged yet | ? |

**Relations, pair by pair**

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| mat #0 → floor #2 | on [0-23] | - | ✗ TRASER missed this pair | - |
| mat #0 → wall #6 | in front of [0-23] | - | ✗ TRASER missed this pair | - |
| mat #1 → mat #0 | behind [0-23] | - | ✗ TRASER missed this pair | - |
| mat #1 → floor #2 | on [0-23] | - | ✗ TRASER missed this pair | - |
| pole #3 → floor #2 | on [0-23] | - | ✗ TRASER missed this pair | - |
| pole #3 → wall #6 | in front of [0-23] | - | ✗ TRASER missed this pair | - |
| man #4 → mat #0 | approaching [18-21]; moving away from [20-23] | moving relative to [0-24]; in front of [0-24] | ✓ TRASER has this pair | ? ? |
| man #4 → floor #2 | on [0-23]; walking on [18-23] | - | ✗ TRASER missed this pair | - - |
| man #4 → bat #5 | holding [0-23] | holding [0-24] | ✓ TRASER has this pair | ✓ |
| man #4 → wall #6 | in front of [0-23] | in front of [0-24] | ✓ TRASER has this pair | ✓ |
| man #4 → ball cart #7 | in front of [0-23] | moving relative to [0-24]; in front of [0-24] | ✓ TRASER has this pair | ✓ |
| man #4 → shoe #17 | wearing [0-23] | wearing [0-24] | ✓ TRASER has this pair | ✓ |
| man #4 → shoe #18 | wearing [0-23] | wearing [0-24] | ✓ TRASER has this pair | ✓ |
| man #4 → hat #19 | wearing [0-23] | wearing [0-24]; in front of [0-24] | ✓ TRASER has this pair | ✓ |
| man #4 → hoodie #20 | wearing [0-23] | wearing [0-24]; in front of [0-24] | ✓ TRASER has this pair | ✓ |
| man #4 → pants #21 | wearing [0-23] | - | ✗ TRASER missed this pair | - |
| bat #5 → floor #2 | above [0-23] | - | ✗ TRASER missed this pair | - |
| bat #5 → wall #6 | in front of [0-23] | - | ✗ TRASER missed this pair | - |
| ball cart #7 → floor #2 | on [0-23] | - | ✗ TRASER missed this pair | - |
| ball cart #7 → wall #6 | in front of [0-23] | - | ✗ TRASER missed this pair | - |
| stripe or mat #8 → floor #2 | on [0-23] | - | ✗ TRASER missed this pair | - |
| stripe #9 → floor #2 | on [0-23] | - | ✗ TRASER missed this pair | - |
| stripe #10 → floor #2 | on [0-23] | - | ✗ TRASER missed this pair | - |
| wall poster #11 → wall #6 | on [0-23] | - | ✗ TRASER missed this pair | - |
| wall poster #12 → wall #6 | on [0-23] | - | ✗ TRASER missed this pair | - |
| wall poster #13 → wall #6 | on [0-23] | - | ✗ TRASER missed this pair | - |
| wall poster #14 → wall #6 | on [0-23] | - | ✗ TRASER missed this pair | - |
| posters #16 → wall #6 | on [0-23] | - | ✗ TRASER missed this pair | - |
| shoe #17 → floor #2 | on [0-23] | - | ✗ TRASER missed this pair | - |
| shoe #18 → floor #2 | on [0-23] | - | ✗ TRASER missed this pair | - |
| hat #19 → man #4 | on [0-23] | - | ↔ TRASER has it reversed | - |
| hat #19 → hoodie #20 | above [0-23] | above [0-24] | ✓ TRASER has this pair | ✓ |
| hoodie #20 → man #4 | on [0-23] | - | ↔ TRASER has it reversed | - |
| hoodie #20 → pants #21 | above [0-23] | - | ✗ TRASER missed this pair | - |
| pants #21 → man #4 | on [0-23] | - | ✗ TRASER missed this pair | - |
| pants #21 → shoe #17 | above [0-23] | - | ✗ TRASER missed this pair | - |
| pants #21 → shoe #18 | above [0-23] | - | ✗ TRASER missed this pair | - |
| poster #23 → wall #6 | on [0-23] | - | ✗ TRASER missed this pair | - |
| poster #23 → ball cart #7 | above [0-23] | - | ✗ TRASER missed this pair | - |
| man #4 → pole #3 | - | moving relative to [0-24]; in front of [0-24] | + only TRASER | - |
| man #4 → stripe or mat #8 | - | in front of [0-24] | + only TRASER | - |
| man #4 → stripe #9 | - | in front of [0-24] | + only TRASER | - |
| man #4 → strip #15 | - | moving relative to [0-24]; in front of [0-24] | + only TRASER | - |
| man #4 → posters #16 | - | moving relative to [0-24]; in front of [0-24] | + only TRASER | - |
| man #4 → ball cart #22 | - | moving relative to [0-24]; in front of [0-24] | + only TRASER | - |
| man #4 → poster #23 | - | moving relative to [0-24]; in front of [0-24] | + only TRASER | - |
| bat #5 → man #4 | - | overlapping [0-24] | + only TRASER | - |
| shoe #17 → mat #0 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| shoe #17 → mat #1 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| shoe #17 → pole #3 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| shoe #17 → ball cart #7 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| shoe #17 → stripe or mat #8 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| shoe #17 → stripe #9 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| shoe #17 → strip #15 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| shoe #17 → posters #16 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| shoe #17 → ball cart #22 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| shoe #17 → poster #23 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| shoe #18 → mat #0 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| shoe #18 → mat #1 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| shoe #18 → pole #3 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| shoe #18 → ball cart #7 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| shoe #18 → stripe or mat #8 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| shoe #18 → stripe #9 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| shoe #18 → strip #15 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| shoe #18 → posters #16 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| shoe #18 → ball cart #22 | - | in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| shoe #18 → poster #23 | - | in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24]; in front of [0-24] | + only TRASER | - |
| hat #19 → shoe #17 | - | above [0-24] | + only TRASER | - |
| hat #19 → shoe #18 | - | above [0-24] | + only TRASER | - |
| hoodie #20 → shoe #17 | - | above [0-24] | + only TRASER | - |
| hoodie #20 → shoe #18 | - | above [0-24] | + only TRASER | - |


## 722__ajUvCkhVcI

22.67 s video; humans: 18 objects, 39 relations on 32 pairs; TRASER: 38 relations on 30 pairs.

**Pairs:** 9 in both, 21 missed by TRASER, 2 reversed, 0 with an object TRASER was not given, 21 only TRASER

**Objects: 5/18 right**

| id | human label | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|
| 0 | baby | child | hypernym/hyponym | ✓ |
| 1 | baby | child | hypernym/hyponym | ✓ |
| 2 | baby | person | hypernym/hyponym | ✓ |
| 3 | ball pit | ball pit | identical | ✓ |
| 4 | side of a cage | net | not judged yet | ? |
| 5 | side of a cage | net | not judged yet | ? |
| 6 | rope | pole (uncertain) | not judged yet | ? |
| 7 | rope | pole (uncertain) | not judged yet | ? |
| 8 | shirt | jersey (uncertain) | not judged yet | ? |
| 9 | head | child | mismatch | ✗ |
| 10 | short | shorts (uncertain) | not judged yet | ? |
| 11 | shirt | jersey (uncertain) | not judged yet | ? |
| 12 | top | jersey (uncertain) | not judged yet | ? |
| 13 | skirt | skirt | identical | ✓ |
| 14 | trouser | trousers | not judged yet | ? |
| 15 | legs | sock (uncertain) | mismatch | ✗ |
| 16 | legs | shoe | not judged yet | ? |
| 17 | legs | ball | not judged yet | ? |

**Relations, pair by pair**

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| baby #0 → baby #1 | looking at [8-11]; in front of [0-23] | next to [0-24] | ✓ TRASER has this pair | ✗ ? |
| baby #0 → baby #2 | looking at [13-23] | - | ↔ TRASER has it reversed | - |
| baby #0 → ball pit #3 | inside [0-23]; playing with [0-23] | in [0-24] | ✓ TRASER has this pair | ? ? |
| baby #0 → side of a cage #4 | in front of [0-23] | in front of [0-24]; below [0-24] | ✓ TRASER has this pair | ✓ |
| baby #0 → side of a cage #5 | in front of [0-23] | in front of [0-24]; below [0-24] | ✓ TRASER has this pair | ✓ |
| baby #0 → shirt #8 | wearing [0-23] | - | ✗ TRASER missed this pair | - |
| baby #0 → short #10 | wearing [0-23] | - | ✗ TRASER missed this pair | - |
| baby #1 → ball pit #3 | inside [0-23] | in [0-24] | ✓ TRASER has this pair | ? |
| baby #1 → side of a cage #4 | in front of [0-23] | in front of [0-24]; below [0-24] | ✓ TRASER has this pair | ✓ |
| baby #1 → side of a cage #5 | holding [8-23]; approaching [1-9]; climbing [8.5-23]; looking at [8-23]; in front of [0-23] | in front of [0-24]; below [0-24] | ✓ TRASER has this pair | ? ? ? ? ✓ |
| baby #1 → shirt #11 | wearing [0-23] | - | ✗ TRASER missed this pair | - |
| baby #1 → trouser #14 | wearing [0-23] | - | ↔ TRASER has it reversed | - |
| baby #2 → ball pit #3 | inside [10-19]; playing with [12-20] | behind [11-24] | ✓ TRASER has this pair | ? ? |
| baby #2 → side of a cage #4 | approaching [12-18] | - | ✗ TRASER missed this pair | - |
| baby #2 → top #12 | wearing [12-21] | - | ✗ TRASER missed this pair | - |
| baby #2 → skirt #13 | wearing [12-23] | - | ✗ TRASER missed this pair | - |
| rope #6 → baby #0 | in front of [0-9] | - | ✗ TRASER missed this pair | - |
| rope #6 → ball pit #3 | in front of [0-9] | - | ✗ TRASER missed this pair | - |
| rope #7 → baby #0 | in front of [0-11] | - | ✗ TRASER missed this pair | - |
| rope #7 → baby #1 | in front of [0-11.5] | - | ✗ TRASER missed this pair | - |
| rope #7 → ball pit #3 | in front of [0-11] | - | ✗ TRASER missed this pair | - |
| shirt #8 → baby #0 | on [0-23] | - | ✗ TRASER missed this pair | - |
| head #9 → shirt #8 | above [0-23] | - | ✗ TRASER missed this pair | - |
| head #9 → short #10 | above [0-23] | - | ✗ TRASER missed this pair | - |
| short #10 → baby #0 | on [0-23] | - | ✗ TRASER missed this pair | - |
| short #10 → shirt #8 | below [0-23] | - | ✗ TRASER missed this pair | - |
| shirt #11 → baby #1 | on [0-23] | - | ✗ TRASER missed this pair | - |
| shirt #11 → trouser #14 | above [0-23] | - | ✗ TRASER missed this pair | - |
| top #12 → baby #2 | on [13-21] | - | ✗ TRASER missed this pair | - |
| skirt #13 → baby #2 | on [12-23] | - | ✗ TRASER missed this pair | - |
| skirt #13 → top #12 | below [12.5-22] | - | ✗ TRASER missed this pair | - |
| trouser #14 → baby #1 | on [0-23] | behind [0-24] | ✓ TRASER has this pair | ✗ |
| baby #0 → head #9 | - | next to [0-24] | + only TRASER | - |
| baby #1 → head #9 | - | next to [0-24] | + only TRASER | - |
| baby #2 → baby #0 | - | behind [11-24] | + only TRASER | - |
| baby #2 → baby #1 | - | behind [11-24] | + only TRASER | - |
| baby #2 → head #9 | - | behind [11-24] | + only TRASER | - |
| head #9 → ball pit #3 | - | in [0-24] | + only TRASER | - |
| head #9 → side of a cage #4 | - | in front of [0-24]; below [0-24] | + only TRASER | - |
| head #9 → side of a cage #5 | - | in front of [0-24]; below [0-24] | + only TRASER | - |
| trouser #14 → baby #0 | - | behind [0-24] | + only TRASER | - |
| trouser #14 → ball pit #3 | - | behind [0-24] | + only TRASER | - |
| trouser #14 → head #9 | - | behind [0-24] | + only TRASER | - |
| legs #16 → baby #0 | - | behind [15-24] | + only TRASER | - |
| legs #16 → baby #1 | - | behind [15-24] | + only TRASER | - |
| legs #16 → ball pit #3 | - | behind [15-24] | + only TRASER | - |
| legs #16 → head #9 | - | behind [15-24] | + only TRASER | - |
| legs #17 → baby #0 | - | near [15-24] | + only TRASER | - |
| legs #17 → baby #1 | - | near [15-24] | + only TRASER | - |
| legs #17 → ball pit #3 | - | in [15-24] | + only TRASER | - |
| legs #17 → side of a cage #4 | - | in front of [15-24]; below [15-24] | + only TRASER | - |
| legs #17 → side of a cage #5 | - | in front of [15-24]; below [15-24] | + only TRASER | - |
| legs #17 → head #9 | - | near [15-24] | + only TRASER | - |


## 744_1X6KvqPjk6I

7.5 s video; humans: 32 objects, 26 relations on 23 pairs; TRASER: 38 relations on 36 pairs.

**Pairs:** 10 in both, 11 missed by TRASER, 2 reversed, 0 with an object TRASER was not given, 26 only TRASER

**Objects: 15/32 right**

| id | human label | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|
| 0 | dog | dog | identical | ✓ |
| 1 | tree | tree | identical | ✓ |
| 2 | plant | plant | identical | ✓ |
| 3 | fence | fence | identical | ✓ |
| 4 | grass | grass | identical | ✓ |
| 5 | plants, soil | soil | not judged yet | ? |
| 6 | plant | plant | identical | ✓ |
| 7 | person | person | identical | ✓ |
| 8 | person | pole | mismatch | ✗ |
| 9 | hat | hat | identical | ✓ |
| 10 | hair | hair | identical | ✓ |
| 11 | tail | tail | identical | ✓ |
| 12 | dog leg | leg | hypernym/hyponym | ✓ |
| 13 | dog leg | dog's leg | identical | ✓ |
| 14 | dog leg | dog's leg | identical | ✓ |
| 15 | head | dog | not judged yet | ? |
| 16 | barricade | wooden plank | mismatch | ✗ |
| 17 | barricade | wooden plank | mismatch | ✗ |
| 18 | stone | wooden block | not judged yet | ? |
| 19 | gardening glove | flowerpot | mismatch | ✗ |
| 20 | fence | roof | not judged yet | ? |
| 21 | pillar | pole | not judged yet | ? |
| 22 | fence | pole | mismatch | ✗ |
| 23 | fence | fence | identical | ✓ |
| 24 | pillar | pole | not judged yet | ? |
| 25 | fence | fence | identical | ✓ |
| 26 | wall | pole | not judged yet | ? |
| 27 | wall | stick | not judged yet | ? |
| 28 | pillar | pole | not judged yet | ? |
| 29 | pillar | pole | not judged yet | ? |
| 30 | fence | pole | mismatch | ✗ |
| 31 | trouser | wooden plank | not judged yet | ? |

**Relations, pair by pair**

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| dog #0 → grass #4 | looking at [0-8] | on [0-9] | ✓ TRASER has this pair | ? |
| dog #0 → barricade #17 | behind [0-8] | - | ✗ TRASER missed this pair | - |
| dog #0 → wall #27 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| grass #4 → barricade #17 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| plants, soil #5 → person #7 | in front of [0-8] | - | ↔ TRASER has it reversed | - |
| plants, soil #5 → barricade #17 | in front of [0-8] | - | ↔ TRASER has it reversed | - |
| person #7 → plants, soil #5 | pulling [0-8]; looking at [0-8]; weeding [0-8]; holding [0-8] | digging [0-9]; looking at [0-9]; gardening [0-9] | ✓ TRASER has this pair | ? ✓ ? ? |
| person #7 → hat #9 | wearing [0-8] | wearing [0-9] | ✓ TRASER has this pair | ✓ |
| person #7 → barricade #17 | behind [0-8] | - | ✗ TRASER missed this pair | - |
| person #7 → wall #27 | in front of [0-8] | holding [0-9] | ✓ TRASER has this pair | ? |
| person #7 → trouser #31 | wearing [0-8] | - | ✗ TRASER missed this pair | - |
| hat #9 → person #7 | on [0-8] | on [0-9] | ✓ TRASER has this pair | ✓ |
| hair #10 → person #7 | on [0-8] | on [0-9] | ✓ TRASER has this pair | ✓ |
| hair #10 → hat #9 | below [0-8] | - | ✗ TRASER missed this pair | - |
| tail #11 → dog #0 | part of [0-8] | attached to [0-9] | ✓ TRASER has this pair | ? |
| dog leg #12 → dog #0 | part of [0-8] | attached to [0-9] | ✓ TRASER has this pair | ? |
| dog leg #13 → dog #0 | part of [0-8] | attached to [0-9] | ✓ TRASER has this pair | ? |
| dog leg #14 → dog #0 | part of [0-8] | attached to [0-9] | ✓ TRASER has this pair | ? |
| head #15 → dog #0 | part of [0-8] | - | ✗ TRASER missed this pair | - |
| barricade #16 → person #7 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| stone #18 → barricade #16 | on [0-8] | - | ✗ TRASER missed this pair | - |
| gardening glove #19 → barricade #17 | on [0-8] | - | ✗ TRASER missed this pair | - |
| trouser #31 → person #7 | on [0-8] | - | ✗ TRASER missed this pair | - |
| dog #0 → tree #1 | - | in front of [0-9] | + only TRASER | - |
| dog #0 → fence #3 | - | in front of [0-9] | + only TRASER | - |
| dog #0 → tail #11 | - | has [0-9] | + only TRASER | - |
| dog #0 → dog leg #12 | - | has [0-9] | + only TRASER | - |
| dog #0 → dog leg #13 | - | has [0-9] | + only TRASER | - |
| dog #0 → dog leg #14 | - | has [0-9] | + only TRASER | - |
| tree #1 → fence #3 | - | behind [0-9] | + only TRASER | - |
| plant #2 → dog #0 | - | in front of [0-9] | + only TRASER | - |
| plant #2 → tree #1 | - | in front of [0-9] | + only TRASER | - |
| plant #2 → fence #3 | - | in front of [0-9] | + only TRASER | - |
| grass #4 → fence #3 | - | in front of [0-9] | + only TRASER | - |
| plant #6 → tree #1 | - | in front of [0-9] | + only TRASER | - |
| plant #6 → fence #3 | - | in front of [0-9] | + only TRASER | - |
| plant #6 → person #7 | - | in front of [0-9] | + only TRASER | - |
| person #7 → tree #1 | - | in front of [0-9] | + only TRASER | - |
| person #7 → fence #3 | - | in front of [0-9] | + only TRASER | - |
| head #15 → tree #1 | - | in front of [0-9] | + only TRASER | - |
| head #15 → fence #3 | - | in front of [0-9] | + only TRASER | - |
| head #15 → grass #4 | - | on [0-9] | + only TRASER | - |
| barricade #16 → plants, soil #5 | - | above [0-9] | + only TRASER | - |
| barricade #17 → plants, soil #5 | - | above [0-9] | + only TRASER | - |
| stone #18 → plants, soil #5 | - | on [0-9] | + only TRASER | - |
| gardening glove #19 → plants, soil #5 | - | on [0-9] | + only TRASER | - |
| fence #20 → fence #3 | - | above [0-9] | + only TRASER | - |
| wall #27 → plants, soil #5 | - | on [0-9] | + only TRASER | - |
| trouser #31 → plants, soil #5 | - | above [0-9] | + only TRASER | - |


## 888_BS3hab7EtAg

7.5 s video; humans: 26 objects, 39 relations on 36 pairs; TRASER: 66 relations on 61 pairs.

**Pairs:** 21 in both, 13 missed by TRASER, 2 reversed, 0 with an object TRASER was not given, 40 only TRASER

**Objects: 9/26 right**

| id | human label | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|
| 0 | barricade | fence | synonym | ✓ |
| 1 | trunk | pole | not judged yet | ? |
| 2 | building | house | hypernym/hyponym | ✓ |
| 3 | trees | tree | not judged yet | ? |
| 4 | trees | tree | not judged yet | ? |
| 5 | trees | tree | not judged yet | ? |
| 6 | grass | grass | identical | ✓ |
| 7 | grass | bush | semantic overlap | ✓ |
| 8 | grass | grass | identical | ✓ |
| 9 | people | car | not judged yet | ? |
| 10 | tiger | tiger | identical | ✓ |
| 11 | cow | bull | synonym | ✓ |
| 12 | trunk | pole | not judged yet | ? |
| 13 | trunk | tree trunk | not judged yet | ? |
| 14 | trunk | tree trunk | not judged yet | ? |
| 15 | trunk | tree trunk | not judged yet | ? |
| 16 | trunk | tree trunk | not judged yet | ? |
| 17 | trunk | tree trunk | not judged yet | ? |
| 18 | trunk | tree trunk | not judged yet | ? |
| 19 | trunk | pole | not judged yet | ? |
| 20 | trunk | pole | not judged yet | ? |
| 21 | legs | leg | identical | ✓ |
| 22 | legs | tail | mismatch | ✗ |
| 23 | tail | tail | identical | ✓ |
| 24 | tiger head | tiger | not judged yet | ? |
| 25 | ram head | cow's ear | not judged yet | ? |

**Relations, pair by pair**

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| trees #3 → barricade #0 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| trees #3 → people #9 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| trees #4 → barricade #0 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| trees #4 → people #9 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| trees #5 → barricade #0 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| trees #5 → people #9 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| grass #7 → grass #6 | on [0-5] | - | ✗ TRASER missed this pair | - |
| grass #8 → grass #6 | on [0-8] | - | ✗ TRASER missed this pair | - |
| people #9 → barricade #0 | behind [0-8] | - | ✗ TRASER missed this pair | - |
| tiger #10 → barricade #0 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| tiger #10 → trees #3 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| tiger #10 → trees #4 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| tiger #10 → trees #5 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| tiger #10 → grass #6 | on [0-8] | moves across [0-8]; on [0-8] | ✓ TRASER has this pair | ✓ |
| tiger #10 → people #9 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| tiger #10 → cow #11 | looking at [0-8]; approaching [0-8] | approaches [0-4]; moves away from [4-8]; passes by [2-5]; near [0-8] | ✓ TRASER has this pair | ? ? |
| tiger #10 → trunk #14 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| tiger #10 → trunk #17 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| cow #11 → barricade #0 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| cow #11 → trees #3 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| cow #11 → trees #4 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| cow #11 → trees #5 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| cow #11 → grass #6 | on [0-8] | moves across [0-8]; on [0-8] | ✓ TRASER has this pair | ✓ |
| cow #11 → people #9 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| cow #11 → tiger #10 | looking at [2-8]; moving away from [2-5]; approaching [5-8] | - | ↔ TRASER has it reversed | - - - |
| cow #11 → trunk #14 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| cow #11 → trunk #17 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| trunk #14 → barricade #0 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| trunk #16 → barricade #0 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| trunk #17 → barricade #0 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| trunk #18 → barricade #0 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| legs #21 → cow #11 | under [0-8] | attached to [0-8] | ✓ TRASER has this pair | ? |
| legs #22 → tiger #10 | under [0-8] | attached to [0-8] | ✓ TRASER has this pair | ? |
| tail #23 → tiger #10 | attached to [0-8] | attached to [0-8] | ✓ TRASER has this pair | ✓ |
| tiger head #24 → tiger #10 | attached to [0-8] | - | ↔ TRASER has it reversed | - |
| ram head #25 → cow #11 | attached to [0-8] | attached to [0-8] | ✓ TRASER has this pair | ✓ |
| tiger #10 → trunk #1 | - | in front of [0-3] | + only TRASER | - |
| tiger #10 → building #2 | - | in front of [0-8] | + only TRASER | - |
| tiger #10 → grass #7 | - | in front of [0-6] | + only TRASER | - |
| tiger #10 → trunk #12 | - | in front of [0-8] | + only TRASER | - |
| tiger #10 → trunk #13 | - | in front of [0-5] | + only TRASER | - |
| tiger #10 → trunk #15 | - | in front of [0-8] | + only TRASER | - |
| tiger #10 → trunk #16 | - | in front of [0-8] | + only TRASER | - |
| tiger #10 → trunk #18 | - | in front of [0-8] | + only TRASER | - |
| tiger #10 → trunk #19 | - | in front of [0-8] | + only TRASER | - |
| tiger #10 → trunk #20 | - | in front of [0-8] | + only TRASER | - |
| tiger #10 → tiger head #24 | - | near [0-8] | + only TRASER | - |
| cow #11 → trunk #1 | - | in front of [0-3] | + only TRASER | - |
| cow #11 → building #2 | - | in front of [0-8] | + only TRASER | - |
| cow #11 → grass #7 | - | in front of [0-6] | + only TRASER | - |
| cow #11 → trunk #12 | - | in front of [0-8] | + only TRASER | - |
| cow #11 → trunk #13 | - | in front of [0-5] | + only TRASER | - |
| cow #11 → trunk #15 | - | in front of [0-8] | + only TRASER | - |
| cow #11 → trunk #16 | - | in front of [0-8] | + only TRASER | - |
| cow #11 → trunk #18 | - | in front of [0-8] | + only TRASER | - |
| cow #11 → trunk #19 | - | in front of [0-8] | + only TRASER | - |
| cow #11 → trunk #20 | - | in front of [0-8] | + only TRASER | - |
| cow #11 → tiger head #24 | - | near [0-8] | + only TRASER | - |
| tiger head #24 → barricade #0 | - | in front of [0-8] | + only TRASER | - |
| tiger head #24 → trunk #1 | - | in front of [0-3] | + only TRASER | - |
| tiger head #24 → building #2 | - | in front of [0-8] | + only TRASER | - |
| tiger head #24 → trees #3 | - | in front of [0-8] | + only TRASER | - |
| tiger head #24 → trees #4 | - | in front of [0-8] | + only TRASER | - |
| tiger head #24 → trees #5 | - | in front of [0-8] | + only TRASER | - |
| tiger head #24 → grass #6 | - | on [0-8] | + only TRASER | - |
| tiger head #24 → grass #7 | - | in front of [0-6] | + only TRASER | - |
| tiger head #24 → people #9 | - | in front of [0-8] | + only TRASER | - |
| tiger head #24 → trunk #12 | - | in front of [0-8] | + only TRASER | - |
| tiger head #24 → trunk #13 | - | in front of [0-5] | + only TRASER | - |
| tiger head #24 → trunk #14 | - | in front of [0-8] | + only TRASER | - |
| tiger head #24 → trunk #15 | - | in front of [0-8] | + only TRASER | - |
| tiger head #24 → trunk #16 | - | in front of [0-8] | + only TRASER | - |
| tiger head #24 → trunk #17 | - | in front of [0-8] | + only TRASER | - |
| tiger head #24 → trunk #18 | - | in front of [0-8] | + only TRASER | - |
| tiger head #24 → trunk #19 | - | in front of [0-8] | + only TRASER | - |
| tiger head #24 → trunk #20 | - | in front of [0-8] | + only TRASER | - |


## 914_f4HgijyAEYs

7.5 s video; humans: 19 objects, 21 relations on 19 pairs; TRASER: 43 relations on 41 pairs.

**Pairs:** 9 in both, 10 missed by TRASER, 0 reversed, 0 with an object TRASER was not given, 32 only TRASER

**Objects: 7/19 right**

| id | human label | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|
| 0 | person | person | identical | ✓ |
| 1 | cotton candy | cloud-like object (uncertain) | semantic overlap | ✓ |
| 2 | seat | signboard | not judged yet | ? |
| 3 | ride | carousel | not judged yet | ? |
| 4 | landing | table | not judged yet | ? |
| 5 | building | pole | mismatch | ✗ |
| 6 | circus | carousel | mismatch | ✗ |
| 7 | circus | carousel | mismatch | ✗ |
| 8 | circus | string of lights | mismatch | ✗ |
| 9 | sky | awning | not judged yet | ? |
| 10 | seat | signboard | not judged yet | ? |
| 11 | ground | table | not judged yet | ? |
| 12 | light | light source (uncertain) | not judged yet | ? |
| 13 | light | light source (uncertain) | not judged yet | ? |
| 14 | glasses | spectacles | synonym | ✓ |
| 15 | hair | hair | identical | ✓ |
| 16 | jacket | jacket | identical | ✓ |
| 17 | hand | hand | identical | ✓ |
| 18 | hand | hand | identical | ✓ |

**Relations, pair by pair**

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| person #0 → cotton candy #1 | holding [0-8]; eating [0-3]; snacking on [0-3] | - | ✗ TRASER missed this pair | - - - |
| person #0 → ride #3 | in front of [0-8] | in front of [0-9] | ✓ TRASER has this pair | ✓ |
| person #0 → landing #4 | in front of [0-8] | in front of [0-9] | ✓ TRASER has this pair | ✓ |
| person #0 → building #5 | in front of [0-8] | in front of [0-9] | ✓ TRASER has this pair | ✓ |
| person #0 → sky #9 | under [0-8] | in front of [0-9] | ✓ TRASER has this pair | ? |
| person #0 → glasses #14 | wearing [0-4, 5-8] | wearing [0-9] | ✓ TRASER has this pair | ✓ |
| person #0 → jacket #16 | wearing [0-8] | wearing [0-9] | ✓ TRASER has this pair | ✓ |
| cotton candy #1 → person #0 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| cotton candy #1 → ride #3 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| cotton candy #1 → building #5 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| cotton candy #1 → sky #9 | below [0-8] | - | ✗ TRASER missed this pair | - |
| cotton candy #1 → light #12 | above [0-8] | - | ✗ TRASER missed this pair | - |
| cotton candy #1 → light #13 | above [0-8] | - | ✗ TRASER missed this pair | - |
| seat #2 → ride #3 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| light #12 → ride #3 | on [0-8] | - | ✗ TRASER missed this pair | - |
| light #13 → ride #3 | on [0-8] | - | ✗ TRASER missed this pair | - |
| glasses #14 → person #0 | on [0-4, 5-8] | on [0-9] | ✓ TRASER has this pair | ✓ |
| hair #15 → person #0 | on [0-8] | on [0-9] | ✓ TRASER has this pair | ✓ |
| jacket #16 → person #0 | on [0-8] | on [0-9] | ✓ TRASER has this pair | ✓ |
| person #0 → seat #2 | - | in front of [0-9] | + only TRASER | - |
| person #0 → circus #6 | - | in front of [0-9] | + only TRASER | - |
| person #0 → circus #7 | - | in front of [0-9] | + only TRASER | - |
| person #0 → circus #8 | - | in front of [0-9] | + only TRASER | - |
| person #0 → seat #10 | - | in front of [0-9] | + only TRASER | - |
| person #0 → ground #11 | - | in front of [0-9] | + only TRASER | - |
| person #0 → hair #15 | - | has [0-9] | + only TRASER | - |
| person #0 → hand #17 | - | holding [0-9]; looking at [0-9] | + only TRASER | - |
| person #0 → hand #18 | - | holding [0-9]; looking at [0-9] | + only TRASER | - |
| circus #8 → person #0 | - | above [0-9] | + only TRASER | - |
| circus #8 → ride #3 | - | above [0-9] | + only TRASER | - |
| circus #8 → building #5 | - | above [0-9] | + only TRASER | - |
| circus #8 → circus #6 | - | above [0-9] | + only TRASER | - |
| circus #8 → circus #7 | - | above [0-9] | + only TRASER | - |
| sky #9 → landing #4 | - | above [0-9] | + only TRASER | - |
| sky #9 → ground #11 | - | above [0-9] | + only TRASER | - |
| seat #10 → landing #4 | - | on [0-9] | + only TRASER | - |
| seat #10 → ground #11 | - | on [0-9] | + only TRASER | - |
| glasses #14 → sky #9 | - | in front of [0-9] | + only TRASER | - |
| glasses #14 → jacket #16 | - | above [0-9] | + only TRASER | - |
| glasses #14 → hand #17 | - | above [0-9] | + only TRASER | - |
| glasses #14 → hand #18 | - | above [0-9] | + only TRASER | - |
| hair #15 → sky #9 | - | in front of [0-9] | + only TRASER | - |
| hair #15 → jacket #16 | - | above [0-9] | + only TRASER | - |
| jacket #16 → sky #9 | - | in front of [0-9] | + only TRASER | - |
| hand #17 → person #0 | - | attached to [0-9] | + only TRASER | - |
| hand #17 → sky #9 | - | in front of [0-9] | + only TRASER | - |
| hand #17 → jacket #16 | - | in front of [0-9] | + only TRASER | - |
| hand #17 → hand #18 | - | above [0-9] | + only TRASER | - |
| hand #18 → person #0 | - | attached to [0-9] | + only TRASER | - |
| hand #18 → sky #9 | - | in front of [0-9] | + only TRASER | - |
| hand #18 → jacket #16 | - | in front of [0-9] | + only TRASER | - |


## 976_U19VojbI0h4

7.5 s video; humans: 65 objects, 36 relations on 32 pairs; TRASER: 49 relations on 43 pairs.

**Pairs:** 9 in both, 11 missed by TRASER, 0 reversed, 12 with an object TRASER was not given, 34 only TRASER

**Objects: 21/65 right**

| id | human label | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|
| 0 | ground | floor | synonym | ✓ |
| 1 | painting | painting | identical | ✓ |
| 2 | plant | flower arrangement | not judged yet | ? |
| 3 | decoration | basket | mismatch | ✗ |
| 4 | fireplace | fireplace | identical | ✓ |
| 5 | cabinet | fireplace | mismatch | ✗ |
| 6 | door | door | identical | ✓ |
| 7 | wall | wall | identical | ✓ |
| 8 | door | door frame (uncertain) | semantic overlap | ✓ |
| 9 | lamp | lamp | identical | ✓ |
| 10 | table | coffee table | hypernym/hyponym | ✓ |
| 11 | interior | shelf | not judged yet | ? |
| 12 | shelf | shelf | identical | ✓ |
| 13 | interior | plant | not judged yet | ? |
| 14 | ceiling fan | ceiling tile (uncertain) | not judged yet | ? |
| 15 | ceiling and upper wall | ceiling beam (uncertain) | semantic overlap | ✓ |
| 16 | closet | door | mismatch | ✗ |
| 17 | outlet | door handle | not judged yet | ? |
| 18 | table | coffee table | hypernym/hyponym | ✓ |
| 19 | rug | coffee table | not judged yet | ? |
| 20 | vase | flowerpot | not judged yet | ? |
| 21 | doorway | door | not judged yet | ? |
| 22 | wall | wall | identical | ✓ |
| 23 | wall | shelf | not judged yet | ? |
| 24 | wall | wall | identical | ✓ |
| 25 | lamp shade | lampshade | identical | ✓ |
| 26 | lamp base | lamp | semantic overlap | ✓ |
| 27 | throw pillow | table | not judged yet | ? |
| 28 | couch | coffee table | mismatch | ✗ |
| 29 | cup | flowerpot | mismatch | ✗ |
| 30 | leaves | flowerpot | not judged yet | ? |
| 31 | fireplace | fireplace | identical | ✓ |
| 32 | fireplace face | fireplace | hypernym/hyponym | ✓ |
| 33 | ceiling area | beam (uncertain) | not judged yet | ? |
| 34 | fireplace frame | door frame (uncertain) | semantic overlap | ✓ |
| 35 | flower vase | flowerpot | synonym | ✓ |
| 36 | vase | flowerpot | not judged yet | ? |
| 37 | home decor | flowerpot | hypernym/hyponym | ✓ |
| 38 | home decor | flowerpot | hypernym/hyponym | ✓ |
| 39 | socket | flowerpot | not judged yet | ? |
| 40 | flower | - (not given to TRASER) | - | ✗ |
| 41 | vase stand | - (not given to TRASER) | - | ✗ |
| 42 | tray | - (not given to TRASER) | - | ✗ |
| 43 | fan | - (not given to TRASER) | - | ✗ |
| 44 | cupboard handle | - (not given to TRASER) | - | ✗ |
| 45 | cupboard handle | - (not given to TRASER) | - | ✗ |
| 46 | flower vase | - (not given to TRASER) | - | ✗ |
| 47 | flower stand | - (not given to TRASER) | - | ✗ |
| 48 | vase | - (not given to TRASER) | - | ✗ |
| 49 | home decor | - (not given to TRASER) | - | ✗ |
| 50 | glass | - (not given to TRASER) | - | ✗ |
| 51 | fireplace | - (not given to TRASER) | - | ✗ |
| 52 | door | - (not given to TRASER) | - | ✗ |
| 53 | ground | - (not given to TRASER) | - | ✗ |
| 54 | door | - (not given to TRASER) | - | ✗ |
| 55 | shelf | - (not given to TRASER) | - | ✗ |
| 56 | shelf | - (not given to TRASER) | - | ✗ |
| 57 | shelf | - (not given to TRASER) | - | ✗ |
| 58 | household item | - (not given to TRASER) | - | ✗ |
| 59 | wall | - (not given to TRASER) | - | ✗ |
| 60 | light | - (not given to TRASER) | - | ✗ |
| 61 | door frame | - (not given to TRASER) | - | ✗ |
| 62 | top of a cupboard | - (not given to TRASER) | - | ✗ |
| 63 | door of cupboard | - (not given to TRASER) | - | ✗ |
| 64 | door of cupboard | - (not given to TRASER) | - | ✗ |

**Relations, pair by pair**

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| painting #1 → fireplace #4 | above [0-8] | above [0-8] | ✓ TRASER has this pair | ✓ |
| painting #1 → wall #22 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| painting #1 → fireplace face #32 | on [0-8] | above [0-8] | ✓ TRASER has this pair | ✓ |
| plant #2 → fireplace #4 | above [0-8] | above [0-8] | ✓ TRASER has this pair | ✓ |
| plant #2 → wall #22 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| plant #2 → fireplace face #32 | on [0-8] | above [0-8] | ✓ TRASER has this pair | ✓ |
| plant #2 → flower vase #46 | in [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| decoration #3 → wall #22 | in front of [0-5.5] | - | ✗ TRASER missed this pair | - |
| decoration #3 → fireplace face #32 | on [0-5.5] | above [0-6] | ✓ TRASER has this pair | ✓ |
| fireplace #4 → wall #22 | in [0-8]; against [0-8] | - | ✗ TRASER missed this pair | - - |
| cabinet #5 → ground #0 | on [0-4] | - | ✗ TRASER missed this pair | - |
| door #6 → closet #16 | attached to [0-8] | - | ✗ TRASER missed this pair | - |
| door #6 → wall #59 | in [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| door #6 → door frame #61 | inside [0-8]; attached to [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - - |
| door #8 → wall #7 | inside [0-8] | - | ✗ TRASER missed this pair | - |
| lamp #9 → table #10 | on [0-1] | on [0-2]; above [0-2] | ✓ TRASER has this pair | ✗ |
| closet #16 → door #54 | behind [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| table #18 → ground #0 | on [0-7] | on [0-2] | ✓ TRASER has this pair | ✗ |
| rug #19 → ground #0 | on [0-2] | on [0-2] | ✓ TRASER has this pair | ✓ |
| vase #20 → table #18 | on [0-2] | on [0-2] | ✓ TRASER has this pair | ✓ |
| doorway #21 → fireplace frame #34 | in [0-8]; in [0-8] | - | ✗ TRASER missed this pair | - - |
| fireplace #31 → wall #22 | in [0-8] | - | ✗ TRASER missed this pair | - |
| fireplace #31 → fireplace face #32 | under [0-8] | - | ✗ TRASER missed this pair | - |
| fireplace face #32 → wall #22 | against [0-8] | - | ✗ TRASER missed this pair | - |
| flower vase #46 → flower stand #47 | on [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| door #52 → doorway #21 | inside [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| ground #53 → doorway #21 | inside [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| door #54 → wall #59 | in [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| door #54 → door frame #61 | attached to [0-8]; inside [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - - |
| shelf #55 → closet #16 | in [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| shelf #56 → closet #16 | in [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| shelf #57 → closet #16 | in [0-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| ground #0 → fireplace #4 | - | below [0-8] | + only TRASER | - |
| ground #0 → door #6 | - | below [0-8] | + only TRASER | - |
| ground #0 → closet #16 | - | below [0-8] | + only TRASER | - |
| ground #0 → doorway #21 | - | below [0-8] | + only TRASER | - |
| painting #1 → wall #7 | - | mounted on [0-8] | + only TRASER | - |
| painting #1 → fireplace #31 | - | above [0-8] | + only TRASER | - |
| plant #2 → wall #7 | - | mounted on [0-8] | + only TRASER | - |
| plant #2 → fireplace #31 | - | above [0-8] | + only TRASER | - |
| decoration #3 → fireplace #4 | - | above [0-6] | + only TRASER | - |
| decoration #3 → wall #7 | - | mounted on [0-6] | + only TRASER | - |
| decoration #3 → fireplace #31 | - | above [0-6] | + only TRASER | - |
| door #6 → wall #7 | - | in [0-8] | + only TRASER | - |
| table #10 → ground #0 | - | on [0-2] | + only TRASER | - |
| interior #11 → shelf #12 | - | above [0-4] | + only TRASER | - |
| interior #11 → wall #24 | - | mounted on [0-4] | + only TRASER | - |
| shelf #12 → wall #23 | - | above [0-4] | + only TRASER | - |
| shelf #12 → wall #24 | - | mounted on [0-4] | + only TRASER | - |
| interior #13 → flower vase #35 | - | in [0-4]; above [0-4] | + only TRASER | - |
| interior #13 → socket #39 | - | in [0-4]; above [0-4] | + only TRASER | - |
| closet #16 → wall #7 | - | in [0-8] | + only TRASER | - |
| outlet #17 → doorway #21 | - | attached to [0-8]; on [0-8] | + only TRASER | - |
| doorway #21 → wall #7 | - | in [0-8] | + only TRASER | - |
| wall #23 → interior #11 | - | above [0-4] | + only TRASER | - |
| wall #23 → wall #24 | - | mounted on [0-4] | + only TRASER | - |
| lamp shade #25 → lamp #9 | - | on [0-2]; above [0-2] | + only TRASER | - |
| lamp base #26 → throw pillow #27 | - | on [0-2]; above [0-2] | + only TRASER | - |
| throw pillow #27 → ground #0 | - | on [0-2] | + only TRASER | - |
| couch #28 → ground #0 | - | on [0-2] | + only TRASER | - |
| leaves #30 → table #18 | - | on [0-2] | + only TRASER | - |
| flower vase #35 → leaves #30 | - | above [0-2] | + only TRASER | - |
| vase #36 → home decor #37 | - | above [0-3] | + only TRASER | - |
| home decor #37 → home decor #38 | - | above [0-3] | + only TRASER | - |
| home decor #38 → vase #36 | - | above [0-3] | + only TRASER | - |
| socket #39 → leaves #30 | - | above [0-2] | + only TRASER | - |


## sav_053005

18.71 s video; humans: 29 objects, 29 relations on 26 pairs; TRASER: 37 relations on 34 pairs.

**Pairs:** 9 in both, 17 missed by TRASER, 0 reversed, 0 with an object TRASER was not given, 25 only TRASER

**Objects: 12/29 right**

| id | human label | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|
| 0 | person | person | identical | ✓ |
| 1 | carpet | rug | synonym | ✓ |
| 2 | sofa | cushion | semantic overlap | ✓ |
| 3 | table | ottoman | not judged yet | ? |
| 4 | curtain | curtain | identical | ✓ |
| 5 | windows | window | not judged yet | ? |
| 6 | lights | curtain | mismatch | ✗ |
| 7 | chair | sofa | semantic overlap | ✓ |
| 8 | wall panel | baseboard (uncertain) | not judged yet | ? |
| 9 | floor | rug | semantic overlap | ✓ |
| 10 | pillars | wall panel | not judged yet | ? |
| 11 | fountain | runner carpet | mismatch | ✗ |
| 12 | desk | television set | mismatch | ✗ |
| 13 | sofa | chair leg (uncertain) | not judged yet | ? |
| 14 | lights | signboard | mismatch | ✗ |
| 15 | background | pillar | mismatch | ✗ |
| 16 | screen | television | not judged yet | ? |
| 17 | chandelier lights | hand | mismatch | ✗ |
| 18 | door | door | identical | ✓ |
| 19 | oerson | person | identical | ✓ |
| 20 | pillar | pillar | identical | ✓ |
| 21 | reflected lights | curtain | not judged yet | ? |
| 22 | bag | handbag | hypernym/hyponym | ✓ |
| 23 | head | hair | semantic overlap | ✓ |
| 24 | legs | legs | identical | ✓ |
| 25 | entrance | signboard | mismatch | ✗ |
| 26 | balcony | pillar | not judged yet | ? |
| 27 | bench | runner carpet | mismatch | ✗ |
| 28 | sign | signboard | not judged yet | ? |

**Relations, pair by pair**

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| person #0 → carpet #1 | moves on [0-9, 11-19]; on [0-9, 11-19] | on [0-19] | ✓ TRASER has this pair | ? ✓ |
| person #0 → table #3 | in front of [0-9, 11-19] | approaching [0-11]; moving away from [11-19] | ✓ TRASER has this pair | ✗ |
| person #0 → curtain #4 | in front of [0-9, 11-19] | in front of [0-19] | ✓ TRASER has this pair | ✓ |
| person #0 → windows #5 | in front of [0-9, 11-19] | in front of [0-19] | ✓ TRASER has this pair | ✓ |
| person #0 → chair #7 | in front of [0-9, 11-19] | moving away from [0-11]; approaching [11-19]; in front of [0-19] | ✓ TRASER has this pair | ✓ |
| person #0 → wall panel #8 | in front of [0-9, 11-19] | - | ✗ TRASER missed this pair | - |
| person #0 → bag #22 | poses with [0-9, 11-19]; carries [0-9, 11-19] | carrying [0-19] | ✓ TRASER has this pair | ? ? |
| carpet #1 → floor #9 | on [0-5, 9-10, 11-12] | - | ✗ TRASER missed this pair | - |
| sofa #2 → carpet #1 | on [0-8, 12-15, 18-19] | - | ✗ TRASER missed this pair | - |
| table #3 → carpet #1 | on [0-9, 11-19] | - | ✗ TRASER missed this pair | - |
| table #3 → chair #7 | in front of [0-9, 11-19] | in front of [0-19] | ✓ TRASER has this pair | ✓ |
| curtain #4 → windows #5 | in front of [0-9, 11-19] | - | ✗ TRASER missed this pair | - |
| chair #7 → carpet #1 | on [0-9, 11-19] | - | ✗ TRASER missed this pair | - |
| wall panel #8 → curtain #4 | below [0-9, 11-19] | - | ✗ TRASER missed this pair | - |
| pillars #10 → floor #9 | on [9-11] | - | ✗ TRASER missed this pair | - |
| fountain #11 → floor #9 | on [10-12] | - | ✗ TRASER missed this pair | - |
| desk #12 → floor #9 | on [9-10] | - | ✗ TRASER missed this pair | - |
| desk #12 → pillar #20 | in front of [8.5-10.5] | - | ✗ TRASER missed this pair | - |
| sofa #13 → carpet #1 | on [9-10] | - | ✗ TRASER missed this pair | - |
| lights #14 → desk #12 | above [8.5-10.5] | - | ✗ TRASER missed this pair | - |
| door #18 → floor #9 | above [8.5-11] | - | ✗ TRASER missed this pair | - |
| bag #22 → person #0 | moves with [0-9, 11-19]; near [0-9, 11-19] | beside [0-19] | ✓ TRASER has this pair | ? ? |
| head #23 → legs #24 | above [0-9, 11-19] | - | ✗ TRASER missed this pair | - |
| legs #24 → carpet #1 | on [0-9, 11-19] | above [0-19] | ✓ TRASER has this pair | ✓ |
| entrance #25 → floor #9 | above [9-11] | - | ✗ TRASER missed this pair | - |
| bench #27 → floor #9 | on [9.5-12] | - | ✗ TRASER missed this pair | - |
| person #0 → pillars #10 | - | in front of [9-12] | + only TRASER | - |
| person #0 → fountain #11 | - | in front of [9-12] | + only TRASER | - |
| person #0 → desk #12 | - | in front of [9-12] | + only TRASER | - |
| person #0 → lights #14 | - | in front of [9-12] | + only TRASER | - |
| person #0 → background #15 | - | in front of [9-12] | + only TRASER | - |
| person #0 → screen #16 | - | in front of [9-12] | + only TRASER | - |
| person #0 → door #18 | - | in front of [9-12] | + only TRASER | - |
| person #0 → oerson #19 | - | in front of [9-12] | + only TRASER | - |
| person #0 → pillar #20 | - | in front of [9-12] | + only TRASER | - |
| person #0 → head #23 | - | wearing [0-19] | + only TRASER | - |
| person #0 → legs #24 | - | wearing [0-19] | + only TRASER | - |
| person #0 → entrance #25 | - | in front of [9-12] | + only TRASER | - |
| person #0 → balcony #26 | - | in front of [9-12] | + only TRASER | - |
| person #0 → bench #27 | - | in front of [9-12] | + only TRASER | - |
| person #0 → sign #28 | - | in front of [9-12] | + only TRASER | - |
| sofa #2 → curtain #4 | - | in front of [0-8, 13-15] | + only TRASER | - |
| sofa #2 → windows #5 | - | in front of [0-8, 13-15] | + only TRASER | - |
| table #3 → curtain #4 | - | in front of [0-19] | + only TRASER | - |
| table #3 → windows #5 | - | in front of [0-19] | + only TRASER | - |
| chair #7 → curtain #4 | - | in front of [0-19] | + only TRASER | - |
| chair #7 → windows #5 | - | in front of [0-19] | + only TRASER | - |
| bag #22 → carpet #1 | - | above [0-19] | + only TRASER | - |
| head #23 → person #0 | - | on [0-19] | + only TRASER | - |
| head #23 → carpet #1 | - | above [0-19] | + only TRASER | - |
| legs #24 → person #0 | - | on [0-19] | + only TRASER | - |

