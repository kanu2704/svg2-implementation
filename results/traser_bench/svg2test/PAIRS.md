# svg2test: which object pairs TRASER talks about (10 random videos, seed 0)

TRASER is given the human objects (masks) and writes its own list of relations; it is not told which pairs to describe. Each row is one ordered pair (subject → object) that the humans or TRASER mention.

- **✓ TRASER has this pair**: TRASER wrote at least one relation for the same two objects, same direction
- **✗ TRASER missed this pair**: humans annotated it, TRASER said nothing about these two objects
- **↔ reversed**: TRASER only has the other direction (object → subject); scored as missed
- **⊘ object not given**: one of the two objects was not among the (at most 40) objects TRASER received, so it could not answer; scored as missed, as in the paper's setup
- **+ only TRASER**: TRASER describes a pair the humans did not annotate (ignored by the scores)
- last column, one mark per human relation of the pair: ✓ word right and tIoU > 0.5, ✗ not, ? the judge has not compared the words yet

**Total over these videos:** 276 human pairs, 308 TRASER pairs; 90 in both, 155 missed, 9 reversed, 22 with an object not given, 218 only TRASER.

| video | human pairs | TRASER pairs | pairs in both | missed by TRASER | reversed | object not given | only TRASER |
|---|---|---|---|---|---|---|---|
| [1190_UmpN6eLjN8w](#1190_umpn6eljn8w) | 40 | 26 | 7 | 31 | 2 | 0 | 19 |
| [339_j2gELsuQ3Cg](#339_j2gelsuq3cg) | 17 | 14 | 3 | 14 | 0 | 0 | 11 |
| [700_zkhPzSZcRtQ](#700_zkhpzszcrtq) | 39 | 41 | 9 | 28 | 2 | 0 | 32 |
| [714_nooF6zlfzMI](#714_noof6zlfzmi) | 24 | 30 | 8 | 16 | 0 | 0 | 22 |
| [722__ajUvCkhVcI](#722__ajuvckhvci) | 32 | 30 | 9 | 21 | 2 | 0 | 21 |
| [744_1X6KvqPjk6I](#744_1x6kvqpjk6i) | 23 | 36 | 10 | 11 | 2 | 0 | 26 |
| [778_3PmDn84laac](#778_3pmdn84laac) | 18 | 27 | 8 | 9 | 1 | 0 | 19 |
| [914_f4HgijyAEYs](#914_f4hgijyaeys) | 19 | 41 | 9 | 10 | 0 | 0 | 32 |
| [976_U19VojbI0h4](#976_u19vojbi0h4) | 32 | 43 | 9 | 11 | 0 | 12 | 34 |
| [sav_004550](#sav_004550) | 32 | 20 | 18 | 4 | 0 | 10 | 2 |

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


## 714_nooF6zlfzMI

22.67 s video; humans: 13 objects, 26 relations on 24 pairs; TRASER: 34 relations on 30 pairs.

**Pairs:** 8 in both, 16 missed by TRASER, 0 reversed, 0 with an object TRASER was not given, 22 only TRASER

**Objects: 5/13 right**

| id | human label | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|
| 0 | fish | fishing rod (uncertain) | mismatch | ✗ |
| 1 | sky | sun | not judged yet | ? |
| 2 | human | hand | semantic overlap | ✓ |
| 3 | Fishing Rod | fishing reel | semantic overlap | ✓ |
| 4 | shore or ground | rock | not judged yet | ? |
| 5 | embankment | sand | not judged yet | ? |
| 6 | river or canal | water | not judged yet | ? |
| 7 | shore | bridge (uncertain) | not judged yet | ? |
| 8 | handle (grip) | fishing reel | semantic overlap | ✓ |
| 9 | reel | fishing rod (uncertain) | not judged yet | ? |
| 10 | rod | fishing rod | not judged yet | ? |
| 11 | hand | hand | identical | ✓ |
| 12 | hand | hand | identical | ✓ |

**Relations, pair by pair**

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| fish #0 → human #2 | caught by [1.66667-23.6667] | - | ✗ TRASER missed this pair | - |
| fish #0 → Fishing Rod #3 | attached to [1.66667-23.6667] | - | ✗ TRASER missed this pair | - |
| fish #0 → river or canal #6 | above [1.66667-23.6667] | - | ✗ TRASER missed this pair | - |
| sky #1 → fish #0 | above [0-23.6667] | - | ✗ TRASER missed this pair | - |
| sky #1 → human #2 | above [0-23.6667] | - | ✗ TRASER missed this pair | - |
| sky #1 → Fishing Rod #3 | above [0-23.6667] | - | ✗ TRASER missed this pair | - |
| sky #1 → shore or ground #4 | above [0-23.6667] | above [0-23] | ✓ TRASER has this pair | ✓ |
| sky #1 → embankment #5 | above [0-23.6667] | above [0-23] | ✓ TRASER has this pair | ✓ |
| sky #1 → river or canal #6 | above [0-23.6667] | above [0-23] | ✓ TRASER has this pair | ✓ |
| sky #1 → shore #7 | above [0-23.6667] | - | ✗ TRASER missed this pair | - |
| sky #1 → handle (grip) #8 | above [0-23.6667] | - | ✗ TRASER missed this pair | - |
| sky #1 → reel #9 | above [0-23.6667] | - | ✗ TRASER missed this pair | - |
| sky #1 → rod #10 | above [0-23.6667] | - | ✗ TRASER missed this pair | - |
| sky #1 → hand #11 | above [0-23.6667] | - | ✗ TRASER missed this pair | - |
| sky #1 → hand #12 | above [0-23.6667] | - | ✗ TRASER missed this pair | - |
| human #2 → embankment #5 | standing on [0-23.6667]; walking along [0-23.6667] | in front of [0-23] | ✓ TRASER has this pair | ? ? |
| human #2 → river or canal #6 | beside [0-23.6667]; fishing in [0-23.6667] | in front of [0-23] | ✓ TRASER has this pair | ✗ ? |
| human #2 → hand #11 | has [0-23.6667] | - | ✗ TRASER missed this pair | - |
| shore or ground #4 → river or canal #6 | beside [0-23.6667] | adjacent to [0-23] | ✓ TRASER has this pair | ? |
| embankment #5 → river or canal #6 | beside [0-23.6667] | adjacent to [0-23] | ✓ TRASER has this pair | ? |
| reel #9 → Fishing Rod #3 | attached to [0-23.6667] | - | ✗ TRASER missed this pair | - |
| rod #10 → Fishing Rod #3 | attached to [0-23.6667] | attached to [0-23] | ✓ TRASER has this pair | ✓ |
| hand #11 → reel #9 | operating [0-5.16667] | - | ✗ TRASER missed this pair | - |
| hand #12 → handle (grip) #8 | holding [0-23.6667] | - | ✗ TRASER missed this pair | - |
| human #2 → Fishing Rod #3 | - | holding [0-23] | + only TRASER | - |
| human #2 → shore or ground #4 | - | in front of [0-23] | + only TRASER | - |
| human #2 → rod #10 | - | holding [0-23]; fishing with [0-23] | + only TRASER | - |
| Fishing Rod #3 → shore or ground #4 | - | in front of [0-23] | + only TRASER | - |
| Fishing Rod #3 → embankment #5 | - | in front of [0-23] | + only TRASER | - |
| Fishing Rod #3 → river or canal #6 | - | moving relative to [0-23]; in front of [0-23] | + only TRASER | - |
| shore or ground #4 → embankment #5 | - | adjacent to [0-23] | + only TRASER | - |
| handle (grip) #8 → shore or ground #4 | - | in front of [0-23] | + only TRASER | - |
| handle (grip) #8 → embankment #5 | - | in front of [0-23] | + only TRASER | - |
| handle (grip) #8 → river or canal #6 | - | in front of [0-23] | + only TRASER | - |
| rod #10 → shore or ground #4 | - | in front of [0-23] | + only TRASER | - |
| rod #10 → embankment #5 | - | in front of [0-23] | + only TRASER | - |
| rod #10 → river or canal #6 | - | moving relative to [0-23]; in front of [0-23] | + only TRASER | - |
| rod #10 → handle (grip) #8 | - | attached to [0-23] | + only TRASER | - |
| hand #11 → shore or ground #4 | - | in front of [0-5, 13-14] | + only TRASER | - |
| hand #11 → embankment #5 | - | in front of [0-5, 13-14] | + only TRASER | - |
| hand #11 → river or canal #6 | - | in front of [0-5, 13-14] | + only TRASER | - |
| hand #12 → Fishing Rod #3 | - | holding [0-23] | + only TRASER | - |
| hand #12 → shore or ground #4 | - | in front of [0-23] | + only TRASER | - |
| hand #12 → embankment #5 | - | in front of [0-23] | + only TRASER | - |
| hand #12 → river or canal #6 | - | in front of [0-23] | + only TRASER | - |
| hand #12 → rod #10 | - | holding [0-23]; fishing with [0-23] | + only TRASER | - |


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


## 778_3PmDn84laac

7.5 s video; humans: 23 objects, 27 relations on 18 pairs; TRASER: 32 relations on 27 pairs.

**Pairs:** 8 in both, 9 missed by TRASER, 1 reversed, 0 with an object TRASER was not given, 19 only TRASER

**Objects: 15/23 right**

| id | human label | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|
| 0 | smoke | smoke | identical | ✓ |
| 1 | tree | mountain | not judged yet | ? |
| 2 | grass/trees/shrubs | bush | hypernym/hyponym | ✓ |
| 3 | train bridge | bridge | not judged yet | ? |
| 4 | sky | cloud | semantic overlap | ✓ |
| 5 | grass/trees | hill | semantic overlap | ✓ |
| 6 | train | train | identical | ✓ |
| 7 | train car | train car | identical | ✓ |
| 8 | train car | train car | identical | ✓ |
| 9 | train car | train car | identical | ✓ |
| 10 | cell phone tower | telephone pole | semantic overlap | ✓ |
| 11 | train car | train car | identical | ✓ |
| 12 | locomotive | locomotive | identical | ✓ |
| 13 | trees | tree | not judged yet | ? |
| 14 | bushes | bush | identical | ✓ |
| 15 | bushes | bush | identical | ✓ |
| 16 | fence post | plant | mismatch | ✗ |
| 17 | fence post | pole | synonym | ✓ |
| 18 | stick | pole | not judged yet | ? |
| 19 | pole | pole | identical | ✓ |
| 20 | tree | pole | mismatch | ✗ |
| 21 | trees | plant | not judged yet | ? |
| 22 | trees | hill | not judged yet | ? |

**Relations, pair by pair**

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| smoke #0 → train bridge #3 | above [0-8] | - | ✗ TRASER missed this pair | - |
| smoke #0 → sky #4 | rises in [0-8]; in front of [0-8] | - | ✗ TRASER missed this pair | - - |
| smoke #0 → train #6 | trails behind [0-8]; above [0-8] | above [0-8] | ✓ TRASER has this pair | ? ✓ |
| train bridge #3 → tree #1 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| train bridge #3 → bushes #14 | above [0-8] | - | ↔ TRASER has it reversed | - |
| sky #4 → tree #1 | above [0-8] | above [0-8] | ✓ TRASER has this pair | ✓ |
| train #6 → tree #1 | moves past [0-8]; in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ? ✓ |
| train #6 → grass/trees/shrubs #2 | above [0-8] | - | ✗ TRASER missed this pair | - |
| train #6 → train bridge #3 | moves across [0-8]; on [0-8] | moving along [0-8]; passing under [0-8]; traveling through [0-8]; on [0-8] | ✓ TRASER has this pair | ? ✓ |
| train #6 → trees #22 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| train car #7 → train #6 | attached to [0-8]; connected to [0-8] | - | ✗ TRASER missed this pair | - - |
| train car #8 → train #6 | attached to [0-8]; connected to [0-8] | - | ✗ TRASER missed this pair | - - |
| train car #9 → train #6 | attached to [0-8]; connected to [0-8] | - | ✗ TRASER missed this pair | - - |
| cell phone tower #10 → sky #4 | in front of [0-8] | - | ✗ TRASER missed this pair | - |
| train car #11 → train bridge #3 | moves across [0-8] | on [0-8] | ✓ TRASER has this pair | ? |
| train car #11 → train #6 | attached to [0-8]; connected to [0-8] | - | ✗ TRASER missed this pair | - - |
| locomotive #12 → train #6 | attached to [0-7]; connected to [0-7] | attached to [0-8] | ✓ TRASER has this pair | ✓ ? |
| bushes #14 → train bridge #3 | in front of [0-8] | in front of [0-8] | ✓ TRASER has this pair | ✓ |
| smoke #0 → tree #1 | - | in front of [0-8] | + only TRASER | - |
| smoke #0 → locomotive #12 | - | rising from [0-8]; above [0-8] | + only TRASER | - |
| grass/trees/shrubs #2 → train bridge #3 | - | in front of [0-8] | + only TRASER | - |
| grass/trees #5 → tree #1 | - | in front of [0-8] | + only TRASER | - |
| train car #7 → train bridge #3 | - | on [0-8] | + only TRASER | - |
| train car #8 → train bridge #3 | - | on [0-8] | + only TRASER | - |
| train car #9 → train bridge #3 | - | on [0-8] | + only TRASER | - |
| cell phone tower #10 → grass/trees #5 | - | on [0-8] | + only TRASER | - |
| locomotive #12 → tree #1 | - | in front of [0-8] | + only TRASER | - |
| locomotive #12 → train bridge #3 | - | moving along [0-8]; on [0-8] | + only TRASER | - |
| trees #13 → train bridge #3 | - | in front of [0-8] | + only TRASER | - |
| bushes #15 → train bridge #3 | - | in front of [0-8] | + only TRASER | - |
| fence post #16 → train bridge #3 | - | in front of [0-8] | + only TRASER | - |
| fence post #17 → train bridge #3 | - | in front of [0-8] | + only TRASER | - |
| stick #18 → train bridge #3 | - | in front of [0-8] | + only TRASER | - |
| pole #19 → train bridge #3 | - | in front of [0-8] | + only TRASER | - |
| tree #20 → train bridge #3 | - | in front of [0-8] | + only TRASER | - |
| trees #21 → train bridge #3 | - | in front of [0-8] | + only TRASER | - |
| trees #22 → tree #1 | - | in front of [0-8] | + only TRASER | - |


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


## sav_004550

13.71 s video; humans: 52 objects, 37 relations on 32 pairs; TRASER: 27 relations on 20 pairs.

**Pairs:** 18 in both, 4 missed by TRASER, 0 reversed, 10 with an object TRASER was not given, 2 only TRASER

**Objects: 29/52 right**

| id | human label | TRASER label | verdict | right (lenient) |
|---|---|---|---|---|
| 0 | bridegroom | person | hypernym/hyponym | ✓ |
| 1 | bride | bride | identical | ✓ |
| 2 | stone column | column (uncertain) | not judged yet | ? |
| 3 | wall | painting | mismatch | ✗ |
| 4 | archway | painting | mismatch | ✗ |
| 5 | floor | carpet | semantic overlap | ✓ |
| 6 | railing | chair | not judged yet | ? |
| 7 | door | door | identical | ✓ |
| 8 | fence | gate | semantic overlap | ✓ |
| 9 | wall | painting | mismatch | ✗ |
| 10 | flower | flower arrangement | hypernym/hyponym | ✓ |
| 11 | crowds | person | hypernym/hyponym | ✓ |
| 12 | person | person | identical | ✓ |
| 13 | person | person | identical | ✓ |
| 14 | person | person | identical | ✓ |
| 15 | person | person | identical | ✓ |
| 16 | person | person | identical | ✓ |
| 17 | person | person | identical | ✓ |
| 18 | person | - (not given to TRASER) | - | ✗ |
| 19 | person | person | identical | ✓ |
| 20 | person | person | identical | ✓ |
| 21 | person | dress | mismatch | ✗ |
| 22 | person | person | identical | ✓ |
| 23 | person | person | identical | ✓ |
| 24 | person | person | identical | ✓ |
| 25 | person | - (not given to TRASER) | - | ✗ |
| 26 | person | person | identical | ✓ |
| 27 | person | person | identical | ✓ |
| 28 | person | dress | mismatch | ✗ |
| 29 | person | person | identical | ✓ |
| 30 | person | person | identical | ✓ |
| 31 | person | dress | mismatch | ✗ |
| 32 | person | dress | mismatch | ✗ |
| 33 | person | person | identical | ✓ |
| 34 | person | person | identical | ✓ |
| 35 | person | person | identical | ✓ |
| 36 | person | person | identical | ✓ |
| 37 | person | person | identical | ✓ |
| 38 | person | person | identical | ✓ |
| 39 | person | person | identical | ✓ |
| 40 | person | - (not given to TRASER) | - | ✗ |
| 41 | person | - (not given to TRASER) | - | ✗ |
| 42 | person | - (not given to TRASER) | - | ✗ |
| 43 | person | - (not given to TRASER) | - | ✗ |
| 44 | person | - (not given to TRASER) | - | ✗ |
| 45 | person | - (not given to TRASER) | - | ✗ |
| 46 | person | - (not given to TRASER) | - | ✗ |
| 47 | person | - (not given to TRASER) | - | ✗ |
| 48 | carpet | - (not given to TRASER) | - | ✗ |
| 49 | painting | - (not given to TRASER) | - | ✗ |
| 50 | window | - (not given to TRASER) | - | ✗ |
| 51 | light | - (not given to TRASER) | - | ✗ |

**Relations, pair by pair**

| pair (subject → object) | human said | TRASER said | pair | relation right? (lenient, tIoU > 0.5) |
|---|---|---|---|---|
| bridegroom #0 → bride #1 | walks with [0-14] | holding hands with [0-2]; moving away from [2-5]; looking at [0-2]; next to [0-15] | ✓ TRASER has this pair | ? |
| bridegroom #0 → stone column #2 | in front of [0-5] | - | ✗ TRASER missed this pair | - |
| bridegroom #0 → wall #3 | in front of [0-4.5] | in front of [0-15] | ✓ TRASER has this pair | ✗ |
| bridegroom #0 → archway #4 | in front of [6-14] | in front of [5-15] | ✓ TRASER has this pair | ✓ |
| bridegroom #0 → floor #5 | on [0-5, 6-14] | on [0-15] | ✓ TRASER has this pair | ✓ |
| bridegroom #0 → railing #6 | adjacent to [0-14] | in front of [0-15] | ✓ TRASER has this pair | ? |
| bridegroom #0 → door #7 | in front of [4-6] | in front of [5-15] | ✓ TRASER has this pair | ✗ |
| bridegroom #0 → fence #8 | in front of [0-4] | in front of [0-4] | ✓ TRASER has this pair | ✓ |
| bridegroom #0 → wall #9 | in front of [0-5.5] | in front of [0-15] | ✓ TRASER has this pair | ✗ |
| bridegroom #0 → crowds #11 | in front of [0-7.5] | looking at [10-15]; in front of [0-15] | ✓ TRASER has this pair | ✗ |
| bridegroom #0 → carpet #48 | moves along [0-5, 7-14]; on [0-5, 7-14] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - - |
| bridegroom #0 → painting #49 | in front of [4-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| bridegroom #0 → window #50 | in front of [0-4] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| bridegroom #0 → light #51 | below [0-4.5] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| bride #1 → bridegroom #0 | holds arm of [0-14]; moves with [0-14]; walks down aisle with [0-14]; touching [0-14] | approaching [7-11]; moving away from [11-15]; looking at [0-2] | ✓ TRASER has this pair | ? ? ? ✗ |
| bride #1 → stone column #2 | in front of [0-3] | - | ✗ TRASER missed this pair | - |
| bride #1 → wall #3 | in front of [0-4] | in front of [0-15] | ✓ TRASER has this pair | ✗ |
| bride #1 → archway #4 | in front of [7-14] | in front of [5-15] | ✓ TRASER has this pair | ✓ |
| bride #1 → floor #5 | on [0-5, 6-14] | on [0-15] | ✓ TRASER has this pair | ✓ |
| bride #1 → railing #6 | adjacent to [0-14] | in front of [0-15] | ✓ TRASER has this pair | ? |
| bride #1 → door #7 | in front of [5-14] | in front of [5-15] | ✓ TRASER has this pair | ✓ |
| bride #1 → fence #8 | in front of [0-3.5] | in front of [0-4] | ✓ TRASER has this pair | ✓ |
| bride #1 → wall #9 | in front of [0-14] | in front of [0-15] | ✓ TRASER has this pair | ✓ |
| bride #1 → crowds #11 | in front of [0-14] | looking at [10-15]; in front of [0-15] | ✓ TRASER has this pair | ✓ |
| bride #1 → carpet #48 | moves along [0-14]; on [0-5, 7-14] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - - |
| bride #1 → painting #49 | in front of [3-5, 6-8] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| bride #1 → window #50 | in front of [0-3] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| bride #1 → light #51 | below [0-4.5] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| railing #6 → carpet #48 | beside [0-14] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| person #30 → bride #1 | looks at [9-14] | - | ✗ TRASER missed this pair | - |
| person #31 → bride #1 | looks at [11-14] | - | ✗ TRASER missed this pair | - |
| carpet #48 → floor #5 | on [0-5, 7-14] | - | ⊘ an object was not given to TRASER (40-object cap / no mask on its frames) | - |
| bridegroom #0 → flower #10 | - | in front of [13-15] | + only TRASER | - |
| bride #1 → flower #10 | - | in front of [13-15] | + only TRASER | - |

