# svg2test: human labels vs TRASER, video by video

100 videos with a prediction. Lenient criterion, temporal IoU > 0.5. ✓ right, ✗ wrong, ? = the judge (Kimi K3) has not compared these two labels yet (identical text counts as right without the judge). Relation = same two objects, predicate not a mismatch, tIoU > 0.5; triplet = relation right and both object labels right. Made by `tools/bench_eval.py write_compare`.

**So far: objects 1930/3305, relations 864/3187, triplets 676/3187** (unjudged pairs count as not right; scores in README.md)

| video | objects right | relations right | triplets right | not judged yet (?) |
|---|---|---|---|---|
| [1016_8J41CsGYhNI](#1016_8j41csgyhni) | 9/15 | 9/24 | 9/24 | 0 |
| [1047_-_XOsbwGZgg](#1047_-_xosbwgzgg) | 31/53 | 20/56 | 17/56 | 0 |
| [1086_iywqpda7d8k](#1086_iywqpda7d8k) | 9/9 | 6/19 | 6/19 | 0 |
| [1125_Cbv34yDZ8gc](#1125_cbv34ydz8gc) | 19/46 | 8/25 | 0/25 | 0 |
| [1187_AqH9dWCvTkY](#1187_aqh9dwcvtky) | 25/36 | 2/4 | 2/4 | 0 |
| [1190_UmpN6eLjN8w](#1190_umpn6eljn8w) | 7/18 | 7/44 | 7/44 | 0 |
| [1251__MCY-QkVaZw](#1251__mcy-qkvazw) | 9/12 | 5/11 | 2/11 | 0 |
| [1253_TPxVj7do42I](#1253_tpxvj7do42i) | 13/21 | 6/35 | 6/35 | 0 |
| [1256_Y_19xu4yTms](#1256_y_19xu4ytms) | 24/32 | 22/61 | 20/61 | 0 |
| [1261_wsHfWwHXgLs](#1261_wshfwwhxgls) | 7/8 | 5/22 | 5/22 | 0 |
| [1268_h58xqlUE5xA](#1268_h58xqlue5xa) | 6/11 | 7/21 | 3/21 | 0 |
| [1275_ARcg-EyKWrA](#1275_arcg-eykwra) | 17/68 | 6/21 | 6/21 | 0 |
| [1308_-C_XboJfD0g](#1308_-c_xbojfd0g) | 7/14 | 1/15 | 0/15 | 0 |
| [1352_nt-UZxGk9Bg](#1352_nt-uzxgk9bg) | 11/14 | 13/35 | 13/35 | 0 |
| [1480_WAGXu9_6Uv0](#1480_wagxu9_6uv0) | 20/46 | 3/41 | 2/41 | 0 |
| [1503_gwrvCEAZVl0](#1503_gwrvceazvl0) | 16/20 | 5/34 | 5/34 | 0 |
| [1638_MhoaeR88gm4](#1638_mhoaer88gm4) | 16/63 | 0/10 | 0/10 | 0 |
| [1691_md-DpQ4HX7Q](#1691_md-dpq4hx7q) | 10/21 | 25/39 | 14/39 | 0 |
| [1717_lh_2_1duNgw](#1717_lh_2_1dungw) | 38/65 | 34/79 | 28/79 | 0 |
| [1757_0jsMPnghnck](#1757_0jsmpnghnck) | 18/23 | 22/28 | 17/28 | 0 |
| [179_mha1KKixPts](#179_mha1kkixpts) | 25/27 | 1/14 | 0/14 | 0 |
| [1903_cFq3flHndS0](#1903_cfq3flhnds0) | 16/20 | 5/21 | 5/21 | 0 |
| [1936_gvKlIkjfP0Q](#1936_gvklikjfp0q) | 24/56 | 0/40 | 0/40 | 0 |
| [2143_6OMR3X7IcZ0](#2143_6omr3x7icz0) | 13/16 | 2/28 | 2/28 | 0 |
| [2225_6acPX_00M9Q](#2225_6acpx_00m9q) | 16/19 | 11/38 | 6/38 | 0 |
| [226_n7YpGfnTqoY](#226_n7ypgfntqoy) | 15/20 | 31/51 | 24/51 | 0 |
| [241_oEkly9vzEGQ](#241_oekly9vzegq) | 19/26 | 11/31 | 11/31 | 0 |
| [246_QcRqBBAiC4o](#246_qcrqbbaic4o) | 27/56 | 6/36 | 6/36 | 0 |
| [254_-7d3nOFx1V8](#254_-7d3nofx1v8) | 26/30 | 9/25 | 8/25 | 0 |
| [276_3HgBHBOnpbg](#276_3hgbhbonpbg) | 7/40 | 0/55 | 0/55 | 0 |
| [279_qw5ySRNNfNM](#279_qw5ysrnnfnm) | 21/89 | 6/47 | 6/47 | 0 |
| [285_EP_blwEf2K8](#285_ep_blwef2k8) | 17/58 | 10/50 | 9/50 | 0 |
| [308_7WhzIsqPQW8](#308_7whzisqpqw8) | 28/42 | 9/41 | 7/41 | 0 |
| [339_j2gELsuQ3Cg](#339_j2gelsuq3cg) | 12/14 | 1/20 | 1/20 | 0 |
| [359_4ZPKJtcNGZE](#359_4zpkjtcngze) | 18/27 | 3/20 | 2/20 | 0 |
| [365_JFqiSr9A-Go](#365_jfqisr9a-go) | 23/48 | 3/53 | 3/53 | 0 |
| [419_CykhOKWEAjo](#419_cykhokweajo) | 28/43 | 8/32 | 8/32 | 0 |
| [434_eOTP9yrATX8](#434_eotp9yratx8) | 10/14 | 22/37 | 13/37 | 0 |
| [465_nbJ_SLWUDxk](#465_nbj_slwudxk) | 34/39 | 7/24 | 6/24 | 0 |
| [470_BiIqH60-A1M](#470_biiqh60-a1m) | 20/36 | 11/30 | 11/30 | 0 |
| [474_b-Qlvj48YQw](#474_b-qlvj48yqw) | 24/72 | 12/30 | 11/30 | 0 |
| [520_JbMXRRGOEkk](#520_jbmxrrgoekk) | 14/24 | 9/31 | 2/31 | 0 |
| [547_7E-Xian95Qk](#547_7e-xian95qk) | 18/22 | 14/28 | 13/28 | 0 |
| [551_VHxQVmG1pOA](#551_vhxqvmg1poa) | 35/47 | 17/53 | 15/53 | 0 |
| [562_OA61thiz9wU](#562_oa61thiz9wu) | 10/40 | 2/34 | 1/34 | 0 |
| [628_nQRJD435Fh4](#628_nqrjd435fh4) | 32/40 | 21/52 | 20/52 | 0 |
| [642_ljk5b80TmkE](#642_ljk5b80tmke) | 13/23 | 2/25 | 1/25 | 0 |
| [66_927BvkIZglw](#66_927bvkizglw) | 13/20 | 3/28 | 3/28 | 0 |
| [670_JboU-y2LdkU](#670_jbou-y2ldku) | 21/24 | 19/33 | 19/33 | 0 |
| [700_zkhPzSZcRtQ](#700_zkhpzszcrtq) | 13/24 | 8/41 | 6/41 | 0 |
| [714_nooF6zlfzMI](#714_noof6zlfzmi) | 10/13 | 6/26 | 4/26 | 0 |
| [722__ajUvCkhVcI](#722__ajuvckhvci) | 12/18 | 7/39 | 7/39 | 0 |
| [742_ctcOIuSzy-s](#742_ctcoiuszy-s) | 13/16 | 16/25 | 13/25 | 0 |
| [744_1X6KvqPjk6I](#744_1x6kvqpjk6i) | 20/32 | 9/26 | 9/26 | 0 |
| [752_RWBJGgqDpwk](#752_rwbjggqdpwk) | 25/60 | 6/25 | 1/25 | 0 |
| [754_TYUV8DYWe8k](#754_tyuv8dywe8k) | 19/28 | 1/26 | 1/26 | 0 |
| [761_liWqb_am68c](#761_liwqb_am68c) | 9/13 | 4/27 | 4/27 | 0 |
| [766_m1Vdl-EMY1E](#766_m1vdl-emy1e) | 15/20 | 11/32 | 5/32 | 0 |
| [778_3PmDn84laac](#778_3pmdn84laac) | 19/23 | 10/27 | 6/27 | 0 |
| [839_SS_1452uWvg](#839_ss_1452uwvg) | 17/73 | 21/36 | 17/36 | 0 |
| [856_coe8HkbRIk4](#856_coe8hkbrik4) | 18/25 | 16/33 | 13/33 | 0 |
| [888_BS3hab7EtAg](#888_bs3hab7etag) | 23/26 | 18/39 | 15/39 | 0 |
| [914_f4HgijyAEYs](#914_f4hgijyaeys) | 10/19 | 8/21 | 6/21 | 0 |
| [950_94nfEhq6S5w](#950_94nfehq6s5w) | 27/44 | 10/27 | 8/27 | 0 |
| [973_ceJ5D6wluX0](#973_cej5d6wlux0) | 5/7 | 5/18 | 5/18 | 0 |
| [976_U19VojbI0h4](#976_u19vojbi0h4) | 28/65 | 7/36 | 5/36 | 0 |
| [987_g0mln-jiQTw](#987_g0mln-jiqtw) | 7/11 | 5/17 | 3/17 | 0 |
| [sav_002789](#sav_002789) | 27/47 | 1/41 | 1/41 | 0 |
| [sav_004381](#sav_004381) | 26/37 | 3/11 | 3/11 | 0 |
| [sav_004550](#sav_004550) | 30/52 | 12/37 | 7/37 | 0 |
| [sav_009146](#sav_009146) | 21/32 | 1/36 | 1/36 | 0 |
| [sav_009307](#sav_009307) | 38/63 | 8/53 | 8/53 | 0 |
| [sav_009687](#sav_009687) | 31/52 | 9/18 | 9/18 | 0 |
| [sav_010164](#sav_010164) | 25/36 | 7/42 | 0/42 | 0 |
| [sav_010923](#sav_010923) | 25/36 | 13/34 | 9/34 | 0 |
| [sav_011754](#sav_011754) | 35/53 | 1/46 | 1/46 | 0 |
| [sav_015587](#sav_015587) | 25/41 | 5/28 | 2/28 | 0 |
| [sav_015763](#sav_015763) | 14/14 | 10/30 | 10/30 | 0 |
| [sav_016333](#sav_016333) | 28/39 | 0/5 | 0/5 | 0 |
| [sav_023013](#sav_023013) | 20/25 | 13/25 | 6/25 | 0 |
| [sav_023742](#sav_023742) | 15/24 | 4/5 | 4/5 | 0 |
| [sav_023860](#sav_023860) | 35/41 | 19/73 | 1/73 | 0 |
| [sav_025082](#sav_025082) | 29/48 | 0/9 | 0/9 | 0 |
| [sav_026800](#sav_026800) | 12/19 | 4/10 | 4/10 | 0 |
| [sav_028579](#sav_028579) | 32/50 | 4/30 | 4/30 | 0 |
| [sav_028748](#sav_028748) | 8/14 | 10/25 | 6/25 | 0 |
| [sav_030325](#sav_030325) | 12/16 | 20/36 | 18/36 | 0 |
| [sav_031935](#sav_031935) | 16/36 | 7/35 | 5/35 | 0 |
| [sav_032329](#sav_032329) | 26/52 | 8/45 | 3/45 | 0 |
| [sav_033373](#sav_033373) | 23/34 | 4/31 | 3/31 | 0 |
| [sav_036919](#sav_036919) | 9/15 | 1/31 | 1/31 | 0 |
| [sav_037370](#sav_037370) | 14/20 | 3/13 | 3/13 | 0 |
| [sav_037495](#sav_037495) | 21/38 | 11/34 | 10/34 | 0 |
| [sav_042890](#sav_042890) | 25/32 | 3/25 | 3/25 | 0 |
| [sav_043183](#sav_043183) | 6/16 | 11/33 | 10/33 | 0 |
| [sav_048782](#sav_048782) | 30/35 | 7/44 | 7/44 | 0 |
| [sav_052661](#sav_052661) | 26/51 | 8/45 | 8/45 | 0 |
| [sav_053005](#sav_053005) | 17/29 | 10/29 | 10/29 | 0 |
| [sav_054217](#sav_054217) | 18/22 | 8/23 | 8/23 | 0 |
| [sav_054440](#sav_054440) | 30/42 | 10/53 | 8/53 | 0 |

## 1016_8J41CsGYhNI

22.67 s, 23 frames read | human: 15 objects, 24 relations | TRASER: 15 objects, 24 relations, valid JSON, 1088 tokens

**Objects: 9/15 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | ball | yes (object 1) | sports ball (uncertain) | hypernym/hyponym | ✓ |
| 1 | tennis net | yes (object 2) | tennis net | identical | ✓ |
| 2 | curtain | yes (object 3) | curtain | identical | ✓ |
| 3 | tennis court surface | yes (object 4) | tennis ball | mismatch | ✗ |
| 4 | person | yes (object 5) | person | identical | ✓ |
| 5 | tennis racquet | yes (object 6) | tennis racket | identical | ✓ |
| 6 | headwear | yes (object 7) | headband (uncertain) | hypernym/hyponym | ✓ |
| 7 | shirt | yes (object 8) | jersey (uncertain) | hypernym/hyponym | ✓ |
| 8 | short | yes (object 9) | shorts | identical | ✓ |
| 9 | shoes | yes (object 10) | shoe | identical | ✓ |
| 10 | floor | yes (object 11) | tennis ball | mismatch | ✗ |
| 11 | floor | yes (object 12) | tennis ball | mismatch | ✗ |
| 12 | floor | yes (object 13) | tennis ball | mismatch | ✗ |
| 13 | floor | yes (object 14) | tennis ball | mismatch | ✗ |
| 14 | floor | yes (object 15) | tennis ball | mismatch | ✗ |

**Relations: 9/24 right, triplets: 9/24 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| ball #0 - approaches - tennis racquet #5 | 10-12 | nothing for this pair | - | - | - | ✗ | ✗ |
| ball #0 - above - tennis net #1 | 9-10.5, 20-21.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| ball #0 - approaches - tennis net #1 | 9-10, 20-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| ball #0 - above - tennis court surface #3 | 0-1, 9-12.5, 20-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| ball #0 - in front of - curtain #2 | 0-1, 9-12, 20-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tennis net #1 - on - tennis court surface #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tennis net #1 - in front of - curtain #2 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #4 - holding - tennis racquet #5 | 0-23 | holding | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #4 - wearing - headwear #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - wearing - shirt #7 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - wearing - short #8 | 0-23 | wearing | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #4 - hits - ball #0 | 11-12 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - looking at - ball #0 | 9-12, 20-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - approaches - tennis net #1 | 1-6 | moving along (+2 more) | 0-24 | mismatch | 0.21 | ✗ | ✗ |
| person #4 - behind - tennis net #1 | 0-23 | behind (+2 more) | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #4 - on - tennis court surface #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - in front of - curtain #2 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| tennis racquet #5 - above - tennis court surface #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tennis racquet #5 - near - person #4 | 0-23 | near (+1 more) | 0-24 | identical | 0.96 | ✓ | ✓ |
| tennis racquet #5 - in front of - curtain #2 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| headwear #6 - on - person #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #7 - on - person #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| short #8 - on - person #4 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ✓ |
| shoes #9 - on - person #4 | 0-18.5, 19.5-23 | on | 0-24 | identical | 0.92 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (12): person #4 - wearing - shoes #9 [0-24]; tennis racquet #5 - above - tennis net #1 [0-24]; short #8 - behind - tennis net #1 [0-24]; shoes #9 - behind - tennis net #1 [0-24]; shoes #9 - below - short #8 [0-24]; tennis racquet #5 - above - short #8 [0-24]; tennis racquet #5 - above - shoes #9 [0-24]; floor #10 - above - tennis net #1 [0-24]; floor #11 - above - tennis net #1 [0-24]; floor #12 - above - tennis net #1 [0-1, 23-24]


## 1047_-_XOsbwGZgg

7.5 s, 8 frames read | human: 53 objects, 56 relations | TRASER: 40 objects, 68 relations, valid JSON, 3264 tokens

**Objects: 31/53 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | person | yes (object 2) | person | identical | ✓ |
| 2 | person | yes (object 3) | person | identical | ✓ |
| 3 | person | yes (object 4) | person | identical | ✓ |
| 4 | person | yes (object 5) | suit jacket | mismatch | ✗ |
| 5 | thrash can | yes (object 6) | cardboard box | mismatch | ✗ |
| 6 | door | yes (object 7) | door | identical | ✓ |
| 7 | wall | yes (object 8) | wall | identical | ✓ |
| 8 | tree | yes (object 9) | plant | hypernym/hyponym | ✓ |
| 9 | rope | yes (object 10) | tape (uncertain) | semantic overlap | ✓ |
| 10 | mat | yes (object 11) | mat | identical | ✓ |
| 11 | bench | yes (object 12) | bench | identical | ✓ |
| 12 | floor | yes (object 13) | doormat | semantic overlap | ✓ |
| 13 | sign | yes (object 14) | signboard | synonym | ✓ |
| 14 | box | yes (object 15) | box | identical | ✓ |
| 15 | ground | yes (object 16) | doormat | semantic overlap | ✓ |
| 16 | bollard | yes (object 17) | tape (uncertain) | mismatch | ✗ |
| 17 | bench support | yes (object 18) | box | mismatch | ✗ |
| 18 | box | yes (object 19) | speaker (uncertain) | mismatch | ✗ |
| 19 | pot | yes (object 20) | box | mismatch | ✗ |
| 20 | ledge | yes (object 21) | vent (uncertain) | mismatch | ✗ |
| 21 | utility box | yes (object 22) | chair leg (uncertain) | mismatch | ✗ |
| 22 | bench support | yes (object 23) | box | mismatch | ✗ |
| 23 | electrical box | yes (object 24) | wall panel | semantic overlap | ✓ |
| 24 | shirt | yes (object 25) | shirt | identical | ✓ |
| 25 | watch | yes (object 26) | watch | identical | ✓ |
| 26 | trouser | yes (object 27) | trousers | identical | ✓ |
| 27 | shoe | yes (object 28) | shoe | identical | ✓ |
| 28 | shoe | yes (object 29) | shoe | identical | ✓ |
| 29 | hand | yes (object 30) | arm | semantic overlap | ✓ |
| 30 | hand | yes (object 31) | arm | semantic overlap | ✓ |
| 31 | face | yes (object 32) | person | hypernym/hyponym | ✓ |
| 32 | face | yes (object 33) | person | hypernym/hyponym | ✓ |
| 33 | shirt | yes (object 34) | shirt | identical | ✓ |
| 34 | hand | yes (object 35) | hand | identical | ✓ |
| 35 | hand | yes (object 36) | hand | identical | ✓ |
| 36 | trouser | yes (object 37) | trousers | identical | ✓ |
| 37 | shirt | yes (object 38) | suit jacket | semantic overlap | ✓ |
| 38 | face | yes (object 39) | person | hypernym/hyponym | ✓ |
| 39 | shirt | yes (object 40) | shirt | identical | ✓ |
| 40 | left forearm | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | right forearm | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | trouser | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | right shoe | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | left shoe | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | face | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | jacket | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | trouser | no: after the first 40 | - | no label from TRASER | ✗ |
| 48 | shoe | no: after the first 40 | - | no label from TRASER | ✗ |
| 49 | trouser | no: after the first 40 | - | no label from TRASER | ✗ |
| 50 | shoe | no: after the first 40 | - | no label from TRASER | ✗ |
| 51 | bin cover | no: after the first 40 | - | no label from TRASER | ✗ |
| 52 | bin bowl | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 20/56 right, triplets: 17/56 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - balancing on - rope #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - slacklining on - rope #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - above - rope #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - wearing - watch #25 | 0-8 | wearing | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #0 - wearing - shirt #24 | 0-8 | wearing | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #0 - wearing - trouser #26 | 0-8 | wearing | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #0 - in front of - wall #7 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #0 - above - mat #10 | 0-8 | on (+1 more) | 0-9 | semantic overlap | 0.89 | ✓ | ✓ |
| person #1 - looking at - person #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - behind - person #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - wearing - shirt #33 | 0-8 | wearing | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #1 - wearing - trouser #36 | 0-8 | wearing | 0-9 | identical | 0.89 | ✓ | ✓ |
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
| thrash can #5 - on - mat #10 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✗ |
| thrash can #5 - in front of - wall #7 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✗ |
| tree #8 - in front of - wall #7 | 0-8 | on | 0-9 | mismatch | 0.89 | ✗ | ✗ |
| rope #9 - tied to - bollard #16 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| rope #9 - above - floor #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| rope #9 - above - ground #15 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| rope #9 - above - mat #10 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| rope #9 - in front of - wall #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| mat #10 - on - ground #15 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| mat #10 - in front of - wall #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bench #11 - in front of - wall #7 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✓ |
| sign #13 - on - wall #7 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✓ |
| sign #13 - above - box #14 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| box #14 - on - wall #7 | 0-8 | in front of | 0-9 | mismatch | 0.89 | ✗ | ✗ |
| bench support #17 - in front of - wall #7 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✗ |
| bench support #17 - on - ground #15 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| box #18 - on - ground #15 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| pot #19 - on - floor #12 | 1-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| utility box #21 - on - electrical box #23 | 0-1, 7-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bench support #22 - above - floor #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| electrical box #23 - above - bench support #17 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| electrical box #23 - in front of - wall #7 | 0-8 | on | 0-9 | mismatch | 0.89 | ✗ | ✗ |
| bin cover #51 - covering - thrash can #5 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bin cover #51 - above - bin bowl #52 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bin bowl #52 - on - floor #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (42): person #0 - wearing - shoe #27 [0-9]; person #0 - wearing - shoe #28 [0-9]; person #2 - wearing - trouser #36 [0-9]; person #0 - dancing with - person #1 [0-9]; person #0 - in front of - person #1 [0-9]; person #0 - dancing with - person #2 [0-9]; person #0 - in front of - person #2 [0-9]; person #1 - dancing with - person #2 [0-9]; person #3 - on - mat #10 [0-9]; bench #11 - on - mat #10 [0-9]


## 1086_iywqpda7d8k

20.17 s, 20 frames read | human: 9 objects, 19 relations | TRASER: 9 objects, 22 relations, valid JSON, 878 tokens

**Objects: 9/9 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | trees | yes (object 1) | foliage | semantic overlap | ✓ |
| 1 | trees | yes (object 2) | forest | semantic overlap | ✓ |
| 2 | waterfall | yes (object 3) | waterfall | identical | ✓ |
| 3 | plants | yes (object 4) | bush | hypernym/hyponym | ✓ |
| 4 | trees | yes (object 5) | tree | identical | ✓ |
| 5 | trees | yes (object 6) | forest | semantic overlap | ✓ |
| 6 | sky | yes (object 7) | clouds | semantic overlap | ✓ |
| 7 | tree | yes (object 8) | leaves | semantic overlap | ✓ |
| 8 | cliffside | yes (object 9) | cliff | identical | ✓ |

**Relations: 6/19 right, triplets: 6/19 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| trees #0 - below - sky #6 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #0 - in front of - waterfall #2 | 0-21 | in front of (+1 more) | 0-20 | identical | 0.95 | ✓ | ✓ |
| trees #1 - below - sky #6 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| waterfall #2 - flows down past - trees #1 | 0-21 | flows past (+1 more) | 0-20 | hypernym/hyponym | 0.95 | ✓ | ✓ |
| waterfall #2 - in front of - trees #1 | 0-21 | in front of (+1 more) | 0-20 | identical | 0.95 | ✓ | ✓ |
| waterfall #2 - flows down past - cliffside #8 | 17-21 | flows past | 18-20 | hypernym/hyponym | 0.50 | ✗ | ✗ |
| waterfall #2 - in front of - cliffside #8 | 17-21 | flows past | 18-20 | mismatch | 0.50 | ✗ | ✗ |
| waterfall #2 - below - sky #6 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants #3 - below - sky #6 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants #3 - in front of - waterfall #2 | 0-21 | in front of (+1 more) | 0-20 | identical | 0.95 | ✓ | ✓ |
| plants #3 - in front of - trees #1 | 0-21 | in front of | 0-20 | identical | 0.95 | ✓ | ✓ |
| plants #3 - below - trees #1 | 0-21 | in front of | 0-20 | mismatch | 0.95 | ✗ | ✗ |
| plants #3 - in front of - cliffside #8 | 17-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #4 - below - sky #6 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #4 - above - waterfall #2 | 0-21 | behind | 0-20 | mismatch | 0.95 | ✗ | ✗ |
| trees #5 - below - sky #6 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #5 - above - waterfall #2 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #7 - in front of - waterfall #2 | 0-11 | in front of (+1 more) | 0-12 | identical | 0.92 | ✓ | ✓ |
| cliffside #8 - below - sky #6 | 17-21 | below | 18-20 | identical | 0.50 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (10): waterfall #2 - flows past - plants #3 [0-20]; waterfall #2 - flows past - trees #0 [0-20]; waterfall #2 - in front of - trees #5 [0-20]; trees #0 - in front of - trees #1 [0-20]; tree #7 - in front of - trees #1 [0-12]; sky #6 - above - waterfall #2 [0-20]; sky #6 - above - trees #1 [0-20]; sky #6 - above - trees #5 [0-20]; trees #4 - in front of - trees #1 [0-20]; cliffside #8 - in front of - trees #1 [18-20]


## 1125_Cbv34yDZ8gc

7.5 s, 8 frames read | human: 46 objects, 25 relations | TRASER: 40 objects, 40 relations, valid JSON, 2809 tokens

**Objects: 19/46 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | wall | yes (object 1) | wall | identical | ✓ |
| 1 | floor | yes (object 2) | shadow (uncertain) | mismatch | ✗ |
| 2 | plant | yes (object 3) | plant | identical | ✓ |
| 3 | person | yes (object 4) | person | identical | ✓ |
| 4 | phone | yes (object 5) | cellular telephone (uncertain) | synonym | ✓ |
| 5 | trash bag | yes (object 6) | plastic bag | hypernym/hyponym | ✓ |
| 6 | person | yes (object 7) | jersey | mismatch | ✗ |
| 7 | person | yes (object 8) | person | identical | ✓ |
| 8 | person | yes (object 9) | person | identical | ✓ |
| 9 | person | yes (object 10) | person | identical | ✓ |
| 10 | building | yes (object 11) | wall | semantic overlap | ✓ |
| 11 | nail | yes (object 12) | hammer | mismatch | ✗ |
| 12 | hammer | yes (object 13) | hammer | identical | ✓ |
| 13 | bin | yes (object 14) | wall | mismatch | ✗ |
| 14 | wall | yes (object 15) | pipe (uncertain) | mismatch | ✗ |
| 15 | grave | yes (object 16) | box | mismatch | ✗ |
| 16 | grave | yes (object 17) | box | mismatch | ✗ |
| 17 | grave | yes (object 18) | cat | mismatch | ✗ |
| 18 | grave | yes (object 19) | box | mismatch | ✗ |
| 19 | hand | yes (object 20) | arm | semantic overlap | ✓ |
| 20 | shirt | yes (object 21) | shirt | identical | ✓ |
| 21 | cap | yes (object 22) | baseball cap | hypernym/hyponym | ✓ |
| 22 | face | yes (object 23) | hat (uncertain) | mismatch | ✗ |
| 23 | shirt | yes (object 24) | jersey | hypernym/hyponym | ✓ |
| 24 | short | yes (object 25) | jeans (uncertain) | semantic overlap | ✓ |
| 25 | shirt | yes (object 26) | jersey | hypernym/hyponym | ✓ |
| 26 | band | yes (object 27) | watch | mismatch | ✗ |
| 27 | head | yes (object 28) | person | mismatch | ✗ |
| 28 | necklace | yes (object 29) | jersey (uncertain) | mismatch | ✗ |
| 29 | head | yes (object 30) | person | mismatch | ✗ |
| 30 | shirt | yes (object 31) | person | mismatch | ✗ |
| 31 | short | yes (object 32) | jersey (uncertain) | mismatch | ✗ |
| 32 | head | yes (object 33) | person | mismatch | ✗ |
| 33 | short | yes (object 34) | trousers | semantic overlap | ✓ |
| 34 | legs | yes (object 35) | legs | identical | ✓ |
| 35 | wristwatch | yes (object 36) | knob (uncertain) | mismatch | ✗ |
| 36 | epitaph | yes (object 37) | poster | mismatch | ✗ |
| 37 | signboard | yes (object 38) | signboard | identical | ✓ |
| 38 | gravestone top | yes (object 39) | beam (uncertain) | mismatch | ✗ |
| 39 | concrete | yes (object 40) | plastic bag | mismatch | ✗ |
| 40 | stone | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | stone | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | stone | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | stone | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | stone | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | stone | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 8/25 right, triplets: 0/25 right** (lenient, tIoU > 0.5)

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
| nail #11 - on top of - grave #15 | 0-8 | above | 0-8 | synonym | 1.00 | ✓ | ✗ |
| nail #11 - on - grave #15 | 0-8 | above | 0-8 | semantic overlap | 1.00 | ✓ | ✗ |
| hammer #12 - on top of - grave #15 | 0-8 | above | 0-8 | synonym | 1.00 | ✓ | ✗ |
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

**Objects: 25/36 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | track | yes (object 1) | athletic field | semantic overlap | ✓ |
| 1 | runner | yes (object 2) | person | hypernym/hyponym | ✓ |
| 2 | runner | yes (object 3) | person | hypernym/hyponym | ✓ |
| 3 | runner | yes (object 4) | person | hypernym/hyponym | ✓ |
| 4 | runner | yes (object 5) | person | hypernym/hyponym | ✓ |
| 5 | person | yes (object 6) | person | identical | ✓ |
| 6 | runner | yes (object 7) | person | hypernym/hyponym | ✓ |
| 7 | person | yes (object 8) | person | identical | ✓ |
| 8 | person | yes (object 9) | person | identical | ✓ |
| 9 | person | yes (object 10) | person | identical | ✓ |
| 10 | person | yes (object 11) | person | identical | ✓ |
| 11 | bag | yes (object 12) | person | mismatch | ✗ |
| 12 | grass | yes (object 13) | hill | semantic overlap | ✓ |
| 13 | hill | yes (object 14) | tree | mismatch | ✗ |
| 14 | person | yes (object 15) | pole | mismatch | ✗ |
| 15 | person | yes (object 16) | pole | mismatch | ✗ |
| 16 | person | yes (object 17) | person | identical | ✓ |
| 17 | person | yes (object 18) | person | identical | ✓ |
| 18 | person | yes (object 19) | person | identical | ✓ |
| 19 | crowd | yes (object 20) | person | hypernym/hyponym | ✓ |
| 20 | fence | yes (object 21) | fence | identical | ✓ |
| 21 | screen | yes (object 22) | tree | mismatch | ✗ |
| 22 | board | yes (object 23) | banner | semantic overlap | ✓ |
| 23 | screen | yes (object 24) | building | mismatch | ✗ |
| 24 | sky | yes (object 25) | cloud | semantic overlap | ✓ |
| 25 | track | yes (object 26) | fence | mismatch | ✗ |
| 26 | logo | yes (object 27) | signboard | semantic overlap | ✓ |
| 27 | logo | yes (object 28) | person | mismatch | ✗ |
| 28 | chair | yes (object 29) | bench | semantic overlap | ✓ |
| 29 | chair | yes (object 30) | person | mismatch | ✗ |
| 30 | chair | yes (object 31) | person | mismatch | ✗ |
| 31 | chair | yes (object 32) | bench | semantic overlap | ✓ |
| 32 | garbage can | yes (object 33) | person | mismatch | ✗ |
| 33 | person | yes (object 34) | person | identical | ✓ |
| 34 | person | yes (object 35) | person | identical | ✓ |
| 35 | person | yes (object 36) | person | identical | ✓ |

**Relations: 2/4 right, triplets: 2/4 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| runner #1 - runs on - track #0 | 0-8 | running on (+1 more) | 0-8 | identical | 1.00 | ✓ | ✓ |
| runner #1 - pulls away from - runner #2 | 3-8 | moving alongside | 0-8 | mismatch | 0.62 | ✗ | ✗ |
| runner #2 - runs on - track #0 | 0-8 | running on (+1 more) | 0-8 | identical | 1.00 | ✓ | ✓ |
| runner #2 - follows - runner #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (120): runner #1 - approaching - board #22 [4-7]; runner #1 - in front of - board #22 [4-8]; runner #1 - in front of - board #22 [4-8]; runner #2 - approaching - board #22 [4-7]; runner #2 - in front of - board #22 [4-8]; runner #2 - in front of - board #22 [4-8]; runner #1 - in front of - grass #12 [0-8]; runner #1 - in front of - grass #12 [0-8]; runner #2 - in front of - grass #12 [0-8]; runner #2 - in front of - grass #12 [0-8]


## 1190_UmpN6eLjN8w

10.17 s, 10 frames read | human: 18 objects, 44 relations | TRASER: 18 objects, 28 relations, valid JSON, 1355 tokens

**Objects: 7/18 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | plane | yes (object 1) | airplane | synonym | ✓ |
| 1 | person | yes (object 2) | person | identical | ✓ |
| 2 | person | yes (object 3) | hat (uncertain) | mismatch | ✗ |
| 3 | ocean | yes (object 4) | water | hypernym/hyponym | ✓ |
| 4 | person | yes (object 5) | person | identical | ✓ |
| 5 | sky | yes (object 6) | airplane | mismatch | ✗ |
| 6 | hair | yes (object 7) | hair | identical | ✓ |
| 7 | face | yes (object 8) | person | hypernym/hyponym | ✓ |
| 8 | cap | yes (object 9) | hat (uncertain) | hypernym/hyponym | ✓ |
| 9 | neck | yes (object 10) | person | mismatch | ✗ |
| 10 | hair | yes (object 11) | person | mismatch | ✗ |
| 11 | shirt | yes (object 12) | hat (uncertain) | mismatch | ✗ |
| 12 | wing | yes (object 13) | airplane | mismatch | ✗ |
| 13 | wing | yes (object 14) | airplane | mismatch | ✗ |
| 14 | tyres | yes (object 15) | airplane | mismatch | ✗ |
| 15 | tyres | yes (object 16) | airplane | mismatch | ✗ |
| 16 | nose | yes (object 17) | airplane | mismatch | ✗ |
| 17 | hair | yes (object 18) | person | mismatch | ✗ |

**Relations: 7/44 right, triplets: 7/44 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| plane #0 - approaches - person #2 | 0-3, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plane #0 - above - person #2 | 0-3, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plane #0 - approaches - person #4 | 3-11 | above | 0-1, 3-11 | mismatch | 0.89 | ✗ | ✗ |
| plane #0 - above - person #4 | 2.5-11 | above | 0-1, 3-11 | identical | 0.84 | ✓ | ✓ |
| plane #0 - moves across - sky #5 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| plane #0 - in front of - sky #5 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| plane #0 - has - wing #12 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| plane #0 - has - wing #13 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| plane #0 - has - tyres #14 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| plane #0 - has - tyres #15 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| plane #0 - has - nose #16 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| plane #0 - above - ocean #3 | 0-11 | flying over (+2 more) | 0-11 | hypernym/hyponym | 1.00 | ✓ | ✓ |
| plane #0 - above - person #1 | 0-11 | above | 0-11 | identical | 1.00 | ✓ | ✓ |
| plane #0 - approaches - person #1 | 0-11 | above | 0-11 | mismatch | 1.00 | ✗ | ✗ |
| person #1 - looking at - plane #0 | 2.5-5, 6.5-10 | looking at | 0-11 | identical | 0.55 | ✓ | ✓ |
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

**Objects: 9/12 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | swimmer | yes (object 1) | person | hypernym/hyponym | ✓ |
| 1 | towel | yes (object 2) | surfboard | mismatch | ✗ |
| 2 | sky | yes (object 3) | sky | identical | ✓ |
| 3 | ocean | yes (object 4) | person | mismatch | ✗ |
| 4 | ship | yes (object 5) | boat | synonym | ✓ |
| 5 | boat | yes (object 6) | boat | identical | ✓ |
| 6 | boat | yes (object 7) | boat | identical | ✓ |
| 7 | bra | yes (object 8) | swimsuit top | semantic overlap | ✓ |
| 8 | bikini bottoms | yes (object 9) | swimsuit | hypernym/hyponym | ✓ |
| 9 | hair | yes (object 10) | hair | identical | ✓ |
| 10 | face | yes (object 11) | person | hypernym/hyponym | ✓ |
| 11 | band | yes (object 12) | hand | mismatch | ✗ |

**Relations: 5/11 right, triplets: 2/11 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| swimmer #0 - holding - towel #1 | 0-11 | holding (+3 more) | 0-12 | identical | 0.92 | ✓ | ✗ |
| swimmer #0 - dipping - towel #1 | 2-7 | holding (+3 more) | 0-12 | mismatch | 0.42 | ✗ | ✗ |
| swimmer #0 - lifting - towel #1 | 7-10 | holding (+3 more) | 0-12 | hypernym/hyponym | 0.25 | ✗ | ✗ |
| swimmer #0 - looking at - towel #1 | 0-7, 9-11 | looking at (+3 more) | 0-12 | identical | 0.75 | ✓ | ✗ |
| swimmer #0 - rinsing - towel #1 | 2-11 | holding (+3 more) | 0-12 | mismatch | 0.75 | ✗ | ✗ |
| swimmer #0 - splashing - ocean #3 | 3-9 | nothing for this pair | - | - | - | ✗ | ✗ |
| swimmer #0 - wearing - bra #7 | 0-11 | wearing | 0-12 | identical | 0.92 | ✓ | ✓ |
| swimmer #0 - wearing - bikini bottoms #8 | 0-11 | wearing | 0-12 | identical | 0.92 | ✓ | ✓ |
| swimmer #0 - wearing - band #11 | 0-11 | has | 0-12 | hypernym/hyponym | 0.92 | ✓ | ✗ |
| towel #1 - approaching - ocean #3 | 0-2 | nothing for this pair | - | - | - | ✗ | ✗ |
| towel #1 - moving away from - ocean #3 | 7-10 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (19): swimmer #0 - has - hair #9 [0-12]; swimmer #0 - in front of - sky #2 [0-4]; towel #1 - in front of - sky #2 [0-4]; swimmer #0 - in front of - ship #4 [0-4]; swimmer #0 - in front of - boat #5 [0-4]; swimmer #0 - in front of - boat #6 [0-4]; towel #1 - in front of - ship #4 [0-4]; towel #1 - in front of - boat #5 [0-4]; towel #1 - in front of - boat #6 [0-4]; hair #9 - on - swimmer #0 [0-12]


## 1253_TPxVj7do42I

7.5 s, 8 frames read | human: 21 objects, 35 relations | TRASER: 21 objects, 37 relations, valid JSON, 1738 tokens

**Objects: 13/21 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | person | yes (object 2) | person | identical | ✓ |
| 2 | ball pool | yes (object 3) | bead (uncertain) | mismatch | ✗ |
| 3 | ceiling | yes (object 4) | ceiling | identical | ✓ |
| 4 | wall | yes (object 5) | wall panel | hypernym/hyponym | ✓ |
| 5 | window blind | yes (object 6) | curtain | synonym | ✓ |
| 6 | blind | yes (object 7) | curtain | semantic overlap | ✓ |
| 7 | blind | yes (object 8) | curtain | semantic overlap | ✓ |
| 8 | blind | yes (object 9) | window | semantic overlap | ✓ |
| 9 | blind | yes (object 10) | door frame (uncertain) | mismatch | ✗ |
| 10 | wall | yes (object 11) | wall | identical | ✓ |
| 11 | switch | yes (object 12) | door handle | mismatch | ✗ |
| 12 | cabinet | yes (object 13) | cabinet | identical | ✓ |
| 13 | countertop | yes (object 14) | bathtub (uncertain) | mismatch | ✗ |
| 14 | switch | yes (object 15) | bowl | mismatch | ✗ |
| 15 | shirt | yes (object 16) | jersey (uncertain) | hypernym/hyponym | ✓ |
| 16 | head | yes (object 17) | person | mismatch | ✗ |
| 17 | pants | yes (object 18) | sand mound | mismatch | ✗ |
| 18 | cap | yes (object 19) | baseball cap | hypernym/hyponym | ✓ |
| 19 | head | yes (object 20) | person | mismatch | ✗ |
| 20 | t-shirt | yes (object 21) | jersey (uncertain) | semantic overlap | ✓ |

**Relations: 6/35 right, triplets: 6/35 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - wearing - shirt #15 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - wearing - pants #17 | 0-6 | touching (+1 more) | 0-2 | semantic overlap | 0.33 | ✗ | ✗ |
| person #0 - moving through - ball pool #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - in - ball pool #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - in front of - window blind #5 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #0 - pushing - person #1 | 5-7 | moving away from (+2 more) | 3-8 | mismatch | 0.40 | ✗ | ✗ |
| person #0 - behind - person #1 | 0-7 | playing with (+2 more) | 0-8 | mismatch | 0.88 | ✗ | ✗ |
| person #0 - in front of - person #1 | 6-8 | moving away from (+2 more) | 3-8 | mismatch | 0.40 | ✗ | ✗ |
| person #0 - pressing - switch #11 | 6-8 | below | 4-8 | mismatch | 0.50 | ✗ | ✗ |
| person #1 - wearing - cap #18 | 0-8 | wearing | 0-2, 3-8 | identical | 0.88 | ✓ | ✓ |
| person #1 - wearing - t-shirt #20 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - in - ball pool #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - moving through - ball pool #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - in front of - window blind #5 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #1 - in front of - blind #6 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #1 - in front of - blind #7 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #1 - in front of - blind #8 | 0-8 | in front of (+1 more) | 0-8 | identical | 1.00 | ✓ | ✓ |
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
| switch #14 - on - wall #10 | 1-2 | in front of | 0-1 | mismatch | 0.00 | ✗ | ✗ |
| shirt #15 - on - person #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #16 - above - shirt #15 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| pants #17 - on - person #0 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| cap #18 - on - head #19 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #19 - above - t-shirt #20 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| t-shirt #20 - on - person #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (23): person #0 - in front of - blind #8 [0-8]; person #0 - below - blind #8 [0-8]; person #0 - in front of - wall #10 [0-8]; person #1 - in front of - wall #10 [0-8]; person #0 - in front of - blind #6 [0-8]; person #0 - in front of - blind #7 [0-8]; person #0 - in front of - wall #4 [0-8]; person #1 - in front of - wall #4 [0-8]; person #0 - below - ceiling #3 [0-8]; person #1 - below - ceiling #3 [0-8]


## 1256_Y_19xu4yTms

10.17 s, 10 frames read | human: 32 objects, 61 relations | TRASER: 32 objects, 73 relations, valid JSON, 3195 tokens

**Objects: 24/32 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | Person 1 | yes (object 1) | person | identical | ✓ |
| 1 | Person 2 | yes (object 2) | person | identical | ✓ |
| 2 | Person 3 | yes (object 3) | person | identical | ✓ |
| 3 | Person 4 | yes (object 4) | person | identical | ✓ |
| 4 | Person 5 | yes (object 5) | person | identical | ✓ |
| 5 | Person 6 | yes (object 6) | person | identical | ✓ |
| 6 | Boat | yes (object 7) | boat | identical | ✓ |
| 7 | Sea | yes (object 8) | water | hypernym/hyponym | ✓ |
| 8 | sky | yes (object 9) | fog | semantic overlap | ✓ |
| 9 | shark | yes (object 10) | dolphin | semantic overlap | ✓ |
| 10 | cap | yes (object 11) | beanie | semantic overlap | ✓ |
| 11 | glass | yes (object 12) | sunglasses | mismatch | ✗ |
| 12 | sweater | yes (object 13) | jacket | semantic overlap | ✓ |
| 13 | hair | yes (object 14) | hair | identical | ✓ |
| 14 | jacket | yes (object 15) | coat | synonym | ✓ |
| 15 | trouser | yes (object 16) | trousers (uncertain) | identical | ✓ |
| 16 | head gear | yes (object 17) | hooded jacket | mismatch | ✗ |
| 17 | camera | yes (object 18) | camera | identical | ✓ |
| 18 | head gear | yes (object 19) | hooded jacket | mismatch | ✗ |
| 19 | trouser | yes (object 20) | trousers | identical | ✓ |
| 20 | jacket | yes (object 21) | jacket | identical | ✓ |
| 21 | jacket | yes (object 22) | jacket | identical | ✓ |
| 22 | head warmer | yes (object 23) | beanie | hypernym/hyponym | ✓ |
| 23 | face | yes (object 24) | person | hypernym/hyponym | ✓ |
| 24 | jacket | yes (object 25) | jacket | identical | ✓ |
| 25 | head | yes (object 26) | person | mismatch | ✗ |
| 26 | jacket | yes (object 27) | jacket | identical | ✓ |
| 27 | seat | yes (object 28) | backpack | mismatch | ✗ |
| 28 | seat | yes (object 29) | chair backrest | semantic overlap | ✓ |
| 29 | seat | yes (object 30) | backpack | mismatch | ✗ |
| 30 | seat | yes (object 31) | backpack | mismatch | ✗ |
| 31 | seat | yes (object 32) | strap (uncertain) | mismatch | ✗ |

**Relations: 22/61 right, triplets: 20/61 right** (lenient, tIoU > 0.5)

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
| Person 4 #3 - on - Boat #6 | 0-11.1667 | on | 0-11 | identical | 0.99 | ✓ | ✓ |
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
| shark #9 - in - Sea #7 | 0-11.1667 | on (+1 more) | 0-11 | semantic overlap | 0.99 | ✓ | ✓ |
| shark #9 - in front of - Boat #6 | 0-11.1667 | approaching (+1 more) | 0-11 | mismatch | 0.99 | ✗ | ✗ |
| Person 1 #0 - wears - sweater #12 | 0-11.1667 | wearing | 0-11 | identical | 0.99 | ✓ | ✓ |
| Person 1 #0 - holds onto - seat #28 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 1 #0 - looks at - shark #9 | 0-11.1667 | looking at | 0-11 | identical | 0.99 | ✓ | ✓ |
| Person 2 #1 - looks at - shark #9 | 0-11.1667 | looking at | 0-11 | identical | 0.99 | ✓ | ✓ |
| Person 3 #2 - looks at - shark #9 | 0-11.1667 | looking at | 0-11 | identical | 0.99 | ✓ | ✓ |
| Person 3 #2 - records - shark #9 | 0-11.1667 | looking at | 0-11 | mismatch | 0.99 | ✗ | ✗ |
| Person 4 #3 - looks at - shark #9 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 5 #4 - looks at - shark #9 | 0-2, 2.66667-11.1667 | looking at | 0-11 | identical | 0.93 | ✓ | ✓ |
| Person 6 #5 - looks at - shark #9 | 0-11.1667 | looking at | 0-11 | identical | 0.99 | ✓ | ✓ |
| Person 1 #0 - wears - cap #10 | 0-11.1667 | wearing | 0-11 | identical | 0.99 | ✓ | ✓ |
| Person 1 #0 - wears - glass #11 | 0-11.1667 | wearing | 0-11 | identical | 0.99 | ✓ | ✗ |
| Person 2 #1 - has - hair #13 | 0-11.1667 | wearing | 0-11 | hypernym/hyponym | 0.99 | ✓ | ✓ |
| Person 2 #1 - wears - jacket #14 | 0-11.1667 | wearing | 0-11 | identical | 0.99 | ✓ | ✓ |
| Person 2 #1 - wears - trouser #15 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 4 #3 - wears - head gear #16 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 4 #3 - wears - jacket #20 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 3 #2 - holds - camera #17 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 3 #2 - wears - head gear #18 | 0-11.1667 | wearing | 0-11 | identical | 0.99 | ✓ | ✗ |
| Person 3 #2 - wears - jacket #21 | 0-11.1667 | wearing | 0-11 | identical | 0.99 | ✓ | ✓ |
| Person 5 #4 - wears - head warmer #22 | 0-11.1667 | wearing | 0-11 | identical | 0.99 | ✓ | ✓ |
| Person 5 #4 - wears - jacket #24 | 0-11.1667 | wearing | 0-11 | identical | 0.99 | ✓ | ✓ |
| Person 6 #5 - has - head #25 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 6 #5 - wears - jacket #26 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 6 #5 - holds onto - seat #30 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 5 #4 - holds onto - seat #29 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 2 #1 - in front of - seat #27 | 0-11.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| Person 2 #1 - on - Sea #7 | 0-11.1667 | in front of | 0-11 | mismatch | 0.99 | ✗ | ✗ |
| Person 1 #0 - on - Sea #7 | 0-11.1667 | in front of | 0-11 | mismatch | 0.99 | ✗ | ✗ |
| Person 3 #2 - on - Sea #7 | 0-11.1667 | in front of | 0-11 | mismatch | 0.99 | ✗ | ✗ |
| Person 4 #3 - on - Sea #7 | 0-11.1667 | in front of | 0-11 | mismatch | 0.99 | ✗ | ✗ |
| Person 5 #4 - on - Sea #7 | 0-11.1667 | in front of | 0-11 | mismatch | 0.99 | ✗ | ✗ |
| Person 6 #5 - on - Sea #7 | 0-11.1667 | in front of | 0-11 | mismatch | 0.99 | ✗ | ✗ |
| Boat #6 - on - Sea #7 | 0-11.1667 | moving on (+1 more) | 0-11 | hypernym/hyponym | 0.99 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (41): Person 2 #1 - wearing - head gear #16 [0-11]; Person 2 #1 - wearing - jacket #20 [0-11]; Person 3 #2 - wearing - trouser #19 [0-11]; Person 5 #4 - holding - camera #17 [0-11]; Boat #6 - carrying - Person 1 #0 [0-11]; Boat #6 - carrying - Person 2 #1 [0-11]; Boat #6 - carrying - Person 3 #2 [0-11]; Boat #6 - carrying - Person 4 #3 [0-11]; Boat #6 - carrying - Person 5 #4 [0-11]; Boat #6 - carrying - Person 6 #5 [0-11]


## 1261_wsHfWwHXgLs

10.17 s, 10 frames read | human: 8 objects, 22 relations | TRASER: 8 objects, 18 relations, valid JSON, 721 tokens

**Objects: 7/8 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | ocean | yes (object 1) | dog | mismatch | ✗ |
| 1 | sky | yes (object 2) | fog | semantic overlap | ✓ |
| 2 | dog | yes (object 3) | dog | identical | ✓ |
| 3 | inflatable float | yes (object 4) | inflatable raft | synonym | ✓ |
| 4 | pinna | yes (object 5) | dog's ear | hypernym/hyponym | ✓ |
| 5 | side of a float | yes (object 6) | raft | semantic overlap | ✓ |
| 6 | blanket | yes (object 7) | towel | semantic overlap | ✓ |
| 7 | side of a float | yes (object 8) | inflatable raft | semantic overlap | ✓ |

**Relations: 5/22 right, triplets: 5/22 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| sky #1 - above - ocean #0 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #2 - riding - inflatable float #3 | 0-11 | riding (+1 more) | 0-13 | identical | 0.85 | ✓ | ✓ |
| dog #2 - on - inflatable float #3 | 0-11 | riding (+1 more) | 0-13 | semantic overlap | 0.85 | ✓ | ✓ |
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
| pinna #4 - attached to - dog #2 | 0-11 | part of | 0-13 | semantic overlap | 0.85 | ✓ | ✓ |
| pinna #4 - part of - dog #2 | 0-11 | part of | 0-13 | identical | 0.85 | ✓ | ✓ |
| side of a float #5 - attached to - inflatable float #3 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| side of a float #5 - part of - inflatable float #3 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| blanket #6 - moving over - ocean #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| blanket #6 - above - ocean #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| blanket #6 - on - inflatable float #3 | 0-11 | draped on (+1 more) | 0-13 | hypernym/hyponym | 0.85 | ✓ | ✓ |
| side of a float #7 - attached to - inflatable float #3 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| side of a float #7 - part of - inflatable float #3 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (13): dog #2 - riding - side of a float #5 [0-13]; dog #2 - on - side of a float #5 [0-13]; dog #2 - riding - side of a float #7 [0-13]; dog #2 - on - side of a float #7 [0-13]; blanket #6 - on - side of a float #5 [0-13]; blanket #6 - on - side of a float #7 [0-13]; inflatable float #3 - overlapping - side of a float #5 [0-13]; inflatable float #3 - overlapping - side of a float #7 [0-13]; side of a float #5 - overlapping - side of a float #7 [0-13]; sky #1 - above - dog #2 [0-8]


## 1268_h58xqlUE5xA

10.17 s, 10 frames read | human: 11 objects, 21 relations | TRASER: 11 objects, 36 relations, valid JSON, 1071 tokens

**Objects: 6/11 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | railings | yes (object 2) | railing | identical | ✓ |
| 2 | sky | yes (object 3) | clouds | semantic overlap | ✓ |
| 3 | trees | yes (object 4) | hill | mismatch | ✗ |
| 4 | waterfall | yes (object 5) | waterfall | identical | ✓ |
| 5 | waterfall | yes (object 6) | cliff | semantic overlap | ✓ |
| 6 | trees and waterfall | yes (object 7) | cliff | mismatch | ✗ |
| 7 | trees and mist | yes (object 8) | tree | semantic overlap | ✓ |
| 8 | shirt | yes (object 9) | person | mismatch | ✗ |
| 9 | head | yes (object 10) | person | mismatch | ✗ |
| 10 | trousers | yes (object 11) | person | mismatch | ✗ |

**Relations: 7/21 right, triplets: 3/21 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - holding - railings #1 | 0-11 | standing on (+1 more) | 0-10 | mismatch | 0.91 | ✗ | ✗ |
| person #0 - behind - railings #1 | 0-11 | standing on (+1 more) | 0-10 | mismatch | 0.91 | ✗ | ✗ |
| person #0 - wearing - shirt #8 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - wearing - trousers #10 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - watching - waterfall #4 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - in front of - trees #3 | 0-11 | in front of | 0-10 | identical | 0.91 | ✓ | ✗ |
| railings #1 - in front of - trees #3 | 0-11 | in front of | 0-10 | identical | 0.91 | ✓ | ✗ |
| sky #2 - above - waterfall #4 | 0-11 | above | 0-10 | identical | 0.91 | ✓ | ✓ |
| sky #2 - above - waterfall #5 | 0-11 | above | 0-10 | identical | 0.91 | ✓ | ✓ |
| sky #2 - above - trees and waterfall #6 | 0-11 | above | 0-10 | identical | 0.91 | ✓ | ✗ |
| sky #2 - above - trees and mist #7 | 0-11 | above | 0-10 | identical | 0.91 | ✓ | ✓ |
| sky #2 - above - trees #3 | 0-11 | above | 0-10 | identical | 0.91 | ✓ | ✗ |
| waterfall #4 - flowing down - trees #3 | 0-11 | in front of | 0-10 | mismatch | 0.91 | ✗ | ✗ |
| waterfall #5 - flowing down - trees #3 | 0-11 | in front of | 0-10 | mismatch | 0.91 | ✗ | ✗ |
| trees and waterfall #6 - flowing down - trees #3 | 0-11 | in front of | 0-10 | mismatch | 0.91 | ✗ | ✗ |
| trees and mist #7 - flowing down - trees #3 | 0-11 | in front of | 0-10 | mismatch | 0.91 | ✗ | ✗ |
| shirt #8 - overlapping - person #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #8 - above - trousers #10 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #9 - above - shirt #8 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #9 - above - trousers #10 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| trousers #10 - overlapping - person #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (23): shirt #8 - standing on - railings #1 [0-10]; shirt #8 - on - railings #1 [0-10]; head #9 - standing on - railings #1 [0-10]; head #9 - on - railings #1 [0-10]; trousers #10 - standing on - railings #1 [0-10]; trousers #10 - on - railings #1 [0-10]; waterfall #4 - flowing down - trees and waterfall #6 [0-10]; waterfall #4 - flowing down - waterfall #5 [0-10]; railings #1 - in front of - waterfall #4 [0-10]; railings #1 - in front of - waterfall #5 [0-10]


## 1275_ARcg-EyKWrA

10.17 s, 10 frames read | human: 68 objects, 21 relations | TRASER: 40 objects, 47 relations, valid JSON, 2956 tokens

**Objects: 17/68 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | cage | yes (object 1) | birdcage | hypernym/hyponym | ✓ |
| 1 | chest of drawers | yes (object 2) | wooden cabinet | semantic overlap | ✓ |
| 2 | floor | yes (object 3) | cat | mismatch | ✗ |
| 3 | framed poster | yes (object 4) | poster | hypernym/hyponym | ✓ |
| 4 | jar | yes (object 5) | toy (uncertain) | mismatch | ✗ |
| 5 | curtain | yes (object 6) | window | semantic overlap | ✓ |
| 6 | furniture | yes (object 7) | cat | mismatch | ✗ |
| 7 | person | yes (object 8) | person | identical | ✓ |
| 8 | faucet | yes (object 9) | box | mismatch | ✗ |
| 9 | household material | yes (object 10) | plush toy (uncertain) | mismatch | ✗ |
| 10 | household material | yes (object 11) | toy (uncertain) | mismatch | ✗ |
| 11 | furniture | yes (object 12) | cat | mismatch | ✗ |
| 12 | wall | yes (object 13) | wall | identical | ✓ |
| 13 | curtain | yes (object 14) | curtain | identical | ✓ |
| 14 | socket | yes (object 15) | wall socket | identical | ✓ |
| 15 | window | yes (object 16) | window | identical | ✓ |
| 16 | cat | yes (object 17) | cat | identical | ✓ |
| 17 | shirt | yes (object 18) | jersey | hypernym/hyponym | ✓ |
| 18 | shorts | yes (object 19) | trousers | semantic overlap | ✓ |
| 19 | face | yes (object 20) | neck (uncertain) | mismatch | ✗ |
| 20 | hand | yes (object 21) | arm | semantic overlap | ✓ |
| 21 | leg | yes (object 22) | shoe (uncertain) | mismatch | ✗ |
| 22 | leg | yes (object 23) | shoe (uncertain) | mismatch | ✗ |
| 23 | hand | yes (object 24) | tail (uncertain) | mismatch | ✗ |
| 24 | legs | yes (object 25) | tail (uncertain) | mismatch | ✗ |
| 25 | tail | yes (object 26) | tail (uncertain) | identical | ✓ |
| 26 | head | yes (object 27) | cat | mismatch | ✗ |
| 27 | leg | yes (object 28) | tail (uncertain) | mismatch | ✗ |
| 28 | leg | yes (object 29) | tail (uncertain) | mismatch | ✗ |
| 29 | cage toy | yes (object 30) | ball (uncertain) | semantic overlap | ✓ |
| 30 | cage toy | yes (object 31) | toy (uncertain) | hypernym/hyponym | ✓ |
| 31 | toy, cross | yes (object 32) | toy (uncertain) | hypernym/hyponym | ✓ |
| 32 | cage toy | yes (object 33) | birdcage | mismatch | ✗ |
| 33 | cage toy | yes (object 34) | birdcage | mismatch | ✗ |
| 34 | cage toy | yes (object 35) | birdcage | mismatch | ✗ |
| 35 | cage toy | yes (object 36) | birdcage | mismatch | ✗ |
| 36 | frame | yes (object 37) | pole (uncertain) | mismatch | ✗ |
| 37 | frame | yes (object 38) | birdcage | mismatch | ✗ |
| 38 | frame | yes (object 39) | pole (uncertain) | mismatch | ✗ |
| 39 | frame | yes (object 40) | pole (uncertain) | mismatch | ✗ |
| 40 | frame | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | frame | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | frame | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | frame | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | frame | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | frame | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | jar cover | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | jar | no: after the first 40 | - | no label from TRASER | ✗ |
| 48 | jar handle | no: after the first 40 | - | no label from TRASER | ✗ |
| 49 | wall frame | no: after the first 40 | - | no label from TRASER | ✗ |
| 50 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 51 | wall | no: after the first 40 | - | no label from TRASER | ✗ |
| 52 | wall | no: after the first 40 | - | no label from TRASER | ✗ |
| 53 | wall | no: after the first 40 | - | no label from TRASER | ✗ |
| 54 | wall molding | no: after the first 40 | - | no label from TRASER | ✗ |
| 55 | household material | no: after the first 40 | - | no label from TRASER | ✗ |
| 56 | cage frame | no: after the first 40 | - | no label from TRASER | ✗ |
| 57 | lamp base | no: after the first 40 | - | no label from TRASER | ✗ |
| 58 | lamp shade | no: after the first 40 | - | no label from TRASER | ✗ |
| 59 | drawer handle | no: after the first 40 | - | no label from TRASER | ✗ |
| 60 | drawer handle | no: after the first 40 | - | no label from TRASER | ✗ |
| 61 | drawer handle | no: after the first 40 | - | no label from TRASER | ✗ |
| 62 | drawer handle | no: after the first 40 | - | no label from TRASER | ✗ |
| 63 | drawer handle | no: after the first 40 | - | no label from TRASER | ✗ |
| 64 | drawer handle | no: after the first 40 | - | no label from TRASER | ✗ |
| 65 | bag | no: after the first 40 | - | no label from TRASER | ✗ |
| 66 | cage base | no: after the first 40 | - | no label from TRASER | ✗ |
| 67 | baseboard | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 6/21 right, triplets: 6/21 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| cage #0 - on - floor #2 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| cage #0 - in front of - wall #12 | 0-11 | in front of | 0-11 | identical | 1.00 | ✓ | ✓ |
| chest of drawers #1 - in front of - wall #12 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| jar #4 - on - chest of drawers #1 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #7 - hold - cat #16 | 0-11 | holding (+2 more) | 0-11 | identical | 1.00 | ✓ | ✓ |
| person #7 - look at - cat #16 | 0-11 | looking at (+2 more) | 0-11 | identical | 1.00 | ✓ | ✓ |
| person #7 - help climb cage - cat #16 | 0-11 | holding (+2 more) | 0-11 | semantic overlap | 1.00 | ✓ | ✓ |
| person #7 - next to - cage #0 | 0-11 | in front of | 0-11 | mismatch | 1.00 | ✗ | ✗ |
| faucet #8 - above - chest of drawers #1 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #15 - in - wall #12 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| cat #16 - grip - cage #0 | 0-11 | inside (+1 more) | 0-11 | mismatch | 1.00 | ✗ | ✗ |
| cat #16 - climb - cage #0 | 0-11 | inside (+1 more) | 0-11 | mismatch | 1.00 | ✗ | ✗ |
| cat #16 - touching - cage #0 | 0-11 | inside (+1 more) | 0-11 | mismatch | 1.00 | ✗ | ✗ |
| cat #16 - in front of - cage #0 | 0-11 | in front of (+1 more) | 0-11 | identical | 1.00 | ✓ | ✓ |
| cat #16 - look at - toy, cross #31 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| cat #16 - above - floor #2 | 0-11 | in front of | 0-11 | mismatch | 1.00 | ✗ | ✗ |
| cat #16 - in front of - chest of drawers #1 | 0-11 | in front of | 0-11 | identical | 1.00 | ✓ | ✓ |
| cat #16 - below - jar #4 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #20 - touching - cat #16 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #23 - touching - cat #16 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| toy, cross #31 - inside - cage #0 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (38): person #7 - wearing - shirt #17 [0-11]; person #7 - wearing - shorts #18 [0-11]; cat #16 - moving around - person #7 [0-11]; cat #16 - in front of - person #7 [0-11]; cat #16 - below - person #7 [0-11]; head #26 - inside - cage #0 [0-11]; head #26 - in front of - cage #0 [0-11]; cage #0 - in front of - curtain #5 [0-11]; cage #0 - in front of - window #15 [0-11]; cage #0 - in front of - chest of drawers #1 [0-11]


## 1308_-C_XboJfD0g

10.17 s, 10 frames read | human: 14 objects, 15 relations | TRASER: 14 objects, 27 relations, valid JSON, 1367 tokens

**Objects: 7/14 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | shelf | yes (object 1) | cell phone | mismatch | ✗ |
| 1 | hand | yes (object 2) | hand | identical | ✓ |
| 2 | pricetag | yes (object 3) | tag (uncertain) | hypernym/hyponym | ✓ |
| 3 | floor | yes (object 4) | tabletop | semantic overlap | ✓ |
| 4 | screen | yes (object 5) | television set | semantic overlap | ✓ |
| 5 | phone | yes (object 6) | cellular telephone (uncertain) | synonym | ✓ |
| 6 | phone holder | yes (object 7) | power strip | mismatch | ✗ |
| 7 | phone | yes (object 8) | device (uncertain) | hypernym/hyponym | ✓ |
| 8 | ipad | yes (object 9) | cellular telephone (uncertain) | semantic overlap | ✓ |
| 9 | accessories | yes (object 10) | box | mismatch | ✗ |
| 10 | counter top | yes (object 11) | cell phone | mismatch | ✗ |
| 11 | wood | yes (object 12) | box | mismatch | ✗ |
| 12 | wood | yes (object 13) | box | mismatch | ✗ |
| 13 | metal base | yes (object 14) | drawer front (uncertain) | mismatch | ✗ |

**Relations: 1/15 right, triplets: 0/15 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| shelf #0 - on - floor #3 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #1 - moves along - shelf #0 | 0-6 | touching (+2 more) | 0-6 | mismatch | 1.00 | ✗ | ✗ |
| hand #1 - in front of - shelf #0 | 0-6 | in front of (+2 more) | 0-7 | identical | 0.86 | ✓ | ✗ |
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
| accessories #9 - below - counter top #10 | 0-3 | in front of | 0-4 | mismatch | 0.75 | ✗ | ✗ |
| accessories #9 - inside - shelf #0 | 0-3 | in front of | 0-4 | mismatch | 0.75 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (22): hand #1 - in front of - counter top #10 [0-7]; hand #1 - in front of - phone holder #6 [0-1, 2-7]; hand #1 - in front of - screen #4 [0-1, 2-7]; shelf #0 - in front of - phone holder #6 [0-1, 2-12]; shelf #0 - in front of - screen #4 [0-1, 2-12]; counter top #10 - in front of - phone holder #6 [0-1, 2-12]; counter top #10 - in front of - screen #4 [0-1, 2-12]; phone holder #6 - in front of - screen #4 [0-1, 2-12]; accessories #9 - in front of - phone holder #6 [0-1, 2-4]; accessories #9 - in front of - screen #4 [0-1, 2-4]


## 1352_nt-UZxGk9Bg

10.17 s, 10 frames read | human: 14 objects, 35 relations | TRASER: 14 objects, 43 relations, valid JSON, 1397 tokens

**Objects: 11/14 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | snow | yes (object 2) | snowboarder | mismatch | ✗ |
| 2 | snowfeet | yes (object 3) | ski | synonym | ✓ |
| 3 | ski poles | yes (object 4) | ski pole | identical | ✓ |
| 4 | skating stick | yes (object 5) | ski pole | semantic overlap | ✓ |
| 5 | skating stick | yes (object 6) | ski pole | semantic overlap | ✓ |
| 6 | snowboard | yes (object 7) | ski | semantic overlap | ✓ |
| 7 | snowboard | yes (object 8) | ski | semantic overlap | ✓ |
| 8 | face cap | yes (object 9) | helmet | semantic overlap | ✓ |
| 9 | face | yes (object 10) | goggles | mismatch | ✗ |
| 10 | hoodie | yes (object 11) | jacket | hypernym/hyponym | ✓ |
| 11 | trouser | yes (object 12) | trousers | identical | ✓ |
| 12 | shoe | yes (object 13) | ski | mismatch | ✗ |
| 13 | shoe | yes (object 14) | ski boot | hypernym/hyponym | ✓ |

**Relations: 13/35 right, triplets: 13/35 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - on - snow #1 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - move across - snow #1 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - ski - snow #1 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - hold - skating stick #4 | 0-11 | holding | 0-10 | identical | 0.91 | ✓ | ✓ |
| person #0 - hold - skating stick #5 | 0-11 | holding | 0-10 | identical | 0.91 | ✓ | ✓ |
| person #0 - stand on - snowboard #6 | 0-11 | riding (+2 more) | 0-10 | mismatch | 0.91 | ✗ | ✗ |
| person #0 - stand on - snowboard #7 | 0-11 | riding (+2 more) | 0-10 | mismatch | 0.91 | ✗ | ✗ |
| person #0 - wear - face cap #8 | 0-11 | wearing | 0-10 | identical | 0.91 | ✓ | ✓ |
| person #0 - wear - hoodie #10 | 0-11 | wearing | 0-10 | identical | 0.91 | ✓ | ✓ |
| person #0 - wear - trouser #11 | 0-11 | wearing | 0-10 | identical | 0.91 | ✓ | ✓ |
| person #0 - wear - shoe #12 | 0-11 | riding (+2 more) | 0-10 | mismatch | 0.91 | ✗ | ✗ |
| person #0 - wear - shoe #13 | 0-11 | wearing | 0-10 | identical | 0.91 | ✓ | ✓ |
| snowfeet #2 - below - shoe #12 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| snowfeet #2 - below - shoe #13 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| ski poles #3 - above - snow #1 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| skating stick #4 - attached to - ski poles #3 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| skating stick #4 - move with - person #0 | 0-11 | near | 0-10 | semantic overlap | 0.91 | ✓ | ✓ |
| skating stick #5 - attached to - ski poles #3 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| skating stick #5 - move with - person #0 | 0-11 | near | 0-10 | semantic overlap | 0.91 | ✓ | ✓ |
| snowboard #6 - on - snow #1 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| snowboard #6 - move with - person #0 | 0-11 | below | 0-10 | mismatch | 0.91 | ✗ | ✗ |
| snowboard #7 - on - snow #1 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| snowboard #7 - move with - person #0 | 0-11 | below | 0-10 | mismatch | 0.91 | ✗ | ✗ |
| face cap #8 - above - face #9 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| face cap #8 - on - person #0 | 0-11 | on | 0-10 | identical | 0.91 | ✓ | ✓ |
| face #9 - above - hoodie #10 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| hoodie #10 - above - trouser #11 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| hoodie #10 - on - person #0 | 0-11 | on | 0-10 | identical | 0.91 | ✓ | ✓ |
| trouser #11 - above - shoe #12 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| trouser #11 - above - shoe #13 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| trouser #11 - on - person #0 | 0-11 | on | 0-10 | identical | 0.91 | ✓ | ✓ |
| shoe #12 - on - snowboard #7 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| shoe #12 - on - person #0 | 0-11 | below | 0-10 | mismatch | 0.91 | ✗ | ✗ |
| shoe #13 - on - snowboard #6 | 0-11 | on | 0-10 | identical | 0.91 | ✓ | ✓ |
| shoe #13 - on - person #0 | 0-11 | on | 0-10 | identical | 0.91 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (18): person #0 - wearing - face #9 [0-10]; person #0 - holding - ski poles #3 [0-10]; face #9 - on - person #0 [0-10]; shoe #13 - on - snowboard #7 [0-10]; shoe #13 - on - shoe #12 [0-10]; ski poles #3 - near - person #0 [0-10]; ski poles #3 - above - snowboard #6 [0-10]; skating stick #4 - above - snowboard #6 [0-10]; skating stick #5 - above - snowboard #6 [0-10]; ski poles #3 - above - snowboard #7 [0-10]


## 1480_WAGXu9_6Uv0

7.5 s, 8 frames read | human: 46 objects, 41 relations | TRASER: 40 objects, 42 relations, valid JSON, 3214 tokens

**Objects: 20/46 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | sink | yes (object 1) | sink | identical | ✓ |
| 1 | bathroom tap | yes (object 2) | faucet | synonym | ✓ |
| 2 | cup | yes (object 3) | bottle | semantic overlap | ✓ |
| 3 | bathroom product | yes (object 4) | bottle | hypernym/hyponym | ✓ |
| 4 | bathroom container | yes (object 5) | bottle | hypernym/hyponym | ✓ |
| 5 | toothbrush | yes (object 6) | bottle | mismatch | ✗ |
| 6 | toothpaste | yes (object 7) | bottle | mismatch | ✗ |
| 7 | bathroom product | yes (object 8) | cup | mismatch | ✗ |
| 8 | toothbrush | yes (object 9) | bottle | mismatch | ✗ |
| 9 | cord | yes (object 10) | bottle | mismatch | ✗ |
| 10 | paper towel | yes (object 11) | toilet paper roll | semantic overlap | ✓ |
| 11 | towel | yes (object 12) | curtain | mismatch | ✗ |
| 12 | bathroom counter | yes (object 13) | sink | semantic overlap | ✓ |
| 13 | wall | yes (object 14) | mirror (uncertain) | mismatch | ✗ |
| 14 | switch | yes (object 15) | wall socket | semantic overlap | ✓ |
| 15 | towel | yes (object 16) | curtain | mismatch | ✗ |
| 16 | door handle | yes (object 17) | door handle | identical | ✓ |
| 17 | door hanger | yes (object 18) | handle (uncertain) | mismatch | ✗ |
| 18 | brush | yes (object 19) | toothbrush (uncertain) | hypernym/hyponym | ✓ |
| 19 | wall | yes (object 20) | curtain | mismatch | ✗ |
| 20 | chain lock | yes (object 21) | pipe (uncertain) | mismatch | ✗ |
| 21 | door trim | yes (object 22) | refrigerator | mismatch | ✗ |
| 22 | door | yes (object 23) | refrigerator | mismatch | ✗ |
| 23 | mirror | yes (object 24) | mirror | identical | ✓ |
| 24 | door accessory | yes (object 25) | bottle | mismatch | ✗ |
| 25 | door handle | yes (object 26) | doorknob | synonym | ✓ |
| 26 | door | yes (object 27) | curtain | mismatch | ✗ |
| 27 | cabinet | yes (object 28) | cabinet door | semantic overlap | ✓ |
| 28 | floor | yes (object 29) | drawer (uncertain) | mismatch | ✗ |
| 29 | frame | yes (object 30) | sink | mismatch | ✗ |
| 30 | bathroom supply | yes (object 31) | bottle | hypernym/hyponym | ✓ |
| 31 | toothpaste | yes (object 32) | bottle | mismatch | ✗ |
| 32 | towel | yes (object 33) | mirror | mismatch | ✗ |
| 33 | tube | yes (object 34) | bottle | semantic overlap | ✓ |
| 34 | towel | yes (object 35) | roll of toilet paper | mismatch | ✗ |
| 35 | bathroom supply | yes (object 36) | bottle | hypernym/hyponym | ✓ |
| 36 | counter | yes (object 37) | countertop (uncertain) | synonym | ✓ |
| 37 | drain hole | yes (object 38) | drain cover (uncertain) | semantic overlap | ✓ |
| 38 | tap handle | yes (object 39) | faucet | semantic overlap | ✓ |
| 39 | tap handle | yes (object 40) | faucet | semantic overlap | ✓ |
| 40 | cabinet handle | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | cabinet handle | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | cabinet handle | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | cabinet handle | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | cabinet handle | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | cabinet handle | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 3/41 right, triplets: 2/41 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| sink #0 - built into - bathroom counter #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| sink #0 - above - cabinet #27 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bathroom tap #1 - above - sink #0 | 0-8 | on (+1 more) | 0-8 | semantic overlap | 1.00 | ✓ | ✓ |
| bathroom tap #1 - attached to - sink #0 | 0-8 | attached to (+1 more) | 0-8 | identical | 1.00 | ✓ | ✓ |
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
| switch #14 - on - door trim #21 | 0-1, 2-8 | mounted on (+1 more) | 0-8 | hypernym/hyponym | 0.88 | ✓ | ✗ |
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

**Objects: 16/20 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | trees | yes (object 1) | trees | identical | ✓ |
| 1 | sky | yes (object 2) | excavator arm | mismatch | ✗ |
| 2 | person | yes (object 3) | person | identical | ✓ |
| 3 | sand | yes (object 4) | dirt mound | semantic overlap | ✓ |
| 4 | excavator | yes (object 5) | excavator arm | hypernym/hyponym | ✓ |
| 5 | grass | yes (object 6) | field | semantic overlap | ✓ |
| 6 | trees | yes (object 7) | tree | identical | ✓ |
| 7 | trees | yes (object 8) | bush | semantic overlap | ✓ |
| 8 | cap | yes (object 9) | baseball cap | hypernym/hyponym | ✓ |
| 9 | shirt | yes (object 10) | jacket | semantic overlap | ✓ |
| 10 | trouser | yes (object 11) | trousers (uncertain) | identical | ✓ |
| 11 | face | yes (object 12) | baseball cap | mismatch | ✗ |
| 12 | bucket | yes (object 13) | dump truck bed (uncertain) | mismatch | ✗ |
| 13 | bucket cyclinder | yes (object 14) | excavator arm | semantic overlap | ✓ |
| 14 | cab | yes (object 15) | window frame (uncertain) | mismatch | ✗ |
| 15 | sand | yes (object 16) | dirt mound | semantic overlap | ✓ |
| 16 | sand | yes (object 17) | mound of dirt | semantic overlap | ✓ |
| 17 | sand | yes (object 18) | mound of dirt | semantic overlap | ✓ |
| 18 | sand | yes (object 19) | mound of dirt | semantic overlap | ✓ |
| 19 | cab window | yes (object 20) | window frame (uncertain) | semantic overlap | ✓ |

**Relations: 5/34 right, triplets: 5/34 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| trees #0 - under - sky #1 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #6 - under - sky #1 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #7 - under - sky #1 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - under - sky #1 | 0-8.5 | in front of | 0-9 | mismatch | 0.94 | ✗ | ✗ |
| excavator #4 - under - sky #1 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| sand #3 - under - sky #1 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #5 - under - sky #1 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #5 - under - sky #1 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - observe - excavator #4 | 2.33333-8.5 | looking at (+1 more) | 0-8 | synonym | 0.67 | ✓ | ✓ |
| person #2 - left of - excavator #4 | 0-8.5 | in front of (+1 more) | 0-9 | mismatch | 0.94 | ✗ | ✗ |
| person #2 - wears - shirt #9 | 0-8.5 | wearing (+1 more) | 0-8 | identical | 0.94 | ✓ | ✓ |
| person #2 - wears - trouser #10 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| bucket #12 - part of - excavator #4 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| bucket cyclinder #13 - part of - excavator #4 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| cab window #19 - part of - cab #14 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - near - bucket #12 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - standing on - sand #3 | 0-8.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| excavator #4 - in front of - trees #0 | 0-8.5 | in front of (+1 more) | 0-9 | identical | 0.94 | ✓ | ✓ |
| excavator #4 - in front of - trees #6 | 0-8.5 | above | 0-9 | mismatch | 0.94 | ✗ | ✗ |
| excavator #4 - in front of - trees #7 | 0-8.5 | in front of (+1 more) | 0-9 | identical | 0.94 | ✓ | ✓ |
| excavator #4 - in front of - grass #5 | 0-8.5 | in front of (+1 more) | 0-9 | identical | 0.94 | ✓ | ✓ |
| excavator #4 - digging - sand #3 | 0-8.5 | above | 0-9 | mismatch | 0.94 | ✗ | ✗ |
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

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | chair | yes (object 1) | chair | identical | ✓ |
| 1 | chair | yes (object 2) | chair | identical | ✓ |
| 2 | chair | yes (object 3) | chair | identical | ✓ |
| 3 | chair | yes (object 4) | signboard | mismatch | ✗ |
| 4 | chair | yes (object 5) | chair | identical | ✓ |
| 5 | chair | yes (object 6) | chair | identical | ✓ |
| 6 | chair | yes (object 7) | chair | identical | ✓ |
| 7 | chair | yes (object 8) | chair | identical | ✓ |
| 8 | chair | yes (object 9) | chair | identical | ✓ |
| 9 | chair | yes (object 10) | chair | identical | ✓ |
| 10 | chair | yes (object 11) | chair | identical | ✓ |
| 11 | chair | yes (object 12) | chair | identical | ✓ |
| 12 | chair | yes (object 13) | chair | identical | ✓ |
| 13 | chair | yes (object 14) | chair | identical | ✓ |
| 14 | floor | yes (object 15) | chair | mismatch | ✗ |
| 15 | table | yes (object 16) | chair | mismatch | ✗ |
| 16 | table | yes (object 17) | chair | mismatch | ✗ |
| 17 | table | yes (object 18) | chair | mismatch | ✗ |
| 18 | table | yes (object 19) | chair | mismatch | ✗ |
| 19 | window | yes (object 20) | signboard | mismatch | ✗ |
| 20 | window | yes (object 21) | window | identical | ✓ |
| 21 | ceiling | yes (object 22) | ceiling | identical | ✓ |
| 22 | towel | yes (object 23) | chair | mismatch | ✗ |
| 23 | towel | yes (object 24) | chair | mismatch | ✗ |
| 24 | towel | yes (object 25) | chair | mismatch | ✗ |
| 25 | towel | yes (object 26) | chair | mismatch | ✗ |
| 26 | window | yes (object 27) | vent (uncertain) | mismatch | ✗ |
| 27 | towel | yes (object 28) | chair | mismatch | ✗ |
| 28 | towel | yes (object 29) | chair | mismatch | ✗ |
| 29 | towel | yes (object 30) | chair | mismatch | ✗ |
| 30 | towel | yes (object 31) | chair | mismatch | ✗ |
| 31 | towel | yes (object 32) | chair | mismatch | ✗ |
| 32 | towel | yes (object 33) | chair | mismatch | ✗ |
| 33 | towel | yes (object 34) | chair | mismatch | ✗ |
| 34 | towel | yes (object 35) | chair | mismatch | ✗ |
| 35 | towel | yes (object 36) | chair | mismatch | ✗ |
| 36 | window | yes (object 37) | wall panel | mismatch | ✗ |
| 37 | exit sign | yes (object 38) | signboard | hypernym/hyponym | ✓ |
| 38 | counter | yes (object 39) | signboard | mismatch | ✗ |
| 39 | counter | yes (object 40) | wooden panel | mismatch | ✗ |
| 40 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | decoration item | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | counter | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | decoration item | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 48 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 49 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 50 | towel | no: after the first 40 | - | no label from TRASER | ✗ |
| 51 | logo | no: after the first 40 | - | no label from TRASER | ✗ |
| 52 | counter door | no: after the first 40 | - | no label from TRASER | ✗ |
| 53 | box | no: after the first 40 | - | no label from TRASER | ✗ |
| 54 | box | no: after the first 40 | - | no label from TRASER | ✗ |
| 55 | box | no: after the first 40 | - | no label from TRASER | ✗ |
| 56 | chair | no: after the first 40 | - | no label from TRASER | ✗ |
| 57 | chair | no: after the first 40 | - | no label from TRASER | ✗ |
| 58 | poster or logo | no: after the first 40 | - | no label from TRASER | ✗ |
| 59 | poster or logo | no: after the first 40 | - | no label from TRASER | ✗ |
| 60 | decoration item | no: after the first 40 | - | no label from TRASER | ✗ |
| 61 | decoration item | no: after the first 40 | - | no label from TRASER | ✗ |
| 62 | poster or logo | no: after the first 40 | - | no label from TRASER | ✗ |

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

**Objects: 10/21 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | ship | yes (object 1) | boat | synonym | ✓ |
| 1 | bridge | yes (object 2) | bridge | identical | ✓ |
| 2 | sky | yes (object 3) | cloud | semantic overlap | ✓ |
| 3 | trees | yes (object 4) | hill | mismatch | ✗ |
| 4 | trees | yes (object 5) | hill | mismatch | ✗ |
| 5 | trees | yes (object 6) | hill | mismatch | ✗ |
| 6 | trees | yes (object 7) | hill | mismatch | ✗ |
| 7 | tower | yes (object 8) | ship | mismatch | ✗ |
| 8 | ship | yes (object 9) | boat | synonym | ✓ |
| 9 | ship | yes (object 10) | boat | synonym | ✓ |
| 10 | ship | yes (object 11) | boat | synonym | ✓ |
| 11 | boat | yes (object 12) | mast | mismatch | ✗ |
| 12 | river | yes (object 13) | boat | mismatch | ✗ |
| 13 | people | yes (object 14) | crowd | synonym | ✓ |
| 14 | ship's bridge | yes (object 15) | radar dome | mismatch | ✗ |
| 15 | paddle wheel | yes (object 16) | boat | mismatch | ✗ |
| 16 | barricade | yes (object 17) | signboard | mismatch | ✗ |
| 17 | roof | yes (object 18) | awning | semantic overlap | ✓ |
| 18 | hull | yes (object 19) | boat | semantic overlap | ✓ |
| 19 | safety railing | yes (object 20) | radar dome | mismatch | ✗ |
| 20 | ships rear | yes (object 21) | boat | semantic overlap | ✓ |

**Relations: 25/39 right, triplets: 14/39 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| ship #0 - in front of - ship #8 | 0-8 | in front of (+1 more) | 0-9 | identical | 0.89 | ✓ | ✓ |
| ship #0 - in front of - ship #9 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✓ |
| ship #0 - in front of - ship #10 | 0-8 | in front of (+1 more) | 0-9 | identical | 0.89 | ✓ | ✓ |
| ship #0 - in front of - boat #11 | 0-8 | has | 0-9 | mismatch | 0.89 | ✗ | ✗ |
| ship #0 - in front of - tower #7 | 0-8 | in front of (+1 more) | 0-9 | identical | 0.89 | ✓ | ✗ |
| ship #0 - in front of - trees #3 | 0-8 | in front of (+1 more) | 0-9 | identical | 0.89 | ✓ | ✗ |
| ship #0 - in front of - trees #5 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✗ |
| ship #0 - below - sky #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| ship #0 - carrying - people #13 | 0-8 | has | 0-9 | hypernym/hyponym | 0.89 | ✓ | ✓ |
| ship #0 - moving on - river #12 | 0-8 | in front of | 0-9 | mismatch | 0.89 | ✗ | ✗ |
| ship #0 - on - river #12 | 0-8 | in front of | 0-9 | mismatch | 0.89 | ✗ | ✗ |
| ship #0 - passing under - bridge #1 | 0-8 | under (+1 more) | 0-9 | hypernym/hyponym | 0.89 | ✓ | ✓ |
| ship #0 - navigating under - bridge #1 | 0-8 | under (+1 more) | 0-9 | hypernym/hyponym | 0.89 | ✓ | ✓ |
| ship #0 - under - bridge #1 | 0-8 | under (+1 more) | 0-9 | identical | 0.89 | ✓ | ✓ |
| bridge #1 - above - river #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bridge #1 - in front of - sky #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| ship #8 - on - river #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| ship #9 - on - river #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| ship #10 - on - river #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| boat #11 - on - river #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| river #12 - below - sky #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| people #13 - on - ship #0 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✓ |
| people #13 - riding - ship #0 | 0-8 | on | 0-9 | hypernym/hyponym | 0.89 | ✓ | ✓ |
| ship's bridge #14 - above - roof #17 | 0-8 | above | 0-9 | identical | 0.89 | ✓ | ✗ |
| ship's bridge #14 - attached to - ship #0 | 0-8 | on | 0-9 | hypernym/hyponym | 0.89 | ✓ | ✗ |
| paddle wheel #15 - on - ship #0 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✗ |
| paddle wheel #15 - attached to - ship #0 | 0-8 | on | 0-9 | hypernym/hyponym | 0.89 | ✓ | ✗ |
| barricade #16 - on - ship #0 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✗ |
| barricade #16 - attached to - ship #0 | 0-8 | on | 0-9 | hypernym/hyponym | 0.89 | ✓ | ✗ |
| roof #17 - on - ship #0 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✓ |
| roof #17 - attached to - ship #0 | 0-8 | on | 0-9 | hypernym/hyponym | 0.89 | ✓ | ✓ |
| roof #17 - above - people #13 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| hull #18 - below - roof #17 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| hull #18 - on - river #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| hull #18 - part of - ship #0 | 0-8 | on | 0-9 | semantic overlap | 0.89 | ✓ | ✓ |
| safety railing #19 - on - ship #0 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✗ |
| safety railing #19 - attached to - ship #0 | 0-8 | on | 0-9 | hypernym/hyponym | 0.89 | ✓ | ✗ |
| ships rear #20 - on - ship #0 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✓ |
| ships rear #20 - attached to - ship #0 | 0-8 | on | 0-9 | hypernym/hyponym | 0.89 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (41): ship #0 - has - barricade #16 [0-9]; ship #0 - has - roof #17 [0-9]; ship #0 - has - ship's bridge #14 [0-9]; ship #0 - has - safety railing #19 [0-9]; ship #0 - has - paddle wheel #15 [0-9]; ship #0 - in front of - paddle wheel #15 [0-9]; ship #0 - has - ships rear #20 [0-9]; ship #0 - in front of - ships rear #20 [0-9]; ship #0 - has - hull #18 [0-9]; ship #0 - in front of - hull #18 [0-9]


## 1717_lh_2_1duNgw

7.5 s, 8 frames read | human: 65 objects, 79 relations | TRASER: 40 objects, 101 relations, valid JSON, 3490 tokens

**Objects: 38/65 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | player | yes (object 1) | person | hypernym/hyponym | ✓ |
| 1 | referee | yes (object 2) | person | hypernym/hyponym | ✓ |
| 2 | player | yes (object 3) | person | hypernym/hyponym | ✓ |
| 3 | player | yes (object 4) | person | hypernym/hyponym | ✓ |
| 4 | player | yes (object 5) | person | hypernym/hyponym | ✓ |
| 5 | player | yes (object 6) | person | hypernym/hyponym | ✓ |
| 6 | player | yes (object 7) | person | hypernym/hyponym | ✓ |
| 7 | spectators | yes (object 8) | crowd | synonym | ✓ |
| 8 | field | yes (object 9) | soccer ball | mismatch | ✗ |
| 9 | goalposts | yes (object 10) | pole | hypernym/hyponym | ✓ |
| 10 | scoreboard | yes (object 11) | signboard | hypernym/hyponym | ✓ |
| 11 | barrier wall | yes (object 12) | barrier (uncertain) | hypernym/hyponym | ✓ |
| 12 | tunnel | yes (object 13) | pole | mismatch | ✗ |
| 13 | security person | yes (object 14) | person | hypernym/hyponym | ✓ |
| 14 | security staff | yes (object 15) | person | hypernym/hyponym | ✓ |
| 15 | security staff | yes (object 16) | person | hypernym/hyponym | ✓ |
| 16 | people | yes (object 17) | person | hypernym/hyponym | ✓ |
| 17 | people | yes (object 18) | person | hypernym/hyponym | ✓ |
| 18 | people | yes (object 19) | person | hypernym/hyponym | ✓ |
| 19 | people | yes (object 20) | person | hypernym/hyponym | ✓ |
| 20 | people | yes (object 21) | person | hypernym/hyponym | ✓ |
| 21 | helmet | yes (object 22) | helmet | identical | ✓ |
| 22 | helmet | yes (object 23) | helmet | identical | ✓ |
| 23 | helmet | yes (object 24) | helmet | identical | ✓ |
| 24 | helmet | yes (object 25) | helmet | identical | ✓ |
| 25 | helmet | yes (object 26) | helmet | identical | ✓ |
| 26 | helmet | yes (object 27) | helmet | identical | ✓ |
| 27 | shoe | yes (object 28) | shoe | identical | ✓ |
| 28 | shoe | yes (object 29) | shoe | identical | ✓ |
| 29 | shoe | yes (object 30) | shoe | identical | ✓ |
| 30 | shoe | yes (object 31) | shoe | identical | ✓ |
| 31 | shoe | yes (object 32) | shoe | identical | ✓ |
| 32 | shoe | yes (object 33) | shoe | identical | ✓ |
| 33 | shoe | yes (object 34) | shoe | identical | ✓ |
| 34 | shoe | yes (object 35) | shoe | identical | ✓ |
| 35 | shoe | yes (object 36) | shoe | identical | ✓ |
| 36 | shoe | yes (object 37) | shoe | identical | ✓ |
| 37 | shoe | yes (object 38) | shoe | identical | ✓ |
| 38 | shoe | yes (object 39) | shoe | identical | ✓ |
| 39 | shoe | yes (object 40) | shoe | identical | ✓ |
| 40 | uniform | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | uniform | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | uniform | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | uniform | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | uniform | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | uniform | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | uniform | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | uniform | no: after the first 40 | - | no label from TRASER | ✗ |
| 48 | uniform | no: after the first 40 | - | no label from TRASER | ✗ |
| 49 | uniform | no: after the first 40 | - | no label from TRASER | ✗ |
| 50 | uniform | no: after the first 40 | - | no label from TRASER | ✗ |
| 51 | uniform | no: after the first 40 | - | no label from TRASER | ✗ |
| 52 | pants | no: after the first 40 | - | no label from TRASER | ✗ |
| 53 | pants | no: after the first 40 | - | no label from TRASER | ✗ |
| 54 | pants | no: after the first 40 | - | no label from TRASER | ✗ |
| 55 | pants | no: after the first 40 | - | no label from TRASER | ✗ |
| 56 | pants | no: after the first 40 | - | no label from TRASER | ✗ |
| 57 | pants | no: after the first 40 | - | no label from TRASER | ✗ |
| 58 | pants | no: after the first 40 | - | no label from TRASER | ✗ |
| 59 | shirt | no: after the first 40 | - | no label from TRASER | ✗ |
| 60 | hat | no: after the first 40 | - | no label from TRASER | ✗ |
| 61 | glove | no: after the first 40 | - | no label from TRASER | ✗ |
| 62 | glove | no: after the first 40 | - | no label from TRASER | ✗ |
| 63 | glove | no: after the first 40 | - | no label from TRASER | ✗ |
| 64 | glove | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 34/79 right, triplets: 28/79 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| player #0 - on - field #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #0 - wearing - helmet #23 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #0 - wearing - pants #52 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #0 - wearing - shoe #31 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #0 - wearing - shoe #32 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #0 - wearing - glove #63 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #0 - wearing - glove #64 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #0 - in front of - spectators #7 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #0 - in front of - barrier wall #11 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #0 - in front of - goalposts #9 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #0 - in front of - tunnel #12 | 1-8 | in front of | 0-8 | identical | 0.88 | ✓ | ✗ |
| referee #1 - on - field #8 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| referee #1 - moving across - field #8 | 0-5.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| referee #1 - moving away from - player #2 | 0-5.5 | moving away from | 0-5 | identical | 0.91 | ✓ | ✓ |
| referee #1 - in front of - tunnel #12 | 0-5 | in front of | 0-5 | identical | 1.00 | ✓ | ✗ |
| referee #1 - in front of - spectators #7 | 0-5 | in front of | 0-5 | identical | 1.00 | ✓ | ✓ |
| referee #1 - in front of - barrier wall #11 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| referee #1 - in front of - goalposts #9 | 0-5 | in front of | 0-5 | identical | 1.00 | ✓ | ✓ |
| player #2 - on - field #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #2 - touching - player #4 | 0-3.5 | near | 0-8 | hypernym/hyponym | 0.44 | ✗ | ✗ |
| player #2 - looking at - player #3 | 2-7 | near | 0-8 | mismatch | 0.62 | ✗ | ✗ |
| player #2 - wearing - helmet #24 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #2 - wearing - pants #55 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #2 - wearing - shoe #27 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #2 - wearing - shoe #28 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #2 - wearing - glove #61 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #2 - in front of - spectators #7 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #2 - in front of - barrier wall #11 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #2 - in front of - goalposts #9 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #2 - in front of - tunnel #12 | 1-8 | in front of | 0-8 | identical | 0.88 | ✓ | ✗ |
| player #3 - on - field #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #3 - looking at - player #2 | 0-4, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #3 - wearing - helmet #25 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #3 - wearing - pants #53 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #3 - wearing - shoe #29 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #3 - wearing - shoe #30 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #3 - in front of - spectators #7 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #3 - in front of - barrier wall #11 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #3 - in front of - goalposts #9 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #3 - in front of - tunnel #12 | 1-8 | in front of | 0-8 | identical | 0.88 | ✓ | ✗ |
| player #4 - on - field #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #4 - wearing - helmet #26 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #4 - wearing - pants #54 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #4 - wearing - shoe #33 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #4 - wearing - shoe #34 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #4 - wearing - glove #62 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #4 - in front of - tunnel #12 | 1-8 | in front of | 0-8 | identical | 0.88 | ✓ | ✗ |
| player #4 - in front of - spectators #7 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #4 - in front of - barrier wall #11 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #4 - in front of - goalposts #9 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| player #5 - on - field #8 | 4-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #5 - approaching - player #2 | 4-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #5 - wearing - helmet #22 | 4-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #5 - in front of - spectators #7 | 4-8 | in front of | 4-8 | identical | 1.00 | ✓ | ✓ |
| player #5 - in front of - barrier wall #11 | 4-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #5 - in front of - goalposts #9 | 4-8 | in front of | 4-8 | identical | 1.00 | ✓ | ✓ |
| player #6 - on - field #8 | 3-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #6 - approaching - player #2 | 3-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #6 - wearing - helmet #21 | 3-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #6 - in front of - spectators #7 | 3-8 | in front of | 0-1, 4-8 | identical | 0.67 | ✓ | ✓ |
| player #6 - in front of - barrier wall #11 | 3-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| player #6 - in front of - goalposts #9 | 3-8 | in front of | 0-1, 4-8 | identical | 0.67 | ✓ | ✓ |
| spectators #7 - above - barrier wall #11 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| goalposts #9 - in front of - spectators #7 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| scoreboard #10 - above - goalposts #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| barrier wall #11 - in front of - spectators #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| tunnel #12 - below - scoreboard #10 | 1-8 | below | 0-8 | identical | 0.88 | ✓ | ✗ |
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

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | sky | yes (object 1) | sky | identical | ✓ |
| 1 | ground | yes (object 2) | terrain | synonym | ✓ |
| 2 | road | yes (object 3) | road | identical | ✓ |
| 3 | building | yes (object 4) | building | identical | ✓ |
| 4 | house | yes (object 5) | house | identical | ✓ |
| 5 | house | yes (object 6) | building | hypernym/hyponym | ✓ |
| 6 | house | yes (object 7) | building | hypernym/hyponym | ✓ |
| 7 | house | yes (object 8) | tree | mismatch | ✗ |
| 8 | house | yes (object 9) | tree | mismatch | ✗ |
| 9 | house | yes (object 10) | tree | mismatch | ✗ |
| 10 | sand | yes (object 11) | golf hole | mismatch | ✗ |
| 11 | swimming pool | yes (object 12) | swimming pool | identical | ✓ |
| 12 | tree | yes (object 13) | tree | identical | ✓ |
| 13 | tree | yes (object 14) | tree | identical | ✓ |
| 14 | tree | yes (object 15) | tree | identical | ✓ |
| 15 | tree | yes (object 16) | tree | identical | ✓ |
| 16 | tree | yes (object 17) | tree | identical | ✓ |
| 17 | tree | yes (object 18) | tree | identical | ✓ |
| 18 | tree | yes (object 19) | tree | identical | ✓ |
| 19 | tree | yes (object 20) | tree | identical | ✓ |
| 20 | tree | yes (object 21) | tree | identical | ✓ |
| 21 | tree | yes (object 22) | house | mismatch | ✗ |
| 22 | tree | yes (object 23) | tree | identical | ✓ |

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
| sand #10 - on - ground #1 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✗ |
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
| tree #21 - on - ground #1 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✗ |
| tree #22 - on - ground #1 | 0-4 | on | 0-3 | identical | 0.75 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (21): sand #10 - near - swimming pool #11 [0-8]; swimming pool #11 - near - house #6 [0-8]; swimming pool #11 - near - house #4 [0-8]; swimming pool #11 - near - tree #21 [0-8]; swimming pool #11 - near - tree #12 [0-8]; swimming pool #11 - near - tree #13 [0-8]; swimming pool #11 - near - tree #14 [0-8]; swimming pool #11 - near - tree #16 [0-8]; swimming pool #11 - near - tree #17 [0-8]; swimming pool #11 - near - tree #15 [0-8]


## 179_mha1KKixPts

22.67 s, 23 frames read | human: 27 objects, 14 relations | TRASER: 27 objects, 20 relations, valid JSON, 1635 tokens

**Objects: 25/27 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | tree | yes (object 1) | tree trunk | semantic overlap | ✓ |
| 1 | tree | yes (object 2) | tree trunk | semantic overlap | ✓ |
| 2 | tree | yes (object 3) | tree trunk | semantic overlap | ✓ |
| 3 | tree | yes (object 4) | tree trunk | semantic overlap | ✓ |
| 4 | tree | yes (object 5) | tree trunk | semantic overlap | ✓ |
| 5 | tree | yes (object 6) | tree trunk | semantic overlap | ✓ |
| 6 | excavator | yes (object 7) | bulldozer | semantic overlap | ✓ |
| 7 | trees and leaves | yes (object 8) | tree | semantic overlap | ✓ |
| 8 | leaves | yes (object 9) | leaves | identical | ✓ |
| 9 | trees | yes (object 10) | tree | identical | ✓ |
| 10 | trees | yes (object 11) | tree | identical | ✓ |
| 11 | trees | yes (object 12) | tree | identical | ✓ |
| 12 | trees | yes (object 13) | tree trunk | hypernym/hyponym | ✓ |
| 13 | floor | yes (object 14) | grass | semantic overlap | ✓ |
| 14 | trunk | yes (object 15) | tree trunk | identical | ✓ |
| 15 | trunk | yes (object 16) | tree trunk | identical | ✓ |
| 16 | trunk | yes (object 17) | tree trunk | identical | ✓ |
| 17 | trunk | yes (object 18) | tree trunk | identical | ✓ |
| 18 | trunk | yes (object 19) | tree trunk | identical | ✓ |
| 19 | trunk | yes (object 20) | tree trunk | identical | ✓ |
| 20 | trunk | yes (object 21) | tree trunk | identical | ✓ |
| 21 | trunk | yes (object 22) | tree trunk | identical | ✓ |
| 22 | trunk | yes (object 23) | tree trunk | identical | ✓ |
| 23 | trunk | yes (object 24) | tree trunk | identical | ✓ |
| 24 | bucket | yes (object 25) | dump truck | mismatch | ✗ |
| 25 | cyclinder | yes (object 26) | tree trunk | mismatch | ✗ |
| 26 | cab | yes (object 27) | truck | hypernym/hyponym | ✓ |

**Relations: 1/14 right, triplets: 0/14 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| excavator #6 - on - floor #13 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| excavator #6 - under - trees #9 | 0-23 | in front of | 0-24 | mismatch | 0.96 | ✗ | ✗ |
| excavator #6 - raises - bucket #24 | 0-23 | attached to (+3 more) | 0-24 | mismatch | 0.96 | ✗ | ✗ |
| leaves #8 - on - floor #13 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| leaves #8 - in front of - excavator #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| bucket #24 - attached to - excavator #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| bucket #24 - in front of - cab #26 | 0-23 | in front of (+1 more) | 0-24 | identical | 0.96 | ✓ | ✗ |
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

**Objects: 16/20 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | flowers | yes (object 1) | flower bed | semantic overlap | ✓ |
| 1 | shed | yes (object 2) | shed | identical | ✓ |
| 2 | plants | yes (object 3) | grass | hypernym/hyponym | ✓ |
| 3 | wall | yes (object 4) | stone wall | hypernym/hyponym | ✓ |
| 4 | wall | yes (object 5) | pole (uncertain) | mismatch | ✗ |
| 5 | box | yes (object 6) | door (uncertain) | mismatch | ✗ |
| 6 | tree | yes (object 7) | bush | semantic overlap | ✓ |
| 7 | flowers | yes (object 8) | flower bed | semantic overlap | ✓ |
| 8 | plants | yes (object 9) | plant | identical | ✓ |
| 9 | big plant | yes (object 10) | bush | hypernym/hyponym | ✓ |
| 10 | bush | yes (object 11) | bush | identical | ✓ |
| 11 | trees | yes (object 12) | bush | semantic overlap | ✓ |
| 12 | trees | yes (object 13) | bush | semantic overlap | ✓ |
| 13 | building | yes (object 14) | roof (uncertain) | semantic overlap | ✓ |
| 14 | building | yes (object 15) | wall | semantic overlap | ✓ |
| 15 | wall | yes (object 16) | stone wall | hypernym/hyponym | ✓ |
| 16 | wall | yes (object 17) | stone wall | hypernym/hyponym | ✓ |
| 17 | roof | yes (object 18) | roof (uncertain) | identical | ✓ |
| 18 | wood | yes (object 19) | door (uncertain) | mismatch | ✗ |
| 19 | wood | yes (object 20) | door (uncertain) | mismatch | ✗ |

**Relations: 5/21 right, triplets: 5/21 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| flowers #0 - in front of - wall #3 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| shed #1 - in front of - wall #3 | 0-6.5 | in front of | 0-6 | identical | 0.92 | ✓ | ✓ |
| shed #1 - on - plants #2 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants #2 - in front of - bush #10 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| box #5 - attached to - wall #3 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| box #5 - attached to - shed #1 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #6 - behind - wall #3 | 0-5.5 | in front of | 0-6 | mismatch | 0.92 | ✗ | ✗ |
| plants #8 - in front of - wall #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants #8 - in front of - flowers #0 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| big plant #9 - in front of - wall #3 | 1-8 | in front of | 0-8 | identical | 0.88 | ✓ | ✓ |
| bush #10 - in front of - wall #3 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| trees #11 - behind - wall #3 | 1-5 | in front of | 0-4 | mismatch | 0.60 | ✗ | ✗ |
| trees #12 - behind - wall #3 | 0-6 | in front of | 0-6 | mismatch | 1.00 | ✗ | ✗ |
| building #13 - behind - wall #3 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| building #14 - behind - wall #3 | 0-6 | in front of | 0-6 | mismatch | 1.00 | ✗ | ✗ |
| roof #17 - above - shed #1 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| roof #17 - on - shed #1 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| wood #18 - on - shed #1 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| wood #18 - attached to - shed #1 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| wood #19 - on - shed #1 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| wood #19 - attached to - shed #1 | 0-4 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (44): flowers #0 - in front of - wall #16 [0-8]; flowers #0 - in front of - wall #15 [0-6]; flowers #0 - in front of - shed #1 [0-6]; flowers #0 - on - plants #2 [0-8]; flowers #7 - inside - flowers #0 [0-8]; flowers #7 - in front of - wall #3 [0-8]; flowers #7 - in front of - wall #16 [0-8]; flowers #7 - in front of - wall #15 [0-6]; flowers #7 - in front of - shed #1 [0-6]; flowers #7 - on - plants #2 [0-8]


## 1936_gvKlIkjfP0Q

2.67 s, 4 frames read | human: 56 objects, 40 relations | TRASER: 40 objects, 315 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 24/56 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | car | yes (object 1) | car | identical | ✓ |
| 1 | car | yes (object 2) | car | identical | ✓ |
| 2 | tripod | yes (object 3) | tripod | identical | ✓ |
| 3 | clutter | yes (object 4) | person | mismatch | ✗ |
| 4 | garage wall | yes (object 5) | wall | hypernym/hyponym | ✓ |
| 5 | garage | yes (object 6) | window | mismatch | ✗ |
| 6 | door | yes (object 7) | door (uncertain) | identical | ✓ |
| 7 | power outlet | yes (object 8) | door (uncertain) | mismatch | ✗ |
| 8 | rod | yes (object 9) | pipe (uncertain) | semantic overlap | ✓ |
| 9 | door controller | yes (object 10) | projector | mismatch | ✗ |
| 10 | rod | yes (object 11) | pipe (uncertain) | semantic overlap | ✓ |
| 11 | metal | yes (object 12) | pipe (uncertain) | semantic overlap | ✓ |
| 12 | wall | yes (object 13) | wall | identical | ✓ |
| 13 | bagpack | yes (object 14) | bucket | mismatch | ✗ |
| 14 | hoodie | yes (object 15) | jacket | hypernym/hyponym | ✓ |
| 15 | hand | yes (object 16) | arm | semantic overlap | ✓ |
| 16 | side mirror | yes (object 17) | car door handle | mismatch | ✗ |
| 17 | car door handle | yes (object 18) | car door handle | identical | ✓ |
| 18 | tyre | yes (object 19) | wheel | synonym | ✓ |
| 19 | metal | yes (object 20) | chair | mismatch | ✗ |
| 20 | window | yes (object 21) | window | identical | ✓ |
| 21 | windshield | yes (object 22) | car | mismatch | ✗ |
| 22 | bonnet | yes (object 23) | car | semantic overlap | ✓ |
| 23 | rear wing | yes (object 24) | car door handle | mismatch | ✗ |
| 24 | windshield | yes (object 25) | car hood | mismatch | ✗ |
| 25 | headlight | yes (object 26) | headlight | identical | ✓ |
| 26 | bonnet area | yes (object 27) | vent (uncertain) | mismatch | ✗ |
| 27 | front bumper | yes (object 28) | bumper (uncertain) | hypernym/hyponym | ✓ |
| 28 | tyres | yes (object 29) | wheel | synonym | ✓ |
| 29 | fender | yes (object 30) | car door | semantic overlap | ✓ |
| 30 | metal | yes (object 31) | car door handle | mismatch | ✗ |
| 31 | rod | yes (object 32) | pipe (uncertain) | semantic overlap | ✓ |
| 32 | door controller | yes (object 33) | projector | mismatch | ✗ |
| 33 | gym equipment | yes (object 34) | ladder | mismatch | ✗ |
| 34 | bagpack | yes (object 35) | bucket | mismatch | ✗ |
| 35 | hoodie | yes (object 36) | jacket | hypernym/hyponym | ✓ |
| 36 | hand | yes (object 37) | arm | semantic overlap | ✓ |
| 37 | side mirror | yes (object 38) | car door handle | mismatch | ✗ |
| 38 | car door handle | yes (object 39) | car door handle | identical | ✓ |
| 39 | tyre | yes (object 40) | wheel | synonym | ✓ |
| 40 | windshield | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | bonnet | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | side mirror | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | rear wing | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | windshield | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | car engine area | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | headlight | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | bonnet area | no: after the first 40 | - | no label from TRASER | ✗ |
| 48 | front bumper | no: after the first 40 | - | no label from TRASER | ✗ |
| 49 | tires | no: after the first 40 | - | no label from TRASER | ✗ |
| 50 | door glass | no: after the first 40 | - | no label from TRASER | ✗ |
| 51 | car door | no: after the first 40 | - | no label from TRASER | ✗ |
| 52 | fender | no: after the first 40 | - | no label from TRASER | ✗ |
| 53 | metal | no: after the first 40 | - | no label from TRASER | ✗ |
| 54 | car roof | no: after the first 40 | - | no label from TRASER | ✗ |
| 55 | step ladder | no: after the first 40 | - | no label from TRASER | ✗ |

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
| hand #15 - in front of - car #0 | 0-3 | touching (+7 more) | 0-4 | mismatch | 0.75 | ✗ | ✗ |
| hand #15 - in front of - tripod #2 | 0-3 | touching (+4 more) | 0-4 | mismatch | 0.75 | ✗ | ✗ |
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

**Objects: 13/16 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | counter | yes (object 1) | countertop | synonym | ✓ |
| 1 | microwave | yes (object 2) | oven | semantic overlap | ✓ |
| 2 | person | yes (object 3) | arm | mismatch | ✗ |
| 3 | food | yes (object 4) | dough (uncertain) | hypernym/hyponym | ✓ |
| 4 | bracelet | yes (object 5) | bracelet | identical | ✓ |
| 5 | bracelet | yes (object 6) | bracelet (uncertain) | identical | ✓ |
| 6 | top of a microwave | yes (object 7) | countertop | semantic overlap | ✓ |
| 7 | touch panel | yes (object 8) | control panel (uncertain) | hypernym/hyponym | ✓ |
| 8 | door | yes (object 9) | oven | mismatch | ✗ |
| 9 | glass tray | yes (object 10) | bowl | semantic overlap | ✓ |
| 10 | oven | yes (object 11) | oven door | semantic overlap | ✓ |
| 11 | front panel | yes (object 12) | oven door | semantic overlap | ✓ |
| 12 | ring | yes (object 13) | handle (uncertain) | mismatch | ✗ |
| 13 | bracelet (duplicate of id ) | yes (object 14) | bracelet (uncertain) | identical | ✓ |
| 14 | arm | yes (object 15) | arm | identical | ✓ |
| 15 | clothing, shirt | yes (object 16) | fabric (uncertain) | hypernym/hyponym | ✓ |

**Relations: 2/28 right, triplets: 2/28 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| microwave #1 - on - counter #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - inside - microwave #1 | 0-8 | loading (+1 more) | 0-9 | mismatch | 0.89 | ✗ | ✗ |
| person #2 - in front of - microwave #1 | 1-3, 4-6 | in front of (+1 more) | 0-9 | identical | 0.44 | ✗ | ✗ |
| person #2 - above - glass tray #9 | 0-5, 6-8 | holding | 0-9 | mismatch | 0.78 | ✗ | ✗ |
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
| glass tray #9 - inside - microwave #1 | 0-8 | moving into (+1 more) | 0-9 | semantic overlap | 0.89 | ✓ | ✓ |
| glass tray #9 - inside - oven #10 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| glass tray #9 - above - counter #0 | 0-8 | on | 0-9 | semantic overlap | 0.89 | ✓ | ✓ |
| oven #10 - inside - microwave #1 | 0-8 | attached to | 0-9 | mismatch | 0.89 | ✗ | ✗ |
| front panel #11 - inside - microwave #1 | 0-8 | attached to | 0-9 | mismatch | 0.89 | ✗ | ✗ |
| ring #12 - worn by - person #2 | 1-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| bracelet (duplicate of id ) #13 - worn by - arm #14 | 1-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (11): person #2 - wearing - bracelet #4 [0-9]; counter #0 - in front of - microwave #1 [0-9]; counter #0 - below - microwave #1 [0-9]; oven #10 - above - counter #0 [0-9]; front panel #11 - above - counter #0 [0-9]; top of a microwave #6 - above - counter #0 [0-9]; arm #14 - in front of - microwave #1 [0-9]; bracelet #4 - on - person #2 [0-9]; bracelet #4 - in front of - microwave #1 [0-9]; person #2 - above - counter #0 [0-9]


## 2225_6acPX_00M9Q

15.0 s, 15 frames read | human: 19 objects, 38 relations | TRASER: 19 objects, 49 relations, valid JSON, 1958 tokens

**Objects: 16/19 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | rail signal | yes (object 1) | traffic light | hypernym/hyponym | ✓ |
| 1 | warning sign board | yes (object 2) | signboard | hypernym/hyponym | ✓ |
| 2 | mountains | yes (object 3) | mountain | identical | ✓ |
| 3 | ground | yes (object 4) | snow | semantic overlap | ✓ |
| 4 | sky | yes (object 5) | sky | identical | ✓ |
| 5 | mountain | yes (object 6) | mountain | identical | ✓ |
| 6 | train | yes (object 7) | train | identical | ✓ |
| 7 | ground | yes (object 8) | snow | semantic overlap | ✓ |
| 8 | barrier wall | yes (object 9) | snow | mismatch | ✗ |
| 9 | snow | yes (object 10) | smoke | mismatch | ✗ |
| 10 | ground | yes (object 11) | snow | semantic overlap | ✓ |
| 11 | roof | yes (object 12) | snow | mismatch | ✗ |
| 12 | sign board | yes (object 13) | signboard | identical | ✓ |
| 13 | sign board | yes (object 14) | signboard | identical | ✓ |
| 14 | sign board | yes (object 15) | signboard | identical | ✓ |
| 15 | light | yes (object 16) | traffic light | hypernym/hyponym | ✓ |
| 16 | light | yes (object 17) | traffic light | hypernym/hyponym | ✓ |
| 17 | light | yes (object 18) | headlight | hypernym/hyponym | ✓ |
| 18 | window | yes (object 19) | window | identical | ✓ |

**Relations: 11/38 right, triplets: 6/38 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| rail signal #0 - in front of - train #6 | 0-11 | in front of | 0-15 | identical | 0.73 | ✓ | ✓ |
| rail signal #0 - on - ground #3 | 0-16 | above | 0-15 | semantic overlap | 0.94 | ✓ | ✓ |
| rail signal #0 - in front of - barrier wall #8 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| warning sign board #1 - on - ground #3 | 4-13 | above | 4-11 | semantic overlap | 0.78 | ✓ | ✓ |
| warning sign board #1 - below - rail signal #0 | 4-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| warning sign board #1 - attached to - barrier wall #8 | 3.5-13.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| mountains #2 - above - ground #3 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #4 - above - mountains #2 | 4-15 | above | 4-15 | identical | 1.00 | ✓ | ✓ |
| train #6 - in front of - mountains #2 | 0-15 | in front of (+1 more) | 0-15 | identical | 1.00 | ✓ | ✓ |
| train #6 - on - ground #3 | 0-15 | moving on (+1 more) | 0-15 | hypernym/hyponym | 1.00 | ✓ | ✓ |
| train #6 - below - sky #4 | 3.5-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| train #6 - approaches - rail signal #0 | 0-10 | moving past | 0-15 | mismatch | 0.67 | ✗ | ✗ |
| train #6 - passes - rail signal #0 | 9-16 | moving past | 0-15 | synonym | 0.38 | ✗ | ✗ |
| train #6 - clears - snow #9 | 0-15 | moving past | 0-15 | semantic overlap | 1.00 | ✓ | ✗ |
| train #6 - moves through - snow #9 | 0-16 | moving past | 0-15 | semantic overlap | 0.94 | ✓ | ✗ |
| train #6 - moves past - barrier wall #8 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| barrier wall #8 - on - ground #3 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| snow #9 - on - ground #3 | 0-16 | above | 0-15 | semantic overlap | 0.94 | ✓ | ✗ |
| snow #9 - covers - ground #3 | 0-15 | above | 0-15 | semantic overlap | 1.00 | ✓ | ✗ |
| snow #9 - in front of - train #6 | 0-15 | in front of | 0-15 | identical | 1.00 | ✓ | ✗ |
| snow #9 - moves away from - train #6 | 0-16 | in front of | 0-15 | mismatch | 0.94 | ✗ | ✗ |
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
| light #17 - attached to - train #6 | 0-14 | on | 0-2, 10-15 | hypernym/hyponym | 0.40 | ✗ | ✗ |
| window #18 - on - train #6 | 0-14 | on | 0-2, 10-15 | identical | 0.40 | ✗ | ✗ |
| window #18 - attached to - train #6 | 0-14 | on | 0-2, 10-15 | hypernym/hyponym | 0.40 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (35): train #6 - moving past - light #15 [0-15]; train #6 - moving past - light #16 [0-15]; train #6 - moving past - warning sign board #1 [4-11]; train #6 - moving past - sign board #14 [0-2, 10-12]; train #6 - moving past - sign board #12 [0-2]; train #6 - moving past - sign board #13 [0-2]; train #6 - moving past - window #18 [0-2, 10-15]; train #6 - moving past - light #17 [0-2, 10-15]; rail signal #0 - in front of - mountains #2 [0-15]; light #15 - in front of - train #6 [0-15]


## 226_n7YpGfnTqoY

6.33 s, 6 frames read | human: 20 objects, 51 relations | TRASER: 20 objects, 51 relations, valid JSON, 1865 tokens

**Objects: 15/20 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | car | yes (object 1) | car | identical | ✓ |
| 1 | road | yes (object 2) | road | identical | ✓ |
| 2 | grass | yes (object 3) | grass | identical | ✓ |
| 3 | sidewalk | yes (object 4) | curb | semantic overlap | ✓ |
| 4 | road | yes (object 5) | lane separator | mismatch | ✗ |
| 5 | license plate | yes (object 6) | license plate | identical | ✓ |
| 6 | windshield | yes (object 7) | windshield | identical | ✓ |
| 7 | headlight | yes (object 8) | headlight | identical | ✓ |
| 8 | headlight | yes (object 9) | headlight | identical | ✓ |
| 9 | grill | yes (object 10) | grille | identical | ✓ |
| 10 | driver | yes (object 11) | rearview mirror | mismatch | ✗ |
| 11 | bonnet | yes (object 12) | car hood | synonym | ✓ |
| 12 | car logo | yes (object 13) | emblem | synonym | ✓ |
| 13 | fog light | yes (object 14) | vent | mismatch | ✗ |
| 14 | fog light | yes (object 15) | vent | mismatch | ✗ |
| 15 | front bumper | yes (object 16) | bumper | hypernym/hyponym | ✓ |
| 16 | wiper | yes (object 17) | windshield wiper | identical | ✓ |
| 17 | cooling system | yes (object 18) | vent | semantic overlap | ✓ |
| 18 | side mirror | yes (object 19) | rearview mirror | synonym | ✓ |
| 19 | tree | yes (object 20) | pole | mismatch | ✗ |

**Relations: 31/51 right, triplets: 24/51 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| car #0 - on - road #1 | 0-7 | moving on (+2 more) | 0-6 | hypernym/hyponym | 0.86 | ✓ | ✓ |
| car #0 - moving along - road #1 | 0-7 | moving on (+2 more) | 0-6 | synonym | 0.86 | ✓ | ✓ |
| car #0 - traveling on - road #1 | 0-7 | moving on (+2 more) | 0-6 | hypernym/hyponym | 0.86 | ✓ | ✓ |
| car #0 - in front of - grass #2 | 0-7 | in front of (+1 more) | 0-6 | identical | 0.86 | ✓ | ✓ |
| car #0 - moving past - grass #2 | 0-7 | passing (+1 more) | 0-6 | synonym | 0.86 | ✓ | ✓ |
| car #0 - in front of - sidewalk #3 | 0-7 | in front of (+1 more) | 0-6 | identical | 0.86 | ✓ | ✓ |
| car #0 - moving past - sidewalk #3 | 0-7 | passing (+1 more) | 0-6 | synonym | 0.86 | ✓ | ✓ |
| car #0 - moving past - tree #19 | 1.5-7 | passing (+1 more) | 0-6 | synonym | 0.64 | ✓ | ✗ |
| car #0 - in front of - tree #19 | 2-7 | in front of (+1 more) | 0-6 | identical | 0.57 | ✓ | ✗ |
| car #0 - has attached - grill #9 | 0-7 | has | 0-6 | hypernym/hyponym | 0.86 | ✓ | ✓ |
| car #0 - has attached - headlight #7 | 0-7 | has | 0-6 | hypernym/hyponym | 0.86 | ✓ | ✓ |
| car #0 - has attached - bonnet #11 | 0-7 | has | 0-6 | hypernym/hyponym | 0.86 | ✓ | ✓ |
| car #0 - has attached - car logo #12 | 0-7 | has | 0-6 | hypernym/hyponym | 0.86 | ✓ | ✓ |
| car #0 - has attached - license plate #5 | 0-7 | has | 5-6 | hypernym/hyponym | 0.14 | ✗ | ✗ |
| car #0 - has attached - side mirror #18 | 0-7 | has | 0-6 | hypernym/hyponym | 0.86 | ✓ | ✓ |
| car #0 - has attached - wiper #16 | 0-7 | has | 0-6 | hypernym/hyponym | 0.86 | ✓ | ✓ |
| car #0 - has attached - front bumper #15 | 0-7 | has | 0-6 | hypernym/hyponym | 0.86 | ✓ | ✓ |
| car #0 - has attached - fog light #14 | 0-7 | has | 0-6 | hypernym/hyponym | 0.86 | ✓ | ✗ |
| car #0 - has attached - fog light #13 | 0-7 | has | 0-6 | hypernym/hyponym | 0.86 | ✓ | ✗ |
| car #0 - has attached - headlight #8 | 0-7 | has | 0-6 | hypernym/hyponym | 0.86 | ✓ | ✓ |
| road #1 - beside - sidewalk #3 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| road #1 - beside - sidewalk #3 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| sidewalk #3 - beside - grass #2 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| road #4 - beside - road #1 | 6-7 | on | 5-6 | mismatch | 0.00 | ✗ | ✗ |
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
| driver #10 - driving - car #0 | 0-7 | on | 0-6 | mismatch | 0.86 | ✗ | ✗ |
| driver #10 - inside - car #0 | 0-7 | on | 0-6 | mismatch | 0.86 | ✗ | ✗ |
| driver #10 - behind - windshield #6 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| bonnet #11 - on - car #0 | 0-7 | on | 0-6 | identical | 0.86 | ✓ | ✓ |
| bonnet #11 - above - front bumper #15 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| car logo #12 - attached to - grill #9 | 0-7 | above | 0-6 | mismatch | 0.86 | ✗ | ✗ |
| car logo #12 - on - grill #9 | 0-7 | above | 0-6 | semantic overlap | 0.86 | ✓ | ✓ |
| fog light #13 - on - car #0 | 0-7 | on | 0-6 | identical | 0.86 | ✓ | ✗ |
| fog light #13 - below - headlight #7 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| fog light #14 - on - car #0 | 0-7 | on | 0-6 | identical | 0.86 | ✓ | ✗ |
| fog light #14 - below - grill #9 | 0-7 | below | 0-6 | identical | 0.86 | ✓ | ✗ |
| front bumper #15 - on - car #0 | 0-7 | on | 0-6 | identical | 0.86 | ✓ | ✓ |
| wiper #16 - on - car #0 | 0-7 | on | 0-6 | identical | 0.86 | ✓ | ✓ |
| wiper #16 - below - windshield #6 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| side mirror #18 - on - car #0 | 0-7 | on | 0-6 | identical | 0.86 | ✓ | ✓ |
| tree #19 - on - grass #2 | 2-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #19 - behind - sidewalk #3 | 2-7 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (16): car #0 - has - windshield #6 [0-6]; car #0 - has - cooling system #17 [0-6]; car #0 - has - driver #10 [0-6]; sidewalk #3 - adjacent to - road #1 [0-6]; grass #2 - adjacent to - sidewalk #3 [0-6]; car logo #12 - on - car #0 [0-6]; cooling system #17 - on - car #0 [0-6]; front bumper #15 - below - grill #9 [0-6]; grill #9 - below - bonnet #11 [0-6]; wiper #16 - above - grill #9 [0-6]


## 241_oEkly9vzEGQ

12.67 s, 13 frames read | human: 26 objects, 31 relations | TRASER: 26 objects, 41 relations, valid JSON, 2318 tokens

**Objects: 19/26 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | bench | yes (object 2) | bench | identical | ✓ |
| 2 | ground | yes (object 3) | person | mismatch | ✗ |
| 3 | fountain | yes (object 4) | fountain | identical | ✓ |
| 4 | street | yes (object 5) | car | mismatch | ✗ |
| 5 | building | yes (object 6) | pole (uncertain) | mismatch | ✗ |
| 6 | building | yes (object 7) | tree | mismatch | ✗ |
| 7 | building | yes (object 8) | wall | semantic overlap | ✓ |
| 8 | car | yes (object 9) | car | identical | ✓ |
| 9 | car | yes (object 10) | car | identical | ✓ |
| 10 | car | yes (object 11) | car | identical | ✓ |
| 11 | tree | yes (object 12) | tree | identical | ✓ |
| 12 | garagecan | yes (object 13) | flowerpot | mismatch | ✗ |
| 13 | building | yes (object 14) | building | identical | ✓ |
| 14 | parking sign | yes (object 15) | car | mismatch | ✗ |
| 15 | bag | yes (object 16) | handbag | hypernym/hyponym | ✓ |
| 16 | hair | yes (object 17) | hair | identical | ✓ |
| 17 | coat | yes (object 18) | jacket | synonym | ✓ |
| 18 | shoes | yes (object 19) | high heel shoe | hypernym/hyponym | ✓ |
| 19 | tree | yes (object 20) | tree | identical | ✓ |
| 20 | tree | yes (object 21) | tree | identical | ✓ |
| 21 | bush | yes (object 22) | bush | identical | ✓ |
| 22 | bush | yes (object 23) | trash can (uncertain) | mismatch | ✗ |
| 23 | bush | yes (object 24) | bush | identical | ✓ |
| 24 | plant | yes (object 25) | plant | identical | ✓ |
| 25 | plant | yes (object 26) | potted plant | hypernym/hyponym | ✓ |

**Relations: 11/31 right, triplets: 11/31 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - wearing - coat #17 | 0-13 | wearing | 0-14 | identical | 0.93 | ✓ | ✓ |
| person #0 - carrying - bag #15 | 0-13 | carrying | 0-14 | identical | 0.93 | ✓ | ✓ |
| person #0 - on - ground #2 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - walking across - ground #2 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - wearing - shoes #18 | 0-13 | wearing | 0-14 | identical | 0.93 | ✓ | ✓ |
| person #0 - behind - fountain #3 | 0-13 | near (+2 more) | 0-14 | hypernym/hyponym | 0.93 | ✓ | ✓ |
| person #0 - beside - fountain #3 | 0-13 | near (+2 more) | 0-14 | hypernym/hyponym | 0.93 | ✓ | ✓ |
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

**Objects: 27/56 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | printer | yes (object 1) | printer | identical | ✓ |
| 1 | counter | yes (object 2) | desk (uncertain) | semantic overlap | ✓ |
| 2 | wall | yes (object 3) | mirror | mismatch | ✗ |
| 3 | light | yes (object 4) | chandelier | hypernym/hyponym | ✓ |
| 4 | furniture | yes (object 5) | chair | hypernym/hyponym | ✓ |
| 5 | fireplace | yes (object 6) | fireplace | identical | ✓ |
| 6 | cabinet | yes (object 7) | door | semantic overlap | ✓ |
| 7 | monitor | yes (object 8) | computer monitor | hypernym/hyponym | ✓ |
| 8 | monitor | yes (object 9) | computer monitor | hypernym/hyponym | ✓ |
| 9 | counter | yes (object 10) | desk | semantic overlap | ✓ |
| 10 | printer | yes (object 11) | printer | identical | ✓ |
| 11 | pillar | yes (object 12) | column | synonym | ✓ |
| 12 | person | yes (object 13) | person | identical | ✓ |
| 13 | person | yes (object 14) | person | identical | ✓ |
| 14 | cpu | yes (object 15) | printer | mismatch | ✗ |
| 15 | counter | yes (object 16) | desk | semantic overlap | ✓ |
| 16 | device | yes (object 17) | speaker (uncertain) | hypernym/hyponym | ✓ |
| 17 | light | yes (object 18) | ceiling light fixture (uncertain) | hypernym/hyponym | ✓ |
| 18 | light | yes (object 19) | ceiling light fixture (uncertain) | hypernym/hyponym | ✓ |
| 19 | light | yes (object 20) | ceiling light fixture (uncertain) | hypernym/hyponym | ✓ |
| 20 | light | yes (object 21) | ceiling light fixture (uncertain) | hypernym/hyponym | ✓ |
| 21 | light | yes (object 22) | ceiling light fixture (uncertain) | hypernym/hyponym | ✓ |
| 22 | wall | yes (object 23) | wall panel | hypernym/hyponym | ✓ |
| 23 | wall | yes (object 24) | ceiling beam (uncertain) | mismatch | ✗ |
| 24 | wall | yes (object 25) | wall panel | hypernym/hyponym | ✓ |
| 25 | wall | yes (object 26) | ceiling beam (uncertain) | mismatch | ✗ |
| 26 | household material | yes (object 27) | chair | mismatch | ✗ |
| 27 | lights | yes (object 28) | ceiling beam (uncertain) | mismatch | ✗ |
| 28 | chandelier | yes (object 29) | lamp | hypernym/hyponym | ✓ |
| 29 | wall frame | yes (object 30) | printer | mismatch | ✗ |
| 30 | wall frame | yes (object 31) | chair | mismatch | ✗ |
| 31 | document | yes (object 32) | chair | mismatch | ✗ |
| 32 | document | yes (object 33) | paper (uncertain) | synonym | ✓ |
| 33 | decor | yes (object 34) | cellular telephone (uncertain) | mismatch | ✗ |
| 34 | lights | yes (object 35) | light fixture (uncertain) | synonym | ✓ |
| 35 | ceiling | yes (object 36) | ceiling beam (uncertain) | hypernym/hyponym | ✓ |
| 36 | decor | yes (object 37) | chair | mismatch | ✗ |
| 37 | decor | yes (object 38) | television set | mismatch | ✗ |
| 38 | decor | yes (object 39) | chair | mismatch | ✗ |
| 39 | light | yes (object 40) | lamp | hypernym/hyponym | ✓ |
| 40 | light | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | light | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | display cabinet | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | hair | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | glasses | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | shirt | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | hair | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | shirt | no: after the first 40 | - | no label from TRASER | ✗ |
| 48 | face | no: after the first 40 | - | no label from TRASER | ✗ |
| 49 | light | no: after the first 40 | - | no label from TRASER | ✗ |
| 50 | fireplace mantle | no: after the first 40 | - | no label from TRASER | ✗ |
| 51 | wall frame | no: after the first 40 | - | no label from TRASER | ✗ |
| 52 | decor | no: after the first 40 | - | no label from TRASER | ✗ |
| 53 | painting | no: after the first 40 | - | no label from TRASER | ✗ |
| 54 | decor | no: after the first 40 | - | no label from TRASER | ✗ |
| 55 | decor | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 6/36 right, triplets: 6/36 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| printer #0 - on - counter #9 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ✓ |
| light #3 - under - chandelier #28 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #3 - above - furniture #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| furniture #4 - in front of - wall #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| fireplace #5 - attached to - wall #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| monitor #7 - on - counter #15 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| monitor #7 - behind - counter #9 | 0-23 | on | 0-24 | mismatch | 0.96 | ✗ | ✗ |
| monitor #8 - on - counter #15 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| monitor #8 - behind - counter #9 | 0-23 | on | 0-24 | mismatch | 0.96 | ✗ | ✗ |
| counter #9 - in front of - wall #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| printer #10 - on - counter #9 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ✓ |
| pillar #11 - in front of - wall #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| pillar #11 - under - chandelier #28 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #12 - talking with - person #13 | 0-23 | working with | 0-24 | semantic overlap | 0.96 | ✓ | ✓ |
| person #12 - looking at - person #13 | 6-14, 16-23 | working with | 0-24 | mismatch | 0.62 | ✗ | ✗ |
| person #12 - looking at - monitor #8 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #12 - wearing - glasses #44 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #12 - wearing - shirt #45 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #12 - behind - counter #15 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #12 - in front of - wall #22 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #13 - looking at - person #12 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #13 - wearing - shirt #47 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #13 - in front of - wall #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #13 - behind - counter #9 | 0-23 | behind | 0-24 | identical | 0.96 | ✓ | ✓ |
| cpu #14 - under - counter #15 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| counter #15 - behind - counter #9 | 0-23 | behind | 0-24 | identical | 0.96 | ✓ | ✓ |
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

**Objects: 26/30 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | window | yes (object 1) | window | identical | ✓ |
| 1 | person | yes (object 2) | person | identical | ✓ |
| 2 | ledge | yes (object 3) | ledge | identical | ✓ |
| 3 | wall | yes (object 4) | brick wall | hypernym/hyponym | ✓ |
| 4 | spray | yes (object 5) | bottle | semantic overlap | ✓ |
| 5 | wall | yes (object 6) | door frame (uncertain) | mismatch | ✗ |
| 6 | plants | yes (object 7) | vase | mismatch | ✗ |
| 7 | window | yes (object 8) | window | identical | ✓ |
| 8 | home material | yes (object 9) | bottle | mismatch | ✗ |
| 9 | shirt | yes (object 10) | jersey | hypernym/hyponym | ✓ |
| 10 | wall | yes (object 11) | brick wall | hypernym/hyponym | ✓ |
| 11 | wall | yes (object 12) | brick wall | hypernym/hyponym | ✓ |
| 12 | glass | yes (object 13) | window frame (uncertain) | semantic overlap | ✓ |
| 13 | plant | yes (object 14) | flower arrangement | hypernym/hyponym | ✓ |
| 14 | vase planter | yes (object 15) | vase | hypernym/hyponym | ✓ |
| 15 | plant | yes (object 16) | flower arrangement | hypernym/hyponym | ✓ |
| 16 | glass | yes (object 17) | window | semantic overlap | ✓ |
| 17 | glass | yes (object 18) | window | semantic overlap | ✓ |
| 18 | glass | yes (object 19) | window | semantic overlap | ✓ |
| 19 | glass | yes (object 20) | window | semantic overlap | ✓ |
| 20 | glass | yes (object 21) | window | semantic overlap | ✓ |
| 21 | glass | yes (object 22) | window frame (uncertain) | semantic overlap | ✓ |
| 22 | glass | yes (object 23) | window | semantic overlap | ✓ |
| 23 | glass | yes (object 24) | pole (uncertain) | mismatch | ✗ |
| 24 | shirt | yes (object 25) | jersey | hypernym/hyponym | ✓ |
| 25 | jean | yes (object 26) | jeans (uncertain) | identical | ✓ |
| 26 | hand | yes (object 27) | arm | semantic overlap | ✓ |
| 27 | hair | yes (object 28) | hairline | semantic overlap | ✓ |
| 28 | glass | yes (object 29) | spectacles | synonym | ✓ |
| 29 | hand | yes (object 30) | hand | identical | ✓ |

**Relations: 9/25 right, triplets: 8/25 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| window #0 - contain - glass #22 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #0 - in - wall #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #0 - above - ledge #2 | 0-23 | above | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #1 - hold - spray #4 | 0-23 | holding (+2 more) | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #1 - wear - shirt #9 | 0-23 | wearing | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #1 - wear - jean #25 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - look at - window #0 | 0-2, 4-15 | in front of | 0-24 | mismatch | 0.54 | ✗ | ✗ |
| person #1 - repair - window #0 | 0-14 | in front of | 0-24 | mismatch | 0.58 | ✗ | ✗ |
| person #1 - in front of - window #0 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #1 - in front of - wall #3 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| ledge #2 - in front of - wall #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| spray #4 - above - ledge #2 | 0-23 | above | 0-24 | identical | 0.96 | ✓ | ✓ |
| window #7 - in - wall #5 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| home material #8 - on - ledge #2 | 5.5-23 | above | 0-24 | semantic overlap | 0.73 | ✓ | ✗ |
| shirt #9 - on - person #1 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ✓ |
| plant #13 - above - plant #15 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| vase planter #14 - hold - plant #15 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| vase planter #14 - in front of - wall #5 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| vase planter #14 - below - window #7 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| plant #15 - in - vase planter #14 | 0-23 | above | 0-24 | mismatch | 0.96 | ✗ | ✗ |
| glass #16 - in - window #7 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| glass #21 - in - window #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| glass #22 - in - window #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| jean #25 - on - person #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| hair #27 - on - person #1 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (36): person #1 - wearing - shirt #24 [0-24]; person #1 - in front of - window #7 [0-24]; person #1 - in front of - glass #16 [0-24]; person #1 - in front of - glass #17 [0-24]; person #1 - in front of - glass #18 [0-24]; person #1 - in front of - glass #19 [0-24]; person #1 - in front of - glass #20 [0-24]; person #1 - in front of - glass #22 [0-24]; person #1 - in front of - wall #10 [0-24]; person #1 - in front of - wall #11 [0-24]


## 276_3HgBHBOnpbg

7.5 s, 8 frames read | human: 40 objects, 55 relations | TRASER: 11 objects, 0 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 7/40 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | man | yes (object 1) | person | hypernym/hyponym | ✓ |
| 1 | woman | yes (object 2) | person | hypernym/hyponym | ✓ |
| 2 | car | yes (object 3) | sedan | hypernym/hyponym | ✓ |
| 3 | car | yes (object 4) | car | identical | ✓ |
| 4 | building | yes (object 5) | building | identical | ✓ |
| 5 | building | yes (object 6) | tree | mismatch | ✗ |
| 6 | road | yes (object 7) | car | mismatch | ✗ |
| 7 | sky | yes (object 8) | streetlight | mismatch | ✗ |
| 8 | building | yes (object 9) | building | identical | ✓ |
| 9 | shop or building | yes (object 10) | storefront | hypernym/hyponym | ✓ |
| 10 | sidewalk | yes (object 11) | person | mismatch | ✗ |
| 11 | machine | yes (object 12) | - | no label from TRASER | ✗ |
| 12 | bag | yes (object 13) | - | no label from TRASER | ✗ |
| 13 | bag | yes (object 14) | - | no label from TRASER | ✗ |
| 14 | wall | yes (object 15) | - | no label from TRASER | ✗ |
| 15 | wall | yes (object 16) | - | no label from TRASER | ✗ |
| 16 | tree | yes (object 17) | - | no label from TRASER | ✗ |
| 17 | plant | yes (object 18) | - | no label from TRASER | ✗ |
| 18 | car | yes (object 19) | - | no label from TRASER | ✗ |
| 19 | wheel | yes (object 20) | - | no label from TRASER | ✗ |
| 20 | light | yes (object 21) | - | no label from TRASER | ✗ |
| 21 | light | yes (object 22) | - | no label from TRASER | ✗ |
| 22 | window | yes (object 23) | - | no label from TRASER | ✗ |
| 23 | backpack | yes (object 24) | - | no label from TRASER | ✗ |
| 24 | window | yes (object 25) | - | no label from TRASER | ✗ |
| 25 | window | yes (object 26) | - | no label from TRASER | ✗ |
| 26 | door | yes (object 27) | - | no label from TRASER | ✗ |
| 27 | pants | yes (object 28) | - | no label from TRASER | ✗ |
| 28 | shorts | yes (object 29) | - | no label from TRASER | ✗ |
| 29 | clothes | yes (object 30) | - | no label from TRASER | ✗ |
| 30 | T-shirt | yes (object 31) | - | no label from TRASER | ✗ |
| 31 | wheel | yes (object 32) | - | no label from TRASER | ✗ |
| 32 | window | yes (object 33) | - | no label from TRASER | ✗ |
| 33 | side mirror | yes (object 34) | - | no label from TRASER | ✗ |
| 34 | plate | yes (object 35) | - | no label from TRASER | ✗ |
| 35 | door | yes (object 36) | - | no label from TRASER | ✗ |
| 36 | wall | yes (object 37) | - | no label from TRASER | ✗ |
| 37 | shoe | yes (object 38) | - | no label from TRASER | ✗ |
| 38 | shoe | yes (object 39) | - | no label from TRASER | ✗ |
| 39 | shoe | yes (object 40) | - | no label from TRASER | ✗ |

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

**Objects: 21/89 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | sky | yes (object 1) | sky | identical | ✓ |
| 1 | person | yes (object 2) | person | identical | ✓ |
| 2 | person | yes (object 3) | person | identical | ✓ |
| 3 | golf extract | yes (object 4) | golf club | semantic overlap | ✓ |
| 4 | golf cart | yes (object 5) | cart | hypernym/hyponym | ✓ |
| 5 | basket of golfs | yes (object 6) | basketball hoop | mismatch | ✗ |
| 6 | golf ball | yes (object 7) | golf ball | identical | ✓ |
| 7 | golf ball | yes (object 8) | golf ball | identical | ✓ |
| 8 | golf ball | yes (object 9) | golf ball | identical | ✓ |
| 9 | golf ball | yes (object 10) | golf ball | identical | ✓ |
| 10 | golf ball | yes (object 11) | golf ball | identical | ✓ |
| 11 | golf ball | yes (object 12) | golf ball | identical | ✓ |
| 12 | golf ball | yes (object 13) | golf ball | identical | ✓ |
| 13 | golf ball | yes (object 14) | golf ball | identical | ✓ |
| 14 | golf ball | yes (object 15) | golf ball | identical | ✓ |
| 15 | golf ball | yes (object 16) | golf ball | identical | ✓ |
| 16 | golf ball | yes (object 17) | golf ball | identical | ✓ |
| 17 | golf ball | yes (object 18) | golf ball | identical | ✓ |
| 18 | golf ball | yes (object 19) | golf ball | identical | ✓ |
| 19 | umbrella | yes (object 20) | tree | mismatch | ✗ |
| 20 | person | yes (object 21) | golf cart | mismatch | ✗ |
| 21 | person | yes (object 22) | golf cart | mismatch | ✗ |
| 22 | car | yes (object 23) | golf cart | semantic overlap | ✓ |
| 23 | house | yes (object 24) | golf cart | mismatch | ✗ |
| 24 | metal | yes (object 25) | golf cart | mismatch | ✗ |
| 25 | house | yes (object 26) | house | identical | ✓ |
| 26 | background | yes (object 27) | grass | mismatch | ✗ |
| 27 | barricade | yes (object 28) | golf cart | mismatch | ✗ |
| 28 | tree | yes (object 29) | trees | identical | ✓ |
| 29 | barricade | yes (object 30) | golf cart | mismatch | ✗ |
| 30 | barricade | yes (object 31) | golf cart | mismatch | ✗ |
| 31 | barricade | yes (object 32) | golf cart | mismatch | ✗ |
| 32 | barricade | yes (object 33) | golf cart | mismatch | ✗ |
| 33 | barricade | yes (object 34) | golf cart | mismatch | ✗ |
| 34 | barricade | yes (object 35) | golf cart | mismatch | ✗ |
| 35 | barricade | yes (object 36) | golf cart | mismatch | ✗ |
| 36 | barricade | yes (object 37) | golf cart | mismatch | ✗ |
| 37 | barricade | yes (object 38) | golf cart | mismatch | ✗ |
| 38 | crowd | yes (object 39) | golf cart | mismatch | ✗ |
| 39 | floor | yes (object 40) | golf cart | mismatch | ✗ |
| 40 | grass | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | floor | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | grass | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | grass | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | grass | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | post | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | grass | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | cart | no: after the first 40 | - | no label from TRASER | ✗ |
| 48 | person | no: after the first 40 | - | no label from TRASER | ✗ |
| 49 | golf balls | no: after the first 40 | - | no label from TRASER | ✗ |
| 50 | basket | no: after the first 40 | - | no label from TRASER | ✗ |
| 51 | cap | no: after the first 40 | - | no label from TRASER | ✗ |
| 52 | face | no: after the first 40 | - | no label from TRASER | ✗ |
| 53 | shirt | no: after the first 40 | - | no label from TRASER | ✗ |
| 54 | hand | no: after the first 40 | - | no label from TRASER | ✗ |
| 55 | bag | no: after the first 40 | - | no label from TRASER | ✗ |
| 56 | picker | no: after the first 40 | - | no label from TRASER | ✗ |
| 57 | trouser | no: after the first 40 | - | no label from TRASER | ✗ |
| 58 | shoe | no: after the first 40 | - | no label from TRASER | ✗ |
| 59 | shoe | no: after the first 40 | - | no label from TRASER | ✗ |
| 60 | hand | no: after the first 40 | - | no label from TRASER | ✗ |
| 61 | shoe | no: after the first 40 | - | no label from TRASER | ✗ |
| 62 | shoe | no: after the first 40 | - | no label from TRASER | ✗ |
| 63 | shirt | no: after the first 40 | - | no label from TRASER | ✗ |
| 64 | trouser | no: after the first 40 | - | no label from TRASER | ✗ |
| 65 | face | no: after the first 40 | - | no label from TRASER | ✗ |
| 66 | hand | no: after the first 40 | - | no label from TRASER | ✗ |
| 67 | hand | no: after the first 40 | - | no label from TRASER | ✗ |
| 68 | golf materials | no: after the first 40 | - | no label from TRASER | ✗ |
| 69 | job cart | no: after the first 40 | - | no label from TRASER | ✗ |
| 70 | stairs | no: after the first 40 | - | no label from TRASER | ✗ |
| 71 | stairs | no: after the first 40 | - | no label from TRASER | ✗ |
| 72 | roof | no: after the first 40 | - | no label from TRASER | ✗ |
| 73 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 74 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 75 | pavement | no: after the first 40 | - | no label from TRASER | ✗ |
| 76 | barricade | no: after the first 40 | - | no label from TRASER | ✗ |
| 77 | pavement | no: after the first 40 | - | no label from TRASER | ✗ |
| 78 | barricade | no: after the first 40 | - | no label from TRASER | ✗ |
| 79 | barricade | no: after the first 40 | - | no label from TRASER | ✗ |
| 80 | pavement | no: after the first 40 | - | no label from TRASER | ✗ |
| 81 | barricade | no: after the first 40 | - | no label from TRASER | ✗ |
| 82 | pavement | no: after the first 40 | - | no label from TRASER | ✗ |
| 83 | barricade | no: after the first 40 | - | no label from TRASER | ✗ |
| 84 | barricade | no: after the first 40 | - | no label from TRASER | ✗ |
| 85 | barricade | no: after the first 40 | - | no label from TRASER | ✗ |
| 86 | barricade | no: after the first 40 | - | no label from TRASER | ✗ |
| 87 | barricade | no: after the first 40 | - | no label from TRASER | ✗ |
| 88 | tyre | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 6/47 right, triplets: 6/47 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #1 - on - grass #46 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - in front of - golf cart #4 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #1 - in front of - job cart #69 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - holds - golf extract #3 | 0-4, 7.5-23 | holding (+3 more) | 0-24 | identical | 0.81 | ✓ | ✓ |
| person #1 - uses - golf extract #3 | 0-4, 7.5-23 | holding (+3 more) | 0-24 | semantic overlap | 0.81 | ✓ | ✓ |
| person #1 - hands - golf extract #3 | 1-4 | holding (+3 more) | 0-24 | semantic overlap | 0.12 | ✗ | ✗ |
| person #1 - approaches - basket of golfs #5 | 5-9 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - wears - cap #51 | 0-12 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - talks to - person #2 | 0-5, 10-13 | near | 0-24 | mismatch | 0.33 | ✗ | ✗ |
| person #1 - beside - person #2 | 0-23 | near | 0-24 | hypernym/hyponym | 0.96 | ✓ | ✓ |
| person #2 - on - grass #46 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - in front of - golf cart #4 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #2 - in front of - job cart #69 | 0-15, 19-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - holds - golf extract #3 | 3-23 | holding (+3 more) | 0-24 | identical | 0.83 | ✓ | ✓ |
| person #2 - uses - golf extract #3 | 15-23 | holding (+3 more) | 0-24 | semantic overlap | 0.33 | ✗ | ✗ |
| golf extract #3 - above - grass #46 | 18.5-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| golf extract #3 - moves toward - person #2 | 1-5 | overlapping | 0-24 | mismatch | 0.17 | ✗ | ✗ |
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

**Objects: 17/58 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | boat | yes (object 1) | raft | hypernym/hyponym | ✓ |
| 1 | bucket | yes (object 2) | person | mismatch | ✗ |
| 2 | bucket | yes (object 3) | person | mismatch | ✗ |
| 3 | bucket | yes (object 4) | life jacket (uncertain) | mismatch | ✗ |
| 4 | person | yes (object 5) | person | identical | ✓ |
| 5 | person | yes (object 6) | person | identical | ✓ |
| 6 | person | yes (object 7) | person | identical | ✓ |
| 7 | person | yes (object 8) | person | identical | ✓ |
| 8 | pool | yes (object 9) | raft | mismatch | ✗ |
| 9 | person | yes (object 10) | person | identical | ✓ |
| 10 | person | yes (object 11) | person | identical | ✓ |
| 11 | bucket | yes (object 12) | person | mismatch | ✗ |
| 12 | bucket | yes (object 13) | life jacket (uncertain) | mismatch | ✗ |
| 13 | wall | yes (object 14) | wall | identical | ✓ |
| 14 | wall | yes (object 15) | pillar | mismatch | ✗ |
| 15 | wall | yes (object 16) | pillar | mismatch | ✗ |
| 16 | floor | yes (object 17) | wall | mismatch | ✗ |
| 17 | swim ring | yes (object 18) | signboard | mismatch | ✗ |
| 18 | wall | yes (object 19) | brick wall | hypernym/hyponym | ✓ |
| 19 | grass | yes (object 20) | pole (uncertain) | mismatch | ✗ |
| 20 | person | yes (object 21) | person | identical | ✓ |
| 21 | person | yes (object 22) | person | identical | ✓ |
| 22 | window | yes (object 23) | window | identical | ✓ |
| 23 | storage reel | yes (object 24) | ladder | mismatch | ✗ |
| 24 | floatation device | yes (object 25) | pillar | mismatch | ✗ |
| 25 | poolside step | yes (object 26) | ladder | semantic overlap | ✓ |
| 26 | door | yes (object 27) | window | semantic overlap | ✓ |
| 27 | window | yes (object 28) | window | identical | ✓ |
| 28 | chair | yes (object 29) | vent (uncertain) | mismatch | ✗ |
| 29 | door | yes (object 30) | door | identical | ✓ |
| 30 | shelf | yes (object 31) | vent (uncertain) | mismatch | ✗ |
| 31 | poolside step | yes (object 32) | fan | mismatch | ✗ |
| 32 | fan | yes (object 33) | fan | identical | ✓ |
| 33 | storage reel center | yes (object 34) | ladder | mismatch | ✗ |
| 34 | wheel | yes (object 35) | ladder | mismatch | ✗ |
| 35 | wheel | yes (object 36) | ladder | mismatch | ✗ |
| 36 | tyre | yes (object 37) | person | mismatch | ✗ |
| 37 | tyre | yes (object 38) | person | mismatch | ✗ |
| 38 | tyre | yes (object 39) | trash can (uncertain) | mismatch | ✗ |
| 39 | tyre | yes (object 40) | trash can (uncertain) | mismatch | ✗ |
| 40 | head | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | head | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | head | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | head | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | head | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | head | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | head | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | life jacket | no: after the first 40 | - | no label from TRASER | ✗ |
| 48 | life jacket | no: after the first 40 | - | no label from TRASER | ✗ |
| 49 | life jacket | no: after the first 40 | - | no label from TRASER | ✗ |
| 50 | life jacket | no: after the first 40 | - | no label from TRASER | ✗ |
| 51 | life jacket | no: after the first 40 | - | no label from TRASER | ✗ |
| 52 | life jacket | no: after the first 40 | - | no label from TRASER | ✗ |
| 53 | life jacket | no: after the first 40 | - | no label from TRASER | ✗ |
| 54 | shirt | no: after the first 40 | - | no label from TRASER | ✗ |
| 55 | shirt | no: after the first 40 | - | no label from TRASER | ✗ |
| 56 | shirt | no: after the first 40 | - | no label from TRASER | ✗ |
| 57 | short | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 10/50 right, triplets: 9/50 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| boat #0 - moving on - pool #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| boat #0 - in - pool #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| boat #0 - in front of - wall #13 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✓ |
| bucket #1 - in - boat #0 | 0-8 | inside | 0-9 | synonym | 0.89 | ✓ | ✗ |
| bucket #3 - in - boat #0 | 3-5, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - wearing - life jacket #48 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - aboard - boat #0 | 0-8 | inside | 0-9 | synonym | 0.89 | ✓ | ✓ |
| person #4 - in - boat #0 | 0-8 | inside | 0-9 | synonym | 0.89 | ✓ | ✓ |
| person #4 - holding - bucket #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - wearing - life jacket #49 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - aboard - boat #0 | 0-8 | inside | 0-9 | synonym | 0.89 | ✓ | ✓ |
| person #5 - in - boat #0 | 0-8 | inside | 0-9 | synonym | 0.89 | ✓ | ✓ |
| person #5 - splashing with - bucket #2 | 1-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - holding - bucket #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #6 - holding - bucket #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #6 - splashing with - bucket #3 | 4.5-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #6 - wearing - life jacket #51 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #6 - aboard - boat #0 | 0-8 | inside | 0-9 | synonym | 0.89 | ✓ | ✓ |
| person #6 - in - boat #0 | 0-8 | inside | 0-9 | synonym | 0.89 | ✓ | ✓ |
| person #7 - wearing - life jacket #50 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #7 - aboard - boat #0 | 0-8 | inside | 0-9 | synonym | 0.89 | ✓ | ✓ |
| person #7 - in - boat #0 | 0-8 | inside | 0-9 | synonym | 0.89 | ✓ | ✓ |
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

**Objects: 28/42 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | referee | yes (object 1) | person | hypernym/hyponym | ✓ |
| 1 | dancer | yes (object 2) | person | hypernym/hyponym | ✓ |
| 2 | dancer | yes (object 3) | person | hypernym/hyponym | ✓ |
| 3 | dance floor | yes (object 4) | dancer | mismatch | ✗ |
| 4 | trash can | yes (object 5) | banner | mismatch | ✗ |
| 5 | background floor | yes (object 6) | stage | semantic overlap | ✓ |
| 6 | country logo | yes (object 7) | signboard | semantic overlap | ✓ |
| 7 | country logo | yes (object 8) | signboard | semantic overlap | ✓ |
| 8 | country logo | yes (object 9) | signboard | semantic overlap | ✓ |
| 9 | country logo | yes (object 10) | signboard | semantic overlap | ✓ |
| 10 | flower vase | yes (object 11) | signboard | mismatch | ✗ |
| 11 | country logo | yes (object 12) | signboard | semantic overlap | ✓ |
| 12 | flower vase | yes (object 13) | flower arrangement | semantic overlap | ✓ |
| 13 | country logo | yes (object 14) | signboard | semantic overlap | ✓ |
| 14 | flower vase | yes (object 15) | flower arrangement | semantic overlap | ✓ |
| 15 | bottle water | yes (object 16) | bottle | identical | ✓ |
| 16 | flower vase | yes (object 17) | flower arrangement | semantic overlap | ✓ |
| 17 | logo | yes (object 18) | television set | mismatch | ✗ |
| 18 | flower vase | yes (object 19) | flower arrangement | semantic overlap | ✓ |
| 19 | flower vase | yes (object 20) | flower arrangement | semantic overlap | ✓ |
| 20 | flower vase | yes (object 21) | flower arrangement | semantic overlap | ✓ |
| 21 | bottle | yes (object 22) | bottle | identical | ✓ |
| 22 | cup | yes (object 23) | tablecloth | mismatch | ✗ |
| 23 | paper | yes (object 24) | tablecloth | mismatch | ✗ |
| 24 | paper | yes (object 25) | tablecloth | mismatch | ✗ |
| 25 | bottle water | yes (object 26) | chair | mismatch | ✗ |
| 26 | bottle water | yes (object 27) | bottle | identical | ✓ |
| 27 | table | yes (object 28) | banner | mismatch | ✗ |
| 28 | face | yes (object 29) | person | hypernym/hyponym | ✓ |
| 29 | hair | yes (object 30) | hair | identical | ✓ |
| 30 | skirt | yes (object 31) | skirt | identical | ✓ |
| 31 | hand | yes (object 32) | handbag | mismatch | ✗ |
| 32 | hand | yes (object 33) | handbag | mismatch | ✗ |
| 33 | leg | yes (object 34) | legs (uncertain) | identical | ✓ |
| 34 | leg | yes (object 35) | legs (uncertain) | identical | ✓ |
| 35 | shirt | yes (object 36) | dress | semantic overlap | ✓ |
| 36 | head | yes (object 37) | person | mismatch | ✗ |
| 37 | jacket | yes (object 38) | suit jacket | hypernym/hyponym | ✓ |
| 38 | shirt | yes (object 39) | suit jacket | semantic overlap | ✓ |
| 39 | trouser | yes (object 40) | trousers | identical | ✓ |
| 40 | head | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | shoes | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 9/41 right, triplets: 7/41 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| referee #0 - on - dance floor #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| referee #0 - in front of - dancer #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| referee #0 - in front of - dancer #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| referee #0 - wears - jacket #37 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| dancer #1 - on - dance floor #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| dancer #1 - in front of - table #27 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✗ |
| dancer #1 - dances with - dancer #2 | 0-23 | dancing with (+2 more) | 0-24 | identical | 0.96 | ✓ | ✓ |
| dancer #1 - moves with - dancer #2 | 0-23 | moving with (+2 more) | 0-24 | identical | 0.96 | ✓ | ✓ |
| dancer #1 - performs routine with - dancer #2 | 0-23 | dancing with (+2 more) | 0-24 | semantic overlap | 0.96 | ✓ | ✓ |
| dancer #1 - overlapping - dancer #2 | 13.5-20.5 | dancing with (+2 more) | 0-24 | mismatch | 0.29 | ✗ | ✗ |
| dancer #1 - wears - skirt #30 | 0-23 | wearing | 0-24 | identical | 0.96 | ✓ | ✓ |
| dancer #1 - wears - shirt #35 | 0-23 | wearing | 0-24 | identical | 0.96 | ✓ | ✓ |
| dancer #2 - on - dance floor #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| dancer #2 - in front of - table #27 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✗ |
| dancer #2 - follows - dancer #1 | 19-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| dancer #2 - holds - dancer #1 | 12-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| dancer #2 - approaches - dancer #1 | 0-12 | nothing for this pair | - | - | - | ✗ | ✗ |
| dancer #2 - wears - shirt #38 | 0-23 | wearing | 0-24 | identical | 0.96 | ✓ | ✓ |
| dancer #2 - wears - trouser #39 | 0-23 | wearing | 0-24 | identical | 0.96 | ✓ | ✓ |
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

**Objects: 12/14 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | clothes | yes (object 2) | garment (uncertain) | synonym | ✓ |
| 2 | clothes | yes (object 3) | garment (uncertain) | synonym | ✓ |
| 3 | clothes | yes (object 4) | garment (uncertain) | synonym | ✓ |
| 4 | closet | yes (object 5) | door frame (uncertain) | semantic overlap | ✓ |
| 5 | closet divider | yes (object 6) | pole (uncertain) | semantic overlap | ✓ |
| 6 | closet divider | yes (object 7) | door frame (uncertain) | semantic overlap | ✓ |
| 7 | closet shelf | yes (object 8) | drawer (uncertain) | semantic overlap | ✓ |
| 8 | hair | yes (object 9) | hair | identical | ✓ |
| 9 | face | yes (object 10) | person | hypernym/hyponym | ✓ |
| 10 | hand | yes (object 11) | arm | semantic overlap | ✓ |
| 11 | shoulder | yes (object 12) | tank top | mismatch | ✗ |
| 12 | shirt | yes (object 13) | tank top | hypernym/hyponym | ✓ |
| 13 | plywood | yes (object 14) | fabric (uncertain) | mismatch | ✗ |

**Relations: 1/20 right, triplets: 1/20 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - looks at - clothes #1 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - touches - clothes #1 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - moves leftward - clothes #1 | 2-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - wears - shirt #12 | 0-5 | wearing (+1 more) | 0-6 | identical | 0.83 | ✓ | ✓ |
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
| shoulder #11 - below - face #9 | 0-5 | overlapping | 0-6 | mismatch | 0.83 | ✗ | ✗ |
| shirt #12 - below - face #9 | 0-5 | overlapping | 0-6 | mismatch | 0.83 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (15): person #0 - wearing - shoulder #11 [0-6]; person #0 - in front of - shoulder #11 [0-6]; person #0 - has - hair #8 [0-6]; person #0 - in front of - hair #8 [0-6]; person #0 - has - hand #10 [0-6]; person #0 - in front of - hand #10 [0-6]; person #0 - looking at - face #9 [0-6]; person #0 - in front of - face #9 [0-6]; shoulder #11 - overlapping - shirt #12 [0-6]; hair #8 - overlapping - shoulder #11 [0-6]


## 359_4ZPKJtcNGZE

22.67 s, 23 frames read | human: 27 objects, 20 relations | TRASER: 27 objects, 19 relations, valid JSON, 1876 tokens

**Objects: 18/27 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | grass | yes (object 1) | dog | mismatch | ✗ |
| 1 | grass | yes (object 2) | dog | mismatch | ✗ |
| 2 | drainage | yes (object 3) | water | mismatch | ✗ |
| 3 | tractor | yes (object 4) | bulldozer | semantic overlap | ✓ |
| 4 | trees | yes (object 5) | plant | hypernym/hyponym | ✓ |
| 5 | rod | yes (object 6) | machine part (uncertain) | hypernym/hyponym | ✓ |
| 6 | rod | yes (object 7) | machine component (uncertain) | hypernym/hyponym | ✓ |
| 7 | rod | yes (object 8) | pipe (uncertain) | semantic overlap | ✓ |
| 8 | stick | yes (object 9) | log (uncertain) | semantic overlap | ✓ |
| 9 | tyre | yes (object 10) | wheel | synonym | ✓ |
| 10 | rod | yes (object 11) | pipe (uncertain) | semantic overlap | ✓ |
| 11 | excavator arm | yes (object 12) | pipe (uncertain) | mismatch | ✗ |
| 12 | excavator boom arm | yes (object 13) | blade (uncertain) | mismatch | ✗ |
| 13 | tire | yes (object 14) | wheel | semantic overlap | ✓ |
| 14 | boom cylinder | yes (object 15) | pipe (uncertain) | semantic overlap | ✓ |
| 15 | steering wheel | yes (object 16) | pipe (uncertain) | mismatch | ✗ |
| 16 | valve | yes (object 17) | pipe (uncertain) | semantic overlap | ✓ |
| 17 | rock | yes (object 18) | rock | identical | ✓ |
| 18 | rod | yes (object 19) | pole (uncertain) | synonym | ✓ |
| 19 | excavator boom hinge | yes (object 20) | pipe (uncertain) | mismatch | ✗ |
| 20 | rod | yes (object 21) | pipe (uncertain) | semantic overlap | ✓ |
| 21 | rod | yes (object 22) | pipe (uncertain) | semantic overlap | ✓ |
| 22 | rod | yes (object 23) | pipe (uncertain) | semantic overlap | ✓ |
| 23 | rod | yes (object 24) | pipe (uncertain) | semantic overlap | ✓ |
| 24 | dashboard | yes (object 25) | pipe (uncertain) | mismatch | ✗ |
| 25 | component | yes (object 26) | vent (uncertain) | mismatch | ✗ |
| 26 | rod | yes (object 27) | pipe (uncertain) | semantic overlap | ✓ |

**Relations: 3/20 right, triplets: 2/20 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| drainage #2 - adjacent to - grass #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| drainage #2 - below - grass #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| drainage #2 - adjacent to - grass #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| drainage #2 - below - grass #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tractor #3 - on - grass #0 | 8-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tractor #3 - in front of - trees #4 | 8-23 | in front of | 8-24 | identical | 0.94 | ✓ | ✓ |
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
| rock #17 - above - drainage #2 | 6-23 | near | 7-24 | hypernym/hyponym | 0.89 | ✓ | ✗ |
| rock #17 - in front of - tractor #3 | 8-23 | near | 8-24 | hypernym/hyponym | 0.94 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (16): grass #0 - approaches - drainage #2 [0-3]; grass #0 - moves away from - drainage #2 [2-4]; grass #0 - looks at - drainage #2 [1-24]; grass #0 - in front of - drainage #2 [0-24]; grass #0 - near - drainage #2 [0-24]; grass #0 - in front of - tractor #3 [8-24]; grass #0 - in front of - trees #4 [7-24]; grass #0 - in front of - rock #17 [7-24]; drainage #2 - in front of - tractor #3 [8-24]; drainage #2 - in front of - trees #4 [7-24]


## 365_JFqiSr9A-Go

5.0 s, 5 frames read | human: 48 objects, 53 relations | TRASER: 40 objects, 6 relations, valid JSON, 2259 tokens

**Objects: 23/48 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | accessory shelf | yes (object 1) | pegboard | mismatch | ✗ |
| 1 | accessory shelf | yes (object 2) | speaker | mismatch | ✗ |
| 2 | paper shredder | yes (object 3) | speaker | mismatch | ✗ |
| 3 | monitor | yes (object 4) | computer monitor | hypernym/hyponym | ✓ |
| 4 | coffee maker | yes (object 5) | coffee pot | synonym | ✓ |
| 5 | monitor stand | yes (object 6) | desk | mismatch | ✗ |
| 6 | person | yes (object 7) | person | identical | ✓ |
| 7 | keyboard | yes (object 8) | keyboard | identical | ✓ |
| 8 | mouse | yes (object 9) | computer mouse | hypernym/hyponym | ✓ |
| 9 | chair | yes (object 10) | chair | identical | ✓ |
| 10 | shelf | yes (object 11) | shelf | identical | ✓ |
| 11 | table | yes (object 12) | desk | synonym | ✓ |
| 12 | wall | yes (object 13) | wall | identical | ✓ |
| 13 | wall | yes (object 14) | bulletin board | mismatch | ✗ |
| 14 | lamp | yes (object 15) | lamp | identical | ✓ |
| 15 | cord | yes (object 16) | shelf | mismatch | ✗ |
| 16 | artwork | yes (object 17) | poster | hypernym/hyponym | ✓ |
| 17 | artwork | yes (object 18) | picture frame | semantic overlap | ✓ |
| 18 | artwork | yes (object 19) | poster | hypernym/hyponym | ✓ |
| 19 | headset | yes (object 20) | earphones | synonym | ✓ |
| 20 | charger | yes (object 21) | earphones | mismatch | ✗ |
| 21 | cable | yes (object 22) | pegboard | mismatch | ✗ |
| 22 | charger | yes (object 23) | earphones | mismatch | ✗ |
| 23 | charger | yes (object 24) | pegboard | mismatch | ✗ |
| 24 | wire | yes (object 25) | pegboard | mismatch | ✗ |
| 25 | paper | yes (object 26) | pegboard | mismatch | ✗ |
| 26 | file holder | yes (object 27) | speaker | mismatch | ✗ |
| 27 | holder | yes (object 28) | speaker | mismatch | ✗ |
| 28 | monitor screen | yes (object 29) | monitor | hypernym/hyponym | ✓ |
| 29 | monitor stand | yes (object 30) | stand | hypernym/hyponym | ✓ |
| 30 | monitor stand | yes (object 31) | speaker | mismatch | ✗ |
| 31 | handle | yes (object 32) | knob | synonym | ✓ |
| 32 | coffee maker base | yes (object 33) | coffee maker base | identical | ✓ |
| 33 | wood | yes (object 34) | desk | mismatch | ✗ |
| 34 | wood | yes (object 35) | drawer | mismatch | ✗ |
| 35 | shirt | yes (object 36) | jersey | hypernym/hyponym | ✓ |
| 36 | trouser | yes (object 37) | trousers | identical | ✓ |
| 37 | hair | yes (object 38) | hair | identical | ✓ |
| 38 | face | yes (object 39) | head | hypernym/hyponym | ✓ |
| 39 | hand | yes (object 40) | arm | semantic overlap | ✓ |
| 40 | hand | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | arm rest | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | support | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | light | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | stand | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | ring | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | wood | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | wood | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 3/53 right, triplets: 3/53 right** (lenient, tIoU > 0.5)

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
| person #6 - typing on - keyboard #7 | 3-6 | using | 0-7 | hypernym/hyponym | 0.43 | ✗ | ✗ |
| person #6 - looking at - keyboard #7 | 3-6 | using | 0-7 | mismatch | 0.43 | ✗ | ✗ |
| person #6 - wearing - shirt #35 | 0-6 | wearing | 0-7 | identical | 0.86 | ✓ | ✓ |
| person #6 - wearing - trouser #36 | 0-6 | wearing | 0-7 | identical | 0.86 | ✓ | ✓ |
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

**Objects: 28/43 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | tree | yes (object 1) | tree | identical | ✓ |
| 1 | tree | yes (object 2) | tree | identical | ✓ |
| 2 | tree | yes (object 3) | tree | identical | ✓ |
| 3 | tree | yes (object 4) | tree | identical | ✓ |
| 4 | tree | yes (object 5) | plant | hypernym/hyponym | ✓ |
| 5 | wood fence | yes (object 6) | fence | hypernym/hyponym | ✓ |
| 6 | sky | yes (object 7) | wire (uncertain) | mismatch | ✗ |
| 7 | tree | yes (object 8) | tree | identical | ✓ |
| 8 | grass | yes (object 9) | child | mismatch | ✗ |
| 9 | wood | yes (object 10) | wooden planks | hypernym/hyponym | ✓ |
| 10 | person | yes (object 11) | person | identical | ✓ |
| 11 | person | yes (object 12) | child | hypernym/hyponym | ✓ |
| 12 | bag | yes (object 13) | plastic bag | hypernym/hyponym | ✓ |
| 13 | mulch | yes (object 14) | leaves (uncertain) | semantic overlap | ✓ |
| 14 | trees | yes (object 15) | tree | identical | ✓ |
| 15 | tree | yes (object 16) | plant | hypernym/hyponym | ✓ |
| 16 | tree | yes (object 17) | plant | hypernym/hyponym | ✓ |
| 17 | bags | yes (object 18) | plastic bag | hypernym/hyponym | ✓ |
| 18 | wheel | yes (object 19) | wheel | identical | ✓ |
| 19 | porch | yes (object 20) | pipe (uncertain) | mismatch | ✗ |
| 20 | household material | yes (object 21) | motorcycle | mismatch | ✗ |
| 21 | plastic bucket | yes (object 22) | bucket | hypernym/hyponym | ✓ |
| 22 | lumber | yes (object 23) | wooden planks | hypernym/hyponym | ✓ |
| 23 | wire | yes (object 24) | tree | mismatch | ✗ |
| 24 | wire | yes (object 25) | wire (uncertain) | identical | ✓ |
| 25 | lumber | yes (object 26) | shoe | mismatch | ✗ |
| 26 | lumber | yes (object 27) | wooden plank (uncertain) | hypernym/hyponym | ✓ |
| 27 | wood planks | yes (object 28) | bamboo stalks | semantic overlap | ✓ |
| 28 | t-shirt | yes (object 29) | jersey (uncertain) | semantic overlap | ✓ |
| 29 | diaper | yes (object 30) | shorts (uncertain) | mismatch | ✗ |
| 30 | fence | yes (object 31) | pole | mismatch | ✗ |
| 31 | fence post | yes (object 32) | pole | synonym | ✓ |
| 32 | fence post | yes (object 33) | pole | synonym | ✓ |
| 33 | fence post | yes (object 34) | arm (uncertain) | mismatch | ✗ |
| 34 | fence post | yes (object 35) | trash can (uncertain) | mismatch | ✗ |
| 35 | wood | yes (object 36) | vent (uncertain) | mismatch | ✗ |
| 36 | t-shirt | yes (object 37) | shirt | hypernym/hyponym | ✓ |
| 37 | head | yes (object 38) | hair (uncertain) | semantic overlap | ✓ |
| 38 | head | yes (object 39) | child | mismatch | ✗ |
| 39 | wood plank | yes (object 40) | wooden plank (uncertain) | identical | ✓ |
| 40 | wood | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | saw | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | trouser | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 8/32 right, triplets: 8/32 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| sky #6 - above - wood fence #5 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| wood #9 - in front of - wood fence #5 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| wood #9 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #10 - near - wood #9 | 0-8 | near | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #10 - cutting - wood #9 | 0-2, 5-7 | near | 0-8 | mismatch | 0.50 | ✗ | ✗ |
| person #10 - working on - wood #9 | 0-8 | near | 0-8 | mismatch | 1.00 | ✗ | ✗ |
| person #10 - in front of - wood fence #5 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #10 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #10 - holding - saw #41 | 0-4, 5-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #10 - looking at - saw #41 | 0-4, 5-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #11 - near - wood #9 | 0-8 | near | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #11 - in front of - person #10 | 0-8 | in front of (+3 more) | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #11 - looking at - person #10 | 0-8 | looking at (+3 more) | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #11 - looking at - person #10 | 0-5 | looking at (+3 more) | 0-8 | identical | 0.62 | ✓ | ✓ |
| person #11 - in front of - wood fence #5 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #11 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bag #12 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bags #17 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #18 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| porch #19 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| household material #20 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plastic bucket #21 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| lumber #22 - on - grass #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| wire #23 - above - wood fence #5 | 0-8 | behind | 0-8 | mismatch | 1.00 | ✗ | ✗ |
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

**Objects: 10/14 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | forest | yes (object 1) | forest | identical | ✓ |
| 1 | car | yes (object 2) | car | identical | ✓ |
| 2 | people | yes (object 3) | person | hypernym/hyponym | ✓ |
| 3 | snow field or road | yes (object 4) | snow | semantic overlap | ✓ |
| 4 | object (uncertain) | yes (object 5) | person | hypernym/hyponym | ✓ |
| 5 | window | yes (object 6) | car's side mirror | mismatch | ✗ |
| 6 | window | yes (object 7) | car's side mirror | mismatch | ✗ |
| 7 | plate | yes (object 8) | wheel | mismatch | ✗ |
| 8 | wheel | yes (object 9) | wheel | identical | ✓ |
| 9 | wheel | yes (object 10) | wheel | identical | ✓ |
| 10 | wheel | yes (object 11) | wheel | identical | ✓ |
| 11 | rear wing | yes (object 12) | windshield wiper | mismatch | ✗ |
| 12 | light | yes (object 13) | headlight | hypernym/hyponym | ✓ |
| 13 | light | yes (object 14) | headlight | hypernym/hyponym | ✓ |

**Relations: 22/37 right, triplets: 13/37 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| car #1 - moves away from - people #2 | 0-4 | moving away from | 0-9 | identical | 0.44 | ✗ | ✗ |
| car #1 - on - snow field or road #3 | 0-8 | moving on (+2 more) | 0-9 | hypernym/hyponym | 0.89 | ✓ | ✓ |
| car #1 - drives along - snow field or road #3 | 0-8 | moving on (+2 more) | 0-9 | semantic overlap | 0.89 | ✓ | ✓ |
| car #1 - in front of - forest #0 | 0-8 | in front of (+1 more) | 0-9 | identical | 0.89 | ✓ | ✓ |
| people #2 - behind - car #1 | 0-4.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| people #2 - on - snow field or road #3 | 0-4 | on | 0-9 | identical | 0.44 | ✗ | ✗ |
| people #2 - moves along - snow field or road #3 | 0-4.5 | on | 0-9 | mismatch | 0.50 | ✗ | ✗ |
| people #2 - in front of - forest #0 | 0-4 | in front of | 0-9 | identical | 0.44 | ✗ | ✗ |
| snow field or road #3 - in front of - forest #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| object (uncertain) #4 - on - snow field or road #3 | 6-8 | on | 0-9 | identical | 0.22 | ✗ | ✗ |
| object (uncertain) #4 - behind - car #1 | 7-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #5 - attached to - car #1 | 0-8 | attached to | 0-9 | identical | 0.89 | ✓ | ✗ |
| window #5 - part of - car #1 | 0-8 | attached to | 0-9 | semantic overlap | 0.89 | ✓ | ✗ |
| window #5 - above - wheel #10 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #6 - attached to - car #1 | 0-8 | attached to | 0-9 | identical | 0.89 | ✓ | ✗ |
| window #6 - part of - car #1 | 0-8 | attached to | 0-9 | semantic overlap | 0.89 | ✓ | ✗ |
| window #6 - above - wheel #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plate #7 - attached to - car #1 | 0-8 | attached to | 0-9 | identical | 0.89 | ✓ | ✗ |
| plate #7 - part of - car #1 | 0-8 | attached to | 0-9 | semantic overlap | 0.89 | ✓ | ✗ |
| wheel #8 - attached to - car #1 | 0-8 | attached to | 0-9 | identical | 0.89 | ✓ | ✓ |
| wheel #8 - part of - car #1 | 0-8 | attached to | 0-9 | semantic overlap | 0.89 | ✓ | ✓ |
| wheel #8 - on - snow field or road #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #9 - attached to - car #1 | 0-8 | attached to | 0-9 | identical | 0.89 | ✓ | ✓ |
| wheel #9 - part of - car #1 | 0-8 | attached to | 0-9 | semantic overlap | 0.89 | ✓ | ✓ |
| wheel #9 - on - snow field or road #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #10 - attached to - car #1 | 0-8 | attached to | 0-9 | identical | 0.89 | ✓ | ✓ |
| wheel #10 - part of - car #1 | 0-8 | attached to | 0-9 | semantic overlap | 0.89 | ✓ | ✓ |
| wheel #10 - on - snow field or road #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| rear wing #11 - attached to - car #1 | 0-7 | attached to | 0-9 | identical | 0.78 | ✓ | ✗ |
| rear wing #11 - part of - car #1 | 0-8 | attached to | 0-9 | semantic overlap | 0.89 | ✓ | ✗ |
| rear wing #11 - above - wheel #9 | 0-8 | above | 0-9 | identical | 0.89 | ✓ | ✗ |
| light #12 - attached to - car #1 | 0-8 | attached to | 0-9 | identical | 0.89 | ✓ | ✓ |
| light #12 - part of - car #1 | 0-8 | attached to | 0-9 | semantic overlap | 0.89 | ✓ | ✓ |
| light #12 - above - plate #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #13 - attached to - car #1 | 0-8 | attached to | 0-9 | identical | 0.89 | ✓ | ✓ |
| light #13 - part of - car #1 | 0-8 | attached to | 0-9 | semantic overlap | 0.89 | ✓ | ✓ |
| light #13 - above - plate #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (14): car #1 - moving away from - object (uncertain) #4 [0-9]; object (uncertain) #4 - in front of - forest #0 [0-9]; light #12 - above - wheel #10 [0-9]; light #13 - above - wheel #8 [0-9]; rear wing #11 - above - wheel #10 [0-9]; light #12 - in front of - forest #0 [0-9]; light #13 - in front of - forest #0 [0-9]; rear wing #11 - in front of - forest #0 [0-9]; window #5 - in front of - forest #0 [0-9]; window #6 - in front of - forest #0 [0-9]


## 465_nbJ_SLWUDxk

7.5 s, 8 frames read | human: 39 objects, 24 relations | TRASER: 39 objects, 52 relations, valid JSON, 2578 tokens

**Objects: 34/39 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | person | yes (object 2) | person | identical | ✓ |
| 2 | person | yes (object 3) | person | identical | ✓ |
| 3 | person | yes (object 4) | person | identical | ✓ |
| 4 | person | yes (object 5) | person | identical | ✓ |
| 5 | person | yes (object 6) | person | identical | ✓ |
| 6 | person | yes (object 7) | person | identical | ✓ |
| 7 | person | yes (object 8) | child | hypernym/hyponym | ✓ |
| 8 | person | yes (object 9) | person | identical | ✓ |
| 9 | person | yes (object 10) | child | hypernym/hyponym | ✓ |
| 10 | person | yes (object 11) | person | identical | ✓ |
| 11 | person | yes (object 12) | person | identical | ✓ |
| 12 | person | yes (object 13) | person | identical | ✓ |
| 13 | person | yes (object 14) | person | identical | ✓ |
| 14 | person | yes (object 15) | jersey (uncertain) | mismatch | ✗ |
| 15 | person | yes (object 16) | person | identical | ✓ |
| 16 | person | yes (object 17) | person | identical | ✓ |
| 17 | person | yes (object 18) | person | identical | ✓ |
| 18 | person | yes (object 19) | person | identical | ✓ |
| 19 | person | yes (object 20) | person | identical | ✓ |
| 20 | person | yes (object 21) | person | identical | ✓ |
| 21 | person | yes (object 22) | person | identical | ✓ |
| 22 | person | yes (object 23) | person | identical | ✓ |
| 23 | person | yes (object 24) | person | identical | ✓ |
| 24 | person | yes (object 25) | person | identical | ✓ |
| 25 | person | yes (object 26) | person | identical | ✓ |
| 26 | person | yes (object 27) | person | identical | ✓ |
| 27 | person | yes (object 28) | person | identical | ✓ |
| 28 | person | yes (object 29) | person | identical | ✓ |
| 29 | ground | yes (object 30) | person | mismatch | ✗ |
| 30 | buildings | yes (object 31) | hill | mismatch | ✗ |
| 31 | sky | yes (object 32) | streetlight | mismatch | ✗ |
| 32 | river | yes (object 33) | boat | mismatch | ✗ |
| 33 | light | yes (object 34) | streetlight | hypernym/hyponym | ✓ |
| 34 | light | yes (object 35) | streetlight | hypernym/hyponym | ✓ |
| 35 | saxophone | yes (object 36) | saxophone | identical | ✓ |
| 36 | shoes | yes (object 37) | roller skates | semantic overlap | ✓ |
| 37 | hat | yes (object 38) | hat | identical | ✓ |
| 38 | suit | yes (object 39) | suit jacket | hypernym/hyponym | ✓ |

**Relations: 7/24 right, triplets: 6/24 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - in front of - person #7 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #0 - wears - hat #37 | 0-8 | wearing | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #0 - wears - suit #38 | 0-8 | wearing | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #0 - performs for - person #1 | 0-8 | in front of | 0-9 | semantic overlap | 0.89 | ✓ | ✓ |
| person #0 - approaches - person #1 | 0-5 | in front of | 0-9 | mismatch | 0.56 | ✗ | ✗ |
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
| sky #31 - above - buildings #30 | 0-8 | in front of | 0-9 | mismatch | 0.89 | ✗ | ✗ |
| river #32 - behind - person #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #33 - above - ground #29 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #34 - above - ground #29 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| shoes #36 - on - person #2 | 0-6.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| hat #37 - on - person #0 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✓ |
| suit #38 - on - person #0 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (44): person #0 - holding - saxophone #35 [0-9]; person #0 - playing - saxophone #35 [0-9]; person #0 - looking at - saxophone #35 [0-9]; person #0 - performing with - saxophone #35 [0-9]; saxophone #35 - in front of - person #0 [0-9]; saxophone #35 - below - person #0 [0-9]; shoes #36 - below - person #0 [0-9]; shoes #36 - below - saxophone #35 [0-9]; saxophone #35 - in front of - buildings #30 [0-9]; hat #37 - above - suit #38 [0-9]


## 470_BiIqH60-A1M

7.5 s, 8 frames read | human: 36 objects, 30 relations | TRASER: 36 objects, 44 relations, valid JSON, 2586 tokens

**Objects: 20/36 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | person | yes (object 2) | person | identical | ✓ |
| 2 | kid | yes (object 3) | child | identical | ✓ |
| 3 | dad | yes (object 4) | person | hypernym/hyponym | ✓ |
| 4 | floor | yes (object 5) | floor | identical | ✓ |
| 5 | painting | yes (object 6) | painting | identical | ✓ |
| 6 | wall | yes (object 7) | pipe (uncertain) | mismatch | ✗ |
| 7 | roof | yes (object 8) | ceiling (uncertain) | semantic overlap | ✓ |
| 8 | pavement | yes (object 9) | wall | mismatch | ✗ |
| 9 | person | yes (object 10) | flower arrangement | mismatch | ✗ |
| 10 | shirt | yes (object 11) | jacket | semantic overlap | ✓ |
| 11 | cap | yes (object 12) | hat (uncertain) | hypernym/hyponym | ✓ |
| 12 | face | yes (object 13) | hat (uncertain) | mismatch | ✗ |
| 13 | hair | yes (object 14) | hat (uncertain) | mismatch | ✗ |
| 14 | trouser | yes (object 15) | trousers | identical | ✓ |
| 15 | shoe | yes (object 16) | shoe | identical | ✓ |
| 16 | shoe | yes (object 17) | shoe | identical | ✓ |
| 17 | bag | yes (object 18) | backpack | hypernym/hyponym | ✓ |
| 18 | bag | yes (object 19) | trousers | mismatch | ✗ |
| 19 | shirt | yes (object 20) | shirt | identical | ✓ |
| 20 | trouser | yes (object 21) | trousers | identical | ✓ |
| 21 | hand | yes (object 22) | handbag | mismatch | ✗ |
| 22 | hand | yes (object 23) | handbag | mismatch | ✗ |
| 23 | hair | yes (object 24) | flower arrangement | mismatch | ✗ |
| 24 | shirt | yes (object 25) | person | mismatch | ✗ |
| 25 | hair | yes (object 26) | person | mismatch | ✗ |
| 26 | face | yes (object 27) | person | hypernym/hyponym | ✓ |
| 27 | shirt | yes (object 28) | person | mismatch | ✗ |
| 28 | hand | yes (object 29) | handbag | mismatch | ✗ |
| 29 | face | yes (object 30) | child | mismatch | ✗ |
| 30 | trouser | yes (object 31) | trousers | identical | ✓ |
| 31 | cap | yes (object 32) | hat (uncertain) | hypernym/hyponym | ✓ |
| 32 | jacket | yes (object 33) | person | mismatch | ✗ |
| 33 | trouser | yes (object 34) | trousers | identical | ✓ |
| 34 | bag | yes (object 35) | shoe | mismatch | ✗ |
| 35 | face | yes (object 36) | person | hypernym/hyponym | ✓ |

**Relations: 11/30 right, triplets: 11/30 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - on - floor #4 | 0-2 | on | 0-1 | identical | 0.50 | ✗ | ✗ |
| person #0 - in front of - painting #5 | 0-2 | in front of | 0-1 | identical | 0.50 | ✗ | ✗ |
| person #1 - on - floor #4 | 0-8 | on | 0-7 | identical | 0.88 | ✓ | ✓ |
| person #1 - in front of - painting #5 | 1-8 | in front of | 0-7 | identical | 0.75 | ✓ | ✓ |
| person #1 - wears - cap #31 | 3-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - wears - jacket #32 | 0-8 | walking with (+1 more) | 0-7 | mismatch | 0.88 | ✗ | ✗ |
| kid #2 - on - floor #4 | 0-8 | on | 0-7 | identical | 0.88 | ✓ | ✓ |
| kid #2 - walks on - floor #4 | 1-8 | on | 0-7 | hypernym/hyponym | 0.75 | ✓ | ✓ |
| kid #2 - in front of - painting #5 | 0-8 | in front of | 0-7 | identical | 0.88 | ✓ | ✓ |
| kid #2 - in front of - dad #3 | 0-8 | next to | 0-7 | semantic overlap | 0.88 | ✓ | ✓ |
| dad #3 - on - floor #4 | 0-8 | on | 0-7 | identical | 0.88 | ✓ | ✓ |
| dad #3 - walks on - floor #4 | 0-8 | on | 0-7 | hypernym/hyponym | 0.88 | ✓ | ✓ |
| dad #3 - in front of - painting #5 | 0-8 | in front of | 0-7 | identical | 0.88 | ✓ | ✓ |
| dad #3 - holds - kid #2 | 2-8 | walking with | 0-7 | mismatch | 0.62 | ✗ | ✗ |
| dad #3 - escorts - kid #2 | 0-8 | walking with | 0-7 | semantic overlap | 0.88 | ✓ | ✓ |
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

**Objects: 24/72 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | wall | yes (object 1) | train | mismatch | ✗ |
| 1 | train | yes (object 2) | train | identical | ✓ |
| 2 | floor | yes (object 3) | platform | semantic overlap | ✓ |
| 3 | pillars | yes (object 4) | pillar | identical | ✓ |
| 4 | display stand | yes (object 5) | door | mismatch | ✗ |
| 5 | person | yes (object 6) | person | identical | ✓ |
| 6 | person | yes (object 7) | person | identical | ✓ |
| 7 | bag | yes (object 8) | handbag | hypernym/hyponym | ✓ |
| 8 | wall | yes (object 9) | ceiling lamp | mismatch | ✗ |
| 9 | camera | yes (object 10) | streetlight (uncertain) | mismatch | ✗ |
| 10 | light | yes (object 11) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 11 | light | yes (object 12) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 12 | light | yes (object 13) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 13 | light | yes (object 14) | signboard | mismatch | ✗ |
| 14 | light | no: no mask on the frames TRASER reads | - | no label from TRASER | ✗ |
| 15 | roof | yes (object 15) | train | mismatch | ✗ |
| 16 | rail track | yes (object 16) | train track | synonym | ✓ |
| 17 | light | yes (object 17) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 18 | light | yes (object 18) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 19 | light | yes (object 19) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 20 | light | yes (object 20) | vent (uncertain) | mismatch | ✗ |
| 21 | light | yes (object 21) | vent (uncertain) | mismatch | ✗ |
| 22 | light | yes (object 22) | person | mismatch | ✗ |
| 23 | wall | yes (object 23) | wall panel | hypernym/hyponym | ✓ |
| 24 | roof | yes (object 24) | vent (uncertain) | mismatch | ✗ |
| 25 | cart | yes (object 25) | door | mismatch | ✗ |
| 26 | wall | yes (object 26) | ceiling light fixture | mismatch | ✗ |
| 27 | wall | yes (object 27) | wall panel | hypernym/hyponym | ✓ |
| 28 | door | yes (object 28) | poster | mismatch | ✗ |
| 29 | overhead structure | yes (object 29) | ceiling beam (uncertain) | hypernym/hyponym | ✓ |
| 30 | light | yes (object 30) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 31 | sign | yes (object 31) | signboard | synonym | ✓ |
| 32 | sign | yes (object 32) | signboard | synonym | ✓ |
| 33 | head | yes (object 33) | hat (uncertain) | mismatch | ✗ |
| 34 | coat | yes (object 34) | suit jacket | hypernym/hyponym | ✓ |
| 35 | trouser | yes (object 35) | trousers | identical | ✓ |
| 36 | shoe | yes (object 36) | shoe | identical | ✓ |
| 37 | shoe | yes (object 37) | shoe | identical | ✓ |
| 38 | bag | yes (object 38) | handbag | hypernym/hyponym | ✓ |
| 39 | wooden | yes (object 39) | door | mismatch | ✗ |
| 40 | glass | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | glass | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | head | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | shirt | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | trouser | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | camera socket | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | camera | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | camera | no: after the first 40 | - | no label from TRASER | ✗ |
| 48 | light | no: after the first 40 | - | no label from TRASER | ✗ |
| 49 | light | no: after the first 40 | - | no label from TRASER | ✗ |
| 50 | light | no: after the first 40 | - | no label from TRASER | ✗ |
| 51 | light | no: after the first 40 | - | no label from TRASER | ✗ |
| 52 | light | no: after the first 40 | - | no label from TRASER | ✗ |
| 53 | light | no: after the first 40 | - | no label from TRASER | ✗ |
| 54 | door | no: after the first 40 | - | no label from TRASER | ✗ |
| 55 | light | no: after the first 40 | - | no label from TRASER | ✗ |
| 56 | light | no: after the first 40 | - | no label from TRASER | ✗ |
| 57 | door/window | no: after the first 40 | - | no label from TRASER | ✗ |
| 58 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 59 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 60 | door | no: after the first 40 | - | no label from TRASER | ✗ |
| 61 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 62 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 63 | door | no: after the first 40 | - | no label from TRASER | ✗ |
| 64 | light | no: after the first 40 | - | no label from TRASER | ✗ |
| 65 | light | no: after the first 40 | - | no label from TRASER | ✗ |
| 66 | light | no: after the first 40 | - | no label from TRASER | ✗ |
| 67 | light | no: after the first 40 | - | no label from TRASER | ✗ |
| 68 | light | no: after the first 40 | - | no label from TRASER | ✗ |
| 69 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 70 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 71 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 12/30 right, triplets: 11/30 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| train #1 - arriving at - floor #2 | 0-6 | passing | 0-8 | mismatch | 0.75 | ✗ | ✗ |
| train #1 - under - roof #15 | 0-8 | in front of | 0-8 | mismatch | 1.00 | ✗ | ✗ |
| train #1 - alongside - wall #0 | 0-6 | passing (+1 more) | 0-6 | semantic overlap | 1.00 | ✓ | ✗ |
| train #1 - on - rail track #16 | 0-6.5 | above | 0-8 | semantic overlap | 0.81 | ✓ | ✓ |
| train #1 - moving along - rail track #16 | 0-8 | above | 0-8 | mismatch | 1.00 | ✗ | ✗ |
| train #1 - approaching - person #5 | 0-5 | passing | 0-8 | mismatch | 0.62 | ✗ | ✗ |
| train #1 - passing by - person #5 | 5-8 | passing | 0-8 | identical | 0.38 | ✗ | ✗ |
| pillars #3 - on - floor #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| pillars #3 - under - overhead structure #29 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| pillars #3 - in front of - wall #23 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| display stand #4 - on - floor #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - wearing - trouser #35 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #5 - wearing - shoe #36 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #5 - wearing - shoe #37 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #5 - looking at - train #1 | 0-8 | looking at (+1 more) | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #5 - on - floor #2 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #5 - in front of - pillars #3 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
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
| sign #31 - on - wall #23 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| sign #32 - on - wall #23 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| pillar #69 - on - floor #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (52): person #5 - carrying - bag #38 [0-8]; train #1 - passing - pillars #3 [0-8]; person #5 - in front of - display stand #4 [0-8]; person #5 - in front of - cart #25 [0-8]; person #5 - in front of - wooden #39 [0-8]; person #5 - in front of - wall #23 [0-8]; person #5 - in front of - wall #27 [0-8]; person #5 - in front of - door #28 [0-8]; person #5 - in front of - sign #31 [0-8]; person #5 - in front of - sign #32 [0-8]


## 520_JbMXRRGOEkk

5.33 s, 5 frames read | human: 24 objects, 31 relations | TRASER: 24 objects, 39 relations, valid JSON, 1985 tokens

**Objects: 14/24 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | person | yes (object 2) | person | identical | ✓ |
| 2 | person | yes (object 3) | person | identical | ✓ |
| 3 | snow | yes (object 4) | hockey puck (uncertain) | mismatch | ✗ |
| 4 | shield | yes (object 5) | banner | mismatch | ✗ |
| 5 | barricade | yes (object 6) | wall panel | mismatch | ✗ |
| 6 | post | yes (object 7) | hockey goal | mismatch | ✗ |
| 7 | ski stick | yes (object 8) | hockey puck (uncertain) | mismatch | ✗ |
| 8 | legs | yes (object 9) | trousers | mismatch | ✗ |
| 9 | jersey | yes (object 10) | jersey | identical | ✓ |
| 10 | helmet | yes (object 11) | helmet | identical | ✓ |
| 11 | glove | yes (object 12) | glove | identical | ✓ |
| 12 | glove | yes (object 13) | glove | identical | ✓ |
| 13 | hockey stick | yes (object 14) | hockey puck (uncertain) | mismatch | ✗ |
| 14 | helmet | yes (object 15) | helmet | identical | ✓ |
| 15 | jersey | yes (object 16) | hooded jacket | mismatch | ✗ |
| 16 | glove | yes (object 17) | glove (uncertain) | identical | ✓ |
| 17 | legs | yes (object 18) | trousers | mismatch | ✗ |
| 18 | hockey stick | yes (object 19) | shoe (uncertain) | mismatch | ✗ |
| 19 | headgear | yes (object 20) | helmet | hypernym/hyponym | ✓ |
| 20 | shirt | yes (object 21) | jacket | semantic overlap | ✓ |
| 21 | pants | yes (object 22) | trousers | synonym | ✓ |
| 22 | hockey stick | yes (object 23) | hockey stick | identical | ✓ |
| 23 | hand | yes (object 24) | glove | semantic overlap | ✓ |

**Relations: 9/31 right, triplets: 2/31 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - wears - headgear #19 | 0.5-5.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - wears - shirt #20 | 1-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - wears - pants #21 | 1-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - holds - hockey stick #22 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - approaches - post #6 | 1-5.5 | in front of | 0-4 | mismatch | 0.55 | ✗ | ✗ |
| person #0 - on - snow #3 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - in front of - shield #4 | 0-2 | in front of | 0-4 | identical | 0.50 | ✗ | ✗ |
| person #1 - wears - helmet #10 | 0-6 | wearing | 0-6 | identical | 1.00 | ✓ | ✓ |
| person #1 - wears - jersey #9 | 0-6 | wearing | 0-6 | identical | 1.00 | ✓ | ✓ |
| person #1 - wears - legs #8 | 0-6 | wearing | 0-6 | identical | 1.00 | ✓ | ✗ |
| person #1 - holds - ski stick #7 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - approaches - post #6 | 1-4 | approaching (+2 more) | 0-3 | identical | 0.50 | ✗ | ✗ |
| person #1 - moves away from - post #6 | 3.5-6 | moving away from (+2 more) | 3-6 | identical | 0.83 | ✓ | ✗ |
| person #1 - attacks goal - post #6 | 1-3.5 | approaching (+2 more) | 0-3 | semantic overlap | 0.57 | ✓ | ✗ |
| person #1 - celebrates - post #6 | 4-6 | moving away from (+2 more) | 3-6 | mismatch | 0.67 | ✗ | ✗ |
| person #1 - chases - person #0 | 1-4 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - on - snow #3 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - in front of - shield #4 | 0-6 | in front of | 0-6 | identical | 1.00 | ✓ | ✗ |
| person #2 - on - snow #3 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - in front of - shield #4 | 0-5 | in front of | 0-4 | identical | 0.80 | ✓ | ✗ |
| snow #3 - below - barricade #5 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| snow #3 - below - shield #4 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| shield #4 - below - barricade #5 | 0-6 | on | 0-6 | mismatch | 1.00 | ✗ | ✗ |
| post #6 - on - snow #3 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| post #6 - in front of - shield #4 | 0-6 | in front of | 0-6 | identical | 1.00 | ✓ | ✗ |
| post #6 - in front of - barricade #5 | 0-6 | in front of | 0-6 | identical | 1.00 | ✓ | ✗ |
| ski stick #7 - above - snow #3 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| legs #8 - on - snow #3 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| hockey stick #18 - above - snow #3 | 0-1 | nothing for this pair | - | - | - | ✗ | ✗ |
| pants #21 - on - snow #3 | 1-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| hockey stick #22 - above - snow #3 | 0.5-5 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (26): person #1 - wearing - glove #11 [0-6]; person #1 - wearing - glove #12 [0-6]; person #1 - wearing - hand #23 [0-6]; person #1 - holding - hockey stick #22 [0-1, 2-6]; person #1 - in front of - barricade #5 [0-6]; person #0 - in front of - barricade #5 [0-4]; person #2 - in front of - barricade #5 [0-4]; person #2 - in front of - post #6 [0-4]; helmet #10 - above - jersey #9 [0-6]; jersey #9 - above - legs #8 [0-6]


## 547_7E-Xian95Qk

6.67 s, 7 frames read | human: 22 objects, 28 relations | TRASER: 22 objects, 48 relations, valid JSON, 2047 tokens

**Objects: 18/22 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | wall | yes (object 1) | wall | identical | ✓ |
| 1 | tray | yes (object 2) | table | semantic overlap | ✓ |
| 2 | girl | yes (object 3) | child | hypernym/hyponym | ✓ |
| 3 | man | yes (object 4) | child | semantic overlap | ✓ |
| 4 | counter or play table | yes (object 5) | wooden toy structure | semantic overlap | ✓ |
| 5 | toy food | yes (object 6) | toy | hypernym/hyponym | ✓ |
| 6 | tray | yes (object 7) | bowl | semantic overlap | ✓ |
| 7 | drawer | yes (object 8) | table | mismatch | ✗ |
| 8 | storage with handle | yes (object 9) | fabric | mismatch | ✗ |
| 9 | storage with handle | yes (object 10) | poster | mismatch | ✗ |
| 10 | shelves | yes (object 11) | bookshelf | hypernym/hyponym | ✓ |
| 11 | shelf | yes (object 12) | wooden toy structure | mismatch | ✗ |
| 12 | toy donut | yes (object 13) | doughnut | semantic overlap | ✓ |
| 13 | toy donut | yes (object 14) | doughnut | semantic overlap | ✓ |
| 14 | toy donut | yes (object 15) | doughnut | semantic overlap | ✓ |
| 15 | toy donut | yes (object 16) | doughnut | semantic overlap | ✓ |
| 16 | toy donut | yes (object 17) | doughnut | semantic overlap | ✓ |
| 17 | toy donut | yes (object 18) | doughnut | semantic overlap | ✓ |
| 18 | toy pastry | yes (object 19) | doughnut | semantic overlap | ✓ |
| 19 | toy donut | yes (object 20) | doughnut | semantic overlap | ✓ |
| 20 | toy | yes (object 21) | toy | identical | ✓ |
| 21 | toy pastry | yes (object 22) | doughnut | semantic overlap | ✓ |

**Relations: 14/28 right, triplets: 13/28 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| girl #2 - hold - toy #20 | 0-4.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| girl #2 - look at - tray #6 | 0-4 | nothing for this pair | - | - | - | ✗ | ✗ |
| girl #2 - in front of - wall #0 | 0-7 | in front of | 0-7 | identical | 1.00 | ✓ | ✓ |
| man #3 - hold - tray #6 | 0-7 | holding (+2 more) | 0-7 | identical | 1.00 | ✓ | ✓ |
| man #3 - move - tray #6 | 0-6 | holding (+2 more) | 0-7 | mismatch | 0.86 | ✗ | ✗ |
| man #3 - show to - girl #2 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #3 - display - toy food #5 | 0-7 | holding (+2 more) | 0-7 | semantic overlap | 1.00 | ✓ | ✓ |
| man #3 - in front of - wall #0 | 0-7 | in front of | 0-7 | identical | 1.00 | ✓ | ✓ |
| tray #6 - contain - toy food #5 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| tray #6 - carry - toy donut #12 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| tray #6 - carry - toy donut #16 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| tray #6 - in front of - man #3 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| tray #6 - in front of - girl #2 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| storage with handle #8 - on - wall #0 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| storage with handle #9 - on - wall #0 | 0-7 | on | 0-7 | identical | 1.00 | ✓ | ✗ |
| shelf #11 - in front of - wall #0 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| toy donut #12 - in - tray #6 | 0-7 | in | 0-7 | identical | 1.00 | ✓ | ✓ |
| toy donut #12 - on - toy donut #13 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| toy donut #13 - in - tray #6 | 0-7 | in | 0-7 | identical | 1.00 | ✓ | ✓ |
| toy donut #14 - in - tray #6 | 0-7 | in | 0-7 | identical | 1.00 | ✓ | ✓ |
| toy donut #15 - in - tray #6 | 0-7 | in | 0-7 | identical | 1.00 | ✓ | ✓ |
| toy donut #15 - on - toy donut #14 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| toy donut #16 - in - tray #6 | 0-7 | in | 0-7 | identical | 1.00 | ✓ | ✓ |
| toy donut #16 - on - toy donut #15 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| toy donut #17 - in - tray #6 | 0-7 | in | 0-7 | identical | 1.00 | ✓ | ✓ |
| toy pastry #18 - in - tray #6 | 0-7 | in | 0-7 | identical | 1.00 | ✓ | ✓ |
| toy donut #19 - in - tray #6 | 0-1, 3-7 | in | 0-7 | identical | 0.71 | ✓ | ✓ |
| toy pastry #21 - in - tray #6 | 0-7 | in | 0-7 | identical | 1.00 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (30): man #3 - touching - toy donut #12 [0-7]; man #3 - touching - toy donut #13 [0-7]; man #3 - touching - toy donut #14 [0-7]; man #3 - touching - toy donut #15 [0-7]; man #3 - touching - toy donut #16 [0-7]; man #3 - touching - toy donut #17 [0-7]; man #3 - touching - toy pastry #18 [0-7]; man #3 - touching - toy donut #19 [0-7]; man #3 - touching - toy pastry #21 [0-7]; tray #6 - on - drawer #7 [0-7]


## 551_VHxQVmG1pOA

6.83 s, 7 frames read | human: 47 objects, 53 relations | TRASER: 40 objects, 40 relations, valid JSON, 2888 tokens

**Objects: 35/47 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | girl | yes (object 1) | person | hypernym/hyponym | ✓ |
| 1 | man | yes (object 2) | person | hypernym/hyponym | ✓ |
| 2 | man | yes (object 3) | person | hypernym/hyponym | ✓ |
| 3 | man | yes (object 4) | person | hypernym/hyponym | ✓ |
| 4 | man | yes (object 5) | person | hypernym/hyponym | ✓ |
| 5 | glass dome or cover | yes (object 6) | dome-shaped object (uncertain) | hypernym/hyponym | ✓ |
| 6 | glass dome or cover | yes (object 7) | dome-shaped object (uncertain) | hypernym/hyponym | ✓ |
| 7 | glass dome or cover | yes (object 8) | dome-shaped object (uncertain) | hypernym/hyponym | ✓ |
| 8 | woman | yes (object 9) | person | hypernym/hyponym | ✓ |
| 9 | woman | yes (object 10) | person | hypernym/hyponym | ✓ |
| 10 | ceiling | yes (object 11) | ceiling | identical | ✓ |
| 11 | people | yes (object 12) | person | hypernym/hyponym | ✓ |
| 12 | people | yes (object 13) | person | hypernym/hyponym | ✓ |
| 13 | logo | yes (object 14) | signboard | semantic overlap | ✓ |
| 14 | wall | yes (object 15) | archway | semantic overlap | ✓ |
| 15 | boxes | yes (object 16) | box | identical | ✓ |
| 16 | wall | yes (object 17) | wall panel | hypernym/hyponym | ✓ |
| 17 | boxes (uncertain) | yes (object 18) | wall | mismatch | ✗ |
| 18 | boxes (uncertain) | yes (object 19) | person | mismatch | ✗ |
| 19 | light | yes (object 20) | lamp | hypernym/hyponym | ✓ |
| 20 | light | yes (object 21) | lamp | hypernym/hyponym | ✓ |
| 21 | doorway | yes (object 22) | column | mismatch | ✗ |
| 22 | wall | yes (object 23) | column | semantic overlap | ✓ |
| 23 | display counter | yes (object 24) | display case | semantic overlap | ✓ |
| 24 | display counter | yes (object 25) | display case | semantic overlap | ✓ |
| 25 | watch | yes (object 26) | watch | identical | ✓ |
| 26 | glass | yes (object 27) | sunglasses | mismatch | ✗ |
| 27 | cake | yes (object 28) | cake | identical | ✓ |
| 28 | cake | yes (object 29) | cake | identical | ✓ |
| 29 | cake | yes (object 30) | cake | identical | ✓ |
| 30 | cake | yes (object 31) | cake | identical | ✓ |
| 31 | cake | yes (object 32) | cake | identical | ✓ |
| 32 | cake | yes (object 33) | cake | identical | ✓ |
| 33 | cake | yes (object 34) | cake | identical | ✓ |
| 34 | countertop | yes (object 35) | countertop (uncertain) | identical | ✓ |
| 35 | pastries | yes (object 36) | pastry (uncertain) | identical | ✓ |
| 36 | pastries | yes (object 37) | pastry (uncertain) | identical | ✓ |
| 37 | pastries | yes (object 38) | pastry (uncertain) | identical | ✓ |
| 38 | countertop | yes (object 39) | tray (uncertain) | mismatch | ✗ |
| 39 | t-shirt | yes (object 40) | shirt | hypernym/hyponym | ✓ |
| 40 | clothes | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | hair clip | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | t-shirt | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | cake | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | cake | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | cake | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | cake | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 17/53 right, triplets: 15/53 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| girl #0 - wearing - watch #25 | 0-7 | wearing | 0-8 | identical | 0.88 | ✓ | ✓ |
| girl #0 - wearing - glass #26 | 0-7 | wearing | 0-8 | identical | 0.88 | ✓ | ✗ |
| girl #0 - in front of - display counter #23 | 0-7 | in front of (+3 more) | 0-8 | identical | 0.88 | ✓ | ✓ |
| girl #0 - browsing at - display counter #23 | 0-7 | looking at (+3 more) | 0-8 | synonym | 0.88 | ✓ | ✓ |
| girl #0 - looking at - display counter #23 | 0-7 | looking at (+3 more) | 0-8 | identical | 0.88 | ✓ | ✓ |
| girl #0 - wearing - hair clip #41 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| girl #0 - wearing - t-shirt #39 | 0-7 | wearing | 0-8 | identical | 0.88 | ✓ | ✓ |
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
| light #19 - on - ceiling #10 | 0-7 | under | 0-8 | mismatch | 0.88 | ✗ | ✗ |
| light #20 - on - ceiling #10 | 0-7 | under | 0-8 | mismatch | 0.88 | ✗ | ✗ |
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
| t-shirt #39 - on - girl #0 | 0-7 | on | 0-8 | identical | 0.88 | ✓ | ✓ |
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

**Objects: 10/40 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | barricade | yes (object 1) | fence | synonym | ✓ |
| 1 | tree | yes (object 2) | tree | identical | ✓ |
| 2 | sky | yes (object 3) | tree | mismatch | ✗ |
| 3 | ground | yes (object 4) | grass | semantic overlap | ✓ |
| 4 | ship | yes (object 5) | naval vessel (uncertain) | hypernym/hyponym | ✓ |
| 5 | tree | yes (object 6) | trees | identical | ✓ |
| 6 | ocean | yes (object 7) | wall | mismatch | ✗ |
| 7 | fence | yes (object 8) | pole (uncertain) | mismatch | ✗ |
| 8 | fence | yes (object 9) | pole (uncertain) | mismatch | ✗ |
| 9 | barricade | yes (object 10) | pole | mismatch | ✗ |
| 10 | barricade | yes (object 11) | pole | mismatch | ✗ |
| 11 | barricade | yes (object 12) | pole | mismatch | ✗ |
| 12 | barricade | yes (object 13) | pole | mismatch | ✗ |
| 13 | barricade | yes (object 14) | pole | mismatch | ✗ |
| 14 | barricade | yes (object 15) | pole | mismatch | ✗ |
| 15 | barricade | yes (object 16) | pole | mismatch | ✗ |
| 16 | barricade | yes (object 17) | pole | mismatch | ✗ |
| 17 | barricade | yes (object 18) | pole | mismatch | ✗ |
| 18 | mast | yes (object 19) | structure (uncertain) | hypernym/hyponym | ✓ |
| 19 | gun mount | yes (object 20) | missile (uncertain) | mismatch | ✗ |
| 20 | gun mount base | yes (object 21) | storage tank (uncertain) | mismatch | ✗ |
| 21 | gun mount | yes (object 22) | storage tank (uncertain) | mismatch | ✗ |
| 22 | people | yes (object 23) | missile (uncertain) | mismatch | ✗ |
| 23 | gun mount base | yes (object 24) | storage tank (uncertain) | mismatch | ✗ |
| 24 | person | yes (object 25) | missile (uncertain) | mismatch | ✗ |
| 25 | hull | yes (object 26) | ship | semantic overlap | ✓ |
| 26 | sign | yes (object 27) | signboard | synonym | ✓ |
| 27 | pole | yes (object 28) | boat | mismatch | ✗ |
| 28 | anchor | yes (object 29) | boat | mismatch | ✗ |
| 29 | hull number | yes (object 30) | number (uncertain) | hypernym/hyponym | ✓ |
| 30 | hull | yes (object 31) | ship | semantic overlap | ✓ |
| 31 | barricade | yes (object 32) | pole | mismatch | ✗ |
| 32 | barricade | yes (object 33) | pole | mismatch | ✗ |
| 33 | barricade | yes (object 34) | pole | mismatch | ✗ |
| 34 | barricade | yes (object 35) | pole | mismatch | ✗ |
| 35 | barricade | yes (object 36) | pole | mismatch | ✗ |
| 36 | barricade | yes (object 37) | pole | mismatch | ✗ |
| 37 | barricade | yes (object 38) | pole | mismatch | ✗ |
| 38 | barricade | yes (object 39) | pole | mismatch | ✗ |
| 39 | barricade | yes (object 40) | pole | mismatch | ✗ |

**Relations: 2/34 right, triplets: 1/34 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| barricade #0 - in front of - ocean #6 | 0-21 | in front of | 0-20 | identical | 0.95 | ✓ | ✗ |
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
| sign #26 - behind - barricade #0 | 0-21 | above | 0-20 | mismatch | 0.95 | ✗ | ✗ |
| anchor #28 - on - hull #25 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| anchor #28 - attached to - ship #4 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| hull number #29 - on - hull #25 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| hull number #29 - printed on - hull #25 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (39): hull #25 - moves left relative to - tree #1 [0-20]; hull #25 - moves left relative to - barricade #0 [0-20]; hull #25 - behind - barricade #0 [0-20]; hull #25 - above - barricade #0 [0-20]; hull #25 - moves left relative to - ocean #6 [0-20]; hull #25 - above - ocean #6 [0-20]; hull #25 - moves left relative to - sign #26 [0-20]; hull #25 - moves left relative to - pole #27 [0-20]; hull #25 - moves left relative to - anchor #28 [0-20]; hull #25 - in front of - tree #5 [0-20]


## 628_nQRJD435Fh4

22.67 s, 23 frames read | human: 40 objects, 52 relations | TRASER: 40 objects, 115 relations, valid JSON, 4076 tokens

**Objects: 32/40 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | ground | yes (object 1) | floor | synonym | ✓ |
| 1 | person | yes (object 2) | person | identical | ✓ |
| 2 | person | yes (object 3) | person | identical | ✓ |
| 3 | person | yes (object 4) | person | identical | ✓ |
| 4 | person | yes (object 5) | person | identical | ✓ |
| 5 | pingpong ball holder | yes (object 6) | bucket | semantic overlap | ✓ |
| 6 | wall | yes (object 7) | wall panel | hypernym/hyponym | ✓ |
| 7 | door | yes (object 8) | door | identical | ✓ |
| 8 | door | yes (object 9) | door (uncertain) | identical | ✓ |
| 9 | door | yes (object 10) | door | identical | ✓ |
| 10 | door | yes (object 11) | door | identical | ✓ |
| 11 | dumpster | yes (object 12) | trash can | synonym | ✓ |
| 12 | chair | yes (object 13) | chair | identical | ✓ |
| 13 | board | yes (object 14) | banner | semantic overlap | ✓ |
| 14 | ground | yes (object 15) | floor | synonym | ✓ |
| 15 | person | yes (object 16) | person | identical | ✓ |
| 16 | person | yes (object 17) | person | identical | ✓ |
| 17 | person | yes (object 18) | person | identical | ✓ |
| 18 | person | yes (object 19) | person | identical | ✓ |
| 19 | pingpong ball holder | yes (object 20) | bucket | semantic overlap | ✓ |
| 20 | wall | yes (object 21) | wall panel | hypernym/hyponym | ✓ |
| 21 | door | yes (object 22) | door | identical | ✓ |
| 22 | door | yes (object 23) | door (uncertain) | identical | ✓ |
| 23 | door | yes (object 24) | door | identical | ✓ |
| 24 | door | yes (object 25) | door | identical | ✓ |
| 25 | box | yes (object 26) | trash can | mismatch | ✗ |
| 26 | chair | yes (object 27) | chair | identical | ✓ |
| 27 | fencing | yes (object 28) | banner | mismatch | ✗ |
| 28 | table | yes (object 29) | table-tennis table | hypernym/hyponym | ✓ |
| 29 | table | yes (object 30) | table-tennis table | hypernym/hyponym | ✓ |
| 30 | water dispenser | yes (object 31) | chair | mismatch | ✗ |
| 31 | shirt | yes (object 32) | jersey | hypernym/hyponym | ✓ |
| 32 | shirt | yes (object 33) | jersey | hypernym/hyponym | ✓ |
| 33 | shirt | yes (object 34) | person | mismatch | ✗ |
| 34 | shirt | yes (object 35) | jersey | hypernym/hyponym | ✓ |
| 35 | clock | yes (object 36) | clock | identical | ✓ |
| 36 | head | yes (object 37) | person | mismatch | ✗ |
| 37 | head | yes (object 38) | person | mismatch | ✗ |
| 38 | head | yes (object 39) | ball | mismatch | ✗ |
| 39 | head | yes (object 40) | arm (uncertain) | mismatch | ✗ |

**Relations: 21/52 right, triplets: 20/52 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #1 - on - ground #0 | 0-23 | moving on (+1 more) | 0-24 | hypernym/hyponym | 0.96 | ✓ | ✓ |
| person #1 - playing table tennis with - person #2 | 0-23 | playing with (+3 more) | 0-24 | hypernym/hyponym | 0.96 | ✓ | ✓ |
| person #1 - competing with - person #2 | 0-23 | playing with (+3 more) | 0-24 | semantic overlap | 0.96 | ✓ | ✓ |
| person #1 - wearing - shirt #31 | 0-23 | wearing | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #1 - in front of - wall #6 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #1 - near - table #28 | 0-23 | in front of (+1 more) | 0-24 | hypernym/hyponym | 0.96 | ✓ | ✓ |
| person #2 - on - ground #0 | 0-23 | moving on (+1 more) | 0-24 | hypernym/hyponym | 0.96 | ✓ | ✓ |
| person #2 - wearing - shirt #32 | 0-23 | wearing | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #2 - in front of - wall #6 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #2 - near - table #28 | 0-23 | in front of (+1 more) | 0-24 | hypernym/hyponym | 0.96 | ✓ | ✓ |
| person #3 - on - ground #0 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #3 - wearing - shirt #33 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - playing table tennis with - person #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - competing with - person #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - in front of - wall #6 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #3 - behind - table #28 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - near - table #29 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - on - ground #0 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #4 - wearing - shirt #34 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - in front of - wall #6 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #4 - behind - table #28 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - near - table #29 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| pingpong ball holder #5 - on - ground #0 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ✓ |
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
| table #28 - on - ground #0 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ✓ |
| table #28 - in front of - wall #6 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| table #29 - in front of - wall #6 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| table #29 - behind - table #28 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| table #29 - on - ground #0 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ✓ |
| water dispenser #30 - on - ground #0 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ✗ |
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

**Objects: 13/23 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | car | yes (object 1) | car | identical | ✓ |
| 1 | car | yes (object 2) | SUV | hypernym/hyponym | ✓ |
| 2 | car | yes (object 3) | car | identical | ✓ |
| 3 | hand or glove | yes (object 4) | wheel | mismatch | ✗ |
| 4 | vehicle (uncertain) | yes (object 5) | person | mismatch | ✗ |
| 5 | vehicle (uncertain) | yes (object 6) | person | mismatch | ✗ |
| 6 | pole | yes (object 7) | snow plow (uncertain) | mismatch | ✗ |
| 7 | snow field | yes (object 8) | car | mismatch | ✗ |
| 8 | sky | yes (object 9) | snow | mismatch | ✗ |
| 9 | light | yes (object 10) | car | mismatch | ✗ |
| 10 | wheel | yes (object 11) | wheel | identical | ✓ |
| 11 | wheel | yes (object 12) | wheel | identical | ✓ |
| 12 | wheel | yes (object 13) | wheel | identical | ✓ |
| 13 | hood | yes (object 14) | windshield wiper | mismatch | ✗ |
| 14 | light | yes (object 15) | headlight (uncertain) | hypernym/hyponym | ✓ |
| 15 | light | yes (object 16) | headlight (uncertain) | hypernym/hyponym | ✓ |
| 16 | light | yes (object 17) | headlight (uncertain) | hypernym/hyponym | ✓ |
| 17 | engine | yes (object 18) | car hood | mismatch | ✗ |
| 18 | window | yes (object 19) | car | mismatch | ✗ |
| 19 | window | yes (object 20) | car window | hypernym/hyponym | ✓ |
| 20 | window | yes (object 21) | car window | hypernym/hyponym | ✓ |
| 21 | fender | yes (object 22) | car door | semantic overlap | ✓ |
| 22 | door | yes (object 23) | car door | hypernym/hyponym | ✓ |

**Relations: 2/25 right, triplets: 1/25 right** (lenient, tIoU > 0.5)

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
| car #0 - near - car #2 | 0-17.8333 | in front of | 0-18 | hypernym/hyponym | 0.99 | ✓ | ✓ |
| car #0 - in front of - vehicle (uncertain) #4 | 15.8333-20.1667 | in front of | 17-19 | identical | 0.46 | ✗ | ✗ |
| car #0 - near - vehicle (uncertain) #5 | 17-20 | in front of | 17-19 | hypernym/hyponym | 0.67 | ✓ | ✗ |
| fender #21 - part of - car #0 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand or glove #3 - in front of - car #0 | 2.33333-5 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (36): car #0 - in front of - light #9 [0-9]; car #0 - in front of - window #18 [0-15]; car #0 - in front of - window #19 [0-20]; car #0 - in front of - window #20 [0-20]; car #0 - in front of - door #22 [0-24]; car #0 - in front of - fender #21 [0-24]; car #0 - in front of - wheel #10 [0-17]; car #0 - in front of - wheel #11 [0-24]; car #0 - in front of - wheel #12 [0-1, 15-24]; car #0 - in front of - hand or glove #3 [0-3, 19-24]


## 66_927BvkIZglw

7.5 s, 8 frames read | human: 20 objects, 28 relations | TRASER: 20 objects, 25 relations, valid JSON, 1583 tokens

**Objects: 13/20 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | window | yes (object 1) | window | identical | ✓ |
| 1 | roof | yes (object 2) | ceiling | semantic overlap | ✓ |
| 2 | light | yes (object 3) | vent (uncertain) | mismatch | ✗ |
| 3 | television | yes (object 4) | television | identical | ✓ |
| 4 | indoor pool | yes (object 5) | bathtub | semantic overlap | ✓ |
| 5 | wall | yes (object 6) | wall panel | hypernym/hyponym | ✓ |
| 6 | wall | yes (object 7) | wall panel | hypernym/hyponym | ✓ |
| 7 | wall | yes (object 8) | door frame (uncertain) | mismatch | ✗ |
| 8 | water | yes (object 9) | bathtub | mismatch | ✗ |
| 9 | valve | yes (object 10) | remote control (uncertain) | mismatch | ✗ |
| 10 | valve | yes (object 11) | knob (uncertain) | semantic overlap | ✓ |
| 11 | valve | yes (object 12) | knob (uncertain) | semantic overlap | ✓ |
| 12 | valve | yes (object 13) | knob (uncertain) | semantic overlap | ✓ |
| 13 | headrest | yes (object 14) | handle (uncertain) | mismatch | ✗ |
| 14 | valve | yes (object 15) | knob (uncertain) | semantic overlap | ✓ |
| 15 | headrest | yes (object 16) | handle (uncertain) | mismatch | ✗ |
| 16 | window handle | yes (object 17) | hinge (uncertain) | semantic overlap | ✓ |
| 17 | glass | yes (object 18) | window | semantic overlap | ✓ |
| 18 | light | yes (object 19) | vent (uncertain) | mismatch | ✗ |
| 19 | window frame | yes (object 20) | window frame | identical | ✓ |

**Relations: 3/28 right, triplets: 3/28 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| window #0 - in - wall #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #0 - mounted on - wall #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #0 - below - roof #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #0 - above - indoor pool #4 | 0-8 | above | 0-8 | identical | 1.00 | ✓ | ✓ |
| window #0 - has - window handle #16 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #0 - has - glass #17 | 0-8 | adjacent to | 0-8 | mismatch | 1.00 | ✗ | ✗ |
| window #0 - has - window frame #19 | 0-8 | attached to (+1 more) | 0-8 | semantic overlap | 1.00 | ✓ | ✓ |
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
| window frame #19 - around - glass #17 | 0-8 | adjacent to | 0-8 | semantic overlap | 1.00 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (20): glass #17 - attached to - window frame #19 [0-8]; glass #17 - inside - window frame #19 [0-8]; window frame #19 - attached to - wall #5 [0-8]; window frame #19 - in front of - wall #5 [0-8]; window frame #19 - attached to - wall #6 [0-8]; television #3 - mounted on - wall #5 [6-8]; television #3 - on - wall #5 [6-8]; glass #17 - above - indoor pool #4 [0-8]; window frame #19 - above - indoor pool #4 [0-8]; roof #1 - above - indoor pool #4 [0-8]


## 670_JboU-y2LdkU

7.5 s, 8 frames read | human: 24 objects, 33 relations | TRASER: 24 objects, 86 relations, valid JSON, 2857 tokens

**Objects: 21/24 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | grass | yes (object 1) | lawn | synonym | ✓ |
| 1 | bush | yes (object 2) | bush | identical | ✓ |
| 2 | tree | yes (object 3) | bush | semantic overlap | ✓ |
| 3 | tree | yes (object 4) | bush | semantic overlap | ✓ |
| 4 | tree | yes (object 5) | bush | semantic overlap | ✓ |
| 5 | tree | yes (object 6) | bush | semantic overlap | ✓ |
| 6 | tree | yes (object 7) | tree | identical | ✓ |
| 7 | tree | yes (object 8) | car | mismatch | ✗ |
| 8 | tree | yes (object 9) | bush | semantic overlap | ✓ |
| 9 | tree | yes (object 10) | plant | hypernym/hyponym | ✓ |
| 10 | car | yes (object 11) | car | identical | ✓ |
| 11 | tree | yes (object 12) | bush | semantic overlap | ✓ |
| 12 | person | yes (object 13) | person | identical | ✓ |
| 13 | person | yes (object 14) | person | identical | ✓ |
| 14 | person | yes (object 15) | child | hypernym/hyponym | ✓ |
| 15 | person | yes (object 16) | person | identical | ✓ |
| 16 | person | yes (object 17) | person | identical | ✓ |
| 17 | person | yes (object 18) | person | identical | ✓ |
| 18 | person | yes (object 19) | person | identical | ✓ |
| 19 | forest | yes (object 20) | tree | semantic overlap | ✓ |
| 20 | wheel | yes (object 21) | wheel | identical | ✓ |
| 21 | headlight | yes (object 22) | car | mismatch | ✗ |
| 22 | headlight | yes (object 23) | wheel | mismatch | ✗ |
| 23 | windshield | yes (object 24) | car window | hypernym/hyponym | ✓ |

**Relations: 19/33 right, triplets: 19/33 right** (lenient, tIoU > 0.5)

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
| car #10 - parked on - grass #0 | 0-8 | on | 0-8 | hypernym/hyponym | 1.00 | ✓ | ✓ |
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
| wheel #20 - attached to - car #10 | 0-2, 5-6 | below | 0-8 | mismatch | 0.38 | ✗ | ✗ |
| wheel #20 - under - car #10 | 0-2, 5-6 | below | 0-8 | synonym | 0.38 | ✗ | ✗ |
| headlight #21 - attached to - car #10 | 0-4, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| headlight #21 - in front of - windshield #23 | 0-4, 7-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| headlight #22 - attached to - car #10 | 0-2, 4-5, 6-8 | below | 0-8 | mismatch | 0.62 | ✗ | ✗ |
| headlight #22 - in front of - windshield #23 | 0-2, 4-5, 7-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| windshield #23 - attached to - car #10 | 0-5, 7-8 | above | 0-8 | mismatch | 0.75 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (65): person #18 - approaches - tree #7 [0-8]; person #18 - moves away from - car #10 [0-8]; person #18 - approaches - person #14 [0-8]; person #18 - approaches - person #15 [0-8]; person #18 - approaches - person #16 [0-8]; person #18 - approaches - person #17 [0-8]; person #18 - approaches - tree #9 [0-8]; person #18 - approaches - headlight #21 [0-8]; person #18 - approaches - windshield #23 [0-8]; person #18 - approaches - wheel #20 [0-8]


## 700_zkhPzSZcRtQ

22.67 s, 23 frames read | human: 24 objects, 41 relations | TRASER: 24 objects, 116 relations, valid JSON, 3604 tokens

**Objects: 13/24 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | mat | yes (object 1) | mat | identical | ✓ |
| 1 | mat | yes (object 2) | crossbar (uncertain) | mismatch | ✗ |
| 2 | floor | yes (object 3) | person | mismatch | ✗ |
| 3 | pole | yes (object 4) | pole | identical | ✓ |
| 4 | man | yes (object 5) | person | hypernym/hyponym | ✓ |
| 5 | bat | yes (object 6) | handbag | mismatch | ✗ |
| 6 | wall | yes (object 7) | net | mismatch | ✗ |
| 7 | ball cart | yes (object 8) | shopping cart | semantic overlap | ✓ |
| 8 | stripe or mat | yes (object 9) | mat | identical | ✓ |
| 9 | stripe | yes (object 10) | mat | mismatch | ✗ |
| 10 | stripe | yes (object 11) | tape measure (uncertain) | mismatch | ✗ |
| 11 | wall poster | yes (object 12) | vent (uncertain) | mismatch | ✗ |
| 12 | wall poster | yes (object 13) | vent (uncertain) | mismatch | ✗ |
| 13 | wall poster | yes (object 14) | vent (uncertain) | mismatch | ✗ |
| 14 | wall poster | yes (object 15) | vent (uncertain) | mismatch | ✗ |
| 15 | strip | yes (object 16) | tape measure | semantic overlap | ✓ |
| 16 | posters | yes (object 17) | basketball backboard | mismatch | ✗ |
| 17 | shoe | yes (object 18) | shoe | identical | ✓ |
| 18 | shoe | yes (object 19) | shoe | identical | ✓ |
| 19 | hat | yes (object 20) | baseball cap | hypernym/hyponym | ✓ |
| 20 | hoodie | yes (object 21) | jacket | hypernym/hyponym | ✓ |
| 21 | pants | yes (object 22) | trousers (uncertain) | synonym | ✓ |
| 22 | ball cart | yes (object 23) | shopping cart | semantic overlap | ✓ |
| 23 | poster | yes (object 24) | banner | semantic overlap | ✓ |

**Relations: 8/41 right, triplets: 6/41 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| mat #0 - in front of - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| mat #0 - on - floor #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| mat #1 - on - floor #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| mat #1 - behind - mat #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| pole #3 - on - floor #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| pole #3 - in front of - wall #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #4 - in front of - wall #6 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✗ |
| man #4 - in front of - ball cart #7 | 0-23 | in front of (+1 more) | 0-24 | identical | 0.96 | ✓ | ✓ |
| man #4 - approaching - mat #0 | 18-21 | moving relative to (+1 more) | 0-24 | hypernym/hyponym | 0.12 | ✗ | ✗ |
| man #4 - moving away from - mat #0 | 20-23 | moving relative to (+1 more) | 0-24 | hypernym/hyponym | 0.12 | ✗ | ✗ |
| man #4 - on - floor #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #4 - walking on - floor #2 | 18-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #4 - holding - bat #5 | 0-23 | holding | 0-24 | identical | 0.96 | ✓ | ✗ |
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

**Objects: 10/13 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | fish | yes (object 1) | fishing rod (uncertain) | mismatch | ✗ |
| 1 | sky | yes (object 2) | sun | semantic overlap | ✓ |
| 2 | human | yes (object 3) | hand | semantic overlap | ✓ |
| 3 | Fishing Rod | yes (object 4) | fishing reel | semantic overlap | ✓ |
| 4 | shore or ground | yes (object 5) | rock | semantic overlap | ✓ |
| 5 | embankment | yes (object 6) | sand | mismatch | ✗ |
| 6 | river or canal | yes (object 7) | water | hypernym/hyponym | ✓ |
| 7 | shore | yes (object 8) | bridge (uncertain) | mismatch | ✗ |
| 8 | handle (grip) | yes (object 9) | fishing reel | semantic overlap | ✓ |
| 9 | reel | yes (object 10) | fishing rod (uncertain) | semantic overlap | ✓ |
| 10 | rod | yes (object 11) | fishing rod | hypernym/hyponym | ✓ |
| 11 | hand | yes (object 12) | hand | identical | ✓ |
| 12 | hand | yes (object 13) | hand | identical | ✓ |

**Relations: 6/26 right, triplets: 4/26 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| sky #1 - above - fish #0 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #1 - above - human #2 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #1 - above - Fishing Rod #3 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #1 - above - shore or ground #4 | 0-23.6667 | above | 0-23 | identical | 0.97 | ✓ | ✓ |
| sky #1 - above - embankment #5 | 0-23.6667 | above | 0-23 | identical | 0.97 | ✓ | ✗ |
| sky #1 - above - river or canal #6 | 0-23.6667 | above | 0-23 | identical | 0.97 | ✓ | ✓ |
| sky #1 - above - shore #7 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #1 - above - hand #11 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #1 - above - hand #12 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #1 - above - rod #10 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #1 - above - reel #9 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #1 - above - handle (grip) #8 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| reel #9 - attached to - Fishing Rod #3 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| rod #10 - attached to - Fishing Rod #3 | 0-23.6667 | attached to | 0-23 | identical | 0.97 | ✓ | ✓ |
| hand #12 - holding - handle (grip) #8 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #11 - operating - reel #9 | 0-5.16667 | nothing for this pair | - | - | - | ✗ | ✗ |
| human #2 - beside - river or canal #6 | 0-23.6667 | in front of | 0-23 | mismatch | 0.97 | ✗ | ✗ |
| human #2 - fishing in - river or canal #6 | 0-23.6667 | in front of | 0-23 | mismatch | 0.97 | ✗ | ✗ |
| shore or ground #4 - beside - river or canal #6 | 0-23.6667 | adjacent to | 0-23 | synonym | 0.97 | ✓ | ✓ |
| embankment #5 - beside - river or canal #6 | 0-23.6667 | adjacent to | 0-23 | synonym | 0.97 | ✓ | ✗ |
| human #2 - standing on - embankment #5 | 0-23.6667 | in front of | 0-23 | mismatch | 0.97 | ✗ | ✗ |
| human #2 - walking along - embankment #5 | 0-23.6667 | in front of | 0-23 | mismatch | 0.97 | ✗ | ✗ |
| human #2 - has - hand #11 | 0-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| fish #0 - caught by - human #2 | 1.66667-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| fish #0 - attached to - Fishing Rod #3 | 1.66667-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |
| fish #0 - above - river or canal #6 | 1.66667-23.6667 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (26): human #2 - holding - rod #10 [0-23]; human #2 - fishing with - rod #10 [0-23]; hand #12 - holding - rod #10 [0-23]; hand #12 - fishing with - rod #10 [0-23]; human #2 - holding - Fishing Rod #3 [0-23]; hand #12 - holding - Fishing Rod #3 [0-23]; rod #10 - attached to - handle (grip) #8 [0-23]; rod #10 - moving relative to - river or canal #6 [0-23]; rod #10 - in front of - river or canal #6 [0-23]; Fishing Rod #3 - moving relative to - river or canal #6 [0-23]


## 722__ajUvCkhVcI

22.67 s, 23 frames read | human: 18 objects, 39 relations | TRASER: 18 objects, 38 relations, valid JSON, 1581 tokens

**Objects: 12/18 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | baby | yes (object 1) | child | hypernym/hyponym | ✓ |
| 1 | baby | yes (object 2) | child | hypernym/hyponym | ✓ |
| 2 | baby | yes (object 3) | person | hypernym/hyponym | ✓ |
| 3 | ball pit | yes (object 4) | ball pit | identical | ✓ |
| 4 | side of a cage | yes (object 5) | net | semantic overlap | ✓ |
| 5 | side of a cage | yes (object 6) | net | semantic overlap | ✓ |
| 6 | rope | yes (object 7) | pole (uncertain) | mismatch | ✗ |
| 7 | rope | yes (object 8) | pole (uncertain) | mismatch | ✗ |
| 8 | shirt | yes (object 9) | jersey (uncertain) | hypernym/hyponym | ✓ |
| 9 | head | yes (object 10) | child | mismatch | ✗ |
| 10 | short | yes (object 11) | shorts (uncertain) | identical | ✓ |
| 11 | shirt | yes (object 12) | jersey (uncertain) | hypernym/hyponym | ✓ |
| 12 | top | yes (object 13) | jersey (uncertain) | hypernym/hyponym | ✓ |
| 13 | skirt | yes (object 14) | skirt | identical | ✓ |
| 14 | trouser | yes (object 15) | trousers | identical | ✓ |
| 15 | legs | yes (object 16) | sock (uncertain) | mismatch | ✗ |
| 16 | legs | yes (object 17) | shoe | mismatch | ✗ |
| 17 | legs | yes (object 18) | ball | mismatch | ✗ |

**Relations: 7/39 right, triplets: 7/39 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| baby #0 - inside - ball pit #3 | 0-23 | in | 0-24 | synonym | 0.96 | ✓ | ✓ |
| baby #0 - playing with - ball pit #3 | 0-23 | in | 0-24 | mismatch | 0.96 | ✗ | ✗ |
| baby #0 - in front of - side of a cage #5 | 0-23 | in front of (+1 more) | 0-24 | identical | 0.96 | ✓ | ✓ |
| baby #0 - wearing - shirt #8 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| baby #0 - wearing - short #10 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| baby #0 - looking at - baby #1 | 8-11 | next to | 0-24 | mismatch | 0.12 | ✗ | ✗ |
| baby #0 - in front of - baby #1 | 0-23 | next to | 0-24 | semantic overlap | 0.96 | ✓ | ✓ |
| baby #0 - looking at - baby #2 | 13-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| baby #0 - in front of - side of a cage #4 | 0-23 | in front of (+1 more) | 0-24 | identical | 0.96 | ✓ | ✓ |
| baby #1 - inside - ball pit #3 | 0-23 | in | 0-24 | synonym | 0.96 | ✓ | ✓ |
| baby #1 - wearing - shirt #11 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| baby #1 - wearing - trouser #14 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| baby #1 - holding - side of a cage #5 | 8-23 | in front of (+1 more) | 0-24 | mismatch | 0.62 | ✗ | ✗ |
| baby #1 - approaching - side of a cage #5 | 1-9 | in front of (+1 more) | 0-24 | mismatch | 0.33 | ✗ | ✗ |
| baby #1 - climbing - side of a cage #5 | 8.5-23 | in front of (+1 more) | 0-24 | mismatch | 0.60 | ✗ | ✗ |
| baby #1 - looking at - side of a cage #5 | 8-23 | in front of (+1 more) | 0-24 | mismatch | 0.62 | ✗ | ✗ |
| baby #1 - in front of - side of a cage #5 | 0-23 | in front of (+1 more) | 0-24 | identical | 0.96 | ✓ | ✓ |
| baby #1 - in front of - side of a cage #4 | 0-23 | in front of (+1 more) | 0-24 | identical | 0.96 | ✓ | ✓ |
| baby #2 - inside - ball pit #3 | 10-19 | behind | 11-24 | mismatch | 0.57 | ✗ | ✗ |
| baby #2 - playing with - ball pit #3 | 12-20 | behind | 11-24 | mismatch | 0.62 | ✗ | ✗ |
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

**Objects: 13/16 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | trees | yes (object 1) | tree | identical | ✓ |
| 1 | sky | yes (object 2) | cloud | semantic overlap | ✓ |
| 2 | grass | yes (object 3) | log | mismatch | ✗ |
| 3 | ground | yes (object 4) | rock | semantic overlap | ✓ |
| 4 | tree | yes (object 5) | log | semantic overlap | ✓ |
| 5 | grass | yes (object 6) | grass | identical | ✓ |
| 6 | man | yes (object 7) | person | hypernym/hyponym | ✓ |
| 7 | trees | yes (object 8) | leaf | hypernym/hyponym | ✓ |
| 8 | trees | yes (object 9) | branch | semantic overlap | ✓ |
| 9 | trees | yes (object 10) | plant | hypernym/hyponym | ✓ |
| 10 | hat | yes (object 11) | hat | identical | ✓ |
| 11 | gun | yes (object 12) | camera | mismatch | ✗ |
| 12 | glasses | yes (object 13) | sunglasses | hypernym/hyponym | ✓ |
| 13 | hand | yes (object 14) | glove | semantic overlap | ✓ |
| 14 | gloves | yes (object 15) | glove | identical | ✓ |
| 15 | whistle | yes (object 16) | flashlight | mismatch | ✗ |

**Relations: 16/25 right, triplets: 13/25 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| sky #1 - above - trees #0 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #2 - on - ground #3 | 0-7 | on | 0-7 | identical | 1.00 | ✓ | ✗ |
| grass #2 - in front of - trees #0 | 0-7 | in front of | 0-7 | identical | 1.00 | ✓ | ✗ |
| tree #4 - on - ground #3 | 0-7 | on | 0-7 | identical | 1.00 | ✓ | ✓ |
| tree #4 - in front of - trees #0 | 0-7 | in front of | 0-7 | identical | 1.00 | ✓ | ✓ |
| grass #5 - on - ground #3 | 0-5, 6-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #6 - wears - hat #10 | 0-7 | wearing | 0-7 | identical | 1.00 | ✓ | ✓ |
| man #6 - wears - glasses #12 | 0-7 | wearing | 0-7 | identical | 1.00 | ✓ | ✓ |
| man #6 - wears - gloves #14 | 0-7 | wearing | 0-7 | identical | 1.00 | ✓ | ✓ |
| man #6 - holds - gun #11 | 0-7 | holding (+1 more) | 0-7 | identical | 1.00 | ✓ | ✗ |
| man #6 - smokes - whistle #15 | 0-7 | holding (+1 more) | 0-7 | mismatch | 1.00 | ✗ | ✗ |
| man #6 - on - ground #3 | 0-7 | on | 0-7 | identical | 1.00 | ✓ | ✓ |
| man #6 - in front of - tree #4 | 0-7 | in front of (+1 more) | 0-7 | identical | 1.00 | ✓ | ✓ |
| man #6 - near - tree #4 | 0-7 | in front of (+1 more) | 0-7 | hypernym/hyponym | 1.00 | ✓ | ✓ |
| trees #9 - behind - trees #0 | 0-5, 6-7 | in front of | 0-6 | mismatch | 0.71 | ✗ | ✗ |
| hat #10 - on - man #6 | 0-7 | on | 0-7 | identical | 1.00 | ✓ | ✓ |
| hat #10 - above - glasses #12 | 0-7 | above | 0-7 | identical | 1.00 | ✓ | ✓ |
| hat #10 - above - hand #13 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| gun #11 - near - hand #13 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| glasses #12 - on - man #6 | 0-7 | on | 0-7 | identical | 1.00 | ✓ | ✓ |
| hand #13 - attached to - man #6 | 0-7 | on | 0-7 | hypernym/hyponym | 1.00 | ✓ | ✓ |
| gloves #14 - on - man #6 | 0-7 | on | 0-7 | identical | 1.00 | ✓ | ✓ |
| gloves #14 - on - hand #13 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| whistle #15 - below - hat #10 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| whistle #15 - near - glasses #12 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (19): man #6 - wearing - hand #13 [0-7]; gun #11 - on - ground #3 [0-7]; whistle #15 - on - ground #3 [0-7]; gun #11 - in front of - man #6 [0-7]; whistle #15 - in front of - man #6 [0-7]; gun #11 - in front of - tree #4 [0-7]; whistle #15 - in front of - tree #4 [0-7]; trees #0 - in front of - sky #1 [0-7]; man #6 - in front of - trees #0 [0-7]; gun #11 - near - whistle #15 [0-7]


## 744_1X6KvqPjk6I

7.5 s, 8 frames read | human: 32 objects, 26 relations | TRASER: 32 objects, 38 relations, valid JSON, 2394 tokens

**Objects: 20/32 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | dog | yes (object 1) | dog | identical | ✓ |
| 1 | tree | yes (object 2) | tree | identical | ✓ |
| 2 | plant | yes (object 3) | plant | identical | ✓ |
| 3 | fence | yes (object 4) | fence | identical | ✓ |
| 4 | grass | yes (object 5) | grass | identical | ✓ |
| 5 | plants, soil | yes (object 6) | soil | semantic overlap | ✓ |
| 6 | plant | yes (object 7) | plant | identical | ✓ |
| 7 | person | yes (object 8) | person | identical | ✓ |
| 8 | person | yes (object 9) | pole | mismatch | ✗ |
| 9 | hat | yes (object 10) | hat | identical | ✓ |
| 10 | hair | yes (object 11) | hair | identical | ✓ |
| 11 | tail | yes (object 12) | tail | identical | ✓ |
| 12 | dog leg | yes (object 13) | leg | hypernym/hyponym | ✓ |
| 13 | dog leg | yes (object 14) | dog's leg | identical | ✓ |
| 14 | dog leg | yes (object 15) | dog's leg | identical | ✓ |
| 15 | head | yes (object 16) | dog | mismatch | ✗ |
| 16 | barricade | yes (object 17) | wooden plank | mismatch | ✗ |
| 17 | barricade | yes (object 18) | wooden plank | mismatch | ✗ |
| 18 | stone | yes (object 19) | wooden block | mismatch | ✗ |
| 19 | gardening glove | yes (object 20) | flowerpot | mismatch | ✗ |
| 20 | fence | yes (object 21) | roof | mismatch | ✗ |
| 21 | pillar | yes (object 22) | pole | synonym | ✓ |
| 22 | fence | yes (object 23) | pole | mismatch | ✗ |
| 23 | fence | yes (object 24) | fence | identical | ✓ |
| 24 | pillar | yes (object 25) | pole | synonym | ✓ |
| 25 | fence | yes (object 26) | fence | identical | ✓ |
| 26 | wall | yes (object 27) | pole | mismatch | ✗ |
| 27 | wall | yes (object 28) | stick | mismatch | ✗ |
| 28 | pillar | yes (object 29) | pole | synonym | ✓ |
| 29 | pillar | yes (object 30) | pole | synonym | ✓ |
| 30 | fence | yes (object 31) | pole | mismatch | ✗ |
| 31 | trouser | yes (object 32) | wooden plank | mismatch | ✗ |

**Relations: 9/26 right, triplets: 9/26 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| dog #0 - looking at - grass #4 | 0-8 | on | 0-9 | mismatch | 0.89 | ✗ | ✗ |
| dog #0 - behind - barricade #17 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #0 - in front of - wall #27 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #4 - in front of - barricade #17 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants, soil #5 - in front of - person #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants, soil #5 - in front of - barricade #17 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #7 - wearing - hat #9 | 0-8 | wearing | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #7 - wearing - trouser #31 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #7 - pulling - plants, soil #5 | 0-8 | digging (+2 more) | 0-9 | mismatch | 0.89 | ✗ | ✗ |
| person #7 - looking at - plants, soil #5 | 0-8 | looking at (+2 more) | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #7 - weeding - plants, soil #5 | 0-8 | digging (+2 more) | 0-9 | semantic overlap | 0.89 | ✓ | ✓ |
| person #7 - holding - plants, soil #5 | 0-8 | digging (+2 more) | 0-9 | mismatch | 0.89 | ✗ | ✗ |
| person #7 - behind - barricade #17 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #7 - in front of - wall #27 | 0-8 | holding | 0-9 | mismatch | 0.89 | ✗ | ✗ |
| hat #9 - on - person #7 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✓ |
| hair #10 - on - person #7 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✓ |
| hair #10 - below - hat #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| tail #11 - part of - dog #0 | 0-8 | attached to | 0-9 | semantic overlap | 0.89 | ✓ | ✓ |
| dog leg #12 - part of - dog #0 | 0-8 | attached to | 0-9 | semantic overlap | 0.89 | ✓ | ✓ |
| dog leg #13 - part of - dog #0 | 0-8 | attached to | 0-9 | semantic overlap | 0.89 | ✓ | ✓ |
| dog leg #14 - part of - dog #0 | 0-8 | attached to | 0-9 | semantic overlap | 0.89 | ✓ | ✓ |
| head #15 - part of - dog #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| barricade #16 - in front of - person #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| stone #18 - on - barricade #16 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| gardening glove #19 - on - barricade #17 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| trouser #31 - on - person #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (26): dog #0 - has - tail #11 [0-9]; dog #0 - has - dog leg #12 [0-9]; dog #0 - has - dog leg #13 [0-9]; dog #0 - has - dog leg #14 [0-9]; head #15 - on - grass #4 [0-9]; dog #0 - in front of - fence #3 [0-9]; head #15 - in front of - fence #3 [0-9]; person #7 - in front of - fence #3 [0-9]; plant #2 - in front of - fence #3 [0-9]; plant #6 - in front of - fence #3 [0-9]


## 752_RWBJGgqDpwk

7.5 s, 8 frames read | human: 60 objects, 25 relations | TRASER: 40 objects, 45 relations, valid JSON, 3070 tokens

**Objects: 25/60 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | plant | yes (object 1) | plant | identical | ✓ |
| 1 | plant | yes (object 2) | flowerpot | semantic overlap | ✓ |
| 2 | bag | yes (object 3) | tarp | mismatch | ✗ |
| 3 | plant | yes (object 4) | soil bed | mismatch | ✗ |
| 4 | plant | yes (object 5) | soil bed | mismatch | ✗ |
| 5 | plant | yes (object 6) | plant | identical | ✓ |
| 6 | plant | yes (object 7) | soil bed | mismatch | ✗ |
| 7 | plant | yes (object 8) | flowerpot | semantic overlap | ✓ |
| 8 | plant | yes (object 9) | flowerpot | semantic overlap | ✓ |
| 9 | plant | yes (object 10) | flowerpot | semantic overlap | ✓ |
| 10 | plant bed | yes (object 11) | flowerpot | semantic overlap | ✓ |
| 11 | plant bed | yes (object 12) | flowerpot | semantic overlap | ✓ |
| 12 | plant bed | yes (object 13) | flowerpot | semantic overlap | ✓ |
| 13 | plant bed | yes (object 14) | flowerpot | semantic overlap | ✓ |
| 14 | plant bed | yes (object 15) | flowerpot | semantic overlap | ✓ |
| 15 | shovel | yes (object 16) | flowerpot | mismatch | ✗ |
| 16 | shovel | yes (object 17) | shovel | identical | ✓ |
| 17 | bucket | yes (object 18) | shovel | mismatch | ✗ |
| 18 | post | yes (object 19) | pole | synonym | ✓ |
| 19 | post | yes (object 20) | pole | synonym | ✓ |
| 20 | post | yes (object 21) | pole | synonym | ✓ |
| 21 | post | yes (object 22) | pole | synonym | ✓ |
| 22 | tree | yes (object 23) | tree trunk | semantic overlap | ✓ |
| 23 | stick | yes (object 24) | tree trunk | semantic overlap | ✓ |
| 24 | barricade | yes (object 25) | fence | synonym | ✓ |
| 25 | grass | yes (object 26) | lawn | synonym | ✓ |
| 26 | shovel | yes (object 27) | shovel | identical | ✓ |
| 27 | plant | yes (object 28) | flowerpot | semantic overlap | ✓ |
| 28 | grass | yes (object 29) | field | semantic overlap | ✓ |
| 29 | plant | yes (object 30) | stone block | mismatch | ✗ |
| 30 | man | yes (object 31) | person | hypernym/hyponym | ✓ |
| 31 | man | yes (object 32) | person | hypernym/hyponym | ✓ |
| 32 | wood | yes (object 33) | flowerpot | mismatch | ✗ |
| 33 | wood | yes (object 34) | flowerpot | mismatch | ✗ |
| 34 | wood | yes (object 35) | flowerpot | mismatch | ✗ |
| 35 | wood | yes (object 36) | soil bed | mismatch | ✗ |
| 36 | wood | yes (object 37) | flowerpot | mismatch | ✗ |
| 37 | wood | yes (object 38) | flowerpot | mismatch | ✗ |
| 38 | wood | yes (object 39) | flowerpot | mismatch | ✗ |
| 39 | wood | yes (object 40) | flowerpot | mismatch | ✗ |
| 40 | wood | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | wood | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | wood | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | wood | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | wood | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | wood | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | wood | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | face | no: after the first 40 | - | no label from TRASER | ✗ |
| 48 | shirt | no: after the first 40 | - | no label from TRASER | ✗ |
| 49 | hand | no: after the first 40 | - | no label from TRASER | ✗ |
| 50 | trouser | no: after the first 40 | - | no label from TRASER | ✗ |
| 51 | shoe | no: after the first 40 | - | no label from TRASER | ✗ |
| 52 | face | no: after the first 40 | - | no label from TRASER | ✗ |
| 53 | shirt | no: after the first 40 | - | no label from TRASER | ✗ |
| 54 | hand | no: after the first 40 | - | no label from TRASER | ✗ |
| 55 | hand | no: after the first 40 | - | no label from TRASER | ✗ |
| 56 | container | no: after the first 40 | - | no label from TRASER | ✗ |
| 57 | container | no: after the first 40 | - | no label from TRASER | ✗ |
| 58 | container | no: after the first 40 | - | no label from TRASER | ✗ |
| 59 | container | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 6/25 right, triplets: 1/25 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| bag #2 - moves across - wood #39 | 0-8 | on | 0-6 | mismatch | 0.75 | ✗ | ✗ |
| bag #2 - covering - wood #39 | 3-8 | on | 0-6 | hypernym/hyponym | 0.38 | ✗ | ✗ |
| bag #2 - over - plant #3 | 0-8 | covering (+2 more) | 0-6 | semantic overlap | 0.75 | ✓ | ✗ |
| plant #3 - inside - wood #39 | 0-8 | inside | 0-8 | identical | 1.00 | ✓ | ✗ |
| plant bed #10 - inside - wood #44 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bucket #17 - inside - wood #43 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| barricade #24 - behind - plant #5 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| shovel #26 - stuck in - grass #25 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #30 - holding - bag #2 | 0-8 | holding (+2 more) | 0-8 | identical | 1.00 | ✓ | ✗ |
| man #30 - cooperates with - man #31 | 0-8 | cooperating with | 0-8 | identical | 1.00 | ✓ | ✓ |
| man #30 - in front of - man #31 | 0-8 | cooperating with | 0-8 | mismatch | 1.00 | ✗ | ✗ |
| man #30 - approaches - wood #39 | 3-8 | in front of | 0-8 | mismatch | 0.62 | ✗ | ✗ |
| man #30 - covering bed with tarp - wood #39 | 0-8 | in front of | 0-8 | mismatch | 1.00 | ✗ | ✗ |
| man #30 - in front of - wood #39 | 4.5-8 | in front of | 0-8 | identical | 0.44 | ✗ | ✗ |
| man #31 - holding - bag #2 | 0-8 | holding (+2 more) | 0-8 | identical | 1.00 | ✓ | ✗ |
| man #31 - approaches - wood #39 | 3-8 | behind | 0-8 | mismatch | 0.62 | ✗ | ✗ |
| man #31 - covering bed with tarp - wood #39 | 0-8 | behind | 0-8 | mismatch | 1.00 | ✗ | ✗ |
| man #31 - behind - wood #39 | 0-8 | behind | 0-8 | identical | 1.00 | ✓ | ✗ |
| wood #36 - on - grass #25 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| wood #39 - on - grass #25 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| wood #44 - on - grass #25 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| container #56 - inside - container #59 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| container #57 - inside - container #59 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| container #58 - inside - container #59 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| container #59 - on - grass #25 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (31): man #30 - uncovering - plant #3 [5-8]; man #31 - uncovering - plant #3 [5-8]; barricade #24 - behind - wood #39 [0-8]; tree #22 - behind - wood #39 [0-8]; stick #23 - behind - wood #39 [0-8]; shovel #26 - behind - wood #39 [0-8]; plant #29 - behind - wood #39 [0-8]; plant #0 - in - plant #27 [0-8]; plant #5 - in - wood #32 [0-8]; shovel #16 - next to - bucket #17 [0-8]


## 754_TYUV8DYWe8k

22.67 s, 23 frames read | human: 28 objects, 26 relations | TRASER: 28 objects, 47 relations, valid JSON, 2196 tokens

**Objects: 19/28 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | building | yes (object 1) | truck | mismatch | ✗ |
| 1 | tree | yes (object 2) | tree | identical | ✓ |
| 2 | tree | yes (object 3) | tree | identical | ✓ |
| 3 | tree | yes (object 4) | tree | identical | ✓ |
| 4 | building | yes (object 5) | barn | hypernym/hyponym | ✓ |
| 5 | tree | yes (object 6) | tree | identical | ✓ |
| 6 | grass | yes (object 7) | grass | identical | ✓ |
| 7 | sky | yes (object 8) | clouds | semantic overlap | ✓ |
| 8 | dirt | yes (object 9) | soil | synonym | ✓ |
| 9 | grass | yes (object 10) | hill | semantic overlap | ✓ |
| 10 | hand | yes (object 11) | hand | identical | ✓ |
| 11 | bush | yes (object 12) | plant | hypernym/hyponym | ✓ |
| 12 | fence post | yes (object 13) | tree | mismatch | ✗ |
| 13 | stick | yes (object 14) | pole | synonym | ✓ |
| 14 | fence post | yes (object 15) | tree | mismatch | ✗ |
| 15 | stick | yes (object 16) | pole | synonym | ✓ |
| 16 | stick | yes (object 17) | pole | synonym | ✓ |
| 17 | stick | yes (object 18) | pole | synonym | ✓ |
| 18 | stick | yes (object 19) | pole | synonym | ✓ |
| 19 | stick | yes (object 20) | plant | semantic overlap | ✓ |
| 20 | storage | yes (object 21) | truck | mismatch | ✗ |
| 21 | storage | yes (object 22) | truck | mismatch | ✗ |
| 22 | storage | yes (object 23) | truck | mismatch | ✗ |
| 23 | stick | yes (object 24) | pole | synonym | ✓ |
| 24 | stick | yes (object 25) | pole | synonym | ✓ |
| 25 | side of house | yes (object 26) | tree | mismatch | ✗ |
| 26 | side of house | yes (object 27) | tree | mismatch | ✗ |
| 27 | roof | yes (object 28) | tree | mismatch | ✗ |

**Relations: 1/26 right, triplets: 1/26 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| building #0 - behind - grass #6 | 0-23 | on | 0-23 | mismatch | 1.00 | ✗ | ✗ |
| building #0 - beneath - sky #7 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #1 - beneath - sky #7 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #1 - behind - grass #6 | 0-23 | on | 0-23 | mismatch | 1.00 | ✗ | ✗ |
| tree #2 - beneath - sky #7 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #2 - behind - grass #6 | 0-23 | on | 0-23 | mismatch | 1.00 | ✗ | ✗ |
| tree #3 - beneath - sky #7 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #3 - behind - grass #6 | 0-23 | on | 0-23 | mismatch | 1.00 | ✗ | ✗ |
| building #4 - behind - grass #6 | 0-23 | on | 0-23 | mismatch | 1.00 | ✗ | ✗ |
| building #4 - beneath - sky #7 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #6 - in front of - sky #7 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #6 - above - dirt #8 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| dirt #8 - in front of - grass #6 | 0-23 | in front of | 0-23 | identical | 1.00 | ✓ | ✓ |
| hand #10 - above - dirt #8 | 0-1 | touching | 0-1 | mismatch | 1.00 | ✗ | ✗ |
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


## 761_liWqb_am68c

7.5 s, 8 frames read | human: 13 objects, 27 relations | TRASER: 13 objects, 19 relations, valid JSON, 1066 tokens

**Objects: 9/13 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | plants | yes (object 2) | leaves (uncertain) | semantic overlap | ✓ |
| 2 | structure | yes (object 3) | wooden plank (uncertain) | mismatch | ✗ |
| 3 | plants | yes (object 4) | leaves (uncertain) | semantic overlap | ✓ |
| 4 | trees | yes (object 5) | tree | identical | ✓ |
| 5 | baricade | yes (object 6) | fence | synonym | ✓ |
| 6 | floor | yes (object 7) | leaves (uncertain) | mismatch | ✗ |
| 7 | hair | yes (object 8) | hat (uncertain) | mismatch | ✗ |
| 8 | face | yes (object 9) | hat (uncertain) | mismatch | ✗ |
| 9 | hand | yes (object 10) | glove | semantic overlap | ✓ |
| 10 | hand | yes (object 11) | glove | semantic overlap | ✓ |
| 11 | shirt | yes (object 12) | shirt | identical | ✓ |
| 12 | trouser | yes (object 13) | jeans (uncertain) | hypernym/hyponym | ✓ |

**Relations: 4/27 right, triplets: 4/27 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - wearing - shirt #11 | 0-8 | wearing | 0-8 | identical | 1.00 | ✓ | ✓ |
| person #0 - wearing - trouser #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - approaching - plants #1 | 1-4 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - touching - plants #1 | 3-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - behind - plants #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - in front of - plants #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants #1 - attached to - structure #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants #1 - in front of - structure #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants #1 - in front of - baricade #5 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants #1 - in front of - plants #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| structure #2 - in front of - baricade #5 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants #3 - attached to - structure #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants #3 - behind - structure #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants #3 - in front of - baricade #5 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| baricade #5 - behind - person #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| baricade #5 - in front of - trees #4 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| hair #7 - attached to - person #0 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| hair #7 - above - face #8 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| face #8 - attached to - person #0 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #9 - attached to - person #0 | 0-8 | on | 0-8 | hypernym/hyponym | 1.00 | ✓ | ✓ |
| hand #9 - above - plants #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #9 - in front of - structure #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #10 - attached to - person #0 | 0-8 | on | 0-8 | hypernym/hyponym | 1.00 | ✓ | ✓ |
| hand #10 - above - plants #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #10 - in front of - structure #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #11 - on - person #0 | 0-8 | on | 0-8 | identical | 1.00 | ✓ | ✓ |
| trouser #12 - on - person #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (15): person #0 - wearing - hand #9 [0-8]; person #0 - wearing - hand #10 [0-8]; person #0 - handling - trees #4 [0-3]; person #0 - moving away from - trees #4 [2-4]; person #0 - in front of - trees #4 [0-4]; person #0 - in front of - baricade #5 [0-8]; hand #9 - below - shirt #11 [0-8]; hand #10 - below - shirt #11 [0-8]; hand #9 - near - hand #10 [0-8]; hand #9 - in front of - baricade #5 [0-8]


## 766_m1Vdl-EMY1E

22.67 s, 23 frames read | human: 20 objects, 32 relations | TRASER: 20 objects, 32 relations, valid JSON, 1545 tokens

**Objects: 15/20 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | field | yes (object 1) | baseball player | mismatch | ✗ |
| 1 | stadium | yes (object 2) | banner | mismatch | ✗ |
| 2 | sky | yes (object 3) | streetlight | mismatch | ✗ |
| 3 | light | yes (object 4) | streetlight | hypernym/hyponym | ✓ |
| 4 | person | yes (object 5) | person | identical | ✓ |
| 5 | person | yes (object 6) | baseball player | hypernym/hyponym | ✓ |
| 6 | person | yes (object 7) | person | identical | ✓ |
| 7 | person | yes (object 8) | person | identical | ✓ |
| 8 | person | yes (object 9) | person | identical | ✓ |
| 9 | person | yes (object 10) | person | identical | ✓ |
| 10 | person | yes (object 11) | person | identical | ✓ |
| 11 | person | yes (object 12) | person | identical | ✓ |
| 12 | person | yes (object 13) | baseball player | hypernym/hyponym | ✓ |
| 13 | baseball bat | yes (object 14) | baseball bat | identical | ✓ |
| 14 | hat | yes (object 15) | baseball cap | hypernym/hyponym | ✓ |
| 15 | pants | yes (object 16) | trousers (uncertain) | synonym | ✓ |
| 16 | sign | yes (object 17) | signboard | synonym | ✓ |
| 17 | foul line | yes (object 18) | baseball bat | mismatch | ✗ |
| 18 | display | yes (object 19) | scoreboard | hypernym/hyponym | ✓ |
| 19 | antenna | yes (object 20) | telephone pole (uncertain) | mismatch | ✗ |

**Relations: 11/32 right, triplets: 5/32 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| field #0 - below - sky #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| stadium #1 - behind - field #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| stadium #1 - below - sky #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #2 - above - stadium #1 | 0-23 | above | 0-24 | identical | 0.96 | ✓ | ✗ |
| sky #2 - above - field #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #3 - above - stadium #1 | 0-9 | above | 0-24 | identical | 0.38 | ✗ | ✗ |
| light #3 - above - field #0 | 0-9 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - wear - hat #14 | 0-23 | wearing | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #4 - wear - pants #15 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - on - field #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - move away from - person #12 | 19-23 | in front of | 0-24 | mismatch | 0.17 | ✗ | ✗ |
| person #4 - in front of - person #12 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #4 - in front of - stadium #1 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✗ |
| person #5 - wield - baseball bat #13 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - drop - baseball bat #13 | 19-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - move away from - person #12 | 19-23 | in front of | 0-24 | mismatch | 0.17 | ✗ | ✗ |
| person #5 - in front of - person #12 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✓ |
| person #5 - bat against - person #7 | 15-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - on - field #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - in front of - stadium #1 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✗ |
| person #7 - pitch to - person #5 | 15-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #7 - move toward - person #5 | 15-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #12 - on - field #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #12 - in front of - stadium #1 | 0-23 | in front of | 0-24 | identical | 0.96 | ✓ | ✗ |
| baseball bat #13 - move away from - person #5 | 19-23 | in front of | 0-24 | mismatch | 0.17 | ✗ | ✗ |
| baseball bat #13 - near - person #5 | 0-22 | in front of | 0-24 | hypernym/hyponym | 0.92 | ✓ | ✓ |
| hat #14 - on - person #4 | 0-23 | on | 0-24 | identical | 0.96 | ✓ | ✓ |
| pants #15 - on - person #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign #16 - on - stadium #1 | 0-23 | above | 0-24 | semantic overlap | 0.96 | ✓ | ✗ |
| foul line #17 - on - field #0 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| display #18 - on - stadium #1 | 0-23 | above | 0-24 | semantic overlap | 0.96 | ✓ | ✗ |
| antenna #19 - above - stadium #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (20): person #4 - holding - baseball bat #13 [0-24]; person #4 - looking at - person #5 [0-24]; person #4 - approaching - person #5 [0-11]; person #4 - moving away from - person #5 [11-24]; person #4 - coordinating with - person #5 [0-24]; person #4 - in front of - person #5 [0-24]; person #5 - looking at - person #4 [0-24]; baseball bat #13 - near - person #4 [0-24]; baseball bat #13 - in front of - stadium #1 [0-24]; foul line #17 - in front of - stadium #1 [0-24]


## 778_3PmDn84laac

7.5 s, 8 frames read | human: 23 objects, 27 relations | TRASER: 23 objects, 32 relations, valid JSON, 1786 tokens

**Objects: 19/23 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | smoke | yes (object 1) | smoke | identical | ✓ |
| 1 | tree | yes (object 2) | mountain | mismatch | ✗ |
| 2 | grass/trees/shrubs | yes (object 3) | bush | hypernym/hyponym | ✓ |
| 3 | train bridge | yes (object 4) | bridge | hypernym/hyponym | ✓ |
| 4 | sky | yes (object 5) | cloud | semantic overlap | ✓ |
| 5 | grass/trees | yes (object 6) | hill | semantic overlap | ✓ |
| 6 | train | yes (object 7) | train | identical | ✓ |
| 7 | train car | yes (object 8) | train car | identical | ✓ |
| 8 | train car | yes (object 9) | train car | identical | ✓ |
| 9 | train car | yes (object 10) | train car | identical | ✓ |
| 10 | cell phone tower | yes (object 11) | telephone pole | semantic overlap | ✓ |
| 11 | train car | yes (object 12) | train car | identical | ✓ |
| 12 | locomotive | yes (object 13) | locomotive | identical | ✓ |
| 13 | trees | yes (object 14) | tree | identical | ✓ |
| 14 | bushes | yes (object 15) | bush | identical | ✓ |
| 15 | bushes | yes (object 16) | bush | identical | ✓ |
| 16 | fence post | yes (object 17) | plant | mismatch | ✗ |
| 17 | fence post | yes (object 18) | pole | synonym | ✓ |
| 18 | stick | yes (object 19) | pole | synonym | ✓ |
| 19 | pole | yes (object 20) | pole | identical | ✓ |
| 20 | tree | yes (object 21) | pole | mismatch | ✗ |
| 21 | trees | yes (object 22) | plant | hypernym/hyponym | ✓ |
| 22 | trees | yes (object 23) | hill | mismatch | ✗ |

**Relations: 10/27 right, triplets: 6/27 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| smoke #0 - above - train bridge #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| smoke #0 - trails behind - train #6 | 0-8 | above | 0-8 | mismatch | 1.00 | ✗ | ✗ |
| smoke #0 - above - train #6 | 0-8 | above | 0-8 | identical | 1.00 | ✓ | ✓ |
| smoke #0 - rises in - sky #4 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| smoke #0 - in front of - sky #4 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| train bridge #3 - in front of - tree #1 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✗ |
| train bridge #3 - above - bushes #14 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #4 - above - tree #1 | 0-8 | above | 0-8 | identical | 1.00 | ✓ | ✗ |
| train #6 - moves past - tree #1 | 0-8 | in front of | 0-8 | semantic overlap | 1.00 | ✓ | ✗ |
| train #6 - in front of - tree #1 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✗ |
| train #6 - moves across - train bridge #3 | 0-8 | moving along (+3 more) | 0-8 | synonym | 1.00 | ✓ | ✓ |
| train #6 - on - train bridge #3 | 0-8 | moving along (+3 more) | 0-8 | semantic overlap | 1.00 | ✓ | ✓ |
| train #6 - above - grass/trees/shrubs #2 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| train #6 - in front of - trees #22 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| train car #7 - attached to - train #6 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| train car #7 - connected to - train #6 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| train car #8 - attached to - train #6 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| train car #8 - connected to - train #6 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| train car #9 - attached to - train #6 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| train car #9 - connected to - train #6 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| cell phone tower #10 - in front of - sky #4 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| train car #11 - attached to - train #6 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| train car #11 - connected to - train #6 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| train car #11 - moves across - train bridge #3 | 0-8 | on | 0-8 | mismatch | 1.00 | ✗ | ✗ |
| locomotive #12 - attached to - train #6 | 0-7 | attached to | 0-8 | identical | 0.88 | ✓ | ✓ |
| locomotive #12 - connected to - train #6 | 0-7 | attached to | 0-8 | synonym | 0.88 | ✓ | ✓ |
| bushes #14 - in front of - train bridge #3 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (21): locomotive #12 - moving along - train bridge #3 [0-8]; locomotive #12 - on - train bridge #3 [0-8]; smoke #0 - rising from - locomotive #12 [0-8]; smoke #0 - above - locomotive #12 [0-8]; smoke #0 - in front of - tree #1 [0-8]; grass/trees #5 - in front of - tree #1 [0-8]; trees #22 - in front of - tree #1 [0-8]; cell phone tower #10 - on - grass/trees #5 [0-8]; trees #13 - in front of - train bridge #3 [0-8]; grass/trees/shrubs #2 - in front of - train bridge #3 [0-8]


## 839_SS_1452uWvg

22.67 s, 23 frames read | human: 73 objects, 36 relations | TRASER: 40 objects, 96 relations, valid JSON, 3814 tokens

**Objects: 17/73 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | building | yes (object 1) | clock tower | hypernym/hyponym | ✓ |
| 1 | building | yes (object 2) | building | identical | ✓ |
| 2 | building | yes (object 3) | building | identical | ✓ |
| 3 | sky | yes (object 4) | clock tower | mismatch | ✗ |
| 4 | building | yes (object 5) | arch | semantic overlap | ✓ |
| 5 | pillar | yes (object 6) | column | synonym | ✓ |
| 6 | pillar | yes (object 7) | column | synonym | ✓ |
| 7 | arches | yes (object 8) | vent | mismatch | ✗ |
| 8 | arches | yes (object 9) | vent | mismatch | ✗ |
| 9 | window | yes (object 10) | window | identical | ✓ |
| 10 | window | yes (object 11) | window | identical | ✓ |
| 11 | window | yes (object 12) | window | identical | ✓ |
| 12 | window | yes (object 13) | window | identical | ✓ |
| 13 | pillar | yes (object 14) | window | mismatch | ✗ |
| 14 | pillar | yes (object 15) | window | mismatch | ✗ |
| 15 | pillar | yes (object 16) | window | mismatch | ✗ |
| 16 | pillar | yes (object 17) | window | mismatch | ✗ |
| 17 | pillar | yes (object 18) | window | mismatch | ✗ |
| 18 | pillar | yes (object 19) | window | mismatch | ✗ |
| 19 | pillar | yes (object 20) | column | synonym | ✓ |
| 20 | pillar | yes (object 21) | column | synonym | ✓ |
| 21 | pillar | yes (object 22) | column | synonym | ✓ |
| 22 | pillar | yes (object 23) | column | synonym | ✓ |
| 23 | pillar | yes (object 24) | window | mismatch | ✗ |
| 24 | pillar | yes (object 25) | window | mismatch | ✗ |
| 25 | pillar | yes (object 26) | window | mismatch | ✗ |
| 26 | pillar | yes (object 27) | window | mismatch | ✗ |
| 27 | pillar | yes (object 28) | window | mismatch | ✗ |
| 28 | pillar | yes (object 29) | window | mismatch | ✗ |
| 29 | pillar | yes (object 30) | window | mismatch | ✗ |
| 30 | pillar | yes (object 31) | window | mismatch | ✗ |
| 31 | statue | yes (object 32) | statue | identical | ✓ |
| 32 | statue | yes (object 33) | statue | identical | ✓ |
| 33 | window | yes (object 34) | window | identical | ✓ |
| 34 | pillar | yes (object 35) | window | mismatch | ✗ |
| 35 | pillar | yes (object 36) | window | mismatch | ✗ |
| 36 | pillar | yes (object 37) | window | mismatch | ✗ |
| 37 | pillar | yes (object 38) | window | mismatch | ✗ |
| 38 | pillar | yes (object 39) | window | mismatch | ✗ |
| 39 | pillar | yes (object 40) | window | mismatch | ✗ |
| 40 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | antenna | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | flower | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | wall | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | roof | no: after the first 40 | - | no label from TRASER | ✗ |
| 48 | building | no: after the first 40 | - | no label from TRASER | ✗ |
| 49 | door | no: after the first 40 | - | no label from TRASER | ✗ |
| 50 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 51 | door | no: after the first 40 | - | no label from TRASER | ✗ |
| 52 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 53 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 54 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 55 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 56 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 57 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 58 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 59 | doorway | no: after the first 40 | - | no label from TRASER | ✗ |
| 60 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 61 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 62 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 63 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 64 | pillar | no: after the first 40 | - | no label from TRASER | ✗ |
| 65 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 66 | arch | no: after the first 40 | - | no label from TRASER | ✗ |
| 67 | arch | no: after the first 40 | - | no label from TRASER | ✗ |
| 68 | frame | no: after the first 40 | - | no label from TRASER | ✗ |
| 69 | roof | no: after the first 40 | - | no label from TRASER | ✗ |
| 70 | arch | no: after the first 40 | - | no label from TRASER | ✗ |
| 71 | arch | no: after the first 40 | - | no label from TRASER | ✗ |
| 72 | door | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 21/36 right, triplets: 17/36 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| building #0 - in front of - sky #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| building #1 - in front of - sky #3 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| building #2 - in front of - sky #3 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| pillar #5 - attached to - building #0 | 0-23 | attached to (+1 more) | 0-24 | identical | 0.96 | ✓ | ✓ |
| pillar #5 - attached to - building #0 | 0-23 | attached to (+1 more) | 0-24 | identical | 0.96 | ✓ | ✓ |
| pillar #6 - attached to - building #0 | 0-23 | attached to (+1 more) | 0-24 | identical | 0.96 | ✓ | ✓ |
| pillar #6 - attached to - building #0 | 0-23 | attached to (+1 more) | 0-24 | identical | 0.96 | ✓ | ✓ |
| arches #7 - on - building #0 | 11-23 | on (+1 more) | 12-24 | identical | 0.85 | ✓ | ✗ |
| arches #7 - attached to - building #0 | 11-23 | built into (+1 more) | 12-24 | hypernym/hyponym | 0.85 | ✓ | ✗ |
| arches #8 - on - building #0 | 13-23 | on (+1 more) | 12-24 | identical | 0.83 | ✓ | ✗ |
| arches #8 - attached to - building #0 | 13-23 | built into (+1 more) | 12-24 | hypernym/hyponym | 0.83 | ✓ | ✗ |
| window #10 - in - building #0 | 0-23 | built into (+1 more) | 0-24 | semantic overlap | 0.96 | ✓ | ✓ |
| window #10 - attached to - building #0 | 0-23 | built into (+1 more) | 0-24 | hypernym/hyponym | 0.96 | ✓ | ✓ |
| window #10 - above - window #33 | 0-10 | above | 0-12 | identical | 0.83 | ✓ | ✓ |
| window #11 - in - building #0 | 0-23 | built into (+1 more) | 0-24 | semantic overlap | 0.96 | ✓ | ✓ |
| window #11 - attached to - building #0 | 0-23 | built into (+1 more) | 0-24 | hypernym/hyponym | 0.96 | ✓ | ✓ |
| pillar #21 - attached to - building #0 | 0-11 | attached to (+1 more) | 0-12 | identical | 0.92 | ✓ | ✓ |
| pillar #22 - attached to - building #0 | 0-11 | attached to (+1 more) | 0-12 | identical | 0.92 | ✓ | ✓ |
| statue #31 - attached to - building #0 | 0-15 | mounted on (+1 more) | 0-17 | synonym | 0.88 | ✓ | ✓ |
| statue #31 - attached to - building #0 | 0-15 | mounted on (+1 more) | 0-17 | synonym | 0.88 | ✓ | ✓ |
| statue #31 - above - window #33 | 0-10 | above | 0-12 | identical | 0.83 | ✓ | ✓ |
| statue #32 - attached to - building #0 | 0-15 | mounted on (+1 more) | 0-17 | synonym | 0.88 | ✓ | ✓ |
| statue #32 - attached to - building #0 | 0-15 | mounted on (+1 more) | 0-17 | synonym | 0.88 | ✓ | ✓ |
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


## 856_coe8HkbRIk4

20.17 s, 20 frames read | human: 25 objects, 33 relations | TRASER: 25 objects, 64 relations, valid JSON, 2483 tokens

**Objects: 18/25 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | golf club | yes (object 1) | golf club | identical | ✓ |
| 1 | golf | yes (object 2) | golf ball | mismatch | ✗ |
| 2 | fountain | yes (object 3) | water fountain | synonym | ✓ |
| 3 | ground | yes (object 4) | sand mound | semantic overlap | ✓ |
| 4 | trees | yes (object 5) | trees | identical | ✓ |
| 5 | house | yes (object 6) | building | hypernym/hyponym | ✓ |
| 6 | grass | yes (object 7) | golf course | semantic overlap | ✓ |
| 7 | ground | yes (object 8) | sand | semantic overlap | ✓ |
| 8 | person | yes (object 9) | person | identical | ✓ |
| 9 | street light | yes (object 10) | bush | mismatch | ✗ |
| 10 | street light | yes (object 11) | tree trunk | mismatch | ✗ |
| 11 | street light | yes (object 12) | tree trunk | mismatch | ✗ |
| 12 | sky | yes (object 13) | clouds | semantic overlap | ✓ |
| 13 | ground | yes (object 14) | tree | mismatch | ✗ |
| 14 | road | yes (object 15) | car | mismatch | ✗ |
| 15 | cap | yes (object 16) | baseball cap | hypernym/hyponym | ✓ |
| 16 | sweater | yes (object 17) | sweatshirt | synonym | ✓ |
| 17 | jean | yes (object 18) | pair of light blue jeans | identical | ✓ |
| 18 | shoe | yes (object 19) | shoe | identical | ✓ |
| 19 | shoe | yes (object 20) | shoe | identical | ✓ |
| 20 | hand | yes (object 21) | glove | semantic overlap | ✓ |
| 21 | hand | yes (object 22) | hand | identical | ✓ |
| 22 | face | yes (object 23) | face | identical | ✓ |
| 23 | head | yes (object 24) | golf club | mismatch | ✗ |
| 24 | stick | yes (object 25) | golf club | semantic overlap | ✓ |

**Relations: 16/33 right, triplets: 13/33 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #8 - holding - golf club #0 | 0.166667-21.1667 | holding (+1 more) | 0-20 | identical | 0.94 | ✓ | ✓ |
| person #8 - near - golf #1 | 0.166667-21.1667 | looking at | 0-20 | mismatch | 0.94 | ✗ | ✗ |
| person #8 - prepares to hit - golf #1 | 0.166667-21.1667 | looking at | 0-20 | mismatch | 0.94 | ✗ | ✗ |
| person #8 - looking at - golf #1 | 1.83333-8.66667, 12.6667-21.1667 | looking at | 0-20 | identical | 0.67 | ✓ | ✗ |
| person #8 - moves toward - golf #1 | 16-21.1667 | looking at | 0-20 | mismatch | 0.19 | ✗ | ✗ |
| person #8 - standing on - grass #6 | 0.166667-21.1667 | on | 0-20 | hypernym/hyponym | 0.94 | ✓ | ✓ |
| golf club #0 - near - golf #1 | 0.166667-21.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| golf #1 - in front of - person #8 | 0.166667-21.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| golf #1 - on - grass #6 | 0.166667-21.1667 | on | 0-20 | identical | 0.94 | ✓ | ✗ |
| cap #15 - worn by - person #8 | 0.166667-21.1667 | on | 0-20 | hypernym/hyponym | 0.94 | ✓ | ✓ |
| person #8 - facing - trees #4 | 7.66667-13.6667 | in front of | 0-20 | semantic overlap | 0.30 | ✗ | ✗ |
| sky #12 - above - house #5 | 0-21.1667 | above | 0-20 | identical | 0.94 | ✓ | ✓ |
| sky #12 - above - trees #4 | 0-21.1667 | above | 0-20 | identical | 0.94 | ✓ | ✓ |
| sky #12 - above - golf #1 | 0-21.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #12 - above - person #8 | 0-21.1667 | above | 0-20 | identical | 0.94 | ✓ | ✓ |
| sky #12 - above - ground #7 | 0-21.1667 | above | 0-20 | identical | 0.94 | ✓ | ✓ |
| sky #12 - above - fountain #2 | 0-21.1667 | above | 0-20 | identical | 0.94 | ✓ | ✓ |
| person #8 - wearing - sweater #16 | 0-21.1667 | wearing (+1 more) | 0-20 | identical | 0.94 | ✓ | ✓ |
| person #8 - wearing - jean #17 | 0-21.1667 | wearing (+1 more) | 0-20 | identical | 0.94 | ✓ | ✓ |
| person #8 - wearing - shoe #18 | 0-21.1667 | wearing (+1 more) | 0-20 | identical | 0.94 | ✓ | ✓ |
| person #8 - wearing - shoe #19 | 0-21.1667 | wearing (+1 more) | 0-20 | identical | 0.94 | ✓ | ✓ |
| sky #12 - above - ground #13 | 0-21.1667 | above | 0-20 | identical | 0.94 | ✓ | ✗ |
| sky #12 - above - grass #6 | 0-21.1667 | above | 0-20 | identical | 0.94 | ✓ | ✓ |
| house #5 - behind - person #8 | 0-21.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #4 - behind - person #8 | 0-21.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| fountain #2 - behind - person #8 | 0-21.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| ground #3 - behind - person #8 | 0-21.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| road #14 - behind - person #8 | 0-21.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| ground #13 - behind - person #8 | 0-21.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| stick #24 - part of - golf club #0 | 0-21.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| fountain #2 - in front of - trees #4 | 0-21.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| house #5 - in front of - trees #4 | 0-21.1667 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #8 - moving - hand #20 | 16.5-21.1667 | wearing (+1 more) | 0-20 | mismatch | 0.17 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (40): person #8 - wearing - cap #15 [0-20]; person #8 - wearing - cap #15 [0-20]; person #8 - holding - head #23 [0-20]; person #8 - swinging - head #23 [0-20]; person #8 - holding - stick #24 [0-20]; person #8 - swinging - stick #24 [0-20]; fountain #2 - on - grass #6 [0-20]; ground #3 - on - grass #6 [0-20]; ground #7 - on - grass #6 [0-20]; trees #4 - on - grass #6 [0-20]


## 888_BS3hab7EtAg

7.5 s, 8 frames read | human: 26 objects, 39 relations | TRASER: 26 objects, 66 relations, valid JSON, 2580 tokens

**Objects: 23/26 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | barricade | yes (object 1) | fence | synonym | ✓ |
| 1 | trunk | yes (object 2) | pole | semantic overlap | ✓ |
| 2 | building | yes (object 3) | house | hypernym/hyponym | ✓ |
| 3 | trees | yes (object 4) | tree | identical | ✓ |
| 4 | trees | yes (object 5) | tree | identical | ✓ |
| 5 | trees | yes (object 6) | tree | identical | ✓ |
| 6 | grass | yes (object 7) | grass | identical | ✓ |
| 7 | grass | yes (object 8) | bush | semantic overlap | ✓ |
| 8 | grass | yes (object 9) | grass | identical | ✓ |
| 9 | people | yes (object 10) | car | mismatch | ✗ |
| 10 | tiger | yes (object 11) | tiger | identical | ✓ |
| 11 | cow | yes (object 12) | bull | synonym | ✓ |
| 12 | trunk | yes (object 13) | pole | semantic overlap | ✓ |
| 13 | trunk | yes (object 14) | tree trunk | identical | ✓ |
| 14 | trunk | yes (object 15) | tree trunk | identical | ✓ |
| 15 | trunk | yes (object 16) | tree trunk | identical | ✓ |
| 16 | trunk | yes (object 17) | tree trunk | identical | ✓ |
| 17 | trunk | yes (object 18) | tree trunk | identical | ✓ |
| 18 | trunk | yes (object 19) | tree trunk | identical | ✓ |
| 19 | trunk | yes (object 20) | pole | semantic overlap | ✓ |
| 20 | trunk | yes (object 21) | pole | semantic overlap | ✓ |
| 21 | legs | yes (object 22) | leg | identical | ✓ |
| 22 | legs | yes (object 23) | tail | mismatch | ✗ |
| 23 | tail | yes (object 24) | tail | identical | ✓ |
| 24 | tiger head | yes (object 25) | tiger | semantic overlap | ✓ |
| 25 | ram head | yes (object 26) | cow's ear | mismatch | ✗ |

**Relations: 18/39 right, triplets: 15/39 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| trees #3 - in front of - barricade #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #3 - in front of - people #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #4 - in front of - barricade #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #4 - in front of - people #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #5 - in front of - barricade #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #5 - in front of - people #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #7 - on - grass #6 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #8 - on - grass #6 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| people #9 - behind - barricade #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| tiger #10 - on - grass #6 | 0-8 | moves across (+1 more) | 0-8 | semantic overlap | 1.00 | ✓ | ✓ |
| tiger #10 - in front of - trees #3 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| tiger #10 - in front of - trees #4 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| tiger #10 - in front of - trees #5 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| tiger #10 - in front of - barricade #0 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| tiger #10 - in front of - people #9 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✗ |
| tiger #10 - looking at - cow #11 | 0-8 | near (+3 more) | 0-8 | mismatch | 1.00 | ✗ | ✗ |
| tiger #10 - approaching - cow #11 | 0-8 | approaches (+3 more) | 0-4 | identical | 0.50 | ✗ | ✗ |
| tiger #10 - in front of - trunk #14 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| tiger #10 - in front of - trunk #17 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| cow #11 - on - grass #6 | 0-8 | moves across (+1 more) | 0-8 | semantic overlap | 1.00 | ✓ | ✓ |
| cow #11 - in front of - trees #3 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| cow #11 - in front of - trees #4 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| cow #11 - in front of - trees #5 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| cow #11 - in front of - barricade #0 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| cow #11 - in front of - people #9 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✗ |
| cow #11 - looking at - tiger #10 | 2-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| cow #11 - moving away from - tiger #10 | 2-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| cow #11 - approaching - tiger #10 | 5-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| cow #11 - in front of - trunk #14 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| cow #11 - in front of - trunk #17 | 0-8 | in front of | 0-8 | identical | 1.00 | ✓ | ✓ |
| trunk #14 - in front of - barricade #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| trunk #16 - in front of - barricade #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| trunk #17 - in front of - barricade #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| trunk #18 - in front of - barricade #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| legs #21 - under - cow #11 | 0-8 | attached to | 0-8 | mismatch | 1.00 | ✗ | ✗ |
| legs #22 - under - tiger #10 | 0-8 | attached to | 0-8 | mismatch | 1.00 | ✗ | ✗ |
| tail #23 - attached to - tiger #10 | 0-8 | attached to | 0-8 | identical | 1.00 | ✓ | ✓ |
| tiger head #24 - attached to - tiger #10 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| ram head #25 - attached to - cow #11 | 0-8 | attached to | 0-8 | identical | 1.00 | ✓ | ✗ |

TRASER relations between pairs the humans did not annotate (40): tiger head #24 - on - grass #6 [0-8]; tiger head #24 - in front of - barricade #0 [0-8]; tiger #10 - in front of - building #2 [0-8]; cow #11 - in front of - building #2 [0-8]; tiger head #24 - in front of - building #2 [0-8]; tiger head #24 - in front of - people #9 [0-8]; tiger head #24 - in front of - trees #3 [0-8]; tiger head #24 - in front of - trees #4 [0-8]; tiger head #24 - in front of - trees #5 [0-8]; tiger #10 - in front of - trunk #13 [0-5]


## 914_f4HgijyAEYs

7.5 s, 8 frames read | human: 19 objects, 21 relations | TRASER: 19 objects, 43 relations, valid JSON, 1882 tokens

**Objects: 10/19 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | cotton candy | yes (object 2) | cloud-like object (uncertain) | semantic overlap | ✓ |
| 2 | seat | yes (object 3) | signboard | mismatch | ✗ |
| 3 | ride | yes (object 4) | carousel | hypernym/hyponym | ✓ |
| 4 | landing | yes (object 5) | table | mismatch | ✗ |
| 5 | building | yes (object 6) | pole | mismatch | ✗ |
| 6 | circus | yes (object 7) | carousel | mismatch | ✗ |
| 7 | circus | yes (object 8) | carousel | mismatch | ✗ |
| 8 | circus | yes (object 9) | string of lights | mismatch | ✗ |
| 9 | sky | yes (object 10) | awning | mismatch | ✗ |
| 10 | seat | yes (object 11) | signboard | mismatch | ✗ |
| 11 | ground | yes (object 12) | table | mismatch | ✗ |
| 12 | light | yes (object 13) | light source (uncertain) | synonym | ✓ |
| 13 | light | yes (object 14) | light source (uncertain) | synonym | ✓ |
| 14 | glasses | yes (object 15) | spectacles | synonym | ✓ |
| 15 | hair | yes (object 16) | hair | identical | ✓ |
| 16 | jacket | yes (object 17) | jacket | identical | ✓ |
| 17 | hand | yes (object 18) | hand | identical | ✓ |
| 18 | hand | yes (object 19) | hand | identical | ✓ |

**Relations: 8/21 right, triplets: 6/21 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - holding - cotton candy #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - eating - cotton candy #1 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - snacking on - cotton candy #1 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - wearing - glasses #14 | 0-4, 5-8 | wearing | 0-9 | identical | 0.78 | ✓ | ✓ |
| person #0 - wearing - jacket #16 | 0-8 | wearing | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #0 - in front of - ride #3 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #0 - in front of - landing #4 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✗ |
| person #0 - in front of - building #5 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✗ |
| person #0 - under - sky #9 | 0-8 | in front of | 0-9 | mismatch | 0.89 | ✗ | ✗ |
| cotton candy #1 - in front of - person #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| cotton candy #1 - in front of - ride #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| cotton candy #1 - in front of - building #5 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| cotton candy #1 - below - sky #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| cotton candy #1 - above - light #12 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| cotton candy #1 - above - light #13 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| seat #2 - in front of - ride #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #12 - on - ride #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #13 - on - ride #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| glasses #14 - on - person #0 | 0-4, 5-8 | on | 0-9 | identical | 0.78 | ✓ | ✓ |
| hair #15 - on - person #0 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✓ |
| jacket #16 - on - person #0 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (34): person #0 - has - hair #15 [0-9]; person #0 - holding - hand #17 [0-9]; person #0 - looking at - hand #17 [0-9]; person #0 - holding - hand #18 [0-9]; person #0 - looking at - hand #18 [0-9]; person #0 - in front of - circus #6 [0-9]; person #0 - in front of - circus #7 [0-9]; person #0 - in front of - seat #10 [0-9]; person #0 - in front of - ground #11 [0-9]; person #0 - in front of - seat #2 [0-9]


## 950_94nfEhq6S5w

7.5 s, 8 frames read | human: 44 objects, 27 relations | TRASER: 40 objects, 46 relations, valid JSON, 2924 tokens

**Objects: 27/44 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | ceiling | yes (object 1) | ceiling | identical | ✓ |
| 1 | floor | yes (object 2) | floor | identical | ✓ |
| 2 | person | yes (object 3) | person | identical | ✓ |
| 3 | art | yes (object 4) | structure (uncertain) | hypernym/hyponym | ✓ |
| 4 | art | yes (object 5) | person | mismatch | ✗ |
| 5 | art | yes (object 6) | painting | hypernym/hyponym | ✓ |
| 6 | wall | yes (object 7) | wall | identical | ✓ |
| 7 | opening | yes (object 8) | door (uncertain) | semantic overlap | ✓ |
| 8 | person | yes (object 9) | person | identical | ✓ |
| 9 | wall | yes (object 10) | wall panel | hypernym/hyponym | ✓ |
| 10 | wall | yes (object 11) | wall | identical | ✓ |
| 11 | roof | yes (object 12) | light fixture (uncertain) | mismatch | ✗ |
| 12 | roof | yes (object 13) | vent (uncertain) | mismatch | ✗ |
| 13 | roof | yes (object 14) | light fixture (uncertain) | mismatch | ✗ |
| 14 | roof | yes (object 15) | vent (uncertain) | mismatch | ✗ |
| 15 | roof | yes (object 16) | light fixture (uncertain) | mismatch | ✗ |
| 16 | light | yes (object 17) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 17 | light | yes (object 18) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 18 | light | yes (object 19) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 19 | light | yes (object 20) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 20 | light | yes (object 21) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 21 | light | yes (object 22) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 22 | light | yes (object 23) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 23 | sloped wall | yes (object 24) | light fixture (uncertain) | mismatch | ✗ |
| 24 | ceiling | yes (object 25) | vent (uncertain) | semantic overlap | ✓ |
| 25 | ceiling | yes (object 26) | vent (uncertain) | semantic overlap | ✓ |
| 26 | wall plate | yes (object 27) | light fixture (uncertain) | mismatch | ✗ |
| 27 | ceiling | yes (object 28) | ceiling tile (uncertain) | semantic overlap | ✓ |
| 28 | light | yes (object 29) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 29 | light | yes (object 30) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 30 | bag | yes (object 31) | handbag | hypernym/hyponym | ✓ |
| 31 | jacket | yes (object 32) | dress | mismatch | ✗ |
| 32 | trousers | yes (object 33) | foot | mismatch | ✗ |
| 33 | trouser | yes (object 34) | foot | mismatch | ✗ |
| 34 | shoe | yes (object 35) | foot | semantic overlap | ✓ |
| 35 | shoe | yes (object 36) | foot | semantic overlap | ✓ |
| 36 | hair | yes (object 37) | hair | identical | ✓ |
| 37 | face | yes (object 38) | person | hypernym/hyponym | ✓ |
| 38 | hand | yes (object 39) | handbag | mismatch | ✗ |
| 39 | hair | yes (object 40) | person | mismatch | ✗ |
| 40 | bag | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | trouser | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | hand | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | light | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 10/27 right, triplets: 8/27 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| floor #1 - below - ceiling #0 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| floor #1 - adjacent to - wall #10 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| floor #1 - adjacent to - wall #9 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - wears - jacket #31 | 0-8 | wearing | 0-9 | identical | 0.89 | ✓ | ✗ |
| person #2 - carries - bag #30 | 0-8 | carrying | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #2 - approaches - art #3 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - looks at - art #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - approaches and observes - art #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - in front of - art #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - on - floor #1 | 0-8 | walking on (+1 more) | 0-9 | hypernym/hyponym | 0.89 | ✓ | ✓ |
| person #2 - in front of - wall #10 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✓ |
| art #3 - hangs on - wall #10 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| art #3 - attached to - wall #10 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| art #3 - on - floor #1 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| art #4 - hangs on - wall #10 | 0-8 | in front of | 0-9 | mismatch | 0.89 | ✗ | ✗ |
| art #4 - attached to - wall #10 | 0-8 | in front of | 0-9 | mismatch | 0.89 | ✗ | ✗ |
| art #5 - hangs on - wall #9 | 0-8 | on | 0-9 | hypernym/hyponym | 0.89 | ✓ | ✓ |
| art #5 - attached to - wall #9 | 0-8 | on | 0-9 | hypernym/hyponym | 0.89 | ✓ | ✓ |
| person #8 - carries - bag #40 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #8 - moves toward - wall #9 | 0-8 | in front of | 0-9 | mismatch | 0.89 | ✗ | ✗ |
| person #8 - in front of - wall #9 | 0-8 | in front of | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #8 - on - floor #1 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✓ |
| person #8 - in front of - art #5 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| wall plate #26 - on - wall #10 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bag #30 - on - person #2 | 1-8 | on | 0-9 | identical | 0.78 | ✓ | ✓ |
| jacket #31 - on - person #2 | 0-8 | on | 0-9 | identical | 0.89 | ✓ | ✗ |
| bag #40 - on - person #8 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (35): person #2 - has - hair #36 [0-9]; person #2 - approaching - art #5 [0-9]; person #2 - in front of - art #5 [0-9]; person #2 - approaching - art #4 [0-9]; person #2 - approaching - person #8 [0-9]; person #2 - moving away from - wall #9 [0-9]; person #2 - in front of - wall #9 [0-9]; art #4 - on - floor #1 [0-9]; face #37 - on - floor #1 [0-9]; hair #39 - on - floor #1 [0-9]


## 973_ceJ5D6wluX0

22.67 s, 23 frames read | human: 7 objects, 18 relations | TRASER: 7 objects, 8 relations, valid JSON, 544 tokens

**Objects: 5/7 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | smoke | yes (object 1) | smoke | identical | ✓ |
| 1 | train | yes (object 2) | train car | semantic overlap | ✓ |
| 2 | railway bridge | yes (object 3) | bridge | hypernym/hyponym | ✓ |
| 3 | trees | yes (object 4) | hill | mismatch | ✗ |
| 4 | sky | yes (object 5) | tree | mismatch | ✗ |
| 5 | train cars | yes (object 6) | train car | identical | ✓ |
| 6 | locomotive | yes (object 7) | steam locomotive | hypernym/hyponym | ✓ |

**Relations: 5/18 right, triplets: 5/18 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| smoke #0 - follows - locomotive #6 | 0-23 | rising from | 0-24 | mismatch | 0.96 | ✗ | ✗ |
| smoke #0 - above - locomotive #6 | 0-23 | rising from | 0-24 | mismatch | 0.96 | ✗ | ✗ |
| smoke #0 - rises toward - sky #4 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| smoke #0 - above - train #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| smoke #0 - above - railway bridge #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| train #1 - moves along - railway bridge #2 | 0-23 | moving along | 0-24 | identical | 0.96 | ✓ | ✓ |
| train #1 - crosses - railway bridge #2 | 0-23 | moving along | 0-24 | semantic overlap | 0.96 | ✓ | ✓ |
| train #1 - on - railway bridge #2 | 0-23 | moving along | 0-24 | semantic overlap | 0.96 | ✓ | ✓ |
| railway bridge #2 - carries - train #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #4 - above - trees #3 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #4 - above - railway bridge #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #4 - above - train #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| train cars #5 - attached to - locomotive #6 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| train cars #5 - on - railway bridge #2 | 0-23 | moving along | 0-24 | semantic overlap | 0.96 | ✓ | ✓ |
| locomotive #6 - leads - train cars #5 | 0-23 | attached to | 0-24 | mismatch | 0.96 | ✗ | ✗ |
| locomotive #6 - pulls - train cars #5 | 0-23 | attached to | 0-24 | mismatch | 0.96 | ✗ | ✗ |
| locomotive #6 - in front of - train cars #5 | 0-23 | attached to | 0-24 | mismatch | 0.96 | ✗ | ✗ |
| locomotive #6 - on - railway bridge #2 | 0-23 | moving along (+1 more) | 0-24 | semantic overlap | 0.96 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (2): locomotive #6 - attached to - train #1 [0-24]; train #1 - attached to - train cars #5 [0-24]


## 976_U19VojbI0h4

7.5 s, 8 frames read | human: 65 objects, 36 relations | TRASER: 40 objects, 49 relations, valid JSON, 3175 tokens

**Objects: 28/65 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | ground | yes (object 1) | floor | synonym | ✓ |
| 1 | painting | yes (object 2) | painting | identical | ✓ |
| 2 | plant | yes (object 3) | flower arrangement | hypernym/hyponym | ✓ |
| 3 | decoration | yes (object 4) | basket | mismatch | ✗ |
| 4 | fireplace | yes (object 5) | fireplace | identical | ✓ |
| 5 | cabinet | yes (object 6) | fireplace | mismatch | ✗ |
| 6 | door | yes (object 7) | door | identical | ✓ |
| 7 | wall | yes (object 8) | wall | identical | ✓ |
| 8 | door | yes (object 9) | door frame (uncertain) | semantic overlap | ✓ |
| 9 | lamp | yes (object 10) | lamp | identical | ✓ |
| 10 | table | yes (object 11) | coffee table | hypernym/hyponym | ✓ |
| 11 | interior | yes (object 12) | shelf | semantic overlap | ✓ |
| 12 | shelf | yes (object 13) | shelf | identical | ✓ |
| 13 | interior | yes (object 14) | plant | mismatch | ✗ |
| 14 | ceiling fan | yes (object 15) | ceiling tile (uncertain) | semantic overlap | ✓ |
| 15 | ceiling and upper wall | yes (object 16) | ceiling beam (uncertain) | semantic overlap | ✓ |
| 16 | closet | yes (object 17) | door | mismatch | ✗ |
| 17 | outlet | yes (object 18) | door handle | mismatch | ✗ |
| 18 | table | yes (object 19) | coffee table | hypernym/hyponym | ✓ |
| 19 | rug | yes (object 20) | coffee table | mismatch | ✗ |
| 20 | vase | yes (object 21) | flowerpot | synonym | ✓ |
| 21 | doorway | yes (object 22) | door | semantic overlap | ✓ |
| 22 | wall | yes (object 23) | wall | identical | ✓ |
| 23 | wall | yes (object 24) | shelf | mismatch | ✗ |
| 24 | wall | yes (object 25) | wall | identical | ✓ |
| 25 | lamp shade | yes (object 26) | lampshade | identical | ✓ |
| 26 | lamp base | yes (object 27) | lamp | semantic overlap | ✓ |
| 27 | throw pillow | yes (object 28) | table | mismatch | ✗ |
| 28 | couch | yes (object 29) | coffee table | mismatch | ✗ |
| 29 | cup | yes (object 30) | flowerpot | mismatch | ✗ |
| 30 | leaves | yes (object 31) | flowerpot | mismatch | ✗ |
| 31 | fireplace | yes (object 32) | fireplace | identical | ✓ |
| 32 | fireplace face | yes (object 33) | fireplace | hypernym/hyponym | ✓ |
| 33 | ceiling area | yes (object 34) | beam (uncertain) | hypernym/hyponym | ✓ |
| 34 | fireplace frame | yes (object 35) | door frame (uncertain) | semantic overlap | ✓ |
| 35 | flower vase | yes (object 36) | flowerpot | synonym | ✓ |
| 36 | vase | yes (object 37) | flowerpot | synonym | ✓ |
| 37 | home decor | yes (object 38) | flowerpot | hypernym/hyponym | ✓ |
| 38 | home decor | yes (object 39) | flowerpot | hypernym/hyponym | ✓ |
| 39 | socket | yes (object 40) | flowerpot | mismatch | ✗ |
| 40 | flower | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | vase stand | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | tray | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | fan | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | cupboard handle | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | cupboard handle | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | flower vase | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | flower stand | no: after the first 40 | - | no label from TRASER | ✗ |
| 48 | vase | no: after the first 40 | - | no label from TRASER | ✗ |
| 49 | home decor | no: after the first 40 | - | no label from TRASER | ✗ |
| 50 | glass | no: after the first 40 | - | no label from TRASER | ✗ |
| 51 | fireplace | no: after the first 40 | - | no label from TRASER | ✗ |
| 52 | door | no: after the first 40 | - | no label from TRASER | ✗ |
| 53 | ground | no: after the first 40 | - | no label from TRASER | ✗ |
| 54 | door | no: after the first 40 | - | no label from TRASER | ✗ |
| 55 | shelf | no: after the first 40 | - | no label from TRASER | ✗ |
| 56 | shelf | no: after the first 40 | - | no label from TRASER | ✗ |
| 57 | shelf | no: after the first 40 | - | no label from TRASER | ✗ |
| 58 | household item | no: after the first 40 | - | no label from TRASER | ✗ |
| 59 | wall | no: after the first 40 | - | no label from TRASER | ✗ |
| 60 | light | no: after the first 40 | - | no label from TRASER | ✗ |
| 61 | door frame | no: after the first 40 | - | no label from TRASER | ✗ |
| 62 | top of a cupboard | no: after the first 40 | - | no label from TRASER | ✗ |
| 63 | door of cupboard | no: after the first 40 | - | no label from TRASER | ✗ |
| 64 | door of cupboard | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 7/36 right, triplets: 5/36 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| painting #1 - on - fireplace face #32 | 0-8 | above | 0-8 | semantic overlap | 1.00 | ✓ | ✓ |
| painting #1 - in front of - wall #22 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| painting #1 - above - fireplace #4 | 0-8 | above | 0-8 | identical | 1.00 | ✓ | ✓ |
| plant #2 - on - fireplace face #32 | 0-8 | above | 0-8 | semantic overlap | 1.00 | ✓ | ✓ |
| plant #2 - in - flower vase #46 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plant #2 - in front of - wall #22 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| plant #2 - above - fireplace #4 | 0-8 | above | 0-8 | identical | 1.00 | ✓ | ✓ |
| decoration #3 - on - fireplace face #32 | 0-5.5 | above | 0-6 | semantic overlap | 0.92 | ✓ | ✗ |
| decoration #3 - in front of - wall #22 | 0-5.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| fireplace #4 - in - wall #22 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| fireplace #4 - against - wall #22 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| cabinet #5 - on - ground #0 | 0-4 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #6 - attached to - closet #16 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #6 - inside - door frame #61 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #6 - attached to - door frame #61 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #6 - in - wall #59 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #8 - inside - wall #7 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| lamp #9 - on - table #10 | 0-1 | on (+1 more) | 0-2 | identical | 0.50 | ✗ | ✗ |
| closet #16 - behind - door #54 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| table #18 - on - ground #0 | 0-7 | on | 0-2 | identical | 0.29 | ✗ | ✗ |
| rug #19 - on - ground #0 | 0-2 | on | 0-2 | identical | 1.00 | ✓ | ✗ |
| vase #20 - on - table #18 | 0-2 | on | 0-2 | identical | 1.00 | ✓ | ✓ |
| doorway #21 - in - fireplace frame #34 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| doorway #21 - in - fireplace frame #34 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| fireplace #31 - in - wall #22 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| fireplace #31 - under - fireplace face #32 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| fireplace face #32 - against - wall #22 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| flower vase #46 - on - flower stand #47 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #52 - inside - doorway #21 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| ground #53 - inside - doorway #21 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #54 - attached to - door frame #61 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #54 - inside - door frame #61 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #54 - in - wall #59 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| shelf #55 - in - closet #16 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| shelf #56 - in - closet #16 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| shelf #57 - in - closet #16 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (39): outlet #17 - attached to - doorway #21 [0-8]; outlet #17 - on - doorway #21 [0-8]; painting #1 - mounted on - wall #7 [0-8]; plant #2 - mounted on - wall #7 [0-8]; decoration #3 - mounted on - wall #7 [0-6]; interior #11 - mounted on - wall #24 [0-4]; shelf #12 - mounted on - wall #24 [0-4]; wall #23 - mounted on - wall #24 [0-4]; interior #13 - in - flower vase #35 [0-4]; interior #13 - above - flower vase #35 [0-4]


## 987_g0mln-jiQTw

22.67 s, 23 frames read | human: 11 objects, 17 relations | TRASER: 11 objects, 22 relations, valid JSON, 958 tokens

**Objects: 7/11 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | waterfalls | yes (object 1) | waterfall | identical | ✓ |
| 1 | trees | yes (object 2) | foliage (uncertain) | semantic overlap | ✓ |
| 2 | trees | yes (object 3) | foliage | semantic overlap | ✓ |
| 3 | sky | yes (object 4) | cloud | semantic overlap | ✓ |
| 4 | person | yes (object 5) | person | identical | ✓ |
| 5 | head | yes (object 6) | person | mismatch | ✗ |
| 6 | shirt | yes (object 7) | person | mismatch | ✗ |
| 7 | rock | yes (object 8) | bush | mismatch | ✗ |
| 8 | rock | yes (object 9) | waterfall | mismatch | ✗ |
| 9 | rock | yes (object 10) | rock | identical | ✓ |
| 10 | rock | yes (object 11) | rock formation | hypernym/hyponym | ✓ |

**Relations: 5/17 right, triplets: 3/17 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| waterfalls #0 - flows over - rock #8 | 0-23 | overlapping | 0-24 | semantic overlap | 0.96 | ✓ | ✗ |
| waterfalls #0 - on - rock #8 | 0-23 | overlapping | 0-24 | semantic overlap | 0.96 | ✓ | ✗ |
| waterfalls #0 - flows past - trees #2 | 0-23 | flows past | 0-24 | identical | 0.96 | ✓ | ✓ |
| waterfalls #0 - in front of - trees #2 | 0-23 | flows past | 0-24 | mismatch | 0.96 | ✗ | ✗ |
| waterfalls #0 - flows beside - rock #9 | 0-23 | flows over (+1 more) | 0-24 | semantic overlap | 0.96 | ✓ | ✓ |
| waterfalls #0 - on - rock #9 | 0-23 | flows over (+1 more) | 0-24 | semantic overlap | 0.96 | ✓ | ✓ |
| waterfalls #0 - below - rock #10 | 0-23 | flows past (+1 more) | 0-24 | mismatch | 0.96 | ✗ | ✗ |
| waterfalls #0 - in front of - trees #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #3 - above - trees #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #3 - above - trees #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - wears - shirt #6 | 18.5-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - in front of - trees #1 | 19-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| head #5 - in front of - trees #1 | 18-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #6 - on - person #4 | 19-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| rock #7 - in front of - trees #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| rock #8 - in front of - trees #1 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |
| rock #8 - in front of - trees #2 | 0-23 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (16): waterfalls #0 - flows past - rock #7 [0-24]; rock #8 - in front of - rock #10 [0-24]; rock #9 - in front of - rock #10 [0-24]; trees #2 - in front of - rock #10 [0-24]; rock #7 - in front of - rock #10 [0-24]; rock #8 - above - rock #9 [0-24]; trees #2 - overlapping - rock #7 [0-24]; sky #3 - above - rock #10 [0-24]; sky #3 - above - waterfalls #0 [0-24]; sky #3 - above - rock #8 [0-24]


## sav_002789

13.25 s, 13 frames read | human: 47 objects, 41 relations | TRASER: 40 objects, 46 relations, valid JSON, 2878 tokens

**Objects: 27/47 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | man | yes (object 1) | person | hypernym/hyponym | ✓ |
| 1 | woman | yes (object 2) | person | hypernym/hyponym | ✓ |
| 2 | man | yes (object 3) | person | hypernym/hyponym | ✓ |
| 3 | object | yes (object 4) | person | hypernym/hyponym | ✓ |
| 4 | road | yes (object 5) | person | mismatch | ✗ |
| 5 | man | yes (object 6) | jersey (uncertain) | mismatch | ✗ |
| 6 | suitcase | yes (object 7) | suitcase | identical | ✓ |
| 7 | people | yes (object 8) | person | hypernym/hyponym | ✓ |
| 8 | light | yes (object 9) | streetlight | hypernym/hyponym | ✓ |
| 9 | light | yes (object 10) | streetlight | hypernym/hyponym | ✓ |
| 10 | light | yes (object 11) | streetlight | hypernym/hyponym | ✓ |
| 11 | people | yes (object 12) | person | hypernym/hyponym | ✓ |
| 12 | light | yes (object 13) | streetlight | hypernym/hyponym | ✓ |
| 13 | light | yes (object 14) | streetlight | hypernym/hyponym | ✓ |
| 14 | light | yes (object 15) | streetlight | hypernym/hyponym | ✓ |
| 15 | building | yes (object 16) | building | identical | ✓ |
| 16 | sidewalk | yes (object 17) | car | mismatch | ✗ |
| 17 | sky | yes (object 18) | streetlight | mismatch | ✗ |
| 18 | trees | yes (object 19) | tree | identical | ✓ |
| 19 | people | yes (object 20) | person | hypernym/hyponym | ✓ |
| 20 | t-shirt | yes (object 21) | jersey (uncertain) | semantic overlap | ✓ |
| 21 | t-shirt | yes (object 22) | jersey (uncertain) | semantic overlap | ✓ |
| 22 | pants | yes (object 23) | trousers (uncertain) | synonym | ✓ |
| 23 | pants | yes (object 24) | trousers (uncertain) | synonym | ✓ |
| 24 | t-shirt | yes (object 25) | jersey (uncertain) | semantic overlap | ✓ |
| 25 | shorts | yes (object 26) | shorts (uncertain) | identical | ✓ |
| 26 | shoe | yes (object 27) | shoe | identical | ✓ |
| 27 | shoe | yes (object 28) | shoe | identical | ✓ |
| 28 | shirt | yes (object 29) | jacket | semantic overlap | ✓ |
| 29 | pants | yes (object 30) | trousers (uncertain) | synonym | ✓ |
| 30 | t-shirt | yes (object 31) | jersey (uncertain) | semantic overlap | ✓ |
| 31 | shorts | yes (object 32) | jersey (uncertain) | mismatch | ✗ |
| 32 | window | yes (object 33) | signboard | mismatch | ✗ |
| 33 | window | yes (object 34) | signboard | mismatch | ✗ |
| 34 | window | yes (object 35) | signboard | mismatch | ✗ |
| 35 | window | yes (object 36) | signboard | mismatch | ✗ |
| 36 | window | yes (object 37) | signboard | mismatch | ✗ |
| 37 | window | yes (object 38) | signboard | mismatch | ✗ |
| 38 | window | yes (object 39) | signboard | mismatch | ✗ |
| 39 | window | yes (object 40) | signboard | mismatch | ✗ |
| 40 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | shadow | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | shadow | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 1/41 right, triplets: 1/41 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| man #0 - walking along - road #4 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - on - road #4 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - wearing - t-shirt #21 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - wearing - pants #22 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - in front of - man #2 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - in front of - man #5 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #1 - walking along - road #4 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #1 - on - road #4 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #1 - wearing - t-shirt #20 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #1 - wearing - pants #23 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #1 - in front of - man #2 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #1 - in front of - man #5 | 1-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #2 - moving with - man #5 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #2 - walking along - road #4 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #2 - on - road #4 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #2 - wearing - t-shirt #24 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #2 - wearing - shorts #25 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| object #3 - walking along - road #4 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| object #3 - on - road #4 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| object #3 - wearing - shirt #28 | 0-14 | wearing | 0-13 | identical | 0.93 | ✓ | ✓ |
| object #3 - wearing - pants #29 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| object #3 - in front of - man #2 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| object #3 - in front of - man #5 | 1-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #5 - pulling - suitcase #6 | 1-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #5 - transporting - suitcase #6 | 1-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #5 - walking along - road #4 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #5 - on - road #4 | 1-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #5 - wearing - t-shirt #30 | 1-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #5 - wearing - shorts #31 | 1-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| suitcase #6 - moving with - man #5 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| suitcase #6 - rolling along - road #4 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| suitcase #6 - on - road #4 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| suitcase #6 - in front of - object #3 | 1-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #8 - above - road #4 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #8 - above - man #0 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| building #15 - alongside - road #4 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| sidewalk #16 - alongside - road #4 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #17 - above - road #4 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #17 - above - trees #18 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #18 - alongside - road #4 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| shadow #45 - on - road #4 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (45): man #2 - pulling - suitcase #6 [0-13]; man #2 - walking with - suitcase #6 [0-13]; man #2 - near - suitcase #6 [0-13]; man #2 - wearing - shoe #26 [0-13]; man #2 - wearing - shoe #27 [0-13]; suitcase #6 - moving with - man #2 [0-13]; man #2 - in front of - sidewalk #16 [0-13]; object #3 - in front of - sidewalk #16 [0-13]; suitcase #6 - in front of - sidewalk #16 [0-13]; man #2 - in front of - trees #18 [0-13]


## sav_004381

20.83 s, 21 frames read | human: 37 objects, 11 relations | TRASER: 37 objects, 207 relations, valid JSON, 6074 tokens

**Objects: 26/37 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | ice surface | yes (object 1) | ice rink | semantic overlap | ✓ |
| 1 | person | yes (object 2) | person | identical | ✓ |
| 2 | person | yes (object 3) | person | identical | ✓ |
| 3 | person | yes (object 4) | person | identical | ✓ |
| 4 | person | yes (object 5) | person | identical | ✓ |
| 5 | person | yes (object 6) | person | identical | ✓ |
| 6 | person | yes (object 7) | jacket | mismatch | ✗ |
| 7 | person | yes (object 8) | person | identical | ✓ |
| 8 | person | yes (object 9) | skateboard (uncertain) | mismatch | ✗ |
| 9 | person | yes (object 10) | person | identical | ✓ |
| 10 | person | yes (object 11) | banner | mismatch | ✗ |
| 11 | display | yes (object 12) | signboard | semantic overlap | ✓ |
| 12 | person | yes (object 13) | banner | mismatch | ✗ |
| 13 | person | yes (object 14) | person | identical | ✓ |
| 14 | person | yes (object 15) | person | identical | ✓ |
| 15 | person | yes (object 16) | person | identical | ✓ |
| 16 | person | yes (object 17) | person | identical | ✓ |
| 17 | person | yes (object 18) | person | identical | ✓ |
| 18 | rink board | yes (object 19) | banner | mismatch | ✗ |
| 19 | wall | yes (object 20) | structure (uncertain) | hypernym/hyponym | ✓ |
| 20 | rink board | yes (object 21) | banner | mismatch | ✗ |
| 21 | stores | yes (object 22) | ceiling | mismatch | ✗ |
| 22 | ceiling | yes (object 23) | ceiling | identical | ✓ |
| 23 | board | yes (object 24) | banner | semantic overlap | ✓ |
| 24 | board | yes (object 25) | banner | semantic overlap | ✓ |
| 25 | board | yes (object 26) | banner | semantic overlap | ✓ |
| 26 | board | yes (object 27) | banner | semantic overlap | ✓ |
| 27 | board | yes (object 28) | banner | semantic overlap | ✓ |
| 28 | goal net | yes (object 29) | banner | mismatch | ✗ |
| 29 | sign | yes (object 30) | poster | semantic overlap | ✓ |
| 30 | escalator | yes (object 31) | pole | mismatch | ✗ |
| 31 | wall | yes (object 32) | signboard | mismatch | ✗ |
| 32 | pillar | yes (object 33) | column | synonym | ✓ |
| 33 | pillar | yes (object 34) | column | synonym | ✓ |
| 34 | tv | yes (object 35) | banner | mismatch | ✗ |
| 35 | speaker | yes (object 36) | speaker | identical | ✓ |
| 36 | speaker | yes (object 37) | speaker | identical | ✓ |

**Relations: 3/11 right, triplets: 3/11 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #1 - skates on - ice surface #0 | 0-17 | skating on (+2 more) | 0-17 | identical | 1.00 | ✓ | ✓ |
| person #1 - practices skating - ice surface #0 | 0-17 | skating on (+2 more) | 0-17 | semantic overlap | 1.00 | ✓ | ✓ |
| person #1 - approaches - goal net #28 | 4-7 | in front of (+1 more) | 10-17 | mismatch | 0.00 | ✗ | ✗ |
| person #1 - moves away from - goal net #28 | 7-10 | in front of (+1 more) | 10-17 | mismatch | 0.00 | ✗ | ✗ |
| person #1 - approaches - person #9 | 8-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - moves away from - person #9 | 9-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - moves away from - person #7 | 11-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - skates on - ice surface #0 | 14-17 | on | 0-17 | hypernym/hyponym | 0.18 | ✗ | ✗ |
| person #7 - skates on - ice surface #0 | 0-2, 3-8, 11-17, 19-20 | on | 0-17 | hypernym/hyponym | 0.72 | ✓ | ✓ |
| person #9 - skates on - ice surface #0 | 8-11, 19-20 | on | 0-17 | hypernym/hyponym | 0.17 | ✗ | ✗ |
| goal net #28 - rests on - ice surface #0 | 0-11, 12-17, 19-21 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (199): person #1 - moving away from - person #2 [0-17]; person #1 - approaching - escalator #30 [10-17]; person #1 - in front of - escalator #30 [10-17]; person #1 - in front of - escalator #30 [10-17]; person #1 - in front of - escalator #30 [17-20]; person #2 - on - ice surface #0 [0-17]; person #3 - on - ice surface #0 [0-17]; person #4 - on - ice surface #0 [0-17]; person #2 - in front of - rink board #20 [0-8, 14-17]; person #2 - in front of - rink board #20 [14-17]


## sav_004550

13.71 s, 14 frames read | human: 52 objects, 37 relations | TRASER: 38 objects, 27 relations, valid JSON, 2165 tokens

**Objects: 30/52 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | bridegroom | yes (object 1) | person | hypernym/hyponym | ✓ |
| 1 | bride | yes (object 2) | bride | identical | ✓ |
| 2 | stone column | yes (object 3) | column (uncertain) | hypernym/hyponym | ✓ |
| 3 | wall | yes (object 4) | painting | mismatch | ✗ |
| 4 | archway | yes (object 5) | painting | mismatch | ✗ |
| 5 | floor | yes (object 6) | carpet | semantic overlap | ✓ |
| 6 | railing | yes (object 7) | chair | mismatch | ✗ |
| 7 | door | yes (object 8) | door | identical | ✓ |
| 8 | fence | yes (object 9) | gate | semantic overlap | ✓ |
| 9 | wall | yes (object 10) | painting | mismatch | ✗ |
| 10 | flower | yes (object 11) | flower arrangement | hypernym/hyponym | ✓ |
| 11 | crowds | yes (object 12) | person | hypernym/hyponym | ✓ |
| 12 | person | yes (object 13) | person | identical | ✓ |
| 13 | person | yes (object 14) | person | identical | ✓ |
| 14 | person | yes (object 15) | person | identical | ✓ |
| 15 | person | yes (object 16) | person | identical | ✓ |
| 16 | person | yes (object 17) | person | identical | ✓ |
| 17 | person | yes (object 18) | person | identical | ✓ |
| 18 | person | no: no mask on the frames TRASER reads | - | no label from TRASER | ✗ |
| 19 | person | yes (object 19) | person | identical | ✓ |
| 20 | person | yes (object 20) | person | identical | ✓ |
| 21 | person | yes (object 21) | dress | mismatch | ✗ |
| 22 | person | yes (object 22) | person | identical | ✓ |
| 23 | person | yes (object 23) | person | identical | ✓ |
| 24 | person | yes (object 24) | person | identical | ✓ |
| 25 | person | no: no mask on the frames TRASER reads | - | no label from TRASER | ✗ |
| 26 | person | yes (object 25) | person | identical | ✓ |
| 27 | person | yes (object 26) | person | identical | ✓ |
| 28 | person | yes (object 27) | dress | mismatch | ✗ |
| 29 | person | yes (object 28) | person | identical | ✓ |
| 30 | person | yes (object 29) | person | identical | ✓ |
| 31 | person | yes (object 30) | dress | mismatch | ✗ |
| 32 | person | yes (object 31) | dress | mismatch | ✗ |
| 33 | person | yes (object 32) | person | identical | ✓ |
| 34 | person | yes (object 33) | person | identical | ✓ |
| 35 | person | yes (object 34) | person | identical | ✓ |
| 36 | person | yes (object 35) | person | identical | ✓ |
| 37 | person | yes (object 36) | person | identical | ✓ |
| 38 | person | yes (object 37) | person | identical | ✓ |
| 39 | person | yes (object 38) | person | identical | ✓ |
| 40 | person | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | person | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | person | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | person | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | person | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | person | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | person | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | person | no: after the first 40 | - | no label from TRASER | ✗ |
| 48 | carpet | no: after the first 40 | - | no label from TRASER | ✗ |
| 49 | painting | no: after the first 40 | - | no label from TRASER | ✗ |
| 50 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 51 | light | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 12/37 right, triplets: 7/37 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| bridegroom #0 - walks with - bride #1 | 0-14 | next to (+3 more) | 0-15 | hypernym/hyponym | 0.93 | ✓ | ✓ |
| bridegroom #0 - moves along - carpet #48 | 0-5, 7-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| bridegroom #0 - on - carpet #48 | 0-5, 7-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| bridegroom #0 - in front of - stone column #2 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| bridegroom #0 - in front of - window #50 | 0-4 | nothing for this pair | - | - | - | ✗ | ✗ |
| bridegroom #0 - in front of - door #7 | 4-6 | in front of | 5-15 | identical | 0.09 | ✗ | ✗ |
| bridegroom #0 - adjacent to - railing #6 | 0-14 | in front of | 0-15 | hypernym/hyponym | 0.93 | ✓ | ✗ |
| bridegroom #0 - in front of - archway #4 | 6-14 | in front of | 5-15 | identical | 0.80 | ✓ | ✗ |
| bridegroom #0 - in front of - painting #49 | 4-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bridegroom #0 - below - light #51 | 0-4.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| bridegroom #0 - in front of - wall #3 | 0-4.5 | in front of | 0-15 | identical | 0.30 | ✗ | ✗ |
| bridegroom #0 - in front of - wall #9 | 0-5.5 | in front of | 0-15 | identical | 0.37 | ✗ | ✗ |
| bridegroom #0 - on - floor #5 | 0-5, 6-14 | on | 0-15 | identical | 0.87 | ✓ | ✓ |
| bridegroom #0 - in front of - crowds #11 | 0-7.5 | in front of (+1 more) | 0-15 | identical | 0.50 | ✗ | ✗ |
| bridegroom #0 - in front of - fence #8 | 0-4 | in front of | 0-4 | identical | 1.00 | ✓ | ✓ |
| bride #1 - holds arm of - bridegroom #0 | 0-14 | approaching (+2 more) | 7-11 | mismatch | 0.29 | ✗ | ✗ |
| bride #1 - moves with - bridegroom #0 | 0-14 | approaching (+2 more) | 7-11 | mismatch | 0.29 | ✗ | ✗ |
| bride #1 - walks down aisle with - bridegroom #0 | 0-14 | approaching (+2 more) | 7-11 | mismatch | 0.29 | ✗ | ✗ |
| bride #1 - touching - bridegroom #0 | 0-14 | approaching (+2 more) | 7-11 | mismatch | 0.29 | ✗ | ✗ |
| bride #1 - moves along - carpet #48 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| bride #1 - on - carpet #48 | 0-5, 7-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| bride #1 - in front of - fence #8 | 0-3.5 | in front of | 0-4 | identical | 0.88 | ✓ | ✓ |
| bride #1 - in front of - stone column #2 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| bride #1 - in front of - window #50 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| bride #1 - below - light #51 | 0-4.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| bride #1 - in front of - door #7 | 5-14 | in front of | 5-15 | identical | 0.90 | ✓ | ✓ |
| bride #1 - adjacent to - railing #6 | 0-14 | in front of | 0-15 | hypernym/hyponym | 0.93 | ✓ | ✗ |
| bride #1 - in front of - archway #4 | 7-14 | in front of | 5-15 | identical | 0.70 | ✓ | ✗ |
| bride #1 - in front of - painting #49 | 3-5, 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| bride #1 - in front of - wall #3 | 0-4 | in front of | 0-15 | identical | 0.27 | ✗ | ✗ |
| bride #1 - in front of - wall #9 | 0-14 | in front of | 0-15 | identical | 0.93 | ✓ | ✗ |
| bride #1 - on - floor #5 | 0-5, 6-14 | on | 0-15 | identical | 0.87 | ✓ | ✓ |
| bride #1 - in front of - crowds #11 | 0-14 | in front of (+1 more) | 0-15 | identical | 0.93 | ✓ | ✓ |
| railing #6 - beside - carpet #48 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #30 - looks at - bride #1 | 9-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #31 - looks at - bride #1 | 11-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| carpet #48 - on - floor #5 | 0-5, 7-14 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (2): bridegroom #0 - in front of - flower #10 [13-15]; bride #1 - in front of - flower #10 [13-15]


## sav_009146

12.96 s, 13 frames read | human: 32 objects, 36 relations | TRASER: 32 objects, 57 relations, valid JSON, 3006 tokens

**Objects: 21/32 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | basket | yes (object 1) | motorcycle | mismatch | ✗ |
| 1 | tree | yes (object 2) | tree | identical | ✓ |
| 2 | building | yes (object 3) | building | identical | ✓ |
| 3 | sidewalk | yes (object 4) | motorcycle | mismatch | ✗ |
| 4 | planter platform | yes (object 5) | curb | semantic overlap | ✓ |
| 5 | bollard | yes (object 6) | cylindrical object (uncertain) | hypernym/hyponym | ✓ |
| 6 | bollard | yes (object 7) | cylindrical object (uncertain) | hypernym/hyponym | ✓ |
| 7 | bollard | yes (object 8) | pole | hypernym/hyponym | ✓ |
| 8 | light | yes (object 9) | streetlight | hypernym/hyponym | ✓ |
| 9 | tree top | yes (object 10) | tree | semantic overlap | ✓ |
| 10 | tree | yes (object 11) | tree | identical | ✓ |
| 11 | sky | yes (object 12) | streetlight | mismatch | ✗ |
| 12 | people | yes (object 13) | person | hypernym/hyponym | ✓ |
| 13 | bag | yes (object 14) | motorcycle | mismatch | ✗ |
| 14 | electric scooter | yes (object 15) | motorcycle | semantic overlap | ✓ |
| 15 | tree | yes (object 16) | tree | identical | ✓ |
| 16 | building | yes (object 17) | tree | mismatch | ✗ |
| 17 | mixer truck | yes (object 18) | truck | hypernym/hyponym | ✓ |
| 18 | road | yes (object 19) | motorcycle | mismatch | ✗ |
| 19 | tactile paving | yes (object 20) | motorcycle | mismatch | ✗ |
| 20 | line | yes (object 21) | line (uncertain) | identical | ✓ |
| 21 | wheel | yes (object 22) | wheel | identical | ✓ |
| 22 | wheel | yes (object 23) | wheel | identical | ✓ |
| 23 | wheel | yes (object 24) | wheel | identical | ✓ |
| 24 | drum | yes (object 25) | tank (uncertain) | semantic overlap | ✓ |
| 25 | clothes | yes (object 26) | person | mismatch | ✗ |
| 26 | light | yes (object 27) | emblem | mismatch | ✗ |
| 27 | plate | yes (object 28) | license plate | mismatch | ✗ |
| 28 | window | yes (object 29) | window | identical | ✓ |
| 29 | top case | yes (object 30) | motorcycle | mismatch | ✗ |
| 30 | wheel | yes (object 31) | wheel | identical | ✓ |
| 31 | wheel | yes (object 32) | wheel | identical | ✓ |

**Relations: 1/36 right, triplets: 1/36 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| tree #1 - on - sidewalk #3 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #1 - in front of - mixer truck #17 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| building #2 - behind - tree #10 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| bollard #5 - on - sidewalk #3 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| bollard #5 - in front of - mixer truck #17 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| bollard #6 - on - sidewalk #3 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| bollard #6 - in front of - mixer truck #17 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| bollard #7 - on - sidewalk #3 | 0-1, 3-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| bollard #7 - in front of - mixer truck #17 | 0-1.5, 2-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #8 - above - road #18 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree top #9 - above - mixer truck #17 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| people #12 - ride - electric scooter #14 | 0-7 | riding | 2-13 | identical | 0.38 | ✗ | ✗ |
| people #12 - hold - bag #13 | 0-5 | riding | 0-2 | mismatch | 0.40 | ✗ | ✗ |
| people #12 - wear - clothes #25 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| people #12 - move toward - mixer truck #17 | 0-7 | passing by (+1 more) | 0-13 | semantic overlap | 0.54 | ✓ | ✓ |
| electric scooter #14 - carry - bag #13 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| electric scooter #14 - has - top case #29 | 1-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| electric scooter #14 - move toward - mixer truck #17 | 0-7 | moving away from | 2-13 | mismatch | 0.38 | ✗ | ✗ |
| electric scooter #14 - move toward - bollard #7 | 1-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| electric scooter #14 - on - sidewalk #3 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| mixer truck #17 - on - road #18 | 0-14 | in front of (+1 more) | 0-13 | mismatch | 0.93 | ✗ | ✗ |
| tactile paving #19 - on - sidewalk #3 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| line #20 - on - sidewalk #3 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #21 - below - mixer truck #17 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #21 - on - road #18 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #22 - below - mixer truck #17 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #22 - on - road #18 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #23 - below - mixer truck #17 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #23 - on - road #18 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| drum #24 - above - wheel #22 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| drum #24 - on - mixer truck #17 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| drum #24 - above - wheel #21 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #28 - on - mixer truck #17 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| top case #29 - on - electric scooter #14 | 1-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #30 - on - road #18 | 0-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| wheel #31 - below - electric scooter #14 | 1-7 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (50): people #12 - riding - top case #29 [2-13]; bag #13 - moving away from - mixer truck #17 [0-2]; top case #29 - moving away from - mixer truck #17 [2-13]; mixer truck #17 - in front of - tree #1 [0-13]; mixer truck #17 - in front of - tree #1 [0-13]; mixer truck #17 - in front of - building #2 [0-13]; mixer truck #17 - in front of - building #2 [0-13]; mixer truck #17 - in front of - tree top #9 [0-13]; mixer truck #17 - in front of - tree top #9 [0-13]; mixer truck #17 - in front of - tree #10 [0-13]


## sav_009307

15.54 s, 16 frames read | human: 63 objects, 53 relations | TRASER: 40 objects, 58 relations, valid JSON, 2944 tokens

**Objects: 38/63 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | ceiling | yes (object 1) | ceiling | identical | ✓ |
| 1 | pillar | yes (object 2) | pillar | identical | ✓ |
| 2 | store | yes (object 3) | storefront | semantic overlap | ✓ |
| 3 | sign | yes (object 4) | signboard | synonym | ✓ |
| 4 | people | yes (object 5) | person | hypernym/hyponym | ✓ |
| 5 | performers | yes (object 6) | bow (uncertain) | mismatch | ✗ |
| 6 | pillar | yes (object 7) | pillar | identical | ✓ |
| 7 | pillar | yes (object 8) | pillar | identical | ✓ |
| 8 | pillar | yes (object 9) | pillar | identical | ✓ |
| 9 | christmas tree | yes (object 10) | Christmas tree | identical | ✓ |
| 10 | speaker | yes (object 11) | speaker | identical | ✓ |
| 11 | speaker | yes (object 12) | speaker | identical | ✓ |
| 12 | sign | yes (object 13) | signboard | synonym | ✓ |
| 13 | person | yes (object 14) | person | identical | ✓ |
| 14 | person | yes (object 15) | person | identical | ✓ |
| 15 | person | yes (object 16) | person | identical | ✓ |
| 16 | person | yes (object 17) | person | identical | ✓ |
| 17 | person | yes (object 18) | person | identical | ✓ |
| 18 | person | yes (object 19) | person | identical | ✓ |
| 19 | person | yes (object 20) | person | identical | ✓ |
| 20 | person | yes (object 21) | person | identical | ✓ |
| 21 | person | yes (object 22) | person | identical | ✓ |
| 22 | person | yes (object 23) | person | identical | ✓ |
| 23 | person | yes (object 24) | person | identical | ✓ |
| 24 | person | yes (object 25) | person | identical | ✓ |
| 25 | person | yes (object 26) | person | identical | ✓ |
| 26 | person | yes (object 27) | person | identical | ✓ |
| 27 | person | yes (object 28) | person | identical | ✓ |
| 28 | person | yes (object 29) | person | identical | ✓ |
| 29 | person | yes (object 30) | person | identical | ✓ |
| 30 | person | yes (object 31) | person | identical | ✓ |
| 31 | person | yes (object 32) | person | identical | ✓ |
| 32 | person | yes (object 33) | person | identical | ✓ |
| 33 | wheelchair | yes (object 34) | person | mismatch | ✗ |
| 34 | person | yes (object 35) | person | identical | ✓ |
| 35 | person | yes (object 36) | person | identical | ✓ |
| 36 | person | yes (object 37) | person | identical | ✓ |
| 37 | pillar | yes (object 38) | pillar | identical | ✓ |
| 38 | pillar | yes (object 39) | pillar | identical | ✓ |
| 39 | chair | yes (object 40) | chair | identical | ✓ |
| 40 | chair | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | chair | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | chair | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | chair | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | chair | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | chair | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | chair | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | chair | no: after the first 40 | - | no label from TRASER | ✗ |
| 48 | trashcan | no: after the first 40 | - | no label from TRASER | ✗ |
| 49 | present | no: after the first 40 | - | no label from TRASER | ✗ |
| 50 | present | no: after the first 40 | - | no label from TRASER | ✗ |
| 51 | present | no: after the first 40 | - | no label from TRASER | ✗ |
| 52 | present | no: after the first 40 | - | no label from TRASER | ✗ |
| 53 | present | no: after the first 40 | - | no label from TRASER | ✗ |
| 54 | present | no: after the first 40 | - | no label from TRASER | ✗ |
| 55 | present | no: after the first 40 | - | no label from TRASER | ✗ |
| 56 | present | no: after the first 40 | - | no label from TRASER | ✗ |
| 57 | present | no: after the first 40 | - | no label from TRASER | ✗ |
| 58 | present | no: after the first 40 | - | no label from TRASER | ✗ |
| 59 | present | no: after the first 40 | - | no label from TRASER | ✗ |
| 60 | present | no: after the first 40 | - | no label from TRASER | ✗ |
| 61 | guitar | no: after the first 40 | - | no label from TRASER | ✗ |
| 62 | hat | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 8/53 right, triplets: 8/53 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| pillar #1 - under - ceiling #0 | 0-16 | below | 0-15 | synonym | 0.94 | ✓ | ✓ |
| store #2 - under - ceiling #0 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| people #4 - watch - performers #5 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| people #4 - in front of - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| performers #5 - in front of - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| performers #5 - in front of - sign #12 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| performers #5 - under - ceiling #0 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| performers #5 - put on show for - people #4 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| performers #5 - perform for - people #4 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| performers #5 - in front of - store #2 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| pillar #6 - under - ceiling #0 | 0-16 | below | 0-15 | synonym | 0.94 | ✓ | ✓ |
| pillar #7 - under - ceiling #0 | 0-16 | below | 0-15 | synonym | 0.94 | ✓ | ✓ |
| pillar #8 - under - ceiling #0 | 0-16 | below | 0-15 | synonym | 0.94 | ✓ | ✓ |
| christmas tree #9 - in front of - sign #12 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| christmas tree #9 - in front of - sign #3 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| christmas tree #9 - under - ceiling #0 | 0-16 | below | 0-15 | synonym | 0.94 | ✓ | ✓ |
| speaker #10 - in front of - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| speaker #11 - in front of - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #14 - sit on - chair #46 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #15 - sit on - chair #45 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #19 - sit on - chair #40 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #24 - sit on - chair #41 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #25 - sit on - chair #42 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #29 - walk past - christmas tree #9 | 0-9 | passes by (+2 more) | 5-8 | synonym | 0.33 | ✗ | ✗ |
| wheelchair #33 - in front of - performers #5 | 0-10.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #35 - play - guitar #61 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| pillar #37 - under - ceiling #0 | 0-16 | below | 0-15 | synonym | 0.94 | ✓ | ✓ |
| pillar #38 - under - ceiling #0 | 0-16 | below | 0-15 | synonym | 0.94 | ✓ | ✓ |
| chair #39 - in front of - performers #5 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #39 - in front of - store #2 | 0-16 | in front of | 0-15 | identical | 0.94 | ✓ | ✓ |
| chair #40 - in front of - performers #5 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #41 - in front of - performers #5 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #45 - in front of - performers #5 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #46 - in front of - performers #5 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #47 - in front of - performers #5 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #47 - in front of - store #2 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| trashcan #48 - in front of - performers #5 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| present #49 - attached to - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| present #49 - attached to - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| present #50 - attached to - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| present #51 - attached to - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| present #52 - attached to - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| present #52 - attached to - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| present #53 - attached to - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| present #54 - attached to - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| present #54 - attached to - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| present #55 - attached to - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| present #56 - attached to - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| present #57 - attached to - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| present #58 - attached to - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| present #59 - attached to - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| present #60 - attached to - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| guitar #61 - in front of - christmas tree #9 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (47): person #29 - approaches - speaker #10 [0-7]; person #29 - moves away from - speaker #10 [7-15]; person #29 - passes by - speaker #10 [5-8]; person #29 - approaches - store #2 [0-7]; person #29 - moves away from - store #2 [7-15]; person #29 - passes by - store #2 [5-8]; person #29 - in front of - store #2 [0-15]; christmas tree #9 - in front of - store #2 [0-15]; speaker #10 - in front of - store #2 [0-15]; speaker #11 - in front of - store #2 [0-15]


## sav_009687

19.04 s, 19 frames read | human: 52 objects, 18 relations | TRASER: 40 objects, 58 relations, valid JSON, 3430 tokens

**Objects: 31/52 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | person | yes (object 2) | person | identical | ✓ |
| 2 | person | yes (object 3) | handbag | mismatch | ✗ |
| 3 | table | yes (object 4) | tablecloth | semantic overlap | ✓ |
| 4 | picture | yes (object 5) | picture frame | semantic overlap | ✓ |
| 5 | picture | yes (object 6) | picture frame | semantic overlap | ✓ |
| 6 | picture | yes (object 7) | picture frame | semantic overlap | ✓ |
| 7 | picture | yes (object 8) | bookshelf | mismatch | ✗ |
| 8 | chair | yes (object 9) | sofa | semantic overlap | ✓ |
| 9 | wall | yes (object 10) | wall | identical | ✓ |
| 10 | cake | yes (object 11) | cake | identical | ✓ |
| 11 | glasses | yes (object 12) | spectacles | synonym | ✓ |
| 12 | bookcase | yes (object 13) | bookshelf | synonym | ✓ |
| 13 | ipad | yes (object 14) | book | mismatch | ✗ |
| 14 | tissue | yes (object 15) | pillow | mismatch | ✗ |
| 15 | light | yes (object 16) | lampshade | semantic overlap | ✓ |
| 16 | stool | yes (object 17) | cushion | mismatch | ✗ |
| 17 | stool | yes (object 18) | cushion | mismatch | ✗ |
| 18 | door | yes (object 19) | door (uncertain) | identical | ✓ |
| 19 | ground | yes (object 20) | chair leg (uncertain) | mismatch | ✗ |
| 20 | plant | yes (object 21) | flowerpot | semantic overlap | ✓ |
| 21 | picture | yes (object 22) | picture frame | semantic overlap | ✓ |
| 22 | picture | yes (object 23) | picture frame | semantic overlap | ✓ |
| 23 | picture | yes (object 24) | picture frame | semantic overlap | ✓ |
| 24 | picture | yes (object 25) | picture frame | semantic overlap | ✓ |
| 25 | picture | yes (object 26) | picture frame | semantic overlap | ✓ |
| 26 | picture | yes (object 27) | picture frame | semantic overlap | ✓ |
| 27 | picture | yes (object 28) | picture frame | semantic overlap | ✓ |
| 28 | picture | yes (object 29) | picture frame | semantic overlap | ✓ |
| 29 | scarf | yes (object 30) | scarf | identical | ✓ |
| 30 | statue | yes (object 31) | picture frame | mismatch | ✗ |
| 31 | statue | yes (object 32) | picture frame | mismatch | ✗ |
| 32 | jeans | yes (object 33) | trousers | hypernym/hyponym | ✓ |
| 33 | shirt | yes (object 34) | sweater | semantic overlap | ✓ |
| 34 | sweater | yes (object 35) | sweater | identical | ✓ |
| 35 | blanket | yes (object 36) | blanket | identical | ✓ |
| 36 | candle | yes (object 37) | candle | identical | ✓ |
| 37 | candle | yes (object 38) | candle | identical | ✓ |
| 38 | book | yes (object 39) | book | identical | ✓ |
| 39 | book | yes (object 40) | book | identical | ✓ |
| 40 | book | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | book | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | book | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | book | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | book | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | book | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | book | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | book | no: after the first 40 | - | no label from TRASER | ✗ |
| 48 | book | no: after the first 40 | - | no label from TRASER | ✗ |
| 49 | book | no: after the first 40 | - | no label from TRASER | ✗ |
| 50 | book | no: after the first 40 | - | no label from TRASER | ✗ |
| 51 | book | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 9/18 right, triplets: 9/18 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - wear - scarf #29 | 0-20 | wearing | 0-19 | identical | 0.95 | ✓ | ✓ |
| person #0 - wear - sweater #34 | 0-20 | wearing | 0-19 | identical | 0.95 | ✓ | ✓ |
| person #0 - sit on - chair #8 | 0-20 | sitting on (+1 more) | 0-19 | identical | 0.95 | ✓ | ✓ |
| person #0 - look at - cake #10 | 3-20 | looking at (+3 more) | 0-19 | identical | 0.80 | ✓ | ✓ |
| person #1 - hold - cake #10 | 0-6 | holding (+2 more) | 0-6 | identical | 1.00 | ✓ | ✓ |
| person #1 - set down - cake #10 | 2-6 | holding (+2 more) | 0-6 | mismatch | 0.67 | ✗ | ✗ |
| person #1 - move toward - person #0 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - bring cake to - person #0 | 0-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - give to - person #0 | 2-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - move away from - table #3 | 5-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - wear - jeans #32 | 0-7 | wearing | 0-6 | identical | 0.86 | ✓ | ✓ |
| person #1 - wear - shirt #33 | 0-7 | wearing | 0-6 | identical | 0.86 | ✓ | ✓ |
| cake #10 - move toward - table #3 | 0-4 | on | 0-19 | mismatch | 0.21 | ✗ | ✗ |
| cake #10 - move toward - table #3 | 2-5 | on | 0-19 | mismatch | 0.16 | ✗ | ✗ |
| cake #10 - rest on - table #3 | 5-20 | on | 0-19 | hypernym/hyponym | 0.70 | ✓ | ✓ |
| cake #10 - have - candle #36 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| cake #10 - have - candle #37 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| glasses #11 - rest on - table #3 | 7-20 | on | 0-19 | hypernym/hyponym | 0.60 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (43): tissue #14 - on - table #3 [5-19]; person #0 - in front of - bookcase #12 [0-19]; chair #8 - in front of - bookcase #12 [0-19]; cake #10 - in front of - person #0 [0-19]; cake #10 - in front of - chair #8 [0-19]; glasses #11 - in front of - person #0 [0-19]; glasses #11 - in front of - chair #8 [0-19]; tissue #14 - in front of - person #0 [5-19]; tissue #14 - in front of - chair #8 [5-19]; candle #36 - on - cake #10 [0-19]


## sav_010164

16.62 s, 17 frames read | human: 36 objects, 42 relations | TRASER: 36 objects, 73 relations, valid JSON, 3372 tokens

**Objects: 25/36 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | man | yes (object 1) | person | hypernym/hyponym | ✓ |
| 1 | man | yes (object 2) | person | hypernym/hyponym | ✓ |
| 2 | man | yes (object 3) | person | hypernym/hyponym | ✓ |
| 3 | net | yes (object 4) | net | identical | ✓ |
| 4 | bench | yes (object 5) | table | mismatch | ✗ |
| 5 | man | yes (object 6) | person | hypernym/hyponym | ✓ |
| 6 | volleyball | yes (object 7) | soccer ball | semantic overlap | ✓ |
| 7 | car | yes (object 8) | truck | semantic overlap | ✓ |
| 8 | car | yes (object 9) | car | identical | ✓ |
| 9 | court | yes (object 10) | sand | mismatch | ✗ |
| 10 | graffiti wall | yes (object 11) | banner | mismatch | ✗ |
| 11 | lighting | yes (object 12) | streetlight (uncertain) | hypernym/hyponym | ✓ |
| 12 | lighting | yes (object 13) | streetlight (uncertain) | hypernym/hyponym | ✓ |
| 13 | wall | yes (object 14) | net | mismatch | ✗ |
| 14 | tarp or cover | yes (object 15) | tarp | identical | ✓ |
| 15 | tarp or cover | yes (object 16) | tarp | identical | ✓ |
| 16 | pole | yes (object 17) | pole | identical | ✓ |
| 17 | pole | yes (object 18) | flag | mismatch | ✗ |
| 18 | pole | yes (object 19) | pole (uncertain) | identical | ✓ |
| 19 | pole | yes (object 20) | pole | identical | ✓ |
| 20 | pole | yes (object 21) | pole | identical | ✓ |
| 21 | bag | yes (object 22) | chair | mismatch | ✗ |
| 22 | cement flooring | yes (object 23) | bench | mismatch | ✗ |
| 23 | window | yes (object 24) | vent | mismatch | ✗ |
| 24 | window | yes (object 25) | vent | mismatch | ✗ |
| 25 | window | yes (object 26) | vent | mismatch | ✗ |
| 26 | tape or bands | yes (object 27) | tape measure (uncertain) | semantic overlap | ✓ |
| 27 | shirt | yes (object 28) | tank top | hypernym/hyponym | ✓ |
| 28 | shorts | yes (object 29) | shorts (uncertain) | identical | ✓ |
| 29 | shirt | yes (object 30) | jersey | hypernym/hyponym | ✓ |
| 30 | shorts | yes (object 31) | shorts (uncertain) | identical | ✓ |
| 31 | shorts | yes (object 32) | shorts | identical | ✓ |
| 32 | shorts | yes (object 33) | shorts (uncertain) | identical | ✓ |
| 33 | wall | yes (object 34) | tarp | mismatch | ✗ |
| 34 | wall | yes (object 35) | building | semantic overlap | ✓ |
| 35 | net or wall | yes (object 36) | net | identical | ✓ |

**Relations: 7/42 right, triplets: 0/42 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| man #0 - in front of - wall #13 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #0 - moves toward - volleyball #6 | 10-13 | approaching | 0-17 | synonym | 0.18 | ✗ | ✗ |
| man #0 - watching - volleyball #6 | 8-13 | approaching | 0-17 | mismatch | 0.29 | ✗ | ✗ |
| man #0 - on - court #9 | 0-17 | on | 0-17 | identical | 1.00 | ✓ | ✗ |
| man #1 - below - net #3 | 10-11.5 | in front of | 0-17 | mismatch | 0.09 | ✗ | ✗ |
| man #1 - in front of - wall #13 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #1 - hits - volleyball #6 | 10-11 | approaching | 0-17 | mismatch | 0.06 | ✗ | ✗ |
| man #1 - watching - volleyball #6 | 8-13 | approaching | 0-17 | mismatch | 0.29 | ✗ | ✗ |
| man #1 - on - court #9 | 0-17 | on | 0-17 | identical | 1.00 | ✓ | ✗ |
| man #2 - below - net #3 | 0-17 | in front of | 0-17 | mismatch | 1.00 | ✗ | ✗ |
| man #2 - in front of - wall #13 | 0-7, 9-15, 16-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #2 - on - court #9 | 0-17 | on | 0-17 | identical | 1.00 | ✓ | ✗ |
| net #3 - in front of - wall #13 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| net #3 - attached to - pole #16 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| net #3 - attached to - pole #18 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| net #3 - above - court #9 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| bench #4 - in front of - graffiti wall #10 | 0-17 | in front of | 0-17 | identical | 1.00 | ✓ | ✗ |
| bench #4 - on - court #9 | 0-17 | on | 0-17 | identical | 1.00 | ✓ | ✗ |
| man #5 - below - net #3 | 0-17 | in front of | 0-17 | mismatch | 1.00 | ✗ | ✗ |
| man #5 - in front of - wall #13 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #5 - holding - volleyball #6 | 0-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #5 - tosses - volleyball #6 | 8-9 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #5 - watching - volleyball #6 | 8-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #5 - serves - volleyball #6 | 7-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #5 - on - court #9 | 0-17 | on | 0-17 | identical | 1.00 | ✓ | ✗ |
| volleyball #6 - above - court #9 | 0-15 | on | 0-17 | semantic overlap | 0.88 | ✓ | ✗ |
| volleyball #6 - in front of - wall #13 | 0-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| volleyball #6 - moves toward - man #1 | 8-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| volleyball #6 - moves away from - man #1 | 10-12 | nothing for this pair | - | - | - | ✗ | ✗ |
| volleyball #6 - moves away from - man #5 | 8-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #7 - behind - court #9 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #7 - behind - net #3 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #8 - behind - court #9 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #8 - behind - net #3 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| court #9 - in front of - wall #13 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| lighting #11 - above - court #9 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| lighting #12 - above - court #9 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| pole #16 - in front of - wall #13 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| pole #20 - in front of - wall #13 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| bag #21 - on - bench #4 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #23 - in - wall #13 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| tape or bands #26 - attached to - net #3 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (61): man #0 - approaching - man #1 [0-17]; man #0 - moving away from - bench #4 [0-17]; man #1 - wearing - shirt #29 [0-17]; man #0 - wearing - shirt #27 [0-17]; bag #21 - on - court #9 [0-17]; cement flooring #22 - on - court #9 [0-17]; man #0 - in front of - net #3 [0-17]; volleyball #6 - in front of - net #3 [0-17]; bench #4 - in front of - net #3 [0-17]; bag #21 - in front of - net #3 [0-17]


## sav_010923

18.25 s, 18 frames read | human: 36 objects, 34 relations | TRASER: 36 objects, 54 relations, valid JSON, 2742 tokens

**Objects: 25/36 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | air-conditioner | yes (object 2) | air conditioner unit | identical | ✓ |
| 2 | shoe boxes | yes (object 3) | desk | mismatch | ✗ |
| 3 | books | yes (object 4) | box | mismatch | ✗ |
| 4 | mannequin head | yes (object 5) | plastic bag (uncertain) | mismatch | ✗ |
| 5 | painting | yes (object 6) | poster | semantic overlap | ✓ |
| 6 | ceiling | yes (object 7) | ceiling fan | semantic overlap | ✓ |
| 7 | bathroom | yes (object 8) | door | mismatch | ✗ |
| 8 | mop stick | yes (object 9) | pipe (uncertain) | semantic overlap | ✓ |
| 9 | toilet | yes (object 10) | trash can (uncertain) | mismatch | ✗ |
| 10 | floor | yes (object 11) | person | mismatch | ✗ |
| 11 | furniture | yes (object 12) | chair | hypernym/hyponym | ✓ |
| 12 | wall | yes (object 13) | wall | identical | ✓ |
| 13 | shoe box | yes (object 14) | box | hypernym/hyponym | ✓ |
| 14 | wire | yes (object 15) | chair leg (uncertain) | mismatch | ✗ |
| 15 | shoe box | yes (object 16) | speaker (uncertain) | mismatch | ✗ |
| 16 | shoe box | yes (object 17) | box | hypernym/hyponym | ✓ |
| 17 | shoe box | yes (object 18) | chair | mismatch | ✗ |
| 18 | shoe box | yes (object 19) | box | hypernym/hyponym | ✓ |
| 19 | wall | yes (object 20) | wall | identical | ✓ |
| 20 | wall | yes (object 21) | object (uncertain) | hypernym/hyponym | ✓ |
| 21 | wall | yes (object 22) | wall | identical | ✓ |
| 22 | bed | yes (object 23) | chair | mismatch | ✗ |
| 23 | part of an a/c | yes (object 24) | vent | semantic overlap | ✓ |
| 24 | part of an a/c | yes (object 25) | air conditioner unit | semantic overlap | ✓ |
| 25 | part of an a/c | yes (object 26) | air conditioner unit | semantic overlap | ✓ |
| 26 | part of an a/c | yes (object 27) | air conditioner unit | semantic overlap | ✓ |
| 27 | jean | yes (object 28) | shorts | mismatch | ✗ |
| 28 | thigh | yes (object 29) | legs | hypernym/hyponym | ✓ |
| 29 | thigh | yes (object 30) | legs | hypernym/hyponym | ✓ |
| 30 | hand | yes (object 31) | arm | semantic overlap | ✓ |
| 31 | hand | yes (object 32) | arm | semantic overlap | ✓ |
| 32 | door frame | yes (object 33) | door frame (uncertain) | identical | ✓ |
| 33 | shirt | yes (object 34) | jersey | hypernym/hyponym | ✓ |
| 34 | braids | yes (object 35) | hair | hypernym/hyponym | ✓ |
| 35 | face | yes (object 36) | person | hypernym/hyponym | ✓ |

**Relations: 13/34 right, triplets: 9/34 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - above - floor #10 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - dancing on - floor #10 | 3-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - below - ceiling #6 | 0-19 | below | 0-18 | identical | 0.95 | ✓ | ✓ |
| person #0 - below - air-conditioner #1 | 0-19 | below | 0-18 | identical | 0.95 | ✓ | ✓ |
| person #0 - in front of - wall #12 | 0-19 | in front of (+1 more) | 0-18 | identical | 0.95 | ✓ | ✓ |
| person #0 - touching - wall #12 | 3-6, 11-16 | moving relative to (+1 more) | 0-18 | mismatch | 0.44 | ✗ | ✗ |
| person #0 - in front of - furniture #11 | 0.5-19 | in front of (+2 more) | 0-18 | identical | 0.92 | ✓ | ✓ |
| person #0 - approaching - furniture #11 | 14-19 | moving relative to (+2 more) | 0-18 | hypernym/hyponym | 0.21 | ✗ | ✗ |
| person #0 - wearing - shirt #33 | 0-19 | wearing | 0-18 | identical | 0.95 | ✓ | ✓ |
| person #0 - wearing - jean #27 | 1-19 | wearing | 0-18 | identical | 0.89 | ✓ | ✗ |
| person #0 - moving away from - shoe boxes #2 | 1-3 | in front of | 0-18 | mismatch | 0.11 | ✗ | ✗ |
| air-conditioner #1 - on - wall #12 | 0-19 | above | 0-18 | semantic overlap | 0.95 | ✓ | ✓ |
| air-conditioner #1 - mounted on - wall #12 | 0-19 | above | 0-18 | hypernym/hyponym | 0.95 | ✓ | ✓ |
| air-conditioner #1 - below - ceiling #6 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| shoe boxes #2 - on - floor #10 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| shoe boxes #2 - against - wall #12 | 0-19 | in front of | 0-18 | semantic overlap | 0.95 | ✓ | ✗ |
| books #3 - on - shoe boxes #2 | 0-19 | on | 0-18 | identical | 0.95 | ✓ | ✗ |
| painting #5 - on - floor #10 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| painting #5 - against - wall #12 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| painting #5 - leaning against - wall #12 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| bathroom #7 - behind - door frame #32 | 0.5-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| mop stick #8 - inside - bathroom #7 | 1-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| toilet #9 - inside - bathroom #7 | 0.5-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| furniture #11 - on - floor #10 | 1-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| wire #14 - on - shoe boxes #2 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| part of an a/c #23 - attached to - air-conditioner #1 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| part of an a/c #24 - attached to - air-conditioner #1 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| part of an a/c #25 - attached to - air-conditioner #1 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| part of an a/c #26 - attached to - air-conditioner #1 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| jean #27 - on - person #0 | 1-19 | on | 0-18 | identical | 0.89 | ✓ | ✗ |
| door frame #32 - on - wall #21 | 0.5-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #33 - on - person #0 | 0-19 | on | 0-18 | identical | 0.95 | ✓ | ✓ |
| braids #34 - on - person #0 | 0-19 | attached to | 0-18 | semantic overlap | 0.95 | ✓ | ✓ |
| face #35 - on - person #0 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (38): person #0 - has - braids #34 [0-18]; person #0 - has - hand #30 [0-18]; person #0 - has - hand #31 [0-18]; person #0 - moving relative to - bathroom #7 [0-18]; person #0 - in front of - bathroom #7 [0-18]; person #0 - in front of - wall #21 [0-18]; person #0 - in front of - bed #22 [0-18]; person #0 - in front of - painting #5 [0-18]; person #0 - in front of - books #3 [0-18]; person #0 - in front of - shoe box #13 [0-18]


## sav_011754

21.29 s, 21 frames read | human: 53 objects, 46 relations | TRASER: 40 objects, 56 relations, valid JSON, 3110 tokens

**Objects: 35/53 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | goose | yes (object 1) | swan | semantic overlap | ✓ |
| 1 | goose | yes (object 2) | swan | semantic overlap | ✓ |
| 2 | goose | yes (object 3) | bird (uncertain) | hypernym/hyponym | ✓ |
| 3 | goose | yes (object 4) | duck | semantic overlap | ✓ |
| 4 | goose | yes (object 5) | duck | semantic overlap | ✓ |
| 5 | water | yes (object 6) | swan | mismatch | ✗ |
| 6 | goose | yes (object 7) | bird | hypernym/hyponym | ✓ |
| 7 | goose | yes (object 8) | bird (uncertain) | hypernym/hyponym | ✓ |
| 8 | goose | yes (object 9) | bird (uncertain) | hypernym/hyponym | ✓ |
| 9 | goose | yes (object 10) | bird (uncertain) | hypernym/hyponym | ✓ |
| 10 | bush | yes (object 11) | reeds | semantic overlap | ✓ |
| 11 | grass | yes (object 12) | plant | hypernym/hyponym | ✓ |
| 12 | tree | yes (object 13) | tree | identical | ✓ |
| 13 | trees | yes (object 14) | bush | semantic overlap | ✓ |
| 14 | tree | yes (object 15) | palm tree | hypernym/hyponym | ✓ |
| 15 | sky | yes (object 16) | cloud | semantic overlap | ✓ |
| 16 | crowd | yes (object 17) | person | hypernym/hyponym | ✓ |
| 17 | plant | yes (object 18) | plant | identical | ✓ |
| 18 | bank | yes (object 19) | bird (uncertain) | mismatch | ✗ |
| 19 | leaf | yes (object 20) | plant | semantic overlap | ✓ |
| 20 | bush | yes (object 21) | plant | hypernym/hyponym | ✓ |
| 21 | pot | yes (object 22) | bowl | semantic overlap | ✓ |
| 22 | pot | yes (object 23) | bowl | semantic overlap | ✓ |
| 23 | wooden board | yes (object 24) | log | semantic overlap | ✓ |
| 24 | bank | yes (object 25) | log | mismatch | ✗ |
| 25 | bank | yes (object 26) | log | mismatch | ✗ |
| 26 | goose | yes (object 27) | bird | hypernym/hyponym | ✓ |
| 27 | goose | yes (object 28) | bird | hypernym/hyponym | ✓ |
| 28 | goose | yes (object 29) | bird | hypernym/hyponym | ✓ |
| 29 | goose | yes (object 30) | bowl | mismatch | ✗ |
| 30 | goose | yes (object 31) | bird | hypernym/hyponym | ✓ |
| 31 | goose | yes (object 32) | bird | hypernym/hyponym | ✓ |
| 32 | goose | yes (object 33) | bird | hypernym/hyponym | ✓ |
| 33 | goose | yes (object 34) | bird | hypernym/hyponym | ✓ |
| 34 | goose | yes (object 35) | bird | hypernym/hyponym | ✓ |
| 35 | goose | yes (object 36) | bird | hypernym/hyponym | ✓ |
| 36 | tree | yes (object 37) | bush | semantic overlap | ✓ |
| 37 | tree | yes (object 38) | bush | semantic overlap | ✓ |
| 38 | tree | yes (object 39) | bush | semantic overlap | ✓ |
| 39 | grass | yes (object 40) | reeds | semantic overlap | ✓ |
| 40 | bush | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | bush | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | grass | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | bush | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | grass | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | grass | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | grass | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | grass | no: after the first 40 | - | no label from TRASER | ✗ |
| 48 | person | no: after the first 40 | - | no label from TRASER | ✗ |
| 49 | person | no: after the first 40 | - | no label from TRASER | ✗ |
| 50 | person | no: after the first 40 | - | no label from TRASER | ✗ |
| 51 | person | no: after the first 40 | - | no label from TRASER | ✗ |
| 52 | person | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 1/46 right, triplets: 1/46 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| goose #0 - in - water #5 | 0-8, 18-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #0 - swims in - water #5 | 0-7, 17-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #1 - in - water #5 | 0-8, 17.5-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #1 - swims in - water #5 | 2-7, 17-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #1 - follows - goose #0 | 1-8, 18-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #2 - in - water #5 | 0-2 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #3 - in - water #5 | 0-10.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #3 - swims in - water #5 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #3 - follows - goose #4 | 0-10 | near | 0-7 | semantic overlap | 0.70 | ✓ | ✓ |
| goose #4 - in - water #5 | 0-10.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #4 - swims in - water #5 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #6 - in - water #5 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #7 - in - water #5 | 0-5, 7-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #8 - in - water #5 | 0-3.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #9 - in - water #5 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| bush #10 - on - bank #18 | 0-7.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #12 - above - bank #18 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #15 - above - trees #13 | 0-2.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| bank #18 - adjacent to - water #5 | 0-10, 18-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| bush #20 - on - bank #24 | 13-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| pot #21 - on - bank #24 | 13-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| pot #22 - on - bank #24 | 13-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| wooden board #23 - over - water #5 | 14-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| wooden board #23 - on - bank #24 | 14-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| bank #24 - adjacent to - water #5 | 14-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| bank #25 - adjacent to - water #5 | 16-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #26 - on - bank #25 | 16-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #27 - on - bank #25 | 16-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #28 - on - bank #25 | 16.5-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #29 - on - bank #24 | 14-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #29 - on - bank #25 | 17-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #30 - swims in - water #5 | 6-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #30 - in - water #5 | 0-6, 7-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #30 - on - bank #25 | 17-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #31 - follows - goose #30 | 7-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #31 - swims in - water #5 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #31 - in - water #5 | 0-6, 7-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #31 - on - bank #25 | 17-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #32 - on - bank #25 | 17-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #33 - on - bank #25 | 17-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #34 - on - bank #25 | 17-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| goose #35 - on - bank #25 | 17-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| grass #39 - on - bank #18 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| bush #40 - on - bank #18 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| bush #41 - on - bank #18 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| bush #43 - on - bank #25 | 0-3, 18-22 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (55): goose #0 - approaches - goose #1 [17-20]; goose #0 - moves away from - goose #1 [19-21]; goose #0 - passes by - goose #1 [18-20]; goose #0 - near - goose #1 [0-7]; goose #0 - moves along - bank #25 [17-21]; goose #0 - behind - bank #25 [17-21]; goose #1 - moves along - bank #25 [17-21]; goose #1 - behind - bank #25 [17-21]; goose #0 - in front of - bush #10 [0-7]; goose #1 - in front of - bush #10 [0-7]


## sav_015587

13.33 s, 13 frames read | human: 41 objects, 28 relations | TRASER: 40 objects, 106 relations, valid JSON, 4384 tokens

**Objects: 25/41 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | cat | yes (object 1) | kitten | hypernym/hyponym | ✓ |
| 1 | cat | yes (object 2) | kitten | hypernym/hyponym | ✓ |
| 2 | cat | yes (object 3) | cat | identical | ✓ |
| 3 | cat | yes (object 4) | cat | identical | ✓ |
| 4 | cat | yes (object 5) | cat | identical | ✓ |
| 5 | cat | yes (object 6) | cat | identical | ✓ |
| 6 | cat | yes (object 7) | cat | identical | ✓ |
| 7 | cat | yes (object 8) | bowl | mismatch | ✗ |
| 8 | mat | yes (object 9) | doormat | hypernym/hyponym | ✓ |
| 9 | litter box | yes (object 10) | pet bed (uncertain) | mismatch | ✗ |
| 10 | lamp | yes (object 11) | lamp | identical | ✓ |
| 11 | curtain | yes (object 12) | curtain | identical | ✓ |
| 12 | platform | yes (object 13) | curtain | mismatch | ✗ |
| 13 | humidifier | yes (object 14) | power strip | mismatch | ✗ |
| 14 | floor | yes (object 15) | table | mismatch | ✗ |
| 15 | power cable | yes (object 16) | pipe (uncertain) | mismatch | ✗ |
| 16 | tent support pole | yes (object 17) | pole (uncertain) | hypernym/hyponym | ✓ |
| 17 | edge of framing | yes (object 18) | tray (uncertain) | mismatch | ✗ |
| 18 | pet bowl | yes (object 19) | bowl | hypernym/hyponym | ✓ |
| 19 | curtain | yes (object 20) | curtain | identical | ✓ |
| 20 | tube | yes (object 21) | pipe (uncertain) | synonym | ✓ |
| 21 | pet bed | yes (object 22) | tray (uncertain) | mismatch | ✗ |
| 22 | pet bowl | yes (object 23) | bowl | hypernym/hyponym | ✓ |
| 23 | curtain | yes (object 24) | curtain | identical | ✓ |
| 24 | sign | yes (object 25) | signboard | synonym | ✓ |
| 25 | light | yes (object 26) | bottle cap | mismatch | ✗ |
| 26 | flowers | yes (object 27) | flower arrangement | semantic overlap | ✓ |
| 27 | cat basket | yes (object 28) | bowl | mismatch | ✗ |
| 28 | pole | yes (object 29) | ribbon (uncertain) | mismatch | ✗ |
| 29 | pole | yes (object 30) | curtain | mismatch | ✗ |
| 30 | sign | yes (object 31) | poster | semantic overlap | ✓ |
| 31 | cushion | yes (object 32) | pillow | synonym | ✓ |
| 32 | toys | yes (object 33) | blanket | mismatch | ✗ |
| 33 | bowl | yes (object 34) | bowl | identical | ✓ |
| 34 | curtain | yes (object 35) | curtain | identical | ✓ |
| 35 | mat | yes (object 36) | cat | mismatch | ✗ |
| 36 | ball | yes (object 37) | ball | identical | ✓ |
| 37 | bowl | yes (object 38) | bowl | identical | ✓ |
| 38 | curtain | yes (object 39) | curtain | identical | ✓ |
| 39 | mat | yes (object 40) | cat | mismatch | ✗ |
| 40 | ball | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 5/28 right, triplets: 2/28 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| cat #0 - in front of - litter box #9 | 0-14 | in front of | 0-13 | identical | 0.93 | ✓ | ✗ |
| cat #0 - moves away from - cat #1 | 2.5-4 | nothing for this pair | - | - | - | ✗ | ✗ |
| cat #0 - on - mat #8 | 0-14 | on | 0-13 | identical | 0.93 | ✓ | ✓ |
| cat #1 - on - mat #8 | 0-14 | on | 0-13 | identical | 0.93 | ✓ | ✓ |
| cat #1 - in front of - litter box #9 | 0-14 | in front of | 0-13 | identical | 0.93 | ✓ | ✗ |
| cat #2 - in front of - litter box #9 | 0-12 | in front of | 0-13 | identical | 0.92 | ✓ | ✗ |
| cat #2 - jumps over - litter box #9 | 12-13 | in front of | 0-13 | mismatch | 0.08 | ✗ | ✗ |
| cat #2 - pounces on - cat #0 | 12-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| cat #2 - plays with - cat #0 | 12-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| cat #2 - looks at - cat #0 | 8-12 | nothing for this pair | - | - | - | ✗ | ✗ |
| cat #2 - play fights with - cat #0 | 12-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| cat #2 - approaches - cat #0 | 11-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| cat #3 - behind - litter box #9 | 0-14 | in front of | 0-13 | mismatch | 0.93 | ✗ | ✗ |
| cat #4 - behind - litter box #9 | 0-14 | in front of | 0-13 | mismatch | 0.93 | ✗ | ✗ |
| cat #5 - behind - litter box #9 | 0-14 | in front of | 0-13 | mismatch | 0.93 | ✗ | ✗ |
| cat #6 - behind - litter box #9 | 0-14 | in front of | 0-13 | mismatch | 0.93 | ✗ | ✗ |
| cat #7 - on - cat basket #27 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| cat #7 - behind - litter box #9 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| mat #8 - on - floor #14 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| lamp #10 - above - cat #1 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| lamp #10 - above - cat #1 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| lamp #10 - above - cat #2 | 0-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| power cable #15 - on - floor #14 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| cat basket #27 - behind - litter box #9 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| pole #28 - in front of - cat #3 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| pole #28 - in front of - cat #4 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| pole #28 - in front of - cat #5 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| pole #28 - in front of - cat #6 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (97): cat #2 - on - mat #8 [0-13]; cat #3 - on - mat #8 [0-13]; cat #4 - on - mat #8 [0-13]; cat #5 - on - mat #8 [0-13]; cat #6 - on - mat #8 [0-13]; mat #35 - on - mat #8 [0-13]; mat #39 - on - mat #8 [0-13]; mat #35 - in front of - litter box #9 [0-13]; mat #39 - in front of - litter box #9 [0-13]; cat #0 - in front of - cat #2 [0-13]


## sav_015763

20.71 s, 21 frames read | human: 14 objects, 30 relations | TRASER: 14 objects, 24 relations, valid JSON, 1266 tokens

**Objects: 14/14 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | filling | yes (object 1) | meatball | semantic overlap | ✓ |
| 1 | pan | yes (object 2) | pan | identical | ✓ |
| 2 | mat | yes (object 3) | place mat | hypernym/hyponym | ✓ |
| 3 | table | yes (object 4) | table | identical | ✓ |
| 4 | flowers | yes (object 5) | flower | identical | ✓ |
| 5 | hand | yes (object 6) | hand | identical | ✓ |
| 6 | hand | yes (object 7) | hand | identical | ✓ |
| 7 | dough | yes (object 8) | dough | identical | ✓ |
| 8 | dough | yes (object 9) | dough | identical | ✓ |
| 9 | chopstick | yes (object 10) | chopstick | identical | ✓ |
| 10 | chopstick | yes (object 11) | chopstick | identical | ✓ |
| 11 | bowl | yes (object 12) | bowl | identical | ✓ |
| 12 | bowl | yes (object 13) | plate | semantic overlap | ✓ |
| 13 | oil | yes (object 14) | liquid | hypernym/hyponym | ✓ |

**Relations: 10/30 right, triplets: 10/30 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| filling #0 - on - dough #7 | 10-13 | on | 0-2, 9-12 | identical | 0.33 | ✗ | ✗ |
| filling #0 - on - dough #7 | 0-1, 10-13.5 | on | 0-2, 9-12 | identical | 0.46 | ✗ | ✗ |
| pan #1 - on - table #3 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| pan #1 - behind - mat #2 | 0-21 | on | 0-21 | mismatch | 1.00 | ✗ | ✗ |
| mat #2 - on - table #3 | 0-21 | on | 0-21 | identical | 1.00 | ✓ | ✓ |
| flowers #4 - behind - pan #1 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #5 - holds - dough #7 | 5-19 | holding (+3 more) | 0-2, 3-4, 5-21 | identical | 0.74 | ✓ | ✓ |
| hand #5 - prepares - dough #7 | 1-19 | preparing (+3 more) | 5-21 | identical | 0.70 | ✓ | ✓ |
| hand #5 - wraps - dough #7 | 12-17 | holding (+3 more) | 0-2, 3-4, 5-21 | semantic overlap | 0.26 | ✗ | ✗ |
| hand #5 - uses - chopstick #9 | 1-7 | holding | 0-2, 3-4 | semantic overlap | 0.29 | ✗ | ✗ |
| hand #5 - stretches - dough #8 | 1-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #6 - holds - dough #7 | 5-8, 12-19 | holding (+3 more) | 0-2, 3-4, 5-21 | identical | 0.53 | ✓ | ✓ |
| hand #6 - wraps - dough #7 | 12-17 | holding (+3 more) | 0-2, 3-4, 5-21 | semantic overlap | 0.26 | ✗ | ✗ |
| hand #6 - places - dough #7 | 18.5-21 | touching (+3 more) | 0-2, 3-4, 5-21 | semantic overlap | 0.13 | ✗ | ✗ |
| hand #6 - transfers - dough #7 | 18-20 | holding (+3 more) | 0-2, 3-4, 5-21 | semantic overlap | 0.11 | ✗ | ✗ |
| hand #6 - uses - chopstick #10 | 0.5-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #6 - stretches - dough #8 | 1-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| dough #7 - on - hand #5 | 5.5-19.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| dough #7 - above - bowl #12 | 1-19.5 | above | 0-21 | identical | 0.88 | ✓ | ✓ |
| dough #7 - moves away from - bowl #12 | 18-20 | above | 0-21 | mismatch | 0.10 | ✗ | ✗ |
| dough #7 - in - pan #1 | 19-21 | above (+2 more) | 0-21 | mismatch | 0.10 | ✗ | ✗ |
| dough #7 - in - pan #1 | 18.5-21 | above (+2 more) | 0-21 | mismatch | 0.12 | ✗ | ✗ |
| dough #7 - moves into - pan #1 | 18.5-20 | moving toward (+2 more) | 5-11 | semantic overlap | 0.00 | ✗ | ✗ |
| dough #8 - in - bowl #12 | 0-21 | on | 0-21 | semantic overlap | 1.00 | ✓ | ✓ |
| dough #8 - in - bowl #12 | 0-21 | on | 0-21 | semantic overlap | 1.00 | ✓ | ✓ |
| chopstick #10 - above - bowl #12 | 1-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| bowl #11 - on - table #3 | 0-13, 14-21 | on | 0-21 | identical | 0.95 | ✓ | ✓ |
| bowl #12 - on - mat #2 | 0-21 | on | 0-21 | identical | 1.00 | ✓ | ✓ |
| bowl #12 - in front of - pan #1 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| oil #13 - in - pan #1 | 0-21 | in | 0-21 | identical | 1.00 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (4): hand #5 - holding - chopstick #10 [0-2, 3-4]; flowers #4 - on - table #3 [0-21]; chopstick #9 - touching - dough #7 [0-2, 3-4]; chopstick #10 - touching - dough #7 [0-2, 3-4]


## sav_016333

21.38 s, 21 frames read | human: 39 objects, 5 relations | TRASER: 38 objects, 39 relations, valid JSON, 2691 tokens

**Objects: 28/39 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | woman | yes (object 1) | person | hypernym/hyponym | ✓ |
| 1 | woman | yes (object 2) | person | hypernym/hyponym | ✓ |
| 2 | floor | yes (object 3) | floor lamp | mismatch | ✗ |
| 3 | man | yes (object 4) | person | hypernym/hyponym | ✓ |
| 4 | game retail chain or shop | yes (object 5) | signboard | mismatch | ✗ |
| 5 | ceiling | yes (object 6) | ceiling | identical | ✓ |
| 6 | woman | yes (object 7) | person | hypernym/hyponym | ✓ |
| 7 | woman | no: no mask on the frames TRASER reads | - | no label from TRASER | ✗ |
| 8 | person | yes (object 8) | person | identical | ✓ |
| 9 | girl | yes (object 9) | person | hypernym/hyponym | ✓ |
| 10 | woman | yes (object 10) | person | hypernym/hyponym | ✓ |
| 11 | man | yes (object 11) | person | hypernym/hyponym | ✓ |
| 12 | man | yes (object 12) | person | hypernym/hyponym | ✓ |
| 13 | boy | yes (object 13) | child | hypernym/hyponym | ✓ |
| 14 | person | yes (object 14) | person | identical | ✓ |
| 15 | person | yes (object 15) | person | identical | ✓ |
| 16 | people | yes (object 16) | person | hypernym/hyponym | ✓ |
| 17 | bag | yes (object 17) | shopping bag | hypernym/hyponym | ✓ |
| 18 | bag | yes (object 18) | person | mismatch | ✗ |
| 19 | shelves | yes (object 19) | signboard | mismatch | ✗ |
| 20 | barrier or pillar | yes (object 20) | poster | mismatch | ✗ |
| 21 | floor | yes (object 21) | floor lamp | mismatch | ✗ |
| 22 | floor | yes (object 22) | floor | identical | ✓ |
| 23 | poster | yes (object 23) | poster | identical | ✓ |
| 24 | poster | yes (object 24) | poster | identical | ✓ |
| 25 | shelf | yes (object 25) | signboard | mismatch | ✗ |
| 26 | light | yes (object 26) | vent (uncertain) | mismatch | ✗ |
| 27 | light | yes (object 27) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 28 | light | yes (object 28) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 29 | light | yes (object 29) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 30 | light | yes (object 30) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 31 | light | yes (object 31) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 32 | clothes | yes (object 32) | coat | hypernym/hyponym | ✓ |
| 33 | pants | yes (object 33) | trousers | synonym | ✓ |
| 34 | clothes | yes (object 34) | jacket | hypernym/hyponym | ✓ |
| 35 | pants | yes (object 35) | shopping bag | mismatch | ✗ |
| 36 | clothes | yes (object 36) | backpack | mismatch | ✗ |
| 37 | backpack | yes (object 37) | backpack | identical | ✓ |
| 38 | pants | yes (object 38) | jeans (uncertain) | hypernym/hyponym | ✓ |

**Relations: 0/5 right, triplets: 0/5 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| woman #1 - wears - backpack #37 | 0-22 | carrying | 0-21 | mismatch | 0.95 | ✗ | ✗ |
| man #12 - carries - bag #18 | 18-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #12 - passes - woman #0 | 18-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| boy #13 - approaches - barrier or pillar #20 | 0-2 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #14 - approaches - barrier or pillar #20 | 10-15, 16-17 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (38): woman #0 - wearing - clothes #32 [0-19]; woman #0 - wearing - pants #33 [0-19]; woman #1 - carrying - clothes #36 [0-21]; woman #0 - walking with - woman #1 [0-19]; woman #0 - next to - woman #1 [0-19]; woman #0 - approaching - barrier or pillar #20 [0-19]; woman #0 - moving away from - barrier or pillar #20 [19-21]; woman #0 - in front of - barrier or pillar #20 [0-19]; woman #1 - approaching - barrier or pillar #20 [0-19]; woman #1 - moving away from - barrier or pillar #20 [19-21]


## sav_023013

18.21 s, 18 frames read | human: 25 objects, 25 relations | TRASER: 25 objects, 27 relations, valid JSON, 1887 tokens

**Objects: 20/25 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | pork knuckle | yes (object 1) | roasted chicken | mismatch | ✗ |
| 1 | baking tray | yes (object 2) | tray | hypernym/hyponym | ✓ |
| 2 | cooktop | yes (object 3) | stove top | identical | ✓ |
| 3 | spoon | yes (object 4) | spoon | identical | ✓ |
| 4 | bottle | yes (object 5) | jar | semantic overlap | ✓ |
| 5 | countertop | yes (object 6) | countertop (uncertain) | identical | ✓ |
| 6 | wall | yes (object 7) | tile | mismatch | ✗ |
| 7 | box | yes (object 8) | wooden plank (uncertain) | mismatch | ✗ |
| 8 | seasoning set | yes (object 9) | canister | semantic overlap | ✓ |
| 9 | hand | yes (object 10) | hand | identical | ✓ |
| 10 | hand | yes (object 11) | hand | identical | ✓ |
| 11 | torch | yes (object 12) | torch | identical | ✓ |
| 12 | bottle | yes (object 13) | canister | semantic overlap | ✓ |
| 13 | bottle | yes (object 14) | canister | semantic overlap | ✓ |
| 14 | bottle | yes (object 15) | canister | semantic overlap | ✓ |
| 15 | bottle | yes (object 16) | canister | semantic overlap | ✓ |
| 16 | grease | yes (object 17) | liquid | hypernym/hyponym | ✓ |
| 17 | nozzle | yes (object 18) | pipe (uncertain) | semantic overlap | ✓ |
| 18 | flame | yes (object 19) | flame | identical | ✓ |
| 19 | handle | yes (object 20) | hand | mismatch | ✗ |
| 20 | button | yes (object 21) | canister | mismatch | ✗ |
| 21 | torch body | yes (object 22) | torch | semantic overlap | ✓ |
| 22 | heating zone | yes (object 23) | stove burner | synonym | ✓ |
| 23 | heating zone | yes (object 24) | stove burner cover (uncertain) | semantic overlap | ✓ |
| 24 | heating zone | yes (object 25) | stove burner (uncertain) | synonym | ✓ |

**Relations: 13/25 right, triplets: 6/25 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| pork knuckle #0 - over - cooktop #2 | 0-19 | above | 0-18 | synonym | 0.95 | ✓ | ✗ |
| pork knuckle #0 - in - baking tray #1 | 0-19 | in | 0-18 | identical | 0.95 | ✓ | ✗ |
| baking tray #1 - on - cooktop #2 | 0-19 | on | 0-18 | identical | 0.95 | ✓ | ✓ |
| baking tray #1 - on - heating zone #22 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| cooktop #2 - in front of - wall #6 | 0-19 | in front of | 0-18 | identical | 0.95 | ✓ | ✗ |
| spoon #3 - in - baking tray #1 | 0-19 | in | 0-18 | identical | 0.95 | ✓ | ✓ |
| countertop #5 - in front of - wall #6 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| box #7 - on - countertop #5 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| seasoning set #8 - on - countertop #5 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #9 - holds - spoon #3 | 0-8.5 | holding (+1 more) | 0-5 | identical | 0.59 | ✓ | ✓ |
| hand #9 - bastes - pork knuckle #0 | 1-2 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #10 - holds - torch #11 | 2-19 | holding (+2 more) | 0-18 | identical | 0.84 | ✓ | ✓ |
| hand #10 - torches - pork knuckle #0 | 2-19 | heating | 0-18 | semantic overlap | 0.84 | ✓ | ✗ |
| hand #10 - sears - pork knuckle #0 | 2-19 | heating | 0-18 | hypernym/hyponym | 0.84 | ✓ | ✗ |
| torch #11 - over - cooktop #2 | 0-19 | above | 0-18 | synonym | 0.95 | ✓ | ✓ |
| torch #11 - moves around - pork knuckle #0 | 3-19 | moving over (+1 more) | 0-18 | semantic overlap | 0.79 | ✓ | ✗ |
| grease #16 - around - pork knuckle #0 | 0-19 | below | 0-18 | mismatch | 0.95 | ✗ | ✗ |
| grease #16 - in - baking tray #1 | 0-19 | in | 0-18 | identical | 0.95 | ✓ | ✓ |
| nozzle #17 - attached to - torch #11 | 2-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| nozzle #17 - over - baking tray #1 | 2-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| nozzle #17 - over - pork knuckle #0 | 2-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| flame #18 - over - pork knuckle #0 | 2-19 | above (+1 more) | 0-18 | synonym | 0.84 | ✓ | ✗ |
| flame #18 - in front of - nozzle #17 | 2-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| flame #18 - over - baking tray #1 | 2-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| torch body #21 - part of - torch #11 | 2-19 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (9): heating zone #22 - in - cooktop #2 [0-18]; flame #18 - above - heating zone #22 [0-18]; torch #11 - above - baking tray #1 [0-18]; spoon #3 - above - cooktop #2 [0-18]; baking tray #1 - in front of - wall #6 [0-18]; pork knuckle #0 - in front of - wall #6 [0-18]; torch #11 - in front of - wall #6 [0-18]; flame #18 - in front of - wall #6 [0-18]; spoon #3 - in front of - wall #6 [0-18]


## sav_023742

21.38 s, 21 frames read | human: 24 objects, 5 relations | TRASER: 24 objects, 72 relations, valid JSON, 3408 tokens

**Objects: 15/24 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | dog | yes (object 1) | dog | identical | ✓ |
| 1 | dog | yes (object 2) | dog | identical | ✓ |
| 2 | led | yes (object 3) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 3 | plastic mat | yes (object 4) | mat | hypernym/hyponym | ✓ |
| 4 | plastic mat | yes (object 5) | mat | hypernym/hyponym | ✓ |
| 5 | toy | yes (object 6) | plush toy (uncertain) | hypernym/hyponym | ✓ |
| 6 | toy | yes (object 7) | toy (uncertain) | identical | ✓ |
| 7 | toy | yes (object 8) | toy (uncertain) | identical | ✓ |
| 8 | toy | yes (object 9) | plush toy (uncertain) | hypernym/hyponym | ✓ |
| 9 | food bowl | yes (object 10) | bowl | hypernym/hyponym | ✓ |
| 10 | sink | yes (object 11) | sink | identical | ✓ |
| 11 | glass | yes (object 12) | door (uncertain) | mismatch | ✗ |
| 12 | pet care products | yes (object 13) | table | mismatch | ✗ |
| 13 | background | yes (object 14) | mirror | mismatch | ✗ |
| 14 | ceiling | yes (object 15) | ceiling light fixture | semantic overlap | ✓ |
| 15 | light | yes (object 16) | light fixture (uncertain) | hypernym/hyponym | ✓ |
| 16 | vent | yes (object 17) | fan blade (uncertain) | semantic overlap | ✓ |
| 17 | floor | yes (object 18) | tray | mismatch | ✗ |
| 18 | plexiglass joint | yes (object 19) | pole (uncertain) | mismatch | ✗ |
| 19 | background | yes (object 20) | mirror | mismatch | ✗ |
| 20 | water dispenser | yes (object 21) | fan | mismatch | ✗ |
| 21 | trash can | yes (object 22) | box | mismatch | ✗ |
| 22 | cabinet | yes (object 23) | mirror | mismatch | ✗ |
| 23 | towel | yes (object 24) | towel | identical | ✓ |

**Relations: 4/5 right, triplets: 4/5 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| dog #0 - leaning on - glass #11 | 0-8, 14-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| dog #0 - jumping on - plastic mat #3 | 3-9, 14-22 | standing on (+1 more) | 0-8, 13-21 | semantic overlap | 0.67 | ✓ | ✓ |
| dog #0 - standing on - plastic mat #3 | 0-8, 14-22 | standing on (+1 more) | 0-8, 13-21 | identical | 0.88 | ✓ | ✓ |
| dog #1 - standing on - plastic mat #4 | 9-14 | on | 10-14 | hypernym/hyponym | 0.80 | ✓ | ✓ |
| dog #1 - moving on - plastic mat #4 | 9-14 | on | 10-14 | semantic overlap | 0.80 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (69): dog #0 - looking at - dog #1 [13-15]; dog #1 - approaching - dog #0 [13-15]; dog #1 - moving away from - dog #0 [14-16]; dog #0 - in front of - background #19 [0-8, 13-21]; dog #0 - below - ceiling #14 [0-8, 13-21]; dog #0 - in front of - sink #10 [0-8, 13-21]; dog #0 - in front of - water dispenser #20 [0-8, 13-21]; dog #0 - in front of - trash can #21 [0-8, 13-21]; dog #0 - in front of - towel #23 [0-8, 13-21]; dog #0 - in front of - background #13 [0-8, 13-21]


## sav_023860

17.58 s, 18 frames read | human: 41 objects, 73 relations | TRASER: 40 objects, 71 relations, valid JSON, 3178 tokens

**Objects: 35/41 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | person | yes (object 2) | person | identical | ✓ |
| 2 | person | yes (object 3) | person | identical | ✓ |
| 3 | person | yes (object 4) | person | identical | ✓ |
| 4 | person | yes (object 5) | person | identical | ✓ |
| 5 | person | yes (object 6) | person | identical | ✓ |
| 6 | person | yes (object 7) | person | identical | ✓ |
| 7 | person | yes (object 8) | person | identical | ✓ |
| 8 | person | yes (object 9) | person | identical | ✓ |
| 9 | person | yes (object 10) | person | identical | ✓ |
| 10 | person | yes (object 11) | person | identical | ✓ |
| 11 | treadmill | yes (object 12) | exercise machine | hypernym/hyponym | ✓ |
| 12 | treadmill | yes (object 13) | treadmill | identical | ✓ |
| 13 | treadmill | yes (object 14) | treadmill | identical | ✓ |
| 14 | treadmill | yes (object 15) | treadmill belt | semantic overlap | ✓ |
| 15 | ground | yes (object 16) | treadmill | mismatch | ✗ |
| 16 | ceiling | yes (object 17) | ceiling | identical | ✓ |
| 17 | treadmill | yes (object 18) | treadmill belt | semantic overlap | ✓ |
| 18 | treadmill | yes (object 19) | treadmill belt | semantic overlap | ✓ |
| 19 | treadmill | yes (object 20) | treadmill belt | semantic overlap | ✓ |
| 20 | treadmill | yes (object 21) | treadmill | identical | ✓ |
| 21 | treadmill | yes (object 22) | treadmill | identical | ✓ |
| 22 | treadmill | yes (object 23) | treadmill | identical | ✓ |
| 23 | treadmill | yes (object 24) | treadmill | identical | ✓ |
| 24 | treadmill | yes (object 25) | treadmill | identical | ✓ |
| 25 | treadmill | yes (object 26) | treadmill | identical | ✓ |
| 26 | wall | yes (object 27) | counter | mismatch | ✗ |
| 27 | tree | yes (object 28) | Christmas tree | hypernym/hyponym | ✓ |
| 28 | glass | yes (object 29) | television screen | mismatch | ✗ |
| 29 | tv | yes (object 30) | television screen | hypernym/hyponym | ✓ |
| 30 | tv | yes (object 31) | television | identical | ✓ |
| 31 | tv | yes (object 32) | person | mismatch | ✗ |
| 32 | tv | yes (object 33) | television | identical | ✓ |
| 33 | tv | yes (object 34) | television | identical | ✓ |
| 34 | t-shirt | yes (object 35) | jersey | semantic overlap | ✓ |
| 35 | t-shirt | yes (object 36) | jersey | semantic overlap | ✓ |
| 36 | t-shirt | yes (object 37) | jersey | semantic overlap | ✓ |
| 37 | t-shirt | yes (object 38) | jersey | semantic overlap | ✓ |
| 38 | t-shirt | yes (object 39) | jersey | semantic overlap | ✓ |
| 39 | t-shirt | yes (object 40) | person | mismatch | ✗ |
| 40 | speaker | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 19/73 right, triplets: 1/73 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - on - treadmill #12 | 0-18 | on | 0-18 | identical | 1.00 | ✓ | ✓ |
| person #0 - using - treadmill #12 | 0-18 | on | 0-18 | mismatch | 1.00 | ✗ | ✗ |
| person #0 - in front of - glass #28 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - wearing - t-shirt #34 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - below - ceiling #16 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - in front of - wall #26 | 0-18 | in front of | 0-18 | identical | 1.00 | ✓ | ✗ |
| person #1 - on - treadmill #12 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - wearing - t-shirt #35 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - using - treadmill #13 | 0-18 | on | 0-18 | mismatch | 1.00 | ✗ | ✗ |
| person #1 - in front of - glass #28 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - below - ceiling #16 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - in front of - wall #26 | 0-18 | in front of | 0-18 | identical | 1.00 | ✓ | ✗ |
| person #2 - on - treadmill #12 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - wearing - t-shirt #36 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - in front of - glass #28 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - below - ceiling #16 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - in front of - wall #26 | 0-18 | in front of | 0-18 | identical | 1.00 | ✓ | ✗ |
| person #3 - on - treadmill #12 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - wearing - t-shirt #37 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - below - ceiling #16 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - in front of - wall #26 | 0-18 | in front of | 0-18 | identical | 1.00 | ✓ | ✗ |
| person #3 - in front of - glass #28 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - on - treadmill #12 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - below - ceiling #16 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - in front of - wall #26 | 0-18 | in front of | 0-18 | identical | 1.00 | ✓ | ✗ |
| person #4 - in front of - glass #28 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - on - treadmill #12 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - wearing - t-shirt #38 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - in front of - glass #28 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - below - ceiling #16 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #5 - in front of - wall #26 | 0-18 | in front of | 0-18 | identical | 1.00 | ✓ | ✗ |
| person #6 - below - ceiling #16 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #6 - in front of - wall #26 | 0-3 | in front of | 0-18 | identical | 0.17 | ✗ | ✗ |
| person #7 - below - ceiling #16 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #7 - in front of - wall #26 | 0-16 | in front of | 0-18 | identical | 0.89 | ✓ | ✗ |
| person #8 - below - ceiling #16 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #8 - in front of - wall #26 | 0-18 | in front of (+1 more) | 0-18 | identical | 1.00 | ✓ | ✗ |
| person #9 - below - ceiling #16 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #9 - in front of - wall #26 | 0-18 | in front of (+1 more) | 0-18 | identical | 1.00 | ✓ | ✗ |
| person #10 - below - ceiling #16 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #10 - in front of - wall #26 | 0-18 | in front of (+1 more) | 0-18 | identical | 1.00 | ✓ | ✗ |
| treadmill #12 - in front of - wall #26 | 0-18 | in front of | 0-18 | identical | 1.00 | ✓ | ✗ |
| treadmill #12 - on - ground #15 | 0-18 | parallel to | 0-18 | mismatch | 1.00 | ✗ | ✗ |
| treadmill #13 - in front of - wall #26 | 0-18 | in front of | 0-18 | identical | 1.00 | ✓ | ✗ |
| treadmill #13 - on - ground #15 | 0-18 | parallel to (+1 more) | 0-18 | mismatch | 1.00 | ✗ | ✗ |
| treadmill #14 - in front of - wall #26 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| treadmill #14 - on - ground #15 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| treadmill #17 - on - ground #15 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| treadmill #18 - on - ground #15 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| treadmill #19 - on - ground #15 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| treadmill #20 - on - ground #15 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| treadmill #20 - in front of - wall #26 | 0-18 | in front of | 0-18 | identical | 1.00 | ✓ | ✗ |
| treadmill #21 - on - ground #15 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| treadmill #21 - in front of - wall #26 | 0-18 | in front of | 0-18 | identical | 1.00 | ✓ | ✗ |
| treadmill #22 - on - ground #15 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| treadmill #22 - in front of - wall #26 | 0-18 | in front of | 0-18 | identical | 1.00 | ✓ | ✗ |
| treadmill #23 - on - ground #15 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| treadmill #23 - in front of - wall #26 | 0-18 | in front of | 0-18 | identical | 1.00 | ✓ | ✗ |
| treadmill #24 - on - ground #15 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| treadmill #24 - in front of - wall #26 | 0-18 | in front of | 0-18 | identical | 1.00 | ✓ | ✗ |
| treadmill #25 - on - ground #15 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| treadmill #25 - in front of - wall #26 | 0-18 | in front of | 0-18 | identical | 1.00 | ✓ | ✗ |
| tree #27 - on - ground #15 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #27 - below - ceiling #16 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| glass #28 - below - ceiling #16 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| tv #29 - below - ceiling #16 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| tv #30 - below - ceiling #16 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| tv #30 - above - person #0 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| tv #31 - below - ceiling #16 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| tv #32 - below - ceiling #16 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| tv #33 - below - ceiling #16 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| speaker #40 - on - wall #26 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| speaker #40 - below - ceiling #16 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (44): person #2 - on - treadmill #13 [0-18]; person #3 - on - treadmill #13 [0-18]; person #4 - on - treadmill #13 [0-18]; person #5 - on - treadmill #13 [0-18]; person #6 - on - treadmill #13 [0-18]; person #7 - on - treadmill #13 [0-18]; wall #26 - below - ceiling #16 [0-18]; tree #27 - behind - wall #26 [0-18]; glass #28 - above - person #0 [0-18]; glass #28 - above - person #1 [0-18]


## sav_025082

14.79 s, 15 frames read | human: 48 objects, 9 relations | TRASER: 40 objects, 87 relations, valid JSON, 4169 tokens

**Objects: 29/48 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | kitchen drawers | yes (object 1) | cabinet | semantic overlap | ✓ |
| 1 | stove | yes (object 2) | washing machine | mismatch | ✗ |
| 2 | plant | yes (object 3) | flowerpot | semantic overlap | ✓ |
| 3 | window | yes (object 4) | window (uncertain) | identical | ✓ |
| 4 | gas cyclinder | yes (object 5) | skirt | mismatch | ✗ |
| 5 | kitchen counter | yes (object 6) | countertop | synonym | ✓ |
| 6 | rag | yes (object 7) | doormat | mismatch | ✗ |
| 7 | floor | yes (object 8) | shoes | mismatch | ✗ |
| 8 | kitchen counter | yes (object 9) | drawer | mismatch | ✗ |
| 9 | laundry machine | yes (object 10) | bathtub | mismatch | ✗ |
| 10 | kitchen wall | yes (object 11) | wall | hypernym/hyponym | ✓ |
| 11 | person | yes (object 12) | person | identical | ✓ |
| 12 | mop stick | yes (object 13) | trousers | mismatch | ✗ |
| 13 | handle | yes (object 14) | handle | identical | ✓ |
| 14 | handle | yes (object 15) | handle | identical | ✓ |
| 15 | handle | yes (object 16) | handle | identical | ✓ |
| 16 | handle | yes (object 17) | handle | identical | ✓ |
| 17 | drawer | yes (object 18) | drawer | identical | ✓ |
| 18 | drawer | yes (object 19) | drawer | identical | ✓ |
| 19 | drawer | yes (object 20) | drawer | identical | ✓ |
| 20 | cabinet | yes (object 21) | cabinet | identical | ✓ |
| 21 | drawer | yes (object 22) | drawer | identical | ✓ |
| 22 | counter top | yes (object 23) | sink | semantic overlap | ✓ |
| 23 | burner of a cooker | yes (object 24) | stove | hypernym/hyponym | ✓ |
| 24 | foot mat | yes (object 25) | trash can (uncertain) | mismatch | ✗ |
| 25 | shelf | yes (object 26) | shelf (uncertain) | identical | ✓ |
| 26 | household item | yes (object 27) | faucet | hypernym/hyponym | ✓ |
| 27 | cord | yes (object 28) | faucet | mismatch | ✗ |
| 28 | household item | yes (object 29) | bowl | hypernym/hyponym | ✓ |
| 29 | household item | yes (object 30) | pipe (uncertain) | hypernym/hyponym | ✓ |
| 30 | cloth | yes (object 31) | flowerpot | mismatch | ✗ |
| 31 | oven | yes (object 32) | washing machine | semantic overlap | ✓ |
| 32 | oven door | yes (object 33) | washing machine | mismatch | ✗ |
| 33 | control panel | yes (object 34) | knob (uncertain) | semantic overlap | ✓ |
| 34 | plant | yes (object 35) | plant | identical | ✓ |
| 35 | tray | yes (object 36) | basket | semantic overlap | ✓ |
| 36 | wall | yes (object 37) | wall | identical | ✓ |
| 37 | wall | yes (object 38) | wall | identical | ✓ |
| 38 | wall | yes (object 39) | wall | identical | ✓ |
| 39 | wall | yes (object 40) | wall | identical | ✓ |
| 40 | wall | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | shorts | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | shirt | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | hand | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | broom handle | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | brush | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | legs | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | face | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 0/9 right, triplets: 0/9 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| rag #6 - moves on - floor #7 | 4-12 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #11 - wear - shirt #42 | 1-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #11 - moves relative to - stove #1 | 1-2, 3-15 | moving away from (+5 more) | 11-15 | hypernym/hyponym | 0.31 | ✗ | ✗ |
| person #11 - wear - shorts #41 | 1-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #11 - clean - floor #7 | 2-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #11 - sweep - floor #7 | 2-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #11 - use - brush #45 | 10-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #11 - hold - mop stick #12 | 1-15 | wearing (+1 more) | 0-2, 4-15 | mismatch | 0.80 | ✗ | ✗ |
| mop stick #12 - moves on - floor #7 | 2-15 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (79): person #11 - wearing - gas cyclinder #4 [0-2, 4-5, 12-15]; person #11 - in front of - gas cyclinder #4 [0-2, 4-5, 12-15]; kitchen drawers #0 - in front of - kitchen wall #10 [0-15]; stove #1 - in front of - kitchen wall #10 [0-15]; stove #1 - in front of - wall #38 [0-15]; stove #1 - in front of - wall #38 [0-15]; stove #1 - in front of - wall #37 [0-15]; stove #1 - in front of - wall #37 [0-15]; stove #1 - in front of - wall #36 [0-15]; stove #1 - in front of - wall #36 [0-15]


## sav_026800

16.38 s, 16 frames read | human: 19 objects, 10 relations | TRASER: 19 objects, 43 relations, valid JSON, 1818 tokens

**Objects: 12/19 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | road | yes (object 1) | person | mismatch | ✗ |
| 1 | person | yes (object 2) | person | identical | ✓ |
| 2 | person | yes (object 3) | person | identical | ✓ |
| 3 | plants | yes (object 4) | curb (uncertain) | mismatch | ✗ |
| 4 | signboard | yes (object 5) | signboard | identical | ✓ |
| 5 | truck | yes (object 6) | truck | identical | ✓ |
| 6 | sky | yes (object 7) | awning | mismatch | ✗ |
| 7 | building | yes (object 8) | building | identical | ✓ |
| 8 | car | yes (object 9) | truck | semantic overlap | ✓ |
| 9 | car | yes (object 10) | car | identical | ✓ |
| 10 | car | yes (object 11) | truck | semantic overlap | ✓ |
| 11 | person | yes (object 12) | motorcycle | mismatch | ✗ |
| 12 | floor | yes (object 13) | curb (uncertain) | mismatch | ✗ |
| 13 | pole | yes (object 14) | pole | identical | ✓ |
| 14 | truck | yes (object 15) | signboard | mismatch | ✗ |
| 15 | motorcycle | yes (object 16) | motorcycle | identical | ✓ |
| 16 | barrel | yes (object 17) | trash can (uncertain) | semantic overlap | ✓ |
| 17 | person | yes (object 18) | person | identical | ✓ |
| 18 | frame | yes (object 19) | cart | mismatch | ✗ |

**Relations: 4/10 right, triplets: 4/10 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #1 - has arm around - person #2 | 0-6, 7-13.5, 14.5-17 | next to (+1 more) | 0-16 | semantic overlap | 0.82 | ✓ | ✓ |
| person #1 - walks with - person #2 | 0-6, 7-13.5, 14.5-17 | walking with (+1 more) | 0-16 | identical | 0.82 | ✓ | ✓ |
| person #1 - approaches - car #9 | 7.5-13, 14.5-17 | in front of (+1 more) | 0-16 | mismatch | 0.41 | ✗ | ✗ |
| person #1 - passes - motorcycle #15 | 10-13 | in front of (+2 more) | 0-13 | semantic overlap | 0.23 | ✗ | ✗ |
| person #1 - approaches - motorcycle #15 | 1-11 | approaching (+2 more) | 0-11 | identical | 0.91 | ✓ | ✓ |
| person #2 - walks with - person #1 | 0-6, 7-13.5, 14.5-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - approaches - car #9 | 6.5-13, 14.5-17 | in front of (+1 more) | 0-16 | mismatch | 0.47 | ✗ | ✗ |
| person #2 - passes - motorcycle #15 | 10-13 | in front of (+2 more) | 0-13 | semantic overlap | 0.23 | ✗ | ✗ |
| person #2 - approaches - motorcycle #15 | 0-11 | approaching (+2 more) | 0-11 | identical | 1.00 | ✓ | ✓ |
| signboard #4 - attached to - building #7 | 0-2.5 | on | 0-8 | hypernym/hyponym | 0.31 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (30): person #1 - approaching - frame #18 [0-11]; person #1 - in front of - frame #18 [0-11]; person #2 - approaching - frame #18 [0-11]; person #2 - in front of - frame #18 [0-11]; person #1 - under - sky #6 [0-16]; person #2 - under - sky #6 [0-16]; person #1 - in front of - building #7 [0-16]; person #2 - in front of - building #7 [0-16]; person #1 - in front of - person #17 [0-9]; person #2 - in front of - person #17 [0-9]


## sav_028579

19.08 s, 19 frames read | human: 50 objects, 30 relations | TRASER: 40 objects, 73 relations, valid JSON, 3548 tokens

**Objects: 32/50 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | cloth | yes (object 2) | person | mismatch | ✗ |
| 2 | cloth | yes (object 3) | trousers (uncertain) | semantic overlap | ✓ |
| 3 | sneakers | yes (object 4) | shoe | hypernym/hyponym | ✓ |
| 4 | sneakers | yes (object 5) | shoe | hypernym/hyponym | ✓ |
| 5 | carpet | yes (object 6) | floorboard | semantic overlap | ✓ |
| 6 | light | yes (object 7) | lamp | hypernym/hyponym | ✓ |
| 7 | plates | yes (object 8) | pot | mismatch | ✗ |
| 8 | picture frame | yes (object 9) | picture frame | identical | ✓ |
| 9 | picture frame | yes (object 10) | picture frame | identical | ✓ |
| 10 | door | yes (object 11) | door | identical | ✓ |
| 11 | camera | yes (object 12) | fire alarm | mismatch | ✗ |
| 12 | dining chair | yes (object 13) | chair | hypernym/hyponym | ✓ |
| 13 | door | yes (object 14) | door | identical | ✓ |
| 14 | hair | yes (object 15) | hair | identical | ✓ |
| 15 | side of a wall | yes (object 16) | wall | semantic overlap | ✓ |
| 16 | side of a wall | yes (object 17) | wall | semantic overlap | ✓ |
| 17 | wine rack | yes (object 18) | bottle | mismatch | ✗ |
| 18 | walls | yes (object 19) | person | mismatch | ✗ |
| 19 | left hand | yes (object 20) | hand | hypernym/hyponym | ✓ |
| 20 | left hand | yes (object 21) | hand | hypernym/hyponym | ✓ |
| 21 | face | yes (object 22) | head (uncertain) | hypernym/hyponym | ✓ |
| 22 | face | yes (object 23) | hair | mismatch | ✗ |
| 23 | bottle | yes (object 24) | bottle | identical | ✓ |
| 24 | bottle | yes (object 25) | cup | semantic overlap | ✓ |
| 25 | light | yes (object 26) | lampshade | semantic overlap | ✓ |
| 26 | light | yes (object 27) | lamp | hypernym/hyponym | ✓ |
| 27 | chair | yes (object 28) | chair | identical | ✓ |
| 28 | chair | yes (object 29) | curtain | mismatch | ✗ |
| 29 | pants | yes (object 30) | leggings (uncertain) | hypernym/hyponym | ✓ |
| 30 | boots | yes (object 31) | boot | identical | ✓ |
| 31 | boots | yes (object 32) | boot | identical | ✓ |
| 32 | teapot | yes (object 33) | pot | hypernym/hyponym | ✓ |
| 33 | teapot | yes (object 34) | pot | hypernym/hyponym | ✓ |
| 34 | jug | yes (object 35) | pot | semantic overlap | ✓ |
| 35 | jug | yes (object 36) | pot | semantic overlap | ✓ |
| 36 | cabinet | yes (object 37) | cabinet | identical | ✓ |
| 37 | wall | yes (object 38) | person | mismatch | ✗ |
| 38 | picture frame | yes (object 39) | picture frame | identical | ✓ |
| 39 | picture frames | yes (object 40) | picture frame | identical | ✓ |
| 40 | chair covering | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | dining chair | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | dining table | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | chair | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | switch | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | box | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | bottles | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | bottles | no: after the first 40 | - | no label from TRASER | ✗ |
| 48 | wall | no: after the first 40 | - | no label from TRASER | ✗ |
| 49 | head | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 4/30 right, triplets: 4/30 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - wearing - cloth #2 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - wearing - sneakers #3 | 0-20 | above | 0-20 | mismatch | 1.00 | ✗ | ✗ |
| person #0 - wearing - sneakers #4 | 0-20 | above | 0-20 | mismatch | 1.00 | ✗ | ✗ |
| person #0 - moving on - carpet #5 | 2-20 | on (+1 more) | 0-20 | semantic overlap | 0.90 | ✓ | ✓ |
| person #0 - dancing on - carpet #5 | 2-20 | on (+1 more) | 0-20 | hypernym/hyponym | 0.90 | ✓ | ✓ |
| person #0 - on - carpet #5 | 0-20 | on (+1 more) | 0-20 | identical | 1.00 | ✓ | ✓ |
| person #0 - in front of - dining chair #41 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - in front of - dining table #42 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - in front of - cabinet #36 | 0-20 | in front of (+1 more) | 0-20 | identical | 1.00 | ✓ | ✓ |
| sneakers #3 - on - carpet #5 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| sneakers #4 - on - carpet #5 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #6 - above - person #0 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #6 - above - dining table #42 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| picture frame #8 - mounted on - wall #48 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #10 - set in - side of a wall #15 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #10 - in - walls #18 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| camera #11 - mounted on - wall #48 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| camera #11 - on - wall #48 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #13 - in - walls #18 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| bottle #23 - standing on - carpet #5 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| boots #30 - on - carpet #5 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| boots #31 - on - carpet #5 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| cabinet #36 - against - walls #18 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| picture frame #38 - mounted on - wall #48 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| picture frame #38 - on - wall #48 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| picture frames #39 - mounted on - wall #48 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| picture frames #39 - on - wall #48 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| dining chair #41 - in front of - cabinet #36 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| dining table #42 - in front of - cabinet #36 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| switch #44 - on - wall #48 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (67): cloth #1 - on - carpet #5 [0-20]; cloth #1 - above - carpet #5 [0-20]; person #0 - in front of - door #10 [0-20]; person #0 - in front of - door #10 [0-20]; cloth #1 - in front of - door #10 [0-20]; cloth #1 - in front of - door #10 [0-20]; person #0 - in front of - door #13 [0-20]; person #0 - in front of - door #13 [0-20]; cloth #1 - in front of - door #13 [0-20]; cloth #1 - in front of - door #13 [0-20]


## sav_028748

13.71 s, 14 frames read | human: 14 objects, 25 relations | TRASER: 14 objects, 19 relations, valid JSON, 974 tokens

**Objects: 8/14 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | cushion | yes (object 2) | flower | mismatch | ✗ |
| 2 | table | yes (object 3) | table | identical | ✓ |
| 3 | wall | yes (object 4) | wall | identical | ✓ |
| 4 | wall switch | yes (object 5) | wall socket | semantic overlap | ✓ |
| 5 | phone | yes (object 6) | remote control (uncertain) | mismatch | ✗ |
| 6 | bottle | yes (object 7) | pen | mismatch | ✗ |
| 7 | floor | yes (object 8) | chair | mismatch | ✗ |
| 8 | smart band | yes (object 9) | wristband (uncertain) | synonym | ✓ |
| 9 | t-shirt | yes (object 10) | sweater | semantic overlap | ✓ |
| 10 | pants | yes (object 11) | person | mismatch | ✗ |
| 11 | head | yes (object 12) | person | mismatch | ✗ |
| 12 | hand | yes (object 13) | hand | identical | ✓ |
| 13 | hand | yes (object 14) | hand | identical | ✓ |

**Relations: 10/25 right, triplets: 6/25 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - wearing - smart band #8 | 0-6, 7-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - wearing - t-shirt #9 | 0-14 | wearing | 0-14 | identical | 1.00 | ✓ | ✓ |
| person #0 - wearing - pants #10 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - holding - cushion #1 | 0-12 | holding (+2 more) | 0-14 | identical | 0.86 | ✓ | ✗ |
| person #0 - rotating - cushion #1 | 2-3.5, 4.5-7 | holding (+2 more) | 0-14 | mismatch | 0.29 | ✗ | ✗ |
| person #0 - places down - cushion #1 | 11-13 | arranging (+2 more) | 0-14 | semantic overlap | 0.14 | ✗ | ✗ |
| person #0 - in front of - wall #3 | 0-14 | in front of | 0-14 | identical | 1.00 | ✓ | ✓ |
| cushion #1 - approaches - table #2 | 0-2, 2.5-4, 7.5-9.5, 11.5-13 | on | 0-14 | mismatch | 0.50 | ✗ | ✗ |
| cushion #1 - resting on - table #2 | 3-4.5 | on | 0-14 | hypernym/hyponym | 0.11 | ✗ | ✗ |
| cushion #1 - above - table #2 | 0-12 | on | 0-14 | semantic overlap | 0.86 | ✓ | ✗ |
| cushion #1 - on - table #2 | 3-4.5, 12-14 | on | 0-14 | identical | 0.25 | ✗ | ✗ |
| cushion #1 - in front of - bottle #6 | 1-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| cushion #1 - in front of - person #0 | 0-14 | in front of | 0-14 | identical | 1.00 | ✓ | ✗ |
| cushion #1 - in front of - wall #3 | 0-14 | in front of | 0-14 | identical | 1.00 | ✓ | ✗ |
| cushion #1 - in front of - phone #5 | 0-1, 3-6, 8-9, 12-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| table #2 - in front of - wall #3 | 0-14 | in front of | 0-14 | identical | 1.00 | ✓ | ✓ |
| wall switch #4 - attached to - wall #3 | 0-6, 7-13 | on | 0-14 | hypernym/hyponym | 0.86 | ✓ | ✓ |
| wall switch #4 - on - wall #3 | 0-14 | on | 0-14 | identical | 1.00 | ✓ | ✓ |
| phone #5 - resting on - table #2 | 0-1, 3-6, 8-9, 12-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| phone #5 - on - table #2 | 0-1, 3-6, 8-9, 12-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| bottle #6 - resting on - table #2 | 0.5-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| bottle #6 - on - table #2 | 1-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| smart band #8 - on - person #0 | 0-6, 7-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| t-shirt #9 - on - person #0 | 0-14 | on | 0-14 | identical | 1.00 | ✓ | ✓ |
| pants #10 - on - head #11 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (8): person #0 - behind - table #2 [0-14]; hand #12 - above - table #2 [0-14]; hand #13 - above - table #2 [0-14]; hand #12 - in front of - wall #3 [0-14]; hand #13 - in front of - wall #3 [0-14]; bottle #6 - on - wall #3 [0-14]; floor #7 - in front of - wall #3 [0-14]; floor #7 - below - table #2 [0-14]


## sav_030325

15.21 s, 15 frames read | human: 16 objects, 36 relations | TRASER: 16 objects, 45 relations, valid JSON, 1761 tokens

**Objects: 12/16 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | wall | yes (object 2) | wall | identical | ✓ |
| 2 | floor | yes (object 3) | tennis ball | mismatch | ✗ |
| 3 | person | yes (object 4) | person | identical | ✓ |
| 4 | tennis racket | yes (object 5) | volleyball | mismatch | ✗ |
| 5 | tennis racket | yes (object 6) | volleyball | mismatch | ✗ |
| 6 | racquet ball | yes (object 7) | ponytail (uncertain) | mismatch | ✗ |
| 7 | sportwear | yes (object 8) | jersey | hypernym/hyponym | ✓ |
| 8 | short | yes (object 9) | shorts | identical | ✓ |
| 9 | cap | yes (object 10) | baseball cap | hypernym/hyponym | ✓ |
| 10 | shoe | yes (object 11) | shoe | identical | ✓ |
| 11 | shoe | yes (object 12) | shoe | identical | ✓ |
| 12 | sport bra | yes (object 13) | tank top | semantic overlap | ✓ |
| 13 | joggers | yes (object 14) | leggings | semantic overlap | ✓ |
| 14 | shoe | yes (object 15) | shoe | identical | ✓ |
| 15 | shoe | yes (object 16) | shoe | identical | ✓ |

**Relations: 20/36 right, triplets: 18/36 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - holding - tennis racket #5 | 1-2, 3-14, 15-16 | holding (+2 more) | 0-16 | identical | 0.81 | ✓ | ✗ |
| person #0 - wearing - cap #9 | 0-2, 5-12, 14-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - wearing - shoe #10 | 0-16 | wearing | 0-16 | identical | 1.00 | ✓ | ✓ |
| person #0 - wearing - shoe #11 | 0-3, 4-16 | wearing | 0-16 | identical | 0.94 | ✓ | ✓ |
| person #0 - moves away from - person #3 | 0-3.5, 10.5-13, 14-16 | playing with (+1 more) | 0-16 | mismatch | 0.50 | ✗ | ✗ |
| person #0 - playing with - person #3 | 0-10, 12-16 | playing with (+1 more) | 0-16 | identical | 0.88 | ✓ | ✓ |
| person #0 - competes against - person #3 | 0-10, 12-16 | playing with (+1 more) | 0-16 | semantic overlap | 0.88 | ✓ | ✓ |
| person #0 - in front of - person #3 | 0-10, 12-16 | in front of (+1 more) | 0-16 | identical | 0.88 | ✓ | ✓ |
| person #0 - wearing - sportwear #7 | 0-16 | wearing | 0-16 | identical | 1.00 | ✓ | ✓ |
| person #0 - wearing - short #8 | 0-16 | wearing | 0-16 | identical | 1.00 | ✓ | ✓ |
| person #0 - in front of - wall #1 | 0-16 | in front of | 0-16 | identical | 1.00 | ✓ | ✓ |
| person #0 - on - floor #2 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| floor #2 - below - wall #1 | 0-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - holding - tennis racket #4 | 0-10, 11.5-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - wearing - sport bra #12 | 0-10, 12-16 | wearing | 0-16 | identical | 0.88 | ✓ | ✓ |
| person #3 - wearing - joggers #13 | 0-10, 12-16 | wearing | 0-16 | identical | 0.88 | ✓ | ✓ |
| person #3 - wearing - shoe #14 | 0-10, 12-16 | wearing | 0-16 | identical | 0.88 | ✓ | ✓ |
| person #3 - wearing - shoe #15 | 0-8.5, 12-16 | wearing | 0-16 | identical | 0.78 | ✓ | ✓ |
| person #3 - falls onto - floor #2 | 14.5-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - on - floor #2 | 0-10, 12-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - in front of - wall #1 | 0-10, 12-16 | in front of | 0-16 | identical | 0.88 | ✓ | ✓ |
| tennis racket #4 - in front of - wall #1 | 0-10, 11-14, 15-16 | in front of | 0-16 | identical | 0.88 | ✓ | ✗ |
| tennis racket #4 - above - floor #2 | 0-10, 11-14, 15-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| tennis racket #5 - above - floor #2 | 1-2, 3-14, 15-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| tennis racket #5 - in front of - wall #1 | 1-2, 7-10, 15-16 | in front of | 0-16 | identical | 0.31 | ✗ | ✗ |
| racquet ball #6 - approaches - person #3 | 2-4, 7-8.5, 12-13.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| racquet ball #6 - moves away from - person #0 | 1-4.5, 5.5-8, 10.5-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| racquet ball #6 - in front of - wall #1 | 1-4, 5-6, 7-8, 10-12, 15-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| racquet ball #6 - above - floor #2 | 1-4, 5-6, 7-8, 10-12, 15-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| sportwear #7 - on - person #0 | 0-16 | on | 0-16 | identical | 1.00 | ✓ | ✓ |
| short #8 - on - person #0 | 0-16 | on | 0-16 | identical | 1.00 | ✓ | ✓ |
| cap #9 - on - person #0 | 0-3, 5-7, 9-12, 14-16 | on | 0-16 | identical | 0.62 | ✓ | ✓ |
| sport bra #12 - on - person #3 | 0-10, 12-16 | on | 0-16 | identical | 0.88 | ✓ | ✓ |
| joggers #13 - on - person #3 | 0-10, 12-16 | on | 0-16 | identical | 0.88 | ✓ | ✓ |
| shoe #14 - on - floor #2 | 0-10, 12-16 | nothing for this pair | - | - | - | ✗ | ✗ |
| shoe #15 - on - floor #2 | 0-10, 12-16 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (23): tennis racket #5 - approaching - person #0 [0-16]; tennis racket #5 - moving away from - person #0 [1-15]; tennis racket #5 - overlapping - person #0 [0-16]; person #3 - looking at - tennis racket #5 [0-16]; shoe #10 - on - person #0 [0-16]; shoe #11 - on - person #0 [0-16]; shoe #14 - on - person #3 [0-16]; shoe #15 - on - person #3 [0-16]; shoe #10 - below - short #8 [0-16]; shoe #11 - below - short #8 [0-16]


## sav_031935

18.38 s, 18 frames read | human: 36 objects, 35 relations | TRASER: 36 objects, 46 relations, valid JSON, 2849 tokens

**Objects: 16/36 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | wardrope | yes (object 1) | cabinet door | hypernym/hyponym | ✓ |
| 1 | box | yes (object 2) | speaker (uncertain) | mismatch | ✗ |
| 2 | air purfier | yes (object 3) | bottle | mismatch | ✗ |
| 3 | man | yes (object 4) | person | hypernym/hyponym | ✓ |
| 4 | wall | yes (object 5) | wall | identical | ✓ |
| 5 | roof | yes (object 6) | ceiling fan | mismatch | ✗ |
| 6 | fan | yes (object 7) | ceiling fan | hypernym/hyponym | ✓ |
| 7 | wardrope | yes (object 8) | refrigerator | mismatch | ✗ |
| 8 | household material | yes (object 9) | box | mismatch | ✗ |
| 9 | household material | yes (object 10) | box | mismatch | ✗ |
| 10 | household material | yes (object 11) | bottle | mismatch | ✗ |
| 11 | household material | yes (object 12) | speaker (uncertain) | mismatch | ✗ |
| 12 | household material | yes (object 13) | box | mismatch | ✗ |
| 13 | apple | yes (object 14) | cell phone (uncertain) | mismatch | ✗ |
| 14 | cloth | yes (object 15) | box | mismatch | ✗ |
| 15 | compartment | yes (object 16) | shelf (uncertain) | semantic overlap | ✓ |
| 16 | compartment | yes (object 17) | shelf (uncertain) | semantic overlap | ✓ |
| 17 | compartment | yes (object 18) | bottle | mismatch | ✗ |
| 18 | compartment | yes (object 19) | speaker (uncertain) | mismatch | ✗ |
| 19 | compartment | yes (object 20) | shelf (uncertain) | semantic overlap | ✓ |
| 20 | glasses | yes (object 21) | person | mismatch | ✗ |
| 21 | face | yes (object 22) | person | hypernym/hyponym | ✓ |
| 22 | hair | yes (object 23) | hairline (uncertain) | semantic overlap | ✓ |
| 23 | shirt | yes (object 24) | jersey | hypernym/hyponym | ✓ |
| 24 | beard | yes (object 25) | beard | identical | ✓ |
| 25 | hands | yes (object 26) | arm | semantic overlap | ✓ |
| 26 | wristband | yes (object 27) | bracelet | synonym | ✓ |
| 27 | handle | yes (object 28) | handle (uncertain) | identical | ✓ |
| 28 | handle | yes (object 29) | handle (uncertain) | identical | ✓ |
| 29 | wood | yes (object 30) | cabinet door | mismatch | ✗ |
| 30 | wood | yes (object 31) | cabinet door | mismatch | ✗ |
| 31 | wood | yes (object 32) | cabinet door | mismatch | ✗ |
| 32 | wood | yes (object 33) | door | mismatch | ✗ |
| 33 | wood | yes (object 34) | cabinet door | mismatch | ✗ |
| 34 | handle | yes (object 35) | handle (uncertain) | identical | ✓ |
| 35 | wood | yes (object 36) | refrigerator | mismatch | ✗ |

**Relations: 7/35 right, triplets: 5/35 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| wardrope #0 - against - wall #4 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| wardrope #0 - has - handle #27 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| wardrope #0 - has - handle #28 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| box #1 - on - wardrope #7 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| air purfier #2 - on - wardrope #7 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #3 - wearing - glasses #20 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #3 - wearing - shirt #23 | 0-19 | wearing | 0-18 | identical | 0.95 | ✓ | ✓ |
| man #3 - wearing - wristband #26 | 0-5.5, 6.5-9.5 | wearing | 0-18 | identical | 0.47 | ✗ | ✗ |
| man #3 - holding - apple #13 | 10-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #3 - has - beard #24 | 0-19 | has | 0-18 | identical | 0.95 | ✓ | ✓ |
| man #3 - has - hair #22 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| man #3 - below - fan #6 | 0-19 | below | 0-18 | identical | 0.95 | ✓ | ✓ |
| man #3 - in front of - wardrope #0 | 0-19 | in front of | 0-18 | identical | 0.95 | ✓ | ✓ |
| man #3 - in front of - wardrope #7 | 0-19 | in front of | 0-18 | identical | 0.95 | ✓ | ✗ |
| man #3 - in front of - wall #4 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| fan #6 - attached to - roof #5 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| fan #6 - on - roof #5 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| wardrope #7 - against - wall #4 | 0-19 | in front of | 0-18 | semantic overlap | 0.95 | ✓ | ✗ |
| wardrope #7 - has - handle #34 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| household material #8 - in - compartment #15 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| household material #9 - in - compartment #16 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| household material #10 - in - compartment #17 | 0-19 | next to | 0-18 | mismatch | 0.95 | ✗ | ✗ |
| household material #11 - in - compartment #18 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| household material #12 - in - compartment #19 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| apple #13 - in - hands #25 | 9.5-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| apple #13 - in front of - shirt #23 | 10-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| glasses #20 - on - face #21 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| hair #22 - above - face #21 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| shirt #23 - on - man #3 | 0-19 | on | 0-18 | identical | 0.95 | ✓ | ✓ |
| beard #24 - below - face #21 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| hands #25 - in front of - shirt #23 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| wristband #26 - on - hands #25 | 0-5.5, 7-9 | on | 0-18 | identical | 0.42 | ✗ | ✗ |
| handle #27 - on - wood #29 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| handle #28 - on - wood #30 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| handle #34 - on - wood #35 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (36): man #3 - looking at - wood #32 [0-18]; man #3 - in front of - wood #32 [0-18]; man #3 - in front of - wood #35 [0-18]; man #3 - below - roof #5 [0-18]; beard #24 - on - man #3 [0-18]; hands #25 - attached to - man #3 [0-18]; glasses #20 - overlapping - man #3 [0-18]; face #21 - overlapping - man #3 [0-18]; glasses #20 - in front of - wardrope #0 [0-18]; face #21 - in front of - wardrope #0 [0-18]


## sav_032329

12.38 s, 12 frames read | human: 52 objects, 45 relations | TRASER: 38 objects, 56 relations, valid JSON, 3043 tokens

**Objects: 26/52 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | man | yes (object 1) | person | hypernym/hyponym | ✓ |
| 1 | building | yes (object 2) | stone structure (uncertain) | semantic overlap | ✓ |
| 2 | building | yes (object 3) | building | identical | ✓ |
| 3 | building | yes (object 4) | building | identical | ✓ |
| 4 | man | yes (object 5) | chair | mismatch | ✗ |
| 5 | woman | no: no mask on the frames TRASER reads | - | no label from TRASER | ✗ |
| 6 | man | yes (object 6) | person | hypernym/hyponym | ✓ |
| 7 | horse | yes (object 7) | horse | identical | ✓ |
| 8 | carriage | yes (object 8) | bench | mismatch | ✗ |
| 9 | person | yes (object 9) | person | identical | ✓ |
| 10 | people | yes (object 10) | person | hypernym/hyponym | ✓ |
| 11 | people | yes (object 11) | person | hypernym/hyponym | ✓ |
| 12 | person | yes (object 12) | person | identical | ✓ |
| 13 | person | yes (object 13) | person | identical | ✓ |
| 14 | person | yes (object 14) | person | identical | ✓ |
| 15 | person | yes (object 15) | person | identical | ✓ |
| 16 | people | yes (object 16) | person | hypernym/hyponym | ✓ |
| 17 | people | yes (object 17) | person | hypernym/hyponym | ✓ |
| 18 | road | yes (object 18) | stone slab | mismatch | ✗ |
| 19 | sidewalk | yes (object 19) | stone slab | semantic overlap | ✓ |
| 20 | door mat | yes (object 20) | bench | mismatch | ✗ |
| 21 | barrier | yes (object 21) | bench | mismatch | ✗ |
| 22 | building | yes (object 22) | window | semantic overlap | ✓ |
| 23 | building | yes (object 23) | awning | mismatch | ✗ |
| 24 | sky | yes (object 24) | building | mismatch | ✗ |
| 25 | carriage | yes (object 25) | stone wall | mismatch | ✗ |
| 26 | light | yes (object 26) | street lamp | hypernym/hyponym | ✓ |
| 27 | light | yes (object 27) | street lamp | hypernym/hyponym | ✓ |
| 28 | crowd | yes (object 28) | car | mismatch | ✗ |
| 29 | door | yes (object 29) | door | identical | ✓ |
| 30 | display case or panel | yes (object 30) | poster | semantic overlap | ✓ |
| 31 | clothes | yes (object 31) | person | mismatch | ✗ |
| 32 | pants | yes (object 32) | trousers (uncertain) | synonym | ✓ |
| 33 | clothes | yes (object 33) | shirt | hypernym/hyponym | ✓ |
| 34 | jeans | yes (object 34) | jeans (uncertain) | identical | ✓ |
| 35 | pants | yes (object 35) | bench | mismatch | ✗ |
| 36 | shirts | no: no mask on the frames TRASER reads | - | no label from TRASER | ✗ |
| 37 | pants | yes (object 36) | person | mismatch | ✗ |
| 38 | door | yes (object 37) | door | identical | ✓ |
| 39 | seat | yes (object 38) | bench | hypernym/hyponym | ✓ |
| 40 | canopy | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | curtain | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | curtain | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | clothes | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | shorts | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | t-shirt | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | shorts | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | clothes | no: after the first 40 | - | no label from TRASER | ✗ |
| 48 | clothes | no: after the first 40 | - | no label from TRASER | ✗ |
| 49 | shorts | no: after the first 40 | - | no label from TRASER | ✗ |
| 50 | window | no: after the first 40 | - | no label from TRASER | ✗ |
| 51 | t-shirt | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 8/45 right, triplets: 3/45 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| man #0 - on - sidewalk #19 | 0-4.5 | on | 0-3 | identical | 0.67 | ✓ | ✓ |
| man #0 - walking along - sidewalk #19 | 0-4 | on | 0-3 | hypernym/hyponym | 0.75 | ✓ | ✓ |
| man #6 - on - carriage #8 | 0-5 | sitting on (+1 more) | 3-7 | hypernym/hyponym | 0.29 | ✗ | ✗ |
| man #6 - driving - carriage #8 | 0-6.5 | sitting on (+1 more) | 3-7 | semantic overlap | 0.50 | ✗ | ✗ |
| man #6 - controlling - horse #7 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| horse #7 - in front of - carriage #8 | 0-5.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| horse #7 - pulling - carriage #8 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| horse #7 - attached to - carriage #8 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| horse #7 - on - road #18 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| horse #7 - approaching - man #0 | 0-4 | nothing for this pair | - | - | - | ✗ | ✗ |
| carriage #8 - behind - horse #7 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| carriage #8 - on - road #18 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| carriage #8 - under - canopy #40 | 4-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| carriage #8 - carrying - man #6 | 0-5.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| carriage #8 - carrying - man #4 | 4-6.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| carriage #8 - carrying - woman #5 | 4-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| carriage #8 - passing by - barrier #21 | 0-3.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| carriage #8 - approaching - door #29 | 1-2.5 | in front of | 3-7 | mismatch | 0.00 | ✗ | ✗ |
| person #9 - on - sidewalk #19 | 8-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #9 - walking along - sidewalk #19 | 8.5-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| people #10 - walking along - sidewalk #19 | 9-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| people #10 - on - sidewalk #19 | 9-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| sidewalk #19 - next to - road #18 | 0-4, 5-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| door mat #20 - on - sidewalk #19 | 0-9 | on | 0-7 | identical | 0.78 | ✓ | ✗ |
| door mat #20 - in front of - door #29 | 0-9 | in front of | 0-7 | identical | 0.78 | ✓ | ✗ |
| barrier #21 - on - sidewalk #19 | 0-4, 5.5-10 | on | 0-7 | identical | 0.55 | ✓ | ✗ |
| barrier #21 - in front of - door #29 | 0-10 | in front of | 0-7 | identical | 0.70 | ✓ | ✗ |
| barrier #21 - next to - door mat #20 | 0-3, 5-9 | nothing for this pair | - | - | - | ✗ | ✗ |
| barrier #21 - in front of - building #1 | 0-3, 5-9 | in front of | 0-7 | identical | 0.56 | ✓ | ✗ |
| sky #24 - above - building #1 | 0-2 | nothing for this pair | - | - | - | ✗ | ✗ |
| sky #24 - above - building #22 | 10-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| carriage #25 - on - road #18 | 9-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| carriage #25 - moving along - road #18 | 9.5-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| carriage #25 - approaching - crowd #28 | 10-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| carriage #25 - carrying - person #12 | 10-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #26 - on - building #22 | 11-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #27 - on - building #1 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #29 - in - building #1 | 0-9 | in | 0-7 | identical | 0.78 | ✓ | ✓ |
| display case or panel #30 - on - building #1 | 7.5-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| seat #39 - on - carriage #8 | 4-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| seat #39 - attached to - carriage #8 | 4-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| canopy #40 - attached to - carriage #8 | 4-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| curtain #42 - attached to - carriage #25 | 10-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| curtain #42 - attached to - carriage #25 | 10-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #50 - in - building #22 | 11-13 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (46): man #6 - wearing - clothes #33 [3-7]; man #0 - walking past - door #29 [0-3]; man #0 - in front of - door #29 [0-3]; man #0 - walking past - horse #7 [0-3]; horse #7 - on - sidewalk #19 [0-4]; horse #7 - in front of - door #29 [0-4]; door #29 - in - sky #24 [0-4]; door #29 - in - building #2 [0-4]; door #29 - in - building #3 [0-4]; light #27 - above - door #29 [0-4]


## sav_033373

9.46 s, 9 frames read | human: 34 objects, 31 relations | TRASER: 34 objects, 42 relations, valid JSON, 2638 tokens

**Objects: 23/34 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | person | yes (object 2) | person | identical | ✓ |
| 2 | person | yes (object 3) | bicycle | mismatch | ✗ |
| 3 | person | yes (object 4) | person | identical | ✓ |
| 4 | person | yes (object 5) | person | identical | ✓ |
| 5 | person | yes (object 6) | person | identical | ✓ |
| 6 | pavement | yes (object 7) | pathway | synonym | ✓ |
| 7 | road | yes (object 8) | car | mismatch | ✗ |
| 8 | car | yes (object 9) | car | identical | ✓ |
| 9 | car | yes (object 10) | car | identical | ✓ |
| 10 | sign | yes (object 11) | pole | mismatch | ✗ |
| 11 | sign | yes (object 12) | street sign | hypernym/hyponym | ✓ |
| 12 | plants | yes (object 13) | bush | hypernym/hyponym | ✓ |
| 13 | sky bridge | yes (object 14) | awning | semantic overlap | ✓ |
| 14 | fence | yes (object 15) | fence | identical | ✓ |
| 15 | cars | yes (object 16) | car | identical | ✓ |
| 16 | trees | yes (object 17) | tree | identical | ✓ |
| 17 | building | yes (object 18) | cloud | mismatch | ✗ |
| 18 | fence | yes (object 19) | pole (uncertain) | mismatch | ✗ |
| 19 | utility pole | yes (object 20) | pole | hypernym/hyponym | ✓ |
| 20 | trees | yes (object 21) | tree | identical | ✓ |
| 21 | bushes | yes (object 22) | bush | identical | ✓ |
| 22 | crowds | yes (object 23) | person | hypernym/hyponym | ✓ |
| 23 | sewer | yes (object 24) | leaf | mismatch | ✗ |
| 24 | concrete wall | yes (object 25) | pole | mismatch | ✗ |
| 25 | car | yes (object 26) | car | identical | ✓ |
| 26 | bike | yes (object 27) | bicycle | synonym | ✓ |
| 27 | bike | yes (object 28) | bicycle | synonym | ✓ |
| 28 | bag | yes (object 29) | jersey (uncertain) | mismatch | ✗ |
| 29 | box | yes (object 30) | plastic bag | semantic overlap | ✓ |
| 30 | head | yes (object 31) | signboard | mismatch | ✗ |
| 31 | plate | yes (object 32) | license plate | mismatch | ✗ |
| 32 | stone block | yes (object 33) | pole | mismatch | ✗ |
| 33 | car | yes (object 34) | license plate | semantic overlap | ✓ |

**Relations: 4/31 right, triplets: 3/31 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - in front of - sign #11 | 0-2 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - in front of - sign #10 | 6.5-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - on - pavement #6 | 0-2, 7-10 | on (+1 more) | 0-3, 7-9 | identical | 0.67 | ✓ | ✓ |
| person #0 - carrying - bag #28 | 0-2, 7-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - on - pavement #6 | 0-10 | rides along (+1 more) | 2-6 | semantic overlap | 0.40 | ✗ | ✗ |
| person #1 - rides - bike #26 | 0-8.5 | rides | 2-6 | identical | 0.47 | ✗ | ✗ |
| person #2 - on - pavement #6 | 0-10 | on | 2-6, 7-9 | identical | 0.60 | ✓ | ✗ |
| person #2 - rides - bike #27 | 0-4, 5-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #2 - follows - person #1 | 0-4, 4.5-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - on - pavement #6 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #3 - holds - box #29 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #4 - on - pavement #6 | 0-2 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #8 - on - road #7 | 5-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #8 - behind - plants #12 | 5-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #9 - on - road #7 | 6-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign #10 - in front of - trees #16 | 1-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign #10 - on - pavement #6 | 0-4.5 | on | 0-9 | identical | 0.50 | ✗ | ✗ |
| sign #11 - in front of - trees #16 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign #11 - on - pavement #6 | 0-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| plants #12 - next to - pavement #6 | 0-10 | beside | 0-9 | synonym | 0.90 | ✓ | ✓ |
| plants #12 - in front of - fence #14 | 0-10 | in front of | 0-9 | identical | 0.90 | ✓ | ✓ |
| sky bridge #13 - above - road #7 | 0-4 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #16 - above - fence #14 | 0-10 | behind | 0-9 | mismatch | 0.90 | ✗ | ✗ |
| building #17 - behind - fence #14 | 0-10 | above | 0-9 | mismatch | 0.90 | ✗ | ✗ |
| utility pole #19 - on - pavement #6 | 4-6.5, 7-10 | beside | 4-9 | mismatch | 0.75 | ✗ | ✗ |
| sewer #23 - in - pavement #6 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| car #25 - on - road #7 | 0-4 | nothing for this pair | - | - | - | ✗ | ✗ |
| bike #26 - on - pavement #6 | 0-10 | on | 2-6 | identical | 0.40 | ✗ | ✗ |
| bike #27 - on - pavement #6 | 0-4, 5-10 | on | 2-6, 7-9 | identical | 0.50 | ✗ | ✗ |
| box #29 - in front of - person #3 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| stone block #32 - on - pavement #6 | 0-3 | beside | 0-3 | mismatch | 1.00 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (27): person #1 - moves away from - person #0 [2-6]; person #1 - passes - sign #10 [3-6]; bike #26 - passes - sign #10 [3-6]; sign #10 - in front of - fence #14 [0-9]; building #17 - above - trees #16 [0-9]; sign #11 - attached to - sign #10 [0-3]; head #30 - attached to - sign #10 [0-3]; plate #31 - on - car #8 [4-9]; car #33 - on - car #8 [4-9]; car #8 - beside - pavement #6 [4-9]


## sav_036919

17.83 s, 18 frames read | human: 15 objects, 31 relations | TRASER: 15 objects, 20 relations, valid JSON, 1203 tokens

**Objects: 9/15 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | floor | yes (object 1) | pot | mismatch | ✗ |
| 1 | hand | yes (object 2) | hand | identical | ✓ |
| 2 | pot | yes (object 3) | pot | identical | ✓ |
| 3 | firewood | yes (object 4) | log | synonym | ✓ |
| 4 | zinc | yes (object 5) | pipe (uncertain) | mismatch | ✗ |
| 5 | water | yes (object 6) | lid (uncertain) | mismatch | ✗ |
| 6 | brick | yes (object 7) | log | mismatch | ✗ |
| 7 | stick | yes (object 8) | log | semantic overlap | ✓ |
| 8 | stick | yes (object 9) | log | semantic overlap | ✓ |
| 9 | stick | yes (object 10) | log | semantic overlap | ✓ |
| 10 | stick | yes (object 11) | rock | mismatch | ✗ |
| 11 | cooking stove | yes (object 12) | log | mismatch | ✗ |
| 12 | stick | yes (object 13) | log | semantic overlap | ✓ |
| 13 | handle | yes (object 14) | handle (uncertain) | identical | ✓ |
| 14 | handle | yes (object 15) | handle (uncertain) | identical | ✓ |

**Relations: 1/31 right, triplets: 1/31 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| hand #1 - moves away from - pot #2 | 2-7 | moving around (+3 more) | 0-19 | semantic overlap | 0.26 | ✗ | ✗ |
| hand #1 - moves toward - pot #2 | 4-7 | moving around (+3 more) | 0-19 | semantic overlap | 0.16 | ✗ | ✗ |
| hand #1 - above - pot #2 | 0-18 | above (+3 more) | 0-19 | identical | 0.95 | ✓ | ✓ |
| hand #1 - rinses in - water #5 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #1 - above - water #5 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #1 - touches - water #5 | 0-4, 7-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| hand #1 - drips - water #5 | 4-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| pot #2 - contains - water #5 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| pot #2 - on - firewood #3 | 0-18 | in front of | 0-19 | mismatch | 0.95 | ✗ | ✗ |
| pot #2 - above - firewood #3 | 0-18 | in front of | 0-19 | mismatch | 0.95 | ✗ | ✗ |
| pot #2 - above - cooking stove #11 | 0-18 | in front of | 0-19 | mismatch | 0.95 | ✗ | ✗ |
| pot #2 - in front of - zinc #4 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| firewood #3 - on - floor #0 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| water #5 - inside - pot #2 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| brick #6 - on - floor #0 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| brick #6 - under - pot #2 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| stick #7 - on - floor #0 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| stick #7 - under - pot #2 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| stick #8 - on - floor #0 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| stick #8 - under - pot #2 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| stick #9 - on - floor #0 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| stick #9 - under - pot #2 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| stick #10 - on - floor #0 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| stick #10 - under - pot #2 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| cooking stove #11 - on - floor #0 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| stick #12 - on - floor #0 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| stick #12 - under - pot #2 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| handle #13 - attached to - pot #2 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| handle #13 - attached to - pot #2 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| handle #14 - attached to - pot #2 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| handle #14 - attached to - pot #2 | 0-18 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (14): pot #2 - in front of - brick #6 [0-19]; pot #2 - in front of - stick #7 [0-19]; pot #2 - in front of - stick #8 [0-19]; pot #2 - in front of - stick #9 [0-19]; pot #2 - in front of - stick #12 [0-19]; pot #2 - in front of - stick #10 [0-19]; hand #1 - in front of - firewood #3 [0-19]; hand #1 - in front of - brick #6 [0-19]; hand #1 - in front of - stick #7 [0-19]; hand #1 - in front of - stick #8 [0-19]


## sav_037370

19.88 s, 20 frames read | human: 20 objects, 13 relations | TRASER: 20 objects, 48 relations, valid JSON, 2066 tokens

**Objects: 14/20 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | guitarist | yes (object 1) | person | hypernym/hyponym | ✓ |
| 1 | accordion player | yes (object 2) | person | hypernym/hyponym | ✓ |
| 2 | stage backdrop panels | yes (object 3) | curtain | semantic overlap | ✓ |
| 3 | drummer | yes (object 4) | drum set | mismatch | ✗ |
| 4 | guitarist | yes (object 5) | person | hypernym/hyponym | ✓ |
| 5 | people | yes (object 6) | person | hypernym/hyponym | ✓ |
| 6 | stage curtain | yes (object 7) | stage | semantic overlap | ✓ |
| 7 | lighting rig | yes (object 8) | spotlight | hypernym/hyponym | ✓ |
| 8 | stage floor | yes (object 9) | speaker | mismatch | ✗ |
| 9 | drum set | yes (object 10) | drum set | identical | ✓ |
| 10 | speakers | yes (object 11) | speaker | identical | ✓ |
| 11 | object | yes (object 12) | spotlight | hypernym/hyponym | ✓ |
| 12 | device | yes (object 13) | soundboard | hypernym/hyponym | ✓ |
| 13 | electric keyboard | yes (object 14) | soundboard | mismatch | ✗ |
| 14 | piano | yes (object 15) | speaker | mismatch | ✗ |
| 15 | lights | yes (object 16) | speaker | mismatch | ✗ |
| 16 | accordion | yes (object 17) | accordion | identical | ✓ |
| 17 | guitar | yes (object 18) | guitar | identical | ✓ |
| 18 | phone | yes (object 19) | cell phone | synonym | ✓ |
| 19 | rig | yes (object 20) | spotlight | mismatch | ✗ |

**Relations: 3/13 right, triplets: 3/13 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| guitarist #0 - playing - guitar #17 | 0-20 | playing (+2 more) | 0-20 | identical | 1.00 | ✓ | ✓ |
| guitarist #0 - carrying - guitar #17 | 0-20 | playing (+2 more) | 0-20 | mismatch | 1.00 | ✗ | ✗ |
| guitarist #0 - performing with - drummer #3 | 0-20 | in front of | 0-20 | mismatch | 1.00 | ✗ | ✗ |
| guitarist #0 - performing with - accordion player #1 | 0-3, 8-20 | performing with (+1 more) | 0-2, 9-20 | identical | 0.87 | ✓ | ✓ |
| guitarist #0 - performing with - guitarist #4 | 9-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| guitarist #0 - performing for - people #5 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| accordion player #1 - playing - accordion #16 | 0-3, 8-20 | playing (+2 more) | 0-2, 9-20 | identical | 0.87 | ✓ | ✓ |
| accordion player #1 - carrying - accordion #16 | 0-3, 8-20 | playing (+2 more) | 0-2, 9-20 | mismatch | 0.87 | ✗ | ✗ |
| accordion player #1 - performing with - drummer #3 | 0-3, 8-20 | in front of | 0-2, 9-20 | mismatch | 0.87 | ✗ | ✗ |
| drummer #3 - playing - drum set #9 | 0-1 | nothing for this pair | - | - | - | ✗ | ✗ |
| people #5 - holding - phone #18 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| people #5 - recording with - phone #18 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| people #5 - watching - guitarist #0 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (38): guitarist #0 - performing on - stage curtain #6 [0-20]; guitarist #0 - below - stage curtain #6 [0-20]; accordion player #1 - performing on - stage curtain #6 [0-2, 9-20]; accordion player #1 - below - stage curtain #6 [0-2, 9-20]; guitarist #0 - moving rightward relative to - stage backdrop panels #2 [0-20]; guitarist #0 - in front of - stage backdrop panels #2 [0-20]; accordion player #1 - moving leftward relative to - stage backdrop panels #2 [0-2, 9-20]; accordion player #1 - in front of - stage backdrop panels #2 [0-2, 9-20]; drummer #3 - in front of - stage backdrop panels #2 [0-20]; drum set #9 - in front of - stage backdrop panels #2 [0-20]


## sav_037495

20.54 s, 21 frames read | human: 38 objects, 34 relations | TRASER: 36 objects, 46 relations, valid JSON, 2912 tokens

**Objects: 21/38 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | cloth | yes (object 1) | sweater | mismatch | ✗ |
| 1 | wall | yes (object 2) | wallpaper | semantic overlap | ✓ |
| 2 | wall design | yes (object 3) | painting (uncertain) | semantic overlap | ✓ |
| 3 | mat | yes (object 4) | doormat | hypernym/hyponym | ✓ |
| 4 | table | no: no mask on the frames TRASER reads | - | no label from TRASER | ✗ |
| 5 | tv console | yes (object 5) | cabinet | synonym | ✓ |
| 6 | tv set | yes (object 6) | television stand | semantic overlap | ✓ |
| 7 | drawer | yes (object 7) | refrigerator | mismatch | ✗ |
| 8 | drawer | yes (object 8) | baseboard (uncertain) | mismatch | ✗ |
| 9 | wooden object | yes (object 9) | cabinet | hypernym/hyponym | ✓ |
| 10 | wall | yes (object 10) | wallpaper | semantic overlap | ✓ |
| 11 | wall | yes (object 11) | painting (uncertain) | mismatch | ✗ |
| 12 | trouser | yes (object 12) | jeans (uncertain) | hypernym/hyponym | ✓ |
| 13 | hair | yes (object 13) | hair | identical | ✓ |
| 14 | person | yes (object 14) | person | identical | ✓ |
| 15 | sweatpants | yes (object 15) | trousers | hypernym/hyponym | ✓ |
| 16 | floor | yes (object 16) | floor | identical | ✓ |
| 17 | door | yes (object 17) | door | identical | ✓ |
| 18 | pantry | yes (object 18) | cabinet | semantic overlap | ✓ |
| 19 | ceiling | yes (object 19) | ceiling fan | semantic overlap | ✓ |
| 20 | clothes | yes (object 20) | curtain | mismatch | ✗ |
| 21 | door | yes (object 21) | cabinet | mismatch | ✗ |
| 22 | mat | yes (object 22) | baseboard (uncertain) | mismatch | ✗ |
| 23 | cabinet | yes (object 23) | refrigerator | mismatch | ✗ |
| 24 | wall | yes (object 24) | cabinet | mismatch | ✗ |
| 25 | tv | yes (object 25) | television | identical | ✓ |
| 26 | tv accessories | yes (object 26) | power strip | semantic overlap | ✓ |
| 27 | wall | yes (object 27) | cabinet | mismatch | ✗ |
| 28 | wall | yes (object 28) | painting (uncertain) | mismatch | ✗ |
| 29 | wall | yes (object 29) | door frame (uncertain) | mismatch | ✗ |
| 30 | table | no: no mask on the frames TRASER reads | - | no label from TRASER | ✗ |
| 31 | clothing | yes (object 30) | curtain | mismatch | ✗ |
| 32 | clothing | yes (object 31) | curtain | mismatch | ✗ |
| 33 | door | yes (object 32) | cabinet | mismatch | ✗ |
| 34 | door handle | yes (object 33) | door handle | identical | ✓ |
| 35 | glass | yes (object 34) | mirror | semantic overlap | ✓ |
| 36 | glass | yes (object 35) | mirror | semantic overlap | ✓ |
| 37 | glass | yes (object 36) | mirror | semantic overlap | ✓ |

**Relations: 11/34 right, triplets: 10/34 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| cloth #0 - moves away from - tv set #6 | 0-4, 8-11, 14-16, 18-20 | in front of | 0-22 | mismatch | 0.50 | ✗ | ✗ |
| cloth #0 - approaches - tv set #6 | 4-8 | in front of | 0-22 | mismatch | 0.18 | ✗ | ✗ |
| cloth #0 - moves away from - tv set #6 | 0-4, 8-11 | in front of | 0-22 | mismatch | 0.32 | ✗ | ✗ |
| cloth #0 - moves away from - door #17 | 0-5, 8-12.5, 14.5-17.5, 18-21 | moves away from (+2 more) | 17-19 | identical | 0.09 | ✗ | ✗ |
| cloth #0 - above - trouser #12 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| cloth #0 - in front of - wall #1 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| mat #3 - on - floor #16 | 0-4, 5-17, 18-21 | on | 0-22 | identical | 0.86 | ✓ | ✓ |
| mat #3 - in front of - door #17 | 0-4, 5-17, 18-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| tv console #5 - on - floor #16 | 0-21 | on | 0-22 | identical | 0.95 | ✓ | ✓ |
| tv console #5 - in front of - wall #1 | 0-21 | in front of | 0-22 | identical | 0.95 | ✓ | ✓ |
| tv set #6 - on - tv console #5 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| tv set #6 - in front of - wall #1 | 0-21 | in front of | 0-22 | identical | 0.95 | ✓ | ✓ |
| trouser #12 - moves away from - tv set #6 | 0-4, 8-11, 14-16, 18-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| trouser #12 - approaches - tv set #6 | 6-9 | nothing for this pair | - | - | - | ✗ | ✗ |
| trouser #12 - moves away from - tv set #6 | 0-4, 8-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| trouser #12 - moves away from - door #17 | 19-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| trouser #12 - in front of - wall #1 | 0-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| hair #13 - above - cloth #0 | 0-21 | above | 0-22 | identical | 0.95 | ✓ | ✗ |
| person #14 - moves away from - door #17 | 0-6 | approaches (+1 more) | 3-5 | mismatch | 0.33 | ✗ | ✗ |
| person #14 - in front of - door #17 | 0-5 | in front of (+1 more) | 3-5 | identical | 0.40 | ✗ | ✗ |
| person #14 - passes in front of - tv set #6 | 4-6 | in front of | 3-5 | hypernym/hyponym | 0.33 | ✗ | ✗ |
| door #17 - in - wall #1 | 0-4, 5-17, 17.5-21 | in front of | 0-22 | mismatch | 0.89 | ✗ | ✗ |
| pantry #18 - on - floor #16 | 1-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| pantry #18 - in front of - wall #10 | 0-21 | in front of | 0-22 | identical | 0.95 | ✓ | ✓ |
| mat #22 - on - floor #16 | 0-4, 5-17, 18-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| mat #22 - in front of - door #17 | 0-4, 5-17, 18-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| tv #25 - in - tv set #6 | 0-21 | on | 0-22 | semantic overlap | 0.95 | ✓ | ✓ |
| tv #25 - in front of - wall #1 | 0-21 | in front of | 0-22 | identical | 0.95 | ✓ | ✓ |
| tv accessories #26 - on - tv console #5 | 3-15.5, 16-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| tv accessories #26 - in front of - tv set #6 | 3-19, 20-21 | nothing for this pair | - | - | - | ✗ | ✗ |
| door handle #34 - on - door #17 | 0-2, 5-15.5, 16-17, 17.5-21 | on | 0-22 | identical | 0.77 | ✓ | ✓ |
| glass #35 - in - pantry #18 | 5-6, 16-19 | inside | 17-22 | synonym | 0.29 | ✗ | ✗ |
| glass #36 - in - pantry #18 | 2-4, 5-12, 16-21 | inside | 0-22 | synonym | 0.64 | ✓ | ✓ |
| glass #37 - in - pantry #18 | 1-4, 6-12, 13-15, 16-21 | inside | 0-22 | synonym | 0.73 | ✓ | ✓ |

TRASER relations between pairs the humans did not annotate (26): cloth #0 - approaches - tv #25 [0-4]; cloth #0 - moves away from - tv #25 [14-17]; cloth #0 - in front of - tv #25 [0-22]; person #14 - wears - sweatpants #15 [3-5]; person #14 - moves away from - tv #25 [3-5]; person #14 - in front of - tv #25 [3-5]; cloth #0 - in front of - tv console #5 [0-22]; cloth #0 - above - floor #16 [0-22]; hair #13 - in front of - tv #25 [0-22]; hair #13 - in front of - tv set #6 [0-22]


## sav_042890

16.38 s, 16 frames read | human: 32 objects, 25 relations | TRASER: 32 objects, 81 relations, valid JSON, 3150 tokens

**Objects: 25/32 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | t-shirt | yes (object 1) | person | mismatch | ✗ |
| 1 | shorts | yes (object 2) | person | mismatch | ✗ |
| 2 | t-shirt | yes (object 3) | television | mismatch | ✗ |
| 3 | jeans | yes (object 4) | stool | mismatch | ✗ |
| 4 | dresser | yes (object 5) | cabinet | hypernym/hyponym | ✓ |
| 5 | wall | yes (object 6) | wall panel | hypernym/hyponym | ✓ |
| 6 | ceiling | yes (object 7) | ceiling | identical | ✓ |
| 7 | wall | yes (object 8) | wall | identical | ✓ |
| 8 | object | yes (object 9) | marble floor | hypernym/hyponym | ✓ |
| 9 | plant | yes (object 10) | potted plant | hypernym/hyponym | ✓ |
| 10 | object | yes (object 11) | blanket | hypernym/hyponym | ✓ |
| 11 | woman | yes (object 12) | person | hypernym/hyponym | ✓ |
| 12 | dresser | yes (object 13) | cabinet | hypernym/hyponym | ✓ |
| 13 | coffee table | yes (object 14) | stool | mismatch | ✗ |
| 14 | television | yes (object 15) | television | identical | ✓ |
| 15 | photo | yes (object 16) | person | mismatch | ✗ |
| 16 | plant | yes (object 17) | potted plant | hypernym/hyponym | ✓ |
| 17 | wall | yes (object 18) | wall | identical | ✓ |
| 18 | ceiling | yes (object 19) | ceiling | identical | ✓ |
| 19 | flooring | yes (object 20) | marble floor | hypernym/hyponym | ✓ |
| 20 | table | yes (object 21) | blanket | mismatch | ✗ |
| 21 | remote control | yes (object 22) | remote control (uncertain) | identical | ✓ |
| 22 | wall | yes (object 23) | wall | identical | ✓ |
| 23 | wall | yes (object 24) | wall | identical | ✓ |
| 24 | t-shirt | yes (object 25) | jersey | semantic overlap | ✓ |
| 25 | pants | yes (object 26) | jeans (uncertain) | hypernym/hyponym | ✓ |
| 26 | shoe | yes (object 27) | athletic shoe | hypernym/hyponym | ✓ |
| 27 | shoe | yes (object 28) | shoe | identical | ✓ |
| 28 | hat | yes (object 29) | baseball cap | hypernym/hyponym | ✓ |
| 29 | arm | yes (object 30) | arm | identical | ✓ |
| 30 | hair | yes (object 31) | hair | identical | ✓ |
| 31 | arm | yes (object 32) | hand | semantic overlap | ✓ |

**Relations: 3/25 right, triplets: 3/25 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| woman #11 - wearing - hat #28 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #11 - wearing - t-shirt #24 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #11 - wearing - pants #25 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #11 - wearing - shoe #26 | 0-4 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #11 - wearing - shoe #27 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #11 - moves away from - dresser #12 | 1.5-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #11 - in front of - dresser #12 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #11 - moves away from - coffee table #13 | 2-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #11 - in front of - coffee table #13 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #11 - dancing on - flooring #19 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #11 - on - flooring #19 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #11 - in front of - wall #17 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| dresser #12 - holding - remote control #21 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| dresser #12 - on - flooring #19 | 0-17 | above | 0-16 | semantic overlap | 0.94 | ✓ | ✓ |
| dresser #12 - in front of - wall #23 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| coffee table #13 - on - flooring #19 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| coffee table #13 - in front of - wall #17 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| television #14 - mounted on - wall #23 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| television #14 - on - wall #23 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |
| television #14 - above - dresser #12 | 0-17 | above | 0-16 | identical | 0.94 | ✓ | ✓ |
| photo #15 - on - wall #17 | 0-4, 6-7, 9-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| plant #16 - on - flooring #19 | 0-13.5 | above | 0-16 | semantic overlap | 0.84 | ✓ | ✓ |
| plant #16 - in front of - wall #23 | 0-13.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| plant #16 - next to - dresser #12 | 0-13.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| remote control #21 - on - dresser #12 | 0-17 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (78): t-shirt #0 - wearing - t-shirt #24 [0-16]; t-shirt #0 - wearing - hat #28 [0-16]; t-shirt #0 - wearing - shoe #26 [0-4]; t-shirt #0 - wearing - shoe #27 [0-4]; t-shirt #0 - has - hair #30 [0-16]; t-shirt #0 - has - arm #31 [0-16]; t-shirt #0 - sitting on - jeans #3 [0-16]; t-shirt #0 - moving relative to - jeans #3 [0-16]; t-shirt #0 - on - jeans #3 [0-16]; t-shirt #0 - sitting on - coffee table #13 [0-16]


## sav_043183

9.92 s, 10 frames read | human: 16 objects, 33 relations | TRASER: 16 objects, 32 relations, valid JSON, 1401 tokens

**Objects: 6/16 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | person | yes (object 2) | person | identical | ✓ |
| 2 | swing frame | yes (object 3) | swing set | semantic overlap | ✓ |
| 3 | ground | yes (object 4) | swing | mismatch | ✗ |
| 4 | tree | yes (object 5) | tree | identical | ✓ |
| 5 | facilities | yes (object 6) | swing set | hypernym/hyponym | ✓ |
| 6 | sky | yes (object 7) | cloud | semantic overlap | ✓ |
| 7 | head | yes (object 8) | person | mismatch | ✗ |
| 8 | head | yes (object 9) | person | mismatch | ✗ |
| 9 | chain | yes (object 10) | swing | mismatch | ✗ |
| 10 | board | yes (object 11) | swing | mismatch | ✗ |
| 11 | leg | yes (object 12) | pole (uncertain) | mismatch | ✗ |
| 12 | feet | yes (object 13) | sandal | mismatch | ✗ |
| 13 | body | yes (object 14) | shirt | mismatch | ✗ |
| 14 | body | yes (object 15) | shirt | mismatch | ✗ |
| 15 | leg | yes (object 16) | jeans (uncertain) | mismatch | ✗ |

**Relations: 11/33 right, triplets: 10/33 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - under - sky #6 | 0-10 | below (+1 more) | 0-11 | synonym | 0.91 | ✓ | ✓ |
| person #0 - in front of - facilities #5 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - sits on - board #10 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - on - board #10 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - moves back and forth relative to - ground #3 | 0-10 | on | 0-11 | mismatch | 0.91 | ✗ | ✗ |
| person #0 - above - ground #3 | 0-10 | on | 0-11 | semantic overlap | 0.91 | ✓ | ✗ |
| person #0 - swings on - swing frame #2 | 0-10 | swinging on (+1 more) | 0-11 | identical | 0.91 | ✓ | ✓ |
| person #0 - inside - swing frame #2 | 0-10 | holding (+1 more) | 0-11 | mismatch | 0.91 | ✗ | ✗ |
| person #0 - holds - chain #9 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - in front of - person #1 | 0-10 | in front of (+1 more) | 0-11 | identical | 0.91 | ✓ | ✓ |
| person #0 - in front of - tree #4 | 0-10 | in front of | 0-11 | identical | 0.91 | ✓ | ✓ |
| person #1 - under - sky #6 | 0-10 | below (+1 more) | 0-11 | synonym | 0.91 | ✓ | ✓ |
| person #1 - in front of - facilities #5 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - holds - chain #9 | 0-10 | on | 0-11 | mismatch | 0.91 | ✗ | ✗ |
| person #1 - stands on - board #10 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - on - board #10 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - moves back and forth relative to - ground #3 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - above - ground #3 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - swings on - swing frame #2 | 0-10 | swinging on (+1 more) | 0-11 | identical | 0.91 | ✓ | ✓ |
| person #1 - inside - swing frame #2 | 0-10 | holding (+1 more) | 0-11 | mismatch | 0.91 | ✗ | ✗ |
| person #1 - in front of - tree #4 | 0-10 | in front of | 0-11 | identical | 0.91 | ✓ | ✓ |
| swing frame #2 - under - sky #6 | 0-10 | below (+1 more) | 0-11 | synonym | 0.91 | ✓ | ✓ |
| swing frame #2 - on - ground #3 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| swing frame #2 - in front of - tree #4 | 0-10 | in front of | 0-11 | identical | 0.91 | ✓ | ✓ |
| tree #4 - under - sky #6 | 0-10 | below | 0-11 | synonym | 0.91 | ✓ | ✓ |
| chain #9 - attached to - swing frame #2 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| chain #9 - attached to - swing frame #2 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| board #10 - attached to - chain #9 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| board #10 - attached to - chain #9 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| board #10 - moves back and forth relative to - swing frame #2 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| board #10 - moves back and forth relative to - ground #3 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| board #10 - below - person #0 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| board #10 - below - person #1 | 0-10 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (14): person #0 - wearing - body #13 [0-11]; person #1 - wearing - body #14 [0-11]; ground #3 - in front of - tree #4 [0-11]; ground #3 - in front of - sky #6 [0-11]; ground #3 - below - sky #6 [0-11]; chain #9 - in front of - tree #4 [0-11]; chain #9 - in front of - sky #6 [0-11]; board #10 - in front of - tree #4 [0-11]; board #10 - in front of - sky #6 [0-11]; facilities #5 - in front of - tree #4 [0-11]


## sav_048782

21.38 s, 21 frames read | human: 35 objects, 44 relations | TRASER: 35 objects, 302 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 30/35 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | person | yes (object 2) | person | identical | ✓ |
| 2 | bag | yes (object 3) | plastic bag (uncertain) | hypernym/hyponym | ✓ |
| 3 | person | yes (object 4) | person | identical | ✓ |
| 4 | person | yes (object 5) | signboard | mismatch | ✗ |
| 5 | shopfront | yes (object 6) | storefront | identical | ✓ |
| 6 | shopfront | yes (object 7) | storefront | identical | ✓ |
| 7 | shopfront | yes (object 8) | structure (uncertain) | hypernym/hyponym | ✓ |
| 8 | ground | yes (object 9) | walkway | semantic overlap | ✓ |
| 9 | ceiling | yes (object 10) | ceiling structure | hypernym/hyponym | ✓ |
| 10 | shopfront | yes (object 11) | poster | mismatch | ✗ |
| 11 | plant | yes (object 12) | potted plant | hypernym/hyponym | ✓ |
| 12 | person | yes (object 13) | jacket | mismatch | ✗ |
| 13 | bag | yes (object 14) | backpack | hypernym/hyponym | ✓ |
| 14 | bag | yes (object 15) | coat | mismatch | ✗ |
| 15 | window | yes (object 16) | door | semantic overlap | ✓ |
| 16 | window | yes (object 17) | curtain | semantic overlap | ✓ |
| 17 | window | yes (object 18) | door | semantic overlap | ✓ |
| 18 | door | yes (object 19) | wall panel | semantic overlap | ✓ |
| 19 | glass display counter | yes (object 20) | display case | synonym | ✓ |
| 20 | poster | yes (object 21) | poster | identical | ✓ |
| 21 | sign | yes (object 22) | signboard | synonym | ✓ |
| 22 | lamp | yes (object 23) | streetlight (uncertain) | hypernym/hyponym | ✓ |
| 23 | lamp | yes (object 24) | streetlight (uncertain) | hypernym/hyponym | ✓ |
| 24 | lamp | yes (object 25) | streetlight (uncertain) | hypernym/hyponym | ✓ |
| 25 | lamp | yes (object 26) | streetlight (uncertain) | hypernym/hyponym | ✓ |
| 26 | lamp | yes (object 27) | streetlight (uncertain) | hypernym/hyponym | ✓ |
| 27 | stool | yes (object 28) | bench | semantic overlap | ✓ |
| 28 | dragon decorative silhouette | yes (object 29) | dragon | hypernym/hyponym | ✓ |
| 29 | dragon decorative silhouette | yes (object 30) | dragon | hypernym/hyponym | ✓ |
| 30 | dragon decorative silhouette | yes (object 31) | dragon | hypernym/hyponym | ✓ |
| 31 | bowl | yes (object 32) | bowl | identical | ✓ |
| 32 | sign | yes (object 33) | signboard | synonym | ✓ |
| 33 | sign | yes (object 34) | archway | mismatch | ✗ |
| 34 | wall | yes (object 35) | wall panel | hypernym/hyponym | ✓ |

**Relations: 7/44 right, triplets: 7/44 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - walking with - bag #2 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #0 - walking with - person #1 | 0-22 | walking with (+1 more) | 0-21 | identical | 0.95 | ✓ | ✓ |
| person #0 - walking through - shopfront #6 | 0-22 | in front of | 0-21 | mismatch | 0.95 | ✗ | ✗ |
| person #0 - carrying - bag #13 | 0-22 | wearing | 0-21 | semantic overlap | 0.95 | ✓ | ✓ |
| person #0 - walking along - ground #8 | 0-22 | on | 0-21 | hypernym/hyponym | 0.95 | ✓ | ✓ |
| person #0 - moving away from - plant #11 | 3.5-22 | approaching (+1 more) | 0-21 | mismatch | 0.80 | ✗ | ✗ |
| person #1 - moving away from - plant #11 | 0-22 | approaching (+1 more) | 0-21 | mismatch | 0.95 | ✗ | ✗ |
| person #1 - walking with - bag #2 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - walking through - shopfront #6 | 0-22 | in front of | 0-21 | mismatch | 0.95 | ✗ | ✗ |
| person #1 - carrying - bag #14 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| person #1 - walking along - ground #8 | 0-22 | on | 0-21 | hypernym/hyponym | 0.95 | ✓ | ✓ |
| bag #2 - moving away from - plant #11 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| bag #2 - walking along - ground #8 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| shopfront #5 - opposite - shopfront #6 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| ground #8 - below - ceiling #9 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| plant #11 - on - ground #8 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| plant #11 - in front of - window #15 | 0-22 | in front of (+3 more) | 0-21 | identical | 0.95 | ✓ | ✓ |
| plant #11 - in front of - window #16 | 0-22 | in front of (+2 more) | 0-21 | identical | 0.95 | ✓ | ✓ |
| plant #11 - in front of - window #17 | 0-22 | in front of (+3 more) | 0-21 | identical | 0.95 | ✓ | ✓ |
| window #15 - on - shopfront #6 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #16 - on - shopfront #6 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| window #17 - on - shopfront #6 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #18 - in - shopfront #6 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| glass display counter #19 - in front of - shopfront #5 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| glass display counter #19 - on - ground #8 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| poster #20 - on - wall #34 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign #21 - below - dragon decorative silhouette #29 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign #21 - on - shopfront #6 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| lamp #22 - below - ceiling #9 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| lamp #23 - below - ceiling #9 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| lamp #24 - below - ceiling #9 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| lamp #25 - below - ceiling #9 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| lamp #26 - below - ceiling #9 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| stool #27 - on - ground #8 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| stool #27 - in front of - shopfront #7 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| dragon decorative silhouette #28 - below - ceiling #9 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| dragon decorative silhouette #28 - on - shopfront #6 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| dragon decorative silhouette #29 - below - ceiling #9 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| dragon decorative silhouette #29 - on - shopfront #6 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| dragon decorative silhouette #30 - below - ceiling #9 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| dragon decorative silhouette #30 - on - shopfront #6 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| bowl #31 - inside - glass display counter #19 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign #32 - on - shopfront #6 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign #33 - on - shopfront #6 | 0-22 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (280): person #0 - approaching - window #15 [0-21]; person #0 - in front of - window #15 [0-21]; person #1 - approaching - window #15 [0-21]; person #1 - in front of - window #15 [0-21]; person #0 - moving away from - shopfront #5 [0-21]; person #1 - moving away from - shopfront #5 [0-21]; person #0 - approaching - window #17 [0-21]; person #0 - in front of - window #17 [0-21]; person #1 - approaching - window #17 [0-21]; person #1 - in front of - window #17 [0-21]


## sav_052661

18.75 s, 19 frames read | human: 51 objects, 45 relations | TRASER: 40 objects, 303 relations, cut-off answer (salvaged), 8192 tokens

**Objects: 26/51 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | woman | yes (object 1) | person | hypernym/hyponym | ✓ |
| 1 | woman | yes (object 2) | person | hypernym/hyponym | ✓ |
| 2 | light | yes (object 3) | lamp | hypernym/hyponym | ✓ |
| 3 | light | yes (object 4) | lamp | hypernym/hyponym | ✓ |
| 4 | refrigerator | yes (object 5) | refrigerator | identical | ✓ |
| 5 | floor | yes (object 6) | floorboard (uncertain) | hypernym/hyponym | ✓ |
| 6 | ceiling | yes (object 7) | ceiling lamp | semantic overlap | ✓ |
| 7 | door frame | yes (object 8) | mirror | mismatch | ✗ |
| 8 | machine | yes (object 9) | cell phone (uncertain) | hypernym/hyponym | ✓ |
| 9 | table | yes (object 10) | table | identical | ✓ |
| 10 | bar stool | yes (object 11) | chair | hypernym/hyponym | ✓ |
| 11 | door | yes (object 12) | cabinet door | hypernym/hyponym | ✓ |
| 12 | wall | yes (object 13) | wall | identical | ✓ |
| 13 | cabinet | yes (object 14) | cabinet | identical | ✓ |
| 14 | loft or mezzanine | yes (object 15) | cabinet | mismatch | ✗ |
| 15 | wall | yes (object 16) | cabinet | mismatch | ✗ |
| 16 | fruit basket | yes (object 17) | fruit (uncertain) | semantic overlap | ✓ |
| 17 | cabinet | yes (object 18) | cabinet | identical | ✓ |
| 18 | people | yes (object 19) | cell phone (uncertain) | mismatch | ✗ |
| 19 | wall | yes (object 20) | cabinet | mismatch | ✗ |
| 20 | wall | yes (object 21) | cabinet | mismatch | ✗ |
| 21 | countertop | yes (object 22) | cabinet | semantic overlap | ✓ |
| 22 | wall | yes (object 23) | cabinet | mismatch | ✗ |
| 23 | photo wall | yes (object 24) | window blind | mismatch | ✗ |
| 24 | sweatshirt | yes (object 25) | sweater | synonym | ✓ |
| 25 | pants | yes (object 26) | trousers | synonym | ✓ |
| 26 | t-shirt | yes (object 27) | jersey (uncertain) | semantic overlap | ✓ |
| 27 | short | yes (object 28) | shorts | identical | ✓ |
| 28 | fruits | yes (object 29) | fruit (uncertain) | identical | ✓ |
| 29 | fruits | yes (object 30) | fruit (uncertain) | identical | ✓ |
| 30 | railing | yes (object 31) | window blind | mismatch | ✗ |
| 31 | bag | yes (object 32) | cell phone (uncertain) | mismatch | ✗ |
| 32 | socket | yes (object 33) | light switch (uncertain) | semantic overlap | ✓ |
| 33 | supporting beam or soffit | yes (object 34) | cabinet | mismatch | ✗ |
| 34 | light | yes (object 35) | vent (uncertain) | mismatch | ✗ |
| 35 | light | yes (object 36) | vent (uncertain) | mismatch | ✗ |
| 36 | wall | yes (object 37) | wall panel | hypernym/hyponym | ✓ |
| 37 | ceiling | yes (object 38) | ceiling tile (uncertain) | semantic overlap | ✓ |
| 38 | wall | yes (object 39) | ceiling | mismatch | ✗ |
| 39 | wall | yes (object 40) | wall | identical | ✓ |
| 40 | photo | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | photo | no: after the first 40 | - | no label from TRASER | ✗ |
| 42 | photo | no: after the first 40 | - | no label from TRASER | ✗ |
| 43 | photo | no: after the first 40 | - | no label from TRASER | ✗ |
| 44 | photo | no: after the first 40 | - | no label from TRASER | ✗ |
| 45 | photo | no: after the first 40 | - | no label from TRASER | ✗ |
| 46 | photo | no: after the first 40 | - | no label from TRASER | ✗ |
| 47 | photo | no: after the first 40 | - | no label from TRASER | ✗ |
| 48 | photo | no: after the first 40 | - | no label from TRASER | ✗ |
| 49 | photo | no: after the first 40 | - | no label from TRASER | ✗ |
| 50 | photo | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 8/45 right, triplets: 8/45 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| woman #0 - on - floor #5 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #0 - under - ceiling #6 | 0-19 | below | 0-20 | synonym | 0.95 | ✓ | ✓ |
| woman #0 - in front of - refrigerator #4 | 0-5, 11-14.5 | in front of | 0-20 | identical | 0.42 | ✗ | ✗ |
| woman #0 - in front of - cabinet #13 | 4.5-12, 14-19 | in front of (+11 more) | 0-20 | identical | 0.62 | ✓ | ✓ |
| woman #0 - in front of - countertop #21 | 4.5-12.5, 13.5-19 | in front of (+11 more) | 0-20 | identical | 0.68 | ✓ | ✓ |
| woman #0 - in front of - table #9 | 0-5, 12-15 | in front of (+10 more) | 0-20 | identical | 0.40 | ✗ | ✗ |
| woman #0 - dances with - woman #1 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #0 - moves in front of - woman #1 | 13-15.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #0 - performs dance with - woman #1 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #0 - wears - sweatshirt #24 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #0 - wears - pants #25 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #0 - in front of - bar stool #10 | 0-5, 12-15 | in front of (+10 more) | 0-20 | identical | 0.40 | ✗ | ✗ |
| woman #1 - on - floor #5 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #1 - under - ceiling #6 | 0-19 | below | 0-20 | synonym | 0.95 | ✓ | ✓ |
| woman #1 - in front of - refrigerator #4 | 4-11, 13-19 | in front of | 0-20 | identical | 0.65 | ✓ | ✓ |
| woman #1 - in front of - countertop #21 | 0-5, 10-14 | in front of (+11 more) | 0-20 | identical | 0.45 | ✗ | ✗ |
| woman #1 - in front of - table #9 | 4.5-12, 14-19 | in front of (+10 more) | 0-20 | identical | 0.62 | ✓ | ✓ |
| woman #1 - touches - woman #0 | 3-5.5 | approaching (+2 more) | 0-4 | mismatch | 0.18 | ✗ | ✗ |
| woman #1 - approaches - woman #0 | 2.5-4 | approaching (+2 more) | 0-4 | identical | 0.38 | ✗ | ✗ |
| woman #1 - moves away from - woman #0 | 4-6 | dancing with (+2 more) | 3-20 | mismatch | 0.12 | ✗ | ✗ |
| woman #1 - moves left of - woman #0 | 4.5-12 | dancing with (+2 more) | 3-20 | mismatch | 0.44 | ✗ | ✗ |
| woman #1 - moves right of - woman #0 | 10.5-14 | dancing with (+2 more) | 3-20 | mismatch | 0.21 | ✗ | ✗ |
| woman #1 - wears - t-shirt #26 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| woman #1 - wears - short #27 | 0-19 | wearing | 0-20 | identical | 0.95 | ✓ | ✓ |
| woman #1 - in front of - cabinet #13 | 0-5, 10-14 | in front of (+11 more) | 0-20 | identical | 0.45 | ✗ | ✗ |
| woman #1 - in front of - bar stool #10 | 4-11, 14-19 | in front of (+10 more) | 0-20 | identical | 0.60 | ✓ | ✓ |
| light #2 - under - ceiling #6 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #2 - above - table #9 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #3 - under - ceiling #6 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| light #3 - above - table #9 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| refrigerator #4 - on - floor #5 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| refrigerator #4 - beside - cabinet #13 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| table #9 - on - floor #5 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| bar stool #10 - on - floor #5 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| bar stool #10 - under - table #9 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| loft or mezzanine #14 - under - ceiling #6 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| fruit basket #16 - on - countertop #21 | 0-8, 9-10, 11-15, 18-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| people #18 - carries - bag #31 | 16-18 | nothing for this pair | - | - | - | ✗ | ✗ |
| sweatshirt #24 - on - woman #0 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| pants #25 - on - woman #0 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| t-shirt #26 - on - woman #1 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| short #27 - on - woman #1 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| fruits #28 - in - fruit basket #16 | 0-8, 9-10, 11-13, 14-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| fruits #29 - in - fruit basket #16 | 0-7, 11-15 | nothing for this pair | - | - | - | ✗ | ✗ |
| railing #30 - in front of - photo wall #23 | 0-19 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (203): woman #1 - wearing - sweatshirt #24 [0-20]; woman #1 - wearing - pants #25 [0-20]; woman #1 - in front of - door frame #7 [0-20]; woman #1 - in front of - door frame #7 [0-20]; woman #1 - in front of - door frame #7 [0-20]; woman #1 - in front of - door frame #7 [0-20]; woman #1 - in front of - door frame #7 [0-20]; woman #1 - in front of - door frame #7 [0-20]; woman #1 - in front of - door frame #7 [0-20]; woman #1 - in front of - door frame #7 [0-20]


## sav_053005

18.71 s, 19 frames read | human: 29 objects, 29 relations | TRASER: 29 objects, 37 relations, valid JSON, 2275 tokens

**Objects: 17/29 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | person | yes (object 1) | person | identical | ✓ |
| 1 | carpet | yes (object 2) | rug | synonym | ✓ |
| 2 | sofa | yes (object 3) | cushion | semantic overlap | ✓ |
| 3 | table | yes (object 4) | ottoman | semantic overlap | ✓ |
| 4 | curtain | yes (object 5) | curtain | identical | ✓ |
| 5 | windows | yes (object 6) | window | identical | ✓ |
| 6 | lights | yes (object 7) | curtain | mismatch | ✗ |
| 7 | chair | yes (object 8) | sofa | semantic overlap | ✓ |
| 8 | wall panel | yes (object 9) | baseboard (uncertain) | semantic overlap | ✓ |
| 9 | floor | yes (object 10) | rug | semantic overlap | ✓ |
| 10 | pillars | yes (object 11) | wall panel | mismatch | ✗ |
| 11 | fountain | yes (object 12) | runner carpet | mismatch | ✗ |
| 12 | desk | yes (object 13) | television set | mismatch | ✗ |
| 13 | sofa | yes (object 14) | chair leg (uncertain) | mismatch | ✗ |
| 14 | lights | yes (object 15) | signboard | mismatch | ✗ |
| 15 | background | yes (object 16) | pillar | mismatch | ✗ |
| 16 | screen | yes (object 17) | television | semantic overlap | ✓ |
| 17 | chandelier lights | yes (object 18) | hand | mismatch | ✗ |
| 18 | door | yes (object 19) | door | identical | ✓ |
| 19 | oerson | yes (object 20) | person | identical | ✓ |
| 20 | pillar | yes (object 21) | pillar | identical | ✓ |
| 21 | reflected lights | yes (object 22) | curtain | mismatch | ✗ |
| 22 | bag | yes (object 23) | handbag | hypernym/hyponym | ✓ |
| 23 | head | yes (object 24) | hair | semantic overlap | ✓ |
| 24 | legs | yes (object 25) | legs | identical | ✓ |
| 25 | entrance | yes (object 26) | signboard | mismatch | ✗ |
| 26 | balcony | yes (object 27) | pillar | mismatch | ✗ |
| 27 | bench | yes (object 28) | runner carpet | mismatch | ✗ |
| 28 | sign | yes (object 29) | signboard | synonym | ✓ |

**Relations: 10/29 right, triplets: 10/29 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| person #0 - poses with - bag #22 | 0-9, 11-19 | carrying | 0-19 | mismatch | 0.89 | ✗ | ✗ |
| person #0 - carries - bag #22 | 0-9, 11-19 | carrying | 0-19 | identical | 0.89 | ✓ | ✓ |
| person #0 - moves on - carpet #1 | 0-9, 11-19 | on | 0-19 | semantic overlap | 0.89 | ✓ | ✓ |
| person #0 - on - carpet #1 | 0-9, 11-19 | on | 0-19 | identical | 0.89 | ✓ | ✓ |
| person #0 - in front of - curtain #4 | 0-9, 11-19 | in front of | 0-19 | identical | 0.89 | ✓ | ✓ |
| person #0 - in front of - windows #5 | 0-9, 11-19 | in front of | 0-19 | identical | 0.89 | ✓ | ✓ |
| person #0 - in front of - chair #7 | 0-9, 11-19 | in front of (+2 more) | 0-19 | identical | 0.89 | ✓ | ✓ |
| person #0 - in front of - table #3 | 0-9, 11-19 | approaching (+1 more) | 0-11 | mismatch | 0.47 | ✗ | ✗ |
| person #0 - in front of - wall panel #8 | 0-9, 11-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| carpet #1 - on - floor #9 | 0-5, 9-10, 11-12 | nothing for this pair | - | - | - | ✗ | ✗ |
| sofa #2 - on - carpet #1 | 0-8, 12-15, 18-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| table #3 - in front of - chair #7 | 0-9, 11-19 | in front of | 0-19 | identical | 0.89 | ✓ | ✓ |
| table #3 - on - carpet #1 | 0-9, 11-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| curtain #4 - in front of - windows #5 | 0-9, 11-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| chair #7 - on - carpet #1 | 0-9, 11-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| wall panel #8 - below - curtain #4 | 0-9, 11-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| pillars #10 - on - floor #9 | 9-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| fountain #11 - on - floor #9 | 10-12 | nothing for this pair | - | - | - | ✗ | ✗ |
| desk #12 - in front of - pillar #20 | 8.5-10.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| desk #12 - on - floor #9 | 9-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| sofa #13 - on - carpet #1 | 9-10 | nothing for this pair | - | - | - | ✗ | ✗ |
| lights #14 - above - desk #12 | 8.5-10.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| door #18 - above - floor #9 | 8.5-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| bag #22 - moves with - person #0 | 0-9, 11-19 | beside | 0-19 | semantic overlap | 0.89 | ✓ | ✓ |
| bag #22 - near - person #0 | 0-9, 11-19 | beside | 0-19 | synonym | 0.89 | ✓ | ✓ |
| head #23 - above - legs #24 | 0-9, 11-19 | nothing for this pair | - | - | - | ✗ | ✗ |
| legs #24 - on - carpet #1 | 0-9, 11-19 | above | 0-19 | semantic overlap | 0.89 | ✓ | ✓ |
| entrance #25 - above - floor #9 | 9-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| bench #27 - on - floor #9 | 9.5-12 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (25): person #0 - wearing - head #23 [0-19]; person #0 - wearing - legs #24 [0-19]; head #23 - on - person #0 [0-19]; legs #24 - on - person #0 [0-19]; bag #22 - above - carpet #1 [0-19]; head #23 - above - carpet #1 [0-19]; chair #7 - in front of - curtain #4 [0-19]; chair #7 - in front of - windows #5 [0-19]; table #3 - in front of - curtain #4 [0-19]; table #3 - in front of - windows #5 [0-19]


## sav_054217

19.54 s, 20 frames read | human: 22 objects, 23 relations | TRASER: 22 objects, 38 relations, valid JSON, 1793 tokens

**Objects: 18/22 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | girl | yes (object 1) | girl | identical | ✓ |
| 1 | screen | yes (object 2) | screen | identical | ✓ |
| 2 | safety net or wall | yes (object 3) | net | synonym | ✓ |
| 3 | trampoline | yes (object 4) | mat | semantic overlap | ✓ |
| 4 | ceiling | yes (object 5) | ceiling tile (uncertain) | semantic overlap | ✓ |
| 5 | frame | yes (object 6) | pole (uncertain) | mismatch | ✗ |
| 6 | mat | yes (object 7) | mat | identical | ✓ |
| 7 | padding | yes (object 8) | mat | synonym | ✓ |
| 8 | dress | yes (object 9) | dress | identical | ✓ |
| 9 | floor | yes (object 10) | mat | semantic overlap | ✓ |
| 10 | grass | yes (object 11) | mat | mismatch | ✗ |
| 11 | water | yes (object 12) | mat | mismatch | ✗ |
| 12 | sky | yes (object 13) | screen | mismatch | ✗ |
| 13 | hair | yes (object 14) | hair | identical | ✓ |
| 14 | leg | yes (object 15) | legs | identical | ✓ |
| 15 | leg | yes (object 16) | legs | identical | ✓ |
| 16 | arm | yes (object 17) | arm (uncertain) | identical | ✓ |
| 17 | arm | yes (object 18) | arm (uncertain) | identical | ✓ |
| 18 | pad | yes (object 19) | mat | synonym | ✓ |
| 19 | pad | yes (object 20) | mat | synonym | ✓ |
| 20 | pad | yes (object 21) | mat | synonym | ✓ |
| 21 | pad | yes (object 22) | mat | synonym | ✓ |

**Relations: 8/23 right, triplets: 8/23 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| girl #0 - in front of - screen #1 | 0-20 | in front of (+2 more) | 0-20 | identical | 1.00 | ✓ | ✓ |
| girl #0 - play game with - screen #1 | 0-20 | looking at (+2 more) | 0-20 | mismatch | 1.00 | ✗ | ✗ |
| girl #0 - look at - screen #1 | 0-20 | looking at (+2 more) | 0-20 | identical | 1.00 | ✓ | ✓ |
| girl #0 - on - trampoline #3 | 0-20 | standing on (+3 more) | 0-20 | hypernym/hyponym | 1.00 | ✓ | ✓ |
| girl #0 - jump on - trampoline #3 | 0-20 | standing on (+3 more) | 0-20 | semantic overlap | 1.00 | ✓ | ✓ |
| girl #0 - above - mat #6 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| girl #0 - move up and down relative to - mat #6 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| girl #0 - under - ceiling #4 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| girl #0 - inside - frame #5 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| girl #0 - hold - dress #8 | 4.5-17.5, 18-20 | wearing | 0-20 | mismatch | 0.75 | ✗ | ✗ |
| girl #0 - wear - dress #8 | 0-20 | wearing | 0-20 | identical | 1.00 | ✓ | ✓ |
| safety net or wall #2 - inside - frame #5 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| trampoline #3 - in front of - screen #1 | 0-20 | in front of (+1 more) | 0-20 | identical | 1.00 | ✓ | ✓ |
| ceiling #4 - above - screen #1 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| frame #5 - around - screen #1 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| mat #6 - inside - trampoline #3 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| padding #7 - around - mat #6 | 0-20 | nothing for this pair | - | - | - | ✗ | ✗ |
| dress #8 - on - girl #0 | 0-20 | on | 0-20 | identical | 1.00 | ✓ | ✓ |
| grass #10 - on - screen #1 | 0-9 | inside | 0-10 | mismatch | 0.90 | ✗ | ✗ |
| water #11 - on - screen #1 | 9-20 | inside | 10-20 | mismatch | 0.91 | ✗ | ✗ |
| sky #12 - on - screen #1 | 0-20 | inside | 0-20 | mismatch | 1.00 | ✗ | ✗ |
| hair #13 - on - girl #0 | 0-20 | on | 0-20 | identical | 1.00 | ✓ | ✓ |
| hair #13 - swing relative to - girl #0 | 0-20 | on | 0-20 | mismatch | 1.00 | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (23): girl #0 - has - hair #13 [0-20]; girl #0 - in front of - safety net or wall #2 [0-20]; girl #0 - below - safety net or wall #2 [0-20]; leg #14 - on - trampoline #3 [0-20]; leg #15 - on - trampoline #3 [0-20]; safety net or wall #2 - in front of - screen #1 [0-20]; safety net or wall #2 - above - trampoline #3 [0-20]; floor #9 - inside - screen #1 [0-4, 18-20]; pad #21 - inside - screen #1 [0-20]; pad #18 - inside - screen #1 [0-20]


## sav_054440

13.04 s, 13 frames read | human: 42 objects, 53 relations | TRASER: 38 objects, 38 relations, valid JSON, 2827 tokens

**Objects: 30/42 right**

| id | human label | mask given to TRASER? | TRASER label | verdict | right |
|---|---|---|---|---|---|
| 0 | tissue package | yes (object 1) | plastic bag | semantic overlap | ✓ |
| 1 | car | yes (object 2) | dashboard | semantic overlap | ✓ |
| 2 | sky | yes (object 3) | telephone pole (uncertain) | mismatch | ✗ |
| 3 | road | yes (object 4) | car | mismatch | ✗ |
| 4 | tree | yes (object 5) | tree | identical | ✓ |
| 5 | tree | yes (object 6) | tree | identical | ✓ |
| 6 | tree | yes (object 7) | tree | identical | ✓ |
| 7 | tree | yes (object 8) | tree | identical | ✓ |
| 8 | tree | yes (object 9) | tree | identical | ✓ |
| 9 | tree | no: no mask on the frames TRASER reads | - | no label from TRASER | ✗ |
| 10 | tree | yes (object 10) | tree | identical | ✓ |
| 11 | tree | yes (object 11) | tree | identical | ✓ |
| 12 | tree | yes (object 12) | tree | identical | ✓ |
| 13 | tree | no: no mask on the frames TRASER reads | - | no label from TRASER | ✗ |
| 14 | sidewalk | yes (object 13) | sidewalk | identical | ✓ |
| 15 | signboard | yes (object 14) | building | mismatch | ✗ |
| 16 | signboard | yes (object 15) | signboard | identical | ✓ |
| 17 | sign | yes (object 16) | sign | identical | ✓ |
| 18 | building | yes (object 17) | building | identical | ✓ |
| 19 | building | yes (object 18) | building | identical | ✓ |
| 20 | building | yes (object 19) | building | identical | ✓ |
| 21 | trees | yes (object 20) | hill | mismatch | ✗ |
| 22 | buildings | yes (object 21) | mountain | mismatch | ✗ |
| 23 | power pole | yes (object 22) | telephone pole (uncertain) | synonym | ✓ |
| 24 | light or pole | yes (object 23) | telephone pole (uncertain) | hypernym/hyponym | ✓ |
| 25 | power pole | yes (object 24) | telephone pole (uncertain) | synonym | ✓ |
| 26 | electric wire | yes (object 25) | wire (uncertain) | hypernym/hyponym | ✓ |
| 27 | electric wire | yes (object 26) | telephone wire (uncertain) | hypernym/hyponym | ✓ |
| 28 | tree | yes (object 27) | tree | identical | ✓ |
| 29 | wall | yes (object 28) | wall | identical | ✓ |
| 30 | tree | yes (object 29) | tree | identical | ✓ |
| 31 | tree | yes (object 30) | tree | identical | ✓ |
| 32 | tree | yes (object 31) | cloud | mismatch | ✗ |
| 33 | wiper | yes (object 32) | windshield wiper | identical | ✓ |
| 34 | mirror | yes (object 33) | rearview mirror | hypernym/hyponym | ✓ |
| 35 | speaker | yes (object 34) | vent | semantic overlap | ✓ |
| 36 | garage door | yes (object 35) | shutter (uncertain) | semantic overlap | ✓ |
| 37 | car | yes (object 36) | pole (uncertain) | mismatch | ✗ |
| 38 | sun | yes (object 37) | sun | identical | ✓ |
| 39 | rolling shutter door | yes (object 38) | building | mismatch | ✗ |
| 40 | balcony | no: after the first 40 | - | no label from TRASER | ✗ |
| 41 | ac | no: after the first 40 | - | no label from TRASER | ✗ |

**Relations: 10/53 right, triplets: 8/53 right** (lenient, tIoU > 0.5)

| human: subject - predicate - object | human time | TRASER (same two objects) | TRASER time | word | tIoU | relation | triplet |
|---|---|---|---|---|---|---|---|
| tissue package #0 - inside - car #1 | 0-2.5, 6.5-14 | on (+1 more) | 0-13 | mismatch | 0.64 | ✗ | ✗ |
| tissue package #0 - below - speaker #35 | 0-2.5, 6.5-14 | below | 0-13 | identical | 0.64 | ✓ | ✓ |
| car #1 - moving along - road #3 | 0-14 | inside | 0-13 | mismatch | 0.93 | ✗ | ✗ |
| car #1 - driving through - road #3 | 0-14 | inside | 0-13 | semantic overlap | 0.93 | ✓ | ✗ |
| car #1 - passing - signboard #15 | 6-8.5 | in front of | 6-8 | semantic overlap | 0.80 | ✓ | ✗ |
| car #1 - approaching - signboard #16 | 6-9.5 | in front of | 6-8 | mismatch | 0.57 | ✗ | ✗ |
| car #1 - passing by - tree #11 | 6.5-11 | in front of | 6-13 | semantic overlap | 0.64 | ✓ | ✓ |
| car #1 - passing by - building #18 | 7-14 | in front of | 6-13 | semantic overlap | 0.75 | ✓ | ✓ |
| car #1 - moving toward - trees #21 | 6-14 | in front of (+1 more) | 0-13 | mismatch | 0.50 | ✗ | ✗ |
| car #1 - carrying - tissue package #0 | 0-2.5, 6.5-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| road #3 - below - sky #2 | 0-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| road #3 - beside - sidewalk #14 | 0-5.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| road #3 - in front of - buildings #22 | 0-6 | nothing for this pair | - | - | - | ✗ | ✗ |
| road #3 - in front of - trees #21 | 0-2.5, 6-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #4 - beside - sidewalk #14 | 0-2.5, 4-6.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #6 - beside - sidewalk #14 | 2-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #8 - beside - sidewalk #14 | 3-4 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #9 - beside - sidewalk #14 | 4-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| tree #12 - in front of - trees #21 | 11-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| signboard #15 - above - road #3 | 6-8 | nothing for this pair | - | - | - | ✗ | ✗ |
| signboard #16 - above - road #3 | 6-9.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign #17 - mounted on - signboard #16 | 6-9 | nothing for this pair | - | - | - | ✗ | ✗ |
| sign #17 - above - road #3 | 6-9 | nothing for this pair | - | - | - | ✗ | ✗ |
| building #18 - in front of - trees #21 | 6-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| building #19 - in front of - trees #21 | 6-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| trees #21 - below - sky #2 | 0-2, 7-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| buildings #22 - below - sky #2 | 2-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| power pole #23 - in front of - sky #2 | 0-2 | nothing for this pair | - | - | - | ✗ | ✗ |
| light or pole #24 - in front of - sky #2 | 0-3 | nothing for this pair | - | - | - | ✗ | ✗ |
| power pole #25 - in front of - sky #2 | 0-1.5, 3.5-5.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| electric wire #26 - in front of - sky #2 | 1-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| electric wire #26 - connected to - power pole #25 | 4-5.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| electric wire #26 - above - road #3 | 2-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| electric wire #27 - in front of - sky #2 | 7-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| electric wire #27 - above - road #3 | 7-12 | nothing for this pair | - | - | - | ✗ | ✗ |
| wall #29 - part of - building #19 | 8.5-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| wall #29 - in front of - building #19 | 9-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| wiper #33 - mounted on - car #1 | 0-2.5, 5.5-14 | attached to (+1 more) | 0-13 | synonym | 0.71 | ✓ | ✓ |
| wiper #33 - on - car #1 | 0-2, 6-14 | attached to (+1 more) | 0-13 | semantic overlap | 0.64 | ✓ | ✓ |
| mirror #34 - mounted on - car #1 | 1-7.5 | attached to (+1 more) | 0-8 | synonym | 0.81 | ✓ | ✓ |
| mirror #34 - on - car #1 | 2-7 | attached to (+1 more) | 0-8 | semantic overlap | 0.62 | ✓ | ✓ |
| mirror #34 - in front of - road #3 | 2-7 | nothing for this pair | - | - | - | ✗ | ✗ |
| speaker #35 - mounted on - car #1 | 0-2.5, 5.5-14 | attached to (+1 more) | 0-13 | synonym | 0.71 | ✓ | ✓ |
| speaker #35 - inside - car #1 | 0-2, 6-14 | attached to (+1 more) | 0-13 | mismatch | 0.64 | ✗ | ✗ |
| garage door #36 - part of - building #18 | 8-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| garage door #36 - on - building #18 | 7.5-11 | nothing for this pair | - | - | - | ✗ | ✗ |
| sun #38 - above - buildings #22 | 2-5 | nothing for this pair | - | - | - | ✗ | ✗ |
| rolling shutter door #39 - part of - building #18 | 8-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| rolling shutter door #39 - on - building #18 | 8-13 | nothing for this pair | - | - | - | ✗ | ✗ |
| rolling shutter door #39 - below - balcony #40 | 6.5-13.5 | nothing for this pair | - | - | - | ✗ | ✗ |
| balcony #40 - part of - building #18 | 7-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| balcony #40 - on - building #18 | 7-14 | nothing for this pair | - | - | - | ✗ | ✗ |
| ac #41 - mounted on - car #1 | 6-10.5 | nothing for this pair | - | - | - | ✗ | ✗ |

TRASER relations between pairs the humans did not annotate (22): wiper #33 - above - speaker #35 [0-13]; mirror #34 - above - speaker #35 [0-8]; car #1 - in front of - sidewalk #14 [0-6]; car #1 - in front of - buildings #22 [0-6]; car #1 - in front of - buildings #22 [0-6]; car #1 - in front of - building #19 [6-13]; car #1 - in front of - building #20 [10-13]; car #1 - in front of - rolling shutter door #39 [10-13]; car #1 - in front of - tree #12 [10-13]; car #1 - in front of - tree #10 [6-8]

