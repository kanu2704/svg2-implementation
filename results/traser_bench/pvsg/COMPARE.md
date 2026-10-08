# pvsg: human labels vs TRASER, video by video

62 videos with a prediction. Lenient criterion, temporal IoU > 0.5. ✓ right, ✗ wrong, ? = the judge (Kimi K3) has not compared these two labels yet (identical text counts as right without the judge). Relation = same two objects, predicate not a mismatch, tIoU > 0.5; triplet = relation right and both object labels right. Made by `tools/bench_eval.py write_compare`.

**So far: objects 770/1282, relations 132/969, triplets 99/969** (unjudged pairs count as not right; scores in README.md)

| video | objects right | relations right | triplets right | not judged yet (?) |
|---|---|---|---|---|
| [0004_11566980553](#0004_11566980553) | 10/15 | 1/13 | 1/13 | 0 |
| [0010_8610561401](#0010_8610561401) | 4/5 | 1/8 | 1/8 | 0 |
| [0018_4748191834](#0018_4748191834) | 10/14 | 4/17 | 4/17 | 0 |
| [0027_4571353789](#0027_4571353789) | 10/16 | 4/17 | 1/17 | 0 |
| [0028_4021064662](#0028_4021064662) | 6/10 | 5/18 | 4/18 | 0 |
| [0039_6951351121](#0039_6951351121) | 12/17 | 2/13 | 2/13 | 0 |
| [0046_11919433184](#0046_11919433184) | 12/16 | 1/17 | 1/17 | 0 |
| [0051_3702633786](#0051_3702633786) | 7/12 | 0/15 | 0/15 | 0 |
| [0053_5599511471](#0053_5599511471) | 4/7 | 1/14 | 1/14 | 0 |
| [0054_2612939953](#0054_2612939953) | 11/15 | 2/17 | 2/17 | 0 |
| [0057_7001078933](#0057_7001078933) | 13/15 | 4/18 | 4/18 | 0 |
| [0062_6430774273](#0062_6430774273) | 4/6 | 2/13 | 2/13 | 0 |
| [0069_2740320945](#0069_2740320945) | 16/20 | 0/16 | 0/16 | 0 |
| [0075_11566764085](#0075_11566764085) | 9/10 | 3/12 | 3/12 | 0 |
| [0096_5296138427](#0096_5296138427) | 10/11 | 2/12 | 2/12 | 0 |
| [0be30efe-9d71-4698-8304-f1d441aeea58_1](#0be30efe-9d71-4698-8304-f1d441aeea58_1) | 5/12 | 1/10 | 1/10 | 0 |
| [1000_6828150903](#1000_6828150903) | 10/15 | 4/13 | 3/13 | 0 |
| [1001_7007447516](#1001_7007447516) | 17/22 | 2/9 | 2/9 | 0 |
| [1002_5280626374](#1002_5280626374) | 9/13 | 2/12 | 2/12 | 0 |
| [1005_4760962392](#1005_4760962392) | 13/17 | 0/20 | 0/20 | 0 |
| [1005_7031128593](#1005_7031128593) | 3/9 | 2/7 | 1/7 | 0 |
| [1005_7401573420](#1005_7401573420) | 14/20 | 4/23 | 4/23 | 0 |
| [1006_4580824633](#1006_4580824633) | 3/5 | 1/8 | 1/8 | 0 |
| [1007_6631583821](#1007_6631583821) | 8/10 | 5/12 | 5/12 | 0 |
| [1011_4633647136](#1011_4633647136) | 12/14 | 0/20 | 0/20 | 0 |
| [1012_4024008346](#1012_4024008346) | 10/11 | 5/8 | 4/8 | 0 |
| [1015_4698622422](#1015_4698622422) | 10/13 | 3/15 | 3/15 | 0 |
| [1017_3056841458](#1017_3056841458) | 11/14 | 4/16 | 3/16 | 0 |
| [1019_3768851893](#1019_3768851893) | 18/30 | 6/30 | 0/30 | 0 |
| [1020_2471845614](#1020_2471845614) | 21/22 | 9/27 | 9/27 | 0 |
| [1021_3478653250](#1021_3478653250) | 13/13 | 1/23 | 1/23 | 0 |
| [1021_4278168115](#1021_4278168115) | 11/11 | 9/21 | 9/21 | 0 |
| [1025_4615486172](#1025_4615486172) | 21/27 | 0/24 | 0/24 | 0 |
| [1025_6244382586](#1025_6244382586) | 11/11 | 7/12 | 7/12 | 0 |
| [1052_8530515192](#1052_8530515192) | 15/15 | 5/28 | 5/28 | 0 |
| [1100_9117425466](#1100_9117425466) | 8/8 | 1/15 | 1/15 | 0 |
| [1122_3393449055](#1122_3393449055) | 7/9 | 5/11 | 5/11 | 0 |
| [1124_9861436503](#1124_9861436503) | 8/13 | 2/11 | 0/11 | 0 |
| [1161_5895320023](#1161_5895320023) | 25/30 | 0/9 | 0/9 | 0 |
| [1164_6895784766](#1164_6895784766) | 11/16 | 0/14 | 0/14 | 0 |
| [1203_8316378691](#1203_8316378691) | 16/23 | 5/15 | 5/15 | 0 |
| [1bfe5ac2-cbf8-4364-8a30-60d97dd395df_1](#1bfe5ac2-cbf8-4364-8a30-60d97dd395df_1) | 9/19 | 0/14 | 0/14 | 0 |
| [22cc4d54-34be-4580-983a-9e710e831c16](#22cc4d54-34be-4580-983a-9e710e831c16) | 0/10 | 0/18 | 0/18 | 0 |
| [43b0205a-4e3c-46a7-9d1c-c04ead730180](#43b0205a-4e3c-46a7-9d1c-c04ead730180) | 4/26 | 0/8 | 0/8 | 0 |
| [6e0a6558-c212-4cab-b374-007671edb59c_2](#6e0a6558-c212-4cab-b374-007671edb59c_2) | 25/40 | 4/16 | 0/16 | 0 |
| [8be918b2-c819-4a84-98dc-5fe24835a4ac](#8be918b2-c819-4a84-98dc-5fe24835a4ac) | 7/14 | 0/12 | 0/12 | 0 |
| [P01_03](#p01_03) | 25/70 | 0/22 | 0/22 | 0 |
| [P02_10](#p02_10) | 17/28 | 3/5 | 0/5 | 0 |
| [P03_06](#p03_06) | 0/65 | 0/20 | 0/20 | 0 |
| [P04_27](#p04_27) | 18/34 | 0/13 | 0/13 | 0 |
| [P05_05](#p05_05) | 17/30 | 2/22 | 0/22 | 0 |
| [P08_07](#p08_07) | 19/26 | 2/10 | 0/10 | 0 |
| [P09_07](#p09_07) | 15/29 | 1/15 | 0/15 | 0 |
| [P11_11](#p11_11) | 20/44 | 2/15 | 0/15 | 0 |
| [P14_06](#p14_06) | 24/34 | 0/10 | 0/10 | 0 |
| [P19_06](#p19_06) | 17/42 | 0/13 | 0/13 | 0 |
| [P28_19](#p28_19) | 17/28 | 3/10 | 0/10 | 0 |
| [c20407ac-83d6-4c84-88cb-63bced9d456b](#c20407ac-83d6-4c84-88cb-63bced9d456b) | 6/11 | 0/12 | 0/12 | 0 |
| [c2e6d807-d903-4b64-98e1-2c07ca700c78_2](#c2e6d807-d903-4b64-98e1-2c07ca700c78_2) | 24/41 | 0/16 | 0/16 | 0 |
| [d1d4a1b3-a651-4eb8-bb7f-8d66982854fa](#d1d4a1b3-a651-4eb8-bb7f-8d66982854fa) | 25/44 | 0/41 | 0/41 | 0 |
| [d2222009-a717-4b16-91ce-6399c5bb798a](#d2222009-a717-4b16-91ce-6399c5bb798a) | 27/39 | 0/34 | 0/34 | 0 |
| [eed8d8d7-6773-493b-af21-880f0acb063a](#eed8d8d7-6773-493b-af21-880f0acb063a) | 6/16 | 0/10 | 0/10 | 0 |

## 0004_11566980553

57.4 s, 57 frames read | human: 15 objects, 13 relations | TRASER: 15 objects, 23 relations, valid JSON, 1344 tokens

**Objects: 10/15 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | floor | identical | ✓ |
| 2 | wall | wall | identical | ✓ |
| 3 | carpet | rug | synonym | ✓ |
| 4 | gift | blanket | mismatch | ✗ |
| 5 | tv | television (uncertain) | identical | ✓ |
| 6 | door | door frame (uncertain) | semantic overlap | ✓ |
| 7 | cabinet | sofa | mismatch | ✗ |
| 8 | adult | person | hypernym/hyponym | ✓ |
| 9 | child | child | identical | ✓ |
| 10 | sofa | sofa | identical | ✓ |
| 11 | light | lampshade | semantic overlap | ✓ |
| 12 | box | toy (uncertain) | mismatch | ✗ |
| 13 | cellphone | cellular telephone (uncertain) | synonym | ✓ |
| 14 | gift | plastic bag | mismatch | ✗ |
| 15 | cabinet | chair (uncertain) | mismatch | ✗ |

**Relations: 1/13 right, triplets: 1/13 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| child #9 - holding - gift #14 | 24.6-27.6s | holds (+4 more) | 23.1614-58.407s | identical | 0.09 | ✗ | ✗ |
| child #9 - opening - gift #14 | 30.8-44.8s | opens (+4 more) | 23.1614-27.1895s | identical | 0.00 | ✗ | ✗ |
| child #9 - walking on - floor #1 | 0-2.6s, 4.2-6.6s, 20-21s, 24.4-26.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - standing on - floor #1 | 6.6-20s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - sitting on - carpet #3 | 27.4-57.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - holding - gift #4 | 2.6-6.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - sitting on - sofa #10 | 4.8-21.6s, 22.6-29.8s, 34-35.6s | on | 4.02807-21.1474s | hypernym/hyponym | 0.62 | ✓ | ✓ |
| adult #8 - grabbing - gift #4 | 12.2-13.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - looking at - cellphone #13 | 5-7s, 14.4-20s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - holding - box #12 | 44.4-57.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - carrying - gift #4 | 3.4-7.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - holding - gift #4 | 7.2-14.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - carrying - gift #14 | 23.4-27.2s | holds (+4 more) | 23.1614-58.407s | hypernym/hyponym | 0.11 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (17): child #9 - approaches - sofa #10 [1.00702-4.02807s]; child #9 - moves away from - sofa #10 [21.1474-24.1684s]; child #9 - in front of - sofa #10 [1.00702-58.407s]; sofa #10 - on - floor #1 [0-58.407s]; cabinet #7 - on - floor #1 [0-1.00702s, 3.02105-5.03509s, 17.1193-27.1895s, 33.2316-35.2456s]; carpet #3 - on - floor #1 [3.02105-6.04211s, 23.1614-58.407s]; sofa #10 - in front of - wall #2 [0-32.2246s]; cabinet #7 - in front of - wall #2 [0-1.00702s, 3.02105-5.03509s, 17.1193-27.1895s]; child #9 - in front of - wall #2 [1.00702-32.2246s]; gift #14 - on - carpet #3 [23.1614-58.407s]


## 0010_8610561401

36.0 s, 36 frames read | human: 5 objects, 8 relations | TRASER: 5 objects, 13 relations, valid JSON, 487 tokens

**Objects: 4/5 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | wall | curtain | mismatch | ✗ |
| 2 | adult | person | hypernym/hyponym | ✓ |
| 3 | dog | dog | identical | ✓ |
| 4 | sofa | cushion | semantic overlap | ✓ |
| 5 | sofa | sofa | identical | ✓ |

**Relations: 1/8 right, triplets: 1/8 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #2 - next to - dog #3 | 0-24.2s | petting (+1 more) | 0-37s | mismatch | 0.65 | ✗ | ✗ |
| dog #3 - sitting on - sofa #5 | 0-1.2s, 32.8-36s | standing on (+1 more) | 0-37s | semantic overlap | 0.12 | ✗ | ✗ |
| dog #3 - standing on - sofa #4 | 1.2-32.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #2 - sitting on - sofa #4 | 0-36s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #3 - looking at - adult #2 | 0-36s | looking at (+2 more) | 0-37s | identical | 0.97 | ✓ | ✓ |
| dog #3 - touching - sofa #4 | 8.8-10.2s, 16.2-19.2s, 28.6-30.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #2 - looking at - dog #3 | 24.4-36s | looking at (+1 more) | 0-37s | identical | 0.31 | ✗ | ✗ |
| adult #2 - caressing - dog #3 | 32.2-36s | petting (+1 more) | 0-37s | synonym | 0.10 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (6): adult #2 - on - sofa #5 [0-37s]; sofa #4 - on - sofa #5 [0-37s]; dog #3 - in front of - wall #1 [0-37s]; adult #2 - in front of - wall #1 [0-37s]; sofa #5 - in front of - wall #1 [0-37s]; sofa #4 - in front of - wall #1 [0-37s]


## 0018_4748191834

33.2 s, 33 frames read | human: 14 objects, 17 relations | TRASER: 13 objects, 29 relations, valid JSON, 1296 tokens

**Objects: 10/14 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | - | no label from TRASER | ✗ |
| 2 | floor | table | mismatch | ✗ |
| 3 | wall | wall | identical | ✓ |
| 4 | cookie | cake slice | semantic overlap | ✓ |
| 5 | door | cabinet door | hypernym/hyponym | ✓ |
| 6 | adult | person | hypernym/hyponym | ✓ |
| 7 | child | child | identical | ✓ |
| 8 | table | tablecloth | semantic overlap | ✓ |
| 9 | chair | chair backrest | hypernym/hyponym | ✓ |
| 10 | candle | candle | identical | ✓ |
| 11 | cake | cake | identical | ✓ |
| 12 | camera | knife | mismatch | ✗ |
| 13 | adult | shirt | mismatch | ✗ |
| 14 | chair | chair | identical | ✓ |

**Relations: 4/17 right, triplets: 4/17 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #13 - in front of - wall #3 | 0-9.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #13 - walking on - floor #2 | 9.6-19s, 31.4-33.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - in front of - cake #11 | 0-33.4s | looking at | 0-25.1515s | mismatch | 0.75 | ✗ | ✗ |
| child #7 - looking at - adult #6 | 6.8-8.6s | next to | 0-34.2061s | mismatch | 0.05 | ✗ | ✗ |
| adult #6 - touching - child #7 | 9-22.6s | serving (+1 more) | 10.0606-25.1515s | semantic overlap | 0.78 | ✓ | ✓ |
| child #7 - sitting on - chair #9 | 0-33.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| cake #11 - on - table #8 | 0-33.4s | on | 0-34.2061s | identical | 0.98 | ✓ | ✓ |
| candle #10 - on - cake #11 | 0-33.4s | on (+1 more) | 0-34.2061s | identical | 0.98 | ✓ | ✓ |
| adult #13 - holding - camera #12 | 0-32.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - looking at - cake #11 | 8.4-32s | looking at | 0-25.1515s | identical | 0.52 | ✓ | ✓ |
| adult #6 - beside - table #8 | 9-33.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #13 - beside - table #8 | 11-32s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #13 - touching - candle #10 | 20-21s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #13 - touching - cake #11 | 21-22.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - blowing - candle #10 | 22.4-26s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #6 - touching - candle #10 | 25.8-27s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #6 - hugging - child #7 | 7.6-22.6s | serving (+1 more) | 10.0606-25.1515s | mismatch | 0.71 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (22): child #7 - holding - cookie #4 [0-25.1515s]; adult #6 - holding - camera #12 [10.0606-25.1515s]; adult #6 - cutting - cake #11 [10.0606-25.1515s]; adult #6 - looking at - cake #11 [10.0606-25.1515s]; adult #6 - wearing - adult #13 [0-34.2061s]; child #7 - sitting on - chair #14 [0-34.2061s]; cake #11 - in front of - wall #3 [0-34.2061s]; child #7 - in front of - wall #3 [0-34.2061s]; adult #6 - in front of - wall #3 [0-34.2061s]; chair #9 - behind - child #7 [0-34.2061s]


## 0027_4571353789

19.0 s, 19 frames read | human: 16 objects, 17 relations | TRASER: 15 objects, 32 relations, valid JSON, 1398 tokens

**Objects: 10/16 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | tree | tree | identical | ✓ |
| 2 | ground | floor | synonym | ✓ |
| 3 | floor | - | no label from TRASER | ✗ |
| 4 | wall | tent | mismatch | ✗ |
| 5 | adult | person | hypernym/hyponym | ✓ |
| 6 | table | tablecloth | semantic overlap | ✓ |
| 7 | light | string of lights | hypernym/hyponym | ✓ |
| 8 | box | speaker | mismatch | ✗ |
| 9 | camera | hand | mismatch | ✗ |
| 10 | car | car | identical | ✓ |
| 11 | adult | person | hypernym/hyponym | ✓ |
| 12 | light | string of lights | hypernym/hyponym | ✓ |
| 13 | camera | shoe | mismatch | ✗ |
| 14 | adult | person | hypernym/hyponym | ✓ |
| 15 | adult | arm | mismatch | ✗ |
| 16 | adult | person | hypernym/hyponym | ✓ |

**Relations: 4/17 right, triplets: 1/17 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #16 - walking on - ground #2 | 17.2-19s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - camera #9 | 0-19s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - standing on - ground #2 | 0-8.4s | on | 0-11s, 16-20s | hypernym/hyponym | 0.56 | ✓ | ✓ |
| adult #5 - walking on - ground #2 | 8.2-10.4s | on | 0-11s, 16-20s | hypernym/hyponym | 0.15 | ✗ | ✗ |
| adult #5 - looking at - adult #11 | 0-19s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - in front of - table #6 | 0-19s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - in front of - table #6 | 0-19s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - kissing - adult #11 | 5.6-7.2s | looking at (+2 more) | 0-11s | mismatch | 0.15 | ✗ | ✗ |
| adult #14 - holding - adult #11 | 0-12.2s | looking at (+2 more) | 0-11s | mismatch | 0.90 | ✗ | ✗ |
| box #8 - beside - table #6 | 0-19s | nothing for this pair | - | - | - | ✗ | ✗ |
| table #6 - beside - light #7 | 0-19s | under | 0-11s, 16-20s | mismatch | 0.70 | ✗ | ✗ |
| table #6 - in front of - wall #4 | 0-19s | in front of | 0-11s, 16-20s | identical | 0.70 | ✓ | ✗ |
| adult #11 - holding - camera #9 | 17.6-18.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| light #7 - over - wall #4 | 0-19s | above | 0-20s | synonym | 0.95 | ✓ | ✗ |
| light #12 - over - wall #4 | 0-19s | above | 0-20s | synonym | 0.95 | ✓ | ✗ |
| adult #14 - hugging - adult #11 | 8-12s | looking at (+2 more) | 0-11s | mismatch | 0.25 | ✗ | ✗ |
| adult #16 - holding - camera #13 | 17.2-19s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (24): adult #11 - holding hands with - adult #14 [0-11s]; adult #11 - moving away from - adult #14 [11-13s]; adult #11 - moving toward - adult #14 [16-19s]; adult #11 - hugging - adult #14 [18-20s]; adult #11 - looking at - adult #14 [0-11s]; adult #11 - next to - adult #14 [0-11s, 16-20s]; adult #11 - on - ground #2 [0-11s, 16-20s]; adult #14 - on - ground #2 [0-11s, 16-20s]; adult #11 - in front of - wall #4 [0-20s]; adult #14 - in front of - wall #4 [0-20s]


## 0028_4021064662

19.0 s, 19 frames read | human: 10 objects, 18 relations | TRASER: 10 objects, 25 relations, valid JSON, 939 tokens

**Objects: 6/10 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | track | semantic overlap | ✓ |
| 2 | grass | soccer field | semantic overlap | ✓ |
| 3 | adult | person | hypernym/hyponym | ✓ |
| 4 | child | child | identical | ✓ |
| 5 | bottle | bottle | identical | ✓ |
| 6 | hat | baseball cap | hypernym/hyponym | ✓ |
| 7 | bag | shoe | mismatch | ✗ |
| 8 | ball | shoe | mismatch | ✗ |
| 9 | adult | arm | mismatch | ✗ |
| 10 | adult | hand | mismatch | ✗ |

**Relations: 5/18 right, triplets: 4/18 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #10 - in front of - adult #3 | 8.4-9s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #3 - looking at - child #4 | 2.2-4.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| bottle #5 - on - grass #2 | 0-19s | on | 0-19s | identical | 1.00 | ✓ | ✓ |
| bottle #5 - in front of - child #4 | 0-19s | near | 0-19s | hypernym/hyponym | 1.00 | ✓ | ✓ |
| bottle #5 - in front of - adult #3 | 0-19s | near | 0-19s | hypernym/hyponym | 1.00 | ✓ | ✓ |
| adult #3 - standing on - grass #2 | 0-19s | on | 0-19s | hypernym/hyponym | 1.00 | ✓ | ✓ |
| child #4 - wearing - hat #6 | 0-19s | nothing for this pair | - | - | - | ✗ | ✗ |
| bag #7 - on - grass #2 | 0-7.8s | on | 0-9s | identical | 0.87 | ✓ | ✗ |
| child #4 - sitting on - grass #2 | 0-1.2s | on | 0-19s | hypernym/hyponym | 0.06 | ✗ | ✗ |
| child #4 - holding - ball #8 | 1.8-3.8s, 11.2-19s | wearing | 0-19s | mismatch | 0.52 | ✗ | ✗ |
| adult #3 - holding - ball #8 | 3.6-9.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #4 - standing on - grass #2 | 2.2-7.2s, 18.2-19s | on | 0-19s | hypernym/hyponym | 0.31 | ✗ | ✗ |
| child #4 - running on - grass #2 | 7-10s, 11.2-12.8s | on | 0-19s | hypernym/hyponym | 0.24 | ✗ | ✗ |
| child #4 - in front of - adult #3 | 7.6-8s | near (+3 more) | 0-19s | hypernym/hyponym | 0.02 | ✗ | ✗ |
| adult #3 - throwing - ball #8 | 9.6-10.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #4 - catching - ball #8 | 9.8-11.4s | wearing | 0-19s | mismatch | 0.08 | ✗ | ✗ |
| child #4 - playing with - adult #3 | 12.6-18.6s | moving away from (+3 more) | 11-19s | mismatch | 0.75 | ✗ | ✗ |
| adult #3 - hugging - child #4 | 12.4-15.2s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (14): adult #3 - wearing - hat #6 [0-19s]; child #4 - approaching - bottle #5 [10-13s]; child #4 - moving away from - bottle #5 [13-19s]; ball #8 - on - grass #2 [0-19s]; ground #1 - in front of - grass #2 [0-19s]; adult #3 - behind - ground #1 [0-19s]; child #4 - behind - ground #1 [0-19s]; bottle #5 - behind - ground #1 [0-19s]; bag #7 - behind - ground #1 [0-9s]; ball #8 - behind - ground #1 [0-19s]


## 0039_6951351121

15.8 s, 16 frames read | human: 17 objects, 13 relations | TRASER: 17 objects, 38 relations, valid JSON, 1565 tokens

**Objects: 12/17 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | sky | cloud | semantic overlap | ✓ |
| 2 | tree | tree | identical | ✓ |
| 3 | grass | field | semantic overlap | ✓ |
| 4 | helmet | helmet | identical | ✓ |
| 5 | adult | person | hypernym/hyponym | ✓ |
| 6 | ball | hand | mismatch | ✗ |
| 7 | helmet | helmet | identical | ✓ |
| 8 | adult | person | hypernym/hyponym | ✓ |
| 9 | ball | person | mismatch | ✗ |
| 10 | helmet | helmet | identical | ✓ |
| 11 | adult | person | hypernym/hyponym | ✓ |
| 12 | ball | ball | identical | ✓ |
| 13 | helmet | jersey | mismatch | ✗ |
| 14 | adult | shorts | mismatch | ✗ |
| 15 | ball | arm | mismatch | ✗ |
| 16 | adult | person | hypernym/hyponym | ✓ |
| 17 | adult | person | hypernym/hyponym | ✓ |

**Relations: 2/13 right, triplets: 2/13 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #17 - walking on - grass #3 | 1.4-4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - in front of - adult #17 | 1.8-3.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #17 - holding - ball #6 | 1.4-3.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #17 - holding - ball #9 | 1.4-3.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - holding - ball #12 | 15.2-15.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - running on - grass #3 | 0-2.2s, 13-14.2s | on | 0-1.975s, 13.825-15.8s | hypernym/hyponym | 0.47 | ✗ | ✗ |
| adult #8 - throwing - ball #12 | 1.6-3.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #16 - running on - grass #3 | 2.4-10.4s, 12.2-14.8s | on | 0-15.8s | hypernym/hyponym | 0.67 | ✓ | ✓ |
| adult #14 - running on - grass #3 | 4.6-5.8s, 12.2-14.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - catching - ball #12 | 5.6-9s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - throwing - ball #12 | 8.8-13s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - throwing - ball #15 | 13.2-13.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #16 - throwing - ball #12 | 13.8-15s | playing with (+2 more) | 13.825-15.8s | semantic overlap | 0.59 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (33): adult #16 - wearing - helmet #7 [0-1.975s, 2.9625-15.8s]; adult #16 - in front of - helmet #7 [0-1.975s, 2.9625-15.8s]; adult #11 - wearing - helmet #10 [7.9-12.8375s]; adult #11 - wearing - helmet #13 [7.9-12.8375s]; adult #11 - wearing - adult #14 [7.9-12.8375s]; adult #16 - approaching - adult #11 [7.9-10.8625s]; adult #16 - moving away from - adult #11 [10.8625-12.8375s]; adult #16 - chasing - adult #11 [7.9-12.8375s]; adult #16 - in front of - adult #11 [7.9-12.8375s]; ball #12 - moving across - grass #3 [13.825-15.8s]


## 0046_11919433184

112.6 s, 113 frames read | human: 16 objects, 17 relations | TRASER: 15 objects, 12 relations, cut-off answer (salvaged), 4300 tokens

**Objects: 12/16 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | dog | mismatch | ✗ |
| 2 | rock | stone wall | semantic overlap | ✓ |
| 3 | grass | lawn | synonym | ✓ |
| 4 | wall | wall | identical | ✓ |
| 5 | door | plant | mismatch | ✗ |
| 6 | window | window | identical | ✓ |
| 7 | fence | fence | identical | ✓ |
| 8 | adult | person | hypernym/hyponym | ✓ |
| 9 | child | child | identical | ✓ |
| 10 | ball | ball | identical | ✓ |
| 11 | window | flower arrangement | mismatch | ✗ |
| 12 | fence | fence | identical | ✓ |
| 13 | ball | soccer ball | hypernym/hyponym | ✓ |
| 14 | window | window blind | semantic overlap | ✓ |
| 15 | window | window blind | semantic overlap | ✓ |
| 16 | window | - | no label from TRASER | ✗ |

**Relations: 1/17 right, triplets: 1/17 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| child #9 - kicking - ball #13 | 77.4-78.8s, 86.6-88s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - standing on - grass #3 | 0-1.6s, 4.4-7.8s | on | 0-110.607s | hypernym/hyponym | 0.05 | ✗ | ✗ |
| child #9 - kicking - ball #10 | 1.6-4.4s, 49.6-54.2s, 61.8-72s, 78-78.8s, 85.2-86s, 100-105.2s | playing with (+4 more) | 0-2.98938s, 3.98584-12.954s, 13.9504-14.9469s, 15.9434-16.9398s, 17.9363-20.9257s, 21.9221-22.9186s, 23.915-24.9115s, 25.908-26.9044s, 27.9009-30.8903s, 31.8867-32.8832s, 33.8796-34.8761s, 35.8726-36.869s, 37.8655-38.8619s, 39.8584-40.8549s, 41.8513-42.8478s, 43.8442-44.8407s, 45.8372-46.8336s, 47.8301-48.8265s, 49.823-50.8195s, 51.8159-52.8124s, 53.8088-54.8053s, 55.8018-56.7982s, 57.7947-58.7912s, 59.7876-60.7841s, 61.7805-62.777s, 63.7735-64.7699s, 65.7664-66.7628s, 67.7593-68.7558s, 69.7522-70.7487s, 71.7451-72.7416s, 73.7381-74.7345s, 75.731-76.7274s, 77.7239-78.7204s, 79.7168-80.7133s, 81.7097-82.7062s, 83.7027-84.6991s, 85.6956-86.692s, 87.6885-88.685s, 89.6814-90.6779s, 91.6743-92.6708s, 93.6673-94.6637s, 95.6602-96.6566s, 97.6531-98.6496s, 99.646-100.642s, 101.639-102.635s, 103.632-104.628s, 105.625-106.621s, 107.618-108.614s, 109.611-110.607s | mismatch | 0.18 | ✗ | ✗ |
| child #9 - toward - ball #10 | 7.8-10s, 21-29.8s, 47.4-49.6s | approaching (+4 more) | 9.9646-11.9575s | synonym | 0.00 | ✗ | ✗ |
| child #9 - picking - ball #10 | 10-11.2s, 93.6-95s | holding (+4 more) | 10.9611-12.954s, 13.9504-14.9469s, 15.9434-16.9398s, 17.9363-20.9257s, 21.9221-22.9186s, 23.915-24.9115s, 25.908-26.9044s, 27.9009-30.8903s, 31.8867-32.8832s, 33.8796-34.8761s, 35.8726-36.869s, 37.8655-38.8619s, 39.8584-40.8549s, 41.8513-42.8478s, 43.8442-44.8407s, 45.8372-46.8336s, 47.8301-48.8265s, 49.823-50.8195s, 51.8159-52.8124s, 53.8088-54.8053s, 55.8018-56.7982s, 57.7947-58.7912s, 59.7876-60.7841s, 61.7805-62.777s, 63.7735-64.7699s, 65.7664-66.7628s, 67.7593-68.7558s, 69.7522-70.7487s, 71.7451-72.7416s, 73.7381-74.7345s, 75.731-76.7274s, 77.7239-78.7204s, 79.7168-80.7133s, 81.7097-82.7062s, 83.7027-84.6991s, 85.6956-86.692s, 87.6885-88.685s, 89.6814-90.6779s, 91.6743-92.6708s, 93.6673-94.6637s, 95.6602-96.6566s, 97.6531-98.6496s, 99.646-100.642s, 101.639-102.635s, 103.632-104.628s, 105.625-106.621s, 107.618-108.614s, 109.611-110.607s | semantic overlap | 0.02 | ✗ | ✗ |
| child #9 - toward - adult #8 | 11.2-14s | playing with | 0-2.98938s, 3.98584-10.9611s | mismatch | 0.00 | ✗ | ✗ |
| adult #8 - standing on - grass #3 | 0-19s | on | 0-47.8301s, 55.8018-64.7699s, 69.7522-70.7487s, 75.731-88.685s, 103.632-108.614s | hypernym/hyponym | 0.25 | ✗ | ✗ |
| adult #8 - picking - ball #10 | 19-20.4s, 41.6-43.6s | holding | 0-2.98938s, 3.98584-10.9611s | semantic overlap | 0.00 | ✗ | ✗ |
| child #9 - next to - adult #8 | 12.8-47.6s, 57.8-64.6s | playing with | 0-2.98938s, 3.98584-10.9611s | mismatch | 0.00 | ✗ | ✗ |
| adult #8 - pulling - child #9 | 60.6-62s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - picking - ball #13 | 73.2-76s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - chasing - ball #13 | 78.8-85s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #9 - holding - ball #10 | 94.8-99.8s | holding (+4 more) | 10.9611-12.954s, 13.9504-14.9469s, 15.9434-16.9398s, 17.9363-20.9257s, 21.9221-22.9186s, 23.915-24.9115s, 25.908-26.9044s, 27.9009-30.8903s, 31.8867-32.8832s, 33.8796-34.8761s, 35.8726-36.869s, 37.8655-38.8619s, 39.8584-40.8549s, 41.8513-42.8478s, 43.8442-44.8407s, 45.8372-46.8336s, 47.8301-48.8265s, 49.823-50.8195s, 51.8159-52.8124s, 53.8088-54.8053s, 55.8018-56.7982s, 57.7947-58.7912s, 59.7876-60.7841s, 61.7805-62.777s, 63.7735-64.7699s, 65.7664-66.7628s, 67.7593-68.7558s, 69.7522-70.7487s, 71.7451-72.7416s, 73.7381-74.7345s, 75.731-76.7274s, 77.7239-78.7204s, 79.7168-80.7133s, 81.7097-82.7062s, 83.7027-84.6991s, 85.6956-86.692s, 87.6885-88.685s, 89.6814-90.6779s, 91.6743-92.6708s, 93.6673-94.6637s, 95.6602-96.6566s, 97.6531-98.6496s, 99.646-100.642s, 101.639-102.635s, 103.632-104.628s, 105.625-106.621s, 107.618-108.614s, 109.611-110.607s | identical | 0.04 | ✗ | ✗ |
| child #9 - running on - grass #3 | 105.2-112.8s | on | 0-110.607s | hypernym/hyponym | 0.05 | ✗ | ✗ |
| child #9 - jumping from - grass #3 | 20.8-33s, 38.6-40.6s, 44.2-45.8s | on | 0-110.607s | mismatch | 0.14 | ✗ | ✗ |
| child #9 - playing with - ball #10 | 0-112.8s | playing with (+4 more) | 0-2.98938s, 3.98584-12.954s, 13.9504-14.9469s, 15.9434-16.9398s, 17.9363-20.9257s, 21.9221-22.9186s, 23.915-24.9115s, 25.908-26.9044s, 27.9009-30.8903s, 31.8867-32.8832s, 33.8796-34.8761s, 35.8726-36.869s, 37.8655-38.8619s, 39.8584-40.8549s, 41.8513-42.8478s, 43.8442-44.8407s, 45.8372-46.8336s, 47.8301-48.8265s, 49.823-50.8195s, 51.8159-52.8124s, 53.8088-54.8053s, 55.8018-56.7982s, 57.7947-58.7912s, 59.7876-60.7841s, 61.7805-62.777s, 63.7735-64.7699s, 65.7664-66.7628s, 67.7593-68.7558s, 69.7522-70.7487s, 71.7451-72.7416s, 73.7381-74.7345s, 75.731-76.7274s, 77.7239-78.7204s, 79.7168-80.7133s, 81.7097-82.7062s, 83.7027-84.6991s, 85.6956-86.692s, 87.6885-88.685s, 89.6814-90.6779s, 91.6743-92.6708s, 93.6673-94.6637s, 95.6602-96.6566s, 97.6531-98.6496s, 99.646-100.642s, 101.639-102.635s, 103.632-104.628s, 105.625-106.621s, 107.618-108.614s, 109.611-110.607s | identical | 0.56 | ✓ | ✓ |
| child #9 - playing with - ball #13 | 77.4-88s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (3): child #9 - in front of - fence #12 [105.625-110.607s]; adult #8 - in front of - fence #12 [105.625-110.607s]; ball #10 - in front of - fence #12 [105.625-110.607s]


## 0051_3702633786

49.0 s, 49 frames read | human: 12 objects, 15 relations | TRASER: 12 objects, 13 relations, valid JSON, 1195 tokens

**Objects: 7/12 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | tree | person | mismatch | ✗ |
| 2 | ground | dog | mismatch | ✗ |
| 3 | rock | bathtub | mismatch | ✗ |
| 4 | water | hand | mismatch | ✗ |
| 5 | adult | person | hypernym/hyponym | ✓ |
| 6 | dog | dog | identical | ✓ |
| 7 | bottle | bowl | semantic overlap | ✓ |
| 8 | adult | person | hypernym/hyponym | ✓ |
| 9 | dog | person | mismatch | ✗ |
| 10 | adult | person | hypernym/hyponym | ✓ |
| 11 | adult | person | hypernym/hyponym | ✓ |
| 12 | adult | person | hypernym/hyponym | ✓ |

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
| dog #6 - jumping over - rock #3 | 38.8-42.8s | inside | 0-4s, 5-22s, 23-34s, 35-37s, 38-42s, 43-44s | mismatch | 0.08 | ✗ | ✗ |
| adult #5 - guiding - dog #6 | 38.2-46.4s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (12): adult #10 - wash - dog #6 [0-4s, 5-22s, 23-34s, 35-37s, 38-42s, 43-44s]; adult #10 - hold - dog #6 [0-4s, 5-22s, 23-34s, 35-37s, 38-42s, 43-44s]; adult #10 - bathe - dog #6 [0-4s, 5-22s, 23-34s, 35-37s, 38-42s, 43-44s]; bottle #7 - inside - rock #3 [0-1s, 3-4s, 5-22s, 23-34s, 35-37s, 38-40s]; water #4 - touching - dog #6 [0-4s, 5-22s, 23-34s, 35-37s, 38-42s, 43-44s]; water #4 - inside - rock #3 [0-4s, 5-22s, 23-34s, 35-37s, 38-42s, 43-44s]; dog #6 - in front of - adult #10 [0-4s, 5-22s, 23-34s, 35-37s, 38-42s, 43-44s]; bottle #7 - in front of - adult #10 [0-1s, 3-4s, 5-22s, 23-34s, 35-37s, 38-40s]; rock #3 - in front of - adult #10 [0-4s, 5-22s, 23-34s, 35-37s, 38-42s, 43-44s]; dog #6 - in front of - adult #8 [0-4s, 5-22s]


## 0053_5599511471

28.4 s, 28 frames read | human: 7 objects, 14 relations | TRASER: 6 objects, 11 relations, valid JSON, 587 tokens

**Objects: 4/7 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | tree | - | no label from TRASER | ✗ |
| 2 | grass | person | mismatch | ✗ |
| 3 | helmet | helmet | identical | ✓ |
| 4 | adult | jersey | mismatch | ✗ |
| 5 | ball | basketball | hypernym/hyponym | ✓ |
| 6 | adult | person | hypernym/hyponym | ✓ |
| 7 | adult | person | hypernym/hyponym | ✓ |

**Relations: 1/14 right, triplets: 1/14 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #7 - wearing - helmet #3 | 3.8-28.4s | wearing | 5.07143-18.2571s, 19.2714-29.4143s | identical | 0.87 | ✓ | ✓ |
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

**Objects: 11/15 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | sky | horse | mismatch | ✗ |
| 2 | tree | tree | identical | ✓ |
| 3 | ground | horse | mismatch | ✗ |
| 4 | adult | person | hypernym/hyponym | ✓ |
| 5 | horse | horse | identical | ✓ |
| 6 | hat | hat | identical | ✓ |
| 7 | adult | person | hypernym/hyponym | ✓ |
| 8 | horse | horse | identical | ✓ |
| 9 | hat | umbrella | mismatch | ✗ |
| 10 | adult | horse | mismatch | ✗ |
| 11 | hat | hat | identical | ✓ |
| 12 | adult | person | hypernym/hyponym | ✓ |
| 13 | adult | person | hypernym/hyponym | ✓ |
| 14 | adult | person | hypernym/hyponym | ✓ |
| 15 | adult | person | hypernym/hyponym | ✓ |

**Relations: 2/17 right, triplets: 2/17 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #4 - wearing - hat #6 | 0-20.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - wearing - hat #9 | 20.6-66.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - riding - horse #5 | 0-8.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - going down - horse #5 | 8-11.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - riding - horse #5 | 0-20.2s | riding | 0-11.0297s, 15.0405-20.0541s | identical | 0.79 | ✓ | ✓ |
| adult #12 - looking at - adult #4 | 9.2-11.6s | riding (+2 more) | 68.1838-74.2s | mismatch | 0.00 | ✗ | ✗ |
| adult #10 - riding - horse #5 | 18.2-74.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - riding - horse #8 | 0-74.2s | riding (+2 more) | 21.0568-40.1081s, 41.1108-60.1622s | identical | 0.51 | ✓ | ✓ |
| adult #13 - riding - horse #8 | 15.4-20.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #13 - going down - horse #8 | 26.2-33.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - looking at - adult #13 | 26.2-33.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - riding - horse #8 | 42.4-74.2s | riding (+2 more) | 21.0568-40.1081s, 41.1108-60.1622s | identical | 0.34 | ✗ | ✗ |
| adult #7 - getting down on - horse #5 | 8-11.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - pulling - adult #13 | 14-18s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - pulling - adult #15 | 26.4-33.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #15 - getting down on - horse #5 | 26.4-33.2s | riding (+2 more) | 68.1838-74.2s | mismatch | 0.00 | ✗ | ✗ |
| adult #14 - pulling - adult #12 | 37.4-43s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (61): adult #15 - riding - horse #8 [21.0568-40.1081s, 41.1108-60.1622s]; adult #15 - riding - horse #8 [21.0568-40.1081s, 41.1108-60.1622s]; adult #15 - riding - horse #8 [21.0568-40.1081s, 41.1108-60.1622s]; adult #12 - riding - ground #3 [30.0811-60.1622s]; adult #12 - riding - ground #3 [30.0811-60.1622s]; adult #12 - riding - ground #3 [30.0811-60.1622s]; adult #14 - riding - ground #3 [30.0811-60.1622s]; adult #14 - riding - ground #3 [30.0811-60.1622s]; adult #14 - riding - ground #3 [30.0811-60.1622s]; adult #15 - riding - ground #3 [30.0811-60.1622s]


## 0057_7001078933

21.2 s, 21 frames read | human: 15 objects, 18 relations | TRASER: 15 objects, 36 relations, valid JSON, 1481 tokens

**Objects: 13/15 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | tree | tree | identical | ✓ |
| 2 | grass | soccer field | semantic overlap | ✓ |
| 3 | helmet | helmet | identical | ✓ |
| 4 | adult | person | hypernym/hyponym | ✓ |
| 5 | hat | beanie | hypernym/hyponym | ✓ |
| 6 | helmet | helmet | identical | ✓ |
| 7 | adult | person | hypernym/hyponym | ✓ |
| 8 | helmet | helmet | identical | ✓ |
| 9 | adult | jacket | mismatch | ✗ |
| 10 | helmet | helmet | identical | ✓ |
| 11 | adult | person | hypernym/hyponym | ✓ |
| 12 | helmet | helmet | identical | ✓ |
| 13 | adult | person | hypernym/hyponym | ✓ |
| 14 | adult | person | hypernym/hyponym | ✓ |
| 15 | adult | jersey | mismatch | ✗ |

**Relations: 4/18 right, triplets: 4/18 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #4 - standing on - grass #2 | 3-10.2s | on (+2 more) | 0-9.08571s, 18.1714-19.181s | hypernym/hyponym | 0.54 | ✓ | ✓ |
| adult #4 - wearing - helmet #3 | 0-21s | wearing | 0-9.08571s | identical | 0.43 | ✗ | ✗ |
| adult #7 - wearing - helmet #6 | 0-19.2s | wearing | 0-20.1905s | identical | 0.95 | ✓ | ✓ |
| adult #9 - wearing - hat #5 | 0-11.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - wearing - helmet #8 | 0-3s | wearing | 0-7.06667s | identical | 0.42 | ✗ | ✗ |
| adult #13 - wearing - helmet #10 | 9.4-17.2s | wearing | 7.06667-16.1524s | identical | 0.67 | ✓ | ✓ |
| adult #15 - wearing - helmet #12 | 17-18.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - standing on - grass #2 | 16-19.2s | on (+2 more) | 16.1524-19.181s | hypernym/hyponym | 0.95 | ✓ | ✓ |
| adult #4 - walking on - grass #2 | 0-3s | moving across (+2 more) | 0-9.08571s | semantic overlap | 0.33 | ✗ | ✗ |
| adult #7 - walking on - grass #2 | 0-3s | moving across (+2 more) | 0-20.1905s | semantic overlap | 0.15 | ✗ | ✗ |
| adult #9 - walking on - grass #2 | 0-3s | above | 0-7.06667s | mismatch | 0.42 | ✗ | ✗ |
| adult #11 - standing on - grass #2 | 0-3s | on (+2 more) | 0-7.06667s, 21.2-22.2095s | hypernym/hyponym | 0.37 | ✗ | ✗ |
| adult #9 - getting down on - grass #2 | 6-7.6s | above | 0-7.06667s | mismatch | 0.14 | ✗ | ✗ |
| adult #7 - pushing - adult #13 | 11.4-13.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - pushing - adult #14 | 14.8-15.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - pushing - adult #15 | 17-17.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - squatting on - grass #2 | 6.2-7.6s | above | 0-7.06667s | hypernym/hyponym | 0.11 | ✗ | ✗ |
| adult #13 - squatting on - grass #2 | 8.8-11.8s | on (+2 more) | 7.06667-16.1524s, 18.1714-19.181s, 21.2-22.2095s | hypernym/hyponym | 0.27 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (16): adult #11 - wearing - adult #9 [0-7.06667s]; adult #14 - wearing - helmet #12 [16.1524-19.181s]; adult #14 - wearing - adult #15 [16.1524-19.181s]; tree #1 - behind - grass #2 [0-11.1048s, 12.1143-13.1238s, 14.1333-15.1429s, 16.1524-17.1619s, 18.1714-19.181s, 20.1905-22.2095s]; adult #7 - in front of - tree #1 [0-11.1048s, 12.1143-13.1238s, 14.1333-15.1429s, 16.1524-17.1619s, 18.1714-19.181s]; adult #4 - in front of - tree #1 [0-9.08571s, 18.1714-19.181s]; adult #11 - in front of - tree #1 [0-7.06667s, 21.2-22.2095s]; adult #13 - in front of - tree #1 [7.06667-11.1048s, 12.1143-13.1238s, 14.1333-15.1429s, 16.1524-17.1619s, 18.1714-19.181s]; adult #14 - in front of - tree #1 [16.1524-17.1619s, 18.1714-19.181s]; helmet #6 - above - adult #7 [0-20.1905s]


## 0062_6430774273

90.0 s, 90 frames read | human: 6 objects, 13 relations | TRASER: 6 objects, 16 relations, valid JSON, 651 tokens

**Objects: 4/6 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | adult | blanket | mismatch | ✗ |
| 2 | child | child | identical | ✓ |
| 3 | baby | baby | identical | ✓ |
| 4 | bed | blanket | semantic overlap | ✓ |
| 5 | sofa | sofa | identical | ✓ |
| 6 | camera | remote control | mismatch | ✗ |

**Relations: 2/13 right, triplets: 2/13 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #1 - touching - child #2 | 1.8-16.8s, 32.4-44.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #1 - touching - baby #3 | 81-83s | nothing for this pair | - | - | - | ✗ | ✗ |
| baby #3 - lying on - bed #4 | 0-90s | on | 0-90s | hypernym/hyponym | 1.00 | ✓ | ✓ |
| child #2 - sitting on - bed #4 | 5-23s, 34-47s, 50-52.2s, 60-76.2s | on | 0-90s | hypernym/hyponym | 0.55 | ✓ | ✓ |
| child #2 - kissing - baby #3 | 24-26.2s, 48-50.2s, 52-56.6s | next to (+5 more) | 0-90s | mismatch | 0.10 | ✗ | ✗ |
| child #2 - caressing - baby #3 | 27-29.8s, 76.8-79.8s | touches (+5 more) | 3-18s | hypernym/hyponym | 0.00 | ✗ | ✗ |
| child #2 - touching - baby #3 | 30.6-32s | next to (+5 more) | 0-90s | semantic overlap | 0.02 | ✗ | ✗ |
| child #2 - lying on - bed #4 | 76.8-79.8s | on | 0-90s | hypernym/hyponym | 0.03 | ✗ | ✗ |
| child #2 - looking at - baby #3 | 84-85.6s | looks at (+5 more) | 27-32s | identical | 0.00 | ✗ | ✗ |
| adult #1 - holding - camera #6 | 28.4-31.2s, 49.6-53s, 58.6-60.4s, 67-69.2s, 78.6-83.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #1 - caressing - child #2 | 50.8-52s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #1 - carrying - child #2 | 3.2-4.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #2 - hugging - baby #3 | 26.8-31s, 76.8-79.2s | touches (+5 more) | 3-18s | semantic overlap | 0.00 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (8): child #2 - holds - camera #6 [79-84s]; child #2 - in front of - sofa #5 [0-90s]; baby #3 - in front of - sofa #5 [0-90s]; bed #4 - in front of - sofa #5 [0-90s]; adult #1 - in front of - sofa #5 [0-20s, 29-62s, 64-73s, 76-84s, 88-90s]; camera #6 - on - bed #4 [79-84s]; camera #6 - in front of - sofa #5 [79-84s]; camera #6 - near - child #2 [79-84s]


## 0069_2740320945

73.6 s, 74 frames read | human: 20 objects, 16 relations | TRASER: 20 objects, 20 relations, valid JSON, 2315 tokens

**Objects: 16/20 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | sky | sky | identical | ✓ |
| 2 | tree | tree | identical | ✓ |
| 3 | ground | stone structure | semantic overlap | ✓ |
| 4 | rock | fountain | mismatch | ✗ |
| 5 | grass | bush | semantic overlap | ✓ |
| 6 | wall | building | semantic overlap | ✓ |
| 7 | water | pool | semantic overlap | ✓ |
| 8 | shoe | shoe | identical | ✓ |
| 9 | dustbin | trash can | synonym | ✓ |
| 10 | adult | person | hypernym/hyponym | ✓ |
| 11 | bottle | bottle | identical | ✓ |
| 12 | hat | umbrella | mismatch | ✗ |
| 13 | camera | hat | mismatch | ✗ |
| 14 | shoe | shoe | identical | ✓ |
| 15 | adult | person | hypernym/hyponym | ✓ |
| 16 | adult | dress | mismatch | ✗ |
| 17 | adult | person | hypernym/hyponym | ✓ |
| 18 | adult | person | hypernym/hyponym | ✓ |
| 19 | adult | person | hypernym/hyponym | ✓ |
| 20 | adult | person | hypernym/hyponym | ✓ |

**Relations: 0/16 right, triplets: 0/16 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #15 - holding - bottle #11 | 35.8-65.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - holding - bottle #11 | 39.6-44.2s, 47-53.8s, 72-73.8s | holding (+1 more) | 19.8919-20.8865s, 21.8811-22.8757s, 23.8703-24.8649s, 25.8595-26.8541s, 27.8486-28.8432s, 29.8378-30.8324s, 31.827-32.8216s, 33.8162-34.8108s, 35.8054-36.8s, 37.7946-38.7892s, 39.7838-40.7784s, 41.773-42.7676s, 43.7622-44.7568s, 45.7514-46.7459s, 47.7405-48.7351s, 49.7297-50.7243s, 51.7189-52.7135s, 53.7081-54.7027s, 55.6973-56.6919s, 57.6865-58.6811s, 59.6757-60.6703s, 61.6649-62.6595s, 63.6541-64.6486s, 65.6432-66.6378s, 67.6324-68.627s, 69.6216-70.6162s, 71.6108-72.6054s | identical | 0.18 | ✗ | ✗ |
| adult #17 - holding - camera #13 | 0-1.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #15 - walking on - water #7 | 0-40.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - kissing - adult #15 | 40-43.6s | dancing with (+2 more) | 15.9135-66.6378s | mismatch | 0.07 | ✗ | ✗ |
| adult #10 - entering - water #7 | 14-31.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - toward - adult #18 | 28.4-37s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - next to - adult #17 | 11-15.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - in front of - adult #15 | 15.6-34.6s | near (+2 more) | 0-66.6378s, 71.6108-73.6s | hypernym/hyponym | 0.28 | ✗ | ✗ |
| adult #10 - holding - adult #15 | 34.4-66.2s, 72-73.8s | dancing with (+2 more) | 15.9135-66.6378s | mismatch | 0.61 | ✗ | ✗ |
| adult #15 - drinking from - bottle #11 | 47-49.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - drinking from - bottle #11 | 50.8-53.4s | holding (+1 more) | 19.8919-20.8865s, 21.8811-22.8757s, 23.8703-24.8649s, 25.8595-26.8541s, 27.8486-28.8432s, 29.8378-30.8324s, 31.827-32.8216s, 33.8162-34.8108s, 35.8054-36.8s, 37.7946-38.7892s, 39.7838-40.7784s, 41.773-42.7676s, 43.7622-44.7568s, 45.7514-46.7459s, 47.7405-48.7351s, 49.7297-50.7243s, 51.7189-52.7135s, 53.7081-54.7027s, 55.6973-56.6919s, 57.6865-58.6811s, 59.6757-60.6703s, 61.6649-62.6595s, 63.6541-64.6486s, 65.6432-66.6378s, 67.6324-68.627s, 69.6216-70.6162s, 71.6108-72.6054s | semantic overlap | 0.03 | ✗ | ✗ |
| adult #16 - next to - adult #15 | 5.6-9s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - next to - adult #18 | 10.8-14.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #17 - in front of - adult #16 | 0-1s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #20 - pulling - adult #19 | 70-70.8s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (15): adult #10 - in front of - rock #4 [0-66.6378s, 71.6108-73.6s]; adult #15 - in front of - rock #4 [0-66.6378s, 71.6108-73.6s]; adult #10 - in front of - wall #6 [0-66.6378s, 71.6108-73.6s]; adult #15 - in front of - wall #6 [0-66.6378s, 71.6108-73.6s]; rock #4 - in front of - wall #6 [0-73.6s]; rock #4 - in front of - tree #2 [0-73.6s]; water #7 - inside - rock #4 [0-73.6s]; water #7 - in front of - wall #6 [0-73.6s]; water #7 - in front of - tree #2 [0-73.6s]; grass #5 - behind - rock #4 [0-73.6s]


## 0075_11566764085

58.8 s, 59 frames read | human: 10 objects, 12 relations | TRASER: 9 objects, 32 relations, valid JSON, 1212 tokens

**Objects: 9/10 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | floorboard | hypernym/hyponym | ✓ |
| 2 | carpet | rug | synonym | ✓ |
| 3 | scissor | scissors | identical | ✓ |
| 4 | adult | person | hypernym/hyponym | ✓ |
| 5 | child | child | identical | ✓ |
| 6 | sofa | chair | semantic overlap | ✓ |
| 7 | chair | chair | identical | ✓ |
| 8 | box | cardboard box | hypernym/hyponym | ✓ |
| 9 | toy | toy car | hypernym/hyponym | ✓ |
| 10 | child | - | no label from TRASER | ✗ |

**Relations: 3/12 right, triplets: 3/12 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #4 - sitting on - sofa #6 | 0-29s, 51-58.8s | touching (+1 more) | 50.8271-59.7966s | semantic overlap | 0.21 | ✗ | ✗ |
| adult #4 - holding - scissor #3 | 0-9s, 9.8-17.8s, 21.2-26.8s | holding | 0-1.99322s, 2.98983-16.9424s, 17.939-27.9051s | identical | 0.75 | ✓ | ✓ |
| adult #4 - opening - box #8 | 0-9s, 9.8-17.8s, 21.2-26.8s | cutting open (+3 more) | 0-27.9051s | semantic overlap | 0.81 | ✓ | ✓ |
| adult #4 - walking on - carpet #2 | 38.4-40.8s | above | 0-27.9051s, 33.8847-43.8508s, 50.8271-59.7966s | mismatch | 0.05 | ✗ | ✗ |
| adult #4 - grabbing - toy #9 | 49.2-51.2s | holding (+3 more) | 29.8983-33.8847s | hypernym/hyponym | 0.00 | ✗ | ✗ |
| adult #4 - holding - toy #9 | 49.8-58.8s | holding (+3 more) | 29.8983-33.8847s | identical | 0.00 | ✗ | ✗ |
| adult #4 - looking at - toy #9 | 49.2-58.8s | holding (+3 more) | 29.8983-33.8847s | mismatch | 0.00 | ✗ | ✗ |
| child #5 - standing on - carpet #2 | 16.4-19.6s, 20.2-24.4s, 34.4-51.4s | above | 0-7.97288s, 17.939-27.9051s, 29.8983-52.8203s | hypernym/hyponym | 0.54 | ✓ | ✓ |
| child #5 - opening - box #8 | 27.2-31.2s | holding (+1 more) | 17.939-27.9051s | mismatch | 0.05 | ✗ | ✗ |
| child #5 - grabbing - toy #9 | 32-42.4s | touching (+1 more) | 29.8983-36.8746s | hypernym/hyponym | 0.39 | ✗ | ✗ |
| child #5 - holding - toy #9 | 42.4-51.2s | holding (+1 more) | 29.8983-33.8847s | identical | 0.00 | ✗ | ✗ |
| child #5 - looking at - toy #9 | 42.2-46.2s | holding (+1 more) | 29.8983-33.8847s | mismatch | 0.00 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (15): toy #9 - moving toward - box #8 [33.8847-36.8746s]; toy #9 - near - box #8 [29.8983-43.8508s]; child #5 - holding - sofa #6 [50.8271-52.8203s]; child #5 - touching - sofa #6 [50.8271-52.8203s]; adult #4 - holding - child #5 [50.8271-52.8203s]; adult #4 - playing with - child #5 [50.8271-59.7966s]; carpet #2 - on - floor #1 [0-35.878s, 41.8576-59.7966s]; box #8 - on - carpet #2 [0-43.8508s]; box #8 - on - floor #1 [0-35.878s]; sofa #6 - on - floor #1 [0-1.99322s, 9.9661-27.9051s, 41.8576-59.7966s]


## 0096_5296138427

19.4 s, 19 frames read | human: 11 objects, 12 relations | TRASER: 10 objects, 20 relations, valid JSON, 880 tokens

**Objects: 10/11 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | - | no label from TRASER | ✗ |
| 2 | floor | floor | identical | ✓ |
| 3 | towel | napkin | synonym | ✓ |
| 4 | adult | person | hypernym/hyponym | ✓ |
| 5 | table | table | identical | ✓ |
| 6 | chair | chair | identical | ✓ |
| 7 | towel | napkin | synonym | ✓ |
| 8 | adult | person | hypernym/hyponym | ✓ |
| 9 | chair | chair | identical | ✓ |
| 10 | adult | person | hypernym/hyponym | ✓ |
| 11 | chair | chair | identical | ✓ |

**Relations: 2/12 right, triplets: 2/12 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #4 - standing on - floor #2 | 0-19.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - pulling - chair #6 | 4.8-6.4s | sitting on (+1 more) | 0-20.4211s | mismatch | 0.08 | ✗ | ✗ |
| adult #4 - pushing - chair #6 | 6.2-14.8s | sitting on (+1 more) | 0-20.4211s | mismatch | 0.42 | ✗ | ✗ |
| adult #4 - holding - towel #7 | 16.8-19.4s | holding | 17.3579-20.4211s | identical | 0.56 | ✓ | ✓ |
| adult #4 - touching - chair #9 | 18.6-19.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - in front of - adult #10 | 0-7.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - holding - towel #3 | 0-3.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - sitting on - chair #6 | 11-19.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| table #5 - beside - chair #6 | 0-19.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| table #5 - beside - chair #9 | 0-19.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| towel #3 - on - table #5 | 3.6-19.4s | on | 0-20.4211s | identical | 0.77 | ✓ | ✓ |
| towel #7 - on - chair #9 | 0-17s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (16): adult #8 - sitting on - chair #9 [0-20.4211s]; adult #8 - on - chair #9 [0-20.4211s]; adult #4 - looking at - adult #8 [0-20.4211s]; adult #4 - next to - adult #8 [0-20.4211s]; adult #8 - looking at - adult #4 [0-20.4211s]; chair #6 - on - floor #2 [0-20.4211s]; chair #9 - on - floor #2 [0-20.4211s]; chair #11 - on - floor #2 [0-20.4211s]; table #5 - on - floor #2 [0-20.4211s]; adult #4 - in front of - table #5 [0-20.4211s]


## 0be30efe-9d71-4698-8304-f1d441aeea58_1

94.0 s, 94 frames read | human: 12 objects, 10 relations | TRASER: 12 objects, 29 relations, valid JSON, 1448 tokens

**Objects: 5/12 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | person | mismatch | ✗ |
| 2 | grass | person | mismatch | ✗ |
| 3 | floor | person | mismatch | ✗ |
| 4 | wall | mat (uncertain) | mismatch | ✗ |
| 5 | brush | tool (uncertain) | hypernym/hyponym | ✓ |
| 6 | stairs | wooden beam | mismatch | ✗ |
| 7 | fence | wooden beam | semantic overlap | ✓ |
| 8 | adult | person | hypernym/hyponym | ✓ |
| 9 | table | person | mismatch | ✗ |
| 10 | chair | chair | identical | ✓ |
| 11 | car | car | identical | ✓ |
| 12 | stairs | bench | mismatch | ✗ |

**Relations: 1/10 right, triplets: 1/10 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #8 - holding - brush #5 | 0-94s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - walking on - grass #2 | 0-11.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - walking on - stairs #6 | 11.6-13s | moving along (+4 more) | 0-17s, 85-95s | semantic overlap | 0.05 | ✗ | ✗ |
| adult #8 - walking on - floor #3 | 13-91s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - touching - fence #7 | 2-9.4s, 14.8-15.6s, 21.6-22.6s, 35.2-36.8s, 51.2-52.8s, 64.4-71s, 79.4-81.4s, 91.4-94s | holding (+4 more) | 0-95s | hypernym/hyponym | 0.25 | ✗ | ✗ |
| adult #8 - carrying - chair #10 | 18.4-19.8s | sanding (+2 more) | 14-54s, 55-67s, 85-95s | mismatch | 0.02 | ✗ | ✗ |
| adult #8 - brushing - fence #7 | 0-1.4s, 3-10.6s, 14.8-17.6s, 23.4-94s | sanding (+4 more) | 0-95s | semantic overlap | 0.87 | ✓ | ✓ |
| adult #8 - pulling - chair #10 | 18.4-19.8s | moving along (+2 more) | 14-54s, 55-67s, 85-95s | semantic overlap | 0.02 | ✗ | ✗ |
| adult #8 - getting down on - stairs #6 | 9-10.6s | holding (+4 more) | 0-17s, 85-95s | mismatch | 0.06 | ✗ | ✗ |
| adult #8 - stepping on - stairs #6 | 2-10.4s | holding (+4 more) | 0-17s, 85-95s | mismatch | 0.31 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (16): adult #8 - sanding - stairs #12 [21-54s, 55-67s, 85-95s]; adult #8 - moving along - stairs #12 [21-54s, 55-67s, 85-95s]; adult #8 - sanding deck - stairs #12 [21-54s, 55-67s, 85-95s]; adult #8 - on - stairs #12 [21-54s, 55-67s, 85-95s]; adult #8 - sanding - car #11 [21-54s, 55-67s, 85-95s]; adult #8 - moving along - car #11 [21-54s, 55-67s, 85-95s]; adult #8 - sanding deck - car #11 [21-54s, 55-67s, 85-95s]; chair #10 - on - stairs #12 [21-54s, 55-67s, 85-95s]; car #11 - on - stairs #12 [21-54s, 55-67s, 85-95s]; chair #10 - next to - car #11 [21-54s, 55-67s, 85-95s]


## 1000_6828150903

68.0 s, 68 frames read | human: 15 objects, 13 relations | TRASER: 15 objects, 38 relations, valid JSON, 1593 tokens

**Objects: 10/15 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | rock | fireplace | mismatch | ✗ |
| 2 | floor | baseboard | semantic overlap | ✓ |
| 3 | ceiling | curtain | mismatch | ✗ |
| 4 | wall | curtain | mismatch | ✗ |
| 5 | door | door frame | semantic overlap | ✓ |
| 6 | shelf | table | semantic overlap | ✓ |
| 7 | window | window | identical | ✓ |
| 8 | adult | person | hypernym/hyponym | ✓ |
| 9 | baby | child | hypernym/hyponym | ✓ |
| 10 | dog | plush toy | mismatch | ✗ |
| 11 | toy | toy | identical | ✓ |
| 12 | door | door | identical | ✓ |
| 13 | door | curtain | mismatch | ✗ |
| 14 | door | window | semantic overlap | ✓ |
| 15 | door | door | identical | ✓ |

**Relations: 4/13 right, triplets: 3/13 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #8 - beside - door #5 | 0-5.2s | in front of | 0-9s | mismatch | 0.58 | ✗ | ✗ |
| adult #8 - holding - baby #9 | 0-68s | holding (+4 more) | 0-69s | identical | 0.99 | ✓ | ✓ |
| adult #8 - hugging - baby #9 | 0-68s | holding (+4 more) | 0-69s | semantic overlap | 0.99 | ✓ | ✓ |
| adult #8 - walking on - floor #2 | 0-16.8s | above | 10-14s, 50-69s | mismatch | 0.11 | ✗ | ✗ |
| adult #8 - beside - door #12 | 5.2-9.6s | in front of | 0-12s | mismatch | 0.37 | ✗ | ✗ |
| adult #8 - beside - door #14 | 10.2-11.6s | in front of | 10-14s | mismatch | 0.35 | ✗ | ✗ |
| adult #8 - beside - window #7 | 11.6-13.6s | in front of | 10-14s | mismatch | 0.50 | ✗ | ✗ |
| adult #8 - in front of - rock #1 | 16.4-68s | in front of | 16-69s | identical | 0.97 | ✓ | ✗ |
| adult #8 - beside - wall #4 | 16.4-68s | in front of | 0-69s | mismatch | 0.75 | ✗ | ✗ |
| adult #8 - grabbing - toy #11 | 16.8-18s | holding (+1 more) | 16-69s | hypernym/hyponym | 0.02 | ✗ | ✗ |
| adult #8 - holding - toy #11 | 18-45.6s | holding (+1 more) | 16-69s | identical | 0.52 | ✓ | ✓ |
| dog #10 - jumping over - floor #2 | 19-21.4s | above | 19-24s | semantic overlap | 0.48 | ✗ | ✗ |
| baby #9 - holding - toy #11 | 45.6-68s | looking at (+1 more) | 16-69s | mismatch | 0.42 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (21): baby #9 - in front of - wall #4 [0-69s]; baby #9 - in front of - rock #1 [16-69s]; adult #8 - in front of - door #15 [16-69s]; baby #9 - in front of - door #15 [16-69s]; baby #9 - in front of - door #14 [10-14s]; baby #9 - in front of - window #7 [10-14s]; adult #8 - in front of - shelf #6 [12-14s]; baby #9 - in front of - shelf #6 [12-14s]; baby #9 - in front of - door #12 [0-12s]; baby #9 - in front of - door #5 [0-9s]


## 1001_7007447516

83.6 s, 84 frames read | human: 22 objects, 9 relations | TRASER: 21 objects, 53 relations, valid JSON, 2252 tokens

**Objects: 17/22 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | sky | tree | mismatch | ✗ |
| 2 | tree | tree | identical | ✓ |
| 3 | ground | bicycle | mismatch | ✗ |
| 4 | grass | grass | identical | ✓ |
| 5 | wall | fence | semantic overlap | ✓ |
| 6 | dustbin | umbrella | mismatch | ✗ |
| 7 | helmet | helmet | identical | ✓ |
| 8 | fence | gate | semantic overlap | ✓ |
| 9 | adult | person | hypernym/hyponym | ✓ |
| 10 | child | child | identical | ✓ |
| 11 | dog | dog | identical | ✓ |
| 12 | bike | bicycle | synonym | ✓ |
| 13 | car | car | identical | ✓ |
| 14 | helmet | helmet | identical | ✓ |
| 15 | adult | person | hypernym/hyponym | ✓ |
| 16 | car | car | identical | ✓ |
| 17 | adult | person | hypernym/hyponym | ✓ |
| 18 | car | - | no label from TRASER | ✗ |
| 19 | adult | person | hypernym/hyponym | ✓ |
| 20 | car | car | identical | ✓ |
| 21 | adult | person | hypernym/hyponym | ✓ |
| 22 | car | pole | mismatch | ✗ |

**Relations: 2/9 right, triplets: 2/9 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #21 - walking on - ground #3 | 40-70.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #10 - riding - bike #12 | 0-83.4s | riding (+1 more) | 0-76.6333s | identical | 0.92 | ✓ | ✓ |
| adult #9 - looking at - child #10 | 0-75.2s | holding (+4 more) | 0-76.6333s | mismatch | 0.98 | ✗ | ✗ |
| adult #9 - holding - child #10 | 0-15.4s, 42.8-44.6s, 54.6-63s | holding (+4 more) | 0-76.6333s | identical | 0.33 | ✗ | ✗ |
| adult #9 - running on - ground #3 | 15.2-42.8s, 63-72.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #15 - looking at - child #10 | 19.2-25.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #10 - walking on - ground #3 | 72.8-83.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - talking to - child #10 | 72.8-75s | holding (+4 more) | 0-76.6333s | mismatch | 0.03 | ✗ | ✗ |
| adult #9 - guiding - child #10 | 0-71.4s | holding (+4 more) | 0-76.6333s | semantic overlap | 0.93 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (46): adult #9 - wearing - helmet #7 [0-76.6333s]; child #10 - wearing - helmet #7 [0-76.6333s]; adult #9 - riding - bike #12 [0-76.6333s]; adult #9 - on - bike #12 [0-76.6333s]; child #10 - moving with - adult #9 [0-76.6333s]; adult #9 - approaching - fence #8 [19.9048-25.8762s]; adult #9 - passing - fence #8 [23.8857-25.8762s]; adult #9 - moving away from - fence #8 [24.881-26.8714s]; adult #9 - in front of - fence #8 [19.9048-26.8714s, 72.6524-76.6333s]; child #10 - approaching - fence #8 [19.9048-25.8762s]


## 1002_5280626374

35.2 s, 35 frames read | human: 13 objects, 12 relations | TRASER: 13 objects, 28 relations, valid JSON, 1193 tokens

**Objects: 9/13 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | fabric (uncertain) | mismatch | ✗ |
| 2 | book | hand | mismatch | ✗ |
| 3 | glasses | sunglasses | hypernym/hyponym | ✓ |
| 4 | microphone | microphone | identical | ✓ |
| 5 | adult | person | hypernym/hyponym | ✓ |
| 6 | child | child | identical | ✓ |
| 7 | table | tablecloth | semantic overlap | ✓ |
| 8 | toy | paper (uncertain) | mismatch | ✗ |
| 9 | adult | person | hypernym/hyponym | ✓ |
| 10 | toy | balloon | semantic overlap | ✓ |
| 11 | adult | person | hypernym/hyponym | ✓ |
| 12 | adult | dress | mismatch | ✗ |
| 13 | adult | person | hypernym/hyponym | ✓ |

**Relations: 2/12 right, triplets: 2/12 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #5 - standing on - ground #1 | 0-35.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - holding - glasses #3 | 1.4-18.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - book #2 | 20.4-35.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - next to - adult #9 | 0-35.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - next to - child #6 | 0-35.2s | looking at | 0-15.0857s | mismatch | 0.43 | ✗ | ✗ |
| child #6 - standing on - table #7 | 0-35.2s | on | 0-35.2s | hypernym/hyponym | 1.00 | ✓ | ✓ |
| child #6 - in - toy #8 | 4.4-35.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #6 - holding - microphone #4 | 13-35.2s | holding (+2 more) | 15.0857-35.2s | identical | 0.91 | ✓ | ✓ |
| child #6 - wearing - glasses #3 | 19.4-35.2s | wearing | 0-35.2s | identical | 0.45 | ✗ | ✗ |
| adult #9 - talking to - child #6 | 24-26.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - talking to - child #6 | 26.4-35.2s | looking at | 0-15.0857s | semantic overlap | 0.00 | ✗ | ✗ |
| child #6 - talking to - adult #5 | 19.4-35.2s | looking at (+4 more) | 0-15.0857s | semantic overlap | 0.00 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (17): adult #5 - on - table #7 [0-35.2s]; adult #9 - on - table #7 [0-35.2s]; microphone #4 - above - table #7 [0-35.2s]; glasses #3 - on - child #6 [0-35.2s]; child #6 - in front of - adult #9 [0-35.2s]; microphone #4 - in front of - child #6 [0-35.2s]; microphone #4 - in front of - adult #5 [0-35.2s]; microphone #4 - in front of - adult #9 [0-35.2s]; child #6 - in front of - adult #13 [3.01714-22.1257s, 29.1657-35.2s]; adult #5 - in front of - adult #13 [3.01714-22.1257s, 29.1657-35.2s]


## 1005_4760962392

90.0 s, 90 frames read | human: 17 objects, 20 relations | TRASER: 17 objects, 14 relations, valid JSON, 1109 tokens

**Objects: 13/17 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | fabric | mismatch | ✗ |
| 2 | wall | wall | identical | ✓ |
| 3 | spoon | candle | mismatch | ✗ |
| 4 | adult | person | hypernym/hyponym | ✓ |
| 5 | child | girl | hypernym/hyponym | ✓ |
| 6 | table | tablecloth | semantic overlap | ✓ |
| 7 | knife | knife | identical | ✓ |
| 8 | candle | candle | identical | ✓ |
| 9 | plate | napkin | mismatch | ✗ |
| 10 | cake | cake | identical | ✓ |
| 11 | adult | person | hypernym/hyponym | ✓ |
| 12 | child | child | identical | ✓ |
| 13 | knife | bowl | mismatch | ✗ |
| 14 | candle | candle | identical | ✓ |
| 15 | plate | plate | identical | ✓ |
| 16 | adult | person | hypernym/hyponym | ✓ |
| 17 | child | child | identical | ✓ |

**Relations: 0/20 right, triplets: 0/20 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| child #17 - blowing - candle #8 | 5.4-9.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #17 - holding - plate #9 | 39.6-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - holding - plate #15 | 84.6-90s | serving | 84-90s | mismatch | 0.90 | ✗ | ✗ |
| adult #4 - holding - spoon #3 | 86.6-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - holding - child #17 | 0-5.2s | serving | 66-72s | mismatch | 0.00 | ✗ | ✗ |
| adult #4 - looking at - cake #10 | 5-8.2s | cutting (+1 more) | 0-17s, 41-46s | mismatch | 0.15 | ✗ | ✗ |
| adult #4 - holding - knife #7 | 11.6-22.6s | holding | 0-17s, 41-46s | identical | 0.20 | ✗ | ✗ |
| adult #4 - holding - knife #13 | 34-80.2s | holding | 28-38s | identical | 0.08 | ✗ | ✗ |
| adult #4 - cutting - cake #10 | 36-75.2s | preparing cake (+1 more) | 0-90s | semantic overlap | 0.44 | ✗ | ✗ |
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

**Objects: 3/9 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | dog | mismatch | ✗ |
| 2 | wall | curtain | mismatch | ✗ |
| 3 | shelf | suitcase | mismatch | ✗ |
| 4 | adult | person | hypernym/hyponym | ✓ |
| 5 | dog | dog | identical | ✓ |
| 6 | chair | chair | identical | ✓ |
| 7 | toy | handbag (uncertain) | mismatch | ✗ |
| 8 | adult | shoe (uncertain) | mismatch | ✗ |
| 9 | dog | - | no label from TRASER | ✗ |

**Relations: 2/7 right, triplets: 1/7 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| shelf #3 - in front of - wall #2 | 0-90s | in front of | 16-45s, 62-90s | identical | 0.63 | ✓ | ✗ |
| adult #4 - standing on - floor #1 | 0-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #5 - biting - toy #7 | 0-24.2s, 43.6-62.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #5 - playing with - toy #7 | 0-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - holding - toy #7 | 24-33.4s, 62.2-80.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - throwing - toy #7 | 32.8-33.4s, 79.6-80.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - in front of - chair #6 | 0-90s | in front of (+1 more) | 0-45s, 59-90s | identical | 0.84 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (16): adult #4 - petting - dog #5 [0-2s, 3-11s, 12-15s, 16-22s, 23-34s, 35-45s, 59-62s, 63-78s, 79-82s, 83-84s]; adult #4 - holding - dog #5 [15-16s, 22-23s, 45-46s, 47-48s, 52-53s, 54-55s, 56-57s, 58-59s, 62-63s, 64-65s, 66-67s, 68-69s, 70-71s, 72-73s, 74-75s, 76-77s, 78-79s, 80-81s, 82-83s]; adult #4 - playing with - dog #5 [0-2s, 3-11s, 12-15s, 16-22s, 23-34s, 35-45s, 59-62s, 63-78s, 79-82s, 83-84s]; dog #5 - approaching - chair #6 [22-25s]; dog #5 - moving away from - chair #6 [25-34s]; dog #5 - in front of - chair #6 [0-45s, 59-90s]; dog #5 - near - chair #6 [0-45s, 59-90s]; dog #5 - in front of - shelf #3 [0-45s, 59-90s]; dog #5 - near - shelf #3 [0-45s, 59-90s]; adult #4 - in front of - shelf #3 [0-45s, 59-90s]


## 1005_7401573420

85.0 s, 85 frames read | human: 20 objects, 23 relations | TRASER: 19 objects, 43 relations, valid JSON, 1915 tokens

**Objects: 14/20 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | floor | identical | ✓ |
| 2 | wall | wall | identical | ✓ |
| 3 | door | radiator | mismatch | ✗ |
| 4 | cabinet | dresser | semantic overlap | ✓ |
| 5 | window | - | no label from TRASER | ✗ |
| 6 | adult | person | hypernym/hyponym | ✓ |
| 7 | child | baby | hypernym/hyponym | ✓ |
| 8 | cat | cat | identical | ✓ |
| 9 | sofa | sofa | identical | ✓ |
| 10 | table | suitcase | mismatch | ✗ |
| 11 | chair | chair | identical | ✓ |
| 12 | bag | chair | mismatch | ✗ |
| 13 | toy | toy | identical | ✓ |
| 14 | ball | ball | identical | ✓ |
| 15 | door | door | identical | ✓ |
| 16 | table | book | mismatch | ✗ |
| 17 | chair | chair leg | semantic overlap | ✓ |
| 18 | toy | toy | identical | ✓ |
| 19 | chair | arm | mismatch | ✗ |
| 20 | chair | chair | identical | ✓ |

**Relations: 4/23 right, triplets: 4/23 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| child #7 - running on - floor #1 | 0-17.2s | on | 0-85s | hypernym/hyponym | 0.20 | ✗ | ✗ |
| adult #6 - sitting on - floor #1 | 0-85s | on | 10-85s | hypernym/hyponym | 0.88 | ✓ | ✓ |
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
| cat #8 - sitting on - floor #1 | 3.8-5.2s, 48.8-51.4s | on | 0-85s | hypernym/hyponym | 0.05 | ✗ | ✗ |
| cat #8 - standing on - floor #1 | 14.6-17.4s, 22.6-30.2s, 39.2-44s | on | 0-85s | hypernym/hyponym | 0.18 | ✗ | ✗ |
| cat #8 - lying on - floor #1 | 76.6-84.2s | on | 0-85s | hypernym/hyponym | 0.09 | ✗ | ✗ |
| adult #6 - playing with - cat #8 | 17-84.2s | playing with (+2 more) | 64-85s | identical | 0.30 | ✗ | ✗ |
| child #7 - playing with - cat #8 | 14.6-85s | near | 0-85s | mismatch | 0.83 | ✗ | ✗ |
| child #7 - looking at - cat #8 | 14.6-85s | near | 0-85s | mismatch | 0.83 | ✗ | ✗ |
| child #7 - next to - adult #6 | 14.6-85s | in front of (+3 more) | 10-85s | mismatch | 0.94 | ✗ | ✗ |
| child #7 - in front of - adult #6 | 14.6-85s | in front of (+3 more) | 10-85s | identical | 0.94 | ✓ | ✓ |
| child #7 - next to - cat #8 | 14.6-85s | near | 0-85s | hypernym/hyponym | 0.83 | ✓ | ✓ |
| child #7 - squatting on - floor #1 | 17.6-20.2s, 24.4-26.6s | on | 0-85s | hypernym/hyponym | 0.06 | ✗ | ✗ |
| child #7 - walking on - floor #1 | 45.4-49.6s, 76.6-79s | on | 0-85s | hypernym/hyponym | 0.08 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (27): adult #6 - holding - child #7 [16-57s]; adult #6 - lifting - child #7 [16-21s]; adult #6 - hugging - child #7 [21-57s]; adult #6 - playing with - child #7 [16-57s]; adult #6 - looking at - child #7 [16-57s]; adult #6 - helping up - child #7 [16-21s]; adult #6 - playing with baby - child #7 [16-57s]; cat #8 - approaching - adult #6 [64-68s]; cat #8 - in front of - adult #6 [10-85s]; adult #6 - playing with - toy #18 [10-13s]


## 1006_4580824633

40.6 s, 41 frames read | human: 5 objects, 8 relations | TRASER: 5 objects, 9 relations, valid JSON, 462 tokens

**Objects: 3/5 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | tree | tree | identical | ✓ |
| 2 | grass | dog | mismatch | ✗ |
| 3 | adult | person | hypernym/hyponym | ✓ |
| 4 | dog | dog | identical | ✓ |
| 5 | adult | dog | mismatch | ✗ |

**Relations: 1/8 right, triplets: 1/8 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| dog #4 - running on - grass #2 | 0-29.6s, 38.6-40.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #3 - running on - grass #2 | 0-7.2s, 9.8-28.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #2 - in front of - tree #1 | 0-11.4s, 13.4-26.4s, 31.8-38.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #4 - chasing - adult #3 | 0.8-12.2s, 21.6-28.8s | near | 6.93171-10.8927s, 12.8732-39.6098s | mismatch | 0.29 | ✗ | ✗ |
| adult #3 - chasing - dog #4 | 13.4-20.2s | playing with (+2 more) | 26.7366-39.6098s | semantic overlap | 0.00 | ✗ | ✗ |
| adult #3 - standing on - grass #2 | 11.8-13.6s, 29.6-40.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #3 - holding - dog #4 | 29.6-38.4s | holding (+2 more) | 30.6976-39.6098s | identical | 0.77 | ✓ | ✓ |
| adult #3 - kissing - dog #4 | 32.4-36.2s | holding (+2 more) | 30.6976-39.6098s | mismatch | 0.43 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (5): adult #3 - in front of - tree #1 [0-10.8927s, 12.8732-26.7366s, 33.6683-39.6098s]; dog #4 - in front of - tree #1 [6.93171-10.8927s, 12.8732-26.7366s, 33.6683-39.6098s]; adult #5 - in front of - tree #1 [12.8732-14.8537s]; adult #5 - in front of - adult #3 [12.8732-14.8537s]; adult #5 - in front of - dog #4 [12.8732-14.8537s]


## 1007_6631583821

28.8 s, 29 frames read | human: 10 objects, 12 relations | TRASER: 10 objects, 31 relations, valid JSON, 1012 tokens

**Objects: 8/10 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | surface | synonym | ✓ |
| 2 | wall | garage door | mismatch | ✗ |
| 3 | fence | railing | synonym | ✓ |
| 4 | adult | person | hypernym/hyponym | ✓ |
| 5 | child | person | hypernym/hyponym | ✓ |
| 6 | baby | child | hypernym/hyponym | ✓ |
| 7 | ball | ball | identical | ✓ |
| 8 | car | car | identical | ✓ |
| 9 | child | person | hypernym/hyponym | ✓ |
| 10 | child | shoe | mismatch | ✗ |

**Relations: 5/12 right, triplets: 5/12 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| child #5 - standing on - ground #1 | 0-28.8s | on | 0-28.8s | hypernym/hyponym | 1.00 | ✓ | ✓ |
| adult #4 - standing on - ground #1 | 0-28.8s | on | 0-28.8s | hypernym/hyponym | 1.00 | ✓ | ✓ |
| baby #6 - sitting on - ground #1 | 0-28.8s | on | 0-28.8s | hypernym/hyponym | 1.00 | ✓ | ✓ |
| child #9 - standing on - ground #1 | 0-28.8s | on | 0-28.8s | hypernym/hyponym | 1.00 | ✓ | ✓ |
| adult #4 - catching - ball #7 | 0.8-2.4s, 7.2-7.6s, 14.2-17s, 24.6-26.2s | looking at | 0-28.8s | mismatch | 0.22 | ✗ | ✗ |
| adult #4 - throwing - ball #7 | 2.4-3.6s, 8.6-10.2s, 17-18.6s, 26.2-27.2s | looking at | 0-28.8s | mismatch | 0.19 | ✗ | ✗ |
| child #5 - throwing - ball #7 | 0-1s, 4.8-7.2s, 11-14.2s, 19.4-23.6s | holding (+1 more) | 0-28.8s | mismatch | 0.38 | ✗ | ✗ |
| child #5 - catching - ball #7 | 3.6-4.8s, 10.2-11s, 18.6-19.6s, 27.2-28.2s | holding (+1 more) | 0-28.8s | semantic overlap | 0.14 | ✗ | ✗ |
| adult #4 - holding - ball #7 | 7.4-9s | looking at | 0-28.8s | mismatch | 0.06 | ✗ | ✗ |
| child #5 - holding - ball #7 | 10.4-13.2s, 28-28.8s | holding (+1 more) | 0-28.8s | identical | 0.12 | ✗ | ✗ |
| child #5 - playing with - ball #7 | 0-28.8s | holding (+1 more) | 0-28.8s | semantic overlap | 1.00 | ✓ | ✓ |
| adult #4 - playing with - ball #7 | 0-28.8s | looking at | 0-28.8s | mismatch | 1.00 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (24): adult #4 - wearing - child #10 [0-28.8s]; ball #7 - moving toward - adult #4 [15.8897-18.869s]; ball #7 - moving away from - adult #4 [18.869-28.8s]; child #10 - on - ground #1 [0-28.8s]; ball #7 - above - ground #1 [0-28.8s]; adult #4 - in front of - wall #2 [0-28.8s]; child #5 - in front of - wall #2 [0-28.8s]; baby #6 - in front of - wall #2 [0-28.8s]; child #9 - in front of - wall #2 [0-28.8s]; child #10 - in front of - wall #2 [0-28.8s]


## 1011_4633647136

53.6 s, 54 frames read | human: 14 objects, 20 relations | TRASER: 14 objects, 356 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 12/14 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | floor | synonym | ✓ |
| 2 | wall | painting | mismatch | ✗ |
| 3 | door | door | identical | ✓ |
| 4 | adult | person | hypernym/hyponym | ✓ |
| 5 | child | child | identical | ✓ |
| 6 | table | tablecloth | semantic overlap | ✓ |
| 7 | chair | chair | identical | ✓ |
| 8 | candle | bow | mismatch | ✗ |
| 9 | cake | cake | identical | ✓ |
| 10 | adult | person | hypernym/hyponym | ✓ |
| 11 | chair | chair | identical | ✓ |
| 12 | adult | person | hypernym/hyponym | ✓ |
| 13 | chair | chair | identical | ✓ |
| 14 | chair | chair | identical | ✓ |

**Relations: 0/20 right, triplets: 0/20 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #10 - walking on - ground #1 | 8.6-9.8s, 45-49.4s | moving away from (+11 more) | 44.6667-50.6222s | mismatch | 0.61 | ✗ | ✗ |
| adult #4 - holding - child #5 | 30.6-53.6s | holding (+1 more) | 0-53.6s | identical | 0.43 | ✗ | ✗ |
| adult #4 - beside - table #6 | 0-53.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - beside - table #6 | 0-53.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #5 - beside - table #6 | 0-53.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #5 - sitting on - chair #7 | 0-28.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #5 - standing on - chair #7 | 30-53.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| cake #9 - on - table #6 | 0-53.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| candle #8 - on - cake #9 | 0-40.6s, 47.4-53.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - beside - table #6 | 6.2-49.2s | approaching (+5 more) | 5.95556-10.9185s | mismatch | 0.11 | ✗ | ✗ |
| adult #10 - beside - adult #4 | 8.4-45.8s | approaching (+9 more) | 5.95556-10.9185s | mismatch | 0.06 | ✗ | ✗ |
| adult #10 - holding - chair #11 | 7.6-29.4s | approaching (+15 more) | 5.95556-10.9185s | mismatch | 0.14 | ✗ | ✗ |
| adult #4 - picking - child #5 | 27.8-30.2s | holding (+1 more) | 0-53.6s | semantic overlap | 0.04 | ✗ | ✗ |
| adult #10 - touching - cake #9 | 30.6-33.8s | approaching (+5 more) | 5.95556-10.9185s | mismatch | 0.00 | ✗ | ✗ |
| adult #12 - touching - cake #9 | 30-33.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - holding - candle #8 | 40.2-48.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - blowing - candle #8 | 42.4-43.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - lighting - candle #8 | 0-4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - carrying - candle #8 | 40.2-42.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - guiding - child #5 | 42.4-44.4s | holding (+1 more) | 0-53.6s | semantic overlap | 0.04 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (85): adult #12 - holding - child #5 [0-53.6s]; adult #12 - looking at - child #5 [0-53.6s]; child #5 - looking at - cake #9 [0-53.6s]; adult #10 - approaching - child #5 [5.95556-10.9185s]; adult #10 - moving away from - child #5 [44.6667-50.6222s]; adult #10 - approaching - child #5 [5.95556-10.9185s]; adult #10 - moving away from - child #5 [44.6667-50.6222s]; adult #10 - approaching - child #5 [5.95556-10.9185s]; adult #10 - moving away from - child #5 [44.6667-50.6222s]; adult #10 - approaching - child #5 [5.95556-10.9185s]


## 1012_4024008346

19.6 s, 20 frames read | human: 11 objects, 8 relations | TRASER: 11 objects, 31 relations, valid JSON, 1209 tokens

**Objects: 10/11 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | floor | identical | ✓ |
| 2 | wall | wall | identical | ✓ |
| 3 | carpet | doormat | hypernym/hyponym | ✓ |
| 4 | fence | gate | semantic overlap | ✓ |
| 5 | adult | child | hypernym/hyponym | ✓ |
| 6 | child | child | identical | ✓ |
| 7 | sofa | sofa | identical | ✓ |
| 8 | ballon | balloon | identical | ✓ |
| 9 | carpet | baseboard | semantic overlap | ✓ |
| 10 | adult | person | hypernym/hyponym | ✓ |
| 11 | ballon | ball | mismatch | ✗ |

**Relations: 5/8 right, triplets: 4/8 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #10 - sitting on - sofa #7 | 0-19.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #6 - holding - ballon #8 | 0-19.6s | holding (+2 more) | 0-19.6s | identical | 1.00 | ✓ | ✓ |
| child #6 - on - floor #1 | 0-19.6s | on | 0-19.6s | identical | 1.00 | ✓ | ✓ |
| adult #5 - on - floor #1 | 0-19.6s | on | 0-8.82s, 11.76-16.66s | identical | 0.70 | ✓ | ✓ |
| ballon #11 - on - floor #1 | 0-19.6s | on | 0-16.66s | identical | 0.85 | ✓ | ✗ |
| child #6 - playing with - ballon #11 | 0-0.8s, 6-13s | approaching (+1 more) | 9.8-12.74s | mismatch | 0.38 | ✗ | ✗ |
| adult #5 - playing with - ballon #11 | 4.4-5s, 13.4-16s | nothing for this pair | - | - | - | ✗ | ✗ |
| sofa #7 - on - floor #1 | 0-19.6s | on | 0-12.74s, 15.68-19.6s | identical | 0.85 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (22): child #6 - moving away from - sofa #7 [9.8-12.74s]; child #6 - approaching - sofa #7 [15.68-19.6s]; child #6 - in front of - sofa #7 [0-12.74s, 15.68-19.6s]; carpet #3 - on - floor #1 [0-19.6s]; fence #4 - on - floor #1 [0-19.6s]; ballon #8 - above - floor #1 [0-19.6s]; fence #4 - in front of - wall #2 [0-19.6s]; sofa #7 - in front of - wall #2 [0-12.74s, 15.68-19.6s]; child #6 - in front of - fence #4 [0-19.6s]; ballon #11 - in front of - fence #4 [0-16.66s]


## 1015_4698622422

42.0 s, 42 frames read | human: 13 objects, 15 relations | TRASER: 13 objects, 18 relations, valid JSON, 1089 tokens

**Objects: 10/13 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | tree | pole | mismatch | ✗ |
| 2 | grass | tennis ball | mismatch | ✗ |
| 3 | adult | person | hypernym/hyponym | ✓ |
| 4 | child | child | identical | ✓ |
| 5 | table | bench | semantic overlap | ✓ |
| 6 | hat | hand | mismatch | ✗ |
| 7 | bat | tennis racket | semantic overlap | ✓ |
| 8 | ball | soccer ball | hypernym/hyponym | ✓ |
| 9 | car | car | identical | ✓ |
| 10 | adult | person | hypernym/hyponym | ✓ |
| 11 | child | person | hypernym/hyponym | ✓ |
| 12 | car | car | identical | ✓ |
| 13 | car | car | identical | ✓ |

**Relations: 3/15 right, triplets: 3/15 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #10 - holding - hat #6 | 40-41.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| ball #8 - on - grass #2 | 0-41.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #4 - on - grass #2 | 0-41.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #4 - holding - bat #7 | 0-36.2s | holding (+1 more) | 0-17s, 18-36s | identical | 0.97 | ✓ | ✓ |
| child #4 - walking on - grass #2 | 0-10.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #4 - hitting - ball #8 | 10.4-12.6s, 20.6-21.8s, 23.6-24.6s, 26.6-27.6s, 29-29.8s, 33.4-34.4s | hitting (+4 more) | 10-13s, 24-26s, 31-33s | identical | 0.25 | ✗ | ✗ |
| child #4 - throwing - bat #7 | 36-36.6s | holding (+1 more) | 0-17s, 18-36s | mismatch | 0.00 | ✗ | ✗ |
| child #4 - chasing - ball #8 | 12.6-39.2s | playing with (+4 more) | 0-17s, 18-42s | semantic overlap | 0.61 | ✓ | ✓ |
| child #4 - kicking - ball #8 | 36.2-39.2s | playing with (+4 more) | 0-17s, 18-42s | mismatch | 0.07 | ✗ | ✗ |
| adult #3 - standing on - grass #2 | 18.8-19.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - standing on - grass #2 | 40-41.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - pulling - child #4 | 40.6-41.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #11 - in front of - adult #3 | 19-19.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #4 - playing with - ball #8 | 6.6-40.2s | playing with (+4 more) | 0-17s, 18-42s | identical | 0.78 | ✓ | ✓ |
| child #4 - squatting on - grass #2 | 19-41.8s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (11): child #4 - in front of - car #9 [0-15s]; child #4 - in front of - car #12 [4-15s]; child #4 - in front of - car #13 [6-15s]; child #4 - in front of - table #5 [12-15s]; child #4 - in front of - tree #1 [0-15s, 20-22s, 29-38s]; bat #7 - in front of - child #4 [0-17s, 18-36s]; ball #8 - in front of - child #4 [0-17s, 18-42s]; bat #7 - above - ball #8 [0-17s, 18-36s]; child #4 - in front of - adult #10 [41-42s]; child #4 - in front of - adult #3 [17-18s]


## 1017_3056841458

80.6 s, 81 frames read | human: 14 objects, 16 relations | TRASER: 14 objects, 37 relations, valid JSON, 1408 tokens

**Objects: 11/14 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | chair leg | mismatch | ✗ |
| 2 | wall | curtain | mismatch | ✗ |
| 3 | door | window | semantic overlap | ✓ |
| 4 | curtain | curtain | identical | ✓ |
| 5 | shelf | cabinet | semantic overlap | ✓ |
| 6 | towel | cup | mismatch | ✗ |
| 7 | adult | person | hypernym/hyponym | ✓ |
| 8 | child | child | identical | ✓ |
| 9 | table | table | identical | ✓ |
| 10 | chair | chair | identical | ✓ |
| 11 | hat | party hat | hypernym/hyponym | ✓ |
| 12 | cake | cupcake | hypernym/hyponym | ✓ |
| 13 | adult | person | hypernym/hyponym | ✓ |
| 14 | cake | cupcake | hypernym/hyponym | ✓ |

**Relations: 4/16 right, triplets: 3/16 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| cake #14 - on - table #9 | 0-80.6s | on | 0-81.5951s | identical | 0.99 | ✓ | ✓ |
| child #8 - sitting on - chair #10 | 0-80.6s | sitting on | 41.7926-63.684s | identical | 0.27 | ✗ | ✗ |
| cake #12 - on - table #9 | 0-80.6s | on | 0-81.5951s | identical | 0.99 | ✓ | ✓ |
| adult #7 - beside - child #8 | 1-60.2s | touching (+2 more) | 11.9407-41.7926s | semantic overlap | 0.50 | ✓ | ✓ |
| adult #7 - holding - hat #11 | 1-10s, 18.2-21.2s | holding (+1 more) | 0-41.7926s | identical | 0.29 | ✗ | ✗ |
| child #8 - wearing - hat #11 | 5.4-15.4s, 20.2-33.4s | wearing | 12.9358-41.7926s | identical | 0.43 | ✗ | ✗ |
| adult #13 - looking at - child #8 | 0-14s, 15.8-26.2s, 28-74s, 75.2-80.6s | helping | 41.7926-63.684s | mismatch | 0.29 | ✗ | ✗ |
| child #8 - touching - cake #12 | 2.8-3.6s, 18.8-23s, 33.2-34.6s, 47.4-48.2s, 50.6-51.8s, 56.4-57.4s, 64.6-65.4s, 70-71s, 76.2-77s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #13 - holding - hat #11 | 32.4-43s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #8 - eating - cake #12 | 38.2-40.2s, 48.4-49.6s, 52.6-54.4s, 57.6-58.6s, 65.4-66.6s, 71-75.2s, 77.8-79.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #13 - holding - towel #6 | 55.4-66.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| towel #6 - on - table #9 | 0-43s, 66.6-80.6s | on (+1 more) | 0-41.7926s | identical | 0.73 | ✓ | ✗ |
| towel #6 - touching - child #8 | 60-63.8s | moving toward (+1 more) | 41.7926-44.7778s | mismatch | 0.00 | ✗ | ✗ |
| adult #13 - touching - child #8 | 60-63.8s | helping | 41.7926-63.684s | mismatch | 0.17 | ✗ | ✗ |
| adult #13 - kissing - child #8 | 68.2-68.8s | helping | 41.7926-63.684s | mismatch | 0.00 | ✗ | ✗ |
| adult #13 - cleaning - child #8 | 60-63.8s | helping | 41.7926-63.684s | mismatch | 0.17 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (23): hat #11 - moving toward - child #8 [0-12.9358s]; hat #11 - on - child #8 [11.9407-41.7926s]; adult #7 - holding - towel #6 [41.7926-44.7778s]; adult #7 - serving - towel #6 [41.7926-44.7778s]; adult #7 - sitting on - chair #10 [41.7926-63.684s]; adult #13 - sitting on - chair #10 [41.7926-63.684s]; hat #11 - above - table #9 [0-41.7926s]; child #8 - behind - table #9 [0-81.5951s]; adult #13 - behind - table #9 [0-81.5951s]; adult #7 - behind - table #9 [0-63.684s]


## 1019_3768851893

58.6 s, 59 frames read | human: 30 objects, 30 relations | TRASER: 27 objects, 39 relations, valid JSON, 2082 tokens

**Objects: 18/30 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | person | mismatch | ✗ |
| 2 | wall | banner | mismatch | ✗ |
| 3 | tray | ribbon | mismatch | ✗ |
| 4 | curtain | screen | semantic overlap | ✓ |
| 5 | adult | person | hypernym/hyponym | ✓ |
| 6 | child | person | hypernym/hyponym | ✓ |
| 7 | plate | balloon | mismatch | ✗ |
| 8 | paper | - | no label from TRASER | ✗ |
| 9 | ballon | balloon | identical | ✓ |
| 10 | others | - | no label from TRASER | ✗ |
| 11 | adult | person | hypernym/hyponym | ✓ |
| 12 | child | person | hypernym/hyponym | ✓ |
| 13 | paper | balloon | mismatch | ✗ |
| 14 | ballon | - | no label from TRASER | ✗ |
| 15 | adult | person | hypernym/hyponym | ✓ |
| 16 | child | person | hypernym/hyponym | ✓ |
| 17 | paper | balloon | mismatch | ✗ |
| 18 | ballon | balloon | identical | ✓ |
| 19 | adult | person | hypernym/hyponym | ✓ |
| 20 | child | person | hypernym/hyponym | ✓ |
| 21 | paper | balloon | mismatch | ✗ |
| 22 | ballon | balloon | identical | ✓ |
| 23 | child | person | hypernym/hyponym | ✓ |
| 24 | paper | handbag | mismatch | ✗ |
| 25 | ballon | balloon | identical | ✓ |
| 26 | child | person | hypernym/hyponym | ✓ |
| 27 | paper | balloon | mismatch | ✗ |
| 28 | ballon | balloon | identical | ✓ |
| 29 | ballon | balloon | identical | ✓ |
| 30 | ballon | balloon | identical | ✓ |

**Relations: 6/30 right, triplets: 0/30 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #15 - holding - tray #3 | 23-51.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - holding - paper #17 | 36.8-38.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - holding - paper #21 | 41.6-42.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - holding - paper #24 | 48-50.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #23 - holding - paper #24 | 49.8-51.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| curtain #4 - on - wall #2 | 0-52s, 58-58.6s | behind | 7.94576-55.6203s | mismatch | 0.78 | ✗ | ✗ |
| child #6 - beside - child #12 | 9-58.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #6 - in front of - wall #2 | 9-58.6s | in front of | 9.9322-40.722s | identical | 0.62 | ✓ | ✗ |
| child #12 - beside - child #16 | 9-58.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #12 - in front of - wall #2 | 9-58.6s | in front of | 9.9322-45.6881s | identical | 0.72 | ✓ | ✗ |
| child #16 - beside - child #20 | 10.4-58.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #16 - in front of - wall #2 | 9-58.6s | in front of | 9.9322-45.6881s | identical | 0.72 | ✓ | ✗ |
| child #20 - beside - child #23 | 12.4-58.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #20 - in front of - wall #2 | 10.4-58.6s | in front of | 9.9322-45.6881s | identical | 0.73 | ✓ | ✗ |
| child #23 - beside - child #26 | 14-58.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #23 - in front of - wall #2 | 13.4-58.6s | in front of | 11.9186-45.6881s | identical | 0.69 | ✓ | ✗ |
| child #26 - in front of - wall #2 | 13.4-58.6s | in front of | 11.9186-45.6881s | identical | 0.69 | ✓ | ✗ |
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

**Objects: 21/22 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | floor | synonym | ✓ |
| 2 | wall | building | semantic overlap | ✓ |
| 3 | door | door | identical | ✓ |
| 4 | window | window | identical | ✓ |
| 5 | flower | bouquet | hypernym/hyponym | ✓ |
| 6 | glass | wine glass | hypernym/hyponym | ✓ |
| 7 | microphone | microphone | identical | ✓ |
| 8 | adult | person | hypernym/hyponym | ✓ |
| 9 | table | tablecloth | semantic overlap | ✓ |
| 10 | chair | chair | identical | ✓ |
| 11 | light | lamp post | semantic overlap | ✓ |
| 12 | bottle | bottle | identical | ✓ |
| 13 | camera | camera | identical | ✓ |
| 14 | window | window | identical | ✓ |
| 15 | flower | bouquet | hypernym/hyponym | ✓ |
| 16 | glass | wine glass | hypernym/hyponym | ✓ |
| 17 | adult | veil | mismatch | ✗ |
| 18 | chair | chair | identical | ✓ |
| 19 | flower | flower arrangement | hypernym/hyponym | ✓ |
| 20 | glass | wine glass | hypernym/hyponym | ✓ |
| 21 | adult | person | hypernym/hyponym | ✓ |
| 22 | adult | person | hypernym/hyponym | ✓ |

**Relations: 9/27 right, triplets: 9/27 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #22 - talking to - adult #17 | 0-47.6s | in front of | 0-54.8036s | mismatch | 0.87 | ✗ | ✗ |
| adult #22 - talking to - adult #21 | 0-47.6s | looking at | 0-54.8036s | semantic overlap | 0.87 | ✓ | ✓ |
| adult #8 - holding - camera #13 | 0-55.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - looking at - adult #21 | 0-55.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - beside - chair #18 | 0-55.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #22 - holding - microphone #7 | 0-55.8s | in front of | 0-54.8036s | mismatch | 0.98 | ✗ | ✗ |
| adult #22 - in front of - door #3 | 0-50.2s | in front of | 0-54.8036s | identical | 0.92 | ✓ | ✓ |
| adult #21 - caressing - adult #17 | 0-52.2s | wearing (+1 more) | 0-54.8036s | mismatch | 0.95 | ✗ | ✗ |
| adult #21 - caressing - adult #22 | 55.2-55.8s | holding hands with (+2 more) | 0-54.8036s | semantic overlap | 0.00 | ✗ | ✗ |
| adult #22 - standing on - ground #1 | 0-55.8s | on | 0-54.8036s | hypernym/hyponym | 0.98 | ✓ | ✓ |
| chair #18 - in front of - adult #21 | 0-55.8s | in front of | 0-54.8036s | identical | 0.98 | ✓ | ✓ |
| table #9 - in front of - chair #10 | 0-55.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| table #9 - in front of - chair #18 | 0-55.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| flower #5 - on - table #9 | 0-55.8s | on | 3.98571-54.8036s | identical | 0.91 | ✓ | ✓ |
| flower #15 - on - table #9 | 0-55.8s | on | 3.98571-54.8036s | identical | 0.91 | ✓ | ✓ |
| flower #19 - on - table #9 | 0-55.8s | on | 3.98571-21.9214s, 45.8357-54.8036s | identical | 0.48 | ✗ | ✗ |
| bottle #12 - on - table #9 | 0-55.8s | on | 3.98571-54.8036s | identical | 0.91 | ✓ | ✓ |
| adult #17 - beside - adult #21 | 0-55.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #21 - beside - adult #22 | 0-55.8s | holding hands with (+2 more) | 0-54.8036s | semantic overlap | 0.98 | ✓ | ✓ |
| light #11 - on - ground #1 | 0-55.8s | on | 0-54.8036s | identical | 0.98 | ✓ | ✓ |
| adult #21 - looking at - adult #22 | 0-3s, 4.2-10s | looking at (+2 more) | 0-54.8036s | identical | 0.16 | ✗ | ✗ |
| adult #21 - looking at - adult #17 | 3-4.2s, 10-12.4s | wearing (+1 more) | 0-54.8036s | mismatch | 0.07 | ✗ | ✗ |
| adult #17 - holding - glass #16 | 0-55.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #21 - holding - glass #6 | 0-55.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #22 - toward - adult #17 | 48.4-50.2s | in front of | 0-54.8036s | mismatch | 0.03 | ✗ | ✗ |
| adult #22 - hugging - adult #17 | 50.2-53.2s | in front of | 0-54.8036s | mismatch | 0.05 | ✗ | ✗ |
| adult #22 - hugging - adult #21 | 54.4-55.8s | looking at | 0-54.8036s | mismatch | 0.01 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (97): adult #21 - holding - glass #16 [0-54.8036s]; adult #22 - holding - glass #6 [0-54.8036s]; adult #21 - on - ground #1 [0-54.8036s]; chair #10 - on - ground #1 [0-54.8036s]; chair #18 - on - ground #1 [0-54.8036s]; table #9 - on - ground #1 [3.98571-54.8036s]; chair #10 - in front of - wall #2 [0-54.8036s]; chair #18 - in front of - wall #2 [0-54.8036s]; light #11 - in front of - wall #2 [0-54.8036s]; table #9 - in front of - wall #2 [3.98571-54.8036s]


## 1021_3478653250

65.8 s, 66 frames read | human: 13 objects, 23 relations | TRASER: 13 objects, 32 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 13/13 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | tree | bush | semantic overlap | ✓ |
| 2 | ground | stone pathway | semantic overlap | ✓ |
| 3 | grass | lawn | synonym | ✓ |
| 4 | wall | fence | semantic overlap | ✓ |
| 5 | stand | pole | semantic overlap | ✓ |
| 6 | basket | basketball backboard | semantic overlap | ✓ |
| 7 | child | child | identical | ✓ |
| 8 | bat | baseball bat | hypernym/hyponym | ✓ |
| 9 | ball | ball | identical | ✓ |
| 10 | ball | ball | identical | ✓ |
| 11 | ball | ball | identical | ✓ |
| 12 | ball | ball | identical | ✓ |
| 13 | ball | ball | identical | ✓ |

**Relations: 1/23 right, triplets: 1/23 right** (lenient, tIoU > 0.5)

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
| child #7 - holding - bat #8 | 0-62.6s | holding | 0-65.8s | identical | 0.95 | ✓ | ✓ |
| child #7 - hitting - ball #9 | 2-5s | hitting (+3 more) | 0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 45.8606-46.8576s, 47.8545-48.8515s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s | identical | 0.00 | ✗ | ✗ |
| child #7 - picking - ball #10 | 8.8-14s | hitting (+3 more) | 0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s | mismatch | 0.03 | ✗ | ✗ |
| ball #10 - on - stand #5 | 14.2-18.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - hitting - ball #10 | 17.2-18.6s | hitting (+3 more) | 0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s | identical | 0.03 | ✗ | ✗ |
| child #7 - picking - ball #13 | 26.8-28.8s | hitting (+4 more) | 0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s | mismatch | 0.04 | ✗ | ✗ |
| ball #13 - on - stand #5 | 28.4-42.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - hitting - ball #13 | 40.4-43.2s | hitting (+4 more) | 0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s | identical | 0.06 | ✗ | ✗ |
| child #7 - picking - ball #11 | 49.6-52.4s | hitting (+4 more) | 0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s | mismatch | 0.06 | ✗ | ✗ |
| ball #11 - on - stand #5 | 52.2-57.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - hitting - ball #11 | 55.8-57.4s | hitting (+4 more) | 0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s | identical | 0.04 | ✗ | ✗ |
| child #7 - picking - stand #5 | 60-61.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| bat #8 - on - grass #3 | 63-65.8s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (7): child #7 - hitting - ball #12 [0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 45.8606-46.8576s, 47.8545-48.8515s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s]; child #7 - hitting - ball #12 [0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 45.8606-46.8576s, 47.8545-48.8515s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s]; child #7 - hitting - ball #12 [0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 45.8606-46.8576s, 47.8545-48.8515s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s]; child #7 - hitting - ball #12 [0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s]; child #7 - hitting - ball #12 [0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s]; child #7 - hitting - tree #1 [0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 45.8606-46.8576s, 47.8545-48.8515s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s]; child #7 - hitting - tree #1 [0.99697-1.99394s, 12.9606-13.9576s, 14.9545-15.9515s, 16.9485-17.9455s, 19.9394-20.9364s, 21.9333-22.9303s, 23.9273-24.9242s, 25.9212-26.9182s, 27.9152-28.9121s, 29.9091-30.9061s, 31.903-32.9s, 33.897-34.8939s, 35.8909-36.8879s, 37.8848-38.8818s, 39.8788-40.8758s, 41.8727-42.8697s, 43.8667-44.8636s, 45.8606-46.8576s, 47.8545-48.8515s, 49.8485-50.8455s, 51.8424-52.8394s, 53.8364-54.8333s, 55.8303-56.8273s, 57.8242-58.8212s, 59.8182-60.8152s, 61.8121-62.8091s, 63.8061-64.803s]


## 1021_4278168115

79.8 s, 80 frames read | human: 11 objects, 21 relations | TRASER: 11 objects, 40 relations, valid JSON, 1274 tokens

**Objects: 11/11 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | tree | Christmas tree | hypernym/hyponym | ✓ |
| 2 | floor | rug | semantic overlap | ✓ |
| 3 | gift | gift wrap | semantic overlap | ✓ |
| 4 | curtain | curtain | identical | ✓ |
| 5 | book | book | identical | ✓ |
| 6 | adult | person | hypernym/hyponym | ✓ |
| 7 | child | child | identical | ✓ |
| 8 | box | box | identical | ✓ |
| 9 | book | book | identical | ✓ |
| 10 | book | book | identical | ✓ |
| 11 | book | book | identical | ✓ |

**Relations: 9/21 right, triplets: 9/21 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| child #7 - touching - book #9 | 66.2-71.2s | holding (+1 more) | 41.895-51.87s | hypernym/hyponym | 0.00 | ✗ | ✗ |
| child #7 - touching - book #11 | 78.2-79.8s | holding (+1 more) | 51.87-65.835s | hypernym/hyponym | 0.00 | ✗ | ✗ |
| adult #6 - touching - book #5 | 49.4-52s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - on - floor #2 | 0-79.8s | on | 0-80.7975s | identical | 0.99 | ✓ | ✓ |
| adult #6 - sitting on - floor #2 | 0-79.8s | on | 0-80.7975s | hypernym/hyponym | 0.99 | ✓ | ✓ |
| child #7 - in front of - adult #6 | 0-79.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #6 - holding - gift #3 | 0-3s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - opening - gift #3 | 3.6-31s | opening (+2 more) | 1.995-27.93s | identical | 0.84 | ✓ | ✓ |
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

**Objects: 21/27 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | rock | chair | mismatch | ✗ |
| 2 | floor | chair leg (uncertain) | mismatch | ✗ |
| 3 | ceiling | ceiling fan | semantic overlap | ✓ |
| 4 | wall | wall | identical | ✓ |
| 5 | door | door | identical | ✓ |
| 6 | curtain | door frame (uncertain) | mismatch | ✗ |
| 7 | shelf | bookshelf | hypernym/hyponym | ✓ |
| 8 | window | curtain | semantic overlap | ✓ |
| 9 | adult | person | hypernym/hyponym | ✓ |
| 10 | child | child | identical | ✓ |
| 11 | table | tablecloth | semantic overlap | ✓ |
| 12 | chair | table | mismatch | ✗ |
| 13 | candle | cake | semantic overlap | ✓ |
| 14 | cake | cake | identical | ✓ |
| 15 | cellphone | cell phone | identical | ✓ |
| 16 | ballon | balloon | identical | ✓ |
| 17 | chair | chair | identical | ✓ |
| 18 | ballon | balloon | identical | ✓ |
| 19 | adult | person | hypernym/hyponym | ✓ |
| 20 | chair | chair | identical | ✓ |
| 21 | ballon | balloon | identical | ✓ |
| 22 | adult | person | hypernym/hyponym | ✓ |
| 23 | chair | chair | identical | ✓ |
| 24 | ballon | chair | mismatch | ✗ |
| 25 | adult | person | hypernym/hyponym | ✓ |
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
| adult #19 - holding - child #10 | 12.8-90s | photographing (+9 more) | 73-90s | mismatch | 0.22 | ✗ | ✗ |
| adult #19 - picking - chair #12 | 31.6-35.4s | photographing (+8 more) | 73-90s | mismatch | 0.00 | ✗ | ✗ |
| adult #22 - next to - adult #19 | 49.2-90s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #19 - blowing - candle #13 | 58.8-61.4s | looking at (+10 more) | 22-90s | mismatch | 0.04 | ✗ | ✗ |
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

**Objects: 11/11 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | sand | semantic overlap | ✓ |
| 2 | ceiling | ceiling | identical | ✓ |
| 3 | wall | fence | semantic overlap | ✓ |
| 4 | adult | person | hypernym/hyponym | ✓ |
| 5 | child | person | hypernym/hyponym | ✓ |
| 6 | horse | horse | identical | ✓ |
| 7 | hat | helmet | semantic overlap | ✓ |
| 8 | box | box | identical | ✓ |
| 9 | child | person | hypernym/hyponym | ✓ |
| 10 | horse | horse | identical | ✓ |
| 11 | hat | helmet | semantic overlap | ✓ |

**Relations: 7/12 right, triplets: 7/12 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| box #8 - on - ground #1 | 0-5.2s | on | 0-5.88571s | identical | 0.88 | ✓ | ✓ |
| child #5 - wearing - hat #7 | 0-20.6s | wearing | 0-20.6s | identical | 1.00 | ✓ | ✓ |
| child #9 - wearing - hat #11 | 0-5.4s, 10.8-20.6s | wearing | 0-20.6s | identical | 0.74 | ✓ | ✓ |
| child #9 - looking at - child #5 | 0-5.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - looking at - child #5 | 5-8s | nothing for this pair | - | - | - | ✗ | ✗ |
| horse #6 - walking on - ground #1 | 0-20.6s | moving across (+1 more) | 0-20.6s | semantic overlap | 1.00 | ✓ | ✓ |
| horse #10 - walking on - ground #1 | 0-5.4s, 10.8-20.6s | moving across (+1 more) | 0-20.6s | semantic overlap | 0.74 | ✓ | ✓ |
| adult #4 - walking on - ground #1 | 5-8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #5 - riding - horse #6 | 0-20.6s | riding (+1 more) | 0-20.6s | identical | 1.00 | ✓ | ✓ |
| child #9 - riding - horse #10 | 0-5.4s, 10.8-20.6s | riding (+1 more) | 0-20.6s | identical | 0.74 | ✓ | ✓ |
| adult #4 - guiding - child #5 | 0-20.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #4 - guiding - child #9 | 0-20.6s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (17): child #5 - moving across - ground #1 [0-20.6s]; child #9 - moving across - ground #1 [0-20.6s]; horse #6 - moving with - horse #10 [0-20.6s]; horse #6 - next to - horse #10 [0-20.6s]; child #5 - moving with - child #9 [0-20.6s]; child #5 - next to - child #9 [0-20.6s]; horse #6 - in front of - wall #3 [0-20.6s]; horse #10 - in front of - wall #3 [0-20.6s]; child #5 - in front of - wall #3 [0-20.6s]; child #9 - in front of - wall #3 [0-20.6s]


## 1052_8530515192

72.4 s, 72 frames read | human: 15 objects, 28 relations | TRASER: 15 objects, 31 relations, valid JSON, 1258 tokens

**Objects: 15/15 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | adult | person | hypernym/hyponym | ✓ |
| 2 | child | child | identical | ✓ |
| 3 | table | tablecloth | semantic overlap | ✓ |
| 4 | chair | chair | identical | ✓ |
| 5 | candle | candle | identical | ✓ |
| 6 | cake | cake | identical | ✓ |
| 7 | adult | person | hypernym/hyponym | ✓ |
| 8 | child | girl | hypernym/hyponym | ✓ |
| 9 | chair | chair | identical | ✓ |
| 10 | candle | candle | identical | ✓ |
| 11 | cake | cake | identical | ✓ |
| 12 | adult | person | hypernym/hyponym | ✓ |
| 13 | child | child | identical | ✓ |
| 14 | adult | person | hypernym/hyponym | ✓ |
| 15 | child | person | hypernym/hyponym | ✓ |

**Relations: 5/28 right, triplets: 5/28 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| child #8 - blowing - candle #10 | 60.8-68.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - touching - child #2 | 0-0.8s, 2.4-3.6s, 5.6-6.8s, 21-24s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #15 - beside - child #2 | 39-72.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #2 - sitting on - chair #4 | 0-72.4s | sitting on (+1 more) | 0-72.4s | identical | 1.00 | ✓ | ✓ |
| cake #6 - on - table #3 | 0-72.4s | on | 0-72.4s | identical | 1.00 | ✓ | ✓ |
| candle #5 - on - cake #6 | 0-72.4s | attached to (+1 more) | 0-72.4s | semantic overlap | 1.00 | ✓ | ✓ |
| child #2 - beside - table #3 | 0-72.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #8 - sitting on - chair #9 | 0-72.4s | sitting on (+1 more) | 0-72.4s | identical | 1.00 | ✓ | ✓ |
| cake #11 - on - table #3 | 0-72.4s | on | 0-72.4s | identical | 1.00 | ✓ | ✓ |
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
| adult #1 - touching - chair #4 | 36.2-42.6s | sitting on (+1 more) | 0-72.4s | hypernym/hyponym | 0.09 | ✗ | ✗ |
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

**Objects: 8/8 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | sky | cloud | semantic overlap | ✓ |
| 2 | tree | tree | identical | ✓ |
| 3 | ground | basketball court | semantic overlap | ✓ |
| 4 | grass | grass | identical | ✓ |
| 5 | adult | person | hypernym/hyponym | ✓ |
| 6 | child | child | identical | ✓ |
| 7 | ball | sports ball | hypernym/hyponym | ✓ |
| 8 | child | child | identical | ✓ |

**Relations: 1/15 right, triplets: 1/15 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #5 - walking on - ground #3 | 16.8-21.4s | on | 13.113-22.1913s | hypernym/hyponym | 0.51 | ✓ | ✓ |
| child #8 - lying on - ground #3 | 6.8-11.8s | on | 0-22.1913s | hypernym/hyponym | 0.23 | ✗ | ✗ |
| child #6 - standing on - ground #3 | 0-2.6s | on | 0-22.1913s | hypernym/hyponym | 0.12 | ✗ | ✗ |
| child #8 - standing on - ground #3 | 0-2.6s | on | 0-22.1913s | hypernym/hyponym | 0.12 | ✗ | ✗ |
| child #6 - picking - ball #7 | 3.4-8.8s | dribbles | 0-2.01739s, 3.02609-11.0957s | mismatch | 0.54 | ✗ | ✗ |
| child #8 - picking - ball #7 | 3.6-5.6s | dribbles | 11.0957-20.1739s | mismatch | 0.00 | ✗ | ✗ |
| child #6 - kicking - ball #7 | 9.4-10.6s | dribbles | 0-2.01739s, 3.02609-11.0957s | mismatch | 0.12 | ✗ | ✗ |
| child #8 - toward - ball #7 | 14.6-16.6s, 19.8-21.8s | dribbles | 11.0957-20.1739s | mismatch | 0.22 | ✗ | ✗ |
| adult #5 - running on - ground #3 | 14-15.4s | on | 13.113-22.1913s | hypernym/hyponym | 0.15 | ✗ | ✗ |
| adult #5 - picking - ball #7 | 15.4-16.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #8 - grabbing - ball #7 | 16.4-17.8s | dribbles | 11.0957-20.1739s | mismatch | 0.15 | ✗ | ✗ |
| child #8 - kicking - ball #7 | 18-19.8s | dribbles | 11.0957-20.1739s | mismatch | 0.20 | ✗ | ✗ |
| child #6 - toward - ball #7 | 19.8-21.4s | dribbles | 0-2.01739s, 3.02609-11.0957s | mismatch | 0.00 | ✗ | ✗ |
| child #6 - playing with - ball #7 | 0-21.4s | dribbles | 0-2.01739s, 3.02609-11.0957s | hypernym/hyponym | 0.47 | ✗ | ✗ |
| child #8 - playing with - ball #7 | 0-21.4s | dribbles | 11.0957-20.1739s | hypernym/hyponym | 0.42 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (21): child #6 - approaches - child #8 [10.087-13.113s]; child #6 - moves away from - child #8 [13.113-20.1739s]; child #6 - plays with - child #8 [0-20.1739s]; child #6 - near - child #8 [0-20.1739s]; ball #7 - moves across - ground #3 [0-2.01739s, 3.02609-23.2s]; ball #7 - on - ground #3 [0-2.01739s, 3.02609-23.2s]; child #6 - in front of - tree #2 [0-22.1913s]; child #8 - in front of - tree #2 [0-22.1913s]; ball #7 - in front of - tree #2 [0-2.01739s, 3.02609-22.1913s]; adult #5 - in front of - tree #2 [13.113-22.1913s]


## 1122_3393449055

18.4 s, 18 frames read | human: 9 objects, 11 relations | TRASER: 9 objects, 31 relations, valid JSON, 1053 tokens

**Objects: 7/9 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | wall | cabinet | mismatch | ✗ |
| 2 | cabinet | cabinet door | semantic overlap | ✓ |
| 3 | adult | person | hypernym/hyponym | ✓ |
| 4 | child | baby | hypernym/hyponym | ✓ |
| 5 | dog | dog | identical | ✓ |
| 6 | table | table | identical | ✓ |
| 7 | hat | baseball cap | hypernym/hyponym | ✓ |
| 8 | adult | person | hypernym/hyponym | ✓ |
| 9 | hat | toy | mismatch | ✗ |

**Relations: 5/11 right, triplets: 5/11 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #3 - holding - child #4 | 0-18.4s | holding (+3 more) | 0-19.4222s | identical | 0.95 | ✓ | ✓ |
| adult #3 - looking at - child #4 | 0-18.4s | looking at (+3 more) | 0-19.4222s | identical | 0.95 | ✓ | ✓ |
| adult #3 - wearing - hat #7 | 0-18.4s | wearing | 4.08889-15.3333s | identical | 0.61 | ✓ | ✓ |
| adult #8 - holding - dog #5 | 0-12s | holding (+3 more) | 0-12.2667s | identical | 0.98 | ✓ | ✓ |
| adult #8 - looking at - dog #5 | 0-12s | looking at (+3 more) | 0-12.2667s | identical | 0.98 | ✓ | ✓ |
| adult #8 - wearing - hat #9 | 7.8-13.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #5 - playing with - child #4 | 0-8.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #5 - kissing - child #4 | 0-8.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #3 - next to - adult #8 | 0-13.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #3 - cleaning - child #4 | 13-15.4s | holding (+3 more) | 0-19.4222s | mismatch | 0.12 | ✗ | ✗ |
| dog #5 - licking - child #4 | 0-2.4s, 3.4-5s, 6.6-7.8s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (22): adult #3 - in front of - wall #1 [0-19.4222s]; child #4 - in front of - wall #1 [0-19.4222s]; dog #5 - in front of - wall #1 [0-12.2667s]; adult #8 - in front of - wall #1 [0-14.3111s]; table #6 - in front of - wall #1 [0-16.3556s]; cabinet #2 - on - wall #1 [0-15.3333s]; adult #3 - in front of - cabinet #2 [0-15.3333s]; child #4 - in front of - cabinet #2 [0-15.3333s]; dog #5 - in front of - cabinet #2 [0-12.2667s]; adult #8 - in front of - cabinet #2 [0-14.3111s]


## 1124_9861436503

64.6 s, 65 frames read | human: 13 objects, 11 relations | TRASER: 12 objects, 33 relations, valid JSON, 1332 tokens

**Objects: 8/13 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | toy horse | mismatch | ✗ |
| 2 | wall | wall | identical | ✓ |
| 3 | door | door (uncertain) | identical | ✓ |
| 4 | curtain | - | no label from TRASER | ✗ |
| 5 | shelf | cabinet | semantic overlap | ✓ |
| 6 | adult | person | hypernym/hyponym | ✓ |
| 7 | child | child | identical | ✓ |
| 8 | dog | horse | mismatch | ✗ |
| 9 | sofa | sofa | identical | ✓ |
| 10 | table | coffee table | hypernym/hyponym | ✓ |
| 11 | toy | horse | mismatch | ✗ |
| 12 | adult | hand | mismatch | ✗ |
| 13 | sofa | sofa | identical | ✓ |

**Relations: 2/11 right, triplets: 0/11 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| dog #8 - playing with - child #7 | 0-20.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - sitting on - toy #11 | 0-29.8s, 43.8-60.2s | near (+3 more) | 0-64.6s | semantic overlap | 0.72 | ✓ | ✗ |
| dog #8 - biting - toy #11 | 20.2-64.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - walking on - floor #1 | 39.6-43.8s, 60.2-64.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #6 - sitting on - sofa #13 | 41.8-64.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| toy #11 - on - floor #1 | 0-64.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| toy #11 - in front of - table #10 | 0-35.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| toy #11 - in front of - sofa #9 | 36.8-64.6s | in front of | 22.8585-64.6s | identical | 0.67 | ✓ | ✗ |
| table #10 - in front of - sofa #9 | 0-64.6s | in front of | 40.7477-54.6615s, 58.6369-64.6s | identical | 0.31 | ✗ | ✗ |
| child #7 - swinging - toy #11 | 0-30.6s, 45-55.2s | pushes (+3 more) | 0-64.6s | mismatch | 0.63 | ✗ | ✗ |
| child #7 - getting down on - toy #11 | 29.4-30.6s, 55-60.2s | pushes (+3 more) | 0-64.6s | mismatch | 0.10 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (27): child #7 - moves away from - table #10 [40.7477-54.6615s]; child #7 - approaches - sofa #9 [40.7477-46.7108s]; child #7 - moves away from - sofa #9 [53.6677-64.6s]; child #7 - in front of - sofa #9 [22.8585-64.6s]; child #7 - in front of - shelf #5 [0-54.6615s]; child #7 - in front of - wall #2 [0-54.6615s]; child #7 - in front of - sofa #13 [40.7477-64.6s]; child #7 - in front of - adult #6 [40.7477-54.6615s]; toy #11 - in front of - shelf #5 [0-54.6615s]; toy #11 - in front of - wall #2 [0-54.6615s]


## 1161_5895320023

49.4 s, 49 frames read | human: 30 objects, 9 relations | TRASER: 29 objects, 41 relations, valid JSON, 2279 tokens

**Objects: 25/30 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | dog | mismatch | ✗ |
| 2 | wall | balloon | mismatch | ✗ |
| 3 | shoe | shoe (uncertain) | identical | ✓ |
| 4 | pillow | blanket | semantic overlap | ✓ |
| 5 | door | window | semantic overlap | ✓ |
| 6 | curtain | curtain | identical | ✓ |
| 7 | window | curtain | semantic overlap | ✓ |
| 8 | adult | person | hypernym/hyponym | ✓ |
| 9 | dog | dog | identical | ✓ |
| 10 | sofa | sofa | identical | ✓ |
| 11 | table | tablecloth | semantic overlap | ✓ |
| 12 | chair | chair | identical | ✓ |
| 13 | light | cushion | mismatch | ✗ |
| 14 | ball | balloon | semantic overlap | ✓ |
| 15 | pillow | blanket | semantic overlap | ✓ |
| 16 | door | door | identical | ✓ |
| 17 | window | window | identical | ✓ |
| 18 | adult | person | hypernym/hyponym | ✓ |
| 19 | dog | dog | identical | ✓ |
| 20 | sofa | sofa | identical | ✓ |
| 21 | table | tablecloth | semantic overlap | ✓ |
| 22 | chair | chair | identical | ✓ |
| 23 | ball | - | no label from TRASER | ✗ |
| 24 | window | window | identical | ✓ |
| 25 | adult | person | hypernym/hyponym | ✓ |
| 26 | table | box | mismatch | ✗ |
| 27 | chair | chair | identical | ✓ |
| 28 | adult | person | hypernym/hyponym | ✓ |
| 29 | chair | chair | identical | ✓ |
| 30 | adult | person | hypernym/hyponym | ✓ |

**Relations: 0/9 right, triplets: 0/9 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #8 - sitting on - sofa #10 | 0-49.4s | in front of | 0-21.1714s | mismatch | 0.43 | ✗ | ✗ |
| dog #19 - lying on - sofa #10 | 0-49.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| sofa #10 - in front of - adult #18 | 18.6-49.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #28 - sitting on - sofa #20 | 27.2-49.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #9 - chasing - ball #14 | 0-49.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #18 - picking - ball #14 | 16.8-19s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #25 - picking - ball #14 | 27.2-29.4s, 30.4-32.4s, 33.2-34.4s, 36-37.2s, 39-40.4s | holding (+2 more) | 28.2286-42.3429s | semantic overlap | 0.46 | ✗ | ✗ |
| dog #9 - playing with - ball #14 | 0-49.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #9 - jumping from - floor #1 | 26.4-27.4s, 29.4-30.4s, 32-33.4s, 34.2-35.2s, 37.2-38.2s, 40.4-41.6s, 42.6-44.2s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (37): adult #8 - holding - ball #14 [0-20.1633s]; adult #8 - looking at - ball #14 [0-20.1633s]; ball #14 - moving away from - adult #8 [19.1551-21.1714s]; ball #14 - approaching - adult #25 [26.2122-29.2367s]; ball #14 - moving toward - table #26 [42.3429-45.3673s]; ball #14 - moving away from - table #26 [45.3673-48.3918s]; ball #14 - above - table #26 [31.2531-50.4082s]; ball #14 - moving toward - sofa #20 [46.3755-48.3918s]; ball #14 - moving away from - sofa #20 [48.3918-50.4082s]; ball #14 - above - sofa #20 [26.2122-50.4082s]


## 1164_6895784766

44.6 s, 45 frames read | human: 16 objects, 14 relations | TRASER: 14 objects, 21 relations, valid JSON, 2121 tokens

**Objects: 11/16 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | toy car | mismatch | ✗ |
| 2 | ceiling | ceiling light fixture | semantic overlap | ✓ |
| 3 | wall | wall | identical | ✓ |
| 4 | door | door | identical | ✓ |
| 5 | shelf | bookshelf | hypernym/hyponym | ✓ |
| 6 | basket | basketball hoop | semantic overlap | ✓ |
| 7 | adult | child | hypernym/hyponym | ✓ |
| 8 | child | child | identical | ✓ |
| 9 | bed | drawer (uncertain) | mismatch | ✗ |
| 10 | sofa | trash can (uncertain) | mismatch | ✗ |
| 11 | light | lamp | hypernym/hyponym | ✓ |
| 12 | ball | basketball | hypernym/hyponym | ✓ |
| 13 | shelf | - | no label from TRASER | ✗ |
| 14 | adult | - | no label from TRASER | ✗ |
| 15 | child | child | identical | ✓ |
| 16 | ball | sports ball (uncertain) | hypernym/hyponym | ✓ |

**Relations: 0/14 right, triplets: 0/14 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #7 - kicking - ball #16 | 26.6-27.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| basket #6 - next to - shelf #5 | 0-44.6s | in front of | 0-11.8933s, 16.8489-45.5911s | mismatch | 0.87 | ✗ | ✗ |
| child #8 - holding - ball #12 | 0-0.8s, 17.4-44.6s | holding (+1 more) | 0-1.98222s, 2.97333-4.95556s, 9.91111-10.9022s, 11.8933-12.8844s, 13.8756-14.8667s, 15.8578-16.8489s, 17.84-18.8311s, 19.8222-20.8133s, 21.8044-22.7956s, 23.7867-24.7778s, 25.7689-26.76s, 27.7511-28.7422s, 29.7333-30.7244s, 31.7156-32.7067s, 33.6978-34.6889s | identical | 0.28 | ✗ | ✗ |
| child #8 - standing on - floor #1 | 0-34.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #15 - standing on - floor #1 | 0-44.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #15 - holding - ball #12 | 6.4-7.8s | holding (+1 more) | 2.97333-4.95556s, 9.91111-10.9022s, 11.8933-12.8844s, 13.8756-14.8667s, 15.8578-16.8489s, 17.84-18.8311s, 19.8222-20.8133s, 21.8044-22.7956s, 23.7867-24.7778s, 25.7689-26.76s, 27.7511-28.7422s, 29.7333-30.7244s, 31.7156-32.7067s, 33.6978-34.6889s | identical | 0.00 | ✗ | ✗ |
| child #8 - holding - ball #16 | 7.6-10.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #15 - holding - ball #16 | 10.6-16.2s, 18.2-20.2s, 28.4-32.8s, 35.4-38s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - holding - child #8 | 31.6-34.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #8 - throwing - ball #12 | 0-1.2s | holding (+1 more) | 0-1.98222s, 2.97333-4.95556s, 9.91111-10.9022s, 11.8933-12.8844s, 13.8756-14.8667s, 15.8578-16.8489s, 17.84-18.8311s, 19.8222-20.8133s, 21.8044-22.7956s, 23.7867-24.7778s, 25.7689-26.76s, 27.7511-28.7422s, 29.7333-30.7244s, 31.7156-32.7067s, 33.6978-34.6889s | mismatch | 0.07 | ✗ | ✗ |
| child #15 - throwing - ball #12 | 6.8-7.8s | holding (+1 more) | 2.97333-4.95556s, 9.91111-10.9022s, 11.8933-12.8844s, 13.8756-14.8667s, 15.8578-16.8489s, 17.84-18.8311s, 19.8222-20.8133s, 21.8044-22.7956s, 23.7867-24.7778s, 25.7689-26.76s, 27.7511-28.7422s, 29.7333-30.7244s, 31.7156-32.7067s, 33.6978-34.6889s | mismatch | 0.00 | ✗ | ✗ |
| child #15 - carrying - ball #16 | 10-13s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #15 - throwing - ball #16 | 12.8-14.6s, 20-20.8s, 37.8-38.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #8 - squatting on - floor #1 | 16.8-17.8s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (16): child #8 - playing with - child #15 [0-1.98222s, 2.97333-4.95556s, 9.91111-10.9022s, 11.8933-12.8844s, 13.8756-14.8667s, 15.8578-16.8489s, 17.84-18.8311s, 19.8222-20.8133s, 21.8044-22.7956s, 23.7867-24.7778s, 25.7689-26.76s, 27.7511-28.7422s, 29.7333-30.7244s, 31.7156-32.7067s, 33.6978-34.6889s]; child #15 - playing with - child #8 [0-1.98222s, 2.97333-4.95556s, 9.91111-10.9022s, 11.8933-12.8844s, 13.8756-14.8667s, 15.8578-16.8489s, 17.84-18.8311s, 19.8222-20.8133s, 21.8044-22.7956s, 23.7867-24.7778s, 25.7689-26.76s, 27.7511-28.7422s, 29.7333-30.7244s, 31.7156-32.7067s, 33.6978-34.6889s]; child #8 - in front of - basket #6 [0-35.68s]; child #15 - in front of - basket #6 [0-45.5911s]; child #8 - in front of - shelf #5 [0-11.8933s, 16.8489-35.68s]; child #15 - in front of - shelf #5 [0-11.8933s, 16.8489-45.5911s]; basket #6 - in front of - wall #3 [0-45.5911s]; shelf #5 - against - wall #3 [0-11.8933s, 16.8489-45.5911s]; door #4 - in - wall #3 [0-45.5911s]; ceiling #2 - above - basket #6 [7.92889-45.5911s]


## 1203_8316378691

60.2 s, 60 frames read | human: 23 objects, 15 relations | TRASER: 22 objects, 42 relations, valid JSON, 2087 tokens

**Objects: 16/23 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | ground | chair leg | mismatch | ✗ |
| 2 | floor | chair leg | mismatch | ✗ |
| 3 | wall | - | no label from TRASER | ✗ |
| 4 | carpet | doormat | hypernym/hyponym | ✓ |
| 5 | book | hand | mismatch | ✗ |
| 6 | adult | person | hypernym/hyponym | ✓ |
| 7 | child | person | hypernym/hyponym | ✓ |
| 8 | dog | plush toy | mismatch | ✗ |
| 9 | sofa | sofa | identical | ✓ |
| 10 | table | coffee table | hypernym/hyponym | ✓ |
| 11 | cup | cup | identical | ✓ |
| 12 | bag | fabric | mismatch | ✗ |
| 13 | box | box | identical | ✓ |
| 14 | camera | cell phone | semantic overlap | ✓ |
| 15 | adult | person | hypernym/hyponym | ✓ |
| 16 | camera | cell phone | semantic overlap | ✓ |
| 17 | adult | person | hypernym/hyponym | ✓ |
| 18 | cup | cup | identical | ✓ |
| 19 | camera | cell phone | semantic overlap | ✓ |
| 20 | adult | person | hypernym/hyponym | ✓ |
| 21 | adult | person | hypernym/hyponym | ✓ |
| 22 | adult | person | hypernym/hyponym | ✓ |
| 23 | adult | arm | mismatch | ✗ |

**Relations: 5/15 right, triplets: 5/15 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #17 - holding - cup #11 | 0-45.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #23 - holding - bag #12 | 48.6-52.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| child #7 - standing on - carpet #4 | 58.2-60.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #6 - opening - box #13 | 13.8-17s | opening (+3 more) | 10.0333-17.0567s | identical | 0.46 | ✗ | ✗ |
| adult #22 - standing on - carpet #4 | 42.6-60.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #15 - on - sofa #9 | 0-60.2s | sitting on (+1 more) | 0-45.15s, 52.1733-60.2s | hypernym/hyponym | 0.88 | ✓ | ✓ |
| adult #17 - on - sofa #9 | 0-60.2s | sitting on (+1 more) | 0-45.15s, 52.1733-60.2s | hypernym/hyponym | 0.88 | ✓ | ✓ |
| child #7 - on - sofa #9 | 0-12s, 25.6-55.2s | sitting on (+1 more) | 0-45.15s, 52.1733-60.2s | hypernym/hyponym | 0.57 | ✓ | ✓ |
| adult #6 - holding - box #13 | 0-14.2s | holding (+3 more) | 0-25.0833s | identical | 0.57 | ✓ | ✓ |
| child #7 - holding - dog #8 | 16.8-60.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| box #13 - on - table #10 | 7.4-60.2s | on (+1 more) | 0-45.15s, 52.1733-60.2s | identical | 0.76 | ✓ | ✓ |
| dog #8 - in - box #13 | 0-21.6s, 59.8-60.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #20 - holding - camera #14 | 0-60.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #21 - holding - camera #19 | 0-60.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #22 - holding - camera #16 | 0-60.2s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (30): adult #6 - holding - cup #11 [25.0833-27.09s]; adult #6 - holding - camera #14 [27.09-30.1s]; adult #6 - holding - camera #16 [27.09-30.1s]; adult #6 - holding - camera #19 [27.09-30.1s]; adult #6 - holding - bag #12 [47.1567-52.1733s]; adult #6 - looking at - bag #12 [47.1567-52.1733s]; adult #6 - holding - dog #8 [55.1833-60.2s]; adult #6 - looking at - dog #8 [55.1833-60.2s]; table #10 - in front of - sofa #9 [0-45.15s, 52.1733-60.2s]; box #13 - in front of - sofa #9 [0-45.15s, 52.1733-60.2s]


## 1bfe5ac2-cbf8-4364-8a30-60d97dd395df_1

84.0 s, 84 frames read | human: 19 objects, 14 relations | TRASER: 18 objects, 37 relations, valid JSON, 2696 tokens

**Objects: 9/19 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | bottle | mismatch | ✗ |
| 2 | wall | wall | identical | ✓ |
| 3 | others | device (uncertain) | mismatch | ✗ |
| 4 | rag | glove | mismatch | ✗ |
| 5 | pillow | chair leg (uncertain) | mismatch | ✗ |
| 6 | bucket | bucket | identical | ✓ |
| 7 | cabinet | refrigerator door | semantic overlap | ✓ |
| 8 | towel | - | no label from TRASER | ✗ |
| 9 | adult | arm | mismatch | ✗ |
| 10 | sofa | sofa | identical | ✓ |
| 11 | table | table | identical | ✓ |
| 12 | chair | chair | identical | ✓ |
| 13 | bag | chair | mismatch | ✗ |
| 14 | others | cable | mismatch | ✗ |
| 15 | table | chair leg (uncertain) | mismatch | ✗ |
| 16 | chair | chair | identical | ✓ |
| 17 | table | chair | mismatch | ✗ |
| 18 | chair | chair | identical | ✓ |
| 19 | chair | chair leg (uncertain) | semantic overlap | ✓ |

**Relations: 0/14 right, triplets: 0/14 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #9 - holding - rag #4 | 0-23.2s, 25.6-78.2s | wearing | 0-2s, 3-17s, 18-22s, 23-32s, 33-45s, 46-60s, 61-74s, 75-82s | mismatch | 0.84 | ✗ | ✗ |
| adult #9 - cleaning - floor #1 | 1.8-22s, 32.6-47.2s, 58.6-78.2s | holding | 1-2s, 3-17s | mismatch | 0.26 | ✗ | ✗ |
| adult #9 - touching - floor #1 | 3.4-8.6s, 11.2-18.2s, 19.6-21.8s, 35.8-38.4s, 66.6-75.4s | holding | 1-2s, 3-17s | hypernym/hyponym | 0.37 | ✗ | ✗ |
| adult #9 - touching - bucket #6 | 22-23.2s | holding (+1 more) | 23-32s, 46-60s, 76-82s | hypernym/hyponym | 0.01 | ✗ | ✗ |
| rag #4 - in - bucket #6 | 22.4-26.4s, 47.8-51.2s, 78.8-84s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - touching - others #14 | 9-11.2s | holding (+1 more) | 8-13s | hypernym/hyponym | 0.44 | ✗ | ✗ |
| adult #9 - pushing - chair #12 | 23.2-25.6s, 81.6-83.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - holding - table #11 | 38.6-42.2s | holding (+1 more) | 1-2s, 3-17s | identical | 0.00 | ✗ | ✗ |
| adult #9 - holding - bucket #6 | 45.6-51s, 78.2-80.8s | holding (+1 more) | 23-32s, 46-60s, 76-82s | identical | 0.26 | ✗ | ✗ |
| adult #9 - walking on - floor #1 | 56.2-57.6s, 81-84s | holding | 1-2s, 3-17s | mismatch | 0.00 | ✗ | ✗ |
| adult #9 - holding - others #3 | 59.6-66s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - touching - table #17 | 75.8-76.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - cleaning - rag #4 | 22.4-26.4s, 47.8-51.2s | wearing | 0-2s, 3-17s, 18-22s, 23-32s, 33-45s, 46-60s, 61-74s, 75-82s | mismatch | 0.09 | ✗ | ✗ |
| bag #13 - hanging from - chair #18 | 0-84s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (29): adult #9 - in front of - wall #2 [0-2s, 3-17s, 25-32s, 33-45s, 46-60s, 61-74s, 75-76s, 77-78s, 80-82s]; rag #4 - on - adult #9 [0-2s, 3-17s, 18-22s, 23-32s, 33-45s, 46-60s, 61-74s, 75-82s]; bucket #6 - in front of - wall #2 [25-32s, 33-45s, 46-60s, 61-74s, 77-78s, 80-82s]; others #14 - in front of - wall #2 [3-13s]; table #11 - in front of - wall #2 [0-2s, 3-17s, 25-32s, 33-45s, 46-60s, 61-74s, 77-78s, 80-82s]; sofa #10 - in front of - wall #2 [0-2s, 3-17s, 25-32s, 33-45s, 46-60s, 61-74s, 77-78s, 80-82s]; chair #12 - in front of - wall #2 [0-2s, 3-17s, 25-32s, 33-45s, 46-60s, 61-74s, 77-78s, 80-82s]; chair #16 - in front of - wall #2 [25-32s, 33-45s, 46-60s, 61-74s, 77-78s, 80-82s]; table #17 - in front of - wall #2 [25-32s, 33-45s, 46-60s, 61-74s, 77-78s, 80-82s]; chair #18 - in front of - wall #2 [25-32s, 33-45s, 46-60s, 61-74s, 77-78s, 80-82s]


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


## 43b0205a-4e3c-46a7-9d1c-c04ead730180

196.0 s, 128 frames read | human: 26 objects, 8 relations | TRASER: 24 objects, 16 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 4/26 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | broom | mismatch | ✗ |
| 2 | wall | person | mismatch | ✗ |
| 3 | water | pipe (uncertain) | mismatch | ✗ |
| 4 | others | toilet | hypernym/hyponym | ✓ |
| 5 | brush | broom handle (uncertain) | mismatch | ✗ |
| 6 | carpet | broom | mismatch | ✗ |
| 7 | dustbin | toilet seat | mismatch | ✗ |
| 8 | washer | bucket | mismatch | ✗ |
| 9 | spray | pipe (uncertain) | mismatch | ✗ |
| 10 | mop | broom | semantic overlap | ✓ |
| 11 | shelf | chair | mismatch | ✗ |
| 12 | cabinet | tablecloth | mismatch | ✗ |
| 13 | door | trousers | mismatch | ✗ |
| 14 | towel | broom | mismatch | ✗ |
| 15 | adult | broom | mismatch | ✗ |
| 16 | table | tablecloth | semantic overlap | ✓ |
| 17 | chair | broom | mismatch | ✗ |
| 18 | cup | - | no label from TRASER | ✗ |
| 19 | box | arm | mismatch | ✗ |
| 20 | bike | broom | mismatch | ✗ |
| 21 | others | - | no label from TRASER | ✗ |
| 22 | table | toy (uncertain) | mismatch | ✗ |
| 23 | chair | tablecloth | mismatch | ✗ |
| 24 | bike | broom | mismatch | ✗ |
| 25 | others | broom | hypernym/hyponym | ✓ |
| 26 | chair | tablecloth | mismatch | ✗ |

**Relations: 0/8 right, triplets: 0/8 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #15 - holding - mop #10 | 0-4.8s, 10.6-187.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #15 - walking on - floor #1 | 0-17.8s, 31.4-161.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #15 - cleaning - floor #1 | 11.6-161.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #15 - holding - chair #17 | 5-10s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #15 - holding - spray #9 | 162-187.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #15 - cleaning - mop #10 | 163.6-187.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #15 - carrying - chair #17 | 5.2-9.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #15 - watering - mop #10 | 163.6-187.4s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (16): wall #2 - holding - floor #1 [62.7812-87.2812s, 88.8125-189.875s]; wall #2 - sweeping - cabinet #12 [62.7812-87.2812s, 88.8125-189.875s]; wall #2 - cleaning - cabinet #12 [62.7812-87.2812s, 88.8125-189.875s]; wall #2 - sweeping - chair #23 [62.7812-87.2812s, 88.8125-189.875s]; wall #2 - cleaning - chair #23 [62.7812-87.2812s, 88.8125-189.875s]; wall #2 - sweeping - chair #26 [62.7812-87.2812s, 88.8125-189.875s]; wall #2 - cleaning - chair #26 [62.7812-87.2812s, 88.8125-189.875s]; wall #2 - sweeping - table #16 [62.7812-87.2812s, 88.8125-189.875s]; wall #2 - cleaning - table #16 [62.7812-87.2812s, 88.8125-189.875s]; wall #2 - sweeping - shelf #11 [62.7812-65.8438s]


## 6e0a6558-c212-4cab-b374-007671edb59c_2

61.0 s, 61 frames read | human: 40 objects, 16 relations | TRASER: 39 objects, 64 relations, valid JSON, 3506 tokens

**Objects: 25/40 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | person | mismatch | ✗ |
| 2 | ceiling | ceiling fan | semantic overlap | ✓ |
| 3 | wall | refrigerator | mismatch | ✗ |
| 4 | countertop | sink | semantic overlap | ✓ |
| 5 | rack | basket | semantic overlap | ✓ |
| 6 | board | tray | semantic overlap | ✓ |
| 7 | rag | bowl (uncertain) | mismatch | ✗ |
| 8 | dustbin | cup | mismatch | ✗ |
| 9 | oven | box | mismatch | ✗ |
| 10 | stove | oven | semantic overlap | ✓ |
| 11 | sponge | sponge | identical | ✓ |
| 12 | shelf | door | mismatch | ✗ |
| 13 | window | window | identical | ✓ |
| 14 | cabinet | chair | mismatch | ✗ |
| 15 | door | mirror | mismatch | ✗ |
| 16 | fridge | refrigerator | synonym | ✓ |
| 17 | adult | hands | mismatch | ✗ |
| 18 | sink | sink | identical | ✓ |
| 19 | faucet | faucet | identical | ✓ |
| 20 | table | table | identical | ✓ |
| 21 | chair | chair | identical | ✓ |
| 22 | plate | - | no label from TRASER | ✗ |
| 23 | bottle | cup | semantic overlap | ✓ |
| 24 | cup | cup | identical | ✓ |
| 25 | paper | paper towel roll | hypernym/hyponym | ✓ |
| 26 | bag | towel | mismatch | ✗ |
| 27 | board | tray | semantic overlap | ✓ |
| 28 | dustbin | cup | mismatch | ✗ |
| 29 | sponge | sponge | identical | ✓ |
| 30 | cabinet | cabinet | identical | ✓ |
| 31 | chair | chair | identical | ✓ |
| 32 | cup | cup | identical | ✓ |
| 33 | paper | chopping board | mismatch | ✗ |
| 34 | dustbin | bucket | semantic overlap | ✓ |
| 35 | cabinet | microwave oven | mismatch | ✗ |
| 36 | chair | chair | identical | ✓ |
| 37 | cup | cup | identical | ✓ |
| 38 | paper | chopping board | mismatch | ✗ |
| 39 | cabinet | cabinet | identical | ✓ |
| 40 | cup | cup | identical | ✓ |

**Relations: 4/16 right, triplets: 0/16 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #17 - opening - faucet #19 | 0.4-1s, 38.8-39.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #17 - closing - faucet #19 | 5.4-8s, 42.2-43.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #17 - holding - cup #40 | 0-50.2s | holding (+5 more) | 0-11s, 12-23s, 36-46s | identical | 0.64 | ✓ | ✗ |
| cup #40 - on - paper #38 | 50.2-61s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #17 - walking on - floor #1 | 11.2-14s, 25.6-38.8s, 46.2-48.6s, 56.4-461s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #17 - cleaning - cup #40 | 0.6-10.2s, 38.8-45.2s | washing (+5 more) | 0-11s, 12-23s, 36-46s | synonym | 0.50 | ✓ | ✗ |
| adult #17 - holding - bottle #23 | 14-22.4s | holding (+5 more) | 12-23s, 48-52s | identical | 0.56 | ✓ | ✗ |
| adult #17 - pouring - bottle #23 | 14.8-21.2s | holding (+5 more) | 12-23s, 48-52s | semantic overlap | 0.43 | ✗ | ✗ |
| adult #17 - holding - paper #25 | 51.8-55.6s | holding (+5 more) | 52-56s | identical | 0.86 | ✓ | ✗ |
| paper #25 - on - table #20 | 0-61s | nothing for this pair | - | - | - | ✗ | ✗ |
| paper #33 - on - table #20 | 0-61s | nothing for this pair | - | - | - | ✗ | ✗ |
| paper #38 - on - table #20 | 0-61s | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #21 - on - floor #1 | 0-61s | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #21 - beside - table #20 | 0-61s | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #31 - on - floor #1 | 0-61s | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #31 - beside - table #20 | 0-61s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (46): adult #17 - holding - dustbin #8 [56-60s]; adult #17 - washing - dustbin #8 [56-60s]; adult #17 - holding - dustbin #8 [56-60s]; adult #17 - washing - dustbin #8 [56-60s]; adult #17 - holding - dustbin #8 [56-60s]; adult #17 - washing - dustbin #8 [56-60s]; adult #17 - holding - dustbin #28 [56-60s]; adult #17 - washing - dustbin #28 [56-60s]; adult #17 - holding - dustbin #28 [56-60s]; adult #17 - washing - dustbin #28 [56-60s]


## 8be918b2-c819-4a84-98dc-5fe24835a4ac

316.0 s, 128 frames read | human: 14 objects, 12 relations | TRASER: 13 objects, 0 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 7/14 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | sky | bottle | mismatch | ✗ |
| 2 | tree | person | mismatch | ✗ |
| 3 | ground | person | mismatch | ✗ |
| 4 | grass | plant | hypernym/hyponym | ✓ |
| 5 | floor | person | mismatch | ✗ |
| 6 | wall | - | no label from TRASER | ✗ |
| 7 | mat | plastic bag (uncertain) | mismatch | ✗ |
| 8 | brush | paintbrush | hypernym/hyponym | ✓ |
| 9 | stairs | person | mismatch | ✗ |
| 10 | bucket | bucket | identical | ✓ |
| 11 | fence | wooden beam | semantic overlap | ✓ |
| 12 | adult | person | hypernym/hyponym | ✓ |
| 13 | table | tablecloth | semantic overlap | ✓ |
| 14 | chair | chair | identical | ✓ |

**Relations: 0/12 right, triplets: 0/12 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #12 - holding - brush #8 | 0-93.4s, 102.6-316s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - standing on - floor #5 | 61.8-64.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - standing on - ground #3 | 281.2-316s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - brushing - fence #11 | 0-8.6s, 12-27s, 32.8-41.6s, 44.6-49.4s, 51.8-60.2s, 65.4-67.2s, 85.8-91.8s, 106.6-118.4s, 123.8-133.2s, 137.8-187s, 204.6-222.4s, 236.2-276.6s, 289.2-299.4s, 311.4-316s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - holding - bucket #10 | 71.2-78.8s, 303.2-304.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| brush #8 - in - bucket #10 | 9.4-10.6s, 103.2-105.4s, 119.8-121.2s, 134-136.2s, 195.8-200.6s, 223.2-235.2s, 277.8-279.6s, 301.2-308s | nothing for this pair | - | - | - | ✗ | ✗ |
| brush #8 - on - bucket #10 | 93.2-103s | nothing for this pair | - | - | - | ✗ | ✗ |
| ground #3 - next to - stairs #9 | 0-316s | nothing for this pair | - | - | - | ✗ | ✗ |
| stairs #9 - next to - floor #5 | 0-316s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - walking on - mat #7 | 24.4-32s, 61.2-69.6s, 282-284.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - sitting on - mat #7 | 75.6-281.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - getting down on - mat #7 | 66-69.6s | nothing for this pair | - | - | - | ✗ | ✗ |


## P01_03

118.8 s, 119 frames read | human: 70 objects, 22 relations | TRASER: 38 objects, 10 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 25/70 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | person | mismatch | ✗ |
| 2 | wall | refrigerator | mismatch | ✗ |
| 3 | switch | hand | mismatch | ✗ |
| 4 | mat | doormat | hypernym/hyponym | ✓ |
| 5 | others | - | no label from TRASER | ✗ |
| 6 | countertop | chopping board | semantic overlap | ✓ |
| 7 | grain | bowl | mismatch | ✗ |
| 8 | beverage | cup | semantic overlap | ✓ |
| 9 | microwave | microwave oven | synonym | ✓ |
| 10 | pot | bottle | mismatch | ✗ |
| 11 | plant | - | no label from TRASER | ✗ |
| 12 | cover | bottle cap | hypernym/hyponym | ✓ |
| 13 | dustbin | trash can | synonym | ✓ |
| 14 | washer | refrigerator | semantic overlap | ✓ |
| 15 | drawer | drawer | identical | ✓ |
| 16 | oven | oven | identical | ✓ |
| 17 | stove | drawer | mismatch | ✗ |
| 18 | cabinet | refrigerator | mismatch | ✗ |
| 19 | door | refrigerator | mismatch | ✗ |
| 20 | fridge | refrigerator | synonym | ✓ |
| 21 | flower | potted plant | semantic overlap | ✓ |
| 22 | glass | glass cup | hypernym/hyponym | ✓ |
| 23 | spoon | spoon | identical | ✓ |
| 24 | towel | napkin | synonym | ✓ |
| 25 | basket | drawer | semantic overlap | ✓ |
| 26 | adult | hand | mismatch | ✗ |
| 27 | sink | sink | identical | ✓ |
| 28 | sofa | sofa | identical | ✓ |
| 29 | table | table | identical | ✓ |
| 30 | chair | chair | identical | ✓ |
| 31 | bowl | lid | mismatch | ✗ |
| 32 | bottle | bottle | identical | ✓ |
| 33 | cup | cup | identical | ✓ |
| 34 | bread | plastic bag | mismatch | ✗ |
| 35 | bag | plastic bag | hypernym/hyponym | ✓ |
| 36 | box | box | identical | ✓ |
| 37 | others | bottle | hypernym/hyponym | ✓ |
| 38 | countertop | drawer | semantic overlap | ✓ |
| 39 | grain | bowl | mismatch | ✗ |
| 40 | dustbin | bottle | mismatch | ✗ |
| 41 | drawer | - | no label from TRASER | ✗ |
| 42 | oven | - | no label from TRASER | ✗ |
| 43 | cabinet | - | no label from TRASER | ✗ |
| 44 | door | - | no label from TRASER | ✗ |
| 45 | fridge | - | no label from TRASER | ✗ |
| 46 | glass | - | no label from TRASER | ✗ |
| 47 | basket | - | no label from TRASER | ✗ |
| 48 | table | - | no label from TRASER | ✗ |
| 49 | chair | - | no label from TRASER | ✗ |
| 50 | bowl | - | no label from TRASER | ✗ |
| 51 | bottle | - | no label from TRASER | ✗ |
| 52 | cup | - | no label from TRASER | ✗ |
| 53 | box | - | no label from TRASER | ✗ |
| 54 | others | - | no label from TRASER | ✗ |
| 55 | cabinet | - | no label from TRASER | ✗ |
| 56 | glass | - | no label from TRASER | ✗ |
| 57 | basket | - | no label from TRASER | ✗ |
| 58 | table | - | no label from TRASER | ✗ |
| 59 | chair | - | no label from TRASER | ✗ |
| 60 | bottle | - | no label from TRASER | ✗ |
| 61 | box | - | no label from TRASER | ✗ |
| 62 | table | - | no label from TRASER | ✗ |
| 63 | chair | - | no label from TRASER | ✗ |
| 64 | bottle | - | no label from TRASER | ✗ |
| 65 | chair | - | no label from TRASER | ✗ |
| 66 | bottle | - | no label from TRASER | ✗ |
| 67 | chair | - | no label from TRASER | ✗ |
| 68 | bottle | - | no label from TRASER | ✗ |
| 69 | bottle | - | no label from TRASER | ✗ |
| 70 | bottle | - | no label from TRASER | ✗ |

**Relations: 0/22 right, triplets: 0/22 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #26 - touching - switch #3 | 4.6-8.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - opening - fridge #20 | 11-13.6s, 69.6-71.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - holding - box #36 | 13-25.8s, 51.8-72s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - holding - bowl #50 | 14.6-18s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - holding - bowl #31 | 18.2-25.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - closing - fridge #20 | 19.2-22.6s, 72-73.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - touching - mat #4 | 28.4-43s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - holding - bottle #68 | 31.8-33.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - holding - bottle #51 | 33.4-35s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - opening - cabinet #43 | 46.4-47.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - holding - cup #33 | 48-51.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - opening - drawer #15 | 76.4-78.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - holding - spoon #23 | 78.6-82.2s, 115.2-116.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - opening - cabinet #18 | 83.4-84.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - holding - box #53 | 85-95.2s, 97.2-99s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - closing - cabinet #18 | 87.8-89.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - touching - towel #24 | 89.6-90.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - opening - box #53 | 95.2-97.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - holding - bag #35 | 97.2-99.6s, 103-115s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - opening - bag #35 | 99.6-103s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #26 - pulling - drawer #15 | 76.6-78.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| towel #24 - hanging from - cabinet #18 | 0-116.8s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (10): floor #1 - holding - bag #35 [99.8319-117.802s]; floor #1 - placing - bag #35 [117.802-119.798s]; floor #1 - pouring into - grain #39 [107.818-117.802s]; floor #1 - preparing food in - grain #39 [107.818-117.802s]; floor #1 - holding - spoon #23 [107.818-117.802s]; floor #1 - in front of - spoon #23 [107.818-117.802s]; floor #1 - holding - beverage #8 [107.818-117.802s]; floor #1 - on - mat #4 [35.9395-40.9311s, 48.9176-50.9143s, 51.9126-67.8857s, 71.879-73.8756s, 74.8739-76.8706s, 79.8655-81.8622s, 82.8605-83.8588s, 84.8571-85.8555s, 86.8538-87.8521s, 89.8487-90.8471s, 91.8454-92.8437s, 93.842-94.8403s, 95.8387-96.837s, 97.8353-98.8336s, 99.8319-100.83s, 101.829-102.827s, 103.825-104.824s, 105.822-106.82s, 107.818-108.817s, 109.815-110.813s, 111.812-112.81s, 113.808-114.807s, 115.805-116.803s, 117.802-119.798s]; floor #1 - in front of - fridge #20 [9.98319-23.9597s, 25.9563-26.9546s, 30.9479-31.9462s, 32.9445-33.9429s, 34.9412-35.9395s, 36.9378-37.9361s, 39.9328-40.9311s, 41.9294-42.9277s, 43.9261-44.9244s, 45.9227-46.921s, 47.9193-48.9176s, 49.916-50.9143s, 51.9126-52.9109s, 53.9092-54.9076s, 55.9059-56.9042s, 57.9025-58.9008s, 59.8992-60.8975s, 61.8958-62.8941s, 63.8924-64.8908s, 65.8891-66.8874s, 67.8857-68.884s, 69.8824-70.8807s, 71.879-72.8773s, 73.8756-74.8739s, 75.8723-76.8706s, 77.8689-78.8672s, 79.8655-80.8639s, 81.8622-82.8605s, 83.8588-84.8571s, 85.8555-86.8538s, 87.8521-88.8504s, 89.8487-90.8471s, 91.8454-92.8437s, 93.842-94.8403s, 95.8387-96.837s, 97.8353-98.8336s, 99.8319-100.83s, 101.829-102.827s, 103.825-104.824s, 105.822-106.82s, 107.818-108.817s, 109.815-110.813s, 111.812-112.81s, 113.808-114.807s, 115.805-116.803s, 117.802-119.798s]; floor #1 - in front of - flower #21 [35.9395-36.9378s, 37.9361-38.9345s]


## P02_10

48.8 s, 49 frames read | human: 28 objects, 5 relations | TRASER: 26 objects, 30 relations, valid JSON, 2152 tokens

**Objects: 17/28 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | doormat | semantic overlap | ✓ |
| 2 | wall | wall | identical | ✓ |
| 3 | countertop | countertop | identical | ✓ |
| 4 | simmering | mixture | mismatch | ✗ |
| 5 | rack | - | no label from TRASER | ✗ |
| 6 | spatula | wooden spoon | semantic overlap | ✓ |
| 7 | teapot | - | no label from TRASER | ✗ |
| 8 | board | chopping board | hypernym/hyponym | ✓ |
| 9 | cover | lid | synonym | ✓ |
| 10 | glove | sponge | mismatch | ✗ |
| 11 | dustbin | trash can | synonym | ✓ |
| 12 | washer | washing machine door | hypernym/hyponym | ✓ |
| 13 | oven | oven | identical | ✓ |
| 14 | stove | stove | identical | ✓ |
| 15 | pan | pan | identical | ✓ |
| 16 | sponge | bottle | mismatch | ✗ |
| 17 | cabinet | cabinet door | semantic overlap | ✓ |
| 18 | towel | towel | identical | ✓ |
| 19 | adult | hand | mismatch | ✗ |
| 20 | sink | container | hypernym/hyponym | ✓ |
| 21 | faucet | bottle | mismatch | ✗ |
| 22 | fork | handle | mismatch | ✗ |
| 23 | plate | strainer | mismatch | ✗ |
| 24 | ball | ball | identical | ✓ |
| 25 | cover | pot | mismatch | ✗ |
| 26 | glove | towel | mismatch | ✗ |
| 27 | pan | pot | synonym | ✓ |
| 28 | cabinet | cabinet door | semantic overlap | ✓ |

**Relations: 3/5 right, triplets: 0/5 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #19 - holding - spatula #6 | 2.8-46.4s | holding | 4.97959-45.8122s | identical | 0.94 | ✓ | ✗ |
| adult #19 - holding - cover #9 | 3.4-6.8s, 43.4-46s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #19 - touching - pan #15 | 6.8-43.4s | holding (+1 more) | 3.98367-45.8122s | hypernym/hyponym | 0.88 | ✓ | ✗ |
| adult #19 - in front of - stove #14 | 2.8-47.2s | above | 3.98367-46.8082s | mismatch | 0.96 | ✗ | ✗ |
| adult #19 - stirring - simmering #4 | 6-43.2s | stirring (+1 more) | 4.97959-45.8122s | identical | 0.91 | ✓ | ✗ |

TRASER relations between pairs the humans did not annotate (24): pan #15 - moving away from - stove #14 [44.8163-46.8082s]; pan #15 - on - stove #14 [3.98367-45.8122s]; stove #14 - on - countertop #3 [0-46.8082s]; simmering #4 - in - pan #15 [4.97959-45.8122s]; spatula #6 - in - pan #15 [4.97959-45.8122s]; spatula #6 - above - pan #15 [4.97959-45.8122s]; cover #9 - on - countertop #3 [0-46.8082s]; glove #10 - on - countertop #3 [0-4.97959s, 5.97551-10.9551s, 11.951-12.9469s, 13.9429-14.9388s, 15.9347-16.9306s, 17.9265-20.9143s, 21.9102-22.9061s, 23.902-24.898s, 25.8939-26.8898s, 27.8857-28.8816s, 29.8776-30.8735s, 31.8694-32.8653s, 33.8612-34.8571s, 35.8531-36.849s, 37.8449-38.8408s, 39.8367-40.8327s, 41.8286-42.8245s, 43.8204-44.8163s, 45.8122-46.8082s]; plate #23 - on - countertop #3 [0-46.8082s]; cover #25 - on - countertop #3 [4.97959-5.97551s, 15.9347-46.8082s]


## P03_06

109.2 s, 109 frames read | human: 65 objects, 20 relations | TRASER: 0 objects, 0 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 0/65 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | - | no label from TRASER | ✗ |
| 2 | wall | - | no label from TRASER | ✗ |
| 3 | cloth | - | no label from TRASER | ✗ |
| 4 | mat | - | no label from TRASER | ✗ |
| 5 | countertop | - | no label from TRASER | ✗ |
| 6 | grain | - | no label from TRASER | ✗ |
| 7 | simmering | - | no label from TRASER | ✗ |
| 8 | rack | - | no label from TRASER | ✗ |
| 9 | spatula | - | no label from TRASER | ✗ |
| 10 | chopstick | - | no label from TRASER | ✗ |
| 11 | teapot | - | no label from TRASER | ✗ |
| 12 | pot | - | no label from TRASER | ✗ |
| 13 | board | - | no label from TRASER | ✗ |
| 14 | cover | - | no label from TRASER | ✗ |
| 15 | brush | - | no label from TRASER | ✗ |
| 16 | rag | - | no label from TRASER | ✗ |
| 17 | dustbin | - | no label from TRASER | ✗ |
| 18 | washer | - | no label from TRASER | ✗ |
| 19 | drawer | - | no label from TRASER | ✗ |
| 20 | oven | - | no label from TRASER | ✗ |
| 21 | stove | - | no label from TRASER | ✗ |
| 22 | sponge | - | no label from TRASER | ✗ |
| 23 | cabinet | - | no label from TRASER | ✗ |
| 24 | door | - | no label from TRASER | ✗ |
| 25 | glass | - | no label from TRASER | ✗ |
| 26 | spoon | - | no label from TRASER | ✗ |
| 27 | towel | - | no label from TRASER | ✗ |
| 28 | basket | - | no label from TRASER | ✗ |
| 29 | adult | - | no label from TRASER | ✗ |
| 30 | sink | - | no label from TRASER | ✗ |
| 31 | faucet | - | no label from TRASER | ✗ |
| 32 | table | - | no label from TRASER | ✗ |
| 33 | knife | - | no label from TRASER | ✗ |
| 34 | fork | - | no label from TRASER | ✗ |
| 35 | plate | - | no label from TRASER | ✗ |
| 36 | bowl | - | no label from TRASER | ✗ |
| 37 | bottle | - | no label from TRASER | ✗ |
| 38 | box | - | no label from TRASER | ✗ |
| 39 | mat | - | no label from TRASER | ✗ |
| 40 | grain | - | no label from TRASER | ✗ |
| 41 | simmering | - | no label from TRASER | ✗ |
| 42 | rack | - | no label from TRASER | ✗ |
| 43 | pot | - | no label from TRASER | ✗ |
| 44 | cover | - | no label from TRASER | ✗ |
| 45 | oven | - | no label from TRASER | ✗ |
| 46 | cabinet | - | no label from TRASER | ✗ |
| 47 | glass | - | no label from TRASER | ✗ |
| 48 | spoon | - | no label from TRASER | ✗ |
| 49 | basket | - | no label from TRASER | ✗ |
| 50 | knife | - | no label from TRASER | ✗ |
| 51 | plate | - | no label from TRASER | ✗ |
| 52 | bowl | - | no label from TRASER | ✗ |
| 53 | bottle | - | no label from TRASER | ✗ |
| 54 | cup | - | no label from TRASER | ✗ |
| 55 | paper | - | no label from TRASER | ✗ |
| 56 | grain | - | no label from TRASER | ✗ |
| 57 | simmering | - | no label from TRASER | ✗ |
| 58 | pot | - | no label from TRASER | ✗ |
| 59 | basket | - | no label from TRASER | ✗ |
| 60 | knife | - | no label from TRASER | ✗ |
| 61 | plate | - | no label from TRASER | ✗ |
| 62 | bottle | - | no label from TRASER | ✗ |
| 63 | pot | - | no label from TRASER | ✗ |
| 64 | plate | - | no label from TRASER | ✗ |
| 65 | plate | - | no label from TRASER | ✗ |

**Relations: 0/20 right, triplets: 0/20 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #29 - holding - spatula #9 | 2.8-9s, 66-69s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #29 - touching - pot #12 | 3.4-8.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #29 - touching - stove #21 | 9.2-10s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #29 - holding - cover #44 | 10.2-12.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #29 - touching - pot #43 | 10.2-12.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #29 - holding - glass #25 | 13.4-13.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #29 - opening - cabinet #46 | 14.2-15s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #29 - holding - plate #65 | 15.4-19.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #29 - holding - plate #64 | 15-19.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #29 - holding - pot #43 | 20.8-23.2s, 28-62.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #29 - opening - drawer #19 | 24.6-26.6s, 101-101.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #29 - holding - spoon #26 | 26.4-97.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #29 - touching - plate #65 | 63-64.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #29 - holding - pot #12 | 69.4-99.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #29 - holding - knife #33 | 102.2-109.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #29 - holding - fork #34 | 103-109.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| rag #16 - hanging from - oven #20 | 0-109.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #29 - stirring - simmering #7 | 3.8-42.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #29 - pulling - drawer #19 | 25.2-26.4s, 101-102.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #29 - stirring - grain #6 | 28.2-35.6s | nothing for this pair | - | - | - | ✗ | ✗ |


## P04_27

104.8 s, 105 frames read | human: 34 objects, 13 relations | TRASER: 32 objects, 4 relations, cut-off answer (salvaged), 3832 tokens

**Objects: 18/34 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | bowl | mismatch | ✗ |
| 2 | wall | pot | mismatch | ✗ |
| 3 | water | bowl | mismatch | ✗ |
| 4 | countertop | chopping board | semantic overlap | ✓ |
| 5 | simmering | vegetables (uncertain) | mismatch | ✗ |
| 6 | microwave | pot | mismatch | ✗ |
| 7 | spatula | spoon | semantic overlap | ✓ |
| 8 | pot | pot | identical | ✓ |
| 9 | board | chopping board | hypernym/hyponym | ✓ |
| 10 | oven | bowl | mismatch | ✗ |
| 11 | stove | stove top | hypernym/hyponym | ✓ |
| 12 | pan | pot | synonym | ✓ |
| 13 | sponge | spatula (uncertain) | mismatch | ✗ |
| 14 | cabinet | knife | mismatch | ✗ |
| 15 | fridge | wall | mismatch | ✗ |
| 16 | spoon | bowl | mismatch | ✗ |
| 17 | towel | bowl | mismatch | ✗ |
| 18 | adult | bowl | mismatch | ✗ |
| 19 | sink | sink | identical | ✓ |
| 20 | faucet | - | no label from TRASER | ✗ |
| 21 | knife | knife | identical | ✓ |
| 22 | bowl | bowl | identical | ✓ |
| 23 | vegetable | pepper | hypernym/hyponym | ✓ |
| 24 | pot | pot | identical | ✓ |
| 25 | cabinet | pot | mismatch | ✗ |
| 26 | knife | tool (uncertain) | hypernym/hyponym | ✓ |
| 27 | vegetable | bell pepper | hypernym/hyponym | ✓ |
| 28 | pot | bowl | semantic overlap | ✓ |
| 29 | cabinet | wall panel | mismatch | ✗ |
| 30 | vegetable | tomato | hypernym/hyponym | ✓ |
| 31 | pot | - | no label from TRASER | ✗ |
| 32 | cabinet | drawer (uncertain) | semantic overlap | ✓ |
| 33 | vegetable | carrot | hypernym/hyponym | ✓ |
| 34 | vegetable | garlic clove (uncertain) | hypernym/hyponym | ✓ |

**Relations: 0/13 right, triplets: 0/13 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| vegetable #23 - on - board #9 | 0-101.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| vegetable #23 - in - simmering #5 | 102.2-104.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| vegetable #27 - on - board #9 | 0-30.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| vegetable #27 - in - simmering #5 | 33.4-104.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| simmering #5 - in - pot #28 | 0-104.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| pot #28 - on - stove #11 | 0-104.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| knife #21 - on - board #9 | 44.2-51s, 84.8-88.2s, 92.2-104.8s | on | 0-10.979s, 11.9771-12.9752s, 13.9733-14.9714s, 15.9695-16.9676s, 17.9657-18.9638s, 19.9619-20.96s, 21.9581-22.9562s, 23.9543-24.9524s, 25.9505-26.9486s, 27.9467-28.9448s, 29.9429-30.941s, 31.939-32.9371s, 33.9352-34.9333s, 35.9314-36.9295s, 37.9276-38.9257s, 39.9238-40.9219s, 41.92-42.9181s, 43.9162-44.9143s, 45.9124-46.9105s, 47.9086-48.9067s, 49.9048-50.9029s, 51.901-52.899s, 53.8971-54.8952s, 55.8933-56.8914s, 57.8895-58.8876s, 59.8857-60.8838s, 61.8819-62.88s, 63.8781-64.8762s, 65.8743-66.8724s, 67.8705-68.8686s, 69.8667-70.8648s, 71.8629-72.861s, 73.859-74.8571s, 75.8552-76.8533s, 77.8514-78.8495s, 79.8476-80.8457s, 81.8438-82.8419s, 83.84-84.8381s, 85.8362-86.8343s, 87.8324-88.8305s, 89.8286-90.8267s, 91.8248-92.8229s, 93.821-94.819s, 95.8171-96.8152s, 97.8133-98.8114s, 99.8095-100.808s, 101.806-102.804s, 103.802-104.8s, 105.798-106.796s, 107.794-108.792s | identical | 0.17 | ✗ | ✗ |
| adult #18 - holding - knife #21 | 1.6-44.2s, 50.8-84.8s, 88.4-92.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #18 - holding - vegetable #27 | 1.6-13s, 14-27.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #18 - cutting - vegetable #27 | 5.8-11.6s, 19.2-25.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #18 - holding - vegetable #23 | 34-102.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #18 - cutting - vegetable #23 | 35.4-44.2s, 51-83s, 89.6-91.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| towel #17 - hanging from - oven #10 | 0-104.8s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (3): knife #21 - in - pan #12 [12.9752-13.9733s, 14.9714-15.9695s, 16.9676-17.9657s, 18.9638-19.9619s, 20.96-21.9581s, 22.9562-23.9543s, 24.9524-25.9505s, 26.9486-27.9467s, 28.9448-29.9429s, 30.941-31.939s, 32.9371-33.9352s, 34.9333-35.9314s, 36.9295-37.9276s, 38.9257-39.9238s, 40.9219-41.92s, 42.9181-43.9162s, 44.9143-45.9124s, 46.9105-47.9086s, 48.9067-49.9048s, 50.9029-51.901s, 52.899-53.8971s, 54.8952-55.8933s, 56.8914-57.8895s, 58.8876-59.8857s, 60.8838-61.8819s, 62.88-63.8781s, 64.8762-65.8743s, 66.8724-67.8705s, 68.8686-69.8667s, 70.8648-71.8629s, 72.861-73.859s, 74.8571-75.8552s, 76.8533-77.8514s, 78.8495-79.8476s, 80.8457-81.8438s, 82.8419-83.84s, 84.8381-85.8362s, 86.8343-87.8324s, 88.8305-89.8286s, 90.8267-91.8248s, 92.8229-93.821s, 94.819-95.8171s, 96.8152-97.8133s, 98.8114-99.8095s, 100.808-101.806s, 102.804-103.802s, 104.8-105.798s, 106.796-107.794s]; knife #21 - on - countertop #4 [0-10.979s, 11.9771-12.9752s, 13.9733-14.9714s, 15.9695-16.9676s, 17.9657-18.9638s, 19.9619-20.96s, 21.9581-22.9562s, 23.9543-24.9524s, 25.9505-26.9486s, 27.9467-28.9448s, 29.9429-30.941s, 31.939-32.9371s, 33.9352-34.9333s, 35.9314-36.9295s, 37.9276-38.9257s, 39.9238-40.9219s, 41.92-42.9181s, 43.9162-44.9143s, 45.9124-46.9105s, 47.9086-48.9067s, 49.9048-50.9029s, 51.901-52.899s, 53.8971-54.8952s, 55.8933-56.8914s, 57.8895-58.8876s, 59.8857-60.8838s, 61.8819-62.88s, 63.8781-64.8762s, 65.8743-66.8724s, 67.8705-68.8686s, 69.8667-70.8648s, 71.8629-72.861s, 73.859-74.8571s, 75.8552-76.8533s, 77.8514-78.8495s, 79.8476-80.8457s, 81.8438-82.8419s, 83.84-84.8381s, 85.8362-86.8343s, 87.8324-88.8305s, 89.8286-90.8267s, 91.8248-92.8229s, 93.821-94.819s, 95.8171-96.8152s, 97.8133-98.8114s, 99.8095-100.808s, 101.806-102.804s, 103.802-104.8s, 105.798-106.796s, 107.794-108.792s]; knife #21 - in - water #3 [12.9752-13.9733s, 14.9714-15.9695s, 16.9676-17.9657s, 18.9638-19.9619s, 20.96-21.9581s, 22.9562-23.9543s, 24.9524-25.9505s, 26.9486-27.9467s, 28.9448-29.9429s, 30.941-31.939s, 32.9371-33.9352s, 34.9333-35.9314s, 36.9295-37.9276s, 38.9257-39.9238s, 40.9219-41.92s, 42.9181-43.9162s, 44.9143-45.9124s, 46.9105-47.9086s, 48.9067-49.9048s, 50.9029-51.901s, 52.899-53.8971s, 54.8952-55.8933s, 56.8914-57.8895s, 58.8876-59.8857s, 60.8838-61.8819s, 62.88-63.8781s, 64.8762-65.8743s, 66.8724-67.8705s, 68.8686-69.8667s, 70.8648-71.8629s, 72.861-73.859s, 74.8571-75.8552s, 76.8533-77.8514s, 78.8495-79.8476s, 80.8457-81.8438s, 82.8419-83.84s, 84.8381-85.8362s, 86.8343-87.8324s, 88.8305-89.8286s, 90.8267-91.8248s, 92.8229-93.821s, 94.819-95.8171s, 96.8152-97.8133s, 98.8114-99.8095s, 100.808-101.806s, 102.804-103.802s, 104.8-105.798s, 106.796-107.794s]


## P05_05

155.6 s, 128 frames read | human: 30 objects, 22 relations | TRASER: 28 objects, 322 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 17/30 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | person | mismatch | ✗ |
| 2 | wall | person | mismatch | ✗ |
| 3 | countertop | stove top | semantic overlap | ✓ |
| 4 | beverage | cup | semantic overlap | ✓ |
| 5 | cookie | cookie | identical | ✓ |
| 6 | microwave | microwave oven | synonym | ✓ |
| 7 | rack | microwave oven | mismatch | ✗ |
| 8 | cover | box (uncertain) | mismatch | ✗ |
| 9 | rag | bowl | mismatch | ✗ |
| 10 | washer | control panel (uncertain) | semantic overlap | ✓ |
| 11 | cabinet | wall | mismatch | ✗ |
| 12 | fridge | cabinet door | mismatch | ✗ |
| 13 | glass | plastic bag | mismatch | ✗ |
| 14 | adult | hand | mismatch | ✗ |
| 15 | sink | microwave oven | mismatch | ✗ |
| 16 | plate | plate | identical | ✓ |
| 17 | bowl | cup | semantic overlap | ✓ |
| 18 | bottle | pitcher | semantic overlap | ✓ |
| 19 | cup | cup | identical | ✓ |
| 20 | bag | plastic bag | hypernym/hyponym | ✓ |
| 21 | box | tray (uncertain) | semantic overlap | ✓ |
| 22 | rag | - | no label from TRASER | ✗ |
| 23 | washer | handle (uncertain) | semantic overlap | ✓ |
| 24 | cabinet | drawer | semantic overlap | ✓ |
| 25 | plate | plate | identical | ✓ |
| 26 | bottle | hand | mismatch | ✗ |
| 27 | cup | cup | identical | ✓ |
| 28 | bag | box | semantic overlap | ✓ |
| 29 | cabinet | cabinet door | semantic overlap | ✓ |
| 30 | fridge | - | no label from TRASER | ✗ |

**Relations: 2/22 right, triplets: 0/22 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #14 - holding - box #21 | 1-4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - holding - cover #8 | 1-4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - opening - cabinet #24 | 2.6-3.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - closing - cabinet #24 | 3.8-4.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - holding - cup #19 | 4.8-7.2s, 26.8-31.2s, 148-152.8s | holding (+33 more) | 150.737-154.384s | identical | 0.16 | ✗ | ✗ |
| adult #14 - opening - fridge #12 | 7.8-9.2s, 13.4-14.4s, 64.6-66.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - holding - bottle #26 | 9.6-25.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - touching - cup #19 | 15.4-17.2s | holding (+33 more) | 14.5875-20.6656s | hypernym/hyponym | 0.30 | ✗ | ✗ |
| adult #14 - opening - microwave #6 | 27.6-29s, 143.8-146.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - closing - microwave #6 | 31.4-32.6s, 149.2-151s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - touching - microwave #6 | 34.2-34.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - holding - bag #20 | 37-45.8s | holding (+30 more) | 37.6844-44.9781s | identical | 0.83 | ✓ | ✗ |
| adult #14 - holding - bag #28 | 37-66.4s | holding (+32 more) | 42.5469-59.5656s | identical | 0.58 | ✓ | ✗ |
| adult #14 - closing - fridge #12 | 46.6-47.4s, 66.6-67.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #14 - picking - plate #25 | 51.2-53.2s | holding (+31 more) | 150.737-154.384s | semantic overlap | 0.00 | ✗ | ✗ |
| adult #14 - opening - bag #28 | 54-57.6s | holding (+32 more) | 42.5469-59.5656s | mismatch | 0.21 | ✗ | ✗ |
| adult #14 - holding - cookie #5 | 60.4-61.6s | holding (+31 more) | 72.9375-80.2313s | identical | 0.00 | ✗ | ✗ |
| adult #14 - holding - glass #13 | 71.4-80.2s | holding (+30 more) | 150.737-154.384s | identical | 0.00 | ✗ | ✗ |
| adult #14 - holding - bottle #18 | 72.2-80.4s | holding (+30 more) | 66.8594-69.2906s | identical | 0.00 | ✗ | ✗ |
| cookie #5 - on - plate #25 | 61.8-155.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| cup #19 - on - countertop #3 | 6.8-27.4s, 153-155.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| cup #19 - entering - microwave #6 | 29.4-30.4s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (98): adult #14 - holding - beverage #4 [14.5875-20.6656s]; adult #14 - holding - plate #16 [150.737-154.384s]; adult #14 - holding - plate #16 [150.737-154.384s]; adult #14 - holding - plate #16 [150.737-154.384s]; adult #14 - holding - plate #16 [150.737-154.384s]; adult #14 - holding - plate #16 [150.737-154.384s]; adult #14 - holding - plate #16 [150.737-154.384s]; adult #14 - holding - plate #16 [150.737-154.384s]; adult #14 - holding - plate #16 [150.737-154.384s]; adult #14 - holding - plate #16 [150.737-154.384s]


## P08_07

24.0 s, 24 frames read | human: 26 objects, 10 relations | TRASER: 25 objects, 38 relations, valid JSON, 2216 tokens

**Objects: 19/26 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | floor | identical | ✓ |
| 2 | wall | wall | identical | ✓ |
| 3 | countertop | stove top | semantic overlap | ✓ |
| 4 | beverage | cup | semantic overlap | ✓ |
| 5 | can | bowl (uncertain) | mismatch | ✗ |
| 6 | teapot | faucet | mismatch | ✗ |
| 7 | board | - | no label from TRASER | ✗ |
| 8 | glove | towel | mismatch | ✗ |
| 9 | dustbin | trash can | synonym | ✓ |
| 10 | oven | oven | identical | ✓ |
| 11 | stove | stove | identical | ✓ |
| 12 | cabinet | countertop | semantic overlap | ✓ |
| 13 | glass | glass cup | hypernym/hyponym | ✓ |
| 14 | book | paper (uncertain) | semantic overlap | ✓ |
| 15 | towel | towel | identical | ✓ |
| 16 | adult | hands | mismatch | ✗ |
| 17 | sink | sink | identical | ✓ |
| 18 | faucet | faucet | identical | ✓ |
| 19 | bottle | bottle | identical | ✓ |
| 20 | cellphone | cellular telephone (uncertain) | synonym | ✓ |
| 21 | dustbin | trash can (uncertain) | synonym | ✓ |
| 22 | stove | knob (uncertain) | mismatch | ✗ |
| 23 | cabinet | cabinet door | semantic overlap | ✓ |
| 24 | cabinet | cabinet door | semantic overlap | ✓ |
| 25 | cabinet | sink | mismatch | ✗ |
| 26 | cabinet | cabinet door | semantic overlap | ✓ |

**Relations: 2/10 right, triplets: 0/10 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #16 - holding - bottle #19 | 2.4-3.6s, 7.4-17.8s | hold | 3-17s | identical | 0.66 | ✓ | ✗ |
| adult #16 - holding - glass #13 | 6-7.8s, 18.4-21.4s | hold (+3 more) | 8-16s | identical | 0.00 | ✗ | ✗ |
| adult #16 - opening - bottle #19 | 8.6-9.8s | hold | 3-17s | mismatch | 0.09 | ✗ | ✗ |
| adult #16 - closing - bottle #19 | 16-17.6s | hold | 3-17s | mismatch | 0.07 | ✗ | ✗ |
| beverage #4 - in - glass #13 | 12.6-23.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| bottle #19 - on - countertop #3 | 3.2-8.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| glass #13 - on - countertop #3 | 7.6-18.6s, 21-24s | nothing for this pair | - | - | - | ✗ | ✗ |
| towel #15 - hanging from - oven #10 | 0-24s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #16 - carrying - glass #13 | 18.8-21s | hold (+3 more) | 8-16s | hypernym/hyponym | 0.00 | ✗ | ✗ |
| teapot #6 - over - stove #11 | 0-24s | above | 0-24s | synonym | 1.00 | ✓ | ✗ |

TRASER relations between pairs the humans did not annotate (32): adult #16 - hold - beverage #4 [16-18s]; adult #16 - place - beverage #4 [16-18s]; adult #16 - hold - towel #15 [19-22s]; adult #16 - wipe - stove #11 [19-22s]; adult #16 - clean stove - stove #11 [19-22s]; adult #16 - above - stove #11 [3-24s]; adult #16 - wipe - countertop #3 [22-24s]; adult #16 - clean countertop - countertop #3 [22-24s]; adult #16 - above - countertop #3 [3-24s]; countertop #3 - on - stove #11 [0-24s]


## P09_07

55.2 s, 55 frames read | human: 29 objects, 15 relations | TRASER: 27 objects, 72 relations, valid JSON, 7106 tokens

**Objects: 15/29 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | hand | mismatch | ✗ |
| 2 | wall | wall | identical | ✓ |
| 3 | countertop | table | semantic overlap | ✓ |
| 4 | microwave | cabinet door | semantic overlap | ✓ |
| 5 | pot | bottle | mismatch | ✗ |
| 6 | cover | lid (uncertain) | synonym | ✓ |
| 7 | stove | handle (uncertain) | mismatch | ✗ |
| 8 | shelf | bottle | mismatch | ✗ |
| 9 | cabinet | drawer | semantic overlap | ✓ |
| 10 | spoon | scissors | mismatch | ✗ |
| 11 | scissor | scissors | identical | ✓ |
| 12 | adult | hand | mismatch | ✗ |
| 13 | sink | bowl | mismatch | ✗ |
| 14 | knife | knife | identical | ✓ |
| 15 | bottle | cup | semantic overlap | ✓ |
| 16 | paper | paper (uncertain) | identical | ✓ |
| 17 | box | paper (uncertain) | mismatch | ✗ |
| 18 | cover | bowl | mismatch | ✗ |
| 19 | cabinet | drawer | semantic overlap | ✓ |
| 20 | spoon | lid (uncertain) | mismatch | ✗ |
| 21 | knife | knife | identical | ✓ |
| 22 | bottle | - | no label from TRASER | ✗ |
| 23 | powder | cup | mismatch | ✗ |
| 24 | cover | bowl | mismatch | ✗ |
| 25 | cabinet | shelf (uncertain) | semantic overlap | ✓ |
| 26 | spoon | - | no label from TRASER | ✗ |
| 27 | bottle | cup | semantic overlap | ✓ |
| 28 | cover | lid (uncertain) | synonym | ✓ |
| 29 | bottle | lid (uncertain) | semantic overlap | ✓ |

**Relations: 1/15 right, triplets: 0/15 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #12 - holding - bottle #15 | 1.6-5s, 48.6-53.4s | holding (+2 more) | 51.1855-55.2s | identical | 0.22 | ✗ | ✗ |
| adult #12 - opening - bottle #15 | 2.4-4.2s | holding (+2 more) | 16.0582-27.0982s, 33.12-45.1636s | mismatch | 0.00 | ✗ | ✗ |
| adult #12 - holding - cover #6 | 4.2-5s, 48-52.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - opening - cabinet #9 | 5.8-7s, 44.6-45.6s | in front of | 0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s | mismatch | 0.02 | ✗ | ✗ |
| adult #12 - holding - bottle #27 | 7.6-9.8s, 12.4-30.2s | holding (+3 more) | 16.0582-27.0982s, 33.12-45.1636s | identical | 0.34 | ✗ | ✗ |
| adult #12 - holding - bottle #29 | 10.6-12.2s, 32.2-46.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - opening - bottle #27 | 12.4-15.2s | holding (+3 more) | 16.0582-27.0982s, 33.12-45.1636s | mismatch | 0.00 | ✗ | ✗ |
| adult #12 - holding - cover #18 | 14.6-25.4s | holding | 16.0582-27.0982s | identical | 0.75 | ✓ | ✗ |
| adult #12 - holding - spoon #20 | 16.4-25.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - closing - bottle #27 | 25.6-27.6s | holding (+3 more) | 16.0582-27.0982s, 33.12-45.1636s | mismatch | 0.06 | ✗ | ✗ |
| adult #12 - closing - cabinet #9 | 30.6-31.8s, 46.4-47.2s | in front of | 0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s | mismatch | 0.03 | ✗ | ✗ |
| adult #12 - opening - bottle #29 | 32.4-34.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - holding - cover #28 | 33.8-34.6s, 39.4-40.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - closing - bottle #29 | 40.2-43.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #12 - closing - bottle #15 | 48-52.6s | holding (+2 more) | 51.1855-55.2s | mismatch | 0.20 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (63): adult #12 - holding - spoon #10 [35.1273-45.1636s]; adult #12 - cutting - spoon #10 [35.1273-45.1636s]; adult #12 - in front of - spoon #10 [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s]; adult #12 - holding - powder #23 [16.0582-27.0982s]; adult #12 - holding - cover #24 [16.0582-27.0982s]; adult #12 - holding - knife #14 [51.1855-55.2s]; adult #12 - in front of - knife #14 [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s]; adult #12 - in front of - knife #14 [0-2.00727s, 3.01091-4.01455s, 5.01818-6.02182s, 7.02545-8.02909s, 10.0364-11.04s, 12.0436-13.0473s, 14.0509-15.0545s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s]; adult #12 - above - countertop #3 [0-55.2s]; floor #1 - above - countertop #3 [0-2.00727s, 4.01455-11.04s, 16.0582-17.0618s, 18.0655-27.0982s, 28.1018-29.1055s, 30.1091-31.1127s, 32.1164-33.12s, 34.1236-35.1273s, 36.1309-37.1345s, 38.1382-45.1636s, 46.1673-47.1709s, 48.1745-49.1782s, 50.1818-51.1855s, 52.1891-55.2s]


## P11_11

66.4 s, 66 frames read | human: 44 objects, 15 relations | TRASER: 35 objects, 26 relations, valid JSON, 3815 tokens

**Objects: 20/44 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | - | no label from TRASER | ✗ |
| 2 | wall | cabinet door | mismatch | ✗ |
| 3 | mat | countertop | mismatch | ✗ |
| 4 | others | kettle | mismatch | ✗ |
| 5 | countertop | countertop | identical | ✓ |
| 6 | pizza | pizza | identical | ✓ |
| 7 | microwave | microwave oven | synonym | ✓ |
| 8 | rack | oven | mismatch | ✗ |
| 9 | can | - | no label from TRASER | ✗ |
| 10 | pot | - | no label from TRASER | ✗ |
| 11 | brush | hose | mismatch | ✗ |
| 12 | rag | handle (uncertain) | mismatch | ✗ |
| 13 | glove | - | no label from TRASER | ✗ |
| 14 | dustbin | cup | mismatch | ✗ |
| 15 | washer | washing machine | synonym | ✓ |
| 16 | oven | oven | identical | ✓ |
| 17 | stove | stove top | hypernym/hyponym | ✓ |
| 18 | sponge | sponge | identical | ✓ |
| 19 | window | cabinet door | mismatch | ✗ |
| 20 | cabinet | cabinet door | semantic overlap | ✓ |
| 21 | fridge | dishwasher rack | mismatch | ✗ |
| 22 | scissor | scissors | identical | ✓ |
| 23 | towel | towel | identical | ✓ |
| 24 | adult | arm | mismatch | ✗ |
| 25 | sink | sink | identical | ✓ |
| 26 | faucet | faucet | identical | ✓ |
| 27 | sofa | cabinet door | mismatch | ✗ |
| 28 | table | cabinet door | mismatch | ✗ |
| 29 | chair | - | no label from TRASER | ✗ |
| 30 | plate | plate | identical | ✓ |
| 31 | bowl | bowl | identical | ✓ |
| 32 | cup | cup | identical | ✓ |
| 33 | paper | handle (uncertain) | mismatch | ✗ |
| 34 | box | box | identical | ✓ |
| 35 | countertop | sink | semantic overlap | ✓ |
| 36 | cabinet | cabinet door | semantic overlap | ✓ |
| 37 | plate | plates | identical | ✓ |
| 38 | bowl | bowl | identical | ✓ |
| 39 | cup | plate | mismatch | ✗ |
| 40 | box | cup | mismatch | ✗ |
| 41 | cabinet | - | no label from TRASER | ✗ |
| 42 | plate | - | no label from TRASER | ✗ |
| 43 | box | - | no label from TRASER | ✗ |
| 44 | cabinet | - | no label from TRASER | ✗ |

**Relations: 2/15 right, triplets: 0/15 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #24 - opening - cabinet #44 | 2.6-5.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #24 - holding - plate #30 | 5.6-9s | holding | 26.1576-42.2545s | identical | 0.00 | ✗ | ✗ |
| adult #24 - opening - oven #16 | 10-11s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #24 - holding - towel #23 | 10-21s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #24 - holding - rack #8 | 13.4-18.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #24 - closing - oven #16 | 18.4-19.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #24 - holding - scissor #22 | 22.6-60.6s | holding | 26.1576-60.3636s | identical | 0.90 | ✓ | ✗ |
| adult #24 - cutting - pizza #6 | 26.4-39.4s | cutting (+3 more) | 26.1576-42.2545s | identical | 0.81 | ✓ | ✗ |
| adult #24 - closing - cabinet #44 | 42.6-43.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #24 - touching - faucet #26 | 44-47.6s, 51.6-52.2s, 55.2-55.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #24 - cleaning - scissor #22 | 44.4-56.6s | holding | 26.1576-60.3636s | mismatch | 0.36 | ✗ | ✗ |
| adult #24 - holding - sponge #18 | 47.6-51.8s | holding | 56.3394-60.3636s | identical | 0.00 | ✗ | ✗ |
| pizza #6 - on - rack #8 | 13.4-16s | nothing for this pair | - | - | - | ✗ | ✗ |
| pizza #6 - on - plate #30 | 15.6-66.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| towel #23 - hanging from - oven #16 | 0-10.6s, 20.4-66.4s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (19): pizza #6 - moving toward - sink #25 [41.2485-43.2606s]; adult #24 - holding - cup #32 [56.3394-60.3636s]; adult #24 - holding - bowl #31 [56.3394-60.3636s]; adult #24 - washing dishes - sink #25 [56.3394-60.3636s]; mat #3 - in front of - countertop #5 [0-25.1515s, 26.1576-42.2545s, 43.2606-60.3636s, 61.3697-67.4061s]; sink #25 - in - mat #3 [0-5.0303s, 6.03636-7.04242s, 8.04848-9.05455s, 10.0606-11.0667s, 12.0727-13.0788s, 14.0848-15.0909s, 16.097-17.103s, 18.1091-19.1152s, 20.1212-21.1273s, 22.1333-23.1394s, 24.1455-25.1515s, 26.1576-42.2545s, 43.2606-60.3636s, 61.3697-67.4061s]; faucet #26 - above - sink #25 [0-5.0303s, 6.03636-7.04242s, 8.04848-9.05455s, 10.0606-11.0667s, 12.0727-13.0788s, 14.0848-15.0909s, 16.097-17.103s, 18.1091-19.1152s, 20.1212-21.1273s, 22.1333-23.1394s, 24.1455-25.1515s, 26.1576-42.2545s, 43.2606-60.3636s, 61.3697-67.4061s]; stove #17 - on - countertop #5 [0-5.0303s, 6.03636-7.04242s, 8.04848-9.05455s, 10.0606-11.0667s, 12.0727-13.0788s, 14.0848-15.0909s, 16.097-17.103s, 18.1091-19.1152s, 20.1212-21.1273s, 22.1333-23.1394s, 24.1455-25.1515s, 26.1576-42.2545s, 43.2606-60.3636s, 61.3697-67.4061s]; faucet #26 - attached to - stove #17 [0-5.0303s, 6.03636-7.04242s, 8.04848-9.05455s, 10.0606-11.0667s, 12.0727-13.0788s, 14.0848-15.0909s, 16.097-17.103s, 18.1091-19.1152s, 20.1212-21.1273s, 22.1333-23.1394s, 24.1455-25.1515s, 26.1576-42.2545s, 43.2606-60.3636s, 61.3697-67.4061s]; faucet #26 - above - stove #17 [0-5.0303s, 6.03636-7.04242s, 8.04848-9.05455s, 10.0606-11.0667s, 12.0727-13.0788s, 14.0848-15.0909s, 16.097-17.103s, 18.1091-19.1152s, 20.1212-21.1273s, 22.1333-23.1394s, 24.1455-25.1515s, 26.1576-42.2545s, 43.2606-60.3636s, 61.3697-67.4061s]


## P14_06

64.6 s, 65 frames read | human: 34 objects, 10 relations | TRASER: 34 objects, 203 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 24/34 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | person | mismatch | ✗ |
| 2 | wall | wall | identical | ✓ |
| 3 | countertop | countertop | identical | ✓ |
| 4 | grain | bowl | mismatch | ✗ |
| 5 | beverage | box | mismatch | ✗ |
| 6 | rack | dish rack | hypernym/hyponym | ✓ |
| 7 | cover | plate (uncertain) | semantic overlap | ✓ |
| 8 | carpet | doormat | hypernym/hyponym | ✓ |
| 9 | dustbin | plastic bag | mismatch | ✗ |
| 10 | stairs | drawer front (uncertain) | mismatch | ✗ |
| 11 | sponge | sponge | identical | ✓ |
| 12 | shelf | shelf | identical | ✓ |
| 13 | window | pipe (uncertain) | mismatch | ✗ |
| 14 | cabinet | sink | mismatch | ✗ |
| 15 | door | cabinet door | hypernym/hyponym | ✓ |
| 16 | fridge | refrigerator | synonym | ✓ |
| 17 | spoon | knife | mismatch | ✗ |
| 18 | scissor | scissors | identical | ✓ |
| 19 | adult | arm | mismatch | ✗ |
| 20 | sink | sink | identical | ✓ |
| 21 | faucet | faucet | identical | ✓ |
| 22 | table | countertop | semantic overlap | ✓ |
| 23 | knife | knife | identical | ✓ |
| 24 | plate | plate | identical | ✓ |
| 25 | bowl | plate | semantic overlap | ✓ |
| 26 | cup | cup | identical | ✓ |
| 27 | paper | paper (uncertain) | identical | ✓ |
| 28 | box | box | identical | ✓ |
| 29 | beverage | bowl | mismatch | ✗ |
| 30 | cabinet | cabinet door | semantic overlap | ✓ |
| 31 | door | cabinet door | hypernym/hyponym | ✓ |
| 32 | plate | plate | identical | ✓ |
| 33 | bowl | bowl | identical | ✓ |
| 34 | bowl | plate | semantic overlap | ✓ |

**Relations: 0/10 right, triplets: 0/10 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #19 - holding - bowl #33 | 4.2-9s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #19 - opening - fridge #16 | 10.4-12s, 35.8-38.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #19 - holding - beverage #5 | 13.2-40.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #19 - closing - fridge #16 | 13.8-15.2s, 41.6-43s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #19 - opening - beverage #5 | 17.8-19.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #19 - touching - bowl #33 | 21-21.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #19 - holding - box #28 | 45.6-57.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #19 - holding - spoon #17 | 60.2-64.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| beverage #5 - on - table #22 | 17.8-19.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| bowl #33 - on - table #22 | 9-64.6s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (203): floor #1 - holding - beverage #5 [17.8892-36.7723s]; floor #1 - placing - beverage #5 [35.7785-37.7662s]; floor #1 - in front of - beverage #5 [17.8892-36.7723s]; floor #1 - in front of - beverage #5 [17.8892-36.7723s]; floor #1 - in front of - beverage #5 [17.8892-36.7723s]; floor #1 - in front of - beverage #5 [17.8892-36.7723s]; floor #1 - in front of - beverage #5 [17.8892-36.7723s]; floor #1 - in front of - beverage #5 [17.8892-36.7723s]; floor #1 - holding - box #28 [46.7108-57.6431s]; floor #1 - placing - box #28 [57.6431-61.6185s]


## P19_06

233.6 s, 128 frames read | human: 42 objects, 13 relations | TRASER: 35 objects, 14 relations, valid JSON, 2144 tokens

**Objects: 17/42 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | stove top | mismatch | ✗ |
| 2 | wall | wall | identical | ✓ |
| 3 | egg | egg | identical | ✓ |
| 4 | others | vent (uncertain) | hypernym/hyponym | ✓ |
| 5 | countertop | pot | mismatch | ✗ |
| 6 | meat | fish | semantic overlap | ✓ |
| 7 | microwave | pot | mismatch | ✗ |
| 8 | spatula | spatula | identical | ✓ |
| 9 | pot | frying pan | semantic overlap | ✓ |
| 10 | board | sink | mismatch | ✗ |
| 11 | dustbin | bottle | mismatch | ✗ |
| 12 | oven | stove top | semantic overlap | ✓ |
| 13 | stove | stove | identical | ✓ |
| 14 | pan | stove top | mismatch | ✗ |
| 15 | cabinet | stove top | mismatch | ✗ |
| 16 | door | stove top | mismatch | ✗ |
| 17 | fridge | stove top | mismatch | ✗ |
| 18 | adult | stove top | mismatch | ✗ |
| 19 | sink | stove top | mismatch | ✗ |
| 20 | faucet | faucet | identical | ✓ |
| 21 | knife | tray | mismatch | ✗ |
| 22 | bottle | handle (uncertain) | mismatch | ✗ |
| 23 | paper | - | no label from TRASER | ✗ |
| 24 | box | tray | semantic overlap | ✓ |
| 25 | cellphone | cell phone | identical | ✓ |
| 26 | egg | egg | identical | ✓ |
| 27 | others | knob (uncertain) | hypernym/hyponym | ✓ |
| 28 | countertop | stove top | semantic overlap | ✓ |
| 29 | spatula | - | no label from TRASER | ✗ |
| 30 | pot | pot | identical | ✓ |
| 31 | oven | bottle | mismatch | ✗ |
| 32 | stove | - | no label from TRASER | ✗ |
| 33 | cabinet | stove top | mismatch | ✗ |
| 34 | fridge | - | no label from TRASER | ✗ |
| 35 | box | tray | semantic overlap | ✓ |
| 36 | countertop | bowl | mismatch | ✗ |
| 37 | pan | - | no label from TRASER | ✗ |
| 38 | cabinet | stove top | mismatch | ✗ |
| 39 | countertop | stove top | semantic overlap | ✓ |
| 40 | cabinet | wall | mismatch | ✗ |
| 41 | fridge | - | no label from TRASER | ✗ |
| 42 | cabinet | - | no label from TRASER | ✗ |

**Relations: 0/13 right, triplets: 0/13 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #18 - opening - stove #13 | 4.2-6.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #18 - holding - pan #14 | 6.6-10.4s, 54.6-91s, 92.4-94.4s, 109.8-199.6s, 205-207.8s, 212.2-217.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #18 - opening - fridge #17 | 13.8-14.2s, 41.8-43.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #18 - closing - fridge #17 | 21.8-23.2s, 44.2-45.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #18 - holding - box #35 | 14.2-19.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #18 - holding - egg #3 | 17-26s, 91.4-106.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #18 - holding - box #24 | 19.6-44s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #18 - opening - box #24 | 28.2-37.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #18 - holding - meat #6 | 37.4-39s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #18 - holding - spatula #8 | 50.6-91s, 109.8-213.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #18 - cooking - meat #6 | 55-90.8s, 173.6-174.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #18 - cooking - egg #26 | 115.8-173s, 175-199.8s, 204.4-207.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #18 - closing - stove #13 | 207.8-211.6s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (14): spatula #8 - moves toward - egg #26 [100.375-111.325s]; spatula #8 - moves away from - egg #26 [198.925-213.525s]; spatula #8 - cooks - egg #26 [100.375-213.525s]; spatula #8 - over - egg #26 [100.375-213.525s]; spatula #8 - moves over - stove #13 [100.375-213.525s]; spatula #8 - moves over - stove #13 [198.925-220.825s]; spatula #8 - moves toward - meat #6 [198.925-213.525s]; spatula #8 - moves away from - meat #6 [213.525-220.825s]; spatula #8 - cooks - meat #6 [198.925-220.825s]; spatula #8 - over - meat #6 [198.925-220.825s]


## P28_19

90.0 s, 90 frames read | human: 28 objects, 10 relations | TRASER: 27 objects, 18 relations, valid JSON, 1872 tokens

**Objects: 17/28 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | chopping board | mismatch | ✗ |
| 2 | wall | countertop | mismatch | ✗ |
| 3 | egg | tomato | mismatch | ✗ |
| 4 | others | tortilla (uncertain) | hypernym/hyponym | ✓ |
| 5 | countertop | countertop | identical | ✓ |
| 6 | spatula | spatula | identical | ✓ |
| 7 | board | chopping board | hypernym/hyponym | ✓ |
| 8 | rag | chair | mismatch | ✗ |
| 9 | dustbin | pot | mismatch | ✗ |
| 10 | oven | cabinet door | mismatch | ✗ |
| 11 | stove | stove top | hypernym/hyponym | ✓ |
| 12 | pan | frying pan | hypernym/hyponym | ✓ |
| 13 | window | tray | mismatch | ✗ |
| 14 | cabinet | drawer front | semantic overlap | ✓ |
| 15 | door | cabinet door | hypernym/hyponym | ✓ |
| 16 | adult | arm | mismatch | ✗ |
| 17 | sink | sink | identical | ✓ |
| 18 | knife | spoon | semantic overlap | ✓ |
| 19 | plate | tray | semantic overlap | ✓ |
| 20 | bottle | bottle | identical | ✓ |
| 21 | bag | aluminum foil | mismatch | ✗ |
| 22 | box | box | identical | ✓ |
| 23 | countertop | countertop | identical | ✓ |
| 24 | window | - | no label from TRASER | ✗ |
| 25 | cabinet | cabinet door | semantic overlap | ✓ |
| 26 | vegetable | onions | hypernym/hyponym | ✓ |
| 27 | bag | napkin | mismatch | ✗ |
| 28 | box | bag | semantic overlap | ✓ |

**Relations: 3/10 right, triplets: 0/10 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #16 - holding - knife #18 | 1.4-43.2s | holding | 41-43s | identical | 0.05 | ✗ | ✗ |
| adult #16 - holding - vegetable #26 | 1.4-42s | cutting (+1 more) | 3-43s | mismatch | 0.94 | ✗ | ✗ |
| adult #16 - cutting - vegetable #26 | 2.8-39.6s | cutting (+1 more) | 3-43s | identical | 0.91 | ✓ | ✗ |
| adult #16 - holding - bottle #20 | 43-52.4s | holding (+1 more) | 44-51s | identical | 0.74 | ✓ | ✗ |
| adult #16 - opening - bottle #20 | 45-46.2s | holding (+1 more) | 44-51s | mismatch | 0.17 | ✗ | ✗ |
| adult #16 - holding - box #22 | 53.2-59.2s | holding (+1 more) | 52-57s | identical | 0.53 | ✓ | ✗ |
| adult #16 - touching - stove #11 | 60.4-70.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #16 - swinging - pan #12 | 71.2-79.4s | stirring (+6 more) | 72-89s | mismatch | 0.42 | ✗ | ✗ |
| adult #16 - holding - pan #12 | 82.6-83.8s | holding (+6 more) | 45-51s, 72-89s | identical | 0.05 | ✗ | ✗ |
| adult #16 - over - pan #12 | 84.2-88s | serving onto (+6 more) | 72-89s | semantic overlap | 0.22 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (4): adult #16 - holding - spatula #6 [41-43s]; adult #16 - holding - box #28 [89-91s]; adult #16 - holding - box #28 [89-91s]; adult #16 - holding - window #13 [52-57s]


## c20407ac-83d6-4c84-88cb-63bced9d456b

52.8 s, 53 frames read | human: 11 objects, 12 relations | TRASER: 11 objects, 23 relations, valid JSON, 953 tokens

**Objects: 6/11 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | sky | soccer ball | mismatch | ✗ |
| 2 | grass | soccer ball | mismatch | ✗ |
| 3 | adult | person | hypernym/hyponym | ✓ |
| 4 | ball | sports ball (uncertain) | hypernym/hyponym | ✓ |
| 5 | adult | person | hypernym/hyponym | ✓ |
| 6 | adult | person | hypernym/hyponym | ✓ |
| 7 | adult | shoe | mismatch | ✗ |
| 8 | adult | person | hypernym/hyponym | ✓ |
| 9 | adult | person | hypernym/hyponym | ✓ |
| 10 | adult | sports ball (uncertain) | mismatch | ✗ |
| 11 | adult | sports ball (uncertain) | mismatch | ✗ |

**Relations: 0/12 right, triplets: 0/12 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #3 - running on - grass #2 | 0-52.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - running on - grass #2 | 0-52.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #6 - running on - grass #2 | 0-52.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - running on - grass #2 | 0-52.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - running on - grass #2 | 0-52.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - running on - grass #2 | 0-52.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - running on - grass #2 | 0-52.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #11 - running on - grass #2 | 0-52.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #3 - kicking - ball #4 | 0-1.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #7 - kicking - ball #4 | 4.4-5.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #8 - kicking - ball #4 | 15.6-16.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #6 - kicking - ball #4 | 15.8-20.8s, 24.4-25s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (23): adult #5 - approaches - adult #6 [0.996226-3.98491s]; adult #5 - moves away from - adult #6 [2.98868-4.98113s]; adult #5 - in front of - adult #6 [0.996226-4.98113s, 13.9472-16.9358s]; adult #5 - approaches - adult #8 [13.9472-15.9396s]; adult #5 - moves away from - adult #8 [14.9434-16.9358s]; adult #5 - in front of - adult #8 [13.9472-16.9358s]; adult #3 - approaches - adult #5 [21.917-23.9094s]; adult #3 - moves away from - adult #5 [22.9132-24.9057s]; adult #3 - in front of - adult #5 [21.917-23.9094s]; adult #3 - approaches - adult #8 [23.9094-25.9019s]


## c2e6d807-d903-4b64-98e1-2c07ca700c78_2

126.0 s, 126 frames read | human: 41 objects, 16 relations | TRASER: 39 objects, 281 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 24/41 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | person | mismatch | ✗ |
| 2 | wall | person | mismatch | ✗ |
| 3 | countertop | sink | semantic overlap | ✓ |
| 4 | teapot | cup | semantic overlap | ✓ |
| 5 | rag | plastic bag (uncertain) | mismatch | ✗ |
| 6 | glove | hand | semantic overlap | ✓ |
| 7 | carpet | cushion | mismatch | ✗ |
| 8 | dustbin | bottle | mismatch | ✗ |
| 9 | oven | chair | mismatch | ✗ |
| 10 | stove | stove | identical | ✓ |
| 11 | sponge | glass cup | mismatch | ✗ |
| 12 | window | - | no label from TRASER | ✗ |
| 13 | cabinet | person | mismatch | ✗ |
| 14 | door | person | mismatch | ✗ |
| 15 | fridge | chair | mismatch | ✗ |
| 16 | adult | arm | mismatch | ✗ |
| 17 | sink | sink | identical | ✓ |
| 18 | faucet | faucet | identical | ✓ |
| 19 | table | tablecloth | semantic overlap | ✓ |
| 20 | chair | chair | identical | ✓ |
| 21 | plate | plate | identical | ✓ |
| 22 | bowl | glass cup | semantic overlap | ✓ |
| 23 | bottle | bowl | semantic overlap | ✓ |
| 24 | bag | chair | mismatch | ✗ |
| 25 | cabinet | chair | mismatch | ✗ |
| 26 | door | person | mismatch | ✗ |
| 27 | table | tablecloth | semantic overlap | ✓ |
| 28 | chair | chair | identical | ✓ |
| 29 | plate | plates | identical | ✓ |
| 30 | bowl | bowl | identical | ✓ |
| 31 | chair | chair | identical | ✓ |
| 32 | plate | plate | identical | ✓ |
| 33 | cabinet | cabinet door | semantic overlap | ✓ |
| 34 | chair | chair | identical | ✓ |
| 35 | cabinet | table | mismatch | ✗ |
| 36 | chair | chair | identical | ✓ |
| 37 | chair | chair | identical | ✓ |
| 38 | chair | chair | identical | ✓ |
| 39 | chair | chair | identical | ✓ |
| 40 | chair | chair | identical | ✓ |
| 41 | chair | - | no label from TRASER | ✗ |

**Relations: 0/16 right, triplets: 0/16 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #16 - on - floor #1 | 0-125.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #16 - holding - bowl #22 | 3.6-13.8s, 15.8-25s, 47.2-64.8s, 104.2-125.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #16 - opening - faucet #18 | 14-15.2s, 33.6-34.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #16 - closing - faucet #18 | 58.4-59.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #16 - holding - bowl #30 | 25.6-46.4s, 104.2-125.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #16 - cleaning - bowl #22 | 15.8-25s, 47.8-61.8s, 84.8-104s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #16 - cleaning - bowl #30 | 27.4-44.4s, 64.8-83.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #16 - holding - rag #5 | 64.4-104.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #16 - holding - sponge #11 | 13.2-33.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #16 - walking on - floor #1 | 108-125.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #16 - beside - sink #17 | 10-62.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| bowl #22 - on - table #19 | 123.6-126s | nothing for this pair | - | - | - | ✗ | ✗ |
| bowl #30 - on - table #19 | 123.6-126s | nothing for this pair | - | - | - | ✗ | ✗ |
| bowl #22 - on - table #27 | 63.4-114s | nothing for this pair | - | - | - | ✗ | ✗ |
| bowl #30 - on - table #27 | 46.2-114s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #16 - entering - door #26 | 6.6-8s, 117.2-118.4s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (281): floor #1 - holding - bowl #22 [12-17s]; floor #1 - washing - bowl #22 [17-25s]; floor #1 - placing - bowl #22 [25-27s]; floor #1 - washing dishes - bowl #22 [12-17s]; floor #1 - washing dishes - bowl #22 [12-17s]; floor #1 - holding - bowl #30 [27-45s]; floor #1 - washing - bowl #30 [27-45s]; floor #1 - placing - bowl #30 [45-47s]; floor #1 - washing dishes - bowl #30 [27-45s]; floor #1 - washing dishes - bowl #30 [27-45s]


## d1d4a1b3-a651-4eb8-bb7f-8d66982854fa

183.8 s, 128 frames read | human: 44 objects, 41 relations | TRASER: 40 objects, 17 relations, valid JSON, 2019 tokens

**Objects: 25/44 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | wall | table | mismatch | ✗ |
| 2 | mat | hand | mismatch | ✗ |
| 3 | others | cell phone (uncertain) | hypernym/hyponym | ✓ |
| 4 | card | playing card | hypernym/hyponym | ✓ |
| 5 | adult | hand | mismatch | ✗ |
| 6 | table | hand | mismatch | ✗ |
| 7 | box | table | mismatch | ✗ |
| 8 | cellphone | hand | mismatch | ✗ |
| 9 | card | playing card | hypernym/hyponym | ✓ |
| 10 | adult | hand | mismatch | ✗ |
| 11 | box | hand | mismatch | ✗ |
| 12 | cellphone | hand | mismatch | ✗ |
| 13 | card | playing card | hypernym/hyponym | ✓ |
| 14 | card | playing card | hypernym/hyponym | ✓ |
| 15 | card | hand | mismatch | ✗ |
| 16 | card | hand | mismatch | ✗ |
| 17 | card | hand | mismatch | ✗ |
| 18 | card | playing card | hypernym/hyponym | ✓ |
| 19 | card | playing card | hypernym/hyponym | ✓ |
| 20 | card | hand | mismatch | ✗ |
| 21 | card | hand | mismatch | ✗ |
| 22 | card | playing card | hypernym/hyponym | ✓ |
| 23 | card | playing card | hypernym/hyponym | ✓ |
| 24 | card | playing card | hypernym/hyponym | ✓ |
| 25 | card | playing card | hypernym/hyponym | ✓ |
| 26 | card | playing card | hypernym/hyponym | ✓ |
| 27 | card | playing card | hypernym/hyponym | ✓ |
| 28 | card | playing card | hypernym/hyponym | ✓ |
| 29 | card | playing card | hypernym/hyponym | ✓ |
| 30 | card | playing card | hypernym/hyponym | ✓ |
| 31 | card | playing card | hypernym/hyponym | ✓ |
| 32 | card | playing card | hypernym/hyponym | ✓ |
| 33 | card | playing card | hypernym/hyponym | ✓ |
| 34 | card | playing card | hypernym/hyponym | ✓ |
| 35 | card | playing card | hypernym/hyponym | ✓ |
| 36 | card | playing card | hypernym/hyponym | ✓ |
| 37 | card | playing card | hypernym/hyponym | ✓ |
| 38 | card | playing card | hypernym/hyponym | ✓ |
| 39 | card | playing card | hypernym/hyponym | ✓ |
| 40 | card | hand | mismatch | ✗ |
| 41 | card | - | no label from TRASER | ✗ |
| 42 | card | - | no label from TRASER | ✗ |
| 43 | card | - | no label from TRASER | ✗ |
| 44 | card | - | no label from TRASER | ✗ |

**Relations: 0/41 right, triplets: 0/41 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| card #4 - on - table #6 | 0-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #9 - on - table #6 | 0-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #13 - on - table #6 | 0-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #14 - on - table #6 | 0-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #15 - on - table #6 | 0-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #16 - on - table #6 | 0-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - card #18 | 6.6-14.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - holding - card #17 | 8.8-14.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - card #19 | 18.4-21.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #19 - on - card #13 | 20.4-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - card #20 | 23.2-27.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #20 - on - table #6 | 27.6-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - holding - card #21 | 29-31s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #21 - on - table #6 | 30.8-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - holding - card #22 | 32.6-35.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - holding - card #23 | 36-39.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #23 - on - table #6 | 39.8-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - card #24 | 40.6-44s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - card #25 | 45.4-48.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #24 - on - card #4 | 43.8-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - picking - card #23 | 59.4-65.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #23 - on - card #25 | 65-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - card #26 | 72.8-79.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - holding - card #28 | 83.8-86.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #28 - on - card #9 | 86.6-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #25 - on - card #22 | 48.4-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #26 - on - card #20 | 79.2-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - card #30 | 92-99s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #30 - on - card #26 | 98.8-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #36 - on - card #30 | 65-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - card #36 | 125-130.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - holding - card #37 | 132.4-137.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #37 - on - card #35 | 137.2-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #38 - on - card #36 | 142.2-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - card #38 | 139.8-142.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #40 - on - card #38 | 152-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - card #40 | 149-152s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #42 - on - card #40 | 158.4-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - card #42 | 155.8-158.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #5 - holding - card #44 | 167.6-173.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| card #44 - on - card #21 | 173-175.4s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (17): mat #2 - manipulates - card #4 [0-2.87188s, 4.30781-18.6672s]; mat #2 - manipulates - card #13 [18.6672-24.4109s]; mat #2 - manipulates - card #14 [24.4109-31.5906s]; mat #2 - manipulates - card #19 [31.5906-38.7703s]; mat #2 - manipulates - card #22 [38.7703-45.95s]; mat #2 - manipulates - card #23 [45.95-53.1297s]; mat #2 - manipulates - card #25 [53.1297-60.3094s]; mat #2 - manipulates - card #26 [60.3094-67.4891s]; mat #2 - manipulates - card #27 [67.4891-74.6688s]; mat #2 - manipulates - card #28 [74.6688-81.8484s]


## d2222009-a717-4b16-91ce-6399c5bb798a

115.8 s, 116 frames read | human: 39 objects, 34 relations | TRASER: 35 objects, 0 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 27/39 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | mat | chair | mismatch | ✗ |
| 2 | countertop | stove top | semantic overlap | ✓ |
| 3 | dustbin | pot | mismatch | ✗ |
| 4 | tray | tray | identical | ✓ |
| 5 | oven | bottle | mismatch | ✗ |
| 6 | stove | stove | identical | ✓ |
| 7 | cabinet | person | mismatch | ✗ |
| 8 | basket | - | no label from TRASER | ✗ |
| 9 | adult | hand | mismatch | ✗ |
| 10 | table | tablecloth | semantic overlap | ✓ |
| 11 | chair | chair | identical | ✓ |
| 12 | plate | cup | semantic overlap | ✓ |
| 13 | bowl | cup | semantic overlap | ✓ |
| 14 | cup | cup | identical | ✓ |
| 15 | tray | tray | identical | ✓ |
| 16 | cabinet | - | no label from TRASER | ✗ |
| 17 | table | chair | mismatch | ✗ |
| 18 | chair | place mat | mismatch | ✗ |
| 19 | plate | cup | semantic overlap | ✓ |
| 20 | cup | cup | identical | ✓ |
| 21 | chair | chair | identical | ✓ |
| 22 | plate | cup | semantic overlap | ✓ |
| 23 | cup | cup | identical | ✓ |
| 24 | tray | - | no label from TRASER | ✗ |
| 25 | chair | chair | identical | ✓ |
| 26 | plate | cup | semantic overlap | ✓ |
| 27 | cup | cup | identical | ✓ |
| 28 | chair | chair | identical | ✓ |
| 29 | plate | cup | semantic overlap | ✓ |
| 30 | bowl | - | no label from TRASER | ✗ |
| 31 | cup | cup | identical | ✓ |
| 32 | chair | bottle | mismatch | ✗ |
| 33 | cup | cup | identical | ✓ |
| 34 | cup | cup | identical | ✓ |
| 35 | cup | cup | identical | ✓ |
| 36 | cup | cup | identical | ✓ |
| 37 | cup | cup | identical | ✓ |
| 38 | cup | cup | identical | ✓ |
| 39 | cup | cup | identical | ✓ |

**Relations: 0/34 right, triplets: 0/34 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| adult #9 - holding - tray #4 | 2.2-5.6s, 29-35.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| tray #4 - on - table #17 | 29-115.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - beside - table #10 | 4.6-30.2s, 39.6-44.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - beside - table #17 | 53-110.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - holding - tray #15 | 43-55.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - holding - cup #23 | 56.6-60.4s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - beside - plate #29 | 82-88.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - picking - bowl #13 | 4.6-6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - picking - cup #31 | 6-7.2s, 80.8-86.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - picking - plate #22 | 7.2-8.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - picking - cup #23 | 8.6-10.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - picking - cup #20 | 10.2-11.6s, 68.2-73.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - picking - cup #27 | 11.6-13.2s, 80.8-86.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - picking - cup #14 | 14.2-15.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - picking - plate #12 | 15.8-18.8s, 26.4-28.8s, 56-62.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - picking - cup #33 | 21.6-23.8s, 95-101.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - picking - cup #34 | 23.8-26.4s, 95-101.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - picking - plate #26 | 39-41s | nothing for this pair | - | - | - | ✗ | ✗ |
| plate #26 - on - tray #15 | 40.8-115.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| cup #36 - on - tray #15 | 42.6-115.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| cup #35 - on - tray #15 | 42.6-115.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| cup #39 - on - plate #26 | 42-115.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| tray #15 - on - table #17 | 52.2-115.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| plate #12 - on - cabinet #7 | 62.6-115.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| plate #29 - on - cabinet #7 | 62.6-115.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - picking - cup #38 | 68.2-73.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| cup #20 - on - plate #12 | 73-115.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| cup #38 - on - plate #12 | 73-115.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| cup #20 - on - plate #29 | 86-115.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| cup #38 - on - plate #29 | 86-115.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| cup #34 - on - cabinet #7 | 101.6-115.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| cup #33 - on - cabinet #7 | 101.6-115.8s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #9 - picking - tray #4 | 110.4-115.2s | nothing for this pair | - | - | - | ✗ | ✗ |
| tray #4 - on - cabinet #7 | 115-115.8s | nothing for this pair | - | - | - | ✗ | ✗ |


## eed8d8d7-6773-493b-af21-880f0acb063a

68.6 s, 69 frames read | human: 16 objects, 10 relations | TRASER: 16 objects, 28 relations, valid JSON, 1488 tokens

**Objects: 6/16 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 1 | floor | person | mismatch | ✗ |
| 2 | wall | wall | identical | ✓ |
| 3 | cloth | blanket (uncertain) | semantic overlap | ✓ |
| 4 | iron | blanket | mismatch | ✗ |
| 5 | board | doormat | mismatch | ✗ |
| 6 | cabinet | cabinet | identical | ✓ |
| 7 | tv | vent (uncertain) | mismatch | ✗ |
| 8 | door | drawer (uncertain) | mismatch | ✗ |
| 9 | stand | chair | mismatch | ✗ |
| 10 | adult | person | hypernym/hyponym | ✓ |
| 11 | sofa | sofa | identical | ✓ |
| 12 | bottle | box | mismatch | ✗ |
| 13 | cup | pillow | mismatch | ✗ |
| 14 | bag | pillow | mismatch | ✗ |
| 15 | cloth | blanket | semantic overlap | ✓ |
| 16 | door | chair | mismatch | ✗ |

**Relations: 0/10 right, triplets: 0/10 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| sofa #11 - on - floor #1 | 0-67s | nothing for this pair | - | - | - | ✗ | ✗ |
| cabinet #6 - on - floor #1 | 0-67s | nothing for this pair | - | - | - | ✗ | ✗ |
| tv #7 - on - cabinet #6 | 0-67s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - holding - iron #4 | 5-20.2s, 22.6-36s, 44.2-55.2s, 56.8-67s | nothing for this pair | - | - | - | ✗ | ✗ |
| iron #4 - on - cloth #3 | 5.6-19s, 23.2-34.6s, 44.8-53.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| iron #4 - on - board #5 | 19.8-23.2s, 35.8-45s, 54.6-67s | moving on (+1 more) | 0-67.6058s | hypernym/hyponym | 0.37 | ✗ | ✗ |
| adult #10 - holding - cup #13 | 59-67s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - holding - cloth #3 | 0-1.6s | nothing for this pair | - | - | - | ✗ | ✗ |
| cloth #3 - on - board #5 | 1.4-67s | nothing for this pair | - | - | - | ✗ | ✗ |
| adult #10 - watering - iron #4 | 61.2-66.2s | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (26): floor #1 - holding - iron #4 [0-67.6058s]; floor #1 - wiping - board #5 [0-67.6058s]; floor #1 - cleaning - board #5 [0-67.6058s]; floor #1 - on - board #5 [0-67.6058s]; floor #1 - in front of - wall #2 [0-67.6058s]; board #5 - in front of - wall #2 [0-67.6058s]; cabinet #6 - against - wall #2 [0-67.6058s]; sofa #11 - against - wall #2 [0-67.6058s]; stand #9 - in front of - wall #2 [0-67.6058s]; cup #13 - on - stand #9 [0-67.6058s]

