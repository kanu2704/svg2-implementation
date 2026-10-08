# svg2test: human labels vs TRASER, video by video

57 videos with a prediction. Lenient criterion, temporal IoU > 0.5. ✓ right, ✗ wrong, ? = the judge (Kimi K3) has not compared these two labels yet (identical text counts as right without the judge). Relation = same two objects, predicate not a mismatch, tIoU > 0.5; triplet = relation right and both object labels right. Made by `tools/bench_eval.py write_compare`.

**So far: objects 628/1851, relations 387/1882, triplets 161/1882** (unjudged pairs count as not right; scores in README.md)

| video | objects right | relations right | triplets right | not judged yet (?) |
|---|---|---|---|---|
| [1016_8J41CsGYhNI](#1016_8j41csgyhni) | 5/15 | 9/24 | 3/24 | 11 |
| [1047_-_XOsbwGZgg](#1047_-_xosbwgzgg) | 23/53 | 19/56 | 13/56 | 22 |
| [1086_iywqpda7d8k](#1086_iywqpda7d8k) | 2/9 | 5/19 | 0/19 | 15 |
| [1125_Cbv34yDZ8gc](#1125_cbv34ydz8gc) | 13/46 | 6/25 | 0/25 | 18 |
| [1187_AqH9dWCvTkY](#1187_aqh9dwcvtky) | 16/36 | 0/4 | 0/4 | 15 |
| [1190_UmpN6eLjN8w](#1190_umpn6eljn8w) | 6/18 | 7/44 | 3/44 | 13 |
| [1251__MCY-QkVaZw](#1251__mcy-qkvazw) | 6/12 | 4/11 | 0/11 | 10 |
| [1253_TPxVj7do42I](#1253_tpxvj7do42i) | 8/21 | 6/35 | 3/35 | 15 |
| [1256_Y_19xu4yTms](#1256_y_19xu4ytms) | 16/32 | 7/61 | 5/61 | 39 |
| [1261_wsHfWwHXgLs](#1261_wshfwwhxgls) | 3/8 | 4/22 | 3/22 | 7 |
| [1268_h58xqlUE5xA](#1268_h58xqlue5xa) | 2/11 | 7/21 | 0/21 | 21 |
| [1275_ARcg-EyKWrA](#1275_arcg-eykwra) | 12/68 | 3/21 | 3/21 | 17 |
| [1308_-C_XboJfD0g](#1308_-c_xbojfd0g) | 1/14 | 1/15 | 0/15 | 15 |
| [1352_nt-UZxGk9Bg](#1352_nt-uzxgk9bg) | 3/14 | 5/35 | 2/35 | 27 |
| [1480_WAGXu9_6Uv0](#1480_wagxu9_6uv0) | 12/46 | 2/41 | 0/41 | 23 |
| [1503_gwrvCEAZVl0](#1503_gwrvceazvl0) | 7/20 | 3/34 | 2/34 | 17 |
| [1638_MhoaeR88gm4](#1638_mhoaer88gm4) | 16/63 | 0/10 | 0/10 | 17 |
| [1691_md-DpQ4HX7Q](#1691_md-dpq4hx7q) | 4/21 | 15/39 | 0/39 | 41 |
| [1717_lh_2_1duNgw](#1717_lh_2_1dungw) | 25/65 | 34/79 | 0/79 | 48 |
| [1757_0jsMPnghnck](#1757_0jsmpnghnck) | 18/23 | 22/28 | 17/28 | 4 |
| [179_mha1KKixPts](#179_mha1kkixpts) | 1/27 | 1/14 | 0/14 | 29 |
| [1903_cFq3flHndS0](#1903_cfq3flhnds0) | 8/20 | 5/21 | 0/21 | 21 |
| [1936_gvKlIkjfP0Q](#1936_gvklikjfp0q) | 18/56 | 0/40 | 0/40 | 18 |
| [2143_6OMR3X7IcZ0](#2143_6omr3x7icz0) | 10/16 | 1/28 | 1/28 | 9 |
| [2225_6acPX_00M9Q](#2225_6acpx_00m9q) | 11/19 | 8/38 | 3/38 | 17 |
| [226_n7YpGfnTqoY](#226_n7ypgfntqoy) | 11/20 | 16/51 | 9/51 | 26 |
| [241_oEkly9vzEGQ](#241_oekly9vzegq) | 17/26 | 9/31 | 8/31 | 7 |
| [246_QcRqBBAiC4o](#246_qcrqbbaic4o) | 8/56 | 5/36 | 0/36 | 41 |
| [254_-7d3nOFx1V8](#254_-7d3nofx1v8) | 12/30 | 7/25 | 2/25 | 28 |
| [276_3HgBHBOnpbg](#276_3hgbhbonpbg) | 4/40 | 0/55 | 0/55 | 6 |
| [279_qw5ySRNNfNM](#279_qw5ysrnnfnm) | 17/89 | 2/47 | 0/47 | 29 |
| [285_EP_blwEf2K8](#285_ep_blwef2k8) | 14/58 | 1/50 | 0/50 | 30 |
| [308_7WhzIsqPQW8](#308_7whzisqpqw8) | 6/42 | 2/41 | 0/41 | 40 |
| [339_j2gELsuQ3Cg](#339_j2gelsuq3cg) | 7/14 | 0/20 | 0/20 | 10 |
| [359_4ZPKJtcNGZE](#359_4zpkjtcngze) | 2/27 | 2/20 | 0/20 | 22 |
| [365_JFqiSr9A-Go](#365_jfqisr9a-go) | 19/48 | 3/53 | 1/53 | 10 |
| [419_CykhOKWEAjo](#419_cykhokweajo) | 17/43 | 8/32 | 3/32 | 25 |
| [434_eOTP9yrATX8](#434_eotp9yratx8) | 8/14 | 12/37 | 6/37 | 22 |
| [465_nbJ_SLWUDxk](#465_nbj_slwudxk) | 32/39 | 4/24 | 2/24 | 10 |
| [470_BiIqH60-A1M](#470_biiqh60-a1m) | 14/36 | 7/30 | 7/30 | 17 |
| [474_b-Qlvj48YQw](#474_b-qlvj48yqw) | 16/72 | 11/30 | 5/30 | 27 |
| [520_JbMXRRGOEkk](#520_jbmxrrgoekk) | 12/24 | 4/31 | 0/31 | 21 |
| [547_7E-Xian95Qk](#547_7e-xian95qk) | 3/22 | 12/28 | 1/28 | 32 |
| [551_VHxQVmG1pOA](#551_vhxqvmg1poa) | 29/47 | 16/53 | 12/53 | 14 |
| [562_OA61thiz9wU](#562_oa61thiz9wu) | 3/40 | 2/34 | 1/34 | 36 |
| [628_nQRJD435Fh4](#628_nqrjd435fh4) | 22/40 | 20/52 | 6/52 | 31 |
| [642_ljk5b80TmkE](#642_ljk5b80tmke) | 10/23 | 0/25 | 0/25 | 13 |
| [66_927BvkIZglw](#66_927bvkizglw) | 5/20 | 1/28 | 1/28 | 16 |
| [670_JboU-y2LdkU](#670_jbou-y2ldku) | 19/24 | 18/33 | 18/33 | 6 |
| [700_zkhPzSZcRtQ](#700_zkhpzszcrtq) | 10/24 | 8/41 | 6/41 | 14 |
| [714_nooF6zlfzMI](#714_noof6zlfzmi) | 5/13 | 4/26 | 0/26 | 16 |
| [722__ajUvCkhVcI](#722__ajuvckhvci) | 5/18 | 4/39 | 0/39 | 24 |
| [742_ctcOIuSzy-s](#742_ctcoiuszy-s) | 8/16 | 10/25 | 5/25 | 17 |
| [744_1X6KvqPjk6I](#744_1x6kvqpjk6i) | 15/32 | 4/26 | 3/26 | 21 |
| [754_TYUV8DYWe8k](#754_tyuv8dywe8k) | 9/28 | 1/26 | 1/26 | 22 |
| [766_m1Vdl-EMY1E](#766_m1vdl-emy1e) | 14/20 | 9/32 | 3/32 | 13 |
| [839_SS_1452uWvg](#839_ss_1452uwvg) | 9/73 | 11/36 | 3/36 | 49 |

## 1016_8J41CsGYhNI

22.67 s, 23 frames read | human: 15 objects, 24 relations | TRASER: 15 objects, 24 relations, valid JSON, 1088 tokens

**Objects: 5/15 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | ball | sports ball (uncertain) | hypernym/hyponym | ✓ |
| 1 | tennis net | tennis net | identical | ✓ |
| 2 | curtain | curtain | identical | ✓ |
| 3 | tennis court surface | tennis ball | not judged yet | ? |
| 4 | person | person | identical | ✓ |
| 5 | tennis racquet | tennis racket | not judged yet | ? |
| 6 | headwear | headband (uncertain) | hypernym/hyponym | ✓ |
| 7 | shirt | jersey (uncertain) | not judged yet | ? |
| 8 | short | shorts | not judged yet | ? |
| 9 | shoes | shoe | not judged yet | ? |
| 10 | floor | tennis ball | mismatch | ✗ |
| 11 | floor | tennis ball | mismatch | ✗ |
| 12 | floor | tennis ball | mismatch | ✗ |
| 13 | floor | tennis ball | mismatch | ✗ |
| 14 | floor | tennis ball | mismatch | ✗ |

**Relations: 9/24 right, triplets: 3/24 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| ball #0 - approaches - tennis racquet #5 | 10-12 | nothing for this pair | - | - | - | ✗ | ✗ |
| ball #0 - above - tennis net #1 | 9-10.5, 20-21.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| ball #0 - approaches - tennis net #1 | 9-10, 20-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| ball #0 - above - tennis court surface #3 | 0-1, 9-12.5, 20-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| ball #0 - in front of - curtain #2 | 0-1, 9-12, 20-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tennis net #1 - on - tennis court surface #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tennis net #1 - in front of - curtain #2 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #4 - holding - tennis racquet #5 | 0-23 | holding | 0-24 | identical | 0.96 | ✓ | ? |
| person #4 - wearing - headwear #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - wearing - shirt #7 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - wearing - short #8 | 0-23 | wearing | 0-24 | identical | 0.96 | ✓ | ? |
| person #4 - hits - ball #0 | 11-12 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - looking at - ball #0 | 9-12, 20-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - approaches - tennis net #1 | 1-6 | moving along (+2 more) | 0-24 | not judged yet | 0.21 | ✗ | ✗ |
| person #4 - behind - tennis net #1 | 0-23 | behind (+2 more) | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #4 - on - tennis court surface #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - in front of - curtain #2 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| tennis racquet #5 - above - tennis court surface #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tennis racquet #5 - near - person #4 | 0-23 | near (+1 more) | 0-24 | identical | 0.96 | ✓ | ? |
| tennis racquet #5 - in front of - curtain #2 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ? |
| headwear #6 - on - person #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #7 - on - person #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| short #8 - on - person #4 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ? |
| shoes #9 - on - person #4 | 0-18.5, 19.5-23 | on | 0-24 | identical | 0.92 | ✓ | ? |

TRASER relations between pairs the humans did not annotate (12): person #4 - wearing - shoes #9 [0-24]; tennis racquet #5 - above - tennis net #1 [0-24]; short #8 - behind - tennis net #1 [0-24]; shoes #9 - behind - tennis net #1 [0-24]; shoes #9 - below - short #8 [0-24]; tennis racquet #5 - above - short #8 [0-24]; tennis racquet #5 - above - shoes #9 [0-24]; floor #10 - above - tennis net #1 [0-24]; floor #11 - above - tennis net #1 [0-24]; floor #12 - above - tennis net #1 [0-1, 23-24]


## 1047_-_XOsbwGZgg

7.5 s, 8 frames read | human: 53 objects, 56 relations | TRASER: 40 objects, 68 relations, valid JSON, 3264 tokens

**Objects: 23/53 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | person | person | identical | ✓ |
| 1 | person | person | identical | ✓ |
| 2 | person | person | identical | ✓ |
| 3 | person | person | identical | ✓ |
| 4 | person | suit jacket | not judged yet | ? |
| 5 | thrash can | cardboard box | not judged yet | ? |
| 6 | door | door | identical | ✓ |
| 7 | wall | wall | identical | ✓ |
| 8 | tree | plant | not judged yet | ? |
| 9 | rope | tape (uncertain) | not judged yet | ? |
| 10 | mat | mat | identical | ✓ |
| 11 | bench | bench | identical | ✓ |
| 12 | floor | doormat | semantic overlap | ✓ |
| 13 | sign | signboard | not judged yet | ? |
| 14 | box | box | identical | ✓ |
| 15 | ground | doormat | not judged yet | ? |
| 16 | bollard | tape (uncertain) | not judged yet | ? |
| 17 | bench support | box | mismatch | ✗ |
| 18 | box | speaker (uncertain) | mismatch | ✗ |
| 19 | pot | box | not judged yet | ? |
| 20 | ledge | vent (uncertain) | mismatch | ✗ |
| 21 | utility box | chair leg (uncertain) | not judged yet | ? |
| 22 | bench support | box | mismatch | ✗ |
| 23 | electrical box | wall panel | not judged yet | ? |
| 24 | shirt | shirt | identical | ✓ |
| 25 | watch | watch | identical | ✓ |
| 26 | trouser | trousers | not judged yet | ? |
| 27 | shoe | shoe | identical | ✓ |
| 28 | shoe | shoe | identical | ✓ |
| 29 | hand | arm | semantic overlap | ✓ |
| 30 | hand | arm | semantic overlap | ✓ |
| 31 | face | person | hypernym/hyponym | ✓ |
| 32 | face | person | hypernym/hyponym | ✓ |
| 33 | shirt | shirt | identical | ✓ |
| 34 | hand | hand | identical | ✓ |
| 35 | hand | hand | identical | ✓ |
| 36 | trouser | trousers | not judged yet | ? |
| 37 | shirt | suit jacket | not judged yet | ? |
| 38 | face | person | hypernym/hyponym | ✓ |
| 39 | shirt | shirt | identical | ✓ |
| 40 | left forearm | - | no label from TRASER | ✗ |
| 41 | right forearm | - | no label from TRASER | ✗ |
| 42 | trouser | - | no label from TRASER | ✗ |
| 43 | right shoe | - | no label from TRASER | ✗ |
| 44 | left shoe | - | no label from TRASER | ✗ |
| 45 | face | - | no label from TRASER | ✗ |
| 46 | jacket | - | no label from TRASER | ✗ |
| 47 | trouser | - | no label from TRASER | ✗ |
| 48 | shoe | - | no label from TRASER | ✗ |
| 49 | trouser | - | no label from TRASER | ✗ |
| 50 | shoe | - | no label from TRASER | ✗ |
| 51 | bin cover | - | no label from TRASER | ✗ |
| 52 | bin bowl | - | no label from TRASER | ✗ |

**Relations: 19/56 right, triplets: 13/56 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - balancing on - rope #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - slacklining on - rope #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - above - rope #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - wearing - watch #25 | 0-8 | wearing | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #0 - wearing - shirt #24 | 0-8 | wearing | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #0 - wearing - trouser #26 | 0-8 | wearing | 0-9 | identical | 0.89 | ✓ | ? |
| person #0 - in front of - wall #7 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #0 - above - mat #10 | 0-8 | moving on (+1 more) | 0-9 | not judged yet | 0.89 | ? | ? |
| person #1 - looking at - person #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - behind - person #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - wearing - shirt #33 | 0-8 | wearing | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #1 - wearing - trouser #36 | 0-8 | wearing | 0-9 | identical | 0.89 | ✓ | ? |
| person #1 - in front of - wall #7 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #1 - on - mat #10 | 0-8 | moving on (+1 more) | 0-9 | hypernym/hyponym | 0.89 | ✓ | ✓ |
| person #1 - in front of - door #6 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #2 - looking at - person #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - behind - person #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - wearing - shirt #39 | 0-8 | wearing | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #2 - wearing - trouser #42 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - in front of - wall #7 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #2 - on - mat #10 | 0-8 | moving on (+1 more) | 0-9 | hypernym/hyponym | 0.89 | ✓ | ✓ |
| person #3 - looking at - person #0 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - behind - person #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - wearing - jacket #46 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - wearing - trouser #47 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - in front of - wall #7 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #3 - in front of - door #6 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #3 - behind - person #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - on - floor #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - in front of - wall #7 | 1-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - on - floor #12 | 1-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| thrash can #5 - on - mat #10 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ? |
| thrash can #5 - in front of - wall #7 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ? |
| tree #8 - in front of - wall #7 | 0-8 | on | 0-9 | not judged yet | 0.89 | ? | ? |
| rope #9 - tied to - bollard #16 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| rope #9 - above - floor #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| rope #9 - above - ground #15 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| rope #9 - above - mat #10 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| rope #9 - in front of - wall #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| mat #10 - on - ground #15 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| mat #10 - in front of - wall #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bench #11 - in front of - wall #7 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✓ |
| sign #13 - on - wall #7 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ? |
| sign #13 - above - box #14 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| box #14 - on - wall #7 | 0-8 | in front of | 0-9 | not judged yet | 0.89 | ? | ? |
| bench support #17 - in front of - wall #7 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✗ |
| bench support #17 - on - ground #15 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| box #18 - on - ground #15 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| pot #19 - on - floor #12 | 1-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| utility box #21 - on - electrical box #23 | 0-1, 7-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bench support #22 - above - floor #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| electrical box #23 - above - bench support #17 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| electrical box #23 - in front of - wall #7 | 0-8 | on | 0-9 | not judged yet | 0.89 | ? | ? |
| bin cover #51 - covering - thrash can #5 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bin cover #51 - above - bin bowl #52 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bin bowl #52 - on - floor #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (42): person #0 - wearing - shoe #27 [0-9]; person #0 - wearing - shoe #28 [0-9]; person #2 - wearing - trouser #36 [0-9]; person #0 - dancing with - person #1 [0-9]; person #0 - in front of - person #1 [0-9]; person #0 - dancing with - person #2 [0-9]; person #0 - in front of - person #2 [0-9]; person #1 - dancing with - person #2 [0-9]; person #3 - on - mat #10 [0-9]; bench #11 - on - mat #10 [0-9]


## 1086_iywqpda7d8k

20.17 s, 20 frames read | human: 9 objects, 19 relations | TRASER: 9 objects, 22 relations, valid JSON, 878 tokens

**Objects: 2/9 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | trees | foliage | not judged yet | ? |
| 1 | trees | forest | not judged yet | ? |
| 2 | waterfall | waterfall | identical | ✓ |
| 3 | plants | bush | not judged yet | ? |
| 4 | trees | tree | not judged yet | ? |
| 5 | trees | forest | not judged yet | ? |
| 6 | sky | clouds | not judged yet | ? |
| 7 | tree | leaves | not judged yet | ? |
| 8 | cliffside | cliff | identical | ✓ |

**Relations: 5/19 right, triplets: 0/19 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| trees #0 - below - sky #6 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #0 - in front of - waterfall #2 | 0-21 | in front of (+1 more) | 0-20 | identical | 0.95 | ✓ | ? |
| trees #1 - below - sky #6 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| waterfall #2 - flows down past - trees #1 | 0-21 | flows past (+1 more) | 0-20 | not judged yet | 0.95 | ? | ? |
| waterfall #2 - in front of - trees #1 | 0-21 | in front of (+1 more) | 0-20 | identical | 0.95 | ✓ | ? |
| waterfall #2 - flows down past - cliffside #8 | 17-21 | flows past | 18-20 | not judged yet | 0.50 | ✗ | ✗ |
| waterfall #2 - in front of - cliffside #8 | 17-21 | flows past | 18-20 | not judged yet | 0.50 | ✗ | ✗ |
| waterfall #2 - below - sky #6 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants #3 - below - sky #6 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants #3 - in front of - waterfall #2 | 0-21 | in front of (+1 more) | 0-20 | identical | 0.95 | ✓ | ? |
| plants #3 - in front of - trees #1 | 0-21 | in front of | 0-20 | identical | 0.95 | ✓ | ? |
| plants #3 - below - trees #1 | 0-21 | in front of | 0-20 | not judged yet | 0.95 | ? | ? |
| plants #3 - in front of - cliffside #8 | 17-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #4 - below - sky #6 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #4 - above - waterfall #2 | 0-21 | behind | 0-20 | not judged yet | 0.95 | ? | ? |
| trees #5 - below - sky #6 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #5 - above - waterfall #2 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #7 - in front of - waterfall #2 | 0-11 | in front of (+1 more) | 0-12 | identical | 0.92 | ✓ | ? |
| cliffside #8 - below - sky #6 | 17-21 | below | 18-20 | identical | 0.50 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (10): waterfall #2 - flows past - plants #3 [0-20]; waterfall #2 - flows past - trees #0 [0-20]; waterfall #2 - in front of - trees #5 [0-20]; trees #0 - in front of - trees #1 [0-20]; tree #7 - in front of - trees #1 [0-12]; sky #6 - above - waterfall #2 [0-20]; sky #6 - above - trees #1 [0-20]; sky #6 - above - trees #5 [0-20]; trees #4 - in front of - trees #1 [0-20]; cliffside #8 - in front of - trees #1 [18-20]


## 1125_Cbv34yDZ8gc

7.5 s, 8 frames read | human: 46 objects, 25 relations | TRASER: 40 objects, 40 relations, valid JSON, 2809 tokens

**Objects: 13/46 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | wall | wall | identical | ✓ |
| 1 | floor | shadow (uncertain) | not judged yet | ? |
| 2 | plant | plant | identical | ✓ |
| 3 | person | person | identical | ✓ |
| 4 | phone | cellular telephone (uncertain) | not judged yet | ? |
| 5 | trash bag | plastic bag | not judged yet | ? |
| 6 | person | jersey | mismatch | ✗ |
| 7 | person | person | identical | ✓ |
| 8 | person | person | identical | ✓ |
| 9 | person | person | identical | ✓ |
| 10 | building | wall | semantic overlap | ✓ |
| 11 | nail | hammer | mismatch | ✗ |
| 12 | hammer | hammer | identical | ✓ |
| 13 | bin | wall | not judged yet | ? |
| 14 | wall | pipe (uncertain) | not judged yet | ? |
| 15 | grave | box | mismatch | ✗ |
| 16 | grave | box | mismatch | ✗ |
| 17 | grave | cat | not judged yet | ? |
| 18 | grave | box | mismatch | ✗ |
| 19 | hand | arm | semantic overlap | ✓ |
| 20 | shirt | shirt | identical | ✓ |
| 21 | cap | baseball cap | hypernym/hyponym | ✓ |
| 22 | face | hat (uncertain) | mismatch | ✗ |
| 23 | shirt | jersey | not judged yet | ? |
| 24 | short | jeans (uncertain) | not judged yet | ? |
| 25 | shirt | jersey | not judged yet | ? |
| 26 | band | watch | not judged yet | ? |
| 27 | head | person | mismatch | ✗ |
| 28 | necklace | jersey (uncertain) | not judged yet | ? |
| 29 | head | person | mismatch | ✗ |
| 30 | shirt | person | not judged yet | ? |
| 31 | short | jersey (uncertain) | not judged yet | ? |
| 32 | head | person | mismatch | ✗ |
| 33 | short | trousers | not judged yet | ? |
| 34 | legs | legs | identical | ✓ |
| 35 | wristwatch | knob (uncertain) | not judged yet | ? |
| 36 | epitaph | poster | mismatch | ✗ |
| 37 | signboard | signboard | identical | ✓ |
| 38 | gravestone top | beam (uncertain) | not judged yet | ? |
| 39 | concrete | plastic bag | mismatch | ✗ |
| 40 | stone | - | no label from TRASER | ✗ |
| 41 | stone | - | no label from TRASER | ✗ |
| 42 | stone | - | no label from TRASER | ✗ |
| 43 | stone | - | no label from TRASER | ✗ |
| 44 | stone | - | no label from TRASER | ✗ |
| 45 | stone | - | no label from TRASER | ✗ |

**Relations: 6/25 right, triplets: 0/25 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| plant #2 - next to - grave #16 | 0-8 | in front of | 0-8 | mismatch | 1.00 | ✗ | ✗ |
| plant #2 - in front of - wall #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - holding - phone #4 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - looking at - grave #15 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - wearing - cap #21 | 2-5, 7-8 | wearing | 0-8 | identical | 0.50 | ✗ | ✗ |
| phone #4 - touching - hand #19 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| trash bag #5 - in front of - grave #15 | 2-8 | in front of | 0-8 | identical | 0.75 | ✓ | ✗ |
| person #6 - holding - trash bag #5 | 1.5-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #6 - in front of - grave #15 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #7 - looking at - grave #15 | 3-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #7 - wearing - necklace #28 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #8 - looking at - grave #15 | 5-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #9 - wearing - wristwatch #35 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #9 - behind - stone #40 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| building #10 - behind - grave #15 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| nail #11 - on top of - grave #15 | 0-8 | above | 0-8 | not judged yet | 1.00 | ? | ✗ |
| nail #11 - on - grave #15 | 0-8 | above | 0-8 | semantic overlap | 1.00 | ✓ | ✗ |
| hammer #12 - on top of - grave #15 | 0-8 | above | 0-8 | not judged yet | 1.00 | ? | ✗ |
| hammer #12 - on - grave #15 | 0-8 | above | 0-8 | semantic overlap | 1.00 | ✓ | ✗ |
| grave #15 - in front of - wall #0 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✗ |
| grave #15 - on - floor #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| grave #17 - inside - grave #15 | 0-8 | inside (+1 more) | 0-8 | identical | 1.00 | ✓ | ✗ |
| short #33 - above - legs #34 | 0-2, 4-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| epitaph #36 - on - building #10 | 0-3, 4-8 | on | 0-8 | identical | 0.88 | ✓ | ✗ |
| gravestone top #38 - above - building #10 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (31): person #3 - holding - plant #2 [0-8]; person #7 - wearing - shirt #23 [0-8]; person #8 - wearing - short #33 [0-8]; person #8 - wearing - band #26 [0-8]; nail #11 - on - grave #18 [0-8]; nail #11 - above - grave #18 [0-8]; hammer #12 - on - grave #18 [0-8]; hammer #12 - above - grave #18 [0-8]; grave #16 - in front of - wall #0 [0-8]; grave #18 - in front of - wall #0 [0-8]


## 1187_AqH9dWCvTkY

7.5 s, 8 frames read | human: 36 objects, 4 relations | TRASER: 36 objects, 125 relations, valid JSON, 3959 tokens

**Objects: 16/36 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | track | athletic field | not judged yet | ? |
| 1 | runner | person | not judged yet | ? |
| 2 | runner | person | not judged yet | ? |
| 3 | runner | person | not judged yet | ? |
| 4 | runner | person | not judged yet | ? |
| 5 | person | person | identical | ✓ |
| 6 | runner | person | not judged yet | ? |
| 7 | person | person | identical | ✓ |
| 8 | person | person | identical | ✓ |
| 9 | person | person | identical | ✓ |
| 10 | person | person | identical | ✓ |
| 11 | bag | person | mismatch | ✗ |
| 12 | grass | hill | not judged yet | ? |
| 13 | hill | tree | mismatch | ✗ |
| 14 | person | pole | mismatch | ✗ |
| 15 | person | pole | mismatch | ✗ |
| 16 | person | person | identical | ✓ |
| 17 | person | person | identical | ✓ |
| 18 | person | person | identical | ✓ |
| 19 | crowd | person | hypernym/hyponym | ✓ |
| 20 | fence | fence | identical | ✓ |
| 21 | screen | tree | not judged yet | ? |
| 22 | board | banner | semantic overlap | ✓ |
| 23 | screen | building | not judged yet | ? |
| 24 | sky | cloud | semantic overlap | ✓ |
| 25 | track | fence | not judged yet | ? |
| 26 | logo | signboard | semantic overlap | ✓ |
| 27 | logo | person | mismatch | ✗ |
| 28 | chair | bench | not judged yet | ? |
| 29 | chair | person | mismatch | ✗ |
| 30 | chair | person | mismatch | ✗ |
| 31 | chair | bench | not judged yet | ? |
| 32 | garbage can | person | mismatch | ✗ |
| 33 | person | person | identical | ✓ |
| 34 | person | person | identical | ✓ |
| 35 | person | person | identical | ✓ |

**Relations: 0/4 right, triplets: 0/4 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| runner #1 - runs on - track #0 | 0-8 | running on (+1 more) | 0-8 | not judged yet | 1.00 | ? | ? |
| runner #1 - pulls away from - runner #2 | 3-8 | moving alongside | 0-8 | not judged yet | 0.62 | ? | ? |
| runner #2 - runs on - track #0 | 0-8 | running on (+1 more) | 0-8 | not judged yet | 1.00 | ? | ? |
| runner #2 - follows - runner #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (120): runner #1 - approaching - board #22 [4-7]; runner #1 - in front of - board #22 [4-8]; runner #1 - in front of - board #22 [4-8]; runner #2 - approaching - board #22 [4-7]; runner #2 - in front of - board #22 [4-8]; runner #2 - in front of - board #22 [4-8]; runner #1 - in front of - grass #12 [0-8]; runner #1 - in front of - grass #12 [0-8]; runner #2 - in front of - grass #12 [0-8]; runner #2 - in front of - grass #12 [0-8]


## 1190_UmpN6eLjN8w

10.17 s, 10 frames read | human: 18 objects, 44 relations | TRASER: 18 objects, 28 relations, valid JSON, 1355 tokens

**Objects: 6/18 right**

| id | human label | TRASER label | verdict | right |
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

**Relations: 7/44 right, triplets: 3/44 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| plane #0 - approaches - person #2 | 0-3, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plane #0 - above - person #2 | 0-3, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plane #0 - approaches - person #4 | 3-11 | above | 0-1, 3-11 | not judged yet | 0.89 | ? | ? |
| plane #0 - above - person #4 | 2.5-11 | above | 0-1, 3-11 | identical | 0.84 | ✓ | ? |
| plane #0 - moves across - sky #5 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| plane #0 - in front of - sky #5 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| plane #0 - has - wing #12 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| plane #0 - has - wing #13 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| plane #0 - has - tyres #14 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| plane #0 - has - tyres #15 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| plane #0 - has - nose #16 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| plane #0 - above - ocean #3 | 0-11 | above (+2 more) | 0-11 | identical | 1.00 | ✓ | ? |
| plane #0 - above - person #1 | 0-11 | above | 0-11 | identical | 1.00 | ✓ | ? |
| plane #0 - approaches - person #1 | 0-11 | above | 0-11 | not judged yet | 1.00 | ? | ? |
| person #1 - looking at - plane #0 | 2.5-5, 6.5-10 | looking at | 0-11 | identical | 0.55 | ✓ | ? |
| person #1 - has - hair #6 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - has - face #7 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - in front of - ocean #3 | 0-11 | in front of | 0-11 | identical | 1.00 | ✓ | ✓ |
| person #1 - in front of - sky #5 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - looking at - plane #0 | 0-3, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - wears - cap #8 | 0-2, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - wears - shirt #11 | 0-3, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - in front of - ocean #3 | 0-3, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - in front of - sky #5 | 0-3, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| ocean #3 - in front of - sky #5 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - looking at - plane #0 | 3-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - in front of - ocean #3 | 3-11 | in front of | 0-1, 3-11 | identical | 0.89 | ✓ | ✓ |
| person #4 - in front of - sky #5 | 3-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #5 - above - ocean #3 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| hair #6 - above - face #7 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| hair #6 - on - person #1 | 0-11 | on | 0-11 | identical | 1.00 | ✓ | ✓ |
| face #7 - on - person #1 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| cap #8 - on - person #2 | 0-2, 6-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| neck #9 - on - person #2 | 0-2, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| hair #10 - on - person #2 | 0-2.5, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #11 - on - person #2 | 0-2, 6-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| wing #12 - on - plane #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| wing #13 - on - plane #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| tyres #14 - on - plane #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| tyres #14 - below - wing #12 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| tyres #15 - on - plane #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| tyres #15 - below - wing #12 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| nose #16 - on - plane #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| hair #17 - on - person #4 | 3-11 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (19): wing #12 - above - ocean #3 [0-11]; wing #13 - above - ocean #3 [0-11]; tyres #14 - above - ocean #3 [0-11]; tyres #15 - above - ocean #3 [0-11]; nose #16 - above - ocean #3 [0-11]; wing #12 - above - person #1 [0-11]; wing #13 - above - person #1 [0-11]; tyres #14 - above - person #1 [0-11]; tyres #15 - above - person #1 [0-11]; nose #16 - above - person #1 [0-11]


## 1251__MCY-QkVaZw

10.17 s, 10 frames read | human: 12 objects, 11 relations | TRASER: 12 objects, 26 relations, valid JSON, 892 tokens

**Objects: 6/12 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | swimmer | person | not judged yet | ? |
| 1 | towel | surfboard | not judged yet | ? |
| 2 | sky | sky | identical | ✓ |
| 3 | ocean | person | mismatch | ✗ |
| 4 | ship | boat | not judged yet | ? |
| 5 | boat | boat | identical | ✓ |
| 6 | boat | boat | identical | ✓ |
| 7 | bra | swimsuit top | not judged yet | ? |
| 8 | bikini bottoms | swimsuit | hypernym/hyponym | ✓ |
| 9 | hair | hair | identical | ✓ |
| 10 | face | person | hypernym/hyponym | ✓ |
| 11 | band | hand | mismatch | ✗ |

**Relations: 4/11 right, triplets: 0/11 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| swimmer #0 - holding - towel #1 | 0-11 | holding (+3 more) | 0-12 | identical | 0.92 | ✓ | ? |
| swimmer #0 - dipping - towel #1 | 2-7 | holding (+3 more) | 0-12 | not judged yet | 0.42 | ✗ | ✗ |
| swimmer #0 - lifting - towel #1 | 7-10 | holding (+3 more) | 0-12 | not judged yet | 0.25 | ✗ | ✗ |
| swimmer #0 - looking at - towel #1 | 0-7, 9-11 | looking at (+3 more) | 0-12 | identical | 0.75 | ✓ | ? |
| swimmer #0 - rinsing - towel #1 | 2-11 | holding (+3 more) | 0-12 | not judged yet | 0.75 | ? | ? |
| swimmer #0 - splashing - ocean #3 | 3-9 | nothing for this pair | - | - | - | ✗ | ✗ |
| swimmer #0 - wearing - bra #7 | 0-11 | wearing | 0-12 | identical | 0.92 | ✓ | ? |
| swimmer #0 - wearing - bikini bottoms #8 | 0-11 | wearing | 0-12 | identical | 0.92 | ✓ | ? |
| swimmer #0 - wearing - band #11 | 0-11 | has | 0-12 | not judged yet | 0.92 | ? | ✗ |
| towel #1 - approaching - ocean #3 | 0-2 | nothing for this pair | - | - | - | ✗ | ✗ |
| towel #1 - moving away from - ocean #3 | 7-10 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (19): swimmer #0 - has - hair #9 [0-12]; swimmer #0 - in front of - sky #2 [0-4]; towel #1 - in front of - sky #2 [0-4]; swimmer #0 - in front of - ship #4 [0-4]; swimmer #0 - in front of - boat #5 [0-4]; swimmer #0 - in front of - boat #6 [0-4]; towel #1 - in front of - ship #4 [0-4]; towel #1 - in front of - boat #5 [0-4]; towel #1 - in front of - boat #6 [0-4]; hair #9 - on - swimmer #0 [0-12]


## 1253_TPxVj7do42I

7.5 s, 8 frames read | human: 21 objects, 35 relations | TRASER: 21 objects, 37 relations, valid JSON, 1738 tokens

**Objects: 8/21 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | person | person | identical | ✓ |
| 1 | person | person | identical | ✓ |
| 2 | ball pool | bead (uncertain) | mismatch | ✗ |
| 3 | ceiling | ceiling | identical | ✓ |
| 4 | wall | wall panel | not judged yet | ? |
| 5 | window blind | curtain | not judged yet | ? |
| 6 | blind | curtain | semantic overlap | ✓ |
| 7 | blind | curtain | semantic overlap | ✓ |
| 8 | blind | window | not judged yet | ? |
| 9 | blind | door frame (uncertain) | not judged yet | ? |
| 10 | wall | wall | identical | ✓ |
| 11 | switch | door handle | not judged yet | ? |
| 12 | cabinet | cabinet | identical | ✓ |
| 13 | countertop | bathtub (uncertain) | not judged yet | ? |
| 14 | switch | bowl | not judged yet | ? |
| 15 | shirt | jersey (uncertain) | not judged yet | ? |
| 16 | head | person | mismatch | ✗ |
| 17 | pants | sand mound | not judged yet | ? |
| 18 | cap | baseball cap | hypernym/hyponym | ✓ |
| 19 | head | person | mismatch | ✗ |
| 20 | t-shirt | jersey (uncertain) | not judged yet | ? |

**Relations: 6/35 right, triplets: 3/35 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - wearing - shirt #15 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - wearing - pants #17 | 0-6 | in front of (+1 more) | 0-2, 3-8 | not judged yet | 0.62 | ? | ? |
| person #0 - moving through - ball pool #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - in - ball pool #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - in front of - window blind #5 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ? |
| person #0 - pushing - person #1 | 5-7 | moving away from (+2 more) | 3-8 | not judged yet | 0.40 | ✗ | ✗ |
| person #0 - behind - person #1 | 0-7 | playing with (+2 more) | 0-8 | not judged yet | 0.88 | ? | ? |
| person #0 - in front of - person #1 | 6-8 | moving away from (+2 more) | 3-8 | mismatch | 0.40 | ✗ | ✗ |
| person #0 - pressing - switch #11 | 6-8 | below | 4-8 | not judged yet | 0.50 | ✗ | ✗ |
| person #1 - wearing - cap #18 | 0-8 | wearing | 0-2, 3-8 | identical | 0.88 | ✓ | ✓ |
| person #1 - wearing - t-shirt #20 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - in - ball pool #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - moving through - ball pool #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - in front of - window blind #5 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ? |
| person #1 - in front of - blind #6 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #1 - in front of - blind #7 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #1 - in front of - blind #8 | 0-8 | in front of (+1 more) | 0-8 | identical | 1.00 | ✓ | ? |
| person #1 - in front of - blind #9 | 2-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| ceiling #3 - above - ball pool #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| ceiling #3 - above - person #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| ceiling #3 - above - person #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| window blind #5 - above - ball pool #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| blind #6 - above - ball pool #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| blind #7 - above - ball pool #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| blind #8 - above - ball pool #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| blind #9 - above - ball pool #2 | 2-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| switch #11 - on - wall #10 | 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| countertop #13 - on - cabinet #12 | 1-2 | nothing for this pair | - | - | - | ✗ | ✗ |
| switch #14 - on - wall #10 | 1-2 | in front of | 0-1 | not judged yet | 0.00 | ✗ | ✗ |
| shirt #15 - on - person #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #16 - above - shirt #15 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| pants #17 - on - person #0 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| cap #18 - on - head #19 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #19 - above - t-shirt #20 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| t-shirt #20 - on - person #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (23): person #0 - in front of - blind #8 [0-8]; person #0 - below - blind #8 [0-8]; person #0 - in front of - wall #10 [0-8]; person #1 - in front of - wall #10 [0-8]; person #0 - in front of - blind #6 [0-8]; person #0 - in front of - blind #7 [0-8]; person #0 - in front of - wall #4 [0-8]; person #1 - in front of - wall #4 [0-8]; person #0 - below - ceiling #3 [0-8]; person #1 - below - ceiling #3 [0-8]


## 1256_Y_19xu4yTms

10.17 s, 10 frames read | human: 32 objects, 61 relations | TRASER: 32 objects, 73 relations, valid JSON, 3195 tokens

**Objects: 16/32 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | Person 1 | person | identical | ✓ |
| 1 | Person 2 | person | identical | ✓ |
| 2 | Person 3 | person | identical | ✓ |
| 3 | Person 4 | person | not judged yet | ? |
| 4 | Person 5 | person | identical | ✓ |
| 5 | Person 6 | person | identical | ✓ |
| 6 | Boat | boat | identical | ✓ |
| 7 | Sea | water | not judged yet | ? |
| 8 | sky | fog | not judged yet | ? |
| 9 | shark | dolphin | not judged yet | ? |
| 10 | cap | beanie | semantic overlap | ✓ |
| 11 | glass | sunglasses | mismatch | ✗ |
| 12 | sweater | jacket | not judged yet | ? |
| 13 | hair | hair | identical | ✓ |
| 14 | jacket | coat | synonym | ✓ |
| 15 | trouser | trousers (uncertain) | not judged yet | ? |
| 16 | head gear | hooded jacket | not judged yet | ? |
| 17 | camera | camera | identical | ✓ |
| 18 | head gear | hooded jacket | not judged yet | ? |
| 19 | trouser | trousers | not judged yet | ? |
| 20 | jacket | jacket | identical | ✓ |
| 21 | jacket | jacket | identical | ✓ |
| 22 | head warmer | beanie | hypernym/hyponym | ✓ |
| 23 | face | person | hypernym/hyponym | ✓ |
| 24 | jacket | jacket | identical | ✓ |
| 25 | head | person | mismatch | ✗ |
| 26 | jacket | jacket | identical | ✓ |
| 27 | seat | backpack | not judged yet | ? |
| 28 | seat | chair backrest | not judged yet | ? |
| 29 | seat | backpack | not judged yet | ? |
| 30 | seat | backpack | not judged yet | ? |
| 31 | seat | strap (uncertain) | not judged yet | ? |

**Relations: 7/61 right, triplets: 5/61 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| Person 1 #0 - behind - Person 2 #1 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 3 #2 - next to - Person 4 #3 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 6 #5 - behind - Person 3 #2 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 2 #1 - behind - Person 4 #3 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 1 #0 - behind - Person 3 #2 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 1 #0 - behind - Person 4 #3 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 1 #0 - beside - Person 5 #4 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 5 #4 - behind - Person 2 #1 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 5 #4 - behind - Person 3 #2 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 5 #4 - behind - Person 4 #3 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 5 #4 - behind - Person 6 #5 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 1 #0 - on - Boat #6 | 0-11.1667 | on | 0-11 | identical | 0.99 | ✓ | ✓ |
| Person 2 #1 - on - Boat #6 | 0-11.1667 | on | 0-11 | identical | 0.99 | ✓ | ✓ |
| Person 3 #2 - on - Boat #6 | 0-11.1667 | on | 0-11 | identical | 0.99 | ✓ | ✓ |
| Person 4 #3 - on - Boat #6 | 0-11.1667 | on | 0-11 | identical | 0.99 | ✓ | ? |
| Person 5 #4 - on - Boat #6 | 0-11.1667 | on | 0-11 | identical | 0.99 | ✓ | ✓ |
| Person 6 #5 - on - Boat #6 | 0-11.1667 | on | 0-11 | identical | 0.99 | ✓ | ✓ |
| Person 1 #0 - under - sky #8 | 8.16667-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 2 #1 - under - sky #8 | 8.16667-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 3 #2 - under - sky #8 | 8.16667-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 4 #3 - under - sky #8 | 8.16667-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 5 #4 - under - sky #8 | 8.16667-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 6 #5 - under - sky #8 | 8.16667-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Boat #6 - under - sky #8 | 8.16667-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Sea #7 - under - sky #8 | 8.16667-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| shark #9 - under - sky #8 | 8.16667-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| shark #9 - in - Sea #7 | 0-11.1667 | moving on (+1 more) | 0-11 | not judged yet | 0.99 | ? | ? |
| shark #9 - in front of - Boat #6 | 0-11.1667 | behind (+1 more) | 0-11 | not judged yet | 0.99 | ? | ? |
| Person 1 #0 - wears - sweater #12 | 0-11.1667 | wearing | 0-11 | not judged yet | 0.99 | ? | ? |
| Person 1 #0 - holds onto - seat #28 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 1 #0 - looks at - shark #9 | 0-11.1667 | looking at | 0-11 | not judged yet | 0.99 | ? | ? |
| Person 2 #1 - looks at - shark #9 | 0-11.1667 | looking at | 0-11 | not judged yet | 0.99 | ? | ? |
| Person 3 #2 - looks at - shark #9 | 0-11.1667 | looking at | 0-11 | not judged yet | 0.99 | ? | ? |
| Person 3 #2 - records - shark #9 | 0-11.1667 | looking at | 0-11 | not judged yet | 0.99 | ? | ? |
| Person 4 #3 - looks at - shark #9 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 5 #4 - looks at - shark #9 | 0-2, 2.66667-11.1667 | looking at | 0-11 | not judged yet | 0.93 | ? | ? |
| Person 6 #5 - looks at - shark #9 | 0-11.1667 | looking at | 0-11 | not judged yet | 0.99 | ? | ? |
| Person 1 #0 - wears - cap #10 | 0-11.1667 | wearing | 0-11 | not judged yet | 0.99 | ? | ? |
| Person 1 #0 - wears - glass #11 | 0-11.1667 | wearing | 0-11 | not judged yet | 0.99 | ? | ✗ |
| Person 2 #1 - has - hair #13 | 0-11.1667 | wearing | 0-11 | not judged yet | 0.99 | ? | ? |
| Person 2 #1 - wears - jacket #14 | 0-11.1667 | wearing | 0-11 | not judged yet | 0.99 | ? | ? |
| Person 2 #1 - wears - trouser #15 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 4 #3 - wears - head gear #16 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 4 #3 - wears - jacket #20 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 3 #2 - holds - camera #17 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 3 #2 - wears - head gear #18 | 0-11.1667 | wearing | 0-11 | not judged yet | 0.99 | ? | ? |
| Person 3 #2 - wears - jacket #21 | 0-11.1667 | wearing | 0-11 | not judged yet | 0.99 | ? | ? |
| Person 5 #4 - wears - head warmer #22 | 0-11.1667 | wearing | 0-11 | not judged yet | 0.99 | ? | ? |
| Person 5 #4 - wears - jacket #24 | 0-11.1667 | wearing | 0-11 | not judged yet | 0.99 | ? | ? |
| Person 6 #5 - has - head #25 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 6 #5 - wears - jacket #26 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 6 #5 - holds onto - seat #30 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 5 #4 - holds onto - seat #29 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 2 #1 - in front of - seat #27 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 2 #1 - on - Sea #7 | 0-11.1667 | in front of | 0-11 | not judged yet | 0.99 | ? | ? |
| Person 1 #0 - on - Sea #7 | 0-11.1667 | in front of | 0-11 | not judged yet | 0.99 | ? | ? |
| Person 3 #2 - on - Sea #7 | 0-11.1667 | in front of | 0-11 | not judged yet | 0.99 | ? | ? |
| Person 4 #3 - on - Sea #7 | 0-11.1667 | in front of | 0-11 | not judged yet | 0.99 | ? | ? |
| Person 5 #4 - on - Sea #7 | 0-11.1667 | in front of | 0-11 | not judged yet | 0.99 | ? | ? |
| Person 6 #5 - on - Sea #7 | 0-11.1667 | in front of | 0-11 | not judged yet | 0.99 | ? | ? |
| Boat #6 - on - Sea #7 | 0-11.1667 | moving on (+1 more) | 0-11 | hypernym/hyponym | 0.99 | ✓ | ? |

TRASER relations between pairs the humans did not annotate (41): Person 2 #1 - wearing - head gear #16 [0-11]; Person 2 #1 - wearing - jacket #20 [0-11]; Person 3 #2 - wearing - trouser #19 [0-11]; Person 5 #4 - holding - camera #17 [0-11]; Boat #6 - carrying - Person 1 #0 [0-11]; Boat #6 - carrying - Person 2 #1 [0-11]; Boat #6 - carrying - Person 3 #2 [0-11]; Boat #6 - carrying - Person 4 #3 [0-11]; Boat #6 - carrying - Person 5 #4 [0-11]; Boat #6 - carrying - Person 6 #5 [0-11]


## 1261_wsHfWwHXgLs

10.17 s, 10 frames read | human: 8 objects, 22 relations | TRASER: 8 objects, 18 relations, valid JSON, 721 tokens

**Objects: 3/8 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | ocean | dog | not judged yet | ? |
| 1 | sky | fog | not judged yet | ? |
| 2 | dog | dog | identical | ✓ |
| 3 | inflatable float | inflatable raft | synonym | ✓ |
| 4 | pinna | dog's ear | not judged yet | ? |
| 5 | side of a float | raft | not judged yet | ? |
| 6 | blanket | towel | semantic overlap | ✓ |
| 7 | side of a float | inflatable raft | not judged yet | ? |

**Relations: 4/22 right, triplets: 3/22 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| sky #1 - above - ocean #0 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #2 - riding - inflatable float #3 | 0-11 | riding (+1 more) | 0-13 | identical | 0.85 | ✓ | ✓ |
| dog #2 - on - inflatable float #3 | 0-11 | on (+1 more) | 0-13 | identical | 0.85 | ✓ | ✓ |
| dog #2 - resting on - blanket #6 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #2 - on - blanket #6 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #2 - moving over - ocean #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #2 - looking at - ocean #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #2 - rafting across - ocean #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #2 - above - ocean #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| inflatable float #3 - carrying - blanket #6 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| inflatable float #3 - drifting on - ocean #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| inflatable float #3 - on - ocean #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| inflatable float #3 - above - ocean #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| pinna #4 - attached to - dog #2 | 0-11 | part of | 0-13 | not judged yet | 0.85 | ? | ? |
| pinna #4 - part of - dog #2 | 0-11 | part of | 0-13 | identical | 0.85 | ✓ | ? |
| side of a float #5 - attached to - inflatable float #3 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| side of a float #5 - part of - inflatable float #3 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| blanket #6 - moving over - ocean #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| blanket #6 - above - ocean #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| blanket #6 - on - inflatable float #3 | 0-11 | on (+1 more) | 0-13 | identical | 0.85 | ✓ | ✓ |
| side of a float #7 - attached to - inflatable float #3 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| side of a float #7 - part of - inflatable float #3 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (13): dog #2 - riding - side of a float #5 [0-13]; dog #2 - on - side of a float #5 [0-13]; dog #2 - riding - side of a float #7 [0-13]; dog #2 - on - side of a float #7 [0-13]; blanket #6 - on - side of a float #5 [0-13]; blanket #6 - on - side of a float #7 [0-13]; inflatable float #3 - overlapping - side of a float #5 [0-13]; inflatable float #3 - overlapping - side of a float #7 [0-13]; side of a float #5 - overlapping - side of a float #7 [0-13]; sky #1 - above - dog #2 [0-8]


## 1268_h58xqlUE5xA

10.17 s, 10 frames read | human: 11 objects, 21 relations | TRASER: 11 objects, 36 relations, valid JSON, 1071 tokens

**Objects: 2/11 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | person | person | identical | ✓ |
| 1 | railings | railing | not judged yet | ? |
| 2 | sky | clouds | not judged yet | ? |
| 3 | trees | hill | not judged yet | ? |
| 4 | waterfall | waterfall | identical | ✓ |
| 5 | waterfall | cliff | not judged yet | ? |
| 6 | trees and waterfall | cliff | not judged yet | ? |
| 7 | trees and mist | tree | not judged yet | ? |
| 8 | shirt | person | not judged yet | ? |
| 9 | head | person | mismatch | ✗ |
| 10 | trousers | person | not judged yet | ? |

**Relations: 7/21 right, triplets: 0/21 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - holding - railings #1 | 0-11 | standing on (+1 more) | 0-10 | not judged yet | 0.91 | ? | ? |
| person #0 - behind - railings #1 | 0-11 | standing on (+1 more) | 0-10 | not judged yet | 0.91 | ? | ? |
| person #0 - wearing - shirt #8 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - wearing - trousers #10 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - watching - waterfall #4 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - in front of - trees #3 | 0-11 | in front of | 0-10 | identical | 0.91 | ✓ | ? |
| railings #1 - in front of - trees #3 | 0-11 | in front of | 0-10 | identical | 0.91 | ✓ | ? |
| sky #2 - above - waterfall #4 | 0-11 | above | 0-10 | identical | 0.91 | ✓ | ? |
| sky #2 - above - waterfall #5 | 0-11 | above | 0-10 | identical | 0.91 | ✓ | ? |
| sky #2 - above - trees and waterfall #6 | 0-11 | above | 0-10 | identical | 0.91 | ✓ | ? |
| sky #2 - above - trees and mist #7 | 0-11 | above | 0-10 | identical | 0.91 | ✓ | ? |
| sky #2 - above - trees #3 | 0-11 | above | 0-10 | identical | 0.91 | ✓ | ? |
| waterfall #4 - flowing down - trees #3 | 0-11 | in front of | 0-10 | not judged yet | 0.91 | ? | ? |
| waterfall #5 - flowing down - trees #3 | 0-11 | in front of | 0-10 | not judged yet | 0.91 | ? | ? |
| trees and waterfall #6 - flowing down - trees #3 | 0-11 | in front of | 0-10 | not judged yet | 0.91 | ? | ? |
| trees and mist #7 - flowing down - trees #3 | 0-11 | in front of | 0-10 | not judged yet | 0.91 | ? | ? |
| shirt #8 - overlapping - person #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #8 - above - trousers #10 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #9 - above - shirt #8 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #9 - above - trousers #10 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| trousers #10 - overlapping - person #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (23): shirt #8 - standing on - railings #1 [0-10]; shirt #8 - on - railings #1 [0-10]; head #9 - standing on - railings #1 [0-10]; head #9 - on - railings #1 [0-10]; trousers #10 - standing on - railings #1 [0-10]; trousers #10 - on - railings #1 [0-10]; waterfall #4 - flowing down - trees and waterfall #6 [0-10]; waterfall #4 - flowing down - waterfall #5 [0-10]; railings #1 - in front of - waterfall #4 [0-10]; railings #1 - in front of - waterfall #5 [0-10]


## 1275_ARcg-EyKWrA

10.17 s, 10 frames read | human: 68 objects, 21 relations | TRASER: 40 objects, 47 relations, valid JSON, 2956 tokens

**Objects: 12/68 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | cage | birdcage | hypernym/hyponym | ✓ |
| 1 | chest of drawers | wooden cabinet | semantic overlap | ✓ |
| 2 | floor | cat | mismatch | ✗ |
| 3 | framed poster | poster | hypernym/hyponym | ✓ |
| 4 | jar | toy (uncertain) | not judged yet | ? |
| 5 | curtain | window | not judged yet | ? |
| 6 | furniture | cat | mismatch | ✗ |
| 7 | person | person | identical | ✓ |
| 8 | faucet | box | mismatch | ✗ |
| 9 | household material | plush toy (uncertain) | not judged yet | ? |
| 10 | household material | toy (uncertain) | mismatch | ✗ |
| 11 | furniture | cat | mismatch | ✗ |
| 12 | wall | wall | identical | ✓ |
| 13 | curtain | curtain | identical | ✓ |
| 14 | socket | wall socket | not judged yet | ? |
| 15 | window | window | identical | ✓ |
| 16 | cat | cat | identical | ✓ |
| 17 | shirt | jersey | not judged yet | ? |
| 18 | shorts | trousers | not judged yet | ? |
| 19 | face | neck (uncertain) | not judged yet | ? |
| 20 | hand | arm | semantic overlap | ✓ |
| 21 | leg | shoe (uncertain) | not judged yet | ? |
| 22 | leg | shoe (uncertain) | not judged yet | ? |
| 23 | hand | tail (uncertain) | mismatch | ✗ |
| 24 | legs | tail (uncertain) | mismatch | ✗ |
| 25 | tail | tail (uncertain) | identical | ✓ |
| 26 | head | cat | mismatch | ✗ |
| 27 | leg | tail (uncertain) | mismatch | ✗ |
| 28 | leg | tail (uncertain) | mismatch | ✗ |
| 29 | cage toy | ball (uncertain) | semantic overlap | ✓ |
| 30 | cage toy | toy (uncertain) | hypernym/hyponym | ✓ |
| 31 | toy, cross | toy (uncertain) | not judged yet | ? |
| 32 | cage toy | birdcage | mismatch | ✗ |
| 33 | cage toy | birdcage | mismatch | ✗ |
| 34 | cage toy | birdcage | mismatch | ✗ |
| 35 | cage toy | birdcage | mismatch | ✗ |
| 36 | frame | pole (uncertain) | mismatch | ✗ |
| 37 | frame | birdcage | mismatch | ✗ |
| 38 | frame | pole (uncertain) | mismatch | ✗ |
| 39 | frame | pole (uncertain) | mismatch | ✗ |
| 40 | frame | - | no label from TRASER | ✗ |
| 41 | frame | - | no label from TRASER | ✗ |
| 42 | frame | - | no label from TRASER | ✗ |
| 43 | frame | - | no label from TRASER | ✗ |
| 44 | frame | - | no label from TRASER | ✗ |
| 45 | frame | - | no label from TRASER | ✗ |
| 46 | jar cover | - | no label from TRASER | ✗ |
| 47 | jar | - | no label from TRASER | ✗ |
| 48 | jar handle | - | no label from TRASER | ✗ |
| 49 | wall frame | - | no label from TRASER | ✗ |
| 50 | window | - | no label from TRASER | ✗ |
| 51 | wall | - | no label from TRASER | ✗ |
| 52 | wall | - | no label from TRASER | ✗ |
| 53 | wall | - | no label from TRASER | ✗ |
| 54 | wall molding | - | no label from TRASER | ✗ |
| 55 | household material | - | no label from TRASER | ✗ |
| 56 | cage frame | - | no label from TRASER | ✗ |
| 57 | lamp base | - | no label from TRASER | ✗ |
| 58 | lamp shade | - | no label from TRASER | ✗ |
| 59 | drawer handle | - | no label from TRASER | ✗ |
| 60 | drawer handle | - | no label from TRASER | ✗ |
| 61 | drawer handle | - | no label from TRASER | ✗ |
| 62 | drawer handle | - | no label from TRASER | ✗ |
| 63 | drawer handle | - | no label from TRASER | ✗ |
| 64 | drawer handle | - | no label from TRASER | ✗ |
| 65 | bag | - | no label from TRASER | ✗ |
| 66 | cage base | - | no label from TRASER | ✗ |
| 67 | baseboard | - | no label from TRASER | ✗ |

**Relations: 3/21 right, triplets: 3/21 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| cage #0 - on - floor #2 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| cage #0 - in front of - wall #12 | 0-11 | in front of | 0-11 | identical | 1.00 | ✓ | ✓ |
| chest of drawers #1 - in front of - wall #12 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| jar #4 - on - chest of drawers #1 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #7 - hold - cat #16 | 0-11 | holding (+2 more) | 0-11 | not judged yet | 1.00 | ? | ? |
| person #7 - look at - cat #16 | 0-11 | holding (+2 more) | 0-11 | not judged yet | 1.00 | ? | ? |
| person #7 - help climb cage - cat #16 | 0-11 | holding (+2 more) | 0-11 | not judged yet | 1.00 | ? | ? |
| person #7 - next to - cage #0 | 0-11 | in front of | 0-11 | mismatch | 1.00 | ✗ | ✗ |
| faucet #8 - above - chest of drawers #1 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #15 - in - wall #12 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| cat #16 - grip - cage #0 | 0-11 | inside (+1 more) | 0-11 | not judged yet | 1.00 | ? | ? |
| cat #16 - climb - cage #0 | 0-11 | inside (+1 more) | 0-11 | not judged yet | 1.00 | ? | ? |
| cat #16 - touching - cage #0 | 0-11 | inside (+1 more) | 0-11 | not judged yet | 1.00 | ? | ? |
| cat #16 - in front of - cage #0 | 0-11 | in front of (+1 more) | 0-11 | identical | 1.00 | ✓ | ✓ |
| cat #16 - look at - toy, cross #31 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| cat #16 - above - floor #2 | 0-11 | in front of | 0-11 | not judged yet | 1.00 | ? | ✗ |
| cat #16 - in front of - chest of drawers #1 | 0-11 | in front of | 0-11 | identical | 1.00 | ✓ | ✓ |
| cat #16 - below - jar #4 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #20 - touching - cat #16 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #23 - touching - cat #16 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| toy, cross #31 - inside - cage #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (38): person #7 - wearing - shirt #17 [0-11]; person #7 - wearing - shorts #18 [0-11]; cat #16 - moving around - person #7 [0-11]; cat #16 - in front of - person #7 [0-11]; cat #16 - below - person #7 [0-11]; head #26 - inside - cage #0 [0-11]; head #26 - in front of - cage #0 [0-11]; cage #0 - in front of - curtain #5 [0-11]; cage #0 - in front of - window #15 [0-11]; cage #0 - in front of - chest of drawers #1 [0-11]


## 1308_-C_XboJfD0g

10.17 s, 10 frames read | human: 14 objects, 15 relations | TRASER: 14 objects, 27 relations, valid JSON, 1367 tokens

**Objects: 1/14 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | shelf | cell phone | not judged yet | ? |
| 1 | hand | hand | identical | ✓ |
| 2 | pricetag | tag (uncertain) | not judged yet | ? |
| 3 | floor | tabletop | not judged yet | ? |
| 4 | screen | television set | not judged yet | ? |
| 5 | phone | cellular telephone (uncertain) | not judged yet | ? |
| 6 | phone holder | power strip | not judged yet | ? |
| 7 | phone | device (uncertain) | not judged yet | ? |
| 8 | ipad | cellular telephone (uncertain) | not judged yet | ? |
| 9 | accessories | box | not judged yet | ? |
| 10 | counter top | cell phone | mismatch | ✗ |
| 11 | wood | box | not judged yet | ? |
| 12 | wood | box | not judged yet | ? |
| 13 | metal base | drawer front (uncertain) | mismatch | ✗ |

**Relations: 1/15 right, triplets: 0/15 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| shelf #0 - on - floor #3 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #1 - moves along - shelf #0 | 0-6 | touching (+2 more) | 0-6 | not judged yet | 1.00 | ? | ? |
| hand #1 - in front of - shelf #0 | 0-6 | in front of (+2 more) | 0-7 | identical | 0.86 | ✓ | ? |
| hand #1 - approaches - pricetag #2 | 0-4 | nothing for this pair | - | - | - | ✗ | ✗ |
| pricetag #2 - on - shelf #0 | 0-4, 5-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| pricetag #2 - above - accessories #9 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| screen #4 - on - shelf #0 | 0-3, 4-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| phone #5 - beside - phone holder #6 | 4-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| phone #5 - on - shelf #0 | 4-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| phone holder #6 - on - shelf #0 | 0-1, 2-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| phone #7 - on - shelf #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| ipad #8 - beside - phone #5 | 5-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| ipad #8 - on - shelf #0 | 5-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| accessories #9 - below - counter top #10 | 0-3 | in front of | 0-4 | not judged yet | 0.75 | ? | ✗ |
| accessories #9 - inside - shelf #0 | 0-3 | in front of | 0-4 | not judged yet | 0.75 | ? | ? |

TRASER relations between pairs the humans did not annotate (22): hand #1 - in front of - counter top #10 [0-7]; hand #1 - in front of - phone holder #6 [0-1, 2-7]; hand #1 - in front of - screen #4 [0-1, 2-7]; shelf #0 - in front of - phone holder #6 [0-1, 2-12]; shelf #0 - in front of - screen #4 [0-1, 2-12]; counter top #10 - in front of - phone holder #6 [0-1, 2-12]; counter top #10 - in front of - screen #4 [0-1, 2-12]; phone holder #6 - in front of - screen #4 [0-1, 2-12]; accessories #9 - in front of - phone holder #6 [0-1, 2-4]; accessories #9 - in front of - screen #4 [0-1, 2-4]


## 1352_nt-UZxGk9Bg

10.17 s, 10 frames read | human: 14 objects, 35 relations | TRASER: 14 objects, 43 relations, valid JSON, 1397 tokens

**Objects: 3/14 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | person | person | identical | ✓ |
| 1 | snow | snowboarder | not judged yet | ? |
| 2 | snowfeet | ski | not judged yet | ? |
| 3 | ski poles | ski pole | not judged yet | ? |
| 4 | skating stick | ski pole | not judged yet | ? |
| 5 | skating stick | ski pole | not judged yet | ? |
| 6 | snowboard | ski | not judged yet | ? |
| 7 | snowboard | ski | not judged yet | ? |
| 8 | face cap | helmet | semantic overlap | ✓ |
| 9 | face | goggles | mismatch | ✗ |
| 10 | hoodie | jacket | hypernym/hyponym | ✓ |
| 11 | trouser | trousers | not judged yet | ? |
| 12 | shoe | ski | not judged yet | ? |
| 13 | shoe | ski boot | not judged yet | ? |

**Relations: 5/35 right, triplets: 2/35 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - on - snow #1 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - move across - snow #1 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - ski - snow #1 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - hold - skating stick #4 | 0-11 | holding | 0-10 | not judged yet | 0.91 | ? | ? |
| person #0 - hold - skating stick #5 | 0-11 | holding | 0-10 | not judged yet | 0.91 | ? | ? |
| person #0 - stand on - snowboard #6 | 0-11 | riding (+2 more) | 0-10 | not judged yet | 0.91 | ? | ? |
| person #0 - stand on - snowboard #7 | 0-11 | riding (+2 more) | 0-10 | not judged yet | 0.91 | ? | ? |
| person #0 - wear - face cap #8 | 0-11 | wearing | 0-10 | not judged yet | 0.91 | ? | ? |
| person #0 - wear - hoodie #10 | 0-11 | wearing | 0-10 | not judged yet | 0.91 | ? | ? |
| person #0 - wear - trouser #11 | 0-11 | wearing | 0-10 | not judged yet | 0.91 | ? | ? |
| person #0 - wear - shoe #12 | 0-11 | riding (+2 more) | 0-10 | not judged yet | 0.91 | ? | ? |
| person #0 - wear - shoe #13 | 0-11 | wearing | 0-10 | not judged yet | 0.91 | ? | ? |
| snowfeet #2 - below - shoe #12 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| snowfeet #2 - below - shoe #13 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| ski poles #3 - above - snow #1 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| skating stick #4 - attached to - ski poles #3 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| skating stick #4 - move with - person #0 | 0-11 | near | 0-10 | not judged yet | 0.91 | ? | ? |
| skating stick #5 - attached to - ski poles #3 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| skating stick #5 - move with - person #0 | 0-11 | near | 0-10 | not judged yet | 0.91 | ? | ? |
| snowboard #6 - on - snow #1 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| snowboard #6 - move with - person #0 | 0-11 | below | 0-10 | not judged yet | 0.91 | ? | ? |
| snowboard #7 - on - snow #1 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| snowboard #7 - move with - person #0 | 0-11 | below | 0-10 | not judged yet | 0.91 | ? | ? |
| face cap #8 - above - face #9 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| face cap #8 - on - person #0 | 0-11 | on | 0-10 | identical | 0.91 | ✓ | ✓ |
| face #9 - above - hoodie #10 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| hoodie #10 - above - trouser #11 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| hoodie #10 - on - person #0 | 0-11 | on | 0-10 | identical | 0.91 | ✓ | ✓ |
| trouser #11 - above - shoe #12 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| trouser #11 - above - shoe #13 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| trouser #11 - on - person #0 | 0-11 | on | 0-10 | identical | 0.91 | ✓ | ? |
| shoe #12 - on - snowboard #7 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| shoe #12 - on - person #0 | 0-11 | below | 0-10 | not judged yet | 0.91 | ? | ? |
| shoe #13 - on - snowboard #6 | 0-11 | on | 0-10 | identical | 0.91 | ✓ | ? |
| shoe #13 - on - person #0 | 0-11 | on | 0-10 | identical | 0.91 | ✓ | ? |

TRASER relations between pairs the humans did not annotate (18): person #0 - wearing - face #9 [0-10]; person #0 - holding - ski poles #3 [0-10]; face #9 - on - person #0 [0-10]; shoe #13 - on - snowboard #7 [0-10]; shoe #13 - on - shoe #12 [0-10]; ski poles #3 - near - person #0 [0-10]; ski poles #3 - above - snowboard #6 [0-10]; skating stick #4 - above - snowboard #6 [0-10]; skating stick #5 - above - snowboard #6 [0-10]; ski poles #3 - above - snowboard #7 [0-10]


## 1480_WAGXu9_6Uv0

7.5 s, 8 frames read | human: 46 objects, 41 relations | TRASER: 40 objects, 42 relations, valid JSON, 3214 tokens

**Objects: 12/46 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | sink | sink | identical | ✓ |
| 1 | bathroom tap | faucet | not judged yet | ? |
| 2 | cup | bottle | semantic overlap | ✓ |
| 3 | bathroom product | bottle | hypernym/hyponym | ✓ |
| 4 | bathroom container | bottle | not judged yet | ? |
| 5 | toothbrush | bottle | not judged yet | ? |
| 6 | toothpaste | bottle | not judged yet | ? |
| 7 | bathroom product | cup | not judged yet | ? |
| 8 | toothbrush | bottle | not judged yet | ? |
| 9 | cord | bottle | mismatch | ✗ |
| 10 | paper towel | toilet paper roll | semantic overlap | ✓ |
| 11 | towel | curtain | not judged yet | ? |
| 12 | bathroom counter | sink | semantic overlap | ✓ |
| 13 | wall | mirror (uncertain) | not judged yet | ? |
| 14 | switch | wall socket | not judged yet | ? |
| 15 | towel | curtain | not judged yet | ? |
| 16 | door handle | door handle | identical | ✓ |
| 17 | door hanger | handle (uncertain) | mismatch | ✗ |
| 18 | brush | toothbrush (uncertain) | not judged yet | ? |
| 19 | wall | curtain | mismatch | ✗ |
| 20 | chain lock | pipe (uncertain) | not judged yet | ? |
| 21 | door trim | refrigerator | mismatch | ✗ |
| 22 | door | refrigerator | mismatch | ✗ |
| 23 | mirror | mirror | identical | ✓ |
| 24 | door accessory | bottle | not judged yet | ? |
| 25 | door handle | doorknob | not judged yet | ? |
| 26 | door | curtain | mismatch | ✗ |
| 27 | cabinet | cabinet door | semantic overlap | ✓ |
| 28 | floor | drawer (uncertain) | mismatch | ✗ |
| 29 | frame | sink | not judged yet | ? |
| 30 | bathroom supply | bottle | hypernym/hyponym | ✓ |
| 31 | toothpaste | bottle | not judged yet | ? |
| 32 | towel | mirror | not judged yet | ? |
| 33 | tube | bottle | not judged yet | ? |
| 34 | towel | roll of toilet paper | not judged yet | ? |
| 35 | bathroom supply | bottle | hypernym/hyponym | ✓ |
| 36 | counter | countertop (uncertain) | synonym | ✓ |
| 37 | drain hole | drain cover (uncertain) | semantic overlap | ✓ |
| 38 | tap handle | faucet | not judged yet | ? |
| 39 | tap handle | faucet | not judged yet | ? |
| 40 | cabinet handle | - | no label from TRASER | ✗ |
| 41 | cabinet handle | - | no label from TRASER | ✗ |
| 42 | cabinet handle | - | no label from TRASER | ✗ |
| 43 | cabinet handle | - | no label from TRASER | ✗ |
| 44 | cabinet handle | - | no label from TRASER | ✗ |
| 45 | cabinet handle | - | no label from TRASER | ✗ |

**Relations: 2/41 right, triplets: 0/41 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| sink #0 - built into - bathroom counter #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| sink #0 - above - cabinet #27 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bathroom tap #1 - above - sink #0 | 0-8 | attached to (+1 more) | 0-8 | not judged yet | 1.00 | ? | ? |
| bathroom tap #1 - attached to - sink #0 | 0-8 | attached to (+1 more) | 0-8 | identical | 1.00 | ✓ | ? |
| bathroom tap #1 - mounted on - bathroom counter #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bathroom tap #1 - in front of - mirror #23 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| cup #2 - on - bathroom counter #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| cup #2 - in front of - mirror #23 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bathroom product #3 - on - bathroom counter #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bathroom container #4 - on - bathroom counter #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| toothbrush #5 - on - bathroom counter #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| toothpaste #6 - on - bathroom counter #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bathroom product #7 - on - bathroom counter #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| toothbrush #8 - on - bathroom counter #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| cord #9 - attached to - toothbrush #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| paper towel #10 - on - bathroom counter #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| paper towel #10 - in front of - mirror #23 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| towel #11 - on - door #26 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bathroom counter #12 - on - cabinet #27 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| switch #14 - on - door trim #21 | 0-1, 2-8 | on (+1 more) | 0-8 | identical | 0.88 | ✓ | ✗ |
| towel #15 - on - door #22 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| door handle #16 - attached to - door #22 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| door handle #16 - attached to - door #22 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| brush #18 - in front of - door trim #21 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| mirror #23 - above - bathroom counter #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| door handle #25 - attached to - door #26 | 0-1, 4-5.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| door handle #25 - attached to - door #26 | 0-1, 4-5.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| cabinet #27 - attached to - bathroom counter #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| frame #29 - attached to - mirror #23 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| frame #29 - attached to - mirror #23 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bathroom supply #30 - on - bathroom counter #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| toothpaste #31 - on - bathroom counter #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| towel #32 - above - bathroom counter #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| tube #33 - on - bathroom counter #12 | 1-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| towel #34 - above - bathroom counter #12 | 5.5-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| drain hole #37 - attached to - sink #0 | 0-4, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| drain hole #37 - inside - sink #0 | 0-4.5, 5.5-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| tap handle #38 - attached to - bathroom tap #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| tap handle #38 - attached to - bathroom tap #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| tap handle #39 - attached to - tap handle #39 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| cabinet handle #43 - attached to - cabinet #27 | 0-7.5 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (38): tap handle #39 - attached to - sink #0 [0-8]; tap handle #39 - on - sink #0 [0-8]; tap handle #38 - attached to - sink #0 [0-8]; tap handle #38 - on - sink #0 [0-8]; paper towel #10 - attached to - door trim #21 [0-8]; paper towel #10 - on - door trim #21 [0-8]; door handle #16 - attached to - door trim #21 [0-8]; door handle #16 - on - door trim #21 [0-8]; door handle #25 - attached to - cabinet #27 [0-8]; door handle #25 - on - cabinet #27 [0-8]


## 1503_gwrvCEAZVl0

7.5 s, 8 frames read | human: 20 objects, 34 relations | TRASER: 20 objects, 68 relations, valid JSON, 2313 tokens

**Objects: 7/20 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | trees | trees | identical | ✓ |
| 1 | sky | excavator arm | not judged yet | ? |
| 2 | person | person | identical | ✓ |
| 3 | sand | dirt mound | not judged yet | ? |
| 4 | excavator | excavator arm | hypernym/hyponym | ✓ |
| 5 | grass | field | semantic overlap | ✓ |
| 6 | trees | tree | not judged yet | ? |
| 7 | trees | bush | not judged yet | ? |
| 8 | cap | baseball cap | hypernym/hyponym | ✓ |
| 9 | shirt | jacket | not judged yet | ? |
| 10 | trouser | trousers (uncertain) | not judged yet | ? |
| 11 | face | baseball cap | not judged yet | ? |
| 12 | bucket | dump truck bed (uncertain) | mismatch | ✗ |
| 13 | bucket cyclinder | excavator arm | semantic overlap | ✓ |
| 14 | cab | window frame (uncertain) | mismatch | ✗ |
| 15 | sand | dirt mound | not judged yet | ? |
| 16 | sand | mound of dirt | not judged yet | ? |
| 17 | sand | mound of dirt | not judged yet | ? |
| 18 | sand | mound of dirt | not judged yet | ? |
| 19 | cab window | window frame (uncertain) | semantic overlap | ✓ |

**Relations: 3/34 right, triplets: 2/34 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| trees #0 - under - sky #1 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #6 - under - sky #1 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #7 - under - sky #1 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - under - sky #1 | 0-8.5 | in front of | 0-9 | not judged yet | 0.94 | ? | ? |
| excavator #4 - under - sky #1 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| sand #3 - under - sky #1 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #5 - under - sky #1 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #5 - under - sky #1 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - observe - excavator #4 | 2.33333-8.5 | in front of (+1 more) | 0-9 | not judged yet | 0.69 | ? | ? |
| person #2 - left of - excavator #4 | 0-8.5 | in front of (+1 more) | 0-9 | not judged yet | 0.94 | ? | ? |
| person #2 - wears - shirt #9 | 0-8.5 | in front of (+1 more) | 0-9 | not judged yet | 0.94 | ? | ? |
| person #2 - wears - trouser #10 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| bucket #12 - part of - excavator #4 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| bucket cyclinder #13 - part of - excavator #4 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| cab window #19 - part of - cab #14 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - near - bucket #12 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - standing on - sand #3 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| excavator #4 - in front of - trees #0 | 0-8.5 | in front of (+1 more) | 0-9 | identical | 0.94 | ✓ | ✓ |
| excavator #4 - in front of - trees #6 | 0-8.5 | above | 0-9 | mismatch | 0.94 | ✗ | ✗ |
| excavator #4 - in front of - trees #7 | 0-8.5 | in front of (+1 more) | 0-9 | identical | 0.94 | ✓ | ? |
| excavator #4 - in front of - grass #5 | 0-8.5 | in front of (+1 more) | 0-9 | identical | 0.94 | ✓ | ✓ |
| excavator #4 - digging - sand #3 | 0-8.5 | above | 0-9 | not judged yet | 0.94 | ? | ? |
| bucket #12 - digging - sand #3 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| bucket #12 - contacting - sand #3 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #5 - behind - sand #3 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #5 - behind - sand #15 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #5 - behind - sand #16 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #5 - behind - sand #17 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #5 - behind - sand #18 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #5 - behind - person #2 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #5 - behind - excavator #4 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| bucket cyclinder #13 - above - bucket #12 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| bucket #12 - attached to - bucket cyclinder #13 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - has - face #11 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (55): person #2 - wearing - cap #8 [0-8]; person #2 - in front of - cap #8 [0-8]; excavator #4 - moving toward - person #2 [0-8]; excavator #4 - moving away from - person #2 [7-9]; person #2 - in front of - trees #0 [0-9]; person #2 - in front of - grass #5 [0-9]; person #2 - in front of - trees #7 [0-9]; person #2 - in front of - sand #15 [0-9]; person #2 - in front of - sand #16 [0-9]; person #2 - in front of - sand #17 [0-9]


## 1638_MhoaeR88gm4

7.5 s, 8 frames read | human: 63 objects, 10 relations | TRASER: 40 objects, 49 relations, valid JSON, 2994 tokens

**Objects: 16/63 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | chair | chair | identical | ✓ |
| 1 | chair | chair | identical | ✓ |
| 2 | chair | chair | identical | ✓ |
| 3 | chair | signboard | mismatch | ✗ |
| 4 | chair | chair | identical | ✓ |
| 5 | chair | chair | identical | ✓ |
| 6 | chair | chair | identical | ✓ |
| 7 | chair | chair | identical | ✓ |
| 8 | chair | chair | identical | ✓ |
| 9 | chair | chair | identical | ✓ |
| 10 | chair | chair | identical | ✓ |
| 11 | chair | chair | identical | ✓ |
| 12 | chair | chair | identical | ✓ |
| 13 | chair | chair | identical | ✓ |
| 14 | floor | chair | mismatch | ✗ |
| 15 | table | chair | mismatch | ✗ |
| 16 | table | chair | mismatch | ✗ |
| 17 | table | chair | mismatch | ✗ |
| 18 | table | chair | mismatch | ✗ |
| 19 | window | signboard | not judged yet | ? |
| 20 | window | window | identical | ✓ |
| 21 | ceiling | ceiling | identical | ✓ |
| 22 | towel | chair | not judged yet | ? |
| 23 | towel | chair | not judged yet | ? |
| 24 | towel | chair | not judged yet | ? |
| 25 | towel | chair | not judged yet | ? |
| 26 | window | vent (uncertain) | not judged yet | ? |
| 27 | towel | chair | not judged yet | ? |
| 28 | towel | chair | not judged yet | ? |
| 29 | towel | chair | not judged yet | ? |
| 30 | towel | chair | not judged yet | ? |
| 31 | towel | chair | not judged yet | ? |
| 32 | towel | chair | not judged yet | ? |
| 33 | towel | chair | not judged yet | ? |
| 34 | towel | chair | not judged yet | ? |
| 35 | towel | chair | not judged yet | ? |
| 36 | window | wall panel | not judged yet | ? |
| 37 | exit sign | signboard | hypernym/hyponym | ✓ |
| 38 | counter | signboard | mismatch | ✗ |
| 39 | counter | wooden panel | not judged yet | ? |
| 40 | pillar | - | no label from TRASER | ✗ |
| 41 | decoration item | - | no label from TRASER | ✗ |
| 42 | counter | - | no label from TRASER | ✗ |
| 43 | decoration item | - | no label from TRASER | ✗ |
| 44 | window | - | no label from TRASER | ✗ |
| 45 | window | - | no label from TRASER | ✗ |
| 46 | pillar | - | no label from TRASER | ✗ |
| 47 | pillar | - | no label from TRASER | ✗ |
| 48 | pillar | - | no label from TRASER | ✗ |
| 49 | pillar | - | no label from TRASER | ✗ |
| 50 | towel | - | no label from TRASER | ✗ |
| 51 | logo | - | no label from TRASER | ✗ |
| 52 | counter door | - | no label from TRASER | ✗ |
| 53 | box | - | no label from TRASER | ✗ |
| 54 | box | - | no label from TRASER | ✗ |
| 55 | box | - | no label from TRASER | ✗ |
| 56 | chair | - | no label from TRASER | ✗ |
| 57 | chair | - | no label from TRASER | ✗ |
| 58 | poster or logo | - | no label from TRASER | ✗ |
| 59 | poster or logo | - | no label from TRASER | ✗ |
| 60 | decoration item | - | no label from TRASER | ✗ |
| 61 | decoration item | - | no label from TRASER | ✗ |
| 62 | poster or logo | - | no label from TRASER | ✗ |

**Relations: 0/10 right, triplets: 0/10 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| towel #27 - on - chair #7 | 4-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| towel #28 - on - chair #8 | 4-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| towel #29 - on - chair #9 | 5-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| towel #30 - on - chair #10 | 5-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| towel #31 - on - chair #11 | 3-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| towel #32 - on - chair #11 | 2-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| towel #33 - on - chair #13 | 0.5-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| box #53 - on - counter #39 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| box #54 - on - counter #39 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| box #55 - on - counter #39 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (49): chair #0 - in front of - counter #39 [0-4]; chair #1 - in front of - counter #39 [0-4]; chair #5 - in front of - counter #39 [0-5]; chair #6 - in front of - counter #39 [0-5]; floor #14 - in front of - counter #39 [0-8]; table #17 - in front of - counter #39 [0-8]; window #20 - above - counter #39 [0-8]; window #19 - above - counter #39 [0-8]; counter #38 - above - counter #39 [0-4]; chair #3 - above - counter #39 [0-3]


## 1691_md-DpQ4HX7Q

7.5 s, 8 frames read | human: 21 objects, 39 relations | TRASER: 21 objects, 65 relations, valid JSON, 2183 tokens

**Objects: 4/21 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | ship | boat | not judged yet | ? |
| 1 | bridge | bridge | identical | ✓ |
| 2 | sky | cloud | semantic overlap | ✓ |
| 3 | trees | hill | not judged yet | ? |
| 4 | trees | hill | not judged yet | ? |
| 5 | trees | hill | not judged yet | ? |
| 6 | trees | hill | not judged yet | ? |
| 7 | tower | ship | not judged yet | ? |
| 8 | ship | boat | not judged yet | ? |
| 9 | ship | boat | not judged yet | ? |
| 10 | ship | boat | not judged yet | ? |
| 11 | boat | mast | not judged yet | ? |
| 12 | river | boat | not judged yet | ? |
| 13 | people | crowd | synonym | ✓ |
| 14 | ship's bridge | radar dome | not judged yet | ? |
| 15 | paddle wheel | boat | mismatch | ✗ |
| 16 | barricade | signboard | mismatch | ✗ |
| 17 | roof | awning | not judged yet | ? |
| 18 | hull | boat | semantic overlap | ✓ |
| 19 | safety railing | radar dome | not judged yet | ? |
| 20 | ships rear | boat | not judged yet | ? |

**Relations: 15/39 right, triplets: 0/39 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| ship #0 - in front of - ship #8 | 0-8 | in front of (+1 more) | 0-9 | identical | 0.89 | ✓ | ? |
| ship #0 - in front of - ship #9 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ? |
| ship #0 - in front of - ship #10 | 0-8 | in front of (+1 more) | 0-9 | identical | 0.89 | ✓ | ? |
| ship #0 - in front of - boat #11 | 0-8 | has | 0-9 | not judged yet | 0.89 | ? | ? |
| ship #0 - in front of - tower #7 | 0-8 | in front of (+1 more) | 0-9 | identical | 0.89 | ✓ | ? |
| ship #0 - in front of - trees #3 | 0-8 | in front of (+1 more) | 0-9 | identical | 0.89 | ✓ | ? |
| ship #0 - in front of - trees #5 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ? |
| ship #0 - below - sky #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| ship #0 - carrying - people #13 | 0-8 | has | 0-9 | not judged yet | 0.89 | ? | ? |
| ship #0 - moving on - river #12 | 0-8 | in front of | 0-9 | not judged yet | 0.89 | ? | ? |
| ship #0 - on - river #12 | 0-8 | in front of | 0-9 | not judged yet | 0.89 | ? | ? |
| ship #0 - passing under - bridge #1 | 0-8 | approaches (+1 more) | 0-9 | not judged yet | 0.89 | ? | ? |
| ship #0 - navigating under - bridge #1 | 0-8 | approaches (+1 more) | 0-9 | not judged yet | 0.89 | ? | ? |
| ship #0 - under - bridge #1 | 0-8 | under (+1 more) | 0-9 | identical | 0.89 | ✓ | ? |
| bridge #1 - above - river #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bridge #1 - in front of - sky #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| ship #8 - on - river #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| ship #9 - on - river #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| ship #10 - on - river #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| boat #11 - on - river #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| river #12 - below - sky #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| people #13 - on - ship #0 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ? |
| people #13 - riding - ship #0 | 0-8 | on | 0-9 | hypernym/hyponym | 0.89 | ✓ | ? |
| ship's bridge #14 - above - roof #17 | 0-8 | above | 0-9 | identical | 0.89 | ✓ | ? |
| ship's bridge #14 - attached to - ship #0 | 0-8 | on | 0-9 | not judged yet | 0.89 | ? | ? |
| paddle wheel #15 - on - ship #0 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✗ |
| paddle wheel #15 - attached to - ship #0 | 0-8 | on | 0-9 | not judged yet | 0.89 | ? | ✗ |
| barricade #16 - on - ship #0 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✗ |
| barricade #16 - attached to - ship #0 | 0-8 | on | 0-9 | not judged yet | 0.89 | ? | ✗ |
| roof #17 - on - ship #0 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ? |
| roof #17 - attached to - ship #0 | 0-8 | on | 0-9 | not judged yet | 0.89 | ? | ? |
| roof #17 - above - people #13 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| hull #18 - below - roof #17 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| hull #18 - on - river #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| hull #18 - part of - ship #0 | 0-8 | on | 0-9 | not judged yet | 0.89 | ? | ? |
| safety railing #19 - on - ship #0 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ? |
| safety railing #19 - attached to - ship #0 | 0-8 | on | 0-9 | not judged yet | 0.89 | ? | ? |
| ships rear #20 - on - ship #0 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ? |
| ships rear #20 - attached to - ship #0 | 0-8 | on | 0-9 | not judged yet | 0.89 | ? | ? |

TRASER relations between pairs the humans did not annotate (41): ship #0 - has - barricade #16 [0-9]; ship #0 - has - roof #17 [0-9]; ship #0 - has - ship's bridge #14 [0-9]; ship #0 - has - safety railing #19 [0-9]; ship #0 - has - paddle wheel #15 [0-9]; ship #0 - in front of - paddle wheel #15 [0-9]; ship #0 - has - ships rear #20 [0-9]; ship #0 - in front of - ships rear #20 [0-9]; ship #0 - has - hull #18 [0-9]; ship #0 - in front of - hull #18 [0-9]


## 1717_lh_2_1duNgw

7.5 s, 8 frames read | human: 65 objects, 79 relations | TRASER: 40 objects, 101 relations, valid JSON, 3490 tokens

**Objects: 25/65 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | player | person | not judged yet | ? |
| 1 | referee | person | not judged yet | ? |
| 2 | player | person | not judged yet | ? |
| 3 | player | person | not judged yet | ? |
| 4 | player | person | not judged yet | ? |
| 5 | player | person | not judged yet | ? |
| 6 | player | person | not judged yet | ? |
| 7 | spectators | crowd | not judged yet | ? |
| 8 | field | soccer ball | mismatch | ✗ |
| 9 | goalposts | pole | hypernym/hyponym | ✓ |
| 10 | scoreboard | signboard | not judged yet | ? |
| 11 | barrier wall | barrier (uncertain) | not judged yet | ? |
| 12 | tunnel | pole | not judged yet | ? |
| 13 | security person | person | not judged yet | ? |
| 14 | security staff | person | not judged yet | ? |
| 15 | security staff | person | not judged yet | ? |
| 16 | people | person | hypernym/hyponym | ✓ |
| 17 | people | person | hypernym/hyponym | ✓ |
| 18 | people | person | hypernym/hyponym | ✓ |
| 19 | people | person | hypernym/hyponym | ✓ |
| 20 | people | person | hypernym/hyponym | ✓ |
| 21 | helmet | helmet | identical | ✓ |
| 22 | helmet | helmet | identical | ✓ |
| 23 | helmet | helmet | identical | ✓ |
| 24 | helmet | helmet | identical | ✓ |
| 25 | helmet | helmet | identical | ✓ |
| 26 | helmet | helmet | identical | ✓ |
| 27 | shoe | shoe | identical | ✓ |
| 28 | shoe | shoe | identical | ✓ |
| 29 | shoe | shoe | identical | ✓ |
| 30 | shoe | shoe | identical | ✓ |
| 31 | shoe | shoe | identical | ✓ |
| 32 | shoe | shoe | identical | ✓ |
| 33 | shoe | shoe | identical | ✓ |
| 34 | shoe | shoe | identical | ✓ |
| 35 | shoe | shoe | identical | ✓ |
| 36 | shoe | shoe | identical | ✓ |
| 37 | shoe | shoe | identical | ✓ |
| 38 | shoe | shoe | identical | ✓ |
| 39 | shoe | shoe | identical | ✓ |
| 40 | uniform | - | no label from TRASER | ✗ |
| 41 | uniform | - | no label from TRASER | ✗ |
| 42 | uniform | - | no label from TRASER | ✗ |
| 43 | uniform | - | no label from TRASER | ✗ |
| 44 | uniform | - | no label from TRASER | ✗ |
| 45 | uniform | - | no label from TRASER | ✗ |
| 46 | uniform | - | no label from TRASER | ✗ |
| 47 | uniform | - | no label from TRASER | ✗ |
| 48 | uniform | - | no label from TRASER | ✗ |
| 49 | uniform | - | no label from TRASER | ✗ |
| 50 | uniform | - | no label from TRASER | ✗ |
| 51 | uniform | - | no label from TRASER | ✗ |
| 52 | pants | - | no label from TRASER | ✗ |
| 53 | pants | - | no label from TRASER | ✗ |
| 54 | pants | - | no label from TRASER | ✗ |
| 55 | pants | - | no label from TRASER | ✗ |
| 56 | pants | - | no label from TRASER | ✗ |
| 57 | pants | - | no label from TRASER | ✗ |
| 58 | pants | - | no label from TRASER | ✗ |
| 59 | shirt | - | no label from TRASER | ✗ |
| 60 | hat | - | no label from TRASER | ✗ |
| 61 | glove | - | no label from TRASER | ✗ |
| 62 | glove | - | no label from TRASER | ✗ |
| 63 | glove | - | no label from TRASER | ✗ |
| 64 | glove | - | no label from TRASER | ✗ |

**Relations: 34/79 right, triplets: 0/79 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| player #0 - on - field #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #0 - wearing - helmet #23 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ? |
| player #0 - wearing - pants #52 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #0 - wearing - shoe #31 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ? |
| player #0 - wearing - shoe #32 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ? |
| player #0 - wearing - glove #63 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #0 - wearing - glove #64 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #0 - in front of - spectators #7 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ? |
| player #0 - in front of - barrier wall #11 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #0 - in front of - goalposts #9 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ? |
| player #0 - in front of - tunnel #12 | 1-8 | in front of | 0-8 | identical | 0.88 | ✓ | ? |
| referee #1 - on - field #8 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| referee #1 - moving across - field #8 | 0-5.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| referee #1 - moving away from - player #2 | 0-5.5 | moving away from | 0-5 | identical | 0.91 | ✓ | ? |
| referee #1 - in front of - tunnel #12 | 0-5 | in front of | 0-5 | identical | 1.00 | ✓ | ? |
| referee #1 - in front of - spectators #7 | 0-5 | in front of | 0-5 | identical | 1.00 | ✓ | ? |
| referee #1 - in front of - barrier wall #11 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| referee #1 - in front of - goalposts #9 | 0-5 | in front of | 0-5 | identical | 1.00 | ✓ | ? |
| player #2 - on - field #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #2 - touching - player #4 | 0-3.5 | near | 0-8 | not judged yet | 0.44 | ✗ | ✗ |
| player #2 - looking at - player #3 | 2-7 | near | 0-8 | mismatch | 0.62 | ✗ | ✗ |
| player #2 - wearing - helmet #24 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ? |
| player #2 - wearing - pants #55 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #2 - wearing - shoe #27 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ? |
| player #2 - wearing - shoe #28 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ? |
| player #2 - wearing - glove #61 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #2 - in front of - spectators #7 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ? |
| player #2 - in front of - barrier wall #11 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #2 - in front of - goalposts #9 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ? |
| player #2 - in front of - tunnel #12 | 1-8 | in front of | 0-8 | identical | 0.88 | ✓ | ? |
| player #3 - on - field #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #3 - looking at - player #2 | 0-4, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #3 - wearing - helmet #25 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ? |
| player #3 - wearing - pants #53 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #3 - wearing - shoe #29 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ? |
| player #3 - wearing - shoe #30 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ? |
| player #3 - in front of - spectators #7 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ? |
| player #3 - in front of - barrier wall #11 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #3 - in front of - goalposts #9 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ? |
| player #3 - in front of - tunnel #12 | 1-8 | in front of | 0-8 | identical | 0.88 | ✓ | ? |
| player #4 - on - field #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #4 - wearing - helmet #26 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ? |
| player #4 - wearing - pants #54 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #4 - wearing - shoe #33 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ? |
| player #4 - wearing - shoe #34 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ? |
| player #4 - wearing - glove #62 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #4 - in front of - tunnel #12 | 1-8 | in front of | 0-8 | identical | 0.88 | ✓ | ? |
| player #4 - in front of - spectators #7 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ? |
| player #4 - in front of - barrier wall #11 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #4 - in front of - goalposts #9 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ? |
| player #5 - on - field #8 | 4-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #5 - approaching - player #2 | 4-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #5 - wearing - helmet #22 | 4-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #5 - in front of - spectators #7 | 4-8 | in front of | 4-8 | identical | 1.00 | ✓ | ? |
| player #5 - in front of - barrier wall #11 | 4-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #5 - in front of - goalposts #9 | 4-8 | in front of | 4-8 | identical | 1.00 | ✓ | ? |
| player #6 - on - field #8 | 3-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #6 - approaching - player #2 | 3-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #6 - wearing - helmet #21 | 3-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #6 - in front of - spectators #7 | 3-8 | in front of | 0-1, 4-8 | identical | 0.67 | ✓ | ? |
| player #6 - in front of - barrier wall #11 | 3-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #6 - in front of - goalposts #9 | 3-8 | in front of | 0-1, 4-8 | identical | 0.67 | ✓ | ? |
| spectators #7 - above - barrier wall #11 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| goalposts #9 - in front of - spectators #7 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ? |
| scoreboard #10 - above - goalposts #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| barrier wall #11 - in front of - spectators #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| tunnel #12 - below - scoreboard #10 | 1-8 | below | 0-8 | identical | 0.88 | ✓ | ? |
| tunnel #12 - behind - goalposts #9 | 1-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| security person #13 - in front of - barrier wall #11 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| security staff #14 - in front of - barrier wall #11 | 3-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| security staff #15 - in front of - barrier wall #11 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| helmet #23 - on - player #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| helmet #24 - on - player #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| helmet #25 - on - player #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| helmet #26 - on - player #4 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| pants #52 - on - player #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| pants #53 - on - player #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| pants #54 - on - player #4 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| pants #55 - on - player #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (65): referee #1 - wearing - shoe #38 [0-5]; referee #1 - wearing - shoe #39 [0-5]; player #0 - approaching - player #2 [0-8]; player #0 - approaching - player #3 [0-8]; player #0 - approaching - player #4 [0-8]; referee #1 - moving away from - player #3 [0-5]; referee #1 - moving away from - player #4 [0-5]; security person #13 - in front of - spectators #7 [0-8]; security staff #14 - in front of - spectators #7 [0-8]; security staff #15 - in front of - spectators #7 [0-8]


## 1757_0jsMPnghnck

7.33 s, 7 frames read | human: 23 objects, 28 relations | TRASER: 23 objects, 44 relations, valid JSON, 1853 tokens

**Objects: 18/23 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | sky | sky | identical | ✓ |
| 1 | ground | terrain | synonym | ✓ |
| 2 | road | road | identical | ✓ |
| 3 | building | building | identical | ✓ |
| 4 | house | house | identical | ✓ |
| 5 | house | building | hypernym/hyponym | ✓ |
| 6 | house | building | hypernym/hyponym | ✓ |
| 7 | house | tree | mismatch | ✗ |
| 8 | house | tree | mismatch | ✗ |
| 9 | house | tree | mismatch | ✗ |
| 10 | sand | golf hole | not judged yet | ? |
| 11 | swimming pool | swimming pool | identical | ✓ |
| 12 | tree | tree | identical | ✓ |
| 13 | tree | tree | identical | ✓ |
| 14 | tree | tree | identical | ✓ |
| 15 | tree | tree | identical | ✓ |
| 16 | tree | tree | identical | ✓ |
| 17 | tree | tree | identical | ✓ |
| 18 | tree | tree | identical | ✓ |
| 19 | tree | tree | identical | ✓ |
| 20 | tree | tree | identical | ✓ |
| 21 | tree | house | not judged yet | ? |
| 22 | tree | tree | identical | ✓ |

**Relations: 22/28 right, triplets: 17/28 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| sky #0 - above - ground #1 | 0-8 | above | 0-8 | identical | 1.00 | ✓ | ✓ |
| road #2 - on - ground #1 | 0-5 | on | 0-3 | identical | 0.60 | ✓ | ✓ |
| building #3 - on - ground #1 | 0-5 | on | 0-3 | identical | 0.60 | ✓ | ✓ |
| house #4 - on - ground #1 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| house #5 - on - ground #1 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| house #6 - on - ground #1 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| house #7 - on - ground #1 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✗ |
| house #8 - on - ground #1 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✗ |
| house #9 - on - ground #1 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✗ |
| sand #10 - on - ground #1 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ? |
| swimming pool #11 - next to - house #5 | 0-8 | near | 0-8 | hypernym/hyponym | 1.00 | ✓ | ✓ |
| swimming pool #11 - on - ground #1 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| tree #12 - next to - swimming pool #11 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #12 - on - ground #1 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| tree #13 - next to - swimming pool #11 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #13 - on - ground #1 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| tree #14 - next to - swimming pool #11 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #14 - on - ground #1 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| tree #15 - next to - swimming pool #11 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #15 - on - ground #1 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| tree #16 - next to - swimming pool #11 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #16 - on - ground #1 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| tree #17 - on - ground #1 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| tree #18 - on - ground #1 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| tree #19 - on - ground #1 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| tree #20 - on - ground #1 | 4.5-7 | on | 0-5 | identical | 0.07 | ✗ | ✗ |
| tree #21 - on - ground #1 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ? |
| tree #22 - on - ground #1 | 0-4 | on | 0-3 | identical | 0.75 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (21): sand #10 - near - swimming pool #11 [0-8]; swimming pool #11 - near - house #6 [0-8]; swimming pool #11 - near - house #4 [0-8]; swimming pool #11 - near - tree #21 [0-8]; swimming pool #11 - near - tree #12 [0-8]; swimming pool #11 - near - tree #13 [0-8]; swimming pool #11 - near - tree #14 [0-8]; swimming pool #11 - near - tree #16 [0-8]; swimming pool #11 - near - tree #17 [0-8]; swimming pool #11 - near - tree #15 [0-8]


## 179_mha1KKixPts

22.67 s, 23 frames read | human: 27 objects, 14 relations | TRASER: 27 objects, 20 relations, valid JSON, 1635 tokens

**Objects: 1/27 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | tree | tree trunk | not judged yet | ? |
| 1 | tree | tree trunk | not judged yet | ? |
| 2 | tree | tree trunk | not judged yet | ? |
| 3 | tree | tree trunk | not judged yet | ? |
| 4 | tree | tree trunk | not judged yet | ? |
| 5 | tree | tree trunk | not judged yet | ? |
| 6 | excavator | bulldozer | not judged yet | ? |
| 7 | trees and leaves | tree | not judged yet | ? |
| 8 | leaves | leaves | identical | ✓ |
| 9 | trees | tree | not judged yet | ? |
| 10 | trees | tree | not judged yet | ? |
| 11 | trees | tree | not judged yet | ? |
| 12 | trees | tree trunk | not judged yet | ? |
| 13 | floor | grass | not judged yet | ? |
| 14 | trunk | tree trunk | not judged yet | ? |
| 15 | trunk | tree trunk | not judged yet | ? |
| 16 | trunk | tree trunk | not judged yet | ? |
| 17 | trunk | tree trunk | not judged yet | ? |
| 18 | trunk | tree trunk | not judged yet | ? |
| 19 | trunk | tree trunk | not judged yet | ? |
| 20 | trunk | tree trunk | not judged yet | ? |
| 21 | trunk | tree trunk | not judged yet | ? |
| 22 | trunk | tree trunk | not judged yet | ? |
| 23 | trunk | tree trunk | not judged yet | ? |
| 24 | bucket | dump truck | not judged yet | ? |
| 25 | cyclinder | tree trunk | not judged yet | ? |
| 26 | cab | truck | not judged yet | ? |

**Relations: 1/14 right, triplets: 0/14 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| excavator #6 - on - floor #13 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| excavator #6 - under - trees #9 | 0-23 | in front of | 0-24 | not judged yet | 0.96 | ? | ? |
| excavator #6 - raises - bucket #24 | 0-23 | attached to (+3 more) | 0-24 | not judged yet | 0.96 | ? | ? |
| leaves #8 - on - floor #13 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| leaves #8 - in front of - excavator #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| bucket #24 - attached to - excavator #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| bucket #24 - in front of - cab #26 | 0-23 | in front of (+1 more) | 0-24 | identical | 0.96 | ✓ | ? |
| bucket #24 - below - cyclinder #25 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| bucket #24 - above - floor #13 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| bucket #24 - moves away from - floor #13 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| cyclinder #25 - attached to - excavator #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| cyclinder #25 - attached to - excavator #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| cab #26 - attached to - excavator #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| cab #26 - above - floor #13 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (13): excavator #6 - approaching - cab #26 [14-17]; excavator #6 - moving away from - cab #26 [17-24]; excavator #6 - in front of - cab #26 [0-24]; excavator #6 - near - cab #26 [0-24]; excavator #6 - on - leaves #8 [0-24]; bucket #24 - on - leaves #8 [0-24]; cab #26 - on - leaves #8 [0-24]; floor #13 - on - leaves #8 [0-24]; bucket #24 - in front of - trees #9 [0-24]; cab #26 - in front of - trees #9 [0-24]


## 1903_cFq3flHndS0

7.5 s, 8 frames read | human: 20 objects, 21 relations | TRASER: 20 objects, 53 relations, valid JSON, 2254 tokens

**Objects: 8/20 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | flowers | flower bed | semantic overlap | ✓ |
| 1 | shed | shed | identical | ✓ |
| 2 | plants | grass | not judged yet | ? |
| 3 | wall | stone wall | not judged yet | ? |
| 4 | wall | pole (uncertain) | not judged yet | ? |
| 5 | box | door (uncertain) | not judged yet | ? |
| 6 | tree | bush | semantic overlap | ✓ |
| 7 | flowers | flower bed | semantic overlap | ✓ |
| 8 | plants | plant | not judged yet | ? |
| 9 | big plant | bush | hypernym/hyponym | ✓ |
| 10 | bush | bush | identical | ✓ |
| 11 | trees | bush | not judged yet | ? |
| 12 | trees | bush | not judged yet | ? |
| 13 | building | roof (uncertain) | not judged yet | ? |
| 14 | building | wall | semantic overlap | ✓ |
| 15 | wall | stone wall | not judged yet | ? |
| 16 | wall | stone wall | not judged yet | ? |
| 17 | roof | roof (uncertain) | identical | ✓ |
| 18 | wood | door (uncertain) | not judged yet | ? |
| 19 | wood | door (uncertain) | not judged yet | ? |

**Relations: 5/21 right, triplets: 0/21 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| flowers #0 - in front of - wall #3 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ? |
| shed #1 - in front of - wall #3 | 0-6.5 | in front of | 0-6 | identical | 0.92 | ✓ | ? |
| shed #1 - on - plants #2 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants #2 - in front of - bush #10 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| box #5 - attached to - wall #3 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| box #5 - attached to - shed #1 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #6 - behind - wall #3 | 0-5.5 | in front of | 0-6 | not judged yet | 0.92 | ? | ? |
| plants #8 - in front of - wall #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants #8 - in front of - flowers #0 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ? |
| big plant #9 - in front of - wall #3 | 1-8 | in front of | 0-8 | identical | 0.88 | ✓ | ? |
| bush #10 - in front of - wall #3 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ? |
| trees #11 - behind - wall #3 | 1-5 | in front of | 0-4 | not judged yet | 0.60 | ? | ? |
| trees #12 - behind - wall #3 | 0-6 | in front of | 0-6 | not judged yet | 1.00 | ? | ? |
| building #13 - behind - wall #3 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| building #14 - behind - wall #3 | 0-6 | in front of | 0-6 | not judged yet | 1.00 | ? | ? |
| roof #17 - above - shed #1 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| roof #17 - on - shed #1 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| wood #18 - on - shed #1 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| wood #18 - attached to - shed #1 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| wood #19 - on - shed #1 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| wood #19 - attached to - shed #1 | 0-4 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (44): flowers #0 - in front of - wall #16 [0-8]; flowers #0 - in front of - wall #15 [0-6]; flowers #0 - in front of - shed #1 [0-6]; flowers #0 - on - plants #2 [0-8]; flowers #7 - inside - flowers #0 [0-8]; flowers #7 - in front of - wall #3 [0-8]; flowers #7 - in front of - wall #16 [0-8]; flowers #7 - in front of - wall #15 [0-6]; flowers #7 - in front of - shed #1 [0-6]; flowers #7 - on - plants #2 [0-8]


## 1936_gvKlIkjfP0Q

2.67 s, 4 frames read | human: 56 objects, 40 relations | TRASER: 40 objects, 315 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 18/56 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | car | car | identical | ✓ |
| 1 | car | car | identical | ✓ |
| 2 | tripod | tripod | identical | ✓ |
| 3 | clutter | person | not judged yet | ? |
| 4 | garage wall | wall | hypernym/hyponym | ✓ |
| 5 | garage | window | not judged yet | ? |
| 6 | door | door (uncertain) | identical | ✓ |
| 7 | power outlet | door (uncertain) | not judged yet | ? |
| 8 | rod | pipe (uncertain) | not judged yet | ? |
| 9 | door controller | projector | mismatch | ✗ |
| 10 | rod | pipe (uncertain) | not judged yet | ? |
| 11 | metal | pipe (uncertain) | semantic overlap | ✓ |
| 12 | wall | wall | identical | ✓ |
| 13 | bagpack | bucket | mismatch | ✗ |
| 14 | hoodie | jacket | hypernym/hyponym | ✓ |
| 15 | hand | arm | semantic overlap | ✓ |
| 16 | side mirror | car door handle | not judged yet | ? |
| 17 | car door handle | car door handle | identical | ✓ |
| 18 | tyre | wheel | not judged yet | ? |
| 19 | metal | chair | not judged yet | ? |
| 20 | window | window | identical | ✓ |
| 21 | windshield | car | not judged yet | ? |
| 22 | bonnet | car | semantic overlap | ✓ |
| 23 | rear wing | car door handle | not judged yet | ? |
| 24 | windshield | car hood | not judged yet | ? |
| 25 | headlight | headlight | identical | ✓ |
| 26 | bonnet area | vent (uncertain) | not judged yet | ? |
| 27 | front bumper | bumper (uncertain) | hypernym/hyponym | ✓ |
| 28 | tyres | wheel | not judged yet | ? |
| 29 | fender | car door | semantic overlap | ✓ |
| 30 | metal | car door handle | mismatch | ✗ |
| 31 | rod | pipe (uncertain) | not judged yet | ? |
| 32 | door controller | projector | mismatch | ✗ |
| 33 | gym equipment | ladder | mismatch | ✗ |
| 34 | bagpack | bucket | mismatch | ✗ |
| 35 | hoodie | jacket | hypernym/hyponym | ✓ |
| 36 | hand | arm | semantic overlap | ✓ |
| 37 | side mirror | car door handle | not judged yet | ? |
| 38 | car door handle | car door handle | identical | ✓ |
| 39 | tyre | wheel | not judged yet | ? |
| 40 | windshield | - | no label from TRASER | ✗ |
| 41 | bonnet | - | no label from TRASER | ✗ |
| 42 | side mirror | - | no label from TRASER | ✗ |
| 43 | rear wing | - | no label from TRASER | ✗ |
| 44 | windshield | - | no label from TRASER | ✗ |
| 45 | car engine area | - | no label from TRASER | ✗ |
| 46 | headlight | - | no label from TRASER | ✗ |
| 47 | bonnet area | - | no label from TRASER | ✗ |
| 48 | front bumper | - | no label from TRASER | ✗ |
| 49 | tires | - | no label from TRASER | ✗ |
| 50 | door glass | - | no label from TRASER | ✗ |
| 51 | car door | - | no label from TRASER | ✗ |
| 52 | fender | - | no label from TRASER | ✗ |
| 53 | metal | - | no label from TRASER | ✗ |
| 54 | car roof | - | no label from TRASER | ✗ |
| 55 | step ladder | - | no label from TRASER | ✗ |

**Relations: 0/40 right, triplets: 0/40 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| car #0 - in front of - garage wall #4 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #0 - in front of - tripod #2 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #0 - in front of - gym equipment #33 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #0 - has - rear wing #43 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #0 - has - car engine area #45 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #1 - in front of - car #0 | 0-2 | nothing for this pair | - | - | - | ✗ | ✗ |
| tripod #2 - in front of - garage wall #4 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| tripod #2 - in front of - gym equipment #33 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| clutter #3 - in front of - garage wall #4 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #6 - in - garage wall #4 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| power outlet #7 - mounted on - garage wall #4 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| rod #8 - attached to - garage wall #4 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| rod #10 - attached to - garage wall #4 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| bagpack #13 - in front of - garage wall #4 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| hoodie #14 - worn by - hand #15 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #15 - in front of - car #0 | 0-3 | touching (+7 more) | 0-4 | not judged yet | 0.75 | ? | ? |
| hand #15 - in front of - tripod #2 | 0-3 | touching (+4 more) | 0-4 | not judged yet | 0.75 | ? | ? |
| hand #15 - points at - car engine area #45 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #15 - moves toward - car engine area #45 | 0-2 | nothing for this pair | - | - | - | ✗ | ✗ |
| side mirror #16 - attached to - car #0 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| tyre #18 - attached to - car #0 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #20 - in - garage wall #4 | 0-1.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| windshield #21 - attached to - car #1 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| rear wing #23 - attached to - car #0 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| windshield #24 - attached to - car #0 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| headlight #25 - attached to - car #0 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| bonnet area #26 - attached to - car #0 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| front bumper #27 - attached to - car #0 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| tyres #28 - attached to - car #0 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| fender #29 - attached to - car #0 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| rod #31 - attached to - garage wall #4 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| gym equipment #33 - in front of - garage wall #4 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| tyre #39 - attached to - car #0 | 0-2 | nothing for this pair | - | - | - | ✗ | ✗ |
| bonnet #41 - attached to - car #1 | 0-2 | nothing for this pair | - | - | - | ✗ | ✗ |
| side mirror #42 - attached to - car #1 | 0-2 | nothing for this pair | - | - | - | ✗ | ✗ |
| car engine area #45 - inside - car #0 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| door glass #50 - attached to - car door #51 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| car door #51 - attached to - car #0 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| car roof #54 - attached to - car #0 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| step ladder #55 - in front of - garage wall #4 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (302): hand #36 - touching - car #0 [0-4]; hand #36 - touching - car #0 [0-4]; hand #36 - touching - car #0 [0-4]; hand #36 - touching - car #0 [0-4]; hand #36 - touching - car #0 [0-4]; hand #36 - touching - car #0 [0-4]; hand #36 - touching - car #0 [0-4]; hand #36 - touching - car #0 [0-4]; hand #15 - touching - windshield #24 [0-4]; hand #15 - touching - windshield #24 [0-4]


## 2143_6OMR3X7IcZ0

7.5 s, 8 frames read | human: 16 objects, 28 relations | TRASER: 16 objects, 19 relations, valid JSON, 1198 tokens

**Objects: 10/16 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | counter | countertop | synonym | ✓ |
| 1 | microwave | oven | semantic overlap | ✓ |
| 2 | person | arm | mismatch | ✗ |
| 3 | food | dough (uncertain) | hypernym/hyponym | ✓ |
| 4 | bracelet | bracelet | identical | ✓ |
| 5 | bracelet | bracelet (uncertain) | identical | ✓ |
| 6 | top of a microwave | countertop | not judged yet | ? |
| 7 | touch panel | control panel (uncertain) | not judged yet | ? |
| 8 | door | oven | mismatch | ✗ |
| 9 | glass tray | bowl | semantic overlap | ✓ |
| 10 | oven | oven door | not judged yet | ? |
| 11 | front panel | oven door | semantic overlap | ✓ |
| 12 | ring | handle (uncertain) | not judged yet | ? |
| 13 | bracelet (duplicate of id ) | bracelet (uncertain) | identical | ✓ |
| 14 | arm | arm | identical | ✓ |
| 15 | clothing, shirt | fabric (uncertain) | hypernym/hyponym | ✓ |

**Relations: 1/28 right, triplets: 1/28 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| microwave #1 - on - counter #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - inside - microwave #1 | 0-8 | loading (+1 more) | 0-9 | not judged yet | 0.89 | ? | ✗ |
| person #2 - in front of - microwave #1 | 1-3, 4-6 | in front of (+1 more) | 0-9 | identical | 0.44 | ✗ | ✗ |
| person #2 - above - glass tray #9 | 0-5, 6-8 | holding | 0-9 | not judged yet | 0.78 | ? | ✗ |
| person #2 - moves toward - food #3 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - holds - food #3 | 2-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - takes out - food #3 | 2-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - places back - food #3 | 5-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - moves toward - oven #10 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - moves away from - oven #10 | 5-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| food #3 - on - glass tray #9 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| food #3 - above - glass tray #9 | 4-7.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| food #3 - moves away from - glass tray #9 | 4-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| food #3 - moves toward - glass tray #9 | 5-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| food #3 - inside - microwave #1 | 0-5, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| food #3 - in front of - microwave #1 | 5-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| bracelet #4 - worn by - arm #14 | 2-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bracelet #5 - worn by - arm #14 | 1-2, 3-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| top of a microwave #6 - above - glass tray #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| touch panel #7 - attached to - microwave #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #8 - attached to - microwave #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| glass tray #9 - inside - microwave #1 | 0-8 | inside (+1 more) | 0-9 | identical | 0.89 | ✓ | ✓ |
| glass tray #9 - inside - oven #10 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| glass tray #9 - above - counter #0 | 0-8 | on | 0-9 | not judged yet | 0.89 | ? | ? |
| oven #10 - inside - microwave #1 | 0-8 | attached to | 0-9 | not judged yet | 0.89 | ? | ? |
| front panel #11 - inside - microwave #1 | 0-8 | attached to | 0-9 | not judged yet | 0.89 | ? | ? |
| ring #12 - worn by - person #2 | 1-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| bracelet (duplicate of id ) #13 - worn by - arm #14 | 1-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (11): person #2 - wearing - bracelet #4 [0-9]; counter #0 - in front of - microwave #1 [0-9]; counter #0 - below - microwave #1 [0-9]; oven #10 - above - counter #0 [0-9]; front panel #11 - above - counter #0 [0-9]; top of a microwave #6 - above - counter #0 [0-9]; arm #14 - in front of - microwave #1 [0-9]; bracelet #4 - on - person #2 [0-9]; bracelet #4 - in front of - microwave #1 [0-9]; person #2 - above - counter #0 [0-9]


## 2225_6acPX_00M9Q

15.0 s, 15 frames read | human: 19 objects, 38 relations | TRASER: 19 objects, 49 relations, valid JSON, 1958 tokens

**Objects: 11/19 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | rail signal | traffic light | not judged yet | ? |
| 1 | warning sign board | signboard | not judged yet | ? |
| 2 | mountains | mountain | identical | ✓ |
| 3 | ground | snow | semantic overlap | ✓ |
| 4 | sky | sky | identical | ✓ |
| 5 | mountain | mountain | identical | ✓ |
| 6 | train | train | identical | ✓ |
| 7 | ground | snow | semantic overlap | ✓ |
| 8 | barrier wall | snow | mismatch | ✗ |
| 9 | snow | smoke | not judged yet | ? |
| 10 | ground | snow | semantic overlap | ✓ |
| 11 | roof | snow | not judged yet | ? |
| 12 | sign board | signboard | not judged yet | ? |
| 13 | sign board | signboard | not judged yet | ? |
| 14 | sign board | signboard | not judged yet | ? |
| 15 | light | traffic light | hypernym/hyponym | ✓ |
| 16 | light | traffic light | hypernym/hyponym | ✓ |
| 17 | light | headlight | hypernym/hyponym | ✓ |
| 18 | window | window | identical | ✓ |

**Relations: 8/38 right, triplets: 3/38 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| rail signal #0 - in front of - train #6 | 0-11 | in front of | 0-15 | identical | 0.73 | ✓ | ? |
| rail signal #0 - on - ground #3 | 0-16 | above | 0-15 | semantic overlap | 0.94 | ✓ | ? |
| rail signal #0 - in front of - barrier wall #8 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| warning sign board #1 - on - ground #3 | 4-13 | above | 4-11 | semantic overlap | 0.78 | ✓ | ? |
| warning sign board #1 - below - rail signal #0 | 4-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| warning sign board #1 - attached to - barrier wall #8 | 3.5-13.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| mountains #2 - above - ground #3 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #4 - above - mountains #2 | 4-15 | above | 4-15 | identical | 1.00 | ✓ | ✓ |
| train #6 - in front of - mountains #2 | 0-15 | in front of (+1 more) | 0-15 | identical | 1.00 | ✓ | ✓ |
| train #6 - on - ground #3 | 0-15 | moving on (+1 more) | 0-15 | hypernym/hyponym | 1.00 | ✓ | ✓ |
| train #6 - below - sky #4 | 3.5-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| train #6 - approaches - rail signal #0 | 0-10 | moving past | 0-15 | not judged yet | 0.67 | ? | ? |
| train #6 - passes - rail signal #0 | 9-16 | moving past | 0-15 | not judged yet | 0.38 | ✗ | ✗ |
| train #6 - clears - snow #9 | 0-15 | moving past | 0-15 | not judged yet | 1.00 | ? | ? |
| train #6 - moves through - snow #9 | 0-16 | moving past | 0-15 | not judged yet | 0.94 | ? | ? |
| train #6 - moves past - barrier wall #8 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| barrier wall #8 - on - ground #3 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| snow #9 - on - ground #3 | 0-16 | above | 0-15 | semantic overlap | 0.94 | ✓ | ? |
| snow #9 - covers - ground #3 | 0-15 | above | 0-15 | not judged yet | 1.00 | ? | ? |
| snow #9 - in front of - train #6 | 0-15 | in front of | 0-15 | identical | 1.00 | ✓ | ? |
| snow #9 - moves away from - train #6 | 0-16 | in front of | 0-15 | not judged yet | 0.94 | ? | ? |
| sign board #12 - on - rail signal #0 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign board #12 - attached to - rail signal #0 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign board #12 - above - sign board #13 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign board #13 - on - rail signal #0 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign board #13 - attached to - rail signal #0 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign board #13 - above - sign board #14 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign board #14 - on - rail signal #0 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign board #14 - attached to - rail signal #0 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #15 - on - rail signal #0 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #15 - attached to - rail signal #0 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #16 - on - rail signal #0 | 4-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #16 - attached to - rail signal #0 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #16 - above - light #15 | 3.5-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #17 - on - train #6 | 0-14 | on | 0-2, 10-15 | identical | 0.40 | ✗ | ✗ |
| light #17 - attached to - train #6 | 0-14 | on | 0-2, 10-15 | not judged yet | 0.40 | ✗ | ✗ |
| window #18 - on - train #6 | 0-14 | on | 0-2, 10-15 | identical | 0.40 | ✗ | ✗ |
| window #18 - attached to - train #6 | 0-14 | on | 0-2, 10-15 | not judged yet | 0.40 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (35): train #6 - moving past - light #15 [0-15]; train #6 - moving past - light #16 [0-15]; train #6 - moving past - warning sign board #1 [4-11]; train #6 - moving past - sign board #14 [0-2, 10-12]; train #6 - moving past - sign board #12 [0-2]; train #6 - moving past - sign board #13 [0-2]; train #6 - moving past - window #18 [0-2, 10-15]; train #6 - moving past - light #17 [0-2, 10-15]; rail signal #0 - in front of - mountains #2 [0-15]; light #15 - in front of - train #6 [0-15]


## 226_n7YpGfnTqoY

6.33 s, 6 frames read | human: 20 objects, 51 relations | TRASER: 20 objects, 51 relations, valid JSON, 1865 tokens

**Objects: 11/20 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | car | car | identical | ✓ |
| 1 | road | road | identical | ✓ |
| 2 | grass | grass | identical | ✓ |
| 3 | sidewalk | curb | not judged yet | ? |
| 4 | road | lane separator | not judged yet | ? |
| 5 | license plate | license plate | identical | ✓ |
| 6 | windshield | windshield | identical | ✓ |
| 7 | headlight | headlight | identical | ✓ |
| 8 | headlight | headlight | identical | ✓ |
| 9 | grill | grille | identical | ✓ |
| 10 | driver | rearview mirror | mismatch | ✗ |
| 11 | bonnet | car hood | synonym | ✓ |
| 12 | car logo | emblem | synonym | ✓ |
| 13 | fog light | vent | mismatch | ✗ |
| 14 | fog light | vent | mismatch | ✗ |
| 15 | front bumper | bumper | hypernym/hyponym | ✓ |
| 16 | wiper | windshield wiper | not judged yet | ? |
| 17 | cooling system | vent | not judged yet | ? |
| 18 | side mirror | rearview mirror | not judged yet | ? |
| 19 | tree | pole | mismatch | ✗ |

**Relations: 16/51 right, triplets: 9/51 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| car #0 - on - road #1 | 0-7 | moving on (+2 more) | 0-6 | hypernym/hyponym | 0.86 | ✓ | ✓ |
| car #0 - moving along - road #1 | 0-7 | moving on (+2 more) | 0-6 | not judged yet | 0.86 | ? | ? |
| car #0 - traveling on - road #1 | 0-7 | moving on (+2 more) | 0-6 | not judged yet | 0.86 | ? | ? |
| car #0 - in front of - grass #2 | 0-7 | in front of (+1 more) | 0-6 | identical | 0.86 | ✓ | ✓ |
| car #0 - moving past - grass #2 | 0-7 | passing (+1 more) | 0-6 | not judged yet | 0.86 | ? | ? |
| car #0 - in front of - sidewalk #3 | 0-7 | in front of (+1 more) | 0-6 | identical | 0.86 | ✓ | ? |
| car #0 - moving past - sidewalk #3 | 0-7 | passing (+1 more) | 0-6 | not judged yet | 0.86 | ? | ? |
| car #0 - moving past - tree #19 | 1.5-7 | passing (+1 more) | 0-6 | not judged yet | 0.64 | ? | ✗ |
| car #0 - in front of - tree #19 | 2-7 | in front of (+1 more) | 0-6 | identical | 0.57 | ✓ | ✗ |
| car #0 - has attached - grill #9 | 0-7 | has | 0-6 | not judged yet | 0.86 | ? | ? |
| car #0 - has attached - headlight #7 | 0-7 | has | 0-6 | not judged yet | 0.86 | ? | ? |
| car #0 - has attached - bonnet #11 | 0-7 | has | 0-6 | not judged yet | 0.86 | ? | ? |
| car #0 - has attached - car logo #12 | 0-7 | has | 0-6 | not judged yet | 0.86 | ? | ? |
| car #0 - has attached - license plate #5 | 0-7 | has | 5-6 | not judged yet | 0.14 | ✗ | ✗ |
| car #0 - has attached - side mirror #18 | 0-7 | has | 0-6 | not judged yet | 0.86 | ? | ? |
| car #0 - has attached - wiper #16 | 0-7 | has | 0-6 | not judged yet | 0.86 | ? | ? |
| car #0 - has attached - front bumper #15 | 0-7 | has | 0-6 | not judged yet | 0.86 | ? | ? |
| car #0 - has attached - fog light #14 | 0-7 | has | 0-6 | not judged yet | 0.86 | ? | ✗ |
| car #0 - has attached - fog light #13 | 0-7 | has | 0-6 | not judged yet | 0.86 | ? | ✗ |
| car #0 - has attached - headlight #8 | 0-7 | has | 0-6 | not judged yet | 0.86 | ? | ? |
| road #1 - beside - sidewalk #3 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| road #1 - beside - sidewalk #3 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| sidewalk #3 - beside - grass #2 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| road #4 - beside - road #1 | 6-7 | on | 5-6 | not judged yet | 0.00 | ✗ | ✗ |
| license plate #5 - on - car #0 | 4-7 | on | 5-6 | identical | 0.33 | ✗ | ✗ |
| license plate #5 - on - front bumper #15 | 4-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| license plate #5 - below - grill #9 | 4-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| windshield #6 - on - car #0 | 0-7 | on | 0-6 | identical | 0.86 | ✓ | ✓ |
| headlight #7 - on - car #0 | 0-7 | on | 0-6 | identical | 0.86 | ✓ | ✓ |
| headlight #7 - above - fog light #13 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| headlight #8 - on - car #0 | 0-7 | on | 0-6 | identical | 0.86 | ✓ | ✓ |
| headlight #8 - above - fog light #14 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| grill #9 - on - car #0 | 0-7 | on | 0-6 | identical | 0.86 | ✓ | ✓ |
| grill #9 - above - front bumper #15 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| driver #10 - driving - car #0 | 0-7 | on | 0-6 | not judged yet | 0.86 | ? | ✗ |
| driver #10 - inside - car #0 | 0-7 | on | 0-6 | not judged yet | 0.86 | ? | ✗ |
| driver #10 - behind - windshield #6 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| bonnet #11 - on - car #0 | 0-7 | on | 0-6 | identical | 0.86 | ✓ | ✓ |
| bonnet #11 - above - front bumper #15 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| car logo #12 - attached to - grill #9 | 0-7 | above | 0-6 | not judged yet | 0.86 | ? | ? |
| car logo #12 - on - grill #9 | 0-7 | above | 0-6 | semantic overlap | 0.86 | ✓ | ✓ |
| fog light #13 - on - car #0 | 0-7 | on | 0-6 | identical | 0.86 | ✓ | ✗ |
| fog light #13 - below - headlight #7 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| fog light #14 - on - car #0 | 0-7 | on | 0-6 | identical | 0.86 | ✓ | ✗ |
| fog light #14 - below - grill #9 | 0-7 | below | 0-6 | identical | 0.86 | ✓ | ✗ |
| front bumper #15 - on - car #0 | 0-7 | on | 0-6 | identical | 0.86 | ✓ | ✓ |
| wiper #16 - on - car #0 | 0-7 | on | 0-6 | identical | 0.86 | ✓ | ? |
| wiper #16 - below - windshield #6 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| side mirror #18 - on - car #0 | 0-7 | on | 0-6 | identical | 0.86 | ✓ | ? |
| tree #19 - on - grass #2 | 2-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #19 - behind - sidewalk #3 | 2-7 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (16): car #0 - has - windshield #6 [0-6]; car #0 - has - cooling system #17 [0-6]; car #0 - has - driver #10 [0-6]; sidewalk #3 - adjacent to - road #1 [0-6]; grass #2 - adjacent to - sidewalk #3 [0-6]; car logo #12 - on - car #0 [0-6]; cooling system #17 - on - car #0 [0-6]; front bumper #15 - below - grill #9 [0-6]; grill #9 - below - bonnet #11 [0-6]; wiper #16 - above - grill #9 [0-6]


## 241_oEkly9vzEGQ

12.67 s, 13 frames read | human: 26 objects, 31 relations | TRASER: 26 objects, 41 relations, valid JSON, 2318 tokens

**Objects: 17/26 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | person | person | identical | ✓ |
| 1 | bench | bench | identical | ✓ |
| 2 | ground | person | mismatch | ✗ |
| 3 | fountain | fountain | identical | ✓ |
| 4 | street | car | not judged yet | ? |
| 5 | building | pole (uncertain) | mismatch | ✗ |
| 6 | building | tree | mismatch | ✗ |
| 7 | building | wall | semantic overlap | ✓ |
| 8 | car | car | identical | ✓ |
| 9 | car | car | identical | ✓ |
| 10 | car | car | identical | ✓ |
| 11 | tree | tree | identical | ✓ |
| 12 | garagecan | flowerpot | not judged yet | ? |
| 13 | building | building | identical | ✓ |
| 14 | parking sign | car | mismatch | ✗ |
| 15 | bag | handbag | hypernym/hyponym | ✓ |
| 16 | hair | hair | identical | ✓ |
| 17 | coat | jacket | synonym | ✓ |
| 18 | shoes | high heel shoe | not judged yet | ? |
| 19 | tree | tree | identical | ✓ |
| 20 | tree | tree | identical | ✓ |
| 21 | bush | bush | identical | ✓ |
| 22 | bush | trash can (uncertain) | mismatch | ✗ |
| 23 | bush | bush | identical | ✓ |
| 24 | plant | plant | identical | ✓ |
| 25 | plant | potted plant | not judged yet | ? |

**Relations: 9/31 right, triplets: 8/31 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - wearing - coat #17 | 0-13 | wearing | 0-14 | identical | 0.93 | ✓ | ✓ |
| person #0 - carrying - bag #15 | 0-13 | carrying | 0-14 | identical | 0.93 | ✓ | ✓ |
| person #0 - on - ground #2 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - walking across - ground #2 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - wearing - shoes #18 | 0-13 | wearing | 0-14 | identical | 0.93 | ✓ | ? |
| person #0 - behind - fountain #3 | 0-13 | looking at (+2 more) | 0-14 | not judged yet | 0.93 | ? | ? |
| person #0 - beside - fountain #3 | 0-13 | near (+2 more) | 0-14 | not judged yet | 0.93 | ? | ? |
| person #0 - approaching - fountain #3 | 0-13 | approaching (+2 more) | 0-14 | identical | 0.93 | ✓ | ✓ |
| person #0 - in front of - bench #1 | 0-13 | in front of | 0-14 | identical | 0.93 | ✓ | ✓ |
| person #0 - in front of - building #7 | 0-13 | in front of | 0-14 | identical | 0.93 | ✓ | ✓ |
| bench #1 - on - ground #2 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| bench #1 - behind - fountain #3 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| bench #1 - beside - fountain #3 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| bench #1 - in front of - building #7 | 0-13 | in front of | 0-14 | identical | 0.93 | ✓ | ✓ |
| fountain #3 - on - ground #2 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| fountain #3 - in front of - building #13 | 4-13 | in front of | 4-14 | identical | 0.90 | ✓ | ✓ |
| car #9 - on - ground #2 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #9 - behind - fountain #3 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #9 - in front of - building #13 | 0-13 | in front of | 4-14 | identical | 0.64 | ✓ | ✓ |
| car #10 - on - ground #2 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #10 - behind - fountain #3 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #11 - on - ground #2 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #11 - behind - fountain #3 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| garagecan #12 - on - ground #2 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| garagecan #12 - behind - fountain #3 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| bag #15 - above - shoes #18 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| hair #16 - above - coat #17 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| hair #16 - above - bag #15 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| coat #17 - above - shoes #18 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| plant #24 - on - ground #2 | 5-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| plant #25 - on - ground #2 | 10-13 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (30): person #0 - in front of - tree #11 [0-14]; person #0 - in front of - building #13 [4-14]; bag #15 - overlapping - person #0 [0-14]; coat #17 - overlapping - person #0 [0-14]; hair #16 - overlapping - person #0 [0-14]; shoes #18 - below - person #0 [0-14]; shoes #18 - in front of - bench #1 [0-14]; shoes #18 - near - fountain #3 [0-14]; bench #1 - in front of - tree #11 [0-14]; bench #1 - in front of - building #13 [4-14]


## 246_QcRqBBAiC4o

22.67 s, 23 frames read | human: 56 objects, 36 relations | TRASER: 40 objects, 43 relations, valid JSON, 3092 tokens

**Objects: 8/56 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | printer | printer | identical | ✓ |
| 1 | counter | desk (uncertain) | not judged yet | ? |
| 2 | wall | mirror | not judged yet | ? |
| 3 | light | chandelier | not judged yet | ? |
| 4 | furniture | chair | not judged yet | ? |
| 5 | fireplace | fireplace | identical | ✓ |
| 6 | cabinet | door | not judged yet | ? |
| 7 | monitor | computer monitor | hypernym/hyponym | ✓ |
| 8 | monitor | computer monitor | hypernym/hyponym | ✓ |
| 9 | counter | desk | not judged yet | ? |
| 10 | printer | printer | identical | ✓ |
| 11 | pillar | column | not judged yet | ? |
| 12 | person | person | identical | ✓ |
| 13 | person | person | identical | ✓ |
| 14 | cpu | printer | not judged yet | ? |
| 15 | counter | desk | not judged yet | ? |
| 16 | device | speaker (uncertain) | not judged yet | ? |
| 17 | light | ceiling light fixture (uncertain) | not judged yet | ? |
| 18 | light | ceiling light fixture (uncertain) | not judged yet | ? |
| 19 | light | ceiling light fixture (uncertain) | not judged yet | ? |
| 20 | light | ceiling light fixture (uncertain) | not judged yet | ? |
| 21 | light | ceiling light fixture (uncertain) | not judged yet | ? |
| 22 | wall | wall panel | not judged yet | ? |
| 23 | wall | ceiling beam (uncertain) | not judged yet | ? |
| 24 | wall | wall panel | not judged yet | ? |
| 25 | wall | ceiling beam (uncertain) | not judged yet | ? |
| 26 | household material | chair | not judged yet | ? |
| 27 | lights | ceiling beam (uncertain) | not judged yet | ? |
| 28 | chandelier | lamp | not judged yet | ? |
| 29 | wall frame | printer | not judged yet | ? |
| 30 | wall frame | chair | not judged yet | ? |
| 31 | document | chair | not judged yet | ? |
| 32 | document | paper (uncertain) | not judged yet | ? |
| 33 | decor | cellular telephone (uncertain) | not judged yet | ? |
| 34 | lights | light fixture (uncertain) | not judged yet | ? |
| 35 | ceiling | ceiling beam (uncertain) | not judged yet | ? |
| 36 | decor | chair | not judged yet | ? |
| 37 | decor | television set | not judged yet | ? |
| 38 | decor | chair | not judged yet | ? |
| 39 | light | lamp | hypernym/hyponym | ✓ |
| 40 | light | - | no label from TRASER | ✗ |
| 41 | light | - | no label from TRASER | ✗ |
| 42 | display cabinet | - | no label from TRASER | ✗ |
| 43 | hair | - | no label from TRASER | ✗ |
| 44 | glasses | - | no label from TRASER | ✗ |
| 45 | shirt | - | no label from TRASER | ✗ |
| 46 | hair | - | no label from TRASER | ✗ |
| 47 | shirt | - | no label from TRASER | ✗ |
| 48 | face | - | no label from TRASER | ✗ |
| 49 | light | - | no label from TRASER | ✗ |
| 50 | fireplace mantle | - | no label from TRASER | ✗ |
| 51 | wall frame | - | no label from TRASER | ✗ |
| 52 | decor | - | no label from TRASER | ✗ |
| 53 | painting | - | no label from TRASER | ✗ |
| 54 | decor | - | no label from TRASER | ✗ |
| 55 | decor | - | no label from TRASER | ✗ |

**Relations: 5/36 right, triplets: 0/36 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| printer #0 - on - counter #9 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ? |
| light #3 - under - chandelier #28 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #3 - above - furniture #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| furniture #4 - in front of - wall #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| fireplace #5 - attached to - wall #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| monitor #7 - on - counter #15 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| monitor #7 - behind - counter #9 | 0-23 | on | 0-24 | not judged yet | 0.96 | ? | ? |
| monitor #8 - on - counter #15 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| monitor #8 - behind - counter #9 | 0-23 | on | 0-24 | not judged yet | 0.96 | ? | ? |
| counter #9 - in front of - wall #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| printer #10 - on - counter #9 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ? |
| pillar #11 - in front of - wall #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| pillar #11 - under - chandelier #28 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #12 - talking with - person #13 | 0-23 | working with | 0-24 | not judged yet | 0.96 | ? | ? |
| person #12 - looking at - person #13 | 6-14, 16-23 | working with | 0-24 | not judged yet | 0.62 | ? | ? |
| person #12 - looking at - monitor #8 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #12 - wearing - glasses #44 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #12 - wearing - shirt #45 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #12 - behind - counter #15 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #12 - in front of - wall #22 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ? |
| person #13 - looking at - person #12 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #13 - wearing - shirt #47 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #13 - in front of - wall #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #13 - behind - counter #9 | 0-23 | behind | 0-24 | identical | 0.96 | ✓ | ? |
| cpu #14 - under - counter #15 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| counter #15 - behind - counter #9 | 0-23 | behind | 0-24 | identical | 0.96 | ✓ | ? |
| device #16 - on - counter #9 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #20 - under - lights #27 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| wall frame #29 - on - wall #22 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| wall frame #30 - on - wall #24 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| document #31 - on - counter #15 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| document #32 - on - counter #15 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| decor #36 - on - wall #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| decor #37 - on - wall #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| decor #38 - on - wall #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| fireplace mantle #50 - on - wall #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (35): person #12 - looking at - printer #0 [0-24]; person #12 - collaborating on - printer #0 [0-24]; person #13 - looking at - printer #0 [0-24]; person #13 - collaborating on - printer #0 [0-24]; person #12 - behind - counter #9 [0-24]; cpu #14 - on - counter #9 [0-24]; wall frame #29 - on - counter #9 [0-24]; wall #2 - above - counter #9 [0-24]; light #3 - above - counter #9 [0-24]; chandelier #28 - above - counter #9 [0-24]


## 254_-7d3nOFx1V8

22.67 s, 23 frames read | human: 30 objects, 25 relations | TRASER: 30 objects, 48 relations, valid JSON, 2466 tokens

**Objects: 12/30 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | window | window | identical | ✓ |
| 1 | person | person | identical | ✓ |
| 2 | ledge | ledge | identical | ✓ |
| 3 | wall | brick wall | not judged yet | ? |
| 4 | spray | bottle | not judged yet | ? |
| 5 | wall | door frame (uncertain) | not judged yet | ? |
| 6 | plants | vase | not judged yet | ? |
| 7 | window | window | identical | ✓ |
| 8 | home material | bottle | not judged yet | ? |
| 9 | shirt | jersey | not judged yet | ? |
| 10 | wall | brick wall | not judged yet | ? |
| 11 | wall | brick wall | not judged yet | ? |
| 12 | glass | window frame (uncertain) | not judged yet | ? |
| 13 | plant | flower arrangement | not judged yet | ? |
| 14 | vase planter | vase | not judged yet | ? |
| 15 | plant | flower arrangement | not judged yet | ? |
| 16 | glass | window | semantic overlap | ✓ |
| 17 | glass | window | semantic overlap | ✓ |
| 18 | glass | window | semantic overlap | ✓ |
| 19 | glass | window | semantic overlap | ✓ |
| 20 | glass | window | semantic overlap | ✓ |
| 21 | glass | window frame (uncertain) | not judged yet | ? |
| 22 | glass | window | semantic overlap | ✓ |
| 23 | glass | pole (uncertain) | not judged yet | ? |
| 24 | shirt | jersey | not judged yet | ? |
| 25 | jean | jeans (uncertain) | not judged yet | ? |
| 26 | hand | arm | semantic overlap | ✓ |
| 27 | hair | hairline | not judged yet | ? |
| 28 | glass | spectacles | not judged yet | ? |
| 29 | hand | hand | identical | ✓ |

**Relations: 7/25 right, triplets: 2/25 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| window #0 - contain - glass #22 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #0 - in - wall #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #0 - above - ledge #2 | 0-23 | above | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #1 - hold - spray #4 | 0-23 | holding (+2 more) | 0-24 | not judged yet | 0.96 | ? | ? |
| person #1 - wear - shirt #9 | 0-23 | wearing | 0-24 | not judged yet | 0.96 | ? | ? |
| person #1 - wear - jean #25 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - look at - window #0 | 0-2, 4-15 | in front of | 0-24 | not judged yet | 0.54 | ? | ? |
| person #1 - repair - window #0 | 0-14 | in front of | 0-24 | not judged yet | 0.58 | ? | ? |
| person #1 - in front of - window #0 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #1 - in front of - wall #3 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ? |
| ledge #2 - in front of - wall #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| spray #4 - above - ledge #2 | 0-23 | above | 0-24 | identical | 0.96 | ✓ | ? |
| window #7 - in - wall #5 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| home material #8 - on - ledge #2 | 5.5-23 | above | 0-24 | semantic overlap | 0.73 | ✓ | ? |
| shirt #9 - on - person #1 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ? |
| plant #13 - above - plant #15 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| vase planter #14 - hold - plant #15 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| vase planter #14 - in front of - wall #5 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| vase planter #14 - below - window #7 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| plant #15 - in - vase planter #14 | 0-23 | above | 0-24 | not judged yet | 0.96 | ? | ? |
| glass #16 - in - window #7 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| glass #21 - in - window #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| glass #22 - in - window #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| jean #25 - on - person #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| hair #27 - on - person #1 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ? |

TRASER relations between pairs the humans did not annotate (36): person #1 - wearing - shirt #24 [0-24]; person #1 - in front of - window #7 [0-24]; person #1 - in front of - glass #16 [0-24]; person #1 - in front of - glass #17 [0-24]; person #1 - in front of - glass #18 [0-24]; person #1 - in front of - glass #19 [0-24]; person #1 - in front of - glass #20 [0-24]; person #1 - in front of - glass #22 [0-24]; person #1 - in front of - wall #10 [0-24]; person #1 - in front of - wall #11 [0-24]


## 276_3HgBHBOnpbg

7.5 s, 8 frames read | human: 40 objects, 55 relations | TRASER: 11 objects, 0 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 4/40 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | man | person | hypernym/hyponym | ✓ |
| 1 | woman | person | not judged yet | ? |
| 2 | car | sedan | not judged yet | ? |
| 3 | car | car | identical | ✓ |
| 4 | building | building | identical | ✓ |
| 5 | building | tree | mismatch | ✗ |
| 6 | road | car | not judged yet | ? |
| 7 | sky | streetlight | not judged yet | ? |
| 8 | building | building | identical | ✓ |
| 9 | shop or building | storefront | not judged yet | ? |
| 10 | sidewalk | person | not judged yet | ? |
| 11 | machine | - | no label from TRASER | ✗ |
| 12 | bag | - | no label from TRASER | ✗ |
| 13 | bag | - | no label from TRASER | ✗ |
| 14 | wall | - | no label from TRASER | ✗ |
| 15 | wall | - | no label from TRASER | ✗ |
| 16 | tree | - | no label from TRASER | ✗ |
| 17 | plant | - | no label from TRASER | ✗ |
| 18 | car | - | no label from TRASER | ✗ |
| 19 | wheel | - | no label from TRASER | ✗ |
| 20 | light | - | no label from TRASER | ✗ |
| 21 | light | - | no label from TRASER | ✗ |
| 22 | window | - | no label from TRASER | ✗ |
| 23 | backpack | - | no label from TRASER | ✗ |
| 24 | window | - | no label from TRASER | ✗ |
| 25 | window | - | no label from TRASER | ✗ |
| 26 | door | - | no label from TRASER | ✗ |
| 27 | pants | - | no label from TRASER | ✗ |
| 28 | shorts | - | no label from TRASER | ✗ |
| 29 | clothes | - | no label from TRASER | ✗ |
| 30 | T-shirt | - | no label from TRASER | ✗ |
| 31 | wheel | - | no label from TRASER | ✗ |
| 32 | window | - | no label from TRASER | ✗ |
| 33 | side mirror | - | no label from TRASER | ✗ |
| 34 | plate | - | no label from TRASER | ✗ |
| 35 | door | - | no label from TRASER | ✗ |
| 36 | wall | - | no label from TRASER | ✗ |
| 37 | shoe | - | no label from TRASER | ✗ |
| 38 | shoe | - | no label from TRASER | ✗ |
| 39 | shoe | - | no label from TRASER | ✗ |

**Relations: 0/55 right, triplets: 0/55 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| man #0 - left of - woman #1 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - in front of - woman #1 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - walking with - woman #1 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - walking on - sidewalk #10 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #1 - walking on - sidewalk #10 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - wearing - backpack #23 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - holding - machine #11 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #1 - has - bag #12 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #1 - has - bag #13 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #1 - wears - shorts #28 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #1 - wears - clothes #29 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - wears - T-shirt #30 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - wears - pants #27 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #1 - wears - shoe #39 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - wears - shoe #38 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - wears - shoe #37 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - under - sky #7 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #1 - under - sky #7 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #2 - under - sky #7 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #3 - under - sky #7 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| road #6 - under - sky #7 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| sidewalk #10 - under - sky #7 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| plate #34 - attached to - car #2 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| plate #34 - part of - car #2 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - walking past - shop or building #9 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - left of - shop or building #9 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #1 - left of - shop or building #9 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #1 - walking past - shop or building #9 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #1 - right of - building #5 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - right of - building #5 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - near - car #2 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #3 - in front of - man #0 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #1 - near - car #2 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| building #4 - in front of - man #0 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| building #4 - in front of - woman #1 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #19 - part of - car #2 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #20 - part of - car #2 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #21 - part of - car #2 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #22 - part of - car #2 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| side mirror #33 - part of - car #2 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #32 - part of - car #2 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #25 - part of - shop or building #9 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #24 - part of - shop or building #9 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #26 - part of - shop or building #9 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #2 - on - road #6 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #3 - on - road #6 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| plant #17 - on - sidewalk #10 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| plant #17 - near - car #2 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| plant #17 - near - car #3 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #2 - in front of - car #3 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #16 - near - building #5 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| wall #15 - in front of - man #0 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| wall #15 - in front of - woman #1 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| wall #14 - part of - shop or building #9 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| wall #36 - part of - shop or building #9 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |


## 279_qw5ySRNNfNM

22.67 s, 23 frames read | human: 89 objects, 47 relations | TRASER: 40 objects, 166 relations, valid JSON, 5221 tokens

**Objects: 17/89 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | sky | sky | identical | ✓ |
| 1 | person | person | identical | ✓ |
| 2 | person | person | identical | ✓ |
| 3 | golf extract | golf club | not judged yet | ? |
| 4 | golf cart | cart | not judged yet | ? |
| 5 | basket of golfs | basketball hoop | not judged yet | ? |
| 6 | golf ball | golf ball | identical | ✓ |
| 7 | golf ball | golf ball | identical | ✓ |
| 8 | golf ball | golf ball | identical | ✓ |
| 9 | golf ball | golf ball | identical | ✓ |
| 10 | golf ball | golf ball | identical | ✓ |
| 11 | golf ball | golf ball | identical | ✓ |
| 12 | golf ball | golf ball | identical | ✓ |
| 13 | golf ball | golf ball | identical | ✓ |
| 14 | golf ball | golf ball | identical | ✓ |
| 15 | golf ball | golf ball | identical | ✓ |
| 16 | golf ball | golf ball | identical | ✓ |
| 17 | golf ball | golf ball | identical | ✓ |
| 18 | golf ball | golf ball | identical | ✓ |
| 19 | umbrella | tree | not judged yet | ? |
| 20 | person | golf cart | not judged yet | ? |
| 21 | person | golf cart | not judged yet | ? |
| 22 | car | golf cart | not judged yet | ? |
| 23 | house | golf cart | not judged yet | ? |
| 24 | metal | golf cart | not judged yet | ? |
| 25 | house | house | identical | ✓ |
| 26 | background | grass | not judged yet | ? |
| 27 | barricade | golf cart | not judged yet | ? |
| 28 | tree | trees | not judged yet | ? |
| 29 | barricade | golf cart | not judged yet | ? |
| 30 | barricade | golf cart | not judged yet | ? |
| 31 | barricade | golf cart | not judged yet | ? |
| 32 | barricade | golf cart | not judged yet | ? |
| 33 | barricade | golf cart | not judged yet | ? |
| 34 | barricade | golf cart | not judged yet | ? |
| 35 | barricade | golf cart | not judged yet | ? |
| 36 | barricade | golf cart | not judged yet | ? |
| 37 | barricade | golf cart | not judged yet | ? |
| 38 | crowd | golf cart | not judged yet | ? |
| 39 | floor | golf cart | not judged yet | ? |
| 40 | grass | - | no label from TRASER | ✗ |
| 41 | floor | - | no label from TRASER | ✗ |
| 42 | grass | - | no label from TRASER | ✗ |
| 43 | grass | - | no label from TRASER | ✗ |
| 44 | grass | - | no label from TRASER | ✗ |
| 45 | post | - | no label from TRASER | ✗ |
| 46 | grass | - | no label from TRASER | ✗ |
| 47 | cart | - | no label from TRASER | ✗ |
| 48 | person | - | no label from TRASER | ✗ |
| 49 | golf balls | - | no label from TRASER | ✗ |
| 50 | basket | - | no label from TRASER | ✗ |
| 51 | cap | - | no label from TRASER | ✗ |
| 52 | face | - | no label from TRASER | ✗ |
| 53 | shirt | - | no label from TRASER | ✗ |
| 54 | hand | - | no label from TRASER | ✗ |
| 55 | bag | - | no label from TRASER | ✗ |
| 56 | picker | - | no label from TRASER | ✗ |
| 57 | trouser | - | no label from TRASER | ✗ |
| 58 | shoe | - | no label from TRASER | ✗ |
| 59 | shoe | - | no label from TRASER | ✗ |
| 60 | hand | - | no label from TRASER | ✗ |
| 61 | shoe | - | no label from TRASER | ✗ |
| 62 | shoe | - | no label from TRASER | ✗ |
| 63 | shirt | - | no label from TRASER | ✗ |
| 64 | trouser | - | no label from TRASER | ✗ |
| 65 | face | - | no label from TRASER | ✗ |
| 66 | hand | - | no label from TRASER | ✗ |
| 67 | hand | - | no label from TRASER | ✗ |
| 68 | golf materials | - | no label from TRASER | ✗ |
| 69 | job cart | - | no label from TRASER | ✗ |
| 70 | stairs | - | no label from TRASER | ✗ |
| 71 | stairs | - | no label from TRASER | ✗ |
| 72 | roof | - | no label from TRASER | ✗ |
| 73 | window | - | no label from TRASER | ✗ |
| 74 | window | - | no label from TRASER | ✗ |
| 75 | pavement | - | no label from TRASER | ✗ |
| 76 | barricade | - | no label from TRASER | ✗ |
| 77 | pavement | - | no label from TRASER | ✗ |
| 78 | barricade | - | no label from TRASER | ✗ |
| 79 | barricade | - | no label from TRASER | ✗ |
| 80 | pavement | - | no label from TRASER | ✗ |
| 81 | barricade | - | no label from TRASER | ✗ |
| 82 | pavement | - | no label from TRASER | ✗ |
| 83 | barricade | - | no label from TRASER | ✗ |
| 84 | barricade | - | no label from TRASER | ✗ |
| 85 | barricade | - | no label from TRASER | ✗ |
| 86 | barricade | - | no label from TRASER | ✗ |
| 87 | barricade | - | no label from TRASER | ✗ |
| 88 | tyre | - | no label from TRASER | ✗ |

**Relations: 2/47 right, triplets: 0/47 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #1 - on - grass #46 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - in front of - golf cart #4 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ? |
| person #1 - in front of - job cart #69 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - holds - golf extract #3 | 0-4, 7.5-23 | holding (+3 more) | 0-24 | not judged yet | 0.81 | ? | ? |
| person #1 - uses - golf extract #3 | 0-4, 7.5-23 | holding (+3 more) | 0-24 | not judged yet | 0.81 | ? | ? |
| person #1 - hands - golf extract #3 | 1-4 | holding (+3 more) | 0-24 | not judged yet | 0.12 | ✗ | ✗ |
| person #1 - approaches - basket of golfs #5 | 5-9 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - wears - cap #51 | 0-12 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - talks to - person #2 | 0-5, 10-13 | near | 0-24 | not judged yet | 0.33 | ✗ | ✗ |
| person #1 - beside - person #2 | 0-23 | near | 0-24 | not judged yet | 0.96 | ? | ? |
| person #2 - on - grass #46 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - in front of - golf cart #4 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ? |
| person #2 - in front of - job cart #69 | 0-15, 19-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - holds - golf extract #3 | 3-23 | holding (+3 more) | 0-24 | not judged yet | 0.83 | ? | ? |
| person #2 - uses - golf extract #3 | 15-23 | holding (+3 more) | 0-24 | not judged yet | 0.33 | ✗ | ✗ |
| golf extract #3 - above - grass #46 | 18.5-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| golf extract #3 - moves toward - person #2 | 1-5 | overlapping | 0-24 | not judged yet | 0.17 | ✗ | ✗ |
| golf extract #3 - moves toward - golf ball #7 | 15-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| golf cart #4 - on - grass #46 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| basket of golfs #5 - on - grass #46 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| golf ball #6 - on - grass #46 | 9-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| golf ball #7 - on - grass #46 | 14-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| golf ball #8 - on - grass #46 | 15-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| golf ball #9 - on - grass #46 | 13-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| golf ball #10 - on - grass #46 | 12.5-19.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| golf ball #11 - on - grass #46 | 14-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| golf ball #12 - on - grass #46 | 15-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| golf ball #13 - on - grass #46 | 13-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| golf ball #14 - on - grass #46 | 13-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| golf ball #15 - on - grass #46 | 10-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| golf ball #16 - on - grass #46 | 10-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| golf ball #17 - on - grass #46 | 9-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| golf ball #18 - on - grass #46 | 10-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| golf balls #49 - inside - basket #50 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| basket #50 - on - grass #46 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| basket #50 - in front of - golf cart #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| basket #50 - contains - golf balls #49 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| basket #50 - below - person #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| basket #50 - in front of - person #1 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| basket #50 - below - person #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| basket #50 - in front of - person #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| cap #51 - on - person #1 | 0-12 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #53 - on - person #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| trouser #57 - on - person #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #63 - on - person #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| trouser #64 - on - person #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| job cart #69 - on - grass #46 | 0-15, 19-23 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (154): golf extract #3 - overlapping - person #1 [0-24]; person #1 - in front of - tree #28 [0-16]; person #2 - in front of - tree #28 [0-16]; golf cart #4 - in front of - tree #28 [0-16]; person #1 - in front of - house #25 [0-13]; person #2 - in front of - house #25 [0-13]; golf cart #4 - in front of - house #25 [0-13]; person #1 - in front of - umbrella #19 [0-13]; person #2 - in front of - umbrella #19 [0-13]; golf cart #4 - in front of - umbrella #19 [0-13]


## 285_EP_blwEf2K8

7.5 s, 8 frames read | human: 58 objects, 50 relations | TRASER: 40 objects, 127 relations, valid JSON, 4322 tokens

**Objects: 14/58 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | boat | raft | not judged yet | ? |
| 1 | bucket | person | mismatch | ✗ |
| 2 | bucket | person | mismatch | ✗ |
| 3 | bucket | life jacket (uncertain) | not judged yet | ? |
| 4 | person | person | identical | ✓ |
| 5 | person | person | identical | ✓ |
| 6 | person | person | identical | ✓ |
| 7 | person | person | identical | ✓ |
| 8 | pool | raft | not judged yet | ? |
| 9 | person | person | identical | ✓ |
| 10 | person | person | identical | ✓ |
| 11 | bucket | person | mismatch | ✗ |
| 12 | bucket | life jacket (uncertain) | not judged yet | ? |
| 13 | wall | wall | identical | ✓ |
| 14 | wall | pillar | not judged yet | ? |
| 15 | wall | pillar | not judged yet | ? |
| 16 | floor | wall | mismatch | ✗ |
| 17 | swim ring | signboard | not judged yet | ? |
| 18 | wall | brick wall | not judged yet | ? |
| 19 | grass | pole (uncertain) | mismatch | ✗ |
| 20 | person | person | identical | ✓ |
| 21 | person | person | identical | ✓ |
| 22 | window | window | identical | ✓ |
| 23 | storage reel | ladder | not judged yet | ? |
| 24 | floatation device | pillar | mismatch | ✗ |
| 25 | poolside step | ladder | not judged yet | ? |
| 26 | door | window | semantic overlap | ✓ |
| 27 | window | window | identical | ✓ |
| 28 | chair | vent (uncertain) | not judged yet | ? |
| 29 | door | door | identical | ✓ |
| 30 | shelf | vent (uncertain) | not judged yet | ? |
| 31 | poolside step | fan | not judged yet | ? |
| 32 | fan | fan | identical | ✓ |
| 33 | storage reel center | ladder | not judged yet | ? |
| 34 | wheel | ladder | not judged yet | ? |
| 35 | wheel | ladder | not judged yet | ? |
| 36 | tyre | person | not judged yet | ? |
| 37 | tyre | person | not judged yet | ? |
| 38 | tyre | trash can (uncertain) | not judged yet | ? |
| 39 | tyre | trash can (uncertain) | not judged yet | ? |
| 40 | head | - | no label from TRASER | ✗ |
| 41 | head | - | no label from TRASER | ✗ |
| 42 | head | - | no label from TRASER | ✗ |
| 43 | head | - | no label from TRASER | ✗ |
| 44 | head | - | no label from TRASER | ✗ |
| 45 | head | - | no label from TRASER | ✗ |
| 46 | head | - | no label from TRASER | ✗ |
| 47 | life jacket | - | no label from TRASER | ✗ |
| 48 | life jacket | - | no label from TRASER | ✗ |
| 49 | life jacket | - | no label from TRASER | ✗ |
| 50 | life jacket | - | no label from TRASER | ✗ |
| 51 | life jacket | - | no label from TRASER | ✗ |
| 52 | life jacket | - | no label from TRASER | ✗ |
| 53 | life jacket | - | no label from TRASER | ✗ |
| 54 | shirt | - | no label from TRASER | ✗ |
| 55 | shirt | - | no label from TRASER | ✗ |
| 56 | shirt | - | no label from TRASER | ✗ |
| 57 | short | - | no label from TRASER | ✗ |

**Relations: 1/50 right, triplets: 0/50 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| boat #0 - moving on - pool #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| boat #0 - in - pool #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| boat #0 - in front of - wall #13 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ? |
| bucket #1 - in - boat #0 | 0-8 | inside | 0-9 | not judged yet | 0.89 | ? | ✗ |
| bucket #3 - in - boat #0 | 3-5, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - wearing - life jacket #48 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - aboard - boat #0 | 0-8 | inside | 0-9 | not judged yet | 0.89 | ? | ? |
| person #4 - in - boat #0 | 0-8 | inside | 0-9 | not judged yet | 0.89 | ? | ? |
| person #4 - holding - bucket #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - wearing - life jacket #49 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - aboard - boat #0 | 0-8 | inside | 0-9 | not judged yet | 0.89 | ? | ? |
| person #5 - in - boat #0 | 0-8 | inside | 0-9 | not judged yet | 0.89 | ? | ? |
| person #5 - splashing with - bucket #2 | 1-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - holding - bucket #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #6 - holding - bucket #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #6 - splashing with - bucket #3 | 4.5-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #6 - wearing - life jacket #51 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #6 - aboard - boat #0 | 0-8 | inside | 0-9 | not judged yet | 0.89 | ? | ? |
| person #6 - in - boat #0 | 0-8 | inside | 0-9 | not judged yet | 0.89 | ? | ? |
| person #7 - wearing - life jacket #50 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #7 - aboard - boat #0 | 0-8 | inside | 0-9 | not judged yet | 0.89 | ? | ? |
| person #7 - in - boat #0 | 0-8 | inside | 0-9 | not judged yet | 0.89 | ? | ? |
| person #9 - holding - bucket #11 | 0-1, 2-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #9 - splashing with - bucket #11 | 2-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #9 - wearing - life jacket #53 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #10 - wearing - life jacket #52 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| swim ring #17 - on - wall #13 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| storage reel #23 - in front of - window #22 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| poolside step #25 - beside - pool #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #28 - on - floor #16 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| poolside step #31 - beside - pool #8 | 2-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| fan #32 - on - floor #16 | 3-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| storage reel center #33 - on - storage reel #23 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #34 - on - storage reel #23 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #35 - on - storage reel #23 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #40 - on - person #4 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #41 - on - person #5 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #42 - on - person #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #43 - on - person #10 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #44 - on - person #6 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #45 - on - person #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| life jacket #48 - on - person #4 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| life jacket #49 - on - person #5 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| life jacket #50 - on - person #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| life jacket #51 - on - person #6 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| life jacket #52 - on - person #10 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| life jacket #53 - on - person #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #54 - on - person #4 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #55 - on - person #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #56 - on - person #6 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (121): boat #0 - in front of - floor #16 [0-9]; boat #0 - in front of - window #22 [0-9]; boat #0 - in front of - storage reel #23 [0-9]; boat #0 - in front of - floatation device #24 [0-9]; boat #0 - in front of - door #29 [4-9]; boat #0 - in front of - poolside step #31 [3-9]; boat #0 - in front of - fan #32 [4-9]; boat #0 - in front of - wall #14 [0-9]; boat #0 - in front of - wall #15 [0-9]; bucket #2 - inside - boat #0 [0-9]


## 308_7WhzIsqPQW8

22.67 s, 23 frames read | human: 42 objects, 41 relations | TRASER: 40 objects, 163 relations, valid JSON, 5376 tokens

**Objects: 6/42 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | referee | person | not judged yet | ? |
| 1 | dancer | person | not judged yet | ? |
| 2 | dancer | person | not judged yet | ? |
| 3 | dance floor | dancer | not judged yet | ? |
| 4 | trash can | banner | not judged yet | ? |
| 5 | background floor | stage | not judged yet | ? |
| 6 | country logo | signboard | not judged yet | ? |
| 7 | country logo | signboard | not judged yet | ? |
| 8 | country logo | signboard | not judged yet | ? |
| 9 | country logo | signboard | not judged yet | ? |
| 10 | flower vase | signboard | not judged yet | ? |
| 11 | country logo | signboard | not judged yet | ? |
| 12 | flower vase | flower arrangement | not judged yet | ? |
| 13 | country logo | signboard | not judged yet | ? |
| 14 | flower vase | flower arrangement | not judged yet | ? |
| 15 | bottle water | bottle | not judged yet | ? |
| 16 | flower vase | flower arrangement | not judged yet | ? |
| 17 | logo | television set | not judged yet | ? |
| 18 | flower vase | flower arrangement | not judged yet | ? |
| 19 | flower vase | flower arrangement | not judged yet | ? |
| 20 | flower vase | flower arrangement | not judged yet | ? |
| 21 | bottle | bottle | identical | ✓ |
| 22 | cup | tablecloth | not judged yet | ? |
| 23 | paper | tablecloth | not judged yet | ? |
| 24 | paper | tablecloth | not judged yet | ? |
| 25 | bottle water | chair | not judged yet | ? |
| 26 | bottle water | bottle | not judged yet | ? |
| 27 | table | banner | not judged yet | ? |
| 28 | face | person | hypernym/hyponym | ✓ |
| 29 | hair | hair | identical | ✓ |
| 30 | skirt | skirt | identical | ✓ |
| 31 | hand | handbag | mismatch | ✗ |
| 32 | hand | handbag | mismatch | ✗ |
| 33 | leg | legs (uncertain) | identical | ✓ |
| 34 | leg | legs (uncertain) | identical | ✓ |
| 35 | shirt | dress | not judged yet | ? |
| 36 | head | person | mismatch | ✗ |
| 37 | jacket | suit jacket | not judged yet | ? |
| 38 | shirt | suit jacket | not judged yet | ? |
| 39 | trouser | trousers | not judged yet | ? |
| 40 | head | - | no label from TRASER | ✗ |
| 41 | shoes | - | no label from TRASER | ✗ |

**Relations: 2/41 right, triplets: 0/41 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| referee #0 - on - dance floor #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| referee #0 - in front of - dancer #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| referee #0 - in front of - dancer #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| referee #0 - wears - jacket #37 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| dancer #1 - on - dance floor #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| dancer #1 - in front of - table #27 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ? |
| dancer #1 - dances with - dancer #2 | 0-23 | dancing with (+2 more) | 0-24 | not judged yet | 0.96 | ? | ? |
| dancer #1 - moves with - dancer #2 | 0-23 | dancing with (+2 more) | 0-24 | not judged yet | 0.96 | ? | ? |
| dancer #1 - performs routine with - dancer #2 | 0-23 | dancing with (+2 more) | 0-24 | not judged yet | 0.96 | ? | ? |
| dancer #1 - overlapping - dancer #2 | 13.5-20.5 | dancing with (+2 more) | 0-24 | not judged yet | 0.29 | ✗ | ✗ |
| dancer #1 - wears - skirt #30 | 0-23 | wearing | 0-24 | not judged yet | 0.96 | ? | ? |
| dancer #1 - wears - shirt #35 | 0-23 | wearing | 0-24 | not judged yet | 0.96 | ? | ? |
| dancer #2 - on - dance floor #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| dancer #2 - in front of - table #27 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ? |
| dancer #2 - follows - dancer #1 | 19-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| dancer #2 - holds - dancer #1 | 12-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| dancer #2 - approaches - dancer #1 | 0-12 | nothing for this pair | - | - | - | ✗ | ✗ |
| dancer #2 - wears - shirt #38 | 0-23 | wearing | 0-24 | not judged yet | 0.96 | ? | ? |
| dancer #2 - wears - trouser #39 | 0-23 | wearing | 0-24 | not judged yet | 0.96 | ? | ? |
| dance floor #3 - in front of - table #27 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| trash can #4 - on - background floor #5 | 0-12, 21-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| country logo #6 - on - table #27 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| country logo #7 - on - table #27 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| country logo #8 - on - table #27 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| country logo #9 - on - table #27 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| flower vase #10 - on - table #27 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| country logo #11 - on - table #27 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| flower vase #12 - on - table #27 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| country logo #13 - on - table #27 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| flower vase #14 - on - table #27 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| flower vase #16 - on - table #27 | 0-15, 20-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| flower vase #18 - on - table #27 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| flower vase #19 - on - table #27 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| flower vase #20 - on - table #27 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| bottle #21 - on - table #27 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| cup #22 - on - table #27 | 8-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| paper #23 - on - table #27 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| paper #24 - on - table #27 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| bottle water #25 - on - table #27 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| bottle water #26 - on - table #27 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| table #27 - on - background floor #5 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (154): dancer #1 - carrying - hand #31 [0-24]; dancer #1 - carrying - hand #32 [0-24]; dancer #1 - in front of - background floor #5 [0-24]; dancer #2 - in front of - background floor #5 [0-24]; dancer #1 - in front of - logo #17 [0-24]; dancer #1 - in front of - logo #17 [0-24]; dancer #1 - in front of - logo #17 [0-24]; dancer #1 - in front of - logo #17 [0-24]; dancer #1 - in front of - logo #17 [0-24]; dancer #2 - in front of - logo #17 [0-24]


## 339_j2gELsuQ3Cg

5.0 s, 5 frames read | human: 14 objects, 20 relations | TRASER: 14 objects, 19 relations, valid JSON, 1081 tokens

**Objects: 7/14 right**

| id | human label | TRASER label | verdict | right |
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

**Relations: 0/20 right, triplets: 0/20 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - looks at - clothes #1 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - touches - clothes #1 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - moves leftward - clothes #1 | 2-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - wears - shirt #12 | 0-5 | wearing (+1 more) | 0-6 | not judged yet | 0.83 | ? | ? |
| person #0 - in front of - closet #4 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - browses - closet #4 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| clothes #1 - in - closet #4 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| clothes #1 - behind - person #0 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| clothes #2 - behind - person #0 | 0-5.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| clothes #3 - behind - person #0 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| closet divider #5 - behind - person #0 | 1.5-3.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| closet divider #6 - behind - person #0 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| closet shelf #7 - below - closet divider #6 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| hair #8 - in front of - closet #4 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| face #9 - in front of - closet #4 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #10 - in front of - clothes #1 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #10 - in front of - closet #4 | 0-2.5, 3-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #10 - below - face #9 | 0-2.5, 4.5-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| shoulder #11 - below - face #9 | 0-5 | overlapping | 0-6 | not judged yet | 0.83 | ? | ? |
| shirt #12 - below - face #9 | 0-5 | overlapping | 0-6 | not judged yet | 0.83 | ? | ? |

TRASER relations between pairs the humans did not annotate (15): person #0 - wearing - shoulder #11 [0-6]; person #0 - in front of - shoulder #11 [0-6]; person #0 - has - hair #8 [0-6]; person #0 - in front of - hair #8 [0-6]; person #0 - has - hand #10 [0-6]; person #0 - in front of - hand #10 [0-6]; person #0 - looking at - face #9 [0-6]; person #0 - in front of - face #9 [0-6]; shoulder #11 - overlapping - shirt #12 [0-6]; hair #8 - overlapping - shoulder #11 [0-6]


## 359_4ZPKJtcNGZE

22.67 s, 23 frames read | human: 27 objects, 20 relations | TRASER: 27 objects, 19 relations, valid JSON, 1876 tokens

**Objects: 2/27 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | grass | dog | mismatch | ✗ |
| 1 | grass | dog | mismatch | ✗ |
| 2 | drainage | water | mismatch | ✗ |
| 3 | tractor | bulldozer | not judged yet | ? |
| 4 | trees | plant | not judged yet | ? |
| 5 | rod | machine part (uncertain) | not judged yet | ? |
| 6 | rod | machine component (uncertain) | not judged yet | ? |
| 7 | rod | pipe (uncertain) | not judged yet | ? |
| 8 | stick | log (uncertain) | not judged yet | ? |
| 9 | tyre | wheel | not judged yet | ? |
| 10 | rod | pipe (uncertain) | not judged yet | ? |
| 11 | excavator arm | pipe (uncertain) | mismatch | ✗ |
| 12 | excavator boom arm | blade (uncertain) | not judged yet | ? |
| 13 | tire | wheel | not judged yet | ? |
| 14 | boom cylinder | pipe (uncertain) | semantic overlap | ✓ |
| 15 | steering wheel | pipe (uncertain) | not judged yet | ? |
| 16 | valve | pipe (uncertain) | not judged yet | ? |
| 17 | rock | rock | identical | ✓ |
| 18 | rod | pole (uncertain) | not judged yet | ? |
| 19 | excavator boom hinge | pipe (uncertain) | mismatch | ✗ |
| 20 | rod | pipe (uncertain) | not judged yet | ? |
| 21 | rod | pipe (uncertain) | not judged yet | ? |
| 22 | rod | pipe (uncertain) | not judged yet | ? |
| 23 | rod | pipe (uncertain) | not judged yet | ? |
| 24 | dashboard | pipe (uncertain) | mismatch | ✗ |
| 25 | component | vent (uncertain) | not judged yet | ? |
| 26 | rod | pipe (uncertain) | not judged yet | ? |

**Relations: 2/20 right, triplets: 0/20 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| drainage #2 - adjacent to - grass #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| drainage #2 - below - grass #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| drainage #2 - adjacent to - grass #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| drainage #2 - below - grass #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tractor #3 - on - grass #0 | 8-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tractor #3 - in front of - trees #4 | 8-23 | in front of | 8-24 | identical | 0.94 | ✓ | ? |
| tractor #3 - beside - drainage #2 | 7.5-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tractor #3 - attached to - excavator boom arm #12 | 10-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| tractor #3 - attached to - tire #13 | 10-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| tractor #3 - attached to - tyre #9 | 22-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tractor #3 - attached to - boom cylinder #14 | 10-17, 21-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tractor #3 - attached to - steering wheel #15 | 21-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| stick #8 - above - drainage #2 | 7.5-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| excavator arm #11 - above - drainage #2 | 7-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| excavator boom arm #12 - above - drainage #2 | 11-22.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| excavator boom arm #12 - in front of - trees #4 | 11-22.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| excavator boom arm #12 - moves relative to - tractor #3 | 11-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| rock #17 - on - grass #0 | 6-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| rock #17 - above - drainage #2 | 6-23 | near | 7-24 | not judged yet | 0.89 | ? | ✗ |
| rock #17 - in front of - tractor #3 | 8-23 | near | 8-24 | hypernym/hyponym | 0.94 | ✓ | ? |

TRASER relations between pairs the humans did not annotate (16): grass #0 - approaches - drainage #2 [0-3]; grass #0 - moves away from - drainage #2 [2-4]; grass #0 - looks at - drainage #2 [1-24]; grass #0 - in front of - drainage #2 [0-24]; grass #0 - near - drainage #2 [0-24]; grass #0 - in front of - tractor #3 [8-24]; grass #0 - in front of - trees #4 [7-24]; grass #0 - in front of - rock #17 [7-24]; drainage #2 - in front of - tractor #3 [8-24]; drainage #2 - in front of - trees #4 [7-24]


## 365_JFqiSr9A-Go

5.0 s, 5 frames read | human: 48 objects, 53 relations | TRASER: 40 objects, 6 relations, valid JSON, 2259 tokens

**Objects: 19/48 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | accessory shelf | pegboard | mismatch | ✗ |
| 1 | accessory shelf | speaker | mismatch | ✗ |
| 2 | paper shredder | speaker | mismatch | ✗ |
| 3 | monitor | computer monitor | hypernym/hyponym | ✓ |
| 4 | coffee maker | coffee pot | synonym | ✓ |
| 5 | monitor stand | desk | mismatch | ✗ |
| 6 | person | person | identical | ✓ |
| 7 | keyboard | keyboard | identical | ✓ |
| 8 | mouse | computer mouse | hypernym/hyponym | ✓ |
| 9 | chair | chair | identical | ✓ |
| 10 | shelf | shelf | identical | ✓ |
| 11 | table | desk | not judged yet | ? |
| 12 | wall | wall | identical | ✓ |
| 13 | wall | bulletin board | not judged yet | ? |
| 14 | lamp | lamp | identical | ✓ |
| 15 | cord | shelf | mismatch | ✗ |
| 16 | artwork | poster | hypernym/hyponym | ✓ |
| 17 | artwork | picture frame | semantic overlap | ✓ |
| 18 | artwork | poster | hypernym/hyponym | ✓ |
| 19 | headset | earphones | synonym | ✓ |
| 20 | charger | earphones | mismatch | ✗ |
| 21 | cable | pegboard | mismatch | ✗ |
| 22 | charger | earphones | mismatch | ✗ |
| 23 | charger | pegboard | mismatch | ✗ |
| 24 | wire | pegboard | not judged yet | ? |
| 25 | paper | pegboard | mismatch | ✗ |
| 26 | file holder | speaker | mismatch | ✗ |
| 27 | holder | speaker | mismatch | ✗ |
| 28 | monitor screen | monitor | hypernym/hyponym | ✓ |
| 29 | monitor stand | stand | not judged yet | ? |
| 30 | monitor stand | speaker | mismatch | ✗ |
| 31 | handle | knob | synonym | ✓ |
| 32 | coffee maker base | coffee maker base | identical | ✓ |
| 33 | wood | desk | not judged yet | ? |
| 34 | wood | drawer | not judged yet | ? |
| 35 | shirt | jersey | not judged yet | ? |
| 36 | trouser | trousers | not judged yet | ? |
| 37 | hair | hair | identical | ✓ |
| 38 | face | head | hypernym/hyponym | ✓ |
| 39 | hand | arm | semantic overlap | ✓ |
| 40 | hand | - | no label from TRASER | ✗ |
| 41 | arm rest | - | no label from TRASER | ✗ |
| 42 | support | - | no label from TRASER | ✗ |
| 43 | light | - | no label from TRASER | ✗ |
| 44 | stand | - | no label from TRASER | ✗ |
| 45 | ring | - | no label from TRASER | ✗ |
| 46 | wood | - | no label from TRASER | ✗ |
| 47 | wood | - | no label from TRASER | ✗ |

**Relations: 3/53 right, triplets: 1/53 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| accessory shelf #0 - on - wall #13 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| accessory shelf #1 - on - wall #13 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| accessory shelf #1 - below - accessory shelf #0 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| paper shredder #2 - in front of - wall #13 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| monitor #3 - in front of - person #6 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| monitor #3 - in front of - wall #12 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| monitor #3 - above - table #11 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| monitor #3 - supported by - monitor stand #29 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| monitor #3 - mounted on - monitor stand #29 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| monitor #3 - above - monitor stand #5 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| coffee maker #4 - in front of - wall #12 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| coffee maker #4 - on - table #11 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| monitor stand #5 - on - table #11 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #6 - on - chair #9 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #6 - sitting on - chair #9 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #6 - typing on - keyboard #7 | 3-6 | using | 0-7 | not judged yet | 0.43 | ✗ | ✗ |
| person #6 - looking at - keyboard #7 | 3-6 | using | 0-7 | not judged yet | 0.43 | ✗ | ✗ |
| person #6 - wearing - shirt #35 | 0-6 | wearing | 0-7 | identical | 0.86 | ✓ | ? |
| person #6 - wearing - trouser #36 | 0-6 | wearing | 0-7 | identical | 0.86 | ✓ | ? |
| person #6 - wearing - ring #45 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #6 - working on - monitor #3 | 0-6 | working on (+1 more) | 0-7 | identical | 0.86 | ✓ | ✓ |
| person #6 - looking at - monitor #3 | 0-3.5 | looking at (+1 more) | 0-7 | identical | 0.50 | ✗ | ✗ |
| person #6 - using - mouse #8 | 0-3 | using | 0-7 | identical | 0.43 | ✗ | ✗ |
| keyboard #7 - in front of - person #6 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| keyboard #7 - below - monitor #3 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| keyboard #7 - on - table #11 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| mouse #8 - below - monitor #3 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| mouse #8 - on - table #11 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #9 - in front of - wall #13 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| table #11 - in front of - wall #12 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| lamp #14 - in front of - wall #13 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| artwork #16 - on - wall #13 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| artwork #17 - on - wall #12 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| artwork #18 - on - wall #13 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| headset #19 - in front of - wall #13 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| headset #19 - hanging on - accessory shelf #0 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| charger #20 - in front of - wall #13 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| cable #21 - in front of - wall #13 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| charger #22 - on - accessory shelf #0 | 3-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| charger #23 - on - accessory shelf #0 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| wire #24 - below - accessory shelf #0 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| wire #24 - above - accessory shelf #1 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| paper #25 - on - accessory shelf #0 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| file holder #26 - on - accessory shelf #1 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| holder #27 - inside - file holder #26 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| handle #31 - on - coffee maker #4 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| coffee maker base #32 - on - table #11 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #39 - touching - keyboard #7 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #40 - touching - mouse #8 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| arm rest #41 - attached to - chair #9 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| support #42 - under - chair #9 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #43 - on - stand #44 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| ring #45 - on - hand #39 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |


## 419_CykhOKWEAjo

7.5 s, 8 frames read | human: 43 objects, 32 relations | TRASER: 40 objects, 41 relations, valid JSON, 2848 tokens

**Objects: 17/43 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | tree | tree | identical | ✓ |
| 1 | tree | tree | identical | ✓ |
| 2 | tree | tree | identical | ✓ |
| 3 | tree | tree | identical | ✓ |
| 4 | tree | plant | not judged yet | ? |
| 5 | wood fence | fence | not judged yet | ? |
| 6 | sky | wire (uncertain) | not judged yet | ? |
| 7 | tree | tree | identical | ✓ |
| 8 | grass | child | not judged yet | ? |
| 9 | wood | wooden planks | not judged yet | ? |
| 10 | person | person | identical | ✓ |
| 11 | person | child | hypernym/hyponym | ✓ |
| 12 | bag | plastic bag | hypernym/hyponym | ✓ |
| 13 | mulch | leaves (uncertain) | semantic overlap | ✓ |
| 14 | trees | tree | not judged yet | ? |
| 15 | tree | plant | not judged yet | ? |
| 16 | tree | plant | not judged yet | ? |
| 17 | bags | plastic bag | hypernym/hyponym | ✓ |
| 18 | wheel | wheel | identical | ✓ |
| 19 | porch | pipe (uncertain) | not judged yet | ? |
| 20 | household material | motorcycle | mismatch | ✗ |
| 21 | plastic bucket | bucket | not judged yet | ? |
| 22 | lumber | wooden planks | hypernym/hyponym | ✓ |
| 23 | wire | tree | not judged yet | ? |
| 24 | wire | wire (uncertain) | identical | ✓ |
| 25 | lumber | shoe | not judged yet | ? |
| 26 | lumber | wooden plank (uncertain) | hypernym/hyponym | ✓ |
| 27 | wood planks | bamboo stalks | not judged yet | ? |
| 28 | t-shirt | jersey (uncertain) | not judged yet | ? |
| 29 | diaper | shorts (uncertain) | mismatch | ✗ |
| 30 | fence | pole | mismatch | ✗ |
| 31 | fence post | pole | synonym | ✓ |
| 32 | fence post | pole | synonym | ✓ |
| 33 | fence post | arm (uncertain) | mismatch | ✗ |
| 34 | fence post | trash can (uncertain) | not judged yet | ? |
| 35 | wood | vent (uncertain) | not judged yet | ? |
| 36 | t-shirt | shirt | not judged yet | ? |
| 37 | head | hair (uncertain) | semantic overlap | ✓ |
| 38 | head | child | mismatch | ✗ |
| 39 | wood plank | wooden plank (uncertain) | not judged yet | ? |
| 40 | wood | - | no label from TRASER | ✗ |
| 41 | saw | - | no label from TRASER | ✗ |
| 42 | trouser | - | no label from TRASER | ✗ |

**Relations: 8/32 right, triplets: 3/32 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| sky #6 - above - wood fence #5 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| wood #9 - in front of - wood fence #5 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ? |
| wood #9 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #10 - near - wood #9 | 0-8 | near | 0-8 | identical | 1.00 | ✓ | ? |
| person #10 - cutting - wood #9 | 0-2, 5-7 | near | 0-8 | not judged yet | 0.50 | ✗ | ✗ |
| person #10 - working on - wood #9 | 0-8 | near | 0-8 | not judged yet | 1.00 | ? | ? |
| person #10 - in front of - wood fence #5 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ? |
| person #10 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #10 - holding - saw #41 | 0-4, 5-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #10 - looking at - saw #41 | 0-4, 5-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #11 - near - wood #9 | 0-8 | near | 0-8 | identical | 1.00 | ✓ | ? |
| person #11 - in front of - person #10 | 0-8 | in front of (+3 more) | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #11 - looking at - person #10 | 0-8 | looking at (+3 more) | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #11 - looking at - person #10 | 0-5 | looking at (+3 more) | 0-8 | identical | 0.62 | ✓ | ✓ |
| person #11 - in front of - wood fence #5 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ? |
| person #11 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bag #12 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bags #17 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #18 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| porch #19 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| household material #20 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plastic bucket #21 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| lumber #22 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| wire #23 - above - wood fence #5 | 0-8 | behind | 0-8 | not judged yet | 1.00 | ? | ? |
| wire #24 - above - wood fence #5 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| lumber #25 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| t-shirt #28 - on - person #11 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| diaper #29 - on - person #11 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| t-shirt #36 - on - person #10 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| saw #41 - on - lumber #25 | 0-3, 6-7.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| saw #41 - moving on - wood #9 | 0-2.5, 5-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| trouser #42 - on - person #10 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (31): person #11 - holding - wood planks #27 [0-8]; person #11 - near - wood planks #27 [0-8]; person #10 - wearing - t-shirt #36 [0-8]; person #10 - looking at - person #11 [0-8]; lumber #22 - in front of - wood fence #5 [0-8]; wood planks #27 - in front of - wood fence #5 [0-8]; plastic bucket #21 - in front of - wood fence #5 [0-8]; bag #12 - in front of - wood fence #5 [0-8]; bags #17 - in front of - wood fence #5 [0-8]; wheel #18 - in front of - wood fence #5 [0-8]


## 434_eOTP9yrATX8

7.5 s, 8 frames read | human: 14 objects, 37 relations | TRASER: 14 objects, 33 relations, valid JSON, 1245 tokens

**Objects: 8/14 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | forest | forest | identical | ✓ |
| 1 | car | car | identical | ✓ |
| 2 | people | person | hypernym/hyponym | ✓ |
| 3 | snow field or road | snow | not judged yet | ? |
| 4 | object (uncertain) | person | not judged yet | ? |
| 5 | window | car's side mirror | not judged yet | ? |
| 6 | window | car's side mirror | not judged yet | ? |
| 7 | plate | wheel | not judged yet | ? |
| 8 | wheel | wheel | identical | ✓ |
| 9 | wheel | wheel | identical | ✓ |
| 10 | wheel | wheel | identical | ✓ |
| 11 | rear wing | windshield wiper | not judged yet | ? |
| 12 | light | headlight | hypernym/hyponym | ✓ |
| 13 | light | headlight | hypernym/hyponym | ✓ |

**Relations: 12/37 right, triplets: 6/37 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| car #1 - moves away from - people #2 | 0-4 | moving away from | 0-9 | not judged yet | 0.44 | ✗ | ✗ |
| car #1 - on - snow field or road #3 | 0-8 | moving on (+2 more) | 0-9 | hypernym/hyponym | 0.89 | ✓ | ? |
| car #1 - drives along - snow field or road #3 | 0-8 | moving on (+2 more) | 0-9 | not judged yet | 0.89 | ? | ? |
| car #1 - in front of - forest #0 | 0-8 | in front of (+1 more) | 0-9 | identical | 0.89 | ✓ | ✓ |
| people #2 - behind - car #1 | 0-4.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| people #2 - on - snow field or road #3 | 0-4 | on | 0-9 | identical | 0.44 | ✗ | ✗ |
| people #2 - moves along - snow field or road #3 | 0-4.5 | on | 0-9 | not judged yet | 0.50 | ✗ | ✗ |
| people #2 - in front of - forest #0 | 0-4 | in front of | 0-9 | identical | 0.44 | ✗ | ✗ |
| snow field or road #3 - in front of - forest #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| object (uncertain) #4 - on - snow field or road #3 | 6-8 | on | 0-9 | identical | 0.22 | ✗ | ✗ |
| object (uncertain) #4 - behind - car #1 | 7-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #5 - attached to - car #1 | 0-8 | attached to | 0-9 | identical | 0.89 | ✓ | ? |
| window #5 - part of - car #1 | 0-8 | attached to | 0-9 | not judged yet | 0.89 | ? | ? |
| window #5 - above - wheel #10 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #6 - attached to - car #1 | 0-8 | attached to | 0-9 | identical | 0.89 | ✓ | ? |
| window #6 - part of - car #1 | 0-8 | attached to | 0-9 | not judged yet | 0.89 | ? | ? |
| window #6 - above - wheel #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plate #7 - attached to - car #1 | 0-8 | attached to | 0-9 | identical | 0.89 | ✓ | ? |
| plate #7 - part of - car #1 | 0-8 | attached to | 0-9 | not judged yet | 0.89 | ? | ? |
| wheel #8 - attached to - car #1 | 0-8 | attached to | 0-9 | identical | 0.89 | ✓ | ✓ |
| wheel #8 - part of - car #1 | 0-8 | attached to | 0-9 | not judged yet | 0.89 | ? | ? |
| wheel #8 - on - snow field or road #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #9 - attached to - car #1 | 0-8 | attached to | 0-9 | identical | 0.89 | ✓ | ✓ |
| wheel #9 - part of - car #1 | 0-8 | attached to | 0-9 | not judged yet | 0.89 | ? | ? |
| wheel #9 - on - snow field or road #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #10 - attached to - car #1 | 0-8 | attached to | 0-9 | identical | 0.89 | ✓ | ✓ |
| wheel #10 - part of - car #1 | 0-8 | attached to | 0-9 | not judged yet | 0.89 | ? | ? |
| wheel #10 - on - snow field or road #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| rear wing #11 - attached to - car #1 | 0-7 | attached to | 0-9 | identical | 0.78 | ✓ | ? |
| rear wing #11 - part of - car #1 | 0-8 | attached to | 0-9 | not judged yet | 0.89 | ? | ? |
| rear wing #11 - above - wheel #9 | 0-8 | above | 0-9 | identical | 0.89 | ✓ | ? |
| light #12 - attached to - car #1 | 0-8 | attached to | 0-9 | identical | 0.89 | ✓ | ✓ |
| light #12 - part of - car #1 | 0-8 | attached to | 0-9 | not judged yet | 0.89 | ? | ? |
| light #12 - above - plate #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #13 - attached to - car #1 | 0-8 | attached to | 0-9 | identical | 0.89 | ✓ | ✓ |
| light #13 - part of - car #1 | 0-8 | attached to | 0-9 | not judged yet | 0.89 | ? | ? |
| light #13 - above - plate #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (14): car #1 - moving away from - object (uncertain) #4 [0-9]; object (uncertain) #4 - in front of - forest #0 [0-9]; light #12 - above - wheel #10 [0-9]; light #13 - above - wheel #8 [0-9]; rear wing #11 - above - wheel #10 [0-9]; light #12 - in front of - forest #0 [0-9]; light #13 - in front of - forest #0 [0-9]; rear wing #11 - in front of - forest #0 [0-9]; window #5 - in front of - forest #0 [0-9]; window #6 - in front of - forest #0 [0-9]


## 465_nbJ_SLWUDxk

7.5 s, 8 frames read | human: 39 objects, 24 relations | TRASER: 39 objects, 52 relations, valid JSON, 2578 tokens

**Objects: 32/39 right**

| id | human label | TRASER label | verdict | right |
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

**Relations: 4/24 right, triplets: 2/24 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - in front of - person #7 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #0 - wears - hat #37 | 0-8 | wearing | 0-9 | not judged yet | 0.89 | ? | ? |
| person #0 - wears - suit #38 | 0-8 | wearing | 0-9 | not judged yet | 0.89 | ? | ? |
| person #0 - performs for - person #1 | 0-8 | in front of | 0-9 | not judged yet | 0.89 | ? | ? |
| person #0 - approaches - person #1 | 0-5 | in front of | 0-9 | not judged yet | 0.56 | ? | ? |
| person #0 - on - ground #29 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - in front of - buildings #30 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✗ |
| person #1 - in front of - person #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - looks at - person #0 | 5-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - dances with - person #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - in front of - person #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - on - ground #29 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - in front of - buildings #30 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - wears - shoes #36 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - on - ground #29 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - in front of - buildings #30 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #24 - looks at - person #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #31 - above - buildings #30 | 0-8 | in front of | 0-9 | not judged yet | 0.89 | ? | ✗ |
| river #32 - behind - person #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #33 - above - ground #29 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #34 - above - ground #29 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| shoes #36 - on - person #2 | 0-6.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| hat #37 - on - person #0 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✓ |
| suit #38 - on - person #0 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ? |

TRASER relations between pairs the humans did not annotate (44): person #0 - holding - saxophone #35 [0-9]; person #0 - playing - saxophone #35 [0-9]; person #0 - looking at - saxophone #35 [0-9]; person #0 - performing with - saxophone #35 [0-9]; saxophone #35 - in front of - person #0 [0-9]; saxophone #35 - below - person #0 [0-9]; shoes #36 - below - person #0 [0-9]; shoes #36 - below - saxophone #35 [0-9]; saxophone #35 - in front of - buildings #30 [0-9]; hat #37 - above - suit #38 [0-9]


## 470_BiIqH60-A1M

7.5 s, 8 frames read | human: 36 objects, 30 relations | TRASER: 36 objects, 44 relations, valid JSON, 2586 tokens

**Objects: 14/36 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | person | person | identical | ✓ |
| 1 | person | person | identical | ✓ |
| 2 | kid | child | identical | ✓ |
| 3 | dad | person | hypernym/hyponym | ✓ |
| 4 | floor | floor | identical | ✓ |
| 5 | painting | painting | identical | ✓ |
| 6 | wall | pipe (uncertain) | not judged yet | ? |
| 7 | roof | ceiling (uncertain) | not judged yet | ? |
| 8 | pavement | wall | mismatch | ✗ |
| 9 | person | flower arrangement | not judged yet | ? |
| 10 | shirt | jacket | not judged yet | ? |
| 11 | cap | hat (uncertain) | hypernym/hyponym | ✓ |
| 12 | face | hat (uncertain) | mismatch | ✗ |
| 13 | hair | hat (uncertain) | mismatch | ✗ |
| 14 | trouser | trousers | not judged yet | ? |
| 15 | shoe | shoe | identical | ✓ |
| 16 | shoe | shoe | identical | ✓ |
| 17 | bag | backpack | hypernym/hyponym | ✓ |
| 18 | bag | trousers | not judged yet | ? |
| 19 | shirt | shirt | identical | ✓ |
| 20 | trouser | trousers | not judged yet | ? |
| 21 | hand | handbag | mismatch | ✗ |
| 22 | hand | handbag | mismatch | ✗ |
| 23 | hair | flower arrangement | mismatch | ✗ |
| 24 | shirt | person | not judged yet | ? |
| 25 | hair | person | mismatch | ✗ |
| 26 | face | person | hypernym/hyponym | ✓ |
| 27 | shirt | person | not judged yet | ? |
| 28 | hand | handbag | mismatch | ✗ |
| 29 | face | child | mismatch | ✗ |
| 30 | trouser | trousers | not judged yet | ? |
| 31 | cap | hat (uncertain) | hypernym/hyponym | ✓ |
| 32 | jacket | person | mismatch | ✗ |
| 33 | trouser | trousers | not judged yet | ? |
| 34 | bag | shoe | mismatch | ✗ |
| 35 | face | person | hypernym/hyponym | ✓ |

**Relations: 7/30 right, triplets: 7/30 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - on - floor #4 | 0-2 | on | 0-1 | identical | 0.50 | ✗ | ✗ |
| person #0 - in front of - painting #5 | 0-2 | in front of | 0-1 | identical | 0.50 | ✗ | ✗ |
| person #1 - on - floor #4 | 0-8 | on | 0-7 | identical | 0.88 | ✓ | ✓ |
| person #1 - in front of - painting #5 | 1-8 | in front of | 0-7 | identical | 0.75 | ✓ | ✓ |
| person #1 - wears - cap #31 | 3-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - wears - jacket #32 | 0-8 | walking with (+1 more) | 0-7 | not judged yet | 0.88 | ? | ✗ |
| kid #2 - on - floor #4 | 0-8 | on | 0-7 | identical | 0.88 | ✓ | ✓ |
| kid #2 - walks on - floor #4 | 1-8 | on | 0-7 | not judged yet | 0.75 | ? | ? |
| kid #2 - in front of - painting #5 | 0-8 | in front of | 0-7 | identical | 0.88 | ✓ | ✓ |
| kid #2 - in front of - dad #3 | 0-8 | next to | 0-7 | not judged yet | 0.88 | ? | ? |
| dad #3 - on - floor #4 | 0-8 | on | 0-7 | identical | 0.88 | ✓ | ✓ |
| dad #3 - walks on - floor #4 | 0-8 | on | 0-7 | not judged yet | 0.88 | ? | ? |
| dad #3 - in front of - painting #5 | 0-8 | in front of | 0-7 | identical | 0.88 | ✓ | ✓ |
| dad #3 - holds - kid #2 | 2-8 | walking with | 0-7 | not judged yet | 0.62 | ? | ? |
| dad #3 - escorts - kid #2 | 0-8 | walking with | 0-7 | not judged yet | 0.88 | ? | ? |
| dad #3 - wears - shirt #27 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| floor #4 - below - painting #5 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| painting #5 - on - wall #6 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| wall #6 - above - floor #4 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| roof #7 - above - painting #5 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #9 - on - floor #4 | 0-2 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #9 - in front of - painting #5 | 0-2 | nothing for this pair | - | - | - | ✗ | ✗ |
| bag #17 - on - dad #3 | 0-7 | on | 0-7 | identical | 1.00 | ✓ | ✓ |
| bag #18 - on - person #9 | 0-2 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #19 - on - kid #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #27 - on - dad #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| cap #31 - on - person #1 | 1-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| jacket #32 - on - person #1 | 1-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| trouser #33 - on - person #1 | 0.5-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bag #34 - on - person #1 | 1-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (31): dad #3 - carrying - bag #17 [0-7]; dad #3 - wearing - shirt #19 [0-7]; dad #3 - wearing - trouser #20 [0-7]; dad #3 - walking with - face #29 [0-7]; kid #2 - walking with - face #29 [0-7]; kid #2 - next to - face #29 [0-7]; person #1 - walking with - face #35 [0-7]; jacket #32 - walking with - face #35 [0-7]; face #29 - on - floor #4 [0-7]; shirt #27 - on - floor #4 [0-7]


## 474_b-Qlvj48YQw

7.5 s, 8 frames read | human: 72 objects, 30 relations | TRASER: 39 objects, 69 relations, valid JSON, 3349 tokens

**Objects: 16/72 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | wall | train | not judged yet | ? |
| 1 | train | train | identical | ✓ |
| 2 | floor | platform | semantic overlap | ✓ |
| 3 | pillars | pillar | not judged yet | ? |
| 4 | display stand | door | mismatch | ✗ |
| 5 | person | person | identical | ✓ |
| 6 | person | person | identical | ✓ |
| 7 | bag | handbag | hypernym/hyponym | ✓ |
| 8 | wall | ceiling lamp | not judged yet | ? |
| 9 | camera | streetlight (uncertain) | not judged yet | ? |
| 10 | light | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 11 | light | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 12 | light | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 13 | light | signboard | mismatch | ✗ |
| 14 | light | - | no label from TRASER | ✗ |
| 15 | roof | train | not judged yet | ? |
| 16 | rail track | train track | not judged yet | ? |
| 17 | light | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 18 | light | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 19 | light | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 20 | light | vent (uncertain) | mismatch | ✗ |
| 21 | light | vent (uncertain) | mismatch | ✗ |
| 22 | light | person | not judged yet | ? |
| 23 | wall | wall panel | not judged yet | ? |
| 24 | roof | vent (uncertain) | not judged yet | ? |
| 25 | cart | door | mismatch | ✗ |
| 26 | wall | ceiling light fixture | not judged yet | ? |
| 27 | wall | wall panel | not judged yet | ? |
| 28 | door | poster | mismatch | ✗ |
| 29 | overhead structure | ceiling beam (uncertain) | not judged yet | ? |
| 30 | light | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 31 | sign | signboard | not judged yet | ? |
| 32 | sign | signboard | not judged yet | ? |
| 33 | head | hat (uncertain) | mismatch | ✗ |
| 34 | coat | suit jacket | hypernym/hyponym | ✓ |
| 35 | trouser | trousers | not judged yet | ? |
| 36 | shoe | shoe | identical | ✓ |
| 37 | shoe | shoe | identical | ✓ |
| 38 | bag | handbag | hypernym/hyponym | ✓ |
| 39 | wooden | door | not judged yet | ? |
| 40 | glass | - | no label from TRASER | ✗ |
| 41 | glass | - | no label from TRASER | ✗ |
| 42 | head | - | no label from TRASER | ✗ |
| 43 | shirt | - | no label from TRASER | ✗ |
| 44 | trouser | - | no label from TRASER | ✗ |
| 45 | camera socket | - | no label from TRASER | ✗ |
| 46 | camera | - | no label from TRASER | ✗ |
| 47 | camera | - | no label from TRASER | ✗ |
| 48 | light | - | no label from TRASER | ✗ |
| 49 | light | - | no label from TRASER | ✗ |
| 50 | light | - | no label from TRASER | ✗ |
| 51 | light | - | no label from TRASER | ✗ |
| 52 | light | - | no label from TRASER | ✗ |
| 53 | light | - | no label from TRASER | ✗ |
| 54 | door | - | no label from TRASER | ✗ |
| 55 | light | - | no label from TRASER | ✗ |
| 56 | light | - | no label from TRASER | ✗ |
| 57 | door/window | - | no label from TRASER | ✗ |
| 58 | window | - | no label from TRASER | ✗ |
| 59 | window | - | no label from TRASER | ✗ |
| 60 | door | - | no label from TRASER | ✗ |
| 61 | window | - | no label from TRASER | ✗ |
| 62 | window | - | no label from TRASER | ✗ |
| 63 | door | - | no label from TRASER | ✗ |
| 64 | light | - | no label from TRASER | ✗ |
| 65 | light | - | no label from TRASER | ✗ |
| 66 | light | - | no label from TRASER | ✗ |
| 67 | light | - | no label from TRASER | ✗ |
| 68 | light | - | no label from TRASER | ✗ |
| 69 | pillar | - | no label from TRASER | ✗ |
| 70 | pillar | - | no label from TRASER | ✗ |
| 71 | pillar | - | no label from TRASER | ✗ |

**Relations: 11/30 right, triplets: 5/30 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| train #1 - arriving at - floor #2 | 0-6 | passing | 0-8 | not judged yet | 0.75 | ? | ? |
| train #1 - under - roof #15 | 0-8 | in front of | 0-8 | not judged yet | 1.00 | ? | ? |
| train #1 - alongside - wall #0 | 0-6 | passing (+1 more) | 0-6 | not judged yet | 1.00 | ? | ? |
| train #1 - on - rail track #16 | 0-6.5 | above | 0-8 | semantic overlap | 0.81 | ✓ | ? |
| train #1 - moving along - rail track #16 | 0-8 | above | 0-8 | not judged yet | 1.00 | ? | ? |
| train #1 - approaching - person #5 | 0-5 | passing | 0-8 | not judged yet | 0.62 | ? | ? |
| train #1 - passing by - person #5 | 5-8 | passing | 0-8 | not judged yet | 0.38 | ✗ | ✗ |
| pillars #3 - on - floor #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| pillars #3 - under - overhead structure #29 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| pillars #3 - in front of - wall #23 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ? |
| display stand #4 - on - floor #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - wearing - trouser #35 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ? |
| person #5 - wearing - shoe #36 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #5 - wearing - shoe #37 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #5 - looking at - train #1 | 0-8 | looking at (+1 more) | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #5 - on - floor #2 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #5 - in front of - pillars #3 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ? |
| person #5 - wearing - coat #34 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #5 - carrying - bag #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #6 - behind - pillars #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bag #7 - near - person #5 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| camera #9 - attached to - roof #15 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #10 - attached to - roof #15 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #17 - attached to - overhead structure #29 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| cart #25 - on - floor #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| cart #25 - in front of - wall #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #28 - in - wall #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign #31 - on - wall #23 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ? |
| sign #32 - on - wall #23 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ? |
| pillar #69 - on - floor #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (52): person #5 - carrying - bag #38 [0-8]; train #1 - passing - pillars #3 [0-8]; person #5 - in front of - display stand #4 [0-8]; person #5 - in front of - cart #25 [0-8]; person #5 - in front of - wooden #39 [0-8]; person #5 - in front of - wall #23 [0-8]; person #5 - in front of - wall #27 [0-8]; person #5 - in front of - door #28 [0-8]; person #5 - in front of - sign #31 [0-8]; person #5 - in front of - sign #32 [0-8]


## 520_JbMXRRGOEkk

5.33 s, 5 frames read | human: 24 objects, 31 relations | TRASER: 24 objects, 39 relations, valid JSON, 1985 tokens

**Objects: 12/24 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | person | person | identical | ✓ |
| 1 | person | person | identical | ✓ |
| 2 | person | person | identical | ✓ |
| 3 | snow | hockey puck (uncertain) | not judged yet | ? |
| 4 | shield | banner | not judged yet | ? |
| 5 | barricade | wall panel | not judged yet | ? |
| 6 | post | hockey goal | not judged yet | ? |
| 7 | ski stick | hockey puck (uncertain) | not judged yet | ? |
| 8 | legs | trousers | mismatch | ✗ |
| 9 | jersey | jersey | identical | ✓ |
| 10 | helmet | helmet | identical | ✓ |
| 11 | glove | glove | identical | ✓ |
| 12 | glove | glove | identical | ✓ |
| 13 | hockey stick | hockey puck (uncertain) | not judged yet | ? |
| 14 | helmet | helmet | identical | ✓ |
| 15 | jersey | hooded jacket | not judged yet | ? |
| 16 | glove | glove (uncertain) | identical | ✓ |
| 17 | legs | trousers | mismatch | ✗ |
| 18 | hockey stick | shoe (uncertain) | mismatch | ✗ |
| 19 | headgear | helmet | not judged yet | ? |
| 20 | shirt | jacket | not judged yet | ? |
| 21 | pants | trousers | synonym | ✓ |
| 22 | hockey stick | hockey stick | identical | ✓ |
| 23 | hand | glove | semantic overlap | ✓ |

**Relations: 4/31 right, triplets: 0/31 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - wears - headgear #19 | 0.5-5.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - wears - shirt #20 | 1-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - wears - pants #21 | 1-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - holds - hockey stick #22 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - approaches - post #6 | 1-5.5 | in front of | 0-4 | not judged yet | 0.55 | ? | ? |
| person #0 - on - snow #3 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - in front of - shield #4 | 0-2 | in front of | 0-4 | identical | 0.50 | ✗ | ✗ |
| person #1 - wears - helmet #10 | 0-6 | wearing | 0-6 | not judged yet | 1.00 | ? | ? |
| person #1 - wears - jersey #9 | 0-6 | wearing | 0-6 | not judged yet | 1.00 | ? | ? |
| person #1 - wears - legs #8 | 0-6 | wearing | 0-6 | not judged yet | 1.00 | ? | ✗ |
| person #1 - holds - ski stick #7 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - approaches - post #6 | 1-4 | approaching (+2 more) | 0-3 | not judged yet | 0.50 | ✗ | ✗ |
| person #1 - moves away from - post #6 | 3.5-6 | moving away from (+2 more) | 3-6 | not judged yet | 0.83 | ? | ? |
| person #1 - attacks goal - post #6 | 1-3.5 | approaching (+2 more) | 0-3 | not judged yet | 0.57 | ? | ? |
| person #1 - celebrates - post #6 | 4-6 | moving away from (+2 more) | 3-6 | not judged yet | 0.67 | ? | ? |
| person #1 - chases - person #0 | 1-4 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - on - snow #3 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - in front of - shield #4 | 0-6 | in front of | 0-6 | identical | 1.00 | ✓ | ? |
| person #2 - on - snow #3 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - in front of - shield #4 | 0-5 | in front of | 0-4 | identical | 0.80 | ✓ | ? |
| snow #3 - below - barricade #5 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| snow #3 - below - shield #4 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| shield #4 - below - barricade #5 | 0-6 | on | 0-6 | not judged yet | 1.00 | ? | ? |
| post #6 - on - snow #3 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| post #6 - in front of - shield #4 | 0-6 | in front of | 0-6 | identical | 1.00 | ✓ | ? |
| post #6 - in front of - barricade #5 | 0-6 | in front of | 0-6 | identical | 1.00 | ✓ | ? |
| ski stick #7 - above - snow #3 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| legs #8 - on - snow #3 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| hockey stick #18 - above - snow #3 | 0-1 | nothing for this pair | - | - | - | ✗ | ✗ |
| pants #21 - on - snow #3 | 1-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| hockey stick #22 - above - snow #3 | 0.5-5 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (26): person #1 - wearing - glove #11 [0-6]; person #1 - wearing - glove #12 [0-6]; person #1 - wearing - hand #23 [0-6]; person #1 - holding - hockey stick #22 [0-1, 2-6]; person #1 - in front of - barricade #5 [0-6]; person #0 - in front of - barricade #5 [0-4]; person #2 - in front of - barricade #5 [0-4]; person #2 - in front of - post #6 [0-4]; helmet #10 - above - jersey #9 [0-6]; jersey #9 - above - legs #8 [0-6]


## 547_7E-Xian95Qk

6.67 s, 7 frames read | human: 22 objects, 28 relations | TRASER: 22 objects, 48 relations, valid JSON, 2047 tokens

**Objects: 3/22 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | wall | wall | identical | ✓ |
| 1 | tray | table | not judged yet | ? |
| 2 | girl | child | hypernym/hyponym | ✓ |
| 3 | man | child | not judged yet | ? |
| 4 | counter or play table | wooden toy structure | not judged yet | ? |
| 5 | toy food | toy | not judged yet | ? |
| 6 | tray | bowl | not judged yet | ? |
| 7 | drawer | table | mismatch | ✗ |
| 8 | storage with handle | fabric | not judged yet | ? |
| 9 | storage with handle | poster | not judged yet | ? |
| 10 | shelves | bookshelf | not judged yet | ? |
| 11 | shelf | wooden toy structure | not judged yet | ? |
| 12 | toy donut | doughnut | not judged yet | ? |
| 13 | toy donut | doughnut | not judged yet | ? |
| 14 | toy donut | doughnut | not judged yet | ? |
| 15 | toy donut | doughnut | not judged yet | ? |
| 16 | toy donut | doughnut | not judged yet | ? |
| 17 | toy donut | doughnut | not judged yet | ? |
| 18 | toy pastry | doughnut | not judged yet | ? |
| 19 | toy donut | doughnut | not judged yet | ? |
| 20 | toy | toy | identical | ✓ |
| 21 | toy pastry | doughnut | not judged yet | ? |

**Relations: 12/28 right, triplets: 1/28 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| girl #2 - hold - toy #20 | 0-4.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| girl #2 - look at - tray #6 | 0-4 | nothing for this pair | - | - | - | ✗ | ✗ |
| girl #2 - in front of - wall #0 | 0-7 | in front of | 0-7 | identical | 1.00 | ✓ | ✓ |
| man #3 - hold - tray #6 | 0-7 | holding (+2 more) | 0-7 | not judged yet | 1.00 | ? | ? |
| man #3 - move - tray #6 | 0-6 | holding (+2 more) | 0-7 | not judged yet | 0.86 | ? | ? |
| man #3 - show to - girl #2 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #3 - display - toy food #5 | 0-7 | holding (+2 more) | 0-7 | not judged yet | 1.00 | ? | ? |
| man #3 - in front of - wall #0 | 0-7 | in front of | 0-7 | identical | 1.00 | ✓ | ? |
| tray #6 - contain - toy food #5 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| tray #6 - carry - toy donut #12 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| tray #6 - carry - toy donut #16 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| tray #6 - in front of - man #3 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| tray #6 - in front of - girl #2 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| storage with handle #8 - on - wall #0 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| storage with handle #9 - on - wall #0 | 0-7 | on | 0-7 | identical | 1.00 | ✓ | ? |
| shelf #11 - in front of - wall #0 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| toy donut #12 - in - tray #6 | 0-7 | in | 0-7 | identical | 1.00 | ✓ | ? |
| toy donut #12 - on - toy donut #13 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| toy donut #13 - in - tray #6 | 0-7 | in | 0-7 | identical | 1.00 | ✓ | ? |
| toy donut #14 - in - tray #6 | 0-7 | in | 0-7 | identical | 1.00 | ✓ | ? |
| toy donut #15 - in - tray #6 | 0-7 | in | 0-7 | identical | 1.00 | ✓ | ? |
| toy donut #15 - on - toy donut #14 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| toy donut #16 - in - tray #6 | 0-7 | in | 0-7 | identical | 1.00 | ✓ | ? |
| toy donut #16 - on - toy donut #15 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| toy donut #17 - in - tray #6 | 0-7 | in | 0-7 | identical | 1.00 | ✓ | ? |
| toy pastry #18 - in - tray #6 | 0-7 | in | 0-7 | identical | 1.00 | ✓ | ? |
| toy donut #19 - in - tray #6 | 0-1, 3-7 | in | 0-7 | identical | 0.71 | ✓ | ? |
| toy pastry #21 - in - tray #6 | 0-7 | in | 0-7 | identical | 1.00 | ✓ | ? |

TRASER relations between pairs the humans did not annotate (30): man #3 - touching - toy donut #12 [0-7]; man #3 - touching - toy donut #13 [0-7]; man #3 - touching - toy donut #14 [0-7]; man #3 - touching - toy donut #15 [0-7]; man #3 - touching - toy donut #16 [0-7]; man #3 - touching - toy donut #17 [0-7]; man #3 - touching - toy pastry #18 [0-7]; man #3 - touching - toy donut #19 [0-7]; man #3 - touching - toy pastry #21 [0-7]; tray #6 - on - drawer #7 [0-7]


## 551_VHxQVmG1pOA

6.83 s, 7 frames read | human: 47 objects, 53 relations | TRASER: 40 objects, 40 relations, valid JSON, 2888 tokens

**Objects: 29/47 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | girl | person | hypernym/hyponym | ✓ |
| 1 | man | person | hypernym/hyponym | ✓ |
| 2 | man | person | hypernym/hyponym | ✓ |
| 3 | man | person | hypernym/hyponym | ✓ |
| 4 | man | person | hypernym/hyponym | ✓ |
| 5 | glass dome or cover | dome-shaped object (uncertain) | hypernym/hyponym | ✓ |
| 6 | glass dome or cover | dome-shaped object (uncertain) | hypernym/hyponym | ✓ |
| 7 | glass dome or cover | dome-shaped object (uncertain) | hypernym/hyponym | ✓ |
| 8 | woman | person | not judged yet | ? |
| 9 | woman | person | not judged yet | ? |
| 10 | ceiling | ceiling | identical | ✓ |
| 11 | people | person | hypernym/hyponym | ✓ |
| 12 | people | person | hypernym/hyponym | ✓ |
| 13 | logo | signboard | semantic overlap | ✓ |
| 14 | wall | archway | not judged yet | ? |
| 15 | boxes | box | identical | ✓ |
| 16 | wall | wall panel | not judged yet | ? |
| 17 | boxes (uncertain) | wall | not judged yet | ? |
| 18 | boxes (uncertain) | person | not judged yet | ? |
| 19 | light | lamp | hypernym/hyponym | ✓ |
| 20 | light | lamp | hypernym/hyponym | ✓ |
| 21 | doorway | column | not judged yet | ? |
| 22 | wall | column | not judged yet | ? |
| 23 | display counter | display case | semantic overlap | ✓ |
| 24 | display counter | display case | semantic overlap | ✓ |
| 25 | watch | watch | identical | ✓ |
| 26 | glass | sunglasses | mismatch | ✗ |
| 27 | cake | cake | identical | ✓ |
| 28 | cake | cake | identical | ✓ |
| 29 | cake | cake | identical | ✓ |
| 30 | cake | cake | identical | ✓ |
| 31 | cake | cake | identical | ✓ |
| 32 | cake | cake | identical | ✓ |
| 33 | cake | cake | identical | ✓ |
| 34 | countertop | countertop (uncertain) | identical | ✓ |
| 35 | pastries | pastry (uncertain) | identical | ✓ |
| 36 | pastries | pastry (uncertain) | identical | ✓ |
| 37 | pastries | pastry (uncertain) | identical | ✓ |
| 38 | countertop | tray (uncertain) | mismatch | ✗ |
| 39 | t-shirt | shirt | not judged yet | ? |
| 40 | clothes | - | no label from TRASER | ✗ |
| 41 | hair clip | - | no label from TRASER | ✗ |
| 42 | t-shirt | - | no label from TRASER | ✗ |
| 43 | cake | - | no label from TRASER | ✗ |
| 44 | cake | - | no label from TRASER | ✗ |
| 45 | cake | - | no label from TRASER | ✗ |
| 46 | cake | - | no label from TRASER | ✗ |

**Relations: 16/53 right, triplets: 12/53 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| girl #0 - wearing - watch #25 | 0-7 | wearing | 0-8 | identical | 0.88 | ✓ | ✓ |
| girl #0 - wearing - glass #26 | 0-7 | wearing | 0-8 | identical | 0.88 | ✓ | ✗ |
| girl #0 - in front of - display counter #23 | 0-7 | in front of (+3 more) | 0-8 | identical | 0.88 | ✓ | ✓ |
| girl #0 - browsing at - display counter #23 | 0-7 | looking at (+3 more) | 0-8 | not judged yet | 0.88 | ? | ? |
| girl #0 - looking at - display counter #23 | 0-7 | looking at (+3 more) | 0-8 | identical | 0.88 | ✓ | ✓ |
| girl #0 - wearing - hair clip #41 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| girl #0 - wearing - t-shirt #39 | 0-7 | wearing | 0-8 | identical | 0.88 | ✓ | ? |
| man #1 - behind - display counter #23 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #2 - behind - display counter #23 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #3 - behind - display counter #23 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #4 - behind - display counter #23 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| glass dome or cover #5 - on - countertop #34 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| glass dome or cover #5 - covering - pastries #35 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| glass dome or cover #6 - on - countertop #34 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| glass dome or cover #6 - covering - pastries #36 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| glass dome or cover #7 - on - countertop #34 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| glass dome or cover #7 - covering - pastries #37 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #8 - behind - girl #0 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #8 - talking to - girl #0 | 2-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #8 - moved toward - girl #0 | 1-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #8 - in front of - display counter #23 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #8 - browsing at - display counter #23 | 2-6.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #8 - looking at - display counter #23 | 1.5-6.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #8 - wearing - t-shirt #42 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #8 - wearing - clothes #40 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #19 - on - ceiling #10 | 0-7 | under | 0-8 | not judged yet | 0.88 | ? | ? |
| light #20 - on - ceiling #10 | 0-7 | under | 0-8 | not judged yet | 0.88 | ? | ? |
| doorway #21 - in - wall #22 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| display counter #23 - in front of - wall #14 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| display counter #23 - under - ceiling #10 | 0-7 | under | 0-8 | identical | 0.88 | ✓ | ✓ |
| watch #25 - on - girl #0 | 0-7 | on | 0-8 | identical | 0.88 | ✓ | ✓ |
| glass #26 - on - girl #0 | 0-7 | on | 0-8 | identical | 0.88 | ✓ | ✗ |
| cake #27 - inside - display counter #23 | 0-7 | inside | 0-8 | identical | 0.88 | ✓ | ✓ |
| cake #28 - inside - display counter #23 | 0-7 | inside | 0-8 | identical | 0.88 | ✓ | ✓ |
| cake #29 - inside - display counter #23 | 0-7 | inside | 0-8 | identical | 0.88 | ✓ | ✓ |
| cake #30 - inside - display counter #23 | 0-7 | inside | 0-8 | identical | 0.88 | ✓ | ✓ |
| cake #31 - inside - display counter #23 | 0-7 | inside | 0-8 | identical | 0.88 | ✓ | ✓ |
| cake #32 - inside - display counter #23 | 0-7 | inside | 0-8 | identical | 0.88 | ✓ | ✓ |
| cake #33 - inside - display counter #23 | 0-7 | inside | 0-8 | identical | 0.88 | ✓ | ✓ |
| pastries #35 - under - glass dome or cover #6 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| pastries #35 - on - countertop #34 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| pastries #36 - under - glass dome or cover #6 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| pastries #36 - on - countertop #34 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| pastries #37 - under - glass dome or cover #7 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| pastries #37 - on - countertop #34 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| t-shirt #39 - on - girl #0 | 0-7 | on | 0-8 | identical | 0.88 | ✓ | ? |
| clothes #40 - on - woman #8 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| hair clip #41 - on - girl #0 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| t-shirt #42 - on - woman #8 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| cake #43 - inside - display counter #23 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| cake #44 - inside - display counter #23 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| cake #45 - inside - display counter #23 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| cake #46 - inside - display counter #23 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (20): glass #26 - above - t-shirt #39 [0-8]; watch #25 - below - t-shirt #39 [0-8]; girl #0 - in front of - display counter #24 [0-8]; girl #0 - in front of - doorway #21 [0-8]; girl #0 - in front of - wall #22 [0-8]; girl #0 - in front of - wall #14 [0-8]; girl #0 - under - ceiling #10 [0-8]; display counter #24 - under - ceiling #10 [0-8]; doorway #21 - under - ceiling #10 [0-8]; wall #22 - under - ceiling #10 [0-8]


## 562_OA61thiz9wU

20.17 s, 20 frames read | human: 40 objects, 34 relations | TRASER: 40 objects, 43 relations, valid JSON, 3233 tokens

**Objects: 3/40 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | barricade | fence | synonym | ✓ |
| 1 | tree | tree | identical | ✓ |
| 2 | sky | tree | mismatch | ✗ |
| 3 | ground | grass | semantic overlap | ✓ |
| 4 | ship | naval vessel (uncertain) | not judged yet | ? |
| 5 | tree | trees | not judged yet | ? |
| 6 | ocean | wall | not judged yet | ? |
| 7 | fence | pole (uncertain) | mismatch | ✗ |
| 8 | fence | pole (uncertain) | mismatch | ✗ |
| 9 | barricade | pole | not judged yet | ? |
| 10 | barricade | pole | not judged yet | ? |
| 11 | barricade | pole | not judged yet | ? |
| 12 | barricade | pole | not judged yet | ? |
| 13 | barricade | pole | not judged yet | ? |
| 14 | barricade | pole | not judged yet | ? |
| 15 | barricade | pole | not judged yet | ? |
| 16 | barricade | pole | not judged yet | ? |
| 17 | barricade | pole | not judged yet | ? |
| 18 | mast | structure (uncertain) | not judged yet | ? |
| 19 | gun mount | missile (uncertain) | not judged yet | ? |
| 20 | gun mount base | storage tank (uncertain) | not judged yet | ? |
| 21 | gun mount | storage tank (uncertain) | not judged yet | ? |
| 22 | people | missile (uncertain) | not judged yet | ? |
| 23 | gun mount base | storage tank (uncertain) | not judged yet | ? |
| 24 | person | missile (uncertain) | not judged yet | ? |
| 25 | hull | ship | not judged yet | ? |
| 26 | sign | signboard | not judged yet | ? |
| 27 | pole | boat | not judged yet | ? |
| 28 | anchor | boat | not judged yet | ? |
| 29 | hull number | number (uncertain) | not judged yet | ? |
| 30 | hull | ship | not judged yet | ? |
| 31 | barricade | pole | not judged yet | ? |
| 32 | barricade | pole | not judged yet | ? |
| 33 | barricade | pole | not judged yet | ? |
| 34 | barricade | pole | not judged yet | ? |
| 35 | barricade | pole | not judged yet | ? |
| 36 | barricade | pole | not judged yet | ? |
| 37 | barricade | pole | not judged yet | ? |
| 38 | barricade | pole | not judged yet | ? |
| 39 | barricade | pole | not judged yet | ? |

**Relations: 2/34 right, triplets: 1/34 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| barricade #0 - in front of - ocean #6 | 0-21 | in front of | 0-20 | identical | 0.95 | ✓ | ? |
| barricade #0 - on - ground #3 | 0-21 | on | 0-20 | identical | 0.95 | ✓ | ✓ |
| barricade #0 - in front of - ship #4 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #1 - in front of - ocean #6 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #1 - on - ground #3 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #1 - in front of - barricade #0 | 0-21 | above | 0-20 | mismatch | 0.95 | ✗ | ✗ |
| sky #2 - above - tree #1 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| ship #4 - on - ocean #6 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| ship #4 - moving past - ocean #6 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| ship #4 - below - sky #2 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| ship #4 - in front of - tree #5 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| ship #4 - carrying - people #22 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| ship #4 - moving past - tree #1 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| ship #4 - moving past - barricade #0 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #5 - behind - ocean #6 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| ocean #6 - below - sky #2 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| mast #18 - on - ship #4 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| mast #18 - mounted on - ship #4 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| gun mount #19 - on - ship #4 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| gun mount #19 - mounted on - ship #4 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| gun mount #19 - on - gun mount base #20 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| gun mount base #20 - supporting - gun mount #19 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| gun mount #21 - on - ship #4 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| gun mount #21 - mounted on - ship #4 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| gun mount #21 - on - gun mount base #23 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| people #22 - on - ship #4 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| gun mount base #23 - supporting - gun mount #21 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #24 - on - ship #4 | 11-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #24 - walking rightward relative to - barricade #0 | 11-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign #26 - behind - barricade #0 | 0-21 | above | 0-20 | not judged yet | 0.95 | ? | ? |
| anchor #28 - on - hull #25 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| anchor #28 - attached to - ship #4 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| hull number #29 - on - hull #25 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| hull number #29 - printed on - hull #25 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (39): hull #25 - moves left relative to - tree #1 [0-20]; hull #25 - moves left relative to - barricade #0 [0-20]; hull #25 - behind - barricade #0 [0-20]; hull #25 - above - barricade #0 [0-20]; hull #25 - moves left relative to - ocean #6 [0-20]; hull #25 - above - ocean #6 [0-20]; hull #25 - moves left relative to - sign #26 [0-20]; hull #25 - moves left relative to - pole #27 [0-20]; hull #25 - moves left relative to - anchor #28 [0-20]; hull #25 - in front of - tree #5 [0-20]


## 628_nQRJD435Fh4

22.67 s, 23 frames read | human: 40 objects, 52 relations | TRASER: 40 objects, 115 relations, valid JSON, 4076 tokens

**Objects: 22/40 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | ground | floor | synonym | ✓ |
| 1 | person | person | identical | ✓ |
| 2 | person | person | identical | ✓ |
| 3 | person | person | identical | ✓ |
| 4 | person | person | identical | ✓ |
| 5 | pingpong ball holder | bucket | not judged yet | ? |
| 6 | wall | wall panel | not judged yet | ? |
| 7 | door | door | identical | ✓ |
| 8 | door | door (uncertain) | identical | ✓ |
| 9 | door | door | identical | ✓ |
| 10 | door | door | identical | ✓ |
| 11 | dumpster | trash can | not judged yet | ? |
| 12 | chair | chair | identical | ✓ |
| 13 | board | banner | semantic overlap | ✓ |
| 14 | ground | floor | synonym | ✓ |
| 15 | person | person | identical | ✓ |
| 16 | person | person | identical | ✓ |
| 17 | person | person | identical | ✓ |
| 18 | person | person | identical | ✓ |
| 19 | pingpong ball holder | bucket | not judged yet | ? |
| 20 | wall | wall panel | not judged yet | ? |
| 21 | door | door | identical | ✓ |
| 22 | door | door (uncertain) | identical | ✓ |
| 23 | door | door | identical | ✓ |
| 24 | door | door | identical | ✓ |
| 25 | box | trash can | not judged yet | ? |
| 26 | chair | chair | identical | ✓ |
| 27 | fencing | banner | not judged yet | ? |
| 28 | table | table-tennis table | not judged yet | ? |
| 29 | table | table-tennis table | not judged yet | ? |
| 30 | water dispenser | chair | not judged yet | ? |
| 31 | shirt | jersey | not judged yet | ? |
| 32 | shirt | jersey | not judged yet | ? |
| 33 | shirt | person | not judged yet | ? |
| 34 | shirt | jersey | not judged yet | ? |
| 35 | clock | clock | identical | ✓ |
| 36 | head | person | mismatch | ✗ |
| 37 | head | person | mismatch | ✗ |
| 38 | head | ball | not judged yet | ? |
| 39 | head | arm (uncertain) | not judged yet | ? |

**Relations: 20/52 right, triplets: 6/52 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #1 - on - ground #0 | 0-23 | moving on (+1 more) | 0-24 | hypernym/hyponym | 0.96 | ✓ | ✓ |
| person #1 - playing table tennis with - person #2 | 0-23 | playing table tennis with (+3 more) | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #1 - competing with - person #2 | 0-23 | playing with (+3 more) | 0-24 | not judged yet | 0.96 | ? | ? |
| person #1 - wearing - shirt #31 | 0-23 | wearing | 0-24 | identical | 0.96 | ✓ | ? |
| person #1 - in front of - wall #6 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ? |
| person #1 - near - table #28 | 0-23 | near (+1 more) | 0-24 | identical | 0.96 | ✓ | ? |
| person #2 - on - ground #0 | 0-23 | moving on (+1 more) | 0-24 | hypernym/hyponym | 0.96 | ✓ | ✓ |
| person #2 - wearing - shirt #32 | 0-23 | wearing | 0-24 | identical | 0.96 | ✓ | ? |
| person #2 - in front of - wall #6 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ? |
| person #2 - near - table #28 | 0-23 | near (+1 more) | 0-24 | identical | 0.96 | ✓ | ? |
| person #3 - on - ground #0 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #3 - wearing - shirt #33 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - playing table tennis with - person #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - competing with - person #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - in front of - wall #6 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ? |
| person #3 - behind - table #28 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - near - table #29 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - on - ground #0 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #4 - wearing - shirt #34 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - in front of - wall #6 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ? |
| person #4 - behind - table #28 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - near - table #29 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| pingpong ball holder #5 - on - ground #0 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ? |
| pingpong ball holder #5 - in front of - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #7 - in - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #8 - in - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #9 - in - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #10 - in - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| dumpster #11 - on - table #28 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| dumpster #11 - in front of - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #12 - on - ground #0 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ✓ |
| chair #12 - in front of - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #12 - behind - table #28 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| board #13 - on - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| table #28 - on - ground #0 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ? |
| table #28 - in front of - wall #6 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ? |
| table #29 - in front of - wall #6 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ? |
| table #29 - behind - table #28 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| table #29 - on - ground #0 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ? |
| water dispenser #30 - on - ground #0 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ? |
| water dispenser #30 - in front of - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #31 - on - person #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #32 - on - person #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #33 - on - person #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #34 - on - person #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| clock #35 - above - table #29 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| clock #35 - on - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| clock #35 - above - table #28 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #36 - above - shirt #31 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #37 - above - shirt #32 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #38 - above - shirt #33 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #39 - above - shirt #34 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (88): person #2 - looking at - person #1 [0-24]; person #16 - on - ground #0 [0-24]; person #17 - on - ground #0 [0-24]; shirt #33 - on - ground #0 [0-24]; head #37 - on - ground #0 [0-24]; pingpong ball holder #19 - on - ground #0 [0-24]; dumpster #11 - on - ground #0 [0-24]; box #25 - on - ground #0 [0-24]; chair #26 - on - ground #0 [0-24]; person #16 - in front of - wall #6 [0-24]


## 642_ljk5b80TmkE

22.67 s, 23 frames read | human: 23 objects, 25 relations | TRASER: 23 objects, 41 relations, valid JSON, 2128 tokens

**Objects: 10/23 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | car | car | identical | ✓ |
| 1 | car | SUV | not judged yet | ? |
| 2 | car | car | identical | ✓ |
| 3 | hand or glove | wheel | mismatch | ✗ |
| 4 | vehicle (uncertain) | person | not judged yet | ? |
| 5 | vehicle (uncertain) | person | not judged yet | ? |
| 6 | pole | snow plow (uncertain) | not judged yet | ? |
| 7 | snow field | car | not judged yet | ? |
| 8 | sky | snow | not judged yet | ? |
| 9 | light | car | mismatch | ✗ |
| 10 | wheel | wheel | identical | ✓ |
| 11 | wheel | wheel | identical | ✓ |
| 12 | wheel | wheel | identical | ✓ |
| 13 | hood | windshield wiper | not judged yet | ? |
| 14 | light | headlight (uncertain) | hypernym/hyponym | ✓ |
| 15 | light | headlight (uncertain) | hypernym/hyponym | ✓ |
| 16 | light | headlight (uncertain) | hypernym/hyponym | ✓ |
| 17 | engine | car hood | not judged yet | ? |
| 18 | window | car | not judged yet | ? |
| 19 | window | car window | not judged yet | ? |
| 20 | window | car window | not judged yet | ? |
| 21 | fender | car door | semantic overlap | ✓ |
| 22 | door | car door | hypernym/hyponym | ✓ |

**Relations: 0/25 right, triplets: 0/25 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| car #0 - next to - car #1 | 0-17.1667 | in front of | 0-15 | mismatch | 0.87 | ✗ | ✗ |
| car #0 - on - snow field #7 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #1 - on - snow field #7 | 0-17.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #2 - on - snow field #7 | 0-17.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #1 - under - sky #8 | 0-17.3333 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #0 - under - sky #8 | 0-15.8333 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #2 - under - sky #8 | 0-15.8333 | nothing for this pair | - | - | - | ✗ | ✗ |
| pole #6 - near - car #0 | 16.1667-21.3333 | nothing for this pair | - | - | - | ✗ | ✗ |
| pole #6 - on - snow field #7 | 16.1667-21.3333 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #10 - part of - car #0 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #11 - part of - car #0 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #12 - part of - car #0 | 13.6667-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| hood #13 - attached to - car #0 | 0-21.3333 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #14 - part of - car #0 | 0-15.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #15 - part of - car #0 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #22 - part of - car #0 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| engine #17 - part of - car #0 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| engine #17 - below - hood #13 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| engine #17 - in front of - door #22 | 0-20 | above | 0-20 | mismatch | 1.00 | ✗ | ✗ |
| wheel #10 - in front of - wheel #12 | 0-16.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #0 - near - car #2 | 0-17.8333 | in front of | 0-18 | not judged yet | 0.99 | ? | ? |
| car #0 - in front of - vehicle (uncertain) #4 | 15.8333-20.1667 | in front of | 17-19 | identical | 0.46 | ✗ | ✗ |
| car #0 - near - vehicle (uncertain) #5 | 17-20 | in front of | 17-19 | not judged yet | 0.67 | ? | ? |
| fender #21 - part of - car #0 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand or glove #3 - in front of - car #0 | 2.33333-5 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (36): car #0 - in front of - light #9 [0-9]; car #0 - in front of - window #18 [0-15]; car #0 - in front of - window #19 [0-20]; car #0 - in front of - window #20 [0-20]; car #0 - in front of - door #22 [0-24]; car #0 - in front of - fender #21 [0-24]; car #0 - in front of - wheel #10 [0-17]; car #0 - in front of - wheel #11 [0-24]; car #0 - in front of - wheel #12 [0-1, 15-24]; car #0 - in front of - hand or glove #3 [0-3, 19-24]


## 66_927BvkIZglw

7.5 s, 8 frames read | human: 20 objects, 28 relations | TRASER: 20 objects, 25 relations, valid JSON, 1583 tokens

**Objects: 5/20 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | window | window | identical | ✓ |
| 1 | roof | ceiling | not judged yet | ? |
| 2 | light | vent (uncertain) | mismatch | ✗ |
| 3 | television | television | identical | ✓ |
| 4 | indoor pool | bathtub | semantic overlap | ✓ |
| 5 | wall | wall panel | not judged yet | ? |
| 6 | wall | wall panel | not judged yet | ? |
| 7 | wall | door frame (uncertain) | not judged yet | ? |
| 8 | water | bathtub | not judged yet | ? |
| 9 | valve | remote control (uncertain) | not judged yet | ? |
| 10 | valve | knob (uncertain) | not judged yet | ? |
| 11 | valve | knob (uncertain) | not judged yet | ? |
| 12 | valve | knob (uncertain) | not judged yet | ? |
| 13 | headrest | handle (uncertain) | not judged yet | ? |
| 14 | valve | knob (uncertain) | not judged yet | ? |
| 15 | headrest | handle (uncertain) | not judged yet | ? |
| 16 | window handle | hinge (uncertain) | not judged yet | ? |
| 17 | glass | window | semantic overlap | ✓ |
| 18 | light | vent (uncertain) | mismatch | ✗ |
| 19 | window frame | window frame | identical | ✓ |

**Relations: 1/28 right, triplets: 1/28 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| window #0 - in - wall #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #0 - mounted on - wall #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #0 - below - roof #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #0 - above - indoor pool #4 | 0-8 | above | 0-8 | identical | 1.00 | ✓ | ✓ |
| window #0 - has - window handle #16 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #0 - has - glass #17 | 0-8 | adjacent to | 0-8 | not judged yet | 1.00 | ? | ? |
| window #0 - has - window frame #19 | 0-8 | attached to (+1 more) | 0-8 | not judged yet | 1.00 | ? | ? |
| roof #1 - attached to - wall #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #2 - on - roof #1 | 0-1 | nothing for this pair | - | - | - | ✗ | ✗ |
| television #3 - on - wall #7 | 4-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| television #3 - mounted on - wall #7 | 4-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| indoor pool #4 - below - roof #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| indoor pool #4 - contains - water #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| indoor pool #4 - has - headrest #13 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| indoor pool #4 - has - headrest #15 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| indoor pool #4 - has - valve #14 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| water #8 - inside - indoor pool #4 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| valve #9 - on - indoor pool #4 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| valve #10 - on - indoor pool #4 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| valve #11 - on - indoor pool #4 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| valve #12 - on - indoor pool #4 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| headrest #13 - on - indoor pool #4 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| valve #14 - on - indoor pool #4 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| headrest #15 - on - indoor pool #4 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| window handle #16 - on - window #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| window handle #16 - on - window frame #19 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| glass #17 - inside - window #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| window frame #19 - around - glass #17 | 0-8 | adjacent to | 0-8 | not judged yet | 1.00 | ? | ? |

TRASER relations between pairs the humans did not annotate (20): glass #17 - attached to - window frame #19 [0-8]; glass #17 - inside - window frame #19 [0-8]; window frame #19 - attached to - wall #5 [0-8]; window frame #19 - in front of - wall #5 [0-8]; window frame #19 - attached to - wall #6 [0-8]; television #3 - mounted on - wall #5 [6-8]; television #3 - on - wall #5 [6-8]; glass #17 - above - indoor pool #4 [0-8]; window frame #19 - above - indoor pool #4 [0-8]; roof #1 - above - indoor pool #4 [0-8]


## 670_JboU-y2LdkU

7.5 s, 8 frames read | human: 24 objects, 33 relations | TRASER: 24 objects, 86 relations, valid JSON, 2857 tokens

**Objects: 19/24 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | grass | lawn | synonym | ✓ |
| 1 | bush | bush | identical | ✓ |
| 2 | tree | bush | semantic overlap | ✓ |
| 3 | tree | bush | semantic overlap | ✓ |
| 4 | tree | bush | semantic overlap | ✓ |
| 5 | tree | bush | semantic overlap | ✓ |
| 6 | tree | tree | identical | ✓ |
| 7 | tree | car | not judged yet | ? |
| 8 | tree | bush | semantic overlap | ✓ |
| 9 | tree | plant | not judged yet | ? |
| 10 | car | car | identical | ✓ |
| 11 | tree | bush | semantic overlap | ✓ |
| 12 | person | person | identical | ✓ |
| 13 | person | person | identical | ✓ |
| 14 | person | child | hypernym/hyponym | ✓ |
| 15 | person | person | identical | ✓ |
| 16 | person | person | identical | ✓ |
| 17 | person | person | identical | ✓ |
| 18 | person | person | identical | ✓ |
| 19 | forest | tree | semantic overlap | ✓ |
| 20 | wheel | wheel | identical | ✓ |
| 21 | headlight | car | mismatch | ✗ |
| 22 | headlight | wheel | mismatch | ✗ |
| 23 | windshield | car window | not judged yet | ? |

**Relations: 18/33 right, triplets: 18/33 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| grass #0 - in front of - forest #19 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bush #1 - on - grass #0 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| bush #1 - in front of - car #10 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| tree #3 - on - grass #0 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| tree #4 - on - grass #0 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| tree #5 - on - grass #0 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| tree #6 - on - grass #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #8 - on - grass #0 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| car #10 - on - grass #0 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| car #10 - parked on - grass #0 | 0-8 | on | 0-8 | not judged yet | 1.00 | ? | ? |
| car #10 - in front of - forest #19 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| car #10 - has - headlight #21 | 0-4, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #10 - has - headlight #22 | 3.5-5.5, 6.5-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #10 - has - windshield #23 | 0-6, 6.5-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #10 - has - wheel #20 | 0-2.5, 4.5-6.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #12 - on - grass #0 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #12 - in front of - forest #19 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #13 - on - grass #0 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #13 - in front of - forest #19 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #13 - moves away from - car #10 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #14 - on - grass #0 | 0-4, 5-8 | on | 0-8 | identical | 0.88 | ✓ | ✓ |
| person #15 - on - grass #0 | 0-4, 6-8 | on | 0-8 | identical | 0.75 | ✓ | ✓ |
| person #16 - on - grass #0 | 0-4, 6-8 | on | 0-8 | identical | 0.75 | ✓ | ✓ |
| person #17 - on - grass #0 | 0-4, 7-8 | on | 0-8 | identical | 0.62 | ✓ | ✓ |
| person #18 - on - grass #0 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #18 - in front of - forest #19 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| wheel #20 - attached to - car #10 | 0-2, 5-6 | below | 0-8 | not judged yet | 0.38 | ✗ | ✗ |
| wheel #20 - under - car #10 | 0-2, 5-6 | below | 0-8 | not judged yet | 0.38 | ✗ | ✗ |
| headlight #21 - attached to - car #10 | 0-4, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| headlight #21 - in front of - windshield #23 | 0-4, 7-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| headlight #22 - attached to - car #10 | 0-2, 4-5, 6-8 | below | 0-8 | not judged yet | 0.62 | ? | ✗ |
| headlight #22 - in front of - windshield #23 | 0-2, 4-5, 7-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| windshield #23 - attached to - car #10 | 0-5, 7-8 | above | 0-8 | not judged yet | 0.75 | ? | ? |

TRASER relations between pairs the humans did not annotate (65): person #18 - approaches - tree #7 [0-8]; person #18 - moves away from - car #10 [0-8]; person #18 - approaches - person #14 [0-8]; person #18 - approaches - person #15 [0-8]; person #18 - approaches - person #16 [0-8]; person #18 - approaches - person #17 [0-8]; person #18 - approaches - tree #9 [0-8]; person #18 - approaches - headlight #21 [0-8]; person #18 - approaches - windshield #23 [0-8]; person #18 - approaches - wheel #20 [0-8]


## 700_zkhPzSZcRtQ

22.67 s, 23 frames read | human: 24 objects, 41 relations | TRASER: 24 objects, 116 relations, valid JSON, 3604 tokens

**Objects: 10/24 right**

| id | human label | TRASER label | verdict | right |
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

**Relations: 8/41 right, triplets: 6/41 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| mat #0 - in front of - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| mat #0 - on - floor #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| mat #1 - on - floor #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| mat #1 - behind - mat #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| pole #3 - on - floor #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| pole #3 - in front of - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #4 - in front of - wall #6 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ? |
| man #4 - in front of - ball cart #7 | 0-23 | in front of (+1 more) | 0-24 | identical | 0.96 | ✓ | ✓ |
| man #4 - approaching - mat #0 | 18-21 | moving relative to (+1 more) | 0-24 | not judged yet | 0.12 | ✗ | ✗ |
| man #4 - moving away from - mat #0 | 20-23 | moving relative to (+1 more) | 0-24 | not judged yet | 0.12 | ✗ | ✗ |
| man #4 - on - floor #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #4 - walking on - floor #2 | 18-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #4 - holding - bat #5 | 0-23 | holding | 0-24 | identical | 0.96 | ✓ | ? |
| man #4 - wearing - hat #19 | 0-23 | wearing (+1 more) | 0-24 | identical | 0.96 | ✓ | ✓ |
| man #4 - wearing - hoodie #20 | 0-23 | wearing (+1 more) | 0-24 | identical | 0.96 | ✓ | ✓ |
| man #4 - wearing - pants #21 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #4 - wearing - shoe #17 | 0-23 | wearing | 0-24 | identical | 0.96 | ✓ | ✓ |
| man #4 - wearing - shoe #18 | 0-23 | wearing | 0-24 | identical | 0.96 | ✓ | ✓ |
| bat #5 - in front of - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| bat #5 - above - floor #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| ball cart #7 - on - floor #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| ball cart #7 - in front of - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| stripe or mat #8 - on - floor #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| stripe #9 - on - floor #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| stripe #10 - on - floor #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| wall poster #11 - on - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| wall poster #12 - on - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| wall poster #13 - on - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| wall poster #14 - on - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| posters #16 - on - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| shoe #17 - on - floor #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| shoe #18 - on - floor #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| hat #19 - above - hoodie #20 | 0-23 | above | 0-24 | identical | 0.96 | ✓ | ✓ |
| hat #19 - on - man #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| hoodie #20 - above - pants #21 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| hoodie #20 - on - man #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| pants #21 - above - shoe #17 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| pants #21 - above - shoe #18 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| pants #21 - on - man #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| poster #23 - on - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| poster #23 - above - ball cart #7 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (103): man #4 - moving relative to - ball cart #22 [0-24]; man #4 - in front of - ball cart #22 [0-24]; man #4 - moving relative to - strip #15 [0-24]; man #4 - in front of - strip #15 [0-24]; man #4 - moving relative to - posters #16 [0-24]; man #4 - in front of - posters #16 [0-24]; man #4 - moving relative to - poster #23 [0-24]; man #4 - in front of - poster #23 [0-24]; man #4 - moving relative to - pole #3 [0-24]; man #4 - in front of - pole #3 [0-24]


## 714_nooF6zlfzMI

22.67 s, 23 frames read | human: 13 objects, 26 relations | TRASER: 13 objects, 34 relations, valid JSON, 1319 tokens

**Objects: 5/13 right**

| id | human label | TRASER label | verdict | right |
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

**Relations: 4/26 right, triplets: 0/26 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| sky #1 - above - fish #0 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #1 - above - human #2 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #1 - above - Fishing Rod #3 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #1 - above - shore or ground #4 | 0-23.6667 | above | 0-23 | identical | 0.97 | ✓ | ? |
| sky #1 - above - embankment #5 | 0-23.6667 | above | 0-23 | identical | 0.97 | ✓ | ? |
| sky #1 - above - river or canal #6 | 0-23.6667 | above | 0-23 | identical | 0.97 | ✓ | ? |
| sky #1 - above - shore #7 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #1 - above - hand #11 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #1 - above - hand #12 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #1 - above - rod #10 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #1 - above - reel #9 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #1 - above - handle (grip) #8 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| reel #9 - attached to - Fishing Rod #3 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| rod #10 - attached to - Fishing Rod #3 | 0-23.6667 | attached to | 0-23 | identical | 0.97 | ✓ | ? |
| hand #12 - holding - handle (grip) #8 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #11 - operating - reel #9 | 0-5.16667 | nothing for this pair | - | - | - | ✗ | ✗ |
| human #2 - beside - river or canal #6 | 0-23.6667 | in front of | 0-23 | mismatch | 0.97 | ✗ | ✗ |
| human #2 - fishing in - river or canal #6 | 0-23.6667 | in front of | 0-23 | not judged yet | 0.97 | ? | ? |
| shore or ground #4 - beside - river or canal #6 | 0-23.6667 | adjacent to | 0-23 | not judged yet | 0.97 | ? | ? |
| embankment #5 - beside - river or canal #6 | 0-23.6667 | adjacent to | 0-23 | not judged yet | 0.97 | ? | ? |
| human #2 - standing on - embankment #5 | 0-23.6667 | in front of | 0-23 | not judged yet | 0.97 | ? | ? |
| human #2 - walking along - embankment #5 | 0-23.6667 | in front of | 0-23 | not judged yet | 0.97 | ? | ? |
| human #2 - has - hand #11 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| fish #0 - caught by - human #2 | 1.66667-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| fish #0 - attached to - Fishing Rod #3 | 1.66667-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| fish #0 - above - river or canal #6 | 1.66667-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (26): human #2 - holding - rod #10 [0-23]; human #2 - fishing with - rod #10 [0-23]; hand #12 - holding - rod #10 [0-23]; hand #12 - fishing with - rod #10 [0-23]; human #2 - holding - Fishing Rod #3 [0-23]; hand #12 - holding - Fishing Rod #3 [0-23]; rod #10 - attached to - handle (grip) #8 [0-23]; rod #10 - moving relative to - river or canal #6 [0-23]; rod #10 - in front of - river or canal #6 [0-23]; Fishing Rod #3 - moving relative to - river or canal #6 [0-23]


## 722__ajUvCkhVcI

22.67 s, 23 frames read | human: 18 objects, 39 relations | TRASER: 18 objects, 38 relations, valid JSON, 1581 tokens

**Objects: 5/18 right**

| id | human label | TRASER label | verdict | right |
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

**Relations: 4/39 right, triplets: 0/39 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| baby #0 - inside - ball pit #3 | 0-23 | in | 0-24 | not judged yet | 0.96 | ? | ? |
| baby #0 - playing with - ball pit #3 | 0-23 | in | 0-24 | not judged yet | 0.96 | ? | ? |
| baby #0 - in front of - side of a cage #5 | 0-23 | in front of (+1 more) | 0-24 | identical | 0.96 | ✓ | ? |
| baby #0 - wearing - shirt #8 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| baby #0 - wearing - short #10 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| baby #0 - looking at - baby #1 | 8-11 | next to | 0-24 | mismatch | 0.12 | ✗ | ✗ |
| baby #0 - in front of - baby #1 | 0-23 | next to | 0-24 | not judged yet | 0.96 | ? | ? |
| baby #0 - looking at - baby #2 | 13-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| baby #0 - in front of - side of a cage #4 | 0-23 | in front of (+1 more) | 0-24 | identical | 0.96 | ✓ | ? |
| baby #1 - inside - ball pit #3 | 0-23 | in | 0-24 | not judged yet | 0.96 | ? | ? |
| baby #1 - wearing - shirt #11 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| baby #1 - wearing - trouser #14 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| baby #1 - holding - side of a cage #5 | 8-23 | below (+1 more) | 0-24 | not judged yet | 0.62 | ? | ? |
| baby #1 - approaching - side of a cage #5 | 1-9 | in front of (+1 more) | 0-24 | not judged yet | 0.33 | ✗ | ✗ |
| baby #1 - climbing - side of a cage #5 | 8.5-23 | in front of (+1 more) | 0-24 | not judged yet | 0.60 | ? | ? |
| baby #1 - looking at - side of a cage #5 | 8-23 | below (+1 more) | 0-24 | not judged yet | 0.62 | ? | ? |
| baby #1 - in front of - side of a cage #5 | 0-23 | in front of (+1 more) | 0-24 | identical | 0.96 | ✓ | ? |
| baby #1 - in front of - side of a cage #4 | 0-23 | in front of (+1 more) | 0-24 | identical | 0.96 | ✓ | ? |
| baby #2 - inside - ball pit #3 | 10-19 | behind | 11-24 | not judged yet | 0.57 | ? | ? |
| baby #2 - playing with - ball pit #3 | 12-20 | behind | 11-24 | not judged yet | 0.62 | ? | ? |
| baby #2 - wearing - top #12 | 12-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| baby #2 - wearing - skirt #13 | 12-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| baby #2 - approaching - side of a cage #4 | 12-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| rope #6 - in front of - ball pit #3 | 0-9 | nothing for this pair | - | - | - | ✗ | ✗ |
| rope #6 - in front of - baby #0 | 0-9 | nothing for this pair | - | - | - | ✗ | ✗ |
| rope #7 - in front of - ball pit #3 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| rope #7 - in front of - baby #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| rope #7 - in front of - baby #1 | 0-11.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #8 - on - baby #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #9 - above - shirt #8 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #9 - above - short #10 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| short #10 - on - baby #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| short #10 - below - shirt #8 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #11 - on - baby #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #11 - above - trouser #14 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| top #12 - on - baby #2 | 13-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| skirt #13 - on - baby #2 | 12-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| skirt #13 - below - top #12 | 12.5-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| trouser #14 - on - baby #1 | 0-23 | behind | 0-24 | mismatch | 0.96 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (25): head #9 - in - ball pit #3 [0-24]; head #9 - in front of - side of a cage #4 [0-24]; head #9 - below - side of a cage #4 [0-24]; head #9 - in front of - side of a cage #5 [0-24]; head #9 - below - side of a cage #5 [0-24]; baby #0 - next to - head #9 [0-24]; baby #1 - next to - head #9 [0-24]; legs #17 - in - ball pit #3 [15-24]; legs #17 - in front of - side of a cage #4 [15-24]; legs #17 - below - side of a cage #4 [15-24]


## 742_ctcOIuSzy-s

6.17 s, 6 frames read | human: 16 objects, 25 relations | TRASER: 16 objects, 39 relations, valid JSON, 1568 tokens

**Objects: 8/16 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | trees | tree | not judged yet | ? |
| 1 | sky | cloud | semantic overlap | ✓ |
| 2 | grass | log | mismatch | ✗ |
| 3 | ground | rock | semantic overlap | ✓ |
| 4 | tree | log | not judged yet | ? |
| 5 | grass | grass | identical | ✓ |
| 6 | man | person | hypernym/hyponym | ✓ |
| 7 | trees | leaf | not judged yet | ? |
| 8 | trees | branch | not judged yet | ? |
| 9 | trees | plant | not judged yet | ? |
| 10 | hat | hat | identical | ✓ |
| 11 | gun | camera | mismatch | ✗ |
| 12 | glasses | sunglasses | hypernym/hyponym | ✓ |
| 13 | hand | glove | semantic overlap | ✓ |
| 14 | gloves | glove | identical | ✓ |
| 15 | whistle | flashlight | not judged yet | ? |

**Relations: 10/25 right, triplets: 5/25 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| sky #1 - above - trees #0 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #2 - on - ground #3 | 0-7 | on | 0-7 | identical | 1.00 | ✓ | ✗ |
| grass #2 - in front of - trees #0 | 0-7 | in front of | 0-7 | identical | 1.00 | ✓ | ✗ |
| tree #4 - on - ground #3 | 0-7 | on | 0-7 | identical | 1.00 | ✓ | ? |
| tree #4 - in front of - trees #0 | 0-7 | in front of | 0-7 | identical | 1.00 | ✓ | ? |
| grass #5 - on - ground #3 | 0-5, 6-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #6 - wears - hat #10 | 0-7 | wearing | 0-7 | not judged yet | 1.00 | ? | ? |
| man #6 - wears - glasses #12 | 0-7 | wearing | 0-7 | not judged yet | 1.00 | ? | ? |
| man #6 - wears - gloves #14 | 0-7 | wearing | 0-7 | not judged yet | 1.00 | ? | ? |
| man #6 - holds - gun #11 | 0-7 | holding (+1 more) | 0-7 | not judged yet | 1.00 | ? | ✗ |
| man #6 - smokes - whistle #15 | 0-7 | holding (+1 more) | 0-7 | not judged yet | 1.00 | ? | ? |
| man #6 - on - ground #3 | 0-7 | on | 0-7 | identical | 1.00 | ✓ | ✓ |
| man #6 - in front of - tree #4 | 0-7 | in front of (+1 more) | 0-7 | identical | 1.00 | ✓ | ? |
| man #6 - near - tree #4 | 0-7 | filming (+1 more) | 0-7 | not judged yet | 1.00 | ? | ? |
| trees #9 - behind - trees #0 | 0-5, 6-7 | in front of | 0-6 | not judged yet | 0.71 | ? | ? |
| hat #10 - on - man #6 | 0-7 | on | 0-7 | identical | 1.00 | ✓ | ✓ |
| hat #10 - above - glasses #12 | 0-7 | above | 0-7 | identical | 1.00 | ✓ | ✓ |
| hat #10 - above - hand #13 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| gun #11 - near - hand #13 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| glasses #12 - on - man #6 | 0-7 | on | 0-7 | identical | 1.00 | ✓ | ✓ |
| hand #13 - attached to - man #6 | 0-7 | on | 0-7 | not judged yet | 1.00 | ? | ? |
| gloves #14 - on - man #6 | 0-7 | on | 0-7 | identical | 1.00 | ✓ | ✓ |
| gloves #14 - on - hand #13 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| whistle #15 - below - hat #10 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| whistle #15 - near - glasses #12 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (19): man #6 - wearing - hand #13 [0-7]; gun #11 - on - ground #3 [0-7]; whistle #15 - on - ground #3 [0-7]; gun #11 - in front of - man #6 [0-7]; whistle #15 - in front of - man #6 [0-7]; gun #11 - in front of - tree #4 [0-7]; whistle #15 - in front of - tree #4 [0-7]; trees #0 - in front of - sky #1 [0-7]; man #6 - in front of - trees #0 [0-7]; gun #11 - near - whistle #15 [0-7]


## 744_1X6KvqPjk6I

7.5 s, 8 frames read | human: 32 objects, 26 relations | TRASER: 32 objects, 38 relations, valid JSON, 2394 tokens

**Objects: 15/32 right**

| id | human label | TRASER label | verdict | right |
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

**Relations: 4/26 right, triplets: 3/26 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| dog #0 - looking at - grass #4 | 0-8 | on | 0-9 | not judged yet | 0.89 | ? | ? |
| dog #0 - behind - barricade #17 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #0 - in front of - wall #27 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #4 - in front of - barricade #17 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants, soil #5 - in front of - person #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants, soil #5 - in front of - barricade #17 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #7 - wearing - hat #9 | 0-8 | wearing | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #7 - wearing - trouser #31 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #7 - pulling - plants, soil #5 | 0-8 | digging (+2 more) | 0-9 | not judged yet | 0.89 | ? | ? |
| person #7 - looking at - plants, soil #5 | 0-8 | looking at (+2 more) | 0-9 | identical | 0.89 | ✓ | ? |
| person #7 - weeding - plants, soil #5 | 0-8 | digging (+2 more) | 0-9 | not judged yet | 0.89 | ? | ? |
| person #7 - holding - plants, soil #5 | 0-8 | digging (+2 more) | 0-9 | not judged yet | 0.89 | ? | ? |
| person #7 - behind - barricade #17 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #7 - in front of - wall #27 | 0-8 | holding | 0-9 | not judged yet | 0.89 | ? | ? |
| hat #9 - on - person #7 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✓ |
| hair #10 - on - person #7 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✓ |
| hair #10 - below - hat #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| tail #11 - part of - dog #0 | 0-8 | attached to | 0-9 | not judged yet | 0.89 | ? | ? |
| dog leg #12 - part of - dog #0 | 0-8 | attached to | 0-9 | not judged yet | 0.89 | ? | ? |
| dog leg #13 - part of - dog #0 | 0-8 | attached to | 0-9 | not judged yet | 0.89 | ? | ? |
| dog leg #14 - part of - dog #0 | 0-8 | attached to | 0-9 | not judged yet | 0.89 | ? | ? |
| head #15 - part of - dog #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| barricade #16 - in front of - person #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| stone #18 - on - barricade #16 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| gardening glove #19 - on - barricade #17 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| trouser #31 - on - person #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (26): dog #0 - has - tail #11 [0-9]; dog #0 - has - dog leg #12 [0-9]; dog #0 - has - dog leg #13 [0-9]; dog #0 - has - dog leg #14 [0-9]; head #15 - on - grass #4 [0-9]; dog #0 - in front of - fence #3 [0-9]; head #15 - in front of - fence #3 [0-9]; person #7 - in front of - fence #3 [0-9]; plant #2 - in front of - fence #3 [0-9]; plant #6 - in front of - fence #3 [0-9]


## 754_TYUV8DYWe8k

22.67 s, 23 frames read | human: 28 objects, 26 relations | TRASER: 28 objects, 47 relations, valid JSON, 2196 tokens

**Objects: 9/28 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | building | truck | mismatch | ✗ |
| 1 | tree | tree | identical | ✓ |
| 2 | tree | tree | identical | ✓ |
| 3 | tree | tree | identical | ✓ |
| 4 | building | barn | hypernym/hyponym | ✓ |
| 5 | tree | tree | identical | ✓ |
| 6 | grass | grass | identical | ✓ |
| 7 | sky | clouds | not judged yet | ? |
| 8 | dirt | soil | synonym | ✓ |
| 9 | grass | hill | not judged yet | ? |
| 10 | hand | hand | identical | ✓ |
| 11 | bush | plant | hypernym/hyponym | ✓ |
| 12 | fence post | tree | mismatch | ✗ |
| 13 | stick | pole | not judged yet | ? |
| 14 | fence post | tree | mismatch | ✗ |
| 15 | stick | pole | not judged yet | ? |
| 16 | stick | pole | not judged yet | ? |
| 17 | stick | pole | not judged yet | ? |
| 18 | stick | pole | not judged yet | ? |
| 19 | stick | plant | not judged yet | ? |
| 20 | storage | truck | not judged yet | ? |
| 21 | storage | truck | not judged yet | ? |
| 22 | storage | truck | not judged yet | ? |
| 23 | stick | pole | not judged yet | ? |
| 24 | stick | pole | not judged yet | ? |
| 25 | side of house | tree | not judged yet | ? |
| 26 | side of house | tree | not judged yet | ? |
| 27 | roof | tree | not judged yet | ? |

**Relations: 1/26 right, triplets: 1/26 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| building #0 - behind - grass #6 | 0-23 | on | 0-23 | not judged yet | 1.00 | ? | ✗ |
| building #0 - beneath - sky #7 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #1 - beneath - sky #7 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #1 - behind - grass #6 | 0-23 | on | 0-23 | not judged yet | 1.00 | ? | ? |
| tree #2 - beneath - sky #7 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #2 - behind - grass #6 | 0-23 | on | 0-23 | not judged yet | 1.00 | ? | ? |
| tree #3 - beneath - sky #7 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #3 - behind - grass #6 | 0-23 | on | 0-23 | not judged yet | 1.00 | ? | ? |
| building #4 - behind - grass #6 | 0-23 | on | 0-23 | not judged yet | 1.00 | ? | ? |
| building #4 - beneath - sky #7 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #6 - in front of - sky #7 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #6 - above - dirt #8 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| dirt #8 - in front of - grass #6 | 0-23 | in front of | 0-23 | identical | 1.00 | ✓ | ✓ |
| hand #10 - above - dirt #8 | 0-1 | touching | 0-1 | not judged yet | 1.00 | ? | ? |
| storage #20 - attached to - building #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| storage #20 - near - building #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| storage #21 - attached to - building #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| storage #21 - near - building #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| storage #22 - attached to - building #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| storage #22 - near - building #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| side of house #25 - attached to - building #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| side of house #25 - on - building #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| side of house #26 - attached to - building #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| side of house #26 - on - building #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| roof #27 - mounted on - building #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| roof #27 - on - building #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (40): building #0 - moving left relative to - building #4 [0-23]; storage #20 - moving left relative to - building #4 [0-23]; storage #21 - moving left relative to - building #4 [0-23]; storage #22 - moving left relative to - building #4 [0-23]; building #0 - moving with - storage #20 [0-23]; building #0 - moving with - storage #21 [0-23]; building #0 - moving with - storage #22 [0-23]; storage #20 - on - grass #6 [0-23]; storage #21 - on - grass #6 [0-23]; storage #22 - on - grass #6 [0-23]


## 766_m1Vdl-EMY1E

22.67 s, 23 frames read | human: 20 objects, 32 relations | TRASER: 20 objects, 32 relations, valid JSON, 1545 tokens

**Objects: 14/20 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | field | baseball player | mismatch | ✗ |
| 1 | stadium | banner | not judged yet | ? |
| 2 | sky | streetlight | not judged yet | ? |
| 3 | light | streetlight | hypernym/hyponym | ✓ |
| 4 | person | person | identical | ✓ |
| 5 | person | baseball player | hypernym/hyponym | ✓ |
| 6 | person | person | identical | ✓ |
| 7 | person | person | identical | ✓ |
| 8 | person | person | identical | ✓ |
| 9 | person | person | identical | ✓ |
| 10 | person | person | identical | ✓ |
| 11 | person | person | identical | ✓ |
| 12 | person | baseball player | hypernym/hyponym | ✓ |
| 13 | baseball bat | baseball bat | identical | ✓ |
| 14 | hat | baseball cap | hypernym/hyponym | ✓ |
| 15 | pants | trousers (uncertain) | synonym | ✓ |
| 16 | sign | signboard | not judged yet | ? |
| 17 | foul line | baseball bat | not judged yet | ? |
| 18 | display | scoreboard | hypernym/hyponym | ✓ |
| 19 | antenna | telephone pole (uncertain) | not judged yet | ? |

**Relations: 9/32 right, triplets: 3/32 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| field #0 - below - sky #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| stadium #1 - behind - field #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| stadium #1 - below - sky #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #2 - above - stadium #1 | 0-23 | above | 0-24 | identical | 0.96 | ✓ | ? |
| sky #2 - above - field #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #3 - above - stadium #1 | 0-9 | above | 0-24 | identical | 0.38 | ✗ | ✗ |
| light #3 - above - field #0 | 0-9 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - wear - hat #14 | 0-23 | wearing | 0-24 | not judged yet | 0.96 | ? | ? |
| person #4 - wear - pants #15 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - on - field #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - move away from - person #12 | 19-23 | in front of | 0-24 | not judged yet | 0.17 | ✗ | ✗ |
| person #4 - in front of - person #12 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #4 - in front of - stadium #1 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ? |
| person #5 - wield - baseball bat #13 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - drop - baseball bat #13 | 19-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - move away from - person #12 | 19-23 | in front of | 0-24 | not judged yet | 0.17 | ✗ | ✗ |
| person #5 - in front of - person #12 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #5 - bat against - person #7 | 15-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - on - field #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - in front of - stadium #1 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ? |
| person #7 - pitch to - person #5 | 15-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #7 - move toward - person #5 | 15-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #12 - on - field #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #12 - in front of - stadium #1 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ? |
| baseball bat #13 - move away from - person #5 | 19-23 | in front of | 0-24 | not judged yet | 0.17 | ✗ | ✗ |
| baseball bat #13 - near - person #5 | 0-22 | in front of | 0-24 | not judged yet | 0.92 | ? | ? |
| hat #14 - on - person #4 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ✓ |
| pants #15 - on - person #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign #16 - on - stadium #1 | 0-23 | above | 0-24 | semantic overlap | 0.96 | ✓ | ? |
| foul line #17 - on - field #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| display #18 - on - stadium #1 | 0-23 | above | 0-24 | semantic overlap | 0.96 | ✓ | ? |
| antenna #19 - above - stadium #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (20): person #4 - holding - baseball bat #13 [0-24]; person #4 - looking at - person #5 [0-24]; person #4 - approaching - person #5 [0-11]; person #4 - moving away from - person #5 [11-24]; person #4 - coordinating with - person #5 [0-24]; person #4 - in front of - person #5 [0-24]; person #5 - looking at - person #4 [0-24]; baseball bat #13 - near - person #4 [0-24]; baseball bat #13 - in front of - stadium #1 [0-24]; foul line #17 - in front of - stadium #1 [0-24]


## 839_SS_1452uWvg

22.67 s, 23 frames read | human: 73 objects, 36 relations | TRASER: 40 objects, 96 relations, valid JSON, 3814 tokens

**Objects: 9/73 right**

| id | human label | TRASER label | verdict | right |
|---|---|---|---|---|
| 0 | building | clock tower | not judged yet | ? |
| 1 | building | building | identical | ✓ |
| 2 | building | building | identical | ✓ |
| 3 | sky | clock tower | not judged yet | ? |
| 4 | building | arch | not judged yet | ? |
| 5 | pillar | column | not judged yet | ? |
| 6 | pillar | column | not judged yet | ? |
| 7 | arches | vent | not judged yet | ? |
| 8 | arches | vent | not judged yet | ? |
| 9 | window | window | identical | ✓ |
| 10 | window | window | identical | ✓ |
| 11 | window | window | identical | ✓ |
| 12 | window | window | identical | ✓ |
| 13 | pillar | window | not judged yet | ? |
| 14 | pillar | window | not judged yet | ? |
| 15 | pillar | window | not judged yet | ? |
| 16 | pillar | window | not judged yet | ? |
| 17 | pillar | window | not judged yet | ? |
| 18 | pillar | window | not judged yet | ? |
| 19 | pillar | column | not judged yet | ? |
| 20 | pillar | column | not judged yet | ? |
| 21 | pillar | column | not judged yet | ? |
| 22 | pillar | column | not judged yet | ? |
| 23 | pillar | window | not judged yet | ? |
| 24 | pillar | window | not judged yet | ? |
| 25 | pillar | window | not judged yet | ? |
| 26 | pillar | window | not judged yet | ? |
| 27 | pillar | window | not judged yet | ? |
| 28 | pillar | window | not judged yet | ? |
| 29 | pillar | window | not judged yet | ? |
| 30 | pillar | window | not judged yet | ? |
| 31 | statue | statue | identical | ✓ |
| 32 | statue | statue | identical | ✓ |
| 33 | window | window | identical | ✓ |
| 34 | pillar | window | not judged yet | ? |
| 35 | pillar | window | not judged yet | ? |
| 36 | pillar | window | not judged yet | ? |
| 37 | pillar | window | not judged yet | ? |
| 38 | pillar | window | not judged yet | ? |
| 39 | pillar | window | not judged yet | ? |
| 40 | pillar | - | no label from TRASER | ✗ |
| 41 | pillar | - | no label from TRASER | ✗ |
| 42 | window | - | no label from TRASER | ✗ |
| 43 | antenna | - | no label from TRASER | ✗ |
| 44 | window | - | no label from TRASER | ✗ |
| 45 | flower | - | no label from TRASER | ✗ |
| 46 | wall | - | no label from TRASER | ✗ |
| 47 | roof | - | no label from TRASER | ✗ |
| 48 | building | - | no label from TRASER | ✗ |
| 49 | door | - | no label from TRASER | ✗ |
| 50 | window | - | no label from TRASER | ✗ |
| 51 | door | - | no label from TRASER | ✗ |
| 52 | pillar | - | no label from TRASER | ✗ |
| 53 | pillar | - | no label from TRASER | ✗ |
| 54 | pillar | - | no label from TRASER | ✗ |
| 55 | pillar | - | no label from TRASER | ✗ |
| 56 | pillar | - | no label from TRASER | ✗ |
| 57 | pillar | - | no label from TRASER | ✗ |
| 58 | pillar | - | no label from TRASER | ✗ |
| 59 | doorway | - | no label from TRASER | ✗ |
| 60 | window | - | no label from TRASER | ✗ |
| 61 | pillar | - | no label from TRASER | ✗ |
| 62 | pillar | - | no label from TRASER | ✗ |
| 63 | pillar | - | no label from TRASER | ✗ |
| 64 | pillar | - | no label from TRASER | ✗ |
| 65 | window | - | no label from TRASER | ✗ |
| 66 | arch | - | no label from TRASER | ✗ |
| 67 | arch | - | no label from TRASER | ✗ |
| 68 | frame | - | no label from TRASER | ✗ |
| 69 | roof | - | no label from TRASER | ✗ |
| 70 | arch | - | no label from TRASER | ✗ |
| 71 | arch | - | no label from TRASER | ✗ |
| 72 | door | - | no label from TRASER | ✗ |

**Relations: 11/36 right, triplets: 3/36 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| building #0 - in front of - sky #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| building #1 - in front of - sky #3 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| building #2 - in front of - sky #3 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| pillar #5 - attached to - building #0 | 0-23 | attached to (+1 more) | 0-24 | identical | 0.96 | ✓ | ? |
| pillar #5 - attached to - building #0 | 0-23 | attached to (+1 more) | 0-24 | identical | 0.96 | ✓ | ? |
| pillar #6 - attached to - building #0 | 0-23 | attached to (+1 more) | 0-24 | identical | 0.96 | ✓ | ? |
| pillar #6 - attached to - building #0 | 0-23 | attached to (+1 more) | 0-24 | identical | 0.96 | ✓ | ? |
| arches #7 - on - building #0 | 11-23 | on (+1 more) | 12-24 | identical | 0.85 | ✓ | ? |
| arches #7 - attached to - building #0 | 11-23 | built into (+1 more) | 12-24 | not judged yet | 0.85 | ? | ? |
| arches #8 - on - building #0 | 13-23 | on (+1 more) | 12-24 | identical | 0.83 | ✓ | ? |
| arches #8 - attached to - building #0 | 13-23 | built into (+1 more) | 12-24 | not judged yet | 0.83 | ? | ? |
| window #10 - in - building #0 | 0-23 | built into (+1 more) | 0-24 | not judged yet | 0.96 | ? | ? |
| window #10 - attached to - building #0 | 0-23 | built into (+1 more) | 0-24 | not judged yet | 0.96 | ? | ? |
| window #10 - above - window #33 | 0-10 | above | 0-12 | identical | 0.83 | ✓ | ✓ |
| window #11 - in - building #0 | 0-23 | built into (+1 more) | 0-24 | not judged yet | 0.96 | ? | ? |
| window #11 - attached to - building #0 | 0-23 | built into (+1 more) | 0-24 | not judged yet | 0.96 | ? | ? |
| pillar #21 - attached to - building #0 | 0-11 | attached to (+1 more) | 0-12 | identical | 0.92 | ✓ | ? |
| pillar #22 - attached to - building #0 | 0-11 | attached to (+1 more) | 0-12 | identical | 0.92 | ✓ | ? |
| statue #31 - attached to - building #0 | 0-15 | mounted on (+1 more) | 0-17 | not judged yet | 0.88 | ? | ? |
| statue #31 - attached to - building #0 | 0-15 | mounted on (+1 more) | 0-17 | not judged yet | 0.88 | ? | ? |
| statue #31 - above - window #33 | 0-10 | above | 0-12 | identical | 0.83 | ✓ | ✓ |
| statue #32 - attached to - building #0 | 0-15 | mounted on (+1 more) | 0-17 | not judged yet | 0.88 | ? | ? |
| statue #32 - attached to - building #0 | 0-15 | mounted on (+1 more) | 0-17 | not judged yet | 0.88 | ? | ? |
| statue #32 - above - window #33 | 0-10 | above | 0-12 | identical | 0.83 | ✓ | ✓ |
| window #33 - in - building #0 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #33 - attached to - building #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #42 - in - building #1 | 0-9 | nothing for this pair | - | - | - | ✗ | ✗ |
| antenna #43 - on - roof #47 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #44 - in - building #1 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| flower #45 - on - wall #46 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| roof #47 - on - building #1 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| roof #69 - on - building #2 | 0-4 | nothing for this pair | - | - | - | ✗ | ✗ |
| arch #70 - on - building #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| arch #70 - above - door #72 | 0-10.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| arch #71 - on - building #2 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #72 - in - building #2 | 0-2 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (73): pillar #19 - attached to - building #0 [0-12]; pillar #19 - in front of - building #0 [0-12]; pillar #20 - attached to - building #0 [0-12]; pillar #20 - in front of - building #0 [0-12]; window #9 - built into - building #0 [0-24]; window #9 - on - building #0 [0-24]; window #12 - built into - building #0 [0-24]; window #12 - on - building #0 [0-24]; pillar #13 - built into - building #0 [0-24]; pillar #13 - on - building #0 [0-24]

