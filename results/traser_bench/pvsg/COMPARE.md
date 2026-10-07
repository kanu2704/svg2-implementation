# pvsg: human labels vs TRASER, video by video

44 videos with a prediction. Lenient criterion, temporal IoU > 0.5. ✓ right, ✗ wrong, ? = the judge (Kimi K3) has not compared these two labels yet (identical text counts as right without the judge). Relation = same two objects, predicate not a mismatch, tIoU > 0.5; triplet = relation right and both object labels right. Made by `tools/bench_eval.py write_compare`.

**So far: objects 239/670, relations 83/672, triplets 18/672** (before judging; final numbers in README.md)

| video | objects right | relations right | triplets right | not judged yet (?) |
|---|---|---|---|---|
| [0004_11566980553](#0004_11566980553) | 6/15 | 0/13 | 0/13 | 12 |
| [0010_8610561401](#0010_8610561401) | 2/5 | 1/8 | 0/8 | 5 |
| [0018_4748191834](#0018_4748191834) | 5/14 | 3/17 | 2/17 | 12 |
| [0027_4571353789](#0027_4571353789) | 3/16 | 1/17 | 0/17 | 17 |
| [0028_4021064662](#0028_4021064662) | 3/10 | 2/18 | 0/18 | 12 |
| [0039_6951351121](#0039_6951351121) | 6/17 | 0/13 | 0/13 | 13 |
| [0046_11919433184](#0046_11919433184) | 7/16 | 1/17 | 1/17 | 8 |
| [0051_3702633786](#0051_3702633786) | 1/12 | 0/15 | 0/15 | 11 |
| [0053_5599511471](#0053_5599511471) | 1/7 | 1/14 | 0/14 | 5 |
| [0054_2612939953](#0054_2612939953) | 5/15 | 2/17 | 0/17 | 12 |
| [0057_7001078933](#0057_7001078933) | 6/15 | 2/18 | 0/18 | 13 |
| [0062_6430774273](#0062_6430774273) | 3/6 | 0/13 | 0/13 | 6 |
| [0069_2740320945](#0069_2740320945) | 6/20 | 0/16 | 0/16 | 15 |
| [0075_11566764085](#0075_11566764085) | 3/10 | 1/12 | 0/12 | 9 |
| [0096_5296138427](#0096_5296138427) | 5/11 | 2/12 | 0/12 | 7 |
| [0be30efe-9d71-4698-8304-f1d441aeea58_1](#0be30efe-9d71-4698-8304-f1d441aeea58_1) | 2/12 | 0/10 | 0/10 | 8 |
| [1000_6828150903](#1000_6828150903) | 6/15 | 3/13 | 0/13 | 15 |
| [1001_7007447516](#1001_7007447516) | 11/22 | 1/9 | 1/9 | 12 |
| [1002_5280626374](#1002_5280626374) | 2/13 | 1/12 | 1/12 | 12 |
| [1005_4760962392](#1005_4760962392) | 8/17 | 0/20 | 0/20 | 10 |
| [1005_7031128593](#1005_7031128593) | 2/9 | 2/7 | 0/7 | 8 |
| [1005_7401573420](#1005_7401573420) | 11/20 | 2/23 | 1/23 | 14 |
| [1006_4580824633](#1006_4580824633) | 2/5 | 1/8 | 0/8 | 4 |
| [1007_6631583821](#1007_6631583821) | 3/10 | 0/12 | 0/12 | 13 |
| [1011_4633647136](#1011_4633647136) | 8/14 | 0/20 | 0/20 | 7 |
| [1012_4024008346](#1012_4024008346) | 5/11 | 5/8 | 2/8 | 9 |
| [1015_4698622422](#1015_4698622422) | 4/13 | 2/15 | 0/15 | 12 |
| [1017_3056841458](#1017_3056841458) | 4/14 | 3/16 | 0/16 | 14 |
| [1019_3768851893](#1019_3768851893) | 0/30 | 6/30 | 0/30 | 33 |
| [1020_2471845614](#1020_2471845614) | 10/22 | 6/27 | 0/27 | 24 |
| [1021_3478653250](#1021_3478653250) | 7/13 | 1/23 | 0/23 | 7 |
| [1021_4278168115](#1021_4278168115) | 8/11 | 8/21 | 7/21 | 5 |
| [1025_4615486172](#1025_4615486172) | 9/27 | 0/24 | 0/24 | 17 |
| [1025_6244382586](#1025_6244382586) | 5/11 | 5/12 | 1/12 | 12 |
| [1052_8530515192](#1052_8530515192) | 8/15 | 5/28 | 2/28 | 10 |
| [1100_9117425466](#1100_9117425466) | 4/8 | 0/15 | 0/15 | 6 |
| [1122_3393449055](#1122_3393449055) | 4/9 | 5/11 | 0/11 | 10 |
| [1124_9861436503](#1124_9861436503) | 5/13 | 1/11 | 0/11 | 10 |
| [1161_5895320023](#1161_5895320023) | 13/30 | 0/9 | 0/9 | 16 |
| [1164_6895784766](#1164_6895784766) | 6/16 | 0/14 | 0/14 | 9 |
| [1203_8316378691](#1203_8316378691) | 4/23 | 5/15 | 0/15 | 23 |
| [22cc4d54-34be-4580-983a-9e710e831c16](#22cc4d54-34be-4580-983a-9e710e831c16) | 0/10 | 0/18 | 0/18 | 0 |
| [6e0a6558-c212-4cab-b374-007671edb59c_2](#6e0a6558-c212-4cab-b374-007671edb59c_2) | 16/40 | 3/16 | 0/16 | 25 |
| [P02_10](#p02_10) | 10/28 | 2/5 | 0/5 | 20 |

## 0004_11566980553

57.4 s, 57 frames read | human: 15 objects, 13 relations | TRASER: 15 objects, 23 relations, valid JSON, 1344 tokens

**Objects: 6/15 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | floor | identical | ✓ |
| 2 | wall | wall | identical | ✓ |
| 3 | carpet | rug | synonym | ✓ |
| 4 | gift | blanket | not judged yet | ? |
| 5 | tv | television (uncertain) | not judged yet | ? |
| 6 | door | door frame (uncertain) | semantic overlap | ✓ |
| 7 | cabinet | sofa | not judged yet | ? |
| 8 | adult | person | not judged yet | ? |
| 9 | child | child | identical | ✓ |
| 10 | sofa | sofa | identical | ✓ |
| 11 | light | lampshade | not judged yet | ? |
| 12 | box | toy (uncertain) | not judged yet | ? |
| 13 | cellphone | cellular telephone (uncertain) | not judged yet | ? |
| 14 | gift | plastic bag | not judged yet | ? |
| 15 | cabinet | chair (uncertain) | not judged yet | ? |

**Relations: 0/13 right, triplets: 0/13 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| child #9 - holding - gift #14 | 24.6-27.6s | opens (+4 more) | 23.1614-27.1895s | not judged yet | 0.58 | ? | ? |
| child #9 - opening - gift #14 | 30.8-44.8s | holds (+4 more) | 23.1614-58.407s | not judged yet | 0.40 | ✗ | ✗ |
| child #9 - walking on - floor #1 | 0-2.6s, 4.2-6.6s, 20-21s, 24.4-26.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - standing on - floor #1 | 6.6-20s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - sitting on - carpet #3 | 27.4-57.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - holding - gift #4 | 2.6-6.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - sitting on - sofa #10 | 4.8-21.6s, 22.6-29.8s, 34-35.6s | on | 4.02807-21.1474s | not judged yet | 0.62 | ? | ? |
| adult #8 - grabbing - gift #4 | 12.2-13.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - looking at - cellphone #13 | 5-7s, 14.4-20s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - holding - box #12 | 44.4-57.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - carrying - gift #4 | 3.4-7.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - holding - gift #4 | 7.2-14.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - carrying - gift #14 | 23.4-27.2s | opens (+4 more) | 23.1614-27.1895s | not judged yet | 0.94 | ? | ? |

TRASER relations between pairs the humans did not annotate (17): child #9 - approaches - sofa #10 [1.00702-4.02807s]; child #9 - moves away from - sofa #10 [21.1474-24.1684s]; child #9 - in front of - sofa #10 [1.00702-58.407s]; sofa #10 - on - floor #1 [0-58.407s]; cabinet #7 - on - floor #1 [0-1.00702s, 3.02105-5.03509s, 17.1193-27.1895s, 33.2316-35.2456s]; carpet #3 - on - floor #1 [3.02105-6.04211s, 23.1614-58.407s]; sofa #10 - in front of - wall #2 [0-32.2246s]; cabinet #7 - in front of - wall #2 [0-1.00702s, 3.02105-5.03509s, 17.1193-27.1895s]; child #9 - in front of - wall #2 [1.00702-32.2246s]; gift #14 - on - carpet #3 [23.1614-58.407s]


## 0010_8610561401

36.0 s, 36 frames read | human: 5 objects, 8 relations | TRASER: 5 objects, 13 relations, valid JSON, 487 tokens

**Objects: 2/5 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | wall | curtain | not judged yet | ? |
| 2 | adult | person | not judged yet | ? |
| 3 | dog | dog | identical | ✓ |
| 4 | sofa | cushion | not judged yet | ? |
| 5 | sofa | sofa | identical | ✓ |

**Relations: 1/8 right, triplets: 0/8 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #2 - next to - dog #3 | 0-24.2s | petting (+1 more) | 0-37s | not judged yet | 0.65 | ? | ? |
| dog #3 - sitting on - sofa #5 | 0-1.2s, 32.8-36s | standing on (+1 more) | 0-37s | not judged yet | 0.12 | ✗ | ✗ |
| dog #3 - standing on - sofa #4 | 1.2-32.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #2 - sitting on - sofa #4 | 0-36s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #3 - looking at - adult #2 | 0-36s | looking at (+2 more) | 0-37s | identical | 0.97 | ✓ | ? |
| dog #3 - touching - sofa #4 | 8.8-10.2s, 16.2-19.2s, 28.6-30.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #2 - looking at - dog #3 | 24.4-36s | looking at (+1 more) | 0-37s | identical | 0.31 | ✗ | ✗ |
| adult #2 - caressing - dog #3 | 32.2-36s | petting (+1 more) | 0-37s | not judged yet | 0.10 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (6): adult #2 - on - sofa #5 [0-37s]; sofa #4 - on - sofa #5 [0-37s]; dog #3 - in front of - wall #1 [0-37s]; adult #2 - in front of - wall #1 [0-37s]; sofa #5 - in front of - wall #1 [0-37s]; sofa #4 - in front of - wall #1 [0-37s]


## 0018_4748191834

33.2 s, 33 frames read | human: 14 objects, 17 relations | TRASER: 13 objects, 29 relations, valid JSON, 1296 tokens

**Objects: 5/14 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | - | no label from TRASER | ✗ |
| 2 | floor | table | not judged yet | ? |
| 3 | wall | wall | identical | ✓ |
| 4 | cookie | cake slice | not judged yet | ? |
| 5 | door | cabinet door | not judged yet | ? |
| 6 | adult | person | not judged yet | ? |
| 7 | child | child | identical | ✓ |
| 8 | table | tablecloth | not judged yet | ? |
| 9 | chair | chair backrest | not judged yet | ? |
| 10 | candle | candle | identical | ✓ |
| 11 | cake | cake | identical | ✓ |
| 12 | camera | knife | not judged yet | ? |
| 13 | adult | shirt | not judged yet | ? |
| 14 | chair | chair | identical | ✓ |

**Relations: 3/17 right, triplets: 2/17 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #13 - in front of - wall #3 | 0-9.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #13 - walking on - floor #2 | 9.6-19s, 31.4-33.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - in front of - cake #11 | 0-33.4s | looking at | 0-25.1515s | not judged yet | 0.75 | ? | ? |
| child #7 - looking at - adult #6 | 6.8-8.6s | next to | 0-34.2061s | not judged yet | 0.05 | ✗ | ✗ |
| adult #6 - touching - child #7 | 9-22.6s | serving (+1 more) | 10.0606-25.1515s | not judged yet | 0.78 | ? | ? |
| child #7 - sitting on - chair #9 | 0-33.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| cake #11 - on - table #8 | 0-33.4s | on | 0-34.2061s | identical | 0.98 | ✓ | ? |
| candle #10 - on - cake #11 | 0-33.4s | on (+1 more) | 0-34.2061s | identical | 0.98 | ✓ | ✓ |
| adult #13 - holding - camera #12 | 0-32.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - looking at - cake #11 | 8.4-32s | looking at | 0-25.1515s | identical | 0.52 | ✓ | ✓ |
| adult #6 - beside - table #8 | 9-33.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #13 - beside - table #8 | 11-32s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #13 - touching - candle #10 | 20-21s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #13 - touching - cake #11 | 21-22.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - blowing - candle #10 | 22.4-26s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #6 - touching - candle #10 | 25.8-27s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #6 - hugging - child #7 | 7.6-22.6s | serving (+1 more) | 10.0606-25.1515s | not judged yet | 0.71 | ? | ? |

TRASER relations between pairs the humans did not annotate (22): child #7 - holding - cookie #4 [0-25.1515s]; adult #6 - holding - camera #12 [10.0606-25.1515s]; adult #6 - cutting - cake #11 [10.0606-25.1515s]; adult #6 - looking at - cake #11 [10.0606-25.1515s]; adult #6 - wearing - adult #13 [0-34.2061s]; child #7 - sitting on - chair #14 [0-34.2061s]; cake #11 - in front of - wall #3 [0-34.2061s]; child #7 - in front of - wall #3 [0-34.2061s]; adult #6 - in front of - wall #3 [0-34.2061s]; chair #9 - behind - child #7 [0-34.2061s]


## 0027_4571353789

19.0 s, 19 frames read | human: 16 objects, 17 relations | TRASER: 15 objects, 32 relations, valid JSON, 1398 tokens

**Objects: 3/16 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | tree | tree | identical | ✓ |
| 2 | ground | floor | synonym | ✓ |
| 3 | floor | - | no label from TRASER | ✗ |
| 4 | wall | tent | not judged yet | ? |
| 5 | adult | person | not judged yet | ? |
| 6 | table | tablecloth | not judged yet | ? |
| 7 | light | string of lights | not judged yet | ? |
| 8 | box | speaker | mismatch | ✗ |
| 9 | camera | hand | not judged yet | ? |
| 10 | car | car | identical | ✓ |
| 11 | adult | person | not judged yet | ? |
| 12 | light | string of lights | not judged yet | ? |
| 13 | camera | shoe | not judged yet | ? |
| 14 | adult | person | not judged yet | ? |
| 15 | adult | arm | not judged yet | ? |
| 16 | adult | person | not judged yet | ? |

**Relations: 1/17 right, triplets: 0/17 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #16 - walking on - ground #2 | 17.2-19s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - camera #9 | 0-19s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - standing on - ground #2 | 0-8.4s | on | 0-11s, 16-20s | not judged yet | 0.56 | ? | ? |
| adult #5 - walking on - ground #2 | 8.2-10.4s | on | 0-11s, 16-20s | not judged yet | 0.15 | ✗ | ✗ |
| adult #5 - looking at - adult #11 | 0-19s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - in front of - table #6 | 0-19s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - in front of - table #6 | 0-19s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - kissing - adult #11 | 5.6-7.2s | looking at (+2 more) | 0-11s | not judged yet | 0.15 | ✗ | ✗ |
| adult #14 - holding - adult #11 | 0-12.2s | looking at (+2 more) | 0-11s | not judged yet | 0.90 | ? | ? |
| box #8 - beside - table #6 | 0-19s | nothing for this pair | - | - | - | ✗ | ✗ |
| table #6 - beside - light #7 | 0-19s | under | 0-11s, 16-20s | not judged yet | 0.70 | ? | ? |
| table #6 - in front of - wall #4 | 0-19s | in front of | 0-11s, 16-20s | identical | 0.70 | ✓ | ? |
| adult #11 - holding - camera #9 | 17.6-18.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| light #7 - over - wall #4 | 0-19s | above | 0-20s | not judged yet | 0.95 | ? | ? |
| light #12 - over - wall #4 | 0-19s | above | 0-20s | not judged yet | 0.95 | ? | ? |
| adult #14 - hugging - adult #11 | 8-12s | looking at (+2 more) | 0-11s | not judged yet | 0.25 | ✗ | ✗ |
| adult #16 - holding - camera #13 | 17.2-19s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (24): adult #11 - holding hands with - adult #14 [0-11s]; adult #11 - moving away from - adult #14 [11-13s]; adult #11 - moving toward - adult #14 [16-19s]; adult #11 - hugging - adult #14 [18-20s]; adult #11 - looking at - adult #14 [0-11s]; adult #11 - next to - adult #14 [0-11s, 16-20s]; adult #11 - on - ground #2 [0-11s, 16-20s]; adult #14 - on - ground #2 [0-11s, 16-20s]; adult #11 - in front of - wall #4 [0-20s]; adult #14 - in front of - wall #4 [0-20s]


## 0028_4021064662

19.0 s, 19 frames read | human: 10 objects, 18 relations | TRASER: 10 objects, 25 relations, valid JSON, 939 tokens

**Objects: 3/10 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | track | not judged yet | ? |
| 2 | grass | soccer field | not judged yet | ? |
| 3 | adult | person | not judged yet | ? |
| 4 | child | child | identical | ✓ |
| 5 | bottle | bottle | identical | ✓ |
| 6 | hat | baseball cap | hypernym/hyponym | ✓ |
| 7 | bag | shoe | mismatch | ✗ |
| 8 | ball | shoe | not judged yet | ? |
| 9 | adult | arm | not judged yet | ? |
| 10 | adult | hand | not judged yet | ? |

**Relations: 2/18 right, triplets: 0/18 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #10 - in front of - adult #3 | 8.4-9s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #3 - looking at - child #4 | 2.2-4.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| bottle #5 - on - grass #2 | 0-19s | on | 0-19s | identical | 1.00 | ✓ | ? |
| bottle #5 - in front of - child #4 | 0-19s | near | 0-19s | not judged yet | 1.00 | ? | ? |
| bottle #5 - in front of - adult #3 | 0-19s | near | 0-19s | not judged yet | 1.00 | ? | ? |
| adult #3 - standing on - grass #2 | 0-19s | on | 0-19s | not judged yet | 1.00 | ? | ? |
| child #4 - wearing - hat #6 | 0-19s | nothing for this pair | - | - | - | ✗ | ✗ |
| bag #7 - on - grass #2 | 0-7.8s | on | 0-9s | identical | 0.87 | ✓ | ✗ |
| child #4 - sitting on - grass #2 | 0-1.2s | on | 0-19s | not judged yet | 0.06 | ✗ | ✗ |
| child #4 - holding - ball #8 | 1.8-3.8s, 11.2-19s | wearing | 0-19s | not judged yet | 0.52 | ? | ? |
| adult #3 - holding - ball #8 | 3.6-9.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #4 - standing on - grass #2 | 2.2-7.2s, 18.2-19s | on | 0-19s | not judged yet | 0.31 | ✗ | ✗ |
| child #4 - running on - grass #2 | 7-10s, 11.2-12.8s | on | 0-19s | not judged yet | 0.24 | ✗ | ✗ |
| child #4 - in front of - adult #3 | 7.6-8s | approaching (+3 more) | 0-11s | not judged yet | 0.04 | ✗ | ✗ |
| adult #3 - throwing - ball #8 | 9.6-10.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #4 - catching - ball #8 | 9.8-11.4s | wearing | 0-19s | not judged yet | 0.08 | ✗ | ✗ |
| child #4 - playing with - adult #3 | 12.6-18.6s | moving away from (+3 more) | 11-19s | not judged yet | 0.75 | ? | ? |
| adult #3 - hugging - child #4 | 12.4-15.2s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (14): adult #3 - wearing - hat #6 [0-19s]; child #4 - approaching - bottle #5 [10-13s]; child #4 - moving away from - bottle #5 [13-19s]; ball #8 - on - grass #2 [0-19s]; ground #1 - in front of - grass #2 [0-19s]; adult #3 - behind - ground #1 [0-19s]; child #4 - behind - ground #1 [0-19s]; bottle #5 - behind - ground #1 [0-19s]; bag #7 - behind - ground #1 [0-9s]; ball #8 - behind - ground #1 [0-19s]


## 0039_6951351121

15.8 s, 16 frames read | human: 17 objects, 13 relations | TRASER: 17 objects, 38 relations, valid JSON, 1565 tokens

**Objects: 6/17 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | sky | cloud | not judged yet | ? |
| 2 | tree | tree | identical | ✓ |
| 3 | grass | field | semantic overlap | ✓ |
| 4 | helmet | helmet | identical | ✓ |
| 5 | adult | person | not judged yet | ? |
| 6 | ball | hand | not judged yet | ? |
| 7 | helmet | helmet | identical | ✓ |
| 8 | adult | person | not judged yet | ? |
| 9 | ball | person | not judged yet | ? |
| 10 | helmet | helmet | identical | ✓ |
| 11 | adult | person | not judged yet | ? |
| 12 | ball | ball | identical | ✓ |
| 13 | helmet | jersey | not judged yet | ? |
| 14 | adult | shorts | not judged yet | ? |
| 15 | ball | arm | not judged yet | ? |
| 16 | adult | person | not judged yet | ? |
| 17 | adult | person | not judged yet | ? |

**Relations: 0/13 right, triplets: 0/13 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #17 - walking on - grass #3 | 1.4-4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - in front of - adult #17 | 1.8-3.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #17 - holding - ball #6 | 1.4-3.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #17 - holding - ball #9 | 1.4-3.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - holding - ball #12 | 15.2-15.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - running on - grass #3 | 0-2.2s, 13-14.2s | on | 0-1.975s, 13.825-15.8s | not judged yet | 0.47 | ✗ | ✗ |
| adult #8 - throwing - ball #12 | 1.6-3.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #16 - running on - grass #3 | 2.4-10.4s, 12.2-14.8s | on | 0-15.8s | not judged yet | 0.67 | ? | ? |
| adult #14 - running on - grass #3 | 4.6-5.8s, 12.2-14.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - catching - ball #12 | 5.6-9s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - throwing - ball #12 | 8.8-13s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - throwing - ball #15 | 13.2-13.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #16 - throwing - ball #12 | 13.8-15s | kicking (+2 more) | 13.825-14.8125s | not judged yet | 0.82 | ? | ? |

TRASER relations between pairs the humans did not annotate (33): adult #16 - wearing - helmet #7 [0-1.975s, 2.9625-15.8s]; adult #16 - in front of - helmet #7 [0-1.975s, 2.9625-15.8s]; adult #11 - wearing - helmet #10 [7.9-12.8375s]; adult #11 - wearing - helmet #13 [7.9-12.8375s]; adult #11 - wearing - adult #14 [7.9-12.8375s]; adult #16 - approaching - adult #11 [7.9-10.8625s]; adult #16 - moving away from - adult #11 [10.8625-12.8375s]; adult #16 - chasing - adult #11 [7.9-12.8375s]; adult #16 - in front of - adult #11 [7.9-12.8375s]; ball #12 - moving across - grass #3 [13.825-15.8s]


## 0046_11919433184

112.6 s, 113 frames read | human: 16 objects, 17 relations | TRASER: 15 objects, 12 relations, cut-off answer (salvaged), 4300 tokens

**Objects: 7/16 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | dog | not judged yet | ? |
| 2 | rock | stone wall | not judged yet | ? |
| 3 | grass | lawn | synonym | ✓ |
| 4 | wall | wall | identical | ✓ |
| 5 | door | plant | not judged yet | ? |
| 6 | window | window | identical | ✓ |
| 7 | fence | fence | identical | ✓ |
| 8 | adult | person | not judged yet | ? |
| 9 | child | child | identical | ✓ |
| 10 | ball | ball | identical | ✓ |
| 11 | window | flower arrangement | not judged yet | ? |
| 12 | fence | fence | identical | ✓ |
| 13 | ball | soccer ball | not judged yet | ? |
| 14 | window | window blind | not judged yet | ? |
| 15 | window | window blind | not judged yet | ? |
| 16 | window | - | no label from TRASER | ✗ |

**Relations: 1/17 right, triplets: 1/17 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| child #9 - kicking - ball #13 | 77.4-78.8s, 86.6-88s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - standing on - grass #3 | 0-1.6s, 4.4-7.8s | on | 0-110.607s | not judged yet | 0.05 | ✗ | ✗ |
| child #9 - kicking - ball #10 | 1.6-4.4s, 49.6-54.2s, 61.8-72s, 78-78.8s, 85.2-86s, 100-105.2s | playing with (+4 more) | 0-2.98938s, 3.98584-12.954s, 13.9504-14.9469s, 15.9434-16.9398s, 17.9363-20.9257s, 21.9221-22.9186s, 23.915-24.9115s, 25.908-26.9044s, 27.9009-30.8903s, 31.8867-32.8832s, 33.8796-34.8761s, 35.8726-36.869s, 37.8655-38.8619s, 39.8584-40.8549s, 41.8513-42.8478s, 43.8442-44.8407s, 45.8372-46.8336s, 47.8301-48.8265s, 49.823-50.8195s, 51.8159-52.8124s, 53.8088-54.8053s, 55.8018-56.7982s, 57.7947-58.7912s, 59.7876-60.7841s, 61.7805-62.777s, 63.7735-64.7699s, 65.7664-66.7628s, 67.7593-68.7558s, 69.7522-70.7487s, 71.7451-72.7416s, 73.7381-74.7345s, 75.731-76.7274s, 77.7239-78.7204s, 79.7168-80.7133s, 81.7097-82.7062s, 83.7027-84.6991s, 85.6956-86.692s, 87.6885-88.685s, 89.6814-90.6779s, 91.6743-92.6708s, 93.6673-94.6637s, 95.6602-96.6566s, 97.6531-98.6496s, 99.646-100.642s, 101.639-102.635s, 103.632-104.628s, 105.625-106.621s, 107.618-108.614s, 109.611-110.607s | not judged yet | 0.18 | ✗ | ✗ |
| child #9 - toward - ball #10 | 7.8-10s, 21-29.8s, 47.4-49.6s | playing with (+4 more) | 0-2.98938s, 3.98584-12.954s, 13.9504-14.9469s, 15.9434-16.9398s, 17.9363-20.9257s, 21.9221-22.9186s, 23.915-24.9115s, 25.908-26.9044s, 27.9009-30.8903s, 31.8867-32.8832s, 33.8796-34.8761s, 35.8726-36.869s, 37.8655-38.8619s, 39.8584-40.8549s, 41.8513-42.8478s, 43.8442-44.8407s, 45.8372-46.8336s, 47.8301-48.8265s, 49.823-50.8195s, 51.8159-52.8124s, 53.8088-54.8053s, 55.8018-56.7982s, 57.7947-58.7912s, 59.7876-60.7841s, 61.7805-62.777s, 63.7735-64.7699s, 65.7664-66.7628s, 67.7593-68.7558s, 69.7522-70.7487s, 71.7451-72.7416s, 73.7381-74.7345s, 75.731-76.7274s, 77.7239-78.7204s, 79.7168-80.7133s, 81.7097-82.7062s, 83.7027-84.6991s, 85.6956-86.692s, 87.6885-88.685s, 89.6814-90.6779s, 91.6743-92.6708s, 93.6673-94.6637s, 95.6602-96.6566s, 97.6531-98.6496s, 99.646-100.642s, 101.639-102.635s, 103.632-104.628s, 105.625-106.621s, 107.618-108.614s, 109.611-110.607s | not judged yet | 0.12 | ✗ | ✗ |
| child #9 - picking - ball #10 | 10-11.2s, 93.6-95s | approaching (+4 more) | 9.9646-11.9575s | not judged yet | 0.35 | ✗ | ✗ |
| child #9 - toward - adult #8 | 11.2-14s | playing with | 0-2.98938s, 3.98584-10.9611s | not judged yet | 0.00 | ✗ | ✗ |
| adult #8 - standing on - grass #3 | 0-19s | on | 0-47.8301s, 55.8018-64.7699s, 69.7522-70.7487s, 75.731-88.685s, 103.632-108.614s | not judged yet | 0.25 | ✗ | ✗ |
| adult #8 - picking - ball #10 | 19-20.4s, 41.6-43.6s | holding | 0-2.98938s, 3.98584-10.9611s | not judged yet | 0.00 | ✗ | ✗ |
| child #9 - next to - adult #8 | 12.8-47.6s, 57.8-64.6s | playing with | 0-2.98938s, 3.98584-10.9611s | not judged yet | 0.00 | ✗ | ✗ |
| adult #8 - pulling - child #9 | 60.6-62s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - picking - ball #13 | 73.2-76s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - chasing - ball #13 | 78.8-85s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - holding - ball #10 | 94.8-99.8s | holding (+4 more) | 10.9611-12.954s, 13.9504-14.9469s, 15.9434-16.9398s, 17.9363-20.9257s, 21.9221-22.9186s, 23.915-24.9115s, 25.908-26.9044s, 27.9009-30.8903s, 31.8867-32.8832s, 33.8796-34.8761s, 35.8726-36.869s, 37.8655-38.8619s, 39.8584-40.8549s, 41.8513-42.8478s, 43.8442-44.8407s, 45.8372-46.8336s, 47.8301-48.8265s, 49.823-50.8195s, 51.8159-52.8124s, 53.8088-54.8053s, 55.8018-56.7982s, 57.7947-58.7912s, 59.7876-60.7841s, 61.7805-62.777s, 63.7735-64.7699s, 65.7664-66.7628s, 67.7593-68.7558s, 69.7522-70.7487s, 71.7451-72.7416s, 73.7381-74.7345s, 75.731-76.7274s, 77.7239-78.7204s, 79.7168-80.7133s, 81.7097-82.7062s, 83.7027-84.6991s, 85.6956-86.692s, 87.6885-88.685s, 89.6814-90.6779s, 91.6743-92.6708s, 93.6673-94.6637s, 95.6602-96.6566s, 97.6531-98.6496s, 99.646-100.642s, 101.639-102.635s, 103.632-104.628s, 105.625-106.621s, 107.618-108.614s, 109.611-110.607s | identical | 0.04 | ✗ | ✗ |
| child #9 - running on - grass #3 | 105.2-112.8s | on | 0-110.607s | not judged yet | 0.05 | ✗ | ✗ |
| child #9 - jumping from - grass #3 | 20.8-33s, 38.6-40.6s, 44.2-45.8s | on | 0-110.607s | not judged yet | 0.14 | ✗ | ✗ |
| child #9 - playing with - ball #10 | 0-112.8s | playing with (+4 more) | 0-2.98938s, 3.98584-12.954s, 13.9504-14.9469s, 15.9434-16.9398s, 17.9363-20.9257s, 21.9221-22.9186s, 23.915-24.9115s, 25.908-26.9044s, 27.9009-30.8903s, 31.8867-32.8832s, 33.8796-34.8761s, 35.8726-36.869s, 37.8655-38.8619s, 39.8584-40.8549s, 41.8513-42.8478s, 43.8442-44.8407s, 45.8372-46.8336s, 47.8301-48.8265s, 49.823-50.8195s, 51.8159-52.8124s, 53.8088-54.8053s, 55.8018-56.7982s, 57.7947-58.7912s, 59.7876-60.7841s, 61.7805-62.777s, 63.7735-64.7699s, 65.7664-66.7628s, 67.7593-68.7558s, 69.7522-70.7487s, 71.7451-72.7416s, 73.7381-74.7345s, 75.731-76.7274s, 77.7239-78.7204s, 79.7168-80.7133s, 81.7097-82.7062s, 83.7027-84.6991s, 85.6956-86.692s, 87.6885-88.685s, 89.6814-90.6779s, 91.6743-92.6708s, 93.6673-94.6637s, 95.6602-96.6566s, 97.6531-98.6496s, 99.646-100.642s, 101.639-102.635s, 103.632-104.628s, 105.625-106.621s, 107.618-108.614s, 109.611-110.607s | identical | 0.56 | ✓ | ✓ |
| child #9 - playing with - ball #13 | 77.4-88s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (3): child #9 - in front of - fence #12 [105.625-110.607s]; adult #8 - in front of - fence #12 [105.625-110.607s]; ball #10 - in front of - fence #12 [105.625-110.607s]


## 0051_3702633786

49.0 s, 49 frames read | human: 12 objects, 15 relations | TRASER: 12 objects, 13 relations, valid JSON, 1195 tokens

**Objects: 1/12 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | tree | person | not judged yet | ? |
| 2 | ground | dog | not judged yet | ? |
| 3 | rock | bathtub | not judged yet | ? |
| 4 | water | hand | not judged yet | ? |
| 5 | adult | person | not judged yet | ? |
| 6 | dog | dog | identical | ✓ |
| 7 | bottle | bowl | not judged yet | ? |
| 8 | adult | person | not judged yet | ? |
| 9 | dog | person | not judged yet | ? |
| 10 | adult | person | not judged yet | ? |
| 11 | adult | person | not judged yet | ? |
| 12 | adult | person | not judged yet | ? |

**Relations: 0/15 right, triplets: 0/15 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #8 - walking on - ground #2 | 0-2.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #6 - in - water #4 | 0-38.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #6 - walking on - ground #2 | 43-47.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #6 - next to - adult #5 | 42.8-46.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - holding - bottle #7 | 0-49s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - beside - rock #3 | 0-37.2s, 46.8-49s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - dog #6 | 0-49s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - holding - dog #9 | 38.2-49s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - walking on - ground #2 | 38.2-49s | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #1 - in front of - adult #11 | 0-17.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - next to - adult #11 | 2.8-15.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - cleaning - dog #6 | 0-36.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - watering - dog #6 | 4.6-5.6s, 7.4-8.8s, 11-13.4s, 17.4-20.4s, 22.4-33s, 34.4-35.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #6 - jumping over - rock #3 | 38.8-42.8s | inside | 0-4s, 5-22s, 23-34s, 35-37s, 38-42s, 43-44s | not judged yet | 0.08 | ✗ | ✗ |
| adult #5 - guiding - dog #6 | 38.2-46.4s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (12): adult #10 - wash - dog #6 [0-4s, 5-22s, 23-34s, 35-37s, 38-42s, 43-44s]; adult #10 - hold - dog #6 [0-4s, 5-22s, 23-34s, 35-37s, 38-42s, 43-44s]; adult #10 - bathe - dog #6 [0-4s, 5-22s, 23-34s, 35-37s, 38-42s, 43-44s]; bottle #7 - inside - rock #3 [0-1s, 3-4s, 5-22s, 23-34s, 35-37s, 38-40s]; water #4 - touching - dog #6 [0-4s, 5-22s, 23-34s, 35-37s, 38-42s, 43-44s]; water #4 - inside - rock #3 [0-4s, 5-22s, 23-34s, 35-37s, 38-42s, 43-44s]; dog #6 - in front of - adult #10 [0-4s, 5-22s, 23-34s, 35-37s, 38-42s, 43-44s]; bottle #7 - in front of - adult #10 [0-1s, 3-4s, 5-22s, 23-34s, 35-37s, 38-40s]; rock #3 - in front of - adult #10 [0-4s, 5-22s, 23-34s, 35-37s, 38-42s, 43-44s]; dog #6 - in front of - adult #8 [0-4s, 5-22s]


## 0053_5599511471

28.4 s, 28 frames read | human: 7 objects, 14 relations | TRASER: 6 objects, 11 relations, valid JSON, 587 tokens

**Objects: 1/7 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | tree | - | no label from TRASER | ✗ |
| 2 | grass | person | mismatch | ✗ |
| 3 | helmet | helmet | identical | ✓ |
| 4 | adult | jersey | not judged yet | ? |
| 5 | ball | basketball | not judged yet | ? |
| 6 | adult | person | not judged yet | ? |
| 7 | adult | person | not judged yet | ? |

**Relations: 1/14 right, triplets: 0/14 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #7 - wearing - helmet #3 | 3.8-28.4s | wearing | 5.07143-18.2571s, 19.2714-29.4143s | identical | 0.87 | ✓ | ? |
| adult #4 - holding - ball #5 | 0-0.6s, 14.2-28.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #6 - catching - ball #5 | 2.8-3.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - walking on - grass #2 | 13.6-25.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - standing on - grass #2 | 24.6-28.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #6 - running on - grass #2 | 1.4-9.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #6 - walking on - grass #2 | 9.6-25.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #6 - standing on - grass #2 | 24.6-28.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - running on - grass #2 | 1-9.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - walking on - grass #2 | 9.6-25.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - standing on - grass #2 | 24.6-28.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #6 - holding - ball #5 | 3.6-13.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #6 - throwing - ball #5 | 13.6-14.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - catching - ball #5 | 14-14.4s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (10): adult #7 - holding - ball #5 [5.07143-18.2571s, 20.2857-29.4143s]; adult #7 - carrying - ball #5 [5.07143-18.2571s, 20.2857-29.4143s]; adult #7 - playing with - ball #5 [5.07143-18.2571s, 20.2857-29.4143s]; ball #5 - moving with - adult #7 [5.07143-18.2571s, 20.2857-29.4143s]; ball #5 - in front of - adult #7 [5.07143-18.2571s, 20.2857-29.4143s]; helmet #3 - on - adult #7 [5.07143-18.2571s, 19.2714-29.4143s]; ball #5 - below - helmet #3 [5.07143-18.2571s, 20.2857-29.4143s]; adult #4 - on - adult #6 [0-4.05714s, 14.2-18.2571s, 20.2857-29.4143s]; ball #5 - in front of - adult #6 [0-4.05714s, 14.2-18.2571s, 20.2857-29.4143s]; ball #5 - in front of - adult #4 [0-4.05714s, 14.2-18.2571s, 20.2857-29.4143s]


## 0054_2612939953

74.2 s, 74 frames read | human: 15 objects, 17 relations | TRASER: 15 objects, 74 relations, valid JSON, 2291 tokens

**Objects: 5/15 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | sky | horse | not judged yet | ? |
| 2 | tree | tree | identical | ✓ |
| 3 | ground | horse | not judged yet | ? |
| 4 | adult | person | not judged yet | ? |
| 5 | horse | horse | identical | ✓ |
| 6 | hat | hat | identical | ✓ |
| 7 | adult | person | not judged yet | ? |
| 8 | horse | horse | identical | ✓ |
| 9 | hat | umbrella | not judged yet | ? |
| 10 | adult | horse | not judged yet | ? |
| 11 | hat | hat | identical | ✓ |
| 12 | adult | person | not judged yet | ? |
| 13 | adult | person | not judged yet | ? |
| 14 | adult | person | not judged yet | ? |
| 15 | adult | person | not judged yet | ? |

**Relations: 2/17 right, triplets: 0/17 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #4 - wearing - hat #6 | 0-20.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - wearing - hat #9 | 20.6-66.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - riding - horse #5 | 0-8.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - going down - horse #5 | 8-11.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - riding - horse #5 | 0-20.2s | riding | 0-11.0297s, 15.0405-20.0541s | identical | 0.79 | ✓ | ? |
| adult #12 - looking at - adult #4 | 9.2-11.6s | riding (+2 more) | 68.1838-74.2s | not judged yet | 0.00 | ✗ | ✗ |
| adult #10 - riding - horse #5 | 18.2-74.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - riding - horse #8 | 0-74.2s | riding (+2 more) | 21.0568-40.1081s, 41.1108-60.1622s | identical | 0.51 | ✓ | ? |
| adult #13 - riding - horse #8 | 15.4-20.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #13 - going down - horse #8 | 26.2-33.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - looking at - adult #13 | 26.2-33.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - riding - horse #8 | 42.4-74.2s | riding (+2 more) | 21.0568-40.1081s, 41.1108-60.1622s | identical | 0.34 | ✗ | ✗ |
| adult #7 - getting down on - horse #5 | 8-11.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - pulling - adult #13 | 14-18s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - pulling - adult #15 | 26.4-33.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #15 - getting down on - horse #5 | 26.4-33.2s | riding (+2 more) | 68.1838-74.2s | not judged yet | 0.00 | ✗ | ✗ |
| adult #14 - pulling - adult #12 | 37.4-43s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (61): adult #15 - riding - horse #8 [21.0568-40.1081s, 41.1108-60.1622s]; adult #15 - riding - horse #8 [21.0568-40.1081s, 41.1108-60.1622s]; adult #15 - riding - horse #8 [21.0568-40.1081s, 41.1108-60.1622s]; adult #12 - riding - ground #3 [30.0811-60.1622s]; adult #12 - riding - ground #3 [30.0811-60.1622s]; adult #12 - riding - ground #3 [30.0811-60.1622s]; adult #14 - riding - ground #3 [30.0811-60.1622s]; adult #14 - riding - ground #3 [30.0811-60.1622s]; adult #14 - riding - ground #3 [30.0811-60.1622s]; adult #15 - riding - ground #3 [30.0811-60.1622s]


## 0057_7001078933

21.2 s, 21 frames read | human: 15 objects, 18 relations | TRASER: 15 objects, 36 relations, valid JSON, 1481 tokens

**Objects: 6/15 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | tree | tree | identical | ✓ |
| 2 | grass | soccer field | not judged yet | ? |
| 3 | helmet | helmet | identical | ✓ |
| 4 | adult | person | not judged yet | ? |
| 5 | hat | beanie | not judged yet | ? |
| 6 | helmet | helmet | identical | ✓ |
| 7 | adult | person | not judged yet | ? |
| 8 | helmet | helmet | identical | ✓ |
| 9 | adult | jacket | not judged yet | ? |
| 10 | helmet | helmet | identical | ✓ |
| 11 | adult | person | not judged yet | ? |
| 12 | helmet | helmet | identical | ✓ |
| 13 | adult | person | not judged yet | ? |
| 14 | adult | person | not judged yet | ? |
| 15 | adult | jersey | not judged yet | ? |

**Relations: 2/18 right, triplets: 0/18 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #4 - standing on - grass #2 | 3-10.2s | moving across (+2 more) | 0-9.08571s | not judged yet | 0.60 | ? | ? |
| adult #4 - wearing - helmet #3 | 0-21s | wearing | 0-9.08571s | identical | 0.43 | ✗ | ✗ |
| adult #7 - wearing - helmet #6 | 0-19.2s | wearing | 0-20.1905s | identical | 0.95 | ✓ | ? |
| adult #9 - wearing - hat #5 | 0-11.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - wearing - helmet #8 | 0-3s | wearing | 0-7.06667s | identical | 0.42 | ✗ | ✗ |
| adult #13 - wearing - helmet #10 | 9.4-17.2s | wearing | 7.06667-16.1524s | identical | 0.67 | ✓ | ? |
| adult #15 - wearing - helmet #12 | 17-18.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - standing on - grass #2 | 16-19.2s | moving across (+2 more) | 16.1524-19.181s | not judged yet | 0.95 | ? | ? |
| adult #4 - walking on - grass #2 | 0-3s | moving across (+2 more) | 0-9.08571s | not judged yet | 0.33 | ✗ | ✗ |
| adult #7 - walking on - grass #2 | 0-3s | moving across (+2 more) | 0-20.1905s | not judged yet | 0.15 | ✗ | ✗ |
| adult #9 - walking on - grass #2 | 0-3s | above | 0-7.06667s | not judged yet | 0.42 | ✗ | ✗ |
| adult #11 - standing on - grass #2 | 0-3s | moving across (+2 more) | 0-7.06667s | not judged yet | 0.42 | ✗ | ✗ |
| adult #9 - getting down on - grass #2 | 6-7.6s | above | 0-7.06667s | not judged yet | 0.14 | ✗ | ✗ |
| adult #7 - pushing - adult #13 | 11.4-13.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - pushing - adult #14 | 14.8-15.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - pushing - adult #15 | 17-17.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - squatting on - grass #2 | 6.2-7.6s | above | 0-7.06667s | not judged yet | 0.11 | ✗ | ✗ |
| adult #13 - squatting on - grass #2 | 8.8-11.8s | moving across (+2 more) | 7.06667-16.1524s | not judged yet | 0.33 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (16): adult #11 - wearing - adult #9 [0-7.06667s]; adult #14 - wearing - helmet #12 [16.1524-19.181s]; adult #14 - wearing - adult #15 [16.1524-19.181s]; tree #1 - behind - grass #2 [0-11.1048s, 12.1143-13.1238s, 14.1333-15.1429s, 16.1524-17.1619s, 18.1714-19.181s, 20.1905-22.2095s]; adult #7 - in front of - tree #1 [0-11.1048s, 12.1143-13.1238s, 14.1333-15.1429s, 16.1524-17.1619s, 18.1714-19.181s]; adult #4 - in front of - tree #1 [0-9.08571s, 18.1714-19.181s]; adult #11 - in front of - tree #1 [0-7.06667s, 21.2-22.2095s]; adult #13 - in front of - tree #1 [7.06667-11.1048s, 12.1143-13.1238s, 14.1333-15.1429s, 16.1524-17.1619s, 18.1714-19.181s]; adult #14 - in front of - tree #1 [16.1524-17.1619s, 18.1714-19.181s]; helmet #6 - above - adult #7 [0-20.1905s]


## 0062_6430774273

90.0 s, 90 frames read | human: 6 objects, 13 relations | TRASER: 6 objects, 16 relations, valid JSON, 651 tokens

**Objects: 3/6 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | adult | blanket | not judged yet | ? |
| 2 | child | child | identical | ✓ |
| 3 | baby | baby | identical | ✓ |
| 4 | bed | blanket | not judged yet | ? |
| 5 | sofa | sofa | identical | ✓ |
| 6 | camera | remote control | not judged yet | ? |

**Relations: 0/13 right, triplets: 0/13 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #1 - touching - child #2 | 1.8-16.8s, 32.4-44.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #1 - touching - baby #3 | 81-83s | nothing for this pair | - | - | - | ✗ | ✗ |
| baby #3 - lying on - bed #4 | 0-90s | on | 0-90s | not judged yet | 1.00 | ? | ? |
| child #2 - sitting on - bed #4 | 5-23s, 34-47s, 50-52.2s, 60-76.2s | on | 0-90s | not judged yet | 0.55 | ? | ? |
| child #2 - kissing - baby #3 | 24-26.2s, 48-50.2s, 52-56.6s | next to (+5 more) | 0-90s | not judged yet | 0.10 | ✗ | ✗ |
| child #2 - caressing - baby #3 | 27-29.8s, 76.8-79.8s | looks at (+5 more) | 27-32s | not judged yet | 0.35 | ✗ | ✗ |
| child #2 - touching - baby #3 | 30.6-32s | looks at (+5 more) | 27-32s | not judged yet | 0.28 | ✗ | ✗ |
| child #2 - lying on - bed #4 | 76.8-79.8s | on | 0-90s | not judged yet | 0.03 | ✗ | ✗ |
| child #2 - looking at - baby #3 | 84-85.6s | next to (+5 more) | 0-90s | not judged yet | 0.02 | ✗ | ✗ |
| adult #1 - holding - camera #6 | 28.4-31.2s, 49.6-53s, 58.6-60.4s, 67-69.2s, 78.6-83.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #1 - caressing - child #2 | 50.8-52s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #1 - carrying - child #2 | 3.2-4.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #2 - hugging - baby #3 | 26.8-31s, 76.8-79.2s | looks at (+5 more) | 27-32s | not judged yet | 0.53 | ? | ? |

TRASER relations between pairs the humans did not annotate (8): child #2 - holds - camera #6 [79-84s]; child #2 - in front of - sofa #5 [0-90s]; baby #3 - in front of - sofa #5 [0-90s]; bed #4 - in front of - sofa #5 [0-90s]; adult #1 - in front of - sofa #5 [0-20s, 29-62s, 64-73s, 76-84s, 88-90s]; camera #6 - on - bed #4 [79-84s]; camera #6 - in front of - sofa #5 [79-84s]; camera #6 - near - child #2 [79-84s]


## 0069_2740320945

73.6 s, 74 frames read | human: 20 objects, 16 relations | TRASER: 20 objects, 20 relations, valid JSON, 2315 tokens

**Objects: 6/20 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | sky | sky | identical | ✓ |
| 2 | tree | tree | identical | ✓ |
| 3 | ground | stone structure | not judged yet | ? |
| 4 | rock | fountain | not judged yet | ? |
| 5 | grass | bush | semantic overlap | ✓ |
| 6 | wall | building | not judged yet | ? |
| 7 | water | pool | not judged yet | ? |
| 8 | shoe | shoe | identical | ✓ |
| 9 | dustbin | trash can | not judged yet | ? |
| 10 | adult | person | not judged yet | ? |
| 11 | bottle | bottle | identical | ✓ |
| 12 | hat | umbrella | not judged yet | ? |
| 13 | camera | hat | not judged yet | ? |
| 14 | shoe | shoe | identical | ✓ |
| 15 | adult | person | not judged yet | ? |
| 16 | adult | dress | not judged yet | ? |
| 17 | adult | person | not judged yet | ? |
| 18 | adult | person | not judged yet | ? |
| 19 | adult | person | not judged yet | ? |
| 20 | adult | person | not judged yet | ? |

**Relations: 0/16 right, triplets: 0/16 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #15 - holding - bottle #11 | 35.8-65.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - holding - bottle #11 | 39.6-44.2s, 47-53.8s, 72-73.8s | holding (+1 more) | 19.8919-20.8865s, 21.8811-22.8757s, 23.8703-24.8649s, 25.8595-26.8541s, 27.8486-28.8432s, 29.8378-30.8324s, 31.827-32.8216s, 33.8162-34.8108s, 35.8054-36.8s, 37.7946-38.7892s, 39.7838-40.7784s, 41.773-42.7676s, 43.7622-44.7568s, 45.7514-46.7459s, 47.7405-48.7351s, 49.7297-50.7243s, 51.7189-52.7135s, 53.7081-54.7027s, 55.6973-56.6919s, 57.6865-58.6811s, 59.6757-60.6703s, 61.6649-62.6595s, 63.6541-64.6486s, 65.6432-66.6378s, 67.6324-68.627s, 69.6216-70.6162s, 71.6108-72.6054s | identical | 0.18 | ✗ | ✗ |
| adult #17 - holding - camera #13 | 0-1.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #15 - walking on - water #7 | 0-40.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - kissing - adult #15 | 40-43.6s | dancing with (+2 more) | 15.9135-66.6378s | not judged yet | 0.07 | ✗ | ✗ |
| adult #10 - entering - water #7 | 14-31.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - toward - adult #18 | 28.4-37s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - next to - adult #17 | 11-15.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - in front of - adult #15 | 15.6-34.6s | dancing with (+2 more) | 15.9135-66.6378s | not judged yet | 0.37 | ✗ | ✗ |
| adult #10 - holding - adult #15 | 34.4-66.2s, 72-73.8s | dancing with (+2 more) | 15.9135-66.6378s | not judged yet | 0.61 | ? | ? |
| adult #15 - drinking from - bottle #11 | 47-49.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - drinking from - bottle #11 | 50.8-53.4s | holding (+1 more) | 19.8919-20.8865s, 21.8811-22.8757s, 23.8703-24.8649s, 25.8595-26.8541s, 27.8486-28.8432s, 29.8378-30.8324s, 31.827-32.8216s, 33.8162-34.8108s, 35.8054-36.8s, 37.7946-38.7892s, 39.7838-40.7784s, 41.773-42.7676s, 43.7622-44.7568s, 45.7514-46.7459s, 47.7405-48.7351s, 49.7297-50.7243s, 51.7189-52.7135s, 53.7081-54.7027s, 55.6973-56.6919s, 57.6865-58.6811s, 59.6757-60.6703s, 61.6649-62.6595s, 63.6541-64.6486s, 65.6432-66.6378s, 67.6324-68.627s, 69.6216-70.6162s, 71.6108-72.6054s | not judged yet | 0.03 | ✗ | ✗ |
| adult #16 - next to - adult #15 | 5.6-9s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - next to - adult #18 | 10.8-14.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #17 - in front of - adult #16 | 0-1s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #20 - pulling - adult #19 | 70-70.8s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (15): adult #10 - in front of - rock #4 [0-66.6378s, 71.6108-73.6s]; adult #15 - in front of - rock #4 [0-66.6378s, 71.6108-73.6s]; adult #10 - in front of - wall #6 [0-66.6378s, 71.6108-73.6s]; adult #15 - in front of - wall #6 [0-66.6378s, 71.6108-73.6s]; rock #4 - in front of - wall #6 [0-73.6s]; rock #4 - in front of - tree #2 [0-73.6s]; water #7 - inside - rock #4 [0-73.6s]; water #7 - in front of - wall #6 [0-73.6s]; water #7 - in front of - tree #2 [0-73.6s]; grass #5 - behind - rock #4 [0-73.6s]


## 0075_11566764085

58.8 s, 59 frames read | human: 10 objects, 12 relations | TRASER: 9 objects, 32 relations, valid JSON, 1212 tokens

**Objects: 3/10 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | floorboard | not judged yet | ? |
| 2 | carpet | rug | synonym | ✓ |
| 3 | scissor | scissors | not judged yet | ? |
| 4 | adult | person | not judged yet | ? |
| 5 | child | child | identical | ✓ |
| 6 | sofa | chair | not judged yet | ? |
| 7 | chair | chair | identical | ✓ |
| 8 | box | cardboard box | not judged yet | ? |
| 9 | toy | toy car | not judged yet | ? |
| 10 | child | - | no label from TRASER | ✗ |

**Relations: 1/12 right, triplets: 0/12 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #4 - sitting on - sofa #6 | 0-29s, 51-58.8s | holding (+1 more) | 50.8271-59.7966s | not judged yet | 0.21 | ✗ | ✗ |
| adult #4 - holding - scissor #3 | 0-9s, 9.8-17.8s, 21.2-26.8s | holding | 0-1.99322s, 2.98983-16.9424s, 17.939-27.9051s | identical | 0.75 | ✓ | ? |
| adult #4 - opening - box #8 | 0-9s, 9.8-17.8s, 21.2-26.8s | cutting open (+3 more) | 0-27.9051s | not judged yet | 0.81 | ? | ? |
| adult #4 - walking on - carpet #2 | 38.4-40.8s | above | 0-27.9051s, 33.8847-43.8508s, 50.8271-59.7966s | not judged yet | 0.05 | ✗ | ✗ |
| adult #4 - grabbing - toy #9 | 49.2-51.2s | holding (+3 more) | 29.8983-33.8847s | not judged yet | 0.00 | ✗ | ✗ |
| adult #4 - holding - toy #9 | 49.8-58.8s | holding (+3 more) | 29.8983-33.8847s | identical | 0.00 | ✗ | ✗ |
| adult #4 - looking at - toy #9 | 49.2-58.8s | holding (+3 more) | 29.8983-33.8847s | not judged yet | 0.00 | ✗ | ✗ |
| child #5 - standing on - carpet #2 | 16.4-19.6s, 20.2-24.4s, 34.4-51.4s | above | 0-7.97288s, 17.939-27.9051s, 29.8983-52.8203s | not judged yet | 0.54 | ? | ? |
| child #5 - opening - box #8 | 27.2-31.2s | holding (+1 more) | 17.939-27.9051s | not judged yet | 0.05 | ✗ | ✗ |
| child #5 - grabbing - toy #9 | 32-42.4s | touching (+1 more) | 29.8983-36.8746s | not judged yet | 0.39 | ✗ | ✗ |
| child #5 - holding - toy #9 | 42.4-51.2s | holding (+1 more) | 29.8983-33.8847s | identical | 0.00 | ✗ | ✗ |
| child #5 - looking at - toy #9 | 42.2-46.2s | holding (+1 more) | 29.8983-33.8847s | not judged yet | 0.00 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (15): toy #9 - moving toward - box #8 [33.8847-36.8746s]; toy #9 - near - box #8 [29.8983-43.8508s]; child #5 - holding - sofa #6 [50.8271-52.8203s]; child #5 - touching - sofa #6 [50.8271-52.8203s]; adult #4 - holding - child #5 [50.8271-52.8203s]; adult #4 - playing with - child #5 [50.8271-59.7966s]; carpet #2 - on - floor #1 [0-35.878s, 41.8576-59.7966s]; box #8 - on - carpet #2 [0-43.8508s]; box #8 - on - floor #1 [0-35.878s]; sofa #6 - on - floor #1 [0-1.99322s, 9.9661-27.9051s, 41.8576-59.7966s]


## 0096_5296138427

19.4 s, 19 frames read | human: 11 objects, 12 relations | TRASER: 10 objects, 20 relations, valid JSON, 880 tokens

**Objects: 5/11 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | - | no label from TRASER | ✗ |
| 2 | floor | floor | identical | ✓ |
| 3 | towel | napkin | not judged yet | ? |
| 4 | adult | person | not judged yet | ? |
| 5 | table | table | identical | ✓ |
| 6 | chair | chair | identical | ✓ |
| 7 | towel | napkin | not judged yet | ? |
| 8 | adult | person | not judged yet | ? |
| 9 | chair | chair | identical | ✓ |
| 10 | adult | person | not judged yet | ? |
| 11 | chair | chair | identical | ✓ |

**Relations: 2/12 right, triplets: 0/12 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #4 - standing on - floor #2 | 0-19.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - pulling - chair #6 | 4.8-6.4s | sitting on (+1 more) | 0-20.4211s | not judged yet | 0.08 | ✗ | ✗ |
| adult #4 - pushing - chair #6 | 6.2-14.8s | sitting on (+1 more) | 0-20.4211s | not judged yet | 0.42 | ✗ | ✗ |
| adult #4 - holding - towel #7 | 16.8-19.4s | holding | 17.3579-20.4211s | identical | 0.56 | ✓ | ? |
| adult #4 - touching - chair #9 | 18.6-19.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - in front of - adult #10 | 0-7.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - holding - towel #3 | 0-3.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - sitting on - chair #6 | 11-19.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| table #5 - beside - chair #6 | 0-19.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| table #5 - beside - chair #9 | 0-19.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| towel #3 - on - table #5 | 3.6-19.4s | on | 0-20.4211s | identical | 0.77 | ✓ | ? |
| towel #7 - on - chair #9 | 0-17s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (16): adult #8 - sitting on - chair #9 [0-20.4211s]; adult #8 - on - chair #9 [0-20.4211s]; adult #4 - looking at - adult #8 [0-20.4211s]; adult #4 - next to - adult #8 [0-20.4211s]; adult #8 - looking at - adult #4 [0-20.4211s]; chair #6 - on - floor #2 [0-20.4211s]; chair #9 - on - floor #2 [0-20.4211s]; chair #11 - on - floor #2 [0-20.4211s]; table #5 - on - floor #2 [0-20.4211s]; adult #4 - in front of - table #5 [0-20.4211s]


## 0be30efe-9d71-4698-8304-f1d441aeea58_1

94.0 s, 94 frames read | human: 12 objects, 10 relations | TRASER: 12 objects, 29 relations, valid JSON, 1448 tokens

**Objects: 2/12 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | person | mismatch | ✗ |
| 2 | grass | person | mismatch | ✗ |
| 3 | floor | person | mismatch | ✗ |
| 4 | wall | mat (uncertain) | not judged yet | ? |
| 5 | brush | tool (uncertain) | not judged yet | ? |
| 6 | stairs | wooden beam | not judged yet | ? |
| 7 | fence | wooden beam | not judged yet | ? |
| 8 | adult | person | not judged yet | ? |
| 9 | table | person | not judged yet | ? |
| 10 | chair | chair | identical | ✓ |
| 11 | car | car | identical | ✓ |
| 12 | stairs | bench | not judged yet | ? |

**Relations: 0/10 right, triplets: 0/10 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #8 - holding - brush #5 | 0-94s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - walking on - grass #2 | 0-11.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - walking on - stairs #6 | 11.6-13s | holding (+4 more) | 0-17s, 85-95s | not judged yet | 0.05 | ✗ | ✗ |
| adult #8 - walking on - floor #3 | 13-91s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - touching - fence #7 | 2-9.4s, 14.8-15.6s, 21.6-22.6s, 35.2-36.8s, 51.2-52.8s, 64.4-71s, 79.4-81.4s, 91.4-94s | holding (+4 more) | 0-95s | not judged yet | 0.25 | ✗ | ✗ |
| adult #8 - carrying - chair #10 | 18.4-19.8s | sanding (+2 more) | 14-54s, 55-67s, 85-95s | not judged yet | 0.02 | ✗ | ✗ |
| adult #8 - brushing - fence #7 | 0-1.4s, 3-10.6s, 14.8-17.6s, 23.4-94s | holding (+4 more) | 0-95s | not judged yet | 0.87 | ? | ? |
| adult #8 - pulling - chair #10 | 18.4-19.8s | sanding (+2 more) | 14-54s, 55-67s, 85-95s | not judged yet | 0.02 | ✗ | ✗ |
| adult #8 - getting down on - stairs #6 | 9-10.6s | holding (+4 more) | 0-17s, 85-95s | not judged yet | 0.06 | ✗ | ✗ |
| adult #8 - stepping on - stairs #6 | 2-10.4s | holding (+4 more) | 0-17s, 85-95s | not judged yet | 0.31 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (16): adult #8 - sanding - stairs #12 [21-54s, 55-67s, 85-95s]; adult #8 - moving along - stairs #12 [21-54s, 55-67s, 85-95s]; adult #8 - sanding deck - stairs #12 [21-54s, 55-67s, 85-95s]; adult #8 - on - stairs #12 [21-54s, 55-67s, 85-95s]; adult #8 - sanding - car #11 [21-54s, 55-67s, 85-95s]; adult #8 - moving along - car #11 [21-54s, 55-67s, 85-95s]; adult #8 - sanding deck - car #11 [21-54s, 55-67s, 85-95s]; chair #10 - on - stairs #12 [21-54s, 55-67s, 85-95s]; car #11 - on - stairs #12 [21-54s, 55-67s, 85-95s]; chair #10 - next to - car #11 [21-54s, 55-67s, 85-95s]


## 1000_6828150903

68.0 s, 68 frames read | human: 15 objects, 13 relations | TRASER: 15 objects, 38 relations, valid JSON, 1593 tokens

**Objects: 6/15 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | rock | fireplace | not judged yet | ? |
| 2 | floor | baseboard | not judged yet | ? |
| 3 | ceiling | curtain | not judged yet | ? |
| 4 | wall | curtain | not judged yet | ? |
| 5 | door | door frame | semantic overlap | ✓ |
| 6 | shelf | table | not judged yet | ? |
| 7 | window | window | identical | ✓ |
| 8 | adult | person | not judged yet | ? |
| 9 | baby | child | hypernym/hyponym | ✓ |
| 10 | dog | plush toy | not judged yet | ? |
| 11 | toy | toy | identical | ✓ |
| 12 | door | door | identical | ✓ |
| 13 | door | curtain | not judged yet | ? |
| 14 | door | window | not judged yet | ? |
| 15 | door | door | identical | ✓ |

**Relations: 3/13 right, triplets: 0/13 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #8 - beside - door #5 | 0-5.2s | in front of | 0-9s | not judged yet | 0.58 | ? | ? |
| adult #8 - holding - baby #9 | 0-68s | holding (+4 more) | 0-69s | identical | 0.99 | ✓ | ? |
| adult #8 - hugging - baby #9 | 0-68s | holding (+4 more) | 0-69s | not judged yet | 0.99 | ? | ? |
| adult #8 - walking on - floor #2 | 0-16.8s | above | 10-14s, 50-69s | not judged yet | 0.11 | ✗ | ✗ |
| adult #8 - beside - door #12 | 5.2-9.6s | in front of | 0-12s | not judged yet | 0.37 | ✗ | ✗ |
| adult #8 - beside - door #14 | 10.2-11.6s | in front of | 10-14s | not judged yet | 0.35 | ✗ | ✗ |
| adult #8 - beside - window #7 | 11.6-13.6s | in front of | 10-14s | not judged yet | 0.50 | ✗ | ✗ |
| adult #8 - in front of - rock #1 | 16.4-68s | in front of | 16-69s | identical | 0.97 | ✓ | ? |
| adult #8 - beside - wall #4 | 16.4-68s | in front of | 0-69s | not judged yet | 0.75 | ? | ? |
| adult #8 - grabbing - toy #11 | 16.8-18s | holding (+1 more) | 16-69s | not judged yet | 0.02 | ✗ | ✗ |
| adult #8 - holding - toy #11 | 18-45.6s | holding (+1 more) | 16-69s | identical | 0.52 | ✓ | ? |
| dog #10 - jumping over - floor #2 | 19-21.4s | above | 19-24s | not judged yet | 0.48 | ✗ | ✗ |
| baby #9 - holding - toy #11 | 45.6-68s | looking at (+1 more) | 16-69s | not judged yet | 0.42 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (21): baby #9 - in front of - wall #4 [0-69s]; baby #9 - in front of - rock #1 [16-69s]; adult #8 - in front of - door #15 [16-69s]; baby #9 - in front of - door #15 [16-69s]; baby #9 - in front of - door #14 [10-14s]; baby #9 - in front of - window #7 [10-14s]; adult #8 - in front of - shelf #6 [12-14s]; baby #9 - in front of - shelf #6 [12-14s]; baby #9 - in front of - door #12 [0-12s]; baby #9 - in front of - door #5 [0-9s]


## 1001_7007447516

83.6 s, 84 frames read | human: 22 objects, 9 relations | TRASER: 21 objects, 53 relations, valid JSON, 2252 tokens

**Objects: 11/22 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | sky | tree | not judged yet | ? |
| 2 | tree | tree | identical | ✓ |
| 3 | ground | bicycle | not judged yet | ? |
| 4 | grass | grass | identical | ✓ |
| 5 | wall | fence | not judged yet | ? |
| 6 | dustbin | umbrella | not judged yet | ? |
| 7 | helmet | helmet | identical | ✓ |
| 8 | fence | gate | semantic overlap | ✓ |
| 9 | adult | person | not judged yet | ? |
| 10 | child | child | identical | ✓ |
| 11 | dog | dog | identical | ✓ |
| 12 | bike | bicycle | synonym | ✓ |
| 13 | car | car | identical | ✓ |
| 14 | helmet | helmet | identical | ✓ |
| 15 | adult | person | not judged yet | ? |
| 16 | car | car | identical | ✓ |
| 17 | adult | person | not judged yet | ? |
| 18 | car | - | no label from TRASER | ✗ |
| 19 | adult | person | not judged yet | ? |
| 20 | car | car | identical | ✓ |
| 21 | adult | person | not judged yet | ? |
| 22 | car | pole | not judged yet | ? |

**Relations: 1/9 right, triplets: 1/9 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #21 - walking on - ground #3 | 40-70.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #10 - riding - bike #12 | 0-83.4s | riding (+1 more) | 0-76.6333s | identical | 0.92 | ✓ | ✓ |
| adult #9 - looking at - child #10 | 0-75.2s | holding (+4 more) | 0-76.6333s | not judged yet | 0.98 | ? | ? |
| adult #9 - holding - child #10 | 0-15.4s, 42.8-44.6s, 54.6-63s | holding (+4 more) | 0-76.6333s | identical | 0.33 | ✗ | ✗ |
| adult #9 - running on - ground #3 | 15.2-42.8s, 63-72.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #15 - looking at - child #10 | 19.2-25.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #10 - walking on - ground #3 | 72.8-83.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - talking to - child #10 | 72.8-75s | holding (+4 more) | 0-76.6333s | not judged yet | 0.03 | ✗ | ✗ |
| adult #9 - guiding - child #10 | 0-71.4s | holding (+4 more) | 0-76.6333s | not judged yet | 0.93 | ? | ? |

TRASER relations between pairs the humans did not annotate (46): adult #9 - wearing - helmet #7 [0-76.6333s]; child #10 - wearing - helmet #7 [0-76.6333s]; adult #9 - riding - bike #12 [0-76.6333s]; adult #9 - on - bike #12 [0-76.6333s]; child #10 - moving with - adult #9 [0-76.6333s]; adult #9 - approaching - fence #8 [19.9048-25.8762s]; adult #9 - passing - fence #8 [23.8857-25.8762s]; adult #9 - moving away from - fence #8 [24.881-26.8714s]; adult #9 - in front of - fence #8 [19.9048-26.8714s, 72.6524-76.6333s]; child #10 - approaching - fence #8 [19.9048-25.8762s]


## 1002_5280626374

35.2 s, 35 frames read | human: 13 objects, 12 relations | TRASER: 13 objects, 28 relations, valid JSON, 1193 tokens

**Objects: 2/13 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | fabric (uncertain) | not judged yet | ? |
| 2 | book | hand | not judged yet | ? |
| 3 | glasses | sunglasses | not judged yet | ? |
| 4 | microphone | microphone | identical | ✓ |
| 5 | adult | person | not judged yet | ? |
| 6 | child | child | identical | ✓ |
| 7 | table | tablecloth | not judged yet | ? |
| 8 | toy | paper (uncertain) | not judged yet | ? |
| 9 | adult | person | not judged yet | ? |
| 10 | toy | balloon | not judged yet | ? |
| 11 | adult | person | not judged yet | ? |
| 12 | adult | dress | not judged yet | ? |
| 13 | adult | person | not judged yet | ? |

**Relations: 1/12 right, triplets: 1/12 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #5 - standing on - ground #1 | 0-35.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - holding - glasses #3 | 1.4-18.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - book #2 | 20.4-35.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - next to - adult #9 | 0-35.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - next to - child #6 | 0-35.2s | looking at | 0-15.0857s | not judged yet | 0.43 | ✗ | ✗ |
| child #6 - standing on - table #7 | 0-35.2s | on | 0-35.2s | not judged yet | 1.00 | ? | ? |
| child #6 - in - toy #8 | 4.4-35.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #6 - holding - microphone #4 | 13-35.2s | holding (+2 more) | 15.0857-35.2s | identical | 0.91 | ✓ | ✓ |
| child #6 - wearing - glasses #3 | 19.4-35.2s | wearing | 0-35.2s | identical | 0.45 | ✗ | ✗ |
| adult #9 - talking to - child #6 | 24-26.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - talking to - child #6 | 26.4-35.2s | looking at | 0-15.0857s | not judged yet | 0.00 | ✗ | ✗ |
| child #6 - talking to - adult #5 | 19.4-35.2s | in front of (+4 more) | 0-35.2s | not judged yet | 0.45 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (17): adult #5 - on - table #7 [0-35.2s]; adult #9 - on - table #7 [0-35.2s]; microphone #4 - above - table #7 [0-35.2s]; glasses #3 - on - child #6 [0-35.2s]; child #6 - in front of - adult #9 [0-35.2s]; microphone #4 - in front of - child #6 [0-35.2s]; microphone #4 - in front of - adult #5 [0-35.2s]; microphone #4 - in front of - adult #9 [0-35.2s]; child #6 - in front of - adult #13 [3.01714-22.1257s, 29.1657-35.2s]; adult #5 - in front of - adult #13 [3.01714-22.1257s, 29.1657-35.2s]


## 1005_4760962392

90.0 s, 90 frames read | human: 17 objects, 20 relations | TRASER: 17 objects, 14 relations, valid JSON, 1109 tokens

**Objects: 8/17 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | fabric | not judged yet | ? |
| 2 | wall | wall | identical | ✓ |
| 3 | spoon | candle | not judged yet | ? |
| 4 | adult | person | not judged yet | ? |
| 5 | child | girl | not judged yet | ? |
| 6 | table | tablecloth | not judged yet | ? |
| 7 | knife | knife | identical | ✓ |
| 8 | candle | candle | identical | ✓ |
| 9 | plate | napkin | not judged yet | ? |
| 10 | cake | cake | identical | ✓ |
| 11 | adult | person | not judged yet | ? |
| 12 | child | child | identical | ✓ |
| 13 | knife | bowl | not judged yet | ? |
| 14 | candle | candle | identical | ✓ |
| 15 | plate | plate | identical | ✓ |
| 16 | adult | person | not judged yet | ? |
| 17 | child | child | identical | ✓ |

**Relations: 0/20 right, triplets: 0/20 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| child #17 - blowing - candle #8 | 5.4-9.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #17 - holding - plate #9 | 39.6-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - holding - plate #15 | 84.6-90s | serving | 84-90s | not judged yet | 0.90 | ? | ? |
| adult #4 - holding - spoon #3 | 86.6-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - holding - child #17 | 0-5.2s | serving | 66-72s | not judged yet | 0.00 | ✗ | ✗ |
| adult #4 - looking at - cake #10 | 5-8.2s | cutting (+1 more) | 0-17s, 41-46s | not judged yet | 0.15 | ✗ | ✗ |
| adult #4 - holding - knife #7 | 11.6-22.6s | holding | 0-17s, 41-46s | identical | 0.20 | ✗ | ✗ |
| adult #4 - holding - knife #13 | 34-80.2s | holding | 28-38s | identical | 0.08 | ✗ | ✗ |
| adult #4 - cutting - cake #10 | 36-75.2s | cutting (+1 more) | 0-17s, 41-46s | identical | 0.09 | ✗ | ✗ |
| adult #4 - in front of - wall #2 | 0-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #16 - picking - candle #8 | 23-26.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #16 - picking - candle #14 | 23-26.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #5 - beside - child #17 | 0-14.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #5 - beside - adult #4 | 0-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #12 - beside - adult #4 | 0-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #12 - beside - child #17 | 0-20.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #17 - beside - table #6 | 39-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| cake #10 - on - table #6 | 0-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| candle #8 - on - cake #10 | 0-23.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| candle #14 - on - cake #10 | 0-23.2s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (8): adult #4 - serving - child #12 [28-38s]; child #12 - eating from - knife #13 [28-38s]; child #12 - looking at - cake #10 [28-38s]; child #17 - looking at - cake #10 [0-17s, 41-46s]; child #17 - looking at - cake #10 [66-72s]; adult #4 - serving - child #5 [55-64s]; child #5 - looking at - cake #10 [55-64s]; child #17 - looking at - plate #15 [84-90s]


## 1005_7031128593

90.0 s, 90 frames read | human: 9 objects, 7 relations | TRASER: 8 objects, 19 relations, valid JSON, 1155 tokens

**Objects: 2/9 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | dog | not judged yet | ? |
| 2 | wall | curtain | not judged yet | ? |
| 3 | shelf | suitcase | not judged yet | ? |
| 4 | adult | person | not judged yet | ? |
| 5 | dog | dog | identical | ✓ |
| 6 | chair | chair | identical | ✓ |
| 7 | toy | handbag (uncertain) | not judged yet | ? |
| 8 | adult | shoe (uncertain) | not judged yet | ? |
| 9 | dog | - | no label from TRASER | ✗ |

**Relations: 2/7 right, triplets: 0/7 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| shelf #3 - in front of - wall #2 | 0-90s | in front of | 16-45s, 62-90s | identical | 0.63 | ✓ | ? |
| adult #4 - standing on - floor #1 | 0-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #5 - biting - toy #7 | 0-24.2s, 43.6-62.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #5 - playing with - toy #7 | 0-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - holding - toy #7 | 24-33.4s, 62.2-80.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - throwing - toy #7 | 32.8-33.4s, 79.6-80.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - in front of - chair #6 | 0-90s | in front of (+1 more) | 0-45s, 59-90s | identical | 0.84 | ✓ | ? |

TRASER relations between pairs the humans did not annotate (16): adult #4 - petting - dog #5 [0-2s, 3-11s, 12-15s, 16-22s, 23-34s, 35-45s, 59-62s, 63-78s, 79-82s, 83-84s]; adult #4 - holding - dog #5 [15-16s, 22-23s, 45-46s, 47-48s, 52-53s, 54-55s, 56-57s, 58-59s, 62-63s, 64-65s, 66-67s, 68-69s, 70-71s, 72-73s, 74-75s, 76-77s, 78-79s, 80-81s, 82-83s]; adult #4 - playing with - dog #5 [0-2s, 3-11s, 12-15s, 16-22s, 23-34s, 35-45s, 59-62s, 63-78s, 79-82s, 83-84s]; dog #5 - approaching - chair #6 [22-25s]; dog #5 - moving away from - chair #6 [25-34s]; dog #5 - in front of - chair #6 [0-45s, 59-90s]; dog #5 - near - chair #6 [0-45s, 59-90s]; dog #5 - in front of - shelf #3 [0-45s, 59-90s]; dog #5 - near - shelf #3 [0-45s, 59-90s]; adult #4 - in front of - shelf #3 [0-45s, 59-90s]


## 1005_7401573420

85.0 s, 85 frames read | human: 20 objects, 23 relations | TRASER: 19 objects, 43 relations, valid JSON, 1915 tokens

**Objects: 11/20 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | floor | identical | ✓ |
| 2 | wall | wall | identical | ✓ |
| 3 | door | radiator | not judged yet | ? |
| 4 | cabinet | dresser | not judged yet | ? |
| 5 | window | - | no label from TRASER | ✗ |
| 6 | adult | person | not judged yet | ? |
| 7 | child | baby | not judged yet | ? |
| 8 | cat | cat | identical | ✓ |
| 9 | sofa | sofa | identical | ✓ |
| 10 | table | suitcase | not judged yet | ? |
| 11 | chair | chair | identical | ✓ |
| 12 | bag | chair | not judged yet | ? |
| 13 | toy | toy | identical | ✓ |
| 14 | ball | ball | identical | ✓ |
| 15 | door | door | identical | ✓ |
| 16 | table | book | not judged yet | ? |
| 17 | chair | chair leg | semantic overlap | ✓ |
| 18 | toy | toy | identical | ✓ |
| 19 | chair | arm | not judged yet | ? |
| 20 | chair | chair | identical | ✓ |

**Relations: 2/23 right, triplets: 1/23 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| child #7 - running on - floor #1 | 0-17.2s | on | 0-85s | not judged yet | 0.20 | ✗ | ✗ |
| adult #6 - sitting on - floor #1 | 0-85s | on | 10-85s | not judged yet | 0.88 | ? | ? |
| table #10 - on - floor #1 | 0-85s | on | 0-16s | identical | 0.19 | ✗ | ✗ |
| table #16 - on - floor #1 | 0-85s | nothing for this pair | - | - | - | ✗ | ✗ |
| cabinet #4 - on - floor #1 | 0-85s | on | 16-58s | identical | 0.49 | ✗ | ✗ |
| chair #11 - on - floor #1 | 0-85s | on | 0-6s, 22-58s, 76-79s | identical | 0.53 | ✓ | ✓ |
| chair #17 - on - floor #1 | 0-85s | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #19 - on - floor #1 | 0-85s | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #20 - on - floor #1 | 0-85s | on | 0-5s, 47-51s | identical | 0.11 | ✗ | ✗ |
| toy #13 - on - table #16 | 0-85s | nothing for this pair | - | - | - | ✗ | ✗ |
| toy #18 - on - table #16 | 0-85s | nothing for this pair | - | - | - | ✗ | ✗ |
| bag #12 - on - floor #1 | 0-85s | on | 16-58s | identical | 0.49 | ✗ | ✗ |
| cat #8 - sitting on - floor #1 | 3.8-5.2s, 48.8-51.4s | on | 0-85s | not judged yet | 0.05 | ✗ | ✗ |
| cat #8 - standing on - floor #1 | 14.6-17.4s, 22.6-30.2s, 39.2-44s | on | 0-85s | not judged yet | 0.18 | ✗ | ✗ |
| cat #8 - lying on - floor #1 | 76.6-84.2s | on | 0-85s | not judged yet | 0.09 | ✗ | ✗ |
| adult #6 - playing with - cat #8 | 17-84.2s | playing with (+2 more) | 64-85s | identical | 0.30 | ✗ | ✗ |
| child #7 - playing with - cat #8 | 14.6-85s | near | 0-85s | not judged yet | 0.83 | ? | ? |
| child #7 - looking at - cat #8 | 14.6-85s | near | 0-85s | not judged yet | 0.83 | ? | ? |
| child #7 - next to - adult #6 | 14.6-85s | in front of (+3 more) | 10-85s | not judged yet | 0.94 | ? | ? |
| child #7 - in front of - adult #6 | 14.6-85s | in front of (+3 more) | 10-85s | identical | 0.94 | ✓ | ? |
| child #7 - next to - cat #8 | 14.6-85s | near | 0-85s | not judged yet | 0.83 | ? | ? |
| child #7 - squatting on - floor #1 | 17.6-20.2s, 24.4-26.6s | on | 0-85s | not judged yet | 0.06 | ✗ | ✗ |
| child #7 - walking on - floor #1 | 45.4-49.6s, 76.6-79s | on | 0-85s | not judged yet | 0.08 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (27): adult #6 - holding - child #7 [16-57s]; adult #6 - lifting - child #7 [16-21s]; adult #6 - hugging - child #7 [21-57s]; adult #6 - playing with - child #7 [16-57s]; adult #6 - looking at - child #7 [16-57s]; adult #6 - helping up - child #7 [16-21s]; adult #6 - playing with baby - child #7 [16-57s]; cat #8 - approaching - adult #6 [64-68s]; cat #8 - in front of - adult #6 [10-85s]; adult #6 - playing with - toy #18 [10-13s]


## 1006_4580824633

40.6 s, 41 frames read | human: 5 objects, 8 relations | TRASER: 5 objects, 9 relations, valid JSON, 462 tokens

**Objects: 2/5 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | tree | tree | identical | ✓ |
| 2 | grass | dog | not judged yet | ? |
| 3 | adult | person | not judged yet | ? |
| 4 | dog | dog | identical | ✓ |
| 5 | adult | dog | not judged yet | ? |

**Relations: 1/8 right, triplets: 0/8 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| dog #4 - running on - grass #2 | 0-29.6s, 38.6-40.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #3 - running on - grass #2 | 0-7.2s, 9.8-28.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #2 - in front of - tree #1 | 0-11.4s, 13.4-26.4s, 31.8-38.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #4 - chasing - adult #3 | 0.8-12.2s, 21.6-28.8s | near | 6.93171-10.8927s, 12.8732-39.6098s | not judged yet | 0.29 | ✗ | ✗ |
| adult #3 - chasing - dog #4 | 13.4-20.2s | petting (+2 more) | 26.7366-28.7171s, 29.7073-30.6976s | not judged yet | 0.00 | ✗ | ✗ |
| adult #3 - standing on - grass #2 | 11.8-13.6s, 29.6-40.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #3 - holding - dog #4 | 29.6-38.4s | holding (+2 more) | 30.6976-39.6098s | identical | 0.77 | ✓ | ? |
| adult #3 - kissing - dog #4 | 32.4-36.2s | holding (+2 more) | 30.6976-39.6098s | not judged yet | 0.43 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (5): adult #3 - in front of - tree #1 [0-10.8927s, 12.8732-26.7366s, 33.6683-39.6098s]; dog #4 - in front of - tree #1 [6.93171-10.8927s, 12.8732-26.7366s, 33.6683-39.6098s]; adult #5 - in front of - tree #1 [12.8732-14.8537s]; adult #5 - in front of - adult #3 [12.8732-14.8537s]; adult #5 - in front of - dog #4 [12.8732-14.8537s]


## 1007_6631583821

28.8 s, 29 frames read | human: 10 objects, 12 relations | TRASER: 10 objects, 31 relations, valid JSON, 1012 tokens

**Objects: 3/10 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | surface | not judged yet | ? |
| 2 | wall | garage door | not judged yet | ? |
| 3 | fence | railing | not judged yet | ? |
| 4 | adult | person | not judged yet | ? |
| 5 | child | person | not judged yet | ? |
| 6 | baby | child | hypernym/hyponym | ✓ |
| 7 | ball | ball | identical | ✓ |
| 8 | car | car | identical | ✓ |
| 9 | child | person | not judged yet | ? |
| 10 | child | shoe | not judged yet | ? |

**Relations: 0/12 right, triplets: 0/12 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| child #5 - standing on - ground #1 | 0-28.8s | on | 0-28.8s | not judged yet | 1.00 | ? | ? |
| adult #4 - standing on - ground #1 | 0-28.8s | on | 0-28.8s | not judged yet | 1.00 | ? | ? |
| baby #6 - sitting on - ground #1 | 0-28.8s | on | 0-28.8s | not judged yet | 1.00 | ? | ? |
| child #9 - standing on - ground #1 | 0-28.8s | on | 0-28.8s | not judged yet | 1.00 | ? | ? |
| adult #4 - catching - ball #7 | 0.8-2.4s, 7.2-7.6s, 14.2-17s, 24.6-26.2s | looking at | 0-28.8s | not judged yet | 0.22 | ✗ | ✗ |
| adult #4 - throwing - ball #7 | 2.4-3.6s, 8.6-10.2s, 17-18.6s, 26.2-27.2s | looking at | 0-28.8s | not judged yet | 0.19 | ✗ | ✗ |
| child #5 - throwing - ball #7 | 0-1s, 4.8-7.2s, 11-14.2s, 19.4-23.6s | holding (+1 more) | 0-28.8s | not judged yet | 0.38 | ✗ | ✗ |
| child #5 - catching - ball #7 | 3.6-4.8s, 10.2-11s, 18.6-19.6s, 27.2-28.2s | holding (+1 more) | 0-28.8s | not judged yet | 0.14 | ✗ | ✗ |
| adult #4 - holding - ball #7 | 7.4-9s | looking at | 0-28.8s | not judged yet | 0.06 | ✗ | ✗ |
| child #5 - holding - ball #7 | 10.4-13.2s, 28-28.8s | holding (+1 more) | 0-28.8s | identical | 0.12 | ✗ | ✗ |
| child #5 - playing with - ball #7 | 0-28.8s | holding (+1 more) | 0-28.8s | not judged yet | 1.00 | ? | ? |
| adult #4 - playing with - ball #7 | 0-28.8s | looking at | 0-28.8s | not judged yet | 1.00 | ? | ? |

TRASER relations between pairs the humans did not annotate (24): adult #4 - wearing - child #10 [0-28.8s]; ball #7 - moving toward - adult #4 [15.8897-18.869s]; ball #7 - moving away from - adult #4 [18.869-28.8s]; child #10 - on - ground #1 [0-28.8s]; ball #7 - above - ground #1 [0-28.8s]; adult #4 - in front of - wall #2 [0-28.8s]; child #5 - in front of - wall #2 [0-28.8s]; baby #6 - in front of - wall #2 [0-28.8s]; child #9 - in front of - wall #2 [0-28.8s]; child #10 - in front of - wall #2 [0-28.8s]


## 1011_4633647136

53.6 s, 54 frames read | human: 14 objects, 20 relations | TRASER: 14 objects, 356 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 8/14 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | floor | synonym | ✓ |
| 2 | wall | painting | not judged yet | ? |
| 3 | door | door | identical | ✓ |
| 4 | adult | person | not judged yet | ? |
| 5 | child | child | identical | ✓ |
| 6 | table | tablecloth | not judged yet | ? |
| 7 | chair | chair | identical | ✓ |
| 8 | candle | bow | not judged yet | ? |
| 9 | cake | cake | identical | ✓ |
| 10 | adult | person | not judged yet | ? |
| 11 | chair | chair | identical | ✓ |
| 12 | adult | person | not judged yet | ? |
| 13 | chair | chair | identical | ✓ |
| 14 | chair | chair | identical | ✓ |

**Relations: 0/20 right, triplets: 0/20 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #10 - walking on - ground #1 | 8.6-9.8s, 45-49.4s | moving away from (+11 more) | 44.6667-50.6222s | not judged yet | 0.61 | ? | ? |
| adult #4 - holding - child #5 | 30.6-53.6s | holding (+1 more) | 0-53.6s | identical | 0.43 | ✗ | ✗ |
| adult #4 - beside - table #6 | 0-53.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - beside - table #6 | 0-53.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #5 - beside - table #6 | 0-53.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #5 - sitting on - chair #7 | 0-28.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #5 - standing on - chair #7 | 30-53.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| cake #9 - on - table #6 | 0-53.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| candle #8 - on - cake #9 | 0-40.6s, 47.4-53.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - beside - table #6 | 6.2-49.2s | approaching (+5 more) | 5.95556-10.9185s | not judged yet | 0.11 | ✗ | ✗ |
| adult #10 - beside - adult #4 | 8.4-45.8s | approaching (+9 more) | 5.95556-10.9185s | not judged yet | 0.06 | ✗ | ✗ |
| adult #10 - holding - chair #11 | 7.6-29.4s | approaching (+15 more) | 5.95556-10.9185s | not judged yet | 0.14 | ✗ | ✗ |
| adult #4 - picking - child #5 | 27.8-30.2s | holding (+1 more) | 0-53.6s | not judged yet | 0.04 | ✗ | ✗ |
| adult #10 - touching - cake #9 | 30.6-33.8s | approaching (+5 more) | 5.95556-10.9185s | not judged yet | 0.00 | ✗ | ✗ |
| adult #12 - touching - cake #9 | 30-33.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - holding - candle #8 | 40.2-48.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - blowing - candle #8 | 42.4-43.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - lighting - candle #8 | 0-4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - carrying - candle #8 | 40.2-42.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - guiding - child #5 | 42.4-44.4s | holding (+1 more) | 0-53.6s | not judged yet | 0.04 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (85): adult #12 - holding - child #5 [0-53.6s]; adult #12 - looking at - child #5 [0-53.6s]; child #5 - looking at - cake #9 [0-53.6s]; adult #10 - approaching - child #5 [5.95556-10.9185s]; adult #10 - moving away from - child #5 [44.6667-50.6222s]; adult #10 - approaching - child #5 [5.95556-10.9185s]; adult #10 - moving away from - child #5 [44.6667-50.6222s]; adult #10 - approaching - child #5 [5.95556-10.9185s]; adult #10 - moving away from - child #5 [44.6667-50.6222s]; adult #10 - approaching - child #5 [5.95556-10.9185s]


## 1012_4024008346

19.6 s, 20 frames read | human: 11 objects, 8 relations | TRASER: 11 objects, 31 relations, valid JSON, 1209 tokens

**Objects: 5/11 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | floor | identical | ✓ |
| 2 | wall | wall | identical | ✓ |
| 3 | carpet | doormat | not judged yet | ? |
| 4 | fence | gate | semantic overlap | ✓ |
| 5 | adult | child | not judged yet | ? |
| 6 | child | child | identical | ✓ |
| 7 | sofa | sofa | identical | ✓ |
| 8 | ballon | balloon | not judged yet | ? |
| 9 | carpet | baseboard | not judged yet | ? |
| 10 | adult | person | not judged yet | ? |
| 11 | ballon | ball | not judged yet | ? |

**Relations: 5/8 right, triplets: 2/8 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #10 - sitting on - sofa #7 | 0-19.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #6 - holding - ballon #8 | 0-19.6s | holding (+2 more) | 0-19.6s | identical | 1.00 | ✓ | ? |
| child #6 - on - floor #1 | 0-19.6s | on | 0-19.6s | identical | 1.00 | ✓ | ✓ |
| adult #5 - on - floor #1 | 0-19.6s | on | 0-8.82s, 11.76-16.66s | identical | 0.70 | ✓ | ? |
| ballon #11 - on - floor #1 | 0-19.6s | on | 0-16.66s | identical | 0.85 | ✓ | ? |
| child #6 - playing with - ballon #11 | 0-0.8s, 6-13s | approaching (+1 more) | 9.8-12.74s | not judged yet | 0.38 | ✗ | ✗ |
| adult #5 - playing with - ballon #11 | 4.4-5s, 13.4-16s | nothing for this pair | - | - | - | ✗ | ✗ |
| sofa #7 - on - floor #1 | 0-19.6s | on | 0-12.74s, 15.68-19.6s | identical | 0.85 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (22): child #6 - moving away from - sofa #7 [9.8-12.74s]; child #6 - approaching - sofa #7 [15.68-19.6s]; child #6 - in front of - sofa #7 [0-12.74s, 15.68-19.6s]; carpet #3 - on - floor #1 [0-19.6s]; fence #4 - on - floor #1 [0-19.6s]; ballon #8 - above - floor #1 [0-19.6s]; fence #4 - in front of - wall #2 [0-19.6s]; sofa #7 - in front of - wall #2 [0-12.74s, 15.68-19.6s]; child #6 - in front of - fence #4 [0-19.6s]; ballon #11 - in front of - fence #4 [0-16.66s]


## 1015_4698622422

42.0 s, 42 frames read | human: 13 objects, 15 relations | TRASER: 13 objects, 18 relations, valid JSON, 1089 tokens

**Objects: 4/13 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | tree | pole | not judged yet | ? |
| 2 | grass | tennis ball | not judged yet | ? |
| 3 | adult | person | not judged yet | ? |
| 4 | child | child | identical | ✓ |
| 5 | table | bench | not judged yet | ? |
| 6 | hat | hand | not judged yet | ? |
| 7 | bat | tennis racket | not judged yet | ? |
| 8 | ball | soccer ball | not judged yet | ? |
| 9 | car | car | identical | ✓ |
| 10 | adult | person | not judged yet | ? |
| 11 | child | person | not judged yet | ? |
| 12 | car | car | identical | ✓ |
| 13 | car | car | identical | ✓ |

**Relations: 2/15 right, triplets: 0/15 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #10 - holding - hat #6 | 40-41.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| ball #8 - on - grass #2 | 0-41.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #4 - on - grass #2 | 0-41.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #4 - holding - bat #7 | 0-36.2s | holding (+1 more) | 0-17s, 18-36s | identical | 0.97 | ✓ | ? |
| child #4 - walking on - grass #2 | 0-10.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #4 - hitting - ball #8 | 10.4-12.6s, 20.6-21.8s, 23.6-24.6s, 26.6-27.6s, 29-29.8s, 33.4-34.4s | hitting (+4 more) | 10-13s, 24-26s, 31-33s | identical | 0.25 | ✗ | ✗ |
| child #4 - throwing - bat #7 | 36-36.6s | holding (+1 more) | 0-17s, 18-36s | not judged yet | 0.00 | ✗ | ✗ |
| child #4 - chasing - ball #8 | 12.6-39.2s | playing with (+4 more) | 0-17s, 18-42s | not judged yet | 0.61 | ? | ? |
| child #4 - kicking - ball #8 | 36.2-39.2s | playing with (+4 more) | 0-17s, 18-42s | not judged yet | 0.07 | ✗ | ✗ |
| adult #3 - standing on - grass #2 | 18.8-19.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - standing on - grass #2 | 40-41.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - pulling - child #4 | 40.6-41.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #11 - in front of - adult #3 | 19-19.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #4 - playing with - ball #8 | 6.6-40.2s | playing with (+4 more) | 0-17s, 18-42s | identical | 0.78 | ✓ | ? |
| child #4 - squatting on - grass #2 | 19-41.8s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (11): child #4 - in front of - car #9 [0-15s]; child #4 - in front of - car #12 [4-15s]; child #4 - in front of - car #13 [6-15s]; child #4 - in front of - table #5 [12-15s]; child #4 - in front of - tree #1 [0-15s, 20-22s, 29-38s]; bat #7 - in front of - child #4 [0-17s, 18-36s]; ball #8 - in front of - child #4 [0-17s, 18-42s]; bat #7 - above - ball #8 [0-17s, 18-36s]; child #4 - in front of - adult #10 [41-42s]; child #4 - in front of - adult #3 [17-18s]


## 1017_3056841458

80.6 s, 81 frames read | human: 14 objects, 16 relations | TRASER: 14 objects, 37 relations, valid JSON, 1408 tokens

**Objects: 4/14 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | chair leg | not judged yet | ? |
| 2 | wall | curtain | not judged yet | ? |
| 3 | door | window | not judged yet | ? |
| 4 | curtain | curtain | identical | ✓ |
| 5 | shelf | cabinet | not judged yet | ? |
| 6 | towel | cup | not judged yet | ? |
| 7 | adult | person | not judged yet | ? |
| 8 | child | child | identical | ✓ |
| 9 | table | table | identical | ✓ |
| 10 | chair | chair | identical | ✓ |
| 11 | hat | party hat | not judged yet | ? |
| 12 | cake | cupcake | not judged yet | ? |
| 13 | adult | person | not judged yet | ? |
| 14 | cake | cupcake | not judged yet | ? |

**Relations: 3/16 right, triplets: 0/16 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| cake #14 - on - table #9 | 0-80.6s | on | 0-81.5951s | identical | 0.99 | ✓ | ? |
| child #8 - sitting on - chair #10 | 0-80.6s | sitting on | 41.7926-63.684s | identical | 0.27 | ✗ | ✗ |
| cake #12 - on - table #9 | 0-80.6s | on | 0-81.5951s | identical | 0.99 | ✓ | ? |
| adult #7 - beside - child #8 | 1-60.2s | touching (+2 more) | 11.9407-41.7926s | not judged yet | 0.50 | ? | ? |
| adult #7 - holding - hat #11 | 1-10s, 18.2-21.2s | holding (+1 more) | 0-41.7926s | identical | 0.29 | ✗ | ✗ |
| child #8 - wearing - hat #11 | 5.4-15.4s, 20.2-33.4s | wearing | 12.9358-41.7926s | identical | 0.43 | ✗ | ✗ |
| adult #13 - looking at - child #8 | 0-14s, 15.8-26.2s, 28-74s, 75.2-80.6s | helping | 41.7926-63.684s | not judged yet | 0.29 | ✗ | ✗ |
| child #8 - touching - cake #12 | 2.8-3.6s, 18.8-23s, 33.2-34.6s, 47.4-48.2s, 50.6-51.8s, 56.4-57.4s, 64.6-65.4s, 70-71s, 76.2-77s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #13 - holding - hat #11 | 32.4-43s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #8 - eating - cake #12 | 38.2-40.2s, 48.4-49.6s, 52.6-54.4s, 57.6-58.6s, 65.4-66.6s, 71-75.2s, 77.8-79.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #13 - holding - towel #6 | 55.4-66.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| towel #6 - on - table #9 | 0-43s, 66.6-80.6s | on (+1 more) | 0-41.7926s | identical | 0.73 | ✓ | ? |
| towel #6 - touching - child #8 | 60-63.8s | moving toward (+1 more) | 41.7926-44.7778s | not judged yet | 0.00 | ✗ | ✗ |
| adult #13 - touching - child #8 | 60-63.8s | helping | 41.7926-63.684s | not judged yet | 0.17 | ✗ | ✗ |
| adult #13 - kissing - child #8 | 68.2-68.8s | helping | 41.7926-63.684s | not judged yet | 0.00 | ✗ | ✗ |
| adult #13 - cleaning - child #8 | 60-63.8s | helping | 41.7926-63.684s | not judged yet | 0.17 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (23): hat #11 - moving toward - child #8 [0-12.9358s]; hat #11 - on - child #8 [11.9407-41.7926s]; adult #7 - holding - towel #6 [41.7926-44.7778s]; adult #7 - serving - towel #6 [41.7926-44.7778s]; adult #7 - sitting on - chair #10 [41.7926-63.684s]; adult #13 - sitting on - chair #10 [41.7926-63.684s]; hat #11 - above - table #9 [0-41.7926s]; child #8 - behind - table #9 [0-81.5951s]; adult #13 - behind - table #9 [0-81.5951s]; adult #7 - behind - table #9 [0-63.684s]


## 1019_3768851893

58.6 s, 59 frames read | human: 30 objects, 30 relations | TRASER: 27 objects, 39 relations, valid JSON, 2082 tokens

**Objects: 0/30 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | person | mismatch | ✗ |
| 2 | wall | banner | not judged yet | ? |
| 3 | tray | ribbon | not judged yet | ? |
| 4 | curtain | screen | not judged yet | ? |
| 5 | adult | person | not judged yet | ? |
| 6 | child | person | not judged yet | ? |
| 7 | plate | balloon | not judged yet | ? |
| 8 | paper | - | no label from TRASER | ✗ |
| 9 | ballon | balloon | not judged yet | ? |
| 10 | others | - | no label from TRASER | ✗ |
| 11 | adult | person | not judged yet | ? |
| 12 | child | person | not judged yet | ? |
| 13 | paper | balloon | not judged yet | ? |
| 14 | ballon | - | no label from TRASER | ✗ |
| 15 | adult | person | not judged yet | ? |
| 16 | child | person | not judged yet | ? |
| 17 | paper | balloon | not judged yet | ? |
| 18 | ballon | balloon | not judged yet | ? |
| 19 | adult | person | not judged yet | ? |
| 20 | child | person | not judged yet | ? |
| 21 | paper | balloon | not judged yet | ? |
| 22 | ballon | balloon | not judged yet | ? |
| 23 | child | person | not judged yet | ? |
| 24 | paper | handbag | not judged yet | ? |
| 25 | ballon | balloon | not judged yet | ? |
| 26 | child | person | not judged yet | ? |
| 27 | paper | balloon | not judged yet | ? |
| 28 | ballon | balloon | not judged yet | ? |
| 29 | ballon | balloon | not judged yet | ? |
| 30 | ballon | balloon | not judged yet | ? |

**Relations: 6/30 right, triplets: 0/30 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #15 - holding - tray #3 | 23-51.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - holding - paper #17 | 36.8-38.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - holding - paper #21 | 41.6-42.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - holding - paper #24 | 48-50.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #23 - holding - paper #24 | 49.8-51.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| curtain #4 - on - wall #2 | 0-52s, 58-58.6s | behind | 7.94576-55.6203s | not judged yet | 0.78 | ? | ? |
| child #6 - beside - child #12 | 9-58.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #6 - in front of - wall #2 | 9-58.6s | in front of | 9.9322-40.722s | identical | 0.62 | ✓ | ? |
| child #12 - beside - child #16 | 9-58.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #12 - in front of - wall #2 | 9-58.6s | in front of | 9.9322-45.6881s | identical | 0.72 | ✓ | ? |
| child #16 - beside - child #20 | 10.4-58.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #16 - in front of - wall #2 | 9-58.6s | in front of | 9.9322-45.6881s | identical | 0.72 | ✓ | ? |
| child #20 - beside - child #23 | 12.4-58.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #20 - in front of - wall #2 | 10.4-58.6s | in front of | 9.9322-45.6881s | identical | 0.73 | ✓ | ? |
| child #23 - beside - child #26 | 14-58.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #23 - in front of - wall #2 | 13.4-58.6s | in front of | 11.9186-45.6881s | identical | 0.69 | ✓ | ? |
| child #26 - in front of - wall #2 | 13.4-58.6s | in front of | 11.9186-45.6881s | identical | 0.69 | ✓ | ? |
| adult #5 - in front of - wall #2 | 13.8-15.2s | in front of | 11.9186-16.8847s | identical | 0.28 | ✗ | ✗ |
| adult #11 - in front of - wall #2 | 15-16s, 19.2-20.6s | in front of | 11.9186-59.5932s | identical | 0.05 | ✗ | ✗ |
| adult #11 - in front of - child #16 | 20.4-27.2s, 37.8-41.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - in front of - child #6 | 28-32.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - in front of - child #12 | 32-38s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - in front of - child #20 | 41-47.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - in front of - child #23 | 47-52.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - in front of - child #26 | 52-57.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #15 - in front of - wall #2 | 26.8-46.4s, 48.4-53.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #19 - in front of - wall #2 | 40.6-46.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - shaking hand with - child #16 | 39.6-40.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - shaking hand with - child #23 | 50.6-52s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - shaking hand with - child #26 | 55.6-57s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (30): adult #11 - holding - tray #3 [22.8441-55.6203s]; adult #11 - carrying - tray #3 [22.8441-55.6203s]; adult #11 - waving - tray #3 [22.8441-55.6203s]; adult #11 - performing with - tray #3 [22.8441-55.6203s]; adult #11 - moving left relative to - curtain #4 [22.8441-55.6203s]; adult #11 - in front of - curtain #4 [11.9186-55.6203s]; tray #3 - moving left relative to - curtain #4 [22.8441-55.6203s]; tray #3 - in front of - curtain #4 [22.8441-55.6203s]; child #12 - in front of - curtain #4 [9.9322-45.6881s]; child #16 - in front of - curtain #4 [9.9322-45.6881s]


## 1020_2471845614

55.8 s, 56 frames read | human: 22 objects, 27 relations | TRASER: 22 objects, 113 relations, valid JSON, 3759 tokens

**Objects: 10/22 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | floor | synonym | ✓ |
| 2 | wall | building | not judged yet | ? |
| 3 | door | door | identical | ✓ |
| 4 | window | window | identical | ✓ |
| 5 | flower | bouquet | not judged yet | ? |
| 6 | glass | wine glass | not judged yet | ? |
| 7 | microphone | microphone | identical | ✓ |
| 8 | adult | person | not judged yet | ? |
| 9 | table | tablecloth | not judged yet | ? |
| 10 | chair | chair | identical | ✓ |
| 11 | light | lamp post | not judged yet | ? |
| 12 | bottle | bottle | identical | ✓ |
| 13 | camera | camera | identical | ✓ |
| 14 | window | window | identical | ✓ |
| 15 | flower | bouquet | not judged yet | ? |
| 16 | glass | wine glass | not judged yet | ? |
| 17 | adult | veil | not judged yet | ? |
| 18 | chair | chair | identical | ✓ |
| 19 | flower | flower arrangement | hypernym/hyponym | ✓ |
| 20 | glass | wine glass | not judged yet | ? |
| 21 | adult | person | not judged yet | ? |
| 22 | adult | person | not judged yet | ? |

**Relations: 6/27 right, triplets: 0/27 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #22 - talking to - adult #17 | 0-47.6s | in front of | 0-54.8036s | not judged yet | 0.87 | ? | ? |
| adult #22 - talking to - adult #21 | 0-47.6s | looking at | 0-54.8036s | not judged yet | 0.87 | ? | ? |
| adult #8 - holding - camera #13 | 0-55.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - looking at - adult #21 | 0-55.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - beside - chair #18 | 0-55.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #22 - holding - microphone #7 | 0-55.8s | in front of | 0-54.8036s | not judged yet | 0.98 | ? | ? |
| adult #22 - in front of - door #3 | 0-50.2s | in front of | 0-54.8036s | identical | 0.92 | ✓ | ? |
| adult #21 - caressing - adult #17 | 0-52.2s | wearing (+1 more) | 0-54.8036s | not judged yet | 0.95 | ? | ? |
| adult #21 - caressing - adult #22 | 55.2-55.8s | holding hands with (+2 more) | 0-54.8036s | not judged yet | 0.00 | ✗ | ✗ |
| adult #22 - standing on - ground #1 | 0-55.8s | on | 0-54.8036s | not judged yet | 0.98 | ? | ? |
| chair #18 - in front of - adult #21 | 0-55.8s | in front of | 0-54.8036s | identical | 0.98 | ✓ | ? |
| table #9 - in front of - chair #10 | 0-55.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| table #9 - in front of - chair #18 | 0-55.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| flower #5 - on - table #9 | 0-55.8s | on | 3.98571-54.8036s | identical | 0.91 | ✓ | ? |
| flower #15 - on - table #9 | 0-55.8s | on | 3.98571-54.8036s | identical | 0.91 | ✓ | ? |
| flower #19 - on - table #9 | 0-55.8s | on | 3.98571-21.9214s, 45.8357-54.8036s | identical | 0.48 | ✗ | ✗ |
| bottle #12 - on - table #9 | 0-55.8s | on | 3.98571-54.8036s | identical | 0.91 | ✓ | ? |
| adult #17 - beside - adult #21 | 0-55.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #21 - beside - adult #22 | 0-55.8s | holding hands with (+2 more) | 0-54.8036s | not judged yet | 0.98 | ? | ? |
| light #11 - on - ground #1 | 0-55.8s | on | 0-54.8036s | identical | 0.98 | ✓ | ? |
| adult #21 - looking at - adult #22 | 0-3s, 4.2-10s | looking at (+2 more) | 0-54.8036s | identical | 0.16 | ✗ | ✗ |
| adult #21 - looking at - adult #17 | 3-4.2s, 10-12.4s | wearing (+1 more) | 0-54.8036s | not judged yet | 0.07 | ✗ | ✗ |
| adult #17 - holding - glass #16 | 0-55.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #21 - holding - glass #6 | 0-55.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #22 - toward - adult #17 | 48.4-50.2s | in front of | 0-54.8036s | not judged yet | 0.03 | ✗ | ✗ |
| adult #22 - hugging - adult #17 | 50.2-53.2s | in front of | 0-54.8036s | not judged yet | 0.05 | ✗ | ✗ |
| adult #22 - hugging - adult #21 | 54.4-55.8s | looking at | 0-54.8036s | not judged yet | 0.01 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (97): adult #21 - holding - glass #16 [0-54.8036s]; adult #22 - holding - glass #6 [0-54.8036s]; adult #21 - on - ground #1 [0-54.8036s]; chair #10 - on - ground #1 [0-54.8036s]; chair #18 - on - ground #1 [0-54.8036s]; table #9 - on - ground #1 [3.98571-54.8036s]; chair #10 - in front of - wall #2 [0-54.8036s]; chair #18 - in front of - wall #2 [0-54.8036s]; light #11 - in front of - wall #2 [0-54.8036s]; table #9 - in front of - wall #2 [3.98571-54.8036s]


## 1021_3478653250

65.8 s, 66 frames read | human: 13 objects, 23 relations | TRASER: 13 objects, 32 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 7/13 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | tree | bush | not judged yet | ? |
| 2 | ground | stone pathway | not judged yet | ? |
| 3 | grass | lawn | synonym | ✓ |
| 4 | wall | fence | not judged yet | ? |
| 5 | stand | pole | not judged yet | ? |
| 6 | basket | basketball backboard | not judged yet | ? |
| 7 | child | child | identical | ✓ |
| 8 | bat | baseball bat | not judged yet | ? |
| 9 | ball | ball | identical | ✓ |
| 10 | ball | ball | identical | ✓ |
| 11 | ball | ball | identical | ✓ |
| 12 | ball | ball | identical | ✓ |
| 13 | ball | ball | identical | ✓ |

**Relations: 1/23 right, triplets: 0/23 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| basket #6 - on - ground #2 | 0-65.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| ball #12 - on - ground #2 | 0-65.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| stand #5 - on - grass #3 | 0-63.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| ball #12 - next to - tree #1 | 0-63.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #1 - in front of - wall #4 | 0-63.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| basket #6 - in front of - wall #4 | 0-63.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - standing on - grass #3 | 0-63.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| ball #9 - on - stand #5 | 0-4.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| ball #10 - on - grass #3 | 0-9.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| ball #11 - on - grass #3 | 0-49.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - holding - bat #8 | 0-62.6s | holding | 0-65.8s | identical | 0.95 | ✓ | ? |
| child #7 - hitting - ball #9 | 2-5s | hitting (+3 more) | 0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 45.8606-46.8576s, 47.8545-48.8515s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s | identical | 0.00 | ✗ | ✗ |
| child #7 - picking - ball #10 | 8.8-14s | hitting (+3 more) | 0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s | not judged yet | 0.03 | ✗ | ✗ |
| ball #10 - on - stand #5 | 14.2-18.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - hitting - ball #10 | 17.2-18.6s | hitting (+3 more) | 0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s | identical | 0.03 | ✗ | ✗ |
| child #7 - picking - ball #13 | 26.8-28.8s | hitting (+4 more) | 0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s | not judged yet | 0.04 | ✗ | ✗ |
| ball #13 - on - stand #5 | 28.4-42.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - hitting - ball #13 | 40.4-43.2s | hitting (+4 more) | 0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s | identical | 0.06 | ✗ | ✗ |
| child #7 - picking - ball #11 | 49.6-52.4s | hitting (+4 more) | 0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s | not judged yet | 0.06 | ✗ | ✗ |
| ball #11 - on - stand #5 | 52.2-57.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - hitting - ball #11 | 55.8-57.4s | hitting (+4 more) | 0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s | identical | 0.04 | ✗ | ✗ |
| child #7 - picking - stand #5 | 60-61.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| bat #8 - on - grass #3 | 63-65.8s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (7): child #7 - hitting - ball #12 [0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 45.8606-46.8576s, 47.8545-48.8515s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s]; child #7 - hitting - ball #12 [0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 45.8606-46.8576s, 47.8545-48.8515s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s]; child #7 - hitting - ball #12 [0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 45.8606-46.8576s, 47.8545-48.8515s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s]; child #7 - hitting - ball #12 [0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s]; child #7 - hitting - ball #12 [0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s]; child #7 - hitting - tree #1 [0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 45.8606-46.8576s, 47.8545-48.8515s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s]; child #7 - hitting - tree #1 [0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 45.8606-46.8576s, 47.8545-48.8515s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s]


## 1021_4278168115

79.8 s, 80 frames read | human: 11 objects, 21 relations | TRASER: 11 objects, 40 relations, valid JSON, 1274 tokens

**Objects: 8/11 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | tree | Christmas tree | not judged yet | ? |
| 2 | floor | rug | semantic overlap | ✓ |
| 3 | gift | gift wrap | not judged yet | ? |
| 4 | curtain | curtain | identical | ✓ |
| 5 | book | book | identical | ✓ |
| 6 | adult | person | not judged yet | ? |
| 7 | child | child | identical | ✓ |
| 8 | box | box | identical | ✓ |
| 9 | book | book | identical | ✓ |
| 10 | book | book | identical | ✓ |
| 11 | book | book | identical | ✓ |

**Relations: 8/21 right, triplets: 7/21 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| child #7 - touching - book #9 | 66.2-71.2s | holding (+1 more) | 41.895-51.87s | not judged yet | 0.00 | ✗ | ✗ |
| child #7 - touching - book #11 | 78.2-79.8s | holding (+1 more) | 51.87-65.835s | not judged yet | 0.00 | ✗ | ✗ |
| adult #6 - touching - book #5 | 49.4-52s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - on - floor #2 | 0-79.8s | on | 0-80.7975s | identical | 0.99 | ✓ | ✓ |
| adult #6 - sitting on - floor #2 | 0-79.8s | on | 0-80.7975s | not judged yet | 0.99 | ? | ? |
| child #7 - in front of - adult #6 | 0-79.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #6 - holding - gift #3 | 0-3s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - opening - gift #3 | 3.6-31s | opening (+2 more) | 1.995-27.93s | identical | 0.84 | ✓ | ? |
| child #7 - holding - box #8 | 31-33.2s | holding (+2 more) | 30.9225-41.895s | identical | 0.20 | ✗ | ✗ |
| adult #6 - opening - box #8 | 33.4-42.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| book #5 - on - floor #2 | 42.8-43.4s, 50.6-79.8s | on | 41.895-80.7975s | identical | 0.77 | ✓ | ✓ |
| book #9 - on - floor #2 | 42.8-79.8s | on | 41.895-80.7975s | identical | 0.95 | ✓ | ✓ |
| book #10 - on - floor #2 | 42.8-50s, 54-79.8s | on | 41.895-80.7975s | identical | 0.85 | ✓ | ✓ |
| book #11 - on - floor #2 | 42.8-54.6s, 65.4-79.8s | on | 41.895-80.7975s | identical | 0.67 | ✓ | ✓ |
| child #7 - holding - book #5 | 43.2-48.8s | holding (+1 more) | 41.895-51.87s | identical | 0.56 | ✓ | ✓ |
| adult #6 - holding - book #5 | 49-51.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - holding - book #10 | 50-54s | holding (+1 more) | 41.895-51.87s | identical | 0.15 | ✗ | ✗ |
| child #7 - holding - book #11 | 54.6-65.4s | holding (+1 more) | 51.87-65.835s | identical | 0.77 | ✓ | ✓ |
| box #8 - on - floor #2 | 42.4-79.8s | on | 30.9225-41.895s | identical | 0.00 | ✗ | ✗ |
| gift #3 - on - floor #2 | 31-79.8s | on | 2.9925-31.92s | identical | 0.01 | ✗ | ✗ |
| tree #1 - on - floor #2 | 0-79.8s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (18): child #7 - in front of - tree #1 [0-80.7975s]; adult #6 - in front of - tree #1 [0-80.7975s]; tree #1 - in front of - curtain #4 [0-80.7975s]; floor #2 - in front of - curtain #4 [0-80.7975s]; child #7 - in front of - curtain #4 [0-80.7975s]; adult #6 - in front of - curtain #4 [0-80.7975s]; gift #3 - in front of - tree #1 [2.9925-31.92s]; gift #3 - in front of - curtain #4 [2.9925-31.92s]; box #8 - in front of - tree #1 [30.9225-41.895s]; box #8 - in front of - curtain #4 [30.9225-41.895s]


## 1025_4615486172

90.0 s, 90 frames read | human: 27 objects, 24 relations | TRASER: 27 objects, 330 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 9/27 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | rock | chair | not judged yet | ? |
| 2 | floor | chair leg (uncertain) | not judged yet | ? |
| 3 | ceiling | ceiling fan | semantic overlap | ✓ |
| 4 | wall | wall | identical | ✓ |
| 5 | door | door | identical | ✓ |
| 6 | curtain | door frame (uncertain) | not judged yet | ? |
| 7 | shelf | bookshelf | not judged yet | ? |
| 8 | window | curtain | not judged yet | ? |
| 9 | adult | person | not judged yet | ? |
| 10 | child | child | identical | ✓ |
| 11 | table | tablecloth | not judged yet | ? |
| 12 | chair | table | not judged yet | ? |
| 13 | candle | cake | not judged yet | ? |
| 14 | cake | cake | identical | ✓ |
| 15 | cellphone | cell phone | not judged yet | ? |
| 16 | ballon | balloon | not judged yet | ? |
| 17 | chair | chair | identical | ✓ |
| 18 | ballon | balloon | not judged yet | ? |
| 19 | adult | person | not judged yet | ? |
| 20 | chair | chair | identical | ✓ |
| 21 | ballon | balloon | not judged yet | ? |
| 22 | adult | person | not judged yet | ? |
| 23 | chair | chair | identical | ✓ |
| 24 | ballon | chair | not judged yet | ? |
| 25 | adult | person | not judged yet | ? |
| 26 | chair | chair | identical | ✓ |
| 27 | chair | person | mismatch | ✗ |

**Relations: 0/24 right, triplets: 0/24 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #22 - hugging - adult #19 | 50.4-81.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| ballon #21 - on - ceiling #3 | 13.4-20s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - holding - cake #14 | 2.2-29.2s, 76.8-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| candle #13 - on - cake #14 | 2.8-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| cake #14 - on - table #11 | 27.6-86.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #19 - holding - child #10 | 12.8-90s | photographing (+9 more) | 73-90s | not judged yet | 0.22 | ✗ | ✗ |
| adult #19 - picking - chair #12 | 31.6-35.4s | photographing (+8 more) | 73-90s | not judged yet | 0.00 | ✗ | ✗ |
| adult #22 - next to - adult #19 | 49.2-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #19 - blowing - candle #13 | 58.8-61.4s | looking at (+10 more) | 22-90s | not judged yet | 0.04 | ✗ | ✗ |
| adult #22 - blowing - candle #13 | 58.8-61.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #22 - looking at - child #10 | 62-83s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #10 - touching - cake #14 | 75.4-77s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #10 - beside - chair #27 | 5.2-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #22 - in front of - chair #12 | 49.8-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #17 - next to - chair #12 | 4.2-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #20 - beside - chair #17 | 4-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| ballon #16 - on - wall #4 | 4.2-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| ballon #18 - on - wall #4 | 4.2-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| ballon #16 - next to - ballon #18 | 4.2-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #12 - in front of - ballon #16 | 4.2-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #12 - in front of - ballon #18 | 4.2-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - entering - door #5 | 3.4-6.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| ballon #21 - over - table #11 | 0-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #22 - squatting on - floor #2 | 50.4-90s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (300): adult #19 - holding - cellphone #15 [73-90s]; adult #19 - looking at - cellphone #15 [73-90s]; adult #19 - photographing - cellphone #15 [73-90s]; adult #19 - photographing - cellphone #15 [73-90s]; adult #19 - photographing - cellphone #15 [73-90s]; adult #19 - photographing - cellphone #15 [73-90s]; adult #19 - photographing - cellphone #15 [73-90s]; adult #19 - photographing - cellphone #15 [73-90s]; adult #19 - photographing - cellphone #15 [73-90s]; adult #19 - photographing - cellphone #15 [73-90s]


## 1025_6244382586

20.6 s, 21 frames read | human: 11 objects, 12 relations | TRASER: 11 objects, 28 relations, valid JSON, 1084 tokens

**Objects: 5/11 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | sand | semantic overlap | ✓ |
| 2 | ceiling | ceiling | identical | ✓ |
| 3 | wall | fence | not judged yet | ? |
| 4 | adult | person | not judged yet | ? |
| 5 | child | person | not judged yet | ? |
| 6 | horse | horse | identical | ✓ |
| 7 | hat | helmet | not judged yet | ? |
| 8 | box | box | identical | ✓ |
| 9 | child | person | not judged yet | ? |
| 10 | horse | horse | identical | ✓ |
| 11 | hat | helmet | not judged yet | ? |

**Relations: 5/12 right, triplets: 1/12 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| box #8 - on - ground #1 | 0-5.2s | on | 0-5.88571s | identical | 0.88 | ✓ | ✓ |
| child #5 - wearing - hat #7 | 0-20.6s | wearing | 0-20.6s | identical | 1.00 | ✓ | ? |
| child #9 - wearing - hat #11 | 0-5.4s, 10.8-20.6s | wearing | 0-20.6s | identical | 0.74 | ✓ | ? |
| child #9 - looking at - child #5 | 0-5.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - looking at - child #5 | 5-8s | nothing for this pair | - | - | - | ✗ | ✗ |
| horse #6 - walking on - ground #1 | 0-20.6s | moving across (+1 more) | 0-20.6s | not judged yet | 1.00 | ? | ? |
| horse #10 - walking on - ground #1 | 0-5.4s, 10.8-20.6s | moving across (+1 more) | 0-20.6s | not judged yet | 0.74 | ? | ? |
| adult #4 - walking on - ground #1 | 5-8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #5 - riding - horse #6 | 0-20.6s | riding (+1 more) | 0-20.6s | identical | 1.00 | ✓ | ? |
| child #9 - riding - horse #10 | 0-5.4s, 10.8-20.6s | riding (+1 more) | 0-20.6s | identical | 0.74 | ✓ | ? |
| adult #4 - guiding - child #5 | 0-20.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - guiding - child #9 | 0-20.6s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (17): child #5 - moving across - ground #1 [0-20.6s]; child #9 - moving across - ground #1 [0-20.6s]; horse #6 - moving with - horse #10 [0-20.6s]; horse #6 - next to - horse #10 [0-20.6s]; child #5 - moving with - child #9 [0-20.6s]; child #5 - next to - child #9 [0-20.6s]; horse #6 - in front of - wall #3 [0-20.6s]; horse #10 - in front of - wall #3 [0-20.6s]; child #5 - in front of - wall #3 [0-20.6s]; child #9 - in front of - wall #3 [0-20.6s]


## 1052_8530515192

72.4 s, 72 frames read | human: 15 objects, 28 relations | TRASER: 15 objects, 31 relations, valid JSON, 1258 tokens

**Objects: 8/15 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | adult | person | not judged yet | ? |
| 2 | child | child | identical | ✓ |
| 3 | table | tablecloth | not judged yet | ? |
| 4 | chair | chair | identical | ✓ |
| 5 | candle | candle | identical | ✓ |
| 6 | cake | cake | identical | ✓ |
| 7 | adult | person | not judged yet | ? |
| 8 | child | girl | not judged yet | ? |
| 9 | chair | chair | identical | ✓ |
| 10 | candle | candle | identical | ✓ |
| 11 | cake | cake | identical | ✓ |
| 12 | adult | person | not judged yet | ? |
| 13 | child | child | identical | ✓ |
| 14 | adult | person | not judged yet | ? |
| 15 | child | person | not judged yet | ? |

**Relations: 5/28 right, triplets: 2/28 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| child #8 - blowing - candle #10 | 60.8-68.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - touching - child #2 | 0-0.8s, 2.4-3.6s, 5.6-6.8s, 21-24s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #15 - beside - child #2 | 39-72.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #2 - sitting on - chair #4 | 0-72.4s | sitting on (+1 more) | 0-72.4s | identical | 1.00 | ✓ | ✓ |
| cake #6 - on - table #3 | 0-72.4s | on | 0-72.4s | identical | 1.00 | ✓ | ? |
| candle #5 - on - cake #6 | 0-72.4s | on (+1 more) | 0-72.4s | identical | 1.00 | ✓ | ✓ |
| child #2 - beside - table #3 | 0-72.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #8 - sitting on - chair #9 | 0-72.4s | sitting on (+1 more) | 0-72.4s | identical | 1.00 | ✓ | ? |
| cake #11 - on - table #3 | 0-72.4s | on | 0-72.4s | identical | 1.00 | ✓ | ? |
| child #8 - beside - table #3 | 0-72.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #13 - beside - table #3 | 0-72.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #1 - beside - child #2 | 0-72.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - beside - child #8 | 0-72.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - touching - child #2 | 10.2-12s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #2 - touching - adult #1 | 1.2-2.2s, 4.2-13.6s, 34-36.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #2 - blowing - candle #5 | 17.8-23.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #8 - touching - child #2 | 21.8-23.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - beside - table #3 | 26-39.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #2 - touching - adult #7 | 25.8-33s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #2 - kissing - adult #1 | 38.8-39.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #1 - touching - chair #4 | 36.2-42.6s | sitting on (+1 more) | 0-72.4s | not judged yet | 0.09 | ✗ | ✗ |
| adult #7 - touching - child #8 | 42.8-44.2s, 61.6-67.4s, 70-71.4s, 71.8-72.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #1 - touching - child #8 | 46.2-47.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #2 - touching - child #8 | 47.8-50s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #2 - talking to - child #8 | 52.2-56.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #1 - touching - child #2 | 54-55.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #2 - hugging - child #8 | 47.6-49.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - lighting - candle #10 | 26.4-39.2s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (21): adult #1 - holding - candle #5 [0-72.4s]; adult #1 - cutting - cake #6 [0-72.4s]; adult #1 - looking at - cake #6 [0-72.4s]; adult #1 - cutting cake - cake #6 [0-72.4s]; child #2 - looking at - cake #6 [0-72.4s]; child #8 - looking at - cake #6 [0-72.4s]; candle #10 - on - cake #11 [0-72.4s]; cake #6 - in front of - child #2 [0-72.4s]; cake #11 - in front of - child #2 [0-72.4s]; cake #6 - in front of - child #8 [0-72.4s]


## 1100_9117425466

23.2 s, 23 frames read | human: 8 objects, 15 relations | TRASER: 8 objects, 26 relations, valid JSON, 884 tokens

**Objects: 4/8 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | sky | cloud | not judged yet | ? |
| 2 | tree | tree | identical | ✓ |
| 3 | ground | basketball court | not judged yet | ? |
| 4 | grass | grass | identical | ✓ |
| 5 | adult | person | not judged yet | ? |
| 6 | child | child | identical | ✓ |
| 7 | ball | sports ball | not judged yet | ? |
| 8 | child | child | identical | ✓ |

**Relations: 0/15 right, triplets: 0/15 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #5 - walking on - ground #3 | 16.8-21.4s | on | 13.113-22.1913s | not judged yet | 0.51 | ? | ? |
| child #8 - lying on - ground #3 | 6.8-11.8s | on | 0-22.1913s | not judged yet | 0.23 | ✗ | ✗ |
| child #6 - standing on - ground #3 | 0-2.6s | on | 0-22.1913s | not judged yet | 0.12 | ✗ | ✗ |
| child #8 - standing on - ground #3 | 0-2.6s | on | 0-22.1913s | not judged yet | 0.12 | ✗ | ✗ |
| child #6 - picking - ball #7 | 3.4-8.8s | dribbles | 0-2.01739s, 3.02609-11.0957s | not judged yet | 0.54 | ? | ? |
| child #8 - picking - ball #7 | 3.6-5.6s | dribbles | 11.0957-20.1739s | not judged yet | 0.00 | ✗ | ✗ |
| child #6 - kicking - ball #7 | 9.4-10.6s | dribbles | 0-2.01739s, 3.02609-11.0957s | not judged yet | 0.12 | ✗ | ✗ |
| child #8 - toward - ball #7 | 14.6-16.6s, 19.8-21.8s | dribbles | 11.0957-20.1739s | not judged yet | 0.22 | ✗ | ✗ |
| adult #5 - running on - ground #3 | 14-15.4s | on | 13.113-22.1913s | not judged yet | 0.15 | ✗ | ✗ |
| adult #5 - picking - ball #7 | 15.4-16.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #8 - grabbing - ball #7 | 16.4-17.8s | dribbles | 11.0957-20.1739s | not judged yet | 0.15 | ✗ | ✗ |
| child #8 - kicking - ball #7 | 18-19.8s | dribbles | 11.0957-20.1739s | not judged yet | 0.20 | ✗ | ✗ |
| child #6 - toward - ball #7 | 19.8-21.4s | dribbles | 0-2.01739s, 3.02609-11.0957s | not judged yet | 0.00 | ✗ | ✗ |
| child #6 - playing with - ball #7 | 0-21.4s | dribbles | 0-2.01739s, 3.02609-11.0957s | not judged yet | 0.47 | ✗ | ✗ |
| child #8 - playing with - ball #7 | 0-21.4s | dribbles | 11.0957-20.1739s | not judged yet | 0.42 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (21): child #6 - approaches - child #8 [10.087-13.113s]; child #6 - moves away from - child #8 [13.113-20.1739s]; child #6 - plays with - child #8 [0-20.1739s]; child #6 - near - child #8 [0-20.1739s]; ball #7 - moves across - ground #3 [0-2.01739s, 3.02609-23.2s]; ball #7 - on - ground #3 [0-2.01739s, 3.02609-23.2s]; child #6 - in front of - tree #2 [0-22.1913s]; child #8 - in front of - tree #2 [0-22.1913s]; ball #7 - in front of - tree #2 [0-2.01739s, 3.02609-22.1913s]; adult #5 - in front of - tree #2 [13.113-22.1913s]


## 1122_3393449055

18.4 s, 18 frames read | human: 9 objects, 11 relations | TRASER: 9 objects, 31 relations, valid JSON, 1053 tokens

**Objects: 4/9 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | wall | cabinet | not judged yet | ? |
| 2 | cabinet | cabinet door | semantic overlap | ✓ |
| 3 | adult | person | not judged yet | ? |
| 4 | child | baby | not judged yet | ? |
| 5 | dog | dog | identical | ✓ |
| 6 | table | table | identical | ✓ |
| 7 | hat | baseball cap | hypernym/hyponym | ✓ |
| 8 | adult | person | not judged yet | ? |
| 9 | hat | toy | not judged yet | ? |

**Relations: 5/11 right, triplets: 0/11 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #3 - holding - child #4 | 0-18.4s | holding (+3 more) | 0-19.4222s | identical | 0.95 | ✓ | ? |
| adult #3 - looking at - child #4 | 0-18.4s | looking at (+3 more) | 0-19.4222s | identical | 0.95 | ✓ | ? |
| adult #3 - wearing - hat #7 | 0-18.4s | wearing | 4.08889-15.3333s | identical | 0.61 | ✓ | ? |
| adult #8 - holding - dog #5 | 0-12s | holding (+3 more) | 0-12.2667s | identical | 0.98 | ✓ | ? |
| adult #8 - looking at - dog #5 | 0-12s | looking at (+3 more) | 0-12.2667s | identical | 0.98 | ✓ | ? |
| adult #8 - wearing - hat #9 | 7.8-13.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #5 - playing with - child #4 | 0-8.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #5 - kissing - child #4 | 0-8.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #3 - next to - adult #8 | 0-13.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #3 - cleaning - child #4 | 13-15.4s | holding (+3 more) | 0-19.4222s | not judged yet | 0.12 | ✗ | ✗ |
| dog #5 - licking - child #4 | 0-2.4s, 3.4-5s, 6.6-7.8s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (22): adult #3 - in front of - wall #1 [0-19.4222s]; child #4 - in front of - wall #1 [0-19.4222s]; dog #5 - in front of - wall #1 [0-12.2667s]; adult #8 - in front of - wall #1 [0-14.3111s]; table #6 - in front of - wall #1 [0-16.3556s]; cabinet #2 - on - wall #1 [0-15.3333s]; adult #3 - in front of - cabinet #2 [0-15.3333s]; child #4 - in front of - cabinet #2 [0-15.3333s]; dog #5 - in front of - cabinet #2 [0-12.2667s]; adult #8 - in front of - cabinet #2 [0-14.3111s]


## 1124_9861436503

64.6 s, 65 frames read | human: 13 objects, 11 relations | TRASER: 12 objects, 33 relations, valid JSON, 1332 tokens

**Objects: 5/13 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | toy horse | not judged yet | ? |
| 2 | wall | wall | identical | ✓ |
| 3 | door | door (uncertain) | identical | ✓ |
| 4 | curtain | - | no label from TRASER | ✗ |
| 5 | shelf | cabinet | not judged yet | ? |
| 6 | adult | person | not judged yet | ? |
| 7 | child | child | identical | ✓ |
| 8 | dog | horse | not judged yet | ? |
| 9 | sofa | sofa | identical | ✓ |
| 10 | table | coffee table | not judged yet | ? |
| 11 | toy | horse | not judged yet | ? |
| 12 | adult | hand | not judged yet | ? |
| 13 | sofa | sofa | identical | ✓ |

**Relations: 1/11 right, triplets: 0/11 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| dog #8 - playing with - child #7 | 0-20.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - sitting on - toy #11 | 0-29.8s, 43.8-60.2s | pushes (+3 more) | 0-64.6s | not judged yet | 0.72 | ? | ? |
| dog #8 - biting - toy #11 | 20.2-64.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - walking on - floor #1 | 39.6-43.8s, 60.2-64.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #6 - sitting on - sofa #13 | 41.8-64.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| toy #11 - on - floor #1 | 0-64.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| toy #11 - in front of - table #10 | 0-35.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| toy #11 - in front of - sofa #9 | 36.8-64.6s | in front of | 22.8585-64.6s | identical | 0.67 | ✓ | ? |
| table #10 - in front of - sofa #9 | 0-64.6s | in front of | 40.7477-54.6615s, 58.6369-64.6s | identical | 0.31 | ✗ | ✗ |
| child #7 - swinging - toy #11 | 0-30.6s, 45-55.2s | pushes (+3 more) | 0-64.6s | not judged yet | 0.63 | ? | ? |
| child #7 - getting down on - toy #11 | 29.4-30.6s, 55-60.2s | pushes (+3 more) | 0-64.6s | not judged yet | 0.10 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (27): child #7 - moves away from - table #10 [40.7477-54.6615s]; child #7 - approaches - sofa #9 [40.7477-46.7108s]; child #7 - moves away from - sofa #9 [53.6677-64.6s]; child #7 - in front of - sofa #9 [22.8585-64.6s]; child #7 - in front of - shelf #5 [0-54.6615s]; child #7 - in front of - wall #2 [0-54.6615s]; child #7 - in front of - sofa #13 [40.7477-64.6s]; child #7 - in front of - adult #6 [40.7477-54.6615s]; toy #11 - in front of - shelf #5 [0-54.6615s]; toy #11 - in front of - wall #2 [0-54.6615s]


## 1161_5895320023

49.4 s, 49 frames read | human: 30 objects, 9 relations | TRASER: 29 objects, 41 relations, valid JSON, 2279 tokens

**Objects: 13/30 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | dog | not judged yet | ? |
| 2 | wall | balloon | not judged yet | ? |
| 3 | shoe | shoe (uncertain) | identical | ✓ |
| 4 | pillow | blanket | not judged yet | ? |
| 5 | door | window | not judged yet | ? |
| 6 | curtain | curtain | identical | ✓ |
| 7 | window | curtain | not judged yet | ? |
| 8 | adult | person | not judged yet | ? |
| 9 | dog | dog | identical | ✓ |
| 10 | sofa | sofa | identical | ✓ |
| 11 | table | tablecloth | not judged yet | ? |
| 12 | chair | chair | identical | ✓ |
| 13 | light | cushion | not judged yet | ? |
| 14 | ball | balloon | not judged yet | ? |
| 15 | pillow | blanket | not judged yet | ? |
| 16 | door | door | identical | ✓ |
| 17 | window | window | identical | ✓ |
| 18 | adult | person | not judged yet | ? |
| 19 | dog | dog | identical | ✓ |
| 20 | sofa | sofa | identical | ✓ |
| 21 | table | tablecloth | not judged yet | ? |
| 22 | chair | chair | identical | ✓ |
| 23 | ball | - | no label from TRASER | ✗ |
| 24 | window | window | identical | ✓ |
| 25 | adult | person | not judged yet | ? |
| 26 | table | box | not judged yet | ? |
| 27 | chair | chair | identical | ✓ |
| 28 | adult | person | not judged yet | ? |
| 29 | chair | chair | identical | ✓ |
| 30 | adult | person | not judged yet | ? |

**Relations: 0/9 right, triplets: 0/9 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #8 - sitting on - sofa #10 | 0-49.4s | in front of | 0-21.1714s | not judged yet | 0.43 | ✗ | ✗ |
| dog #19 - lying on - sofa #10 | 0-49.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| sofa #10 - in front of - adult #18 | 18.6-49.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #28 - sitting on - sofa #20 | 27.2-49.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #9 - chasing - ball #14 | 0-49.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #18 - picking - ball #14 | 16.8-19s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #25 - picking - ball #14 | 27.2-29.4s, 30.4-32.4s, 33.2-34.4s, 36-37.2s, 39-40.4s | holding (+2 more) | 28.2286-42.3429s | not judged yet | 0.46 | ✗ | ✗ |
| dog #9 - playing with - ball #14 | 0-49.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #9 - jumping from - floor #1 | 26.4-27.4s, 29.4-30.4s, 32-33.4s, 34.2-35.2s, 37.2-38.2s, 40.4-41.6s, 42.6-44.2s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (37): adult #8 - holding - ball #14 [0-20.1633s]; adult #8 - looking at - ball #14 [0-20.1633s]; ball #14 - moving away from - adult #8 [19.1551-21.1714s]; ball #14 - approaching - adult #25 [26.2122-29.2367s]; ball #14 - moving toward - table #26 [42.3429-45.3673s]; ball #14 - moving away from - table #26 [45.3673-48.3918s]; ball #14 - above - table #26 [31.2531-50.4082s]; ball #14 - moving toward - sofa #20 [46.3755-48.3918s]; ball #14 - moving away from - sofa #20 [48.3918-50.4082s]; ball #14 - above - sofa #20 [26.2122-50.4082s]


## 1164_6895784766

44.6 s, 45 frames read | human: 16 objects, 14 relations | TRASER: 14 objects, 21 relations, valid JSON, 2121 tokens

**Objects: 6/16 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | toy car | not judged yet | ? |
| 2 | ceiling | ceiling light fixture | semantic overlap | ✓ |
| 3 | wall | wall | identical | ✓ |
| 4 | door | door | identical | ✓ |
| 5 | shelf | bookshelf | not judged yet | ? |
| 6 | basket | basketball hoop | not judged yet | ? |
| 7 | adult | child | not judged yet | ? |
| 8 | child | child | identical | ✓ |
| 9 | bed | drawer (uncertain) | not judged yet | ? |
| 10 | sofa | trash can (uncertain) | not judged yet | ? |
| 11 | light | lamp | hypernym/hyponym | ✓ |
| 12 | ball | basketball | not judged yet | ? |
| 13 | shelf | - | no label from TRASER | ✗ |
| 14 | adult | - | no label from TRASER | ✗ |
| 15 | child | child | identical | ✓ |
| 16 | ball | sports ball (uncertain) | not judged yet | ? |

**Relations: 0/14 right, triplets: 0/14 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #7 - kicking - ball #16 | 26.6-27.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| basket #6 - next to - shelf #5 | 0-44.6s | in front of | 0-11.8933s, 16.8489-45.5911s | not judged yet | 0.87 | ? | ? |
| child #8 - holding - ball #12 | 0-0.8s, 17.4-44.6s | holding (+1 more) | 0-1.98222s, 2.97333-4.95556s, 9.91111-10.9022s, 11.8933-12.8844s, 13.8756-14.8667s, 15.8578-16.8489s, 17.84-18.8311s, 19.8222-20.8133s, 21.8044-22.7956s, 23.7867-24.7778s, 25.7689-26.76s, 27.7511-28.7422s, 29.7333-30.7244s, 31.7156-32.7067s, 33.6978-34.6889s | identical | 0.28 | ✗ | ✗ |
| child #8 - standing on - floor #1 | 0-34.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #15 - standing on - floor #1 | 0-44.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #15 - holding - ball #12 | 6.4-7.8s | holding (+1 more) | 2.97333-4.95556s, 9.91111-10.9022s, 11.8933-12.8844s, 13.8756-14.8667s, 15.8578-16.8489s, 17.84-18.8311s, 19.8222-20.8133s, 21.8044-22.7956s, 23.7867-24.7778s, 25.7689-26.76s, 27.7511-28.7422s, 29.7333-30.7244s, 31.7156-32.7067s, 33.6978-34.6889s | identical | 0.00 | ✗ | ✗ |
| child #8 - holding - ball #16 | 7.6-10.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #15 - holding - ball #16 | 10.6-16.2s, 18.2-20.2s, 28.4-32.8s, 35.4-38s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - holding - child #8 | 31.6-34.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #8 - throwing - ball #12 | 0-1.2s | holding (+1 more) | 0-1.98222s, 2.97333-4.95556s, 9.91111-10.9022s, 11.8933-12.8844s, 13.8756-14.8667s, 15.8578-16.8489s, 17.84-18.8311s, 19.8222-20.8133s, 21.8044-22.7956s, 23.7867-24.7778s, 25.7689-26.76s, 27.7511-28.7422s, 29.7333-30.7244s, 31.7156-32.7067s, 33.6978-34.6889s | not judged yet | 0.07 | ✗ | ✗ |
| child #15 - throwing - ball #12 | 6.8-7.8s | holding (+1 more) | 2.97333-4.95556s, 9.91111-10.9022s, 11.8933-12.8844s, 13.8756-14.8667s, 15.8578-16.8489s, 17.84-18.8311s, 19.8222-20.8133s, 21.8044-22.7956s, 23.7867-24.7778s, 25.7689-26.76s, 27.7511-28.7422s, 29.7333-30.7244s, 31.7156-32.7067s, 33.6978-34.6889s | not judged yet | 0.00 | ✗ | ✗ |
| child #15 - carrying - ball #16 | 10-13s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #15 - throwing - ball #16 | 12.8-14.6s, 20-20.8s, 37.8-38.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #8 - squatting on - floor #1 | 16.8-17.8s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (16): child #8 - playing with - child #15 [0-1.98222s, 2.97333-4.95556s, 9.91111-10.9022s, 11.8933-12.8844s, 13.8756-14.8667s, 15.8578-16.8489s, 17.84-18.8311s, 19.8222-20.8133s, 21.8044-22.7956s, 23.7867-24.7778s, 25.7689-26.76s, 27.7511-28.7422s, 29.7333-30.7244s, 31.7156-32.7067s, 33.6978-34.6889s]; child #15 - playing with - child #8 [0-1.98222s, 2.97333-4.95556s, 9.91111-10.9022s, 11.8933-12.8844s, 13.8756-14.8667s, 15.8578-16.8489s, 17.84-18.8311s, 19.8222-20.8133s, 21.8044-22.7956s, 23.7867-24.7778s, 25.7689-26.76s, 27.7511-28.7422s, 29.7333-30.7244s, 31.7156-32.7067s, 33.6978-34.6889s]; child #8 - in front of - basket #6 [0-35.68s]; child #15 - in front of - basket #6 [0-45.5911s]; child #8 - in front of - shelf #5 [0-11.8933s, 16.8489-35.68s]; child #15 - in front of - shelf #5 [0-11.8933s, 16.8489-45.5911s]; basket #6 - in front of - wall #3 [0-45.5911s]; shelf #5 - against - wall #3 [0-11.8933s, 16.8489-45.5911s]; door #4 - in - wall #3 [0-45.5911s]; ceiling #2 - above - basket #6 [7.92889-45.5911s]


## 1203_8316378691

60.2 s, 60 frames read | human: 23 objects, 15 relations | TRASER: 22 objects, 42 relations, valid JSON, 2087 tokens

**Objects: 4/23 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | chair leg | not judged yet | ? |
| 2 | floor | chair leg | not judged yet | ? |
| 3 | wall | - | no label from TRASER | ✗ |
| 4 | carpet | doormat | not judged yet | ? |
| 5 | book | hand | not judged yet | ? |
| 6 | adult | person | not judged yet | ? |
| 7 | child | person | not judged yet | ? |
| 8 | dog | plush toy | not judged yet | ? |
| 9 | sofa | sofa | identical | ✓ |
| 10 | table | coffee table | not judged yet | ? |
| 11 | cup | cup | identical | ✓ |
| 12 | bag | fabric | not judged yet | ? |
| 13 | box | box | identical | ✓ |
| 14 | camera | cell phone | not judged yet | ? |
| 15 | adult | person | not judged yet | ? |
| 16 | camera | cell phone | not judged yet | ? |
| 17 | adult | person | not judged yet | ? |
| 18 | cup | cup | identical | ✓ |
| 19 | camera | cell phone | not judged yet | ? |
| 20 | adult | person | not judged yet | ? |
| 21 | adult | person | not judged yet | ? |
| 22 | adult | person | not judged yet | ? |
| 23 | adult | arm | not judged yet | ? |

**Relations: 5/15 right, triplets: 0/15 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #17 - holding - cup #11 | 0-45.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #23 - holding - bag #12 | 48.6-52.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - standing on - carpet #4 | 58.2-60.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #6 - opening - box #13 | 13.8-17s | opening (+3 more) | 10.0333-17.0567s | identical | 0.46 | ✗ | ✗ |
| adult #22 - standing on - carpet #4 | 42.6-60.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #15 - on - sofa #9 | 0-60.2s | on (+1 more) | 0-45.15s, 52.1733-60.2s | identical | 0.88 | ✓ | ? |
| adult #17 - on - sofa #9 | 0-60.2s | on (+1 more) | 0-45.15s, 52.1733-60.2s | identical | 0.88 | ✓ | ? |
| child #7 - on - sofa #9 | 0-12s, 25.6-55.2s | on (+1 more) | 0-45.15s, 52.1733-60.2s | identical | 0.57 | ✓ | ? |
| adult #6 - holding - box #13 | 0-14.2s | holding (+3 more) | 0-25.0833s | identical | 0.57 | ✓ | ? |
| child #7 - holding - dog #8 | 16.8-60.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| box #13 - on - table #10 | 7.4-60.2s | on (+1 more) | 0-45.15s, 52.1733-60.2s | identical | 0.76 | ✓ | ? |
| dog #8 - in - box #13 | 0-21.6s, 59.8-60.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #20 - holding - camera #14 | 0-60.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #21 - holding - camera #19 | 0-60.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #22 - holding - camera #16 | 0-60.2s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (30): adult #6 - holding - cup #11 [25.0833-27.09s]; adult #6 - holding - camera #14 [27.09-30.1s]; adult #6 - holding - camera #16 [27.09-30.1s]; adult #6 - holding - camera #19 [27.09-30.1s]; adult #6 - holding - bag #12 [47.1567-52.1733s]; adult #6 - looking at - bag #12 [47.1567-52.1733s]; adult #6 - holding - dog #8 [55.1833-60.2s]; adult #6 - looking at - dog #8 [55.1833-60.2s]; table #10 - in front of - sofa #9 [0-45.15s, 52.1733-60.2s]; box #13 - in front of - sofa #9 [0-45.15s, 52.1733-60.2s]


## 22cc4d54-34be-4580-983a-9e710e831c16

43.4 s, 43 frames read | human: 10 objects, 18 relations | TRASER: 0 objects, 0 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 0/10 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | tree | - | no label from TRASER | ✗ |
| 2 | grass | - | no label from TRASER | ✗ |
| 3 | scissor | - | no label from TRASER | ✗ |
| 4 | basket | - | no label from TRASER | ✗ |
| 5 | adult | - | no label from TRASER | ✗ |
| 6 | fruit | - | no label from TRASER | ✗ |
| 7 | fruit | - | no label from TRASER | ✗ |
| 8 | fruit | - | no label from TRASER | ✗ |
| 9 | fruit | - | no label from TRASER | ✗ |
| 10 | fruit | - | no label from TRASER | ✗ |

**Relations: 0/18 right, triplets: 0/18 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #5 - holding - scissor #3 | 0-43.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - fruit #7 | 2.2-13.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| scissor #3 - cutting - tree #1 | 2.8-4.6s, 8.6-10.8s, 17.8-21.2s, 33.8-36s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - fruit #6 | 8.2-13.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| fruit #6 - in - basket #4 | 13-43.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| fruit #7 - in - basket #4 | 13.4-43.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - fruit #8 | 16.8-24.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| fruit #8 - in - basket #4 | 24.2-43.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - fruit #10 | 29.6-39.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| fruit #10 - in - basket #4 | 39.8-43.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - fruit #9 | 29.6-43.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| scissor #3 - cutting - fruit #10 | 38-39.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| scissor #3 - cutting - fruit #9 | 40.4-42.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| fruit #6 - hanging from - tree #1 | 0-10.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| fruit #7 - hanging from - tree #1 | 0-4.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| fruit #8 - hanging from - tree #1 | 16.4-21.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| fruit #9 - hanging from - tree #1 | 31-36s | nothing for this pair | - | - | - | ✗ | ✗ |
| fruit #10 - hanging from - tree #1 | 31-36s | nothing for this pair | - | - | - | ✗ | ✗ |


## 6e0a6558-c212-4cab-b374-007671edb59c_2

61.0 s, 61 frames read | human: 40 objects, 16 relations | TRASER: 39 objects, 64 relations, valid JSON, 3506 tokens

**Objects: 16/40 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | person | mismatch | ✗ |
| 2 | ceiling | ceiling fan | semantic overlap | ✓ |
| 3 | wall | refrigerator | not judged yet | ? |
| 4 | countertop | sink | not judged yet | ? |
| 5 | rack | basket | not judged yet | ? |
| 6 | board | tray | not judged yet | ? |
| 7 | rag | bowl (uncertain) | not judged yet | ? |
| 8 | dustbin | cup | not judged yet | ? |
| 9 | oven | box | not judged yet | ? |
| 10 | stove | oven | not judged yet | ? |
| 11 | sponge | sponge | identical | ✓ |
| 12 | shelf | door | not judged yet | ? |
| 13 | window | window | identical | ✓ |
| 14 | cabinet | chair | not judged yet | ? |
| 15 | door | mirror | mismatch | ✗ |
| 16 | fridge | refrigerator | not judged yet | ? |
| 17 | adult | hands | not judged yet | ? |
| 18 | sink | sink | identical | ✓ |
| 19 | faucet | faucet | identical | ✓ |
| 20 | table | table | identical | ✓ |
| 21 | chair | chair | identical | ✓ |
| 22 | plate | - | no label from TRASER | ✗ |
| 23 | bottle | cup | not judged yet | ? |
| 24 | cup | cup | identical | ✓ |
| 25 | paper | paper towel roll | not judged yet | ? |
| 26 | bag | towel | not judged yet | ? |
| 27 | board | tray | not judged yet | ? |
| 28 | dustbin | cup | not judged yet | ? |
| 29 | sponge | sponge | identical | ✓ |
| 30 | cabinet | cabinet | identical | ✓ |
| 31 | chair | chair | identical | ✓ |
| 32 | cup | cup | identical | ✓ |
| 33 | paper | chopping board | not judged yet | ? |
| 34 | dustbin | bucket | not judged yet | ? |
| 35 | cabinet | microwave oven | not judged yet | ? |
| 36 | chair | chair | identical | ✓ |
| 37 | cup | cup | identical | ✓ |
| 38 | paper | chopping board | not judged yet | ? |
| 39 | cabinet | cabinet | identical | ✓ |
| 40 | cup | cup | identical | ✓ |

**Relations: 3/16 right, triplets: 0/16 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #17 - opening - faucet #19 | 0.4-1s, 38.8-39.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #17 - closing - faucet #19 | 5.4-8s, 42.2-43.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #17 - holding - cup #40 | 0-50.2s | holding (+5 more) | 0-11s, 12-23s, 36-46s | identical | 0.64 | ✓ | ? |
| cup #40 - on - paper #38 | 50.2-61s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #17 - walking on - floor #1 | 11.2-14s, 25.6-38.8s, 46.2-48.6s, 56.4-461s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #17 - cleaning - cup #40 | 0.6-10.2s, 38.8-45.2s | holding (+5 more) | 0-11s, 12-23s, 36-46s | not judged yet | 0.50 | ? | ? |
| adult #17 - holding - bottle #23 | 14-22.4s | holding (+5 more) | 12-23s, 48-52s | identical | 0.56 | ✓ | ? |
| adult #17 - pouring - bottle #23 | 14.8-21.2s | holding (+5 more) | 12-23s, 48-52s | not judged yet | 0.43 | ✗ | ✗ |
| adult #17 - holding - paper #25 | 51.8-55.6s | holding (+5 more) | 52-56s | identical | 0.86 | ✓ | ? |
| paper #25 - on - table #20 | 0-61s | nothing for this pair | - | - | - | ✗ | ✗ |
| paper #33 - on - table #20 | 0-61s | nothing for this pair | - | - | - | ✗ | ✗ |
| paper #38 - on - table #20 | 0-61s | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #21 - on - floor #1 | 0-61s | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #21 - beside - table #20 | 0-61s | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #31 - on - floor #1 | 0-61s | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #31 - beside - table #20 | 0-61s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (46): adult #17 - holding - dustbin #8 [56-60s]; adult #17 - washing - dustbin #8 [56-60s]; adult #17 - holding - dustbin #8 [56-60s]; adult #17 - washing - dustbin #8 [56-60s]; adult #17 - holding - dustbin #8 [56-60s]; adult #17 - washing - dustbin #8 [56-60s]; adult #17 - holding - dustbin #28 [56-60s]; adult #17 - washing - dustbin #28 [56-60s]; adult #17 - holding - dustbin #28 [56-60s]; adult #17 - washing - dustbin #28 [56-60s]


## P02_10

48.8 s, 49 frames read | human: 28 objects, 5 relations | TRASER: 26 objects, 30 relations, valid JSON, 2152 tokens

**Objects: 10/28 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | doormat | semantic overlap | ✓ |
| 2 | wall | wall | identical | ✓ |
| 3 | countertop | countertop | identical | ✓ |
| 4 | simmering | mixture | not judged yet | ? |
| 5 | rack | - | no label from TRASER | ✗ |
| 6 | spatula | wooden spoon | not judged yet | ? |
| 7 | teapot | - | no label from TRASER | ✗ |
| 8 | board | chopping board | not judged yet | ? |
| 9 | cover | lid | not judged yet | ? |
| 10 | glove | sponge | not judged yet | ? |
| 11 | dustbin | trash can | not judged yet | ? |
| 12 | washer | washing machine door | not judged yet | ? |
| 13 | oven | oven | identical | ✓ |
| 14 | stove | stove | identical | ✓ |
| 15 | pan | pan | identical | ✓ |
| 16 | sponge | bottle | not judged yet | ? |
| 17 | cabinet | cabinet door | semantic overlap | ✓ |
| 18 | towel | towel | identical | ✓ |
| 19 | adult | hand | not judged yet | ? |
| 20 | sink | container | not judged yet | ? |
| 21 | faucet | bottle | not judged yet | ? |
| 22 | fork | handle | not judged yet | ? |
| 23 | plate | strainer | not judged yet | ? |
| 24 | ball | ball | identical | ✓ |
| 25 | cover | pot | not judged yet | ? |
| 26 | glove | towel | not judged yet | ? |
| 27 | pan | pot | not judged yet | ? |
| 28 | cabinet | cabinet door | semantic overlap | ✓ |

**Relations: 2/5 right, triplets: 0/5 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #19 - holding - spatula #6 | 2.8-46.4s | holding | 4.97959-45.8122s | identical | 0.94 | ✓ | ? |
| adult #19 - holding - cover #9 | 3.4-6.8s, 43.4-46s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #19 - touching - pan #15 | 6.8-43.4s | holding (+1 more) | 3.98367-45.8122s | not judged yet | 0.88 | ? | ? |
| adult #19 - in front of - stove #14 | 2.8-47.2s | above | 3.98367-46.8082s | not judged yet | 0.96 | ? | ? |
| adult #19 - stirring - simmering #4 | 6-43.2s | stirring (+1 more) | 4.97959-45.8122s | identical | 0.91 | ✓ | ? |

TRASER relations between pairs the humans did not annotate (24): pan #15 - moving away from - stove #14 [44.8163-46.8082s]; pan #15 - on - stove #14 [3.98367-45.8122s]; stove #14 - on - countertop #3 [0-46.8082s]; simmering #4 - in - pan #15 [4.97959-45.8122s]; spatula #6 - in - pan #15 [4.97959-45.8122s]; spatula #6 - above - pan #15 [4.97959-45.8122s]; cover #9 - on - countertop #3 [0-46.8082s]; glove #10 - on - countertop #3 [0-4.97959s, 5.97551-10.9551s, 11.951-12.9469s, 13.9429-14.9388s, 15.9347-16.9306s, 17.9265-20.9143s, 21.9102-22.9061s, 23.902-24.898s, 25.8939-26.8898s, 27.8857-28.8816s, 29.8776-30.8735s, 31.8694-32.8653s, 33.8612-34.8571s, 35.8531-36.849s, 37.8449-38.8408s, 39.8367-40.8327s, 41.8286-42.8245s, 43.8204-44.8163s, 45.8122-46.8082s]; plate #23 - on - countertop #3 [0-46.8082s]; cover #25 - on - countertop #3 [4.97959-5.97551s, 15.9347-46.8082s]

