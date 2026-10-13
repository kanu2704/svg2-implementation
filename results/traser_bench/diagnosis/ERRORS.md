# Where TRASER loses its points (diagnosis, part A)

Made by `tools/error_analysis.py` from the saved answers (no GPU). Same scoring as `README.md`: lenient judge, temporal IoU > 0.5, VidOR occurrences merged. Every human relation is followed until the first step it fails. Row by row: `errors.csv` (human relations), `objects.csv` (objects TRASER was given), `traser_relations.csv` (every relation TRASER wrote).

## 1. Where each human relation fails

| step | pvsg | svg2test | vidor |
|---|---|---|---|
| 0. object not given to TRASER | 19 (2%) | 223 (7%) | 8 (0%) |
| 1a. pair written only the other way round | 35 (4%) | 219 (7%) | 5303 (29%) |
| 1b. pair not written at all | 532 (55%) | 1542 (48%) | 4320 (24%) |
| 2. pair written, relation word wrong | 115 (12%) | 250 (8%) | 4503 (25%) |
| 3. word right, time wrong | 133 (14%) | 89 (3%) | 1685 (9%) |
| 4. relation right, an object name wrong (triplet only) | 35 (4%) | 188 (6%) | 319 (2%) |
| relation and triplet right | 100 (10%) | 676 (21%) | 2038 (11%) |
| **all human relations** | 969 | 3187 | 18176 |

Check against `README.md` (lenient, tIoU 0.5): relation = steps 4 + right, triplet = right only.

| | pvsg | svg2test | vidor |
|---|---|---|---|
| Relation recall | 14% | 27% | 13% |
| Triplet recall | 10% | 21% | 11% |

## 2. The guesses (hypotheses) in numbers

**pvsg** (950 human relations whose objects TRASER was given)

- **H1 pair choice:** 60% never get their pair written (4% only the other way round). In 39% of those, TRASER used *both* objects in other relations, just not together.
- **H2 habit:** position words are 48% of TRASER's extra relations vs 42% of the ones that match a human relation; 68% of everything TRASER writes is an extra pair.
- **H3 time:** 35% of written pairs have the right word but the wrong time.
- **H5 loops:** 33% of TRASER's relations repeat an earlier one word for word; 42% come from answers cut off at 8,192 tokens.
- **H6 direction:** 4% of human relations are written only the other way round.

**svg2test** (2964 human relations whose objects TRASER was given)

- **H1 pair choice:** 59% never get their pair written (7% only the other way round). In 48% of those, TRASER used *both* objects in other relations, just not together.
- **H2 habit:** position words are 86% of TRASER's extra relations vs 70% of the ones that match a human relation; 73% of everything TRASER writes is an extra pair.
- **H3 time:** 7% of written pairs have the right word but the wrong time.
- **H5 loops:** 19% of TRASER's relations repeat an earlier one word for word; 15% come from answers cut off at 8,192 tokens.
- **H6 direction:** 7% of human relations are written only the other way round.

**vidor** (18168 human relations whose objects TRASER was given)

- **H1 pair choice:** 53% never get their pair written (29% only the other way round). In 91% of those, TRASER used *both* objects in other relations, just not together.
- **H2 habit:** position words are 81% of TRASER's extra relations vs 67% of the ones that match a human relation; 17% of everything TRASER writes is an extra pair.
- **H3 time:** 20% of written pairs have the right word but the wrong time.
- **H5 loops:** 0% of TRASER's relations repeat an earlier one word for word; 0% come from answers cut off at 8,192 tokens.
- **H6 direction:** 29% of human relations are written only the other way round.

H4 (small objects) is in section 5.

## 3. When does it fail?

Human relations whose objects TRASER was given. Per group: **n**, **pair** = pair written (steps 2-4 and right), **word** = relation word right among written pairs, **rel.** = relation right (counts in the recall). The line under each table compares the first and last group of *pair written* (≈: within 5 points; groups with fewer than 30 relations left out).

Measurements from the masks (size, time on screen together, gap): not made yet (run `tools/mask_features.py` where the masks are), so those tables are missing.

### Relation type (our position-word list vs everything else)

| group | pvsg n | pair | word | rel. | svg2test n | pair | word | rel. | vidor n | pair | word | rel. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| position | 274 | 34% | 78% | 19% | 1926 | 36% | 85% | 29% | 14538 | 44% | 48% | 13% |
| action/other | 676 | 43% | 67% | 12% | 1038 | 48% | 71% | 30% | 3630 | 60% | 46% | 13% |

Pair written, first → last group: pvsg: 34% → 43% ↑; svg2test: 36% → 48% ↑; vidor: 44% → 60% ↑

### How common the relation word is in this dataset

| group | pvsg n | pair | word | rel. | svg2test n | pair | word | rel. | vidor n | pair | word | rel. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| top 10 words | 618 | 37% | 76% | 16% | 2087 | 38% | 86% | 30% | 16767 | 45% | 47% | 13% |
| words 11-50 | 320 | 47% | 62% | 12% | 553 | 44% | 70% | 28% | 1401 | 68% | 54% | 16% |
| rarer words | 12 | 33% | 25% | 0% | 324 | 55% | 60% | 24% | 0 | – | – | – |

Pair written, first → last group: pvsg: 37% → 47% ↑; svg2test: 38% → 55% ↑; vidor: 45% → 68% ↑

### Relation length

| group | pvsg n | pair | word | rel. | svg2test n | pair | word | rel. | vidor n | pair | word | rel. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| < 2 s | 123 | 37% | 49% | 1% | 80 | 32% | 50% | 2% | 2417 | 45% | 32% | 2% |
| 2-5 s | 193 | 41% | 55% | 2% | 332 | 32% | 60% | 6% | 5085 | 43% | 40% | 5% |
| 5-15 s | 201 | 38% | 71% | 10% | 1641 | 44% | 81% | 34% | 5729 | 47% | 51% | 14% |
| >= 15 s | 433 | 42% | 81% | 25% | 911 | 37% | 83% | 31% | 4937 | 52% | 56% | 26% |

Pair written, first → last group: pvsg: 37% → 42% ↑; svg2test: 32% → 37% ≈; vidor: 45% → 52% ↑

### Relation length as a share of the video

| group | pvsg n | pair | word | rel. | svg2test n | pair | word | rel. | vidor n | pair | word | rel. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| < 25% | 500 | 38% | 59% | 3% | 182 | 34% | 54% | 2% | 9051 | 43% | 40% | 4% |
| 25-50% | 124 | 42% | 79% | 18% | 223 | 34% | 68% | 9% | 3196 | 45% | 49% | 9% |
| 50-90% | 128 | 45% | 76% | 28% | 433 | 46% | 74% | 29% | 3055 | 51% | 54% | 26% |
| >= 90% | 198 | 41% | 85% | 30% | 2126 | 41% | 83% | 33% | 2866 | 56% | 58% | 32% |

Pair written, first → last group: pvsg: 38% → 41% ≈; svg2test: 34% → 41% ↑; vidor: 43% → 56% ↑

### Video length

| group | pvsg n | pair | word | rel. | svg2test n | pair | word | rel. | vidor n | pair | word | rel. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| < 15 s | 0 | – | – | – | 1720 | 41% | 80% | 31% | 3278 | 50% | 47% | 16% |
| 15-40 s | 197 | 56% | 71% | 25% | 1244 | 40% | 78% | 27% | 6904 | 47% | 48% | 14% |
| 40-90 s | 468 | 44% | 69% | 15% | 0 | – | – | – | 6316 | 47% | 46% | 11% |
| >= 90 s | 285 | 23% | 71% | 5% | 0 | – | – | – | 1670 | 43% | 49% | 11% |

Pair written, first → last group: pvsg: 56% → 23% ↓; svg2test: 41% → 40% ≈; vidor: 50% → 43% ↓

### Human objects in the video

| group | pvsg n | pair | word | rel. | svg2test n | pair | word | rel. | vidor n | pair | word | rel. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <= 5 | 16 | 56% | 67% | 12% | 0 | – | – | – | 6421 | 61% | 52% | 19% |
| 6-10 | 120 | 60% | 71% | 21% | 59 | 44% | 69% | 27% | 9292 | 42% | 43% | 11% |
| 11-20 | 449 | 45% | 69% | 15% | 772 | 46% | 76% | 31% | 2392 | 29% | 42% | 7% |
| 21-40 | 257 | 34% | 68% | 14% | 1140 | 40% | 80% | 30% | 63 | 19% | 25% | 3% |
| > 40 | 108 | 13% | 93% | 4% | 993 | 37% | 82% | 27% | 0 | – | – | – |

Pair written, first → last group: pvsg: 60% → 13% ↓; svg2test: 44% → 37% ↓; vidor: 61% → 19% ↓

### Image tokens TRASER kept for the smaller object of the pair (before compression)

| group | pvsg n | pair | word | rel. | svg2test n | pair | word | rel. | vidor n | pair | word | rel. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| < 50 | 185 | 33% | 69% | 11% | 1355 | 34% | 80% | 25% | 7003 | 40% | 44% | 11% |
| 50-200 | 254 | 41% | 81% | 17% | 860 | 41% | 82% | 31% | 4929 | 47% | 48% | 13% |
| 200-1000 | 315 | 44% | 70% | 16% | 649 | 50% | 77% | 35% | 4867 | 54% | 48% | 15% |
| >= 1000 | 196 | 41% | 58% | 11% | 100 | 62% | 69% | 36% | 1369 | 57% | 54% | 17% |

Pair written, first → last group: pvsg: 33% → 41% ↑; svg2test: 34% → 62% ↑; vidor: 40% → 57% ↑

### Input position of the later object (Object k of n)

| group | pvsg n | pair | word | rel. | svg2test n | pair | word | rel. | vidor n | pair | word | rel. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| first quarter | 20 | 20% | 75% | 5% | 760 | 48% | 75% | 32% | 548 | 44% | 49% | 9% |
| second | 209 | 46% | 75% | 17% | 837 | 41% | 81% | 30% | 3887 | 48% | 45% | 11% |
| third | 377 | 42% | 75% | 16% | 713 | 34% | 80% | 25% | 4948 | 46% | 47% | 13% |
| last quarter | 344 | 36% | 60% | 11% | 654 | 39% | 83% | 29% | 8785 | 48% | 48% | 14% |

Pair written, first → last group: pvsg: 46% → 36% ↓; svg2test: 48% → 39% ↓; vidor: 44% → 48% ≈

### Subject is a person or animal (camera counts)

| group | pvsg n | pair | word | rel. | svg2test n | pair | word | rel. | vidor n | pair | word | rel. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| yes | 765 | 43% | 67% | 13% | 986 | 54% | 78% | 38% | 13584 | 53% | 47% | 14% |
| no | 185 | 28% | 92% | 18% | 1978 | 34% | 80% | 25% | 4584 | 31% | 49% | 11% |

Pair written, first → last group: pvsg: 43% → 28% ↓; svg2test: 54% → 34% ↓; vidor: 53% → 31% ↓

### TRASER named both objects right (lenient)

| group | pvsg n | pair | word | rel. | svg2test n | pair | word | rel. | vidor n | pair | word | rel. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| both | 529 | 51% | 72% | 19% | 1766 | 51% | 82% | 38% | 14843 | 49% | 49% | 14% |
| one | 353 | 28% | 66% | 9% | 1017 | 27% | 71% | 17% | 3037 | 41% | 39% | 10% |
| neither | 68 | 19% | 69% | 4% | 181 | 10% | 63% | 6% | 288 | 35% | 42% | 8% |

Pair written, first → last group: pvsg: 51% → 19% ↓; svg2test: 51% → 10% ↓; vidor: 49% → 35% ↓

### Answer cut off at 8,192 tokens

| group | pvsg n | pair | word | rel. | svg2test n | pair | word | rel. | vidor n | pair | word | rel. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| no | 760 | 45% | 71% | 17% | 2791 | 42% | 80% | 30% | 18168 | 47% | 47% | 13% |
| yes | 190 | 22% | 63% | 2% | 173 | 18% | 68% | 9% | 0 | – | – | – |

Pair written, first → last group: pvsg: 45% → 22% ↓; svg2test: 42% → 18% ↓; vidor: –

### Answer repeats a relation word for word

| group | pvsg n | pair | word | rel. | svg2test n | pair | word | rel. | vidor n | pair | word | rel. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| no | 742 | 41% | 71% | 15% | 2425 | 42% | 79% | 31% | 17629 | 47% | 48% | 13% |
| yes | 208 | 37% | 64% | 11% | 539 | 32% | 78% | 22% | 539 | 38% | 33% | 7% |

Pair written, first → last group: pvsg: 41% → 37% ≈; svg2test: 42% → 32% ↓; vidor: 47% → 38% ↓

## 4. Relation words

The 15 most common human relation words of each dataset (relations whose objects TRASER was given).

**pvsg**

| word | n | pair written | word right (of written) | relation right |
|---|---|---|---|---|
| holding | 187 | 38% | 83% | 15% |
| on | 133 | 30% | 98% | 23% |
| in front of | 52 | 44% | 91% | 31% |
| beside | 46 | 22% | 20% | 4% |
| touching | 44 | 36% | 81% | 5% |
| standing on | 36 | 47% | 100% | 28% |
| walking on | 35 | 37% | 62% | 9% |
| picking | 31 | 35% | 36% | 0% |
| opening | 29 | 38% | 36% | 7% |
| looking at | 25 | 64% | 44% | 16% |
| sitting on | 23 | 61% | 93% | 35% |
| running on | 20 | 30% | 100% | 5% |
| next to | 19 | 32% | 17% | 5% |
| wearing | 16 | 62% | 100% | 38% |
| playing with | 16 | 62% | 60% | 19% |

**svg2test**

| word | n | pair written | word right (of written) | relation right |
|---|---|---|---|---|
| on | 685 | 34% | 90% | 28% |
| in front of | 515 | 51% | 94% | 44% |
| above | 236 | 24% | 82% | 19% |
| attached to | 148 | 32% | 90% | 27% |
| wearing | 112 | 59% | 97% | 54% |
| behind | 102 | 25% | 19% | 5% |
| below | 102 | 16% | 44% | 6% |
| in | 81 | 41% | 85% | 33% |
| under | 69 | 32% | 73% | 22% |
| wears | 51 | 51% | 92% | 47% |
| part of | 46 | 33% | 100% | 33% |
| inside | 37 | 59% | 55% | 32% |
| looking at | 32 | 50% | 56% | 25% |
| approaches | 30 | 57% | 24% | 7% |
| has | 29 | 14% | 75% | 10% |

**vidor**

| word | n | pair written | word right (of written) | relation right |
|---|---|---|---|---|
| next to | 5059 | 40% | 28% | 8% |
| in front of | 4497 | 45% | 83% | 25% |
| behind | 1845 | 33% | 26% | 4% |
| watch | 1782 | 50% | 30% | 4% |
| away | 1244 | 56% | 25% | 2% |
| towards | 1083 | 55% | 35% | 4% |
| beneath | 387 | 21% | 10% | 2% |
| above | 373 | 77% | 75% | 52% |
| hold | 265 | 74% | 83% | 37% |
| lean on | 232 | 79% | 51% | 34% |
| speak to | 159 | 50% | 44% | 5% |
| ride | 102 | 68% | 83% | 49% |
| hug | 95 | 65% | 76% | 23% |
| touch | 83 | 70% | 50% | 2% |
| carry | 75 | 77% | 83% | 48% |

## 5. Objects: tokens kept, size, names (H4)

Every object TRASER was given. **named right** = lenient judge; **in TRASER rel.** / **in human rel.** = the object appears in at least one relation of TRASER / of the humans.

### Image tokens kept (before compression)

| group | pvsg n | named right | in TRASER rel. | in human rel. | svg2test n | named right | in TRASER rel. | in human rel. | vidor n | named right | in TRASER rel. | in human rel. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| < 50 | 265 | 57% | 53% | 39% | 1531 | 62% | 64% | 53% | 1371 | 79% | 95% | 88% |
| 50-200 | 263 | 78% | 60% | 56% | 640 | 74% | 77% | 65% | 961 | 88% | 97% | 96% |
| 200-1000 | 330 | 73% | 62% | 54% | 507 | 76% | 81% | 81% | 1095 | 92% | 98% | 99% |
| >= 1000 | 308 | 65% | 65% | 65% | 171 | 70% | 77% | 82% | 546 | 93% | 99% | 100% |

## 6. What TRASER writes

Every relation in TRASER's answers (repeats included).

| kind | pvsg | svg2test | vidor |
|---|---|---|---|
| matches a human relation | 177 (6%) | 901 (15%) | 2611 (26%) |
| human pair, other relation | 439 (15%) | 439 (7%) | 5451 (53%) |
| reverse of a human pair | 87 (3%) | 283 (5%) | 388 (4%) |
| extra pair | 1986 (68%) | 4340 (73%) | 1746 (17%) |
| invalid object number | 225 (8%) | 0 (0%) | 2 (0%) |
| **all** | 2914 | 5963 | 10198 |

Extra pairs, what they look like (one relation can have several flags):

| flag | pvsg | svg2test | vidor |
|---|---|---|---|
| position word | 48% | 86% | 81% |
| an object named wrong | 54% | 43% | 28% |
| floor/wall/sky-type object (PVSG only) | 34% | 0% | 0% |
| repeats an earlier relation word for word | 40% | 23% | 0% |
| same subject and word written for 5+ objects | 62% | 58% | 24% |
| answer cut off | 42% | 18% | 0% |

## 7. Examples

Six random human relations per step and dataset (seed 0). *TRASER for this pair* lists its relation words for the same two objects, *reverse* those for the other direction.

### pvsg

**0. object not given to TRASER**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| P03_06 | adult #29 → touching → plate #65 [63-64.8s] | – | – |
| P11_11 | adult #24 → opening → cabinet #44 [2.6-5.4s] | – | – |
| P01_03 | adult #26 → holding → bottle #68 [31.8-33.4s] | – | – |
| P03_06 | adult #29 → opening → cabinet #46 [14.2-15s] | – | – |
| d1d4a1b3-a651-4eb8-bb7f-8d66982854fa | card #42 → on → card #40 [158.4-175.4s] | – | – |
| P03_06 | adult #29 → touching → pot #43 [10.2-12.6s] | – | – |

**1a. pair written only the other way round**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| 1017_3056841458 | child #8 → touching → cake #12 [2.8-3.6s, 18.8-23s, 33.2-34.6s, 47.4-48.2s, 50.6-51.8s, 56.4-57.4s, 64.6-65.4s, 70-71s, 76.2-77s] | – | in front of |
| 0096_5296138427 | table #5 → beside → chair #9 [0-19.4s] | – | in front of |
| 1025_6244382586 | child #9 → looking at → child #5 [0-5.2s] | – | moving with; next to |
| 1005_4760962392 | child #12 → beside → adult #4 [0-90s] | – | serving |
| 0096_5296138427 | table #5 → beside → chair #6 [0-19.4s] | – | in front of |
| 1025_4615486172 | adult #22 → hugging → adult #19 [50.4-81.2s] | – | photographing; photographing; photographing; photographing; photographing; photographing; photographing; photographing; photographing; photographing; photographing; photographing |

**1b. pair not written at all**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| 1025_4615486172 | chair #12 → in front of → ballon #16 [4.2-90s] | – | – |
| d2222009-a717-4b16-91ce-6399c5bb798a | adult #9 → picking → cup #38 [68.2-73.2s] | – | – |
| 1011_4633647136 | cake #9 → on → table #6 [0-53.6s] | – | – |
| 1203_8316378691 | adult #22 → holding → camera #16 [0-60.2s] | – | – |
| 1011_4633647136 | candle #8 → on → cake #9 [0-40.6s, 47.4-53.6s] | – | – |
| 0096_5296138427 | adult #8 → sitting on → chair #6 [11-19.4s] | – | – |

**2. pair written, relation word wrong**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| 1025_4615486172 | adult #19 → holding → child #10 [12.8-90s] | photographing; looking at; photographing; photographing; photographing; photographing | – |
| P05_05 | adult #14 → opening → bag #28 [54-57.6s] | holding; placing; placing; placing | – |
| 1000_6828150903 | adult #8 → beside → door #5 [0-5.2s] | in front of | – |
| 1019_3768851893 | curtain #4 → on → wall #2 [0-52s, 58-58.6s] | behind | – |
| 1124_9861436503 | child #7 → swinging → toy #11 [0-30.6s, 45-55.2s] | pushes; holds; plays with; near | – |
| P08_07 | adult #16 → opening → bottle #19 [8.6-9.8s] | hold | – |

**3. word right, time wrong**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| 0075_11566764085 | adult #4 → holding → toy #9 [49.8-58.8s] | holding; placing; assembling; touching | – |
| 1021_3478653250 | child #7 → hitting → ball #10 [17.2-18.6s] | hitting; hitting; hitting; hitting | – |
| 0057_7001078933 | adult #9 → squatting on → grass #2 [6.2-7.6s] | above | – |
| 0046_11919433184 | child #9 → running on → grass #3 [105.2-112.8s] | on | – |
| 1021_4278168115 | child #7 → holding → box #8 [31-33.2s] | holding; opening; looking at | – |
| P05_05 | adult #14 → holding → cookie #5 [60.4-61.6s] | holding; placing; placing; placing; placing | – |

**4. relation right, an object name wrong (triplet only)**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| 1012_4024008346 | ballon #11 → on → floor #1 [0-19.6s] | on | – |
| P02_10 | adult #19 → stirring → simmering #4 [6-43.2s] | stirring; cooking | – |
| P08_07 | adult #16 → holding → bottle #19 [2.4-3.6s, 7.4-17.8s] | hold | – |
| P02_10 | adult #19 → holding → spatula #6 [2.8-46.4s] | holding | – |
| 6e0a6558-c212-4cab-b374-007671edb59c_2 | adult #17 → holding → paper #25 [51.8-55.6s] | holding; washing; holding; washing; holding; washing | – |
| P11_11 | adult #24 → cutting → pizza #6 [26.4-39.4s] | cutting; holding; placing; preparing | – |

**relation and triplet right**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| 0096_5296138427 | adult #4 → holding → towel #7 [16.8-19.4s] | holding | – |
| 1021_4278168115 | book #5 → on → floor #2 [42.8-43.4s, 50.6-79.8s] | on | – |
| 1020_2471845614 | flower #5 → on → table #9 [0-55.8s] | on | – |
| 1017_3056841458 | adult #7 → beside → child #8 [1-60.2s] | touching; helping; serving drink to | – |
| 1021_3478653250 | child #7 → holding → bat #8 [0-62.6s] | holding | – |
| 1001_7007447516 | adult #9 → guiding → child #10 [0-71.4s] | holding; moving with; riding with; transporting; next to | moving with |

### svg2test

**0. object not given to TRASER**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| 1717_lh_2_1duNgw | player #2 → wearing → glove #61 [0-8] | – | – |
| sav_028579 | picture frame #38 → on → wall #48 [0-20] | – | – |
| 976_U19VojbI0h4 | flower vase #46 → on → flower stand #47 [0-8] | – | – |
| 1047_-_XOsbwGZgg | bin cover #51 → covering → thrash can #5 [0-8] | – | – |
| 1936_gvKlIkjfP0Q | car #0 → has → rear wing #43 [0-3] | – | – |
| sav_009307 | present #55 → attached to → christmas tree #9 [0-16] | – | – |

**1a. pair written only the other way round**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| sav_052661 | woman #0 → moves in front of → woman #1 [13-15.5] | – | approaching; dancing with; performing dance routine with |
| 474_b-Qlvj48YQw | pillars #3 → on → floor #2 [0-8] | – | in front of |
| sav_010923 | face #35 → on → person #0 [0-19] | – | in front of |
| sav_036919 | stick #9 → under → pot #2 [0-18] | – | in front of |
| sav_030325 | person #3 → holding → tennis racket #4 [0-10, 11.5-16] | – | overlapping |
| sav_009146 | bollard #7 → in front of → mixer truck #17 [0-1.5, 2-14] | – | in front of; in front of |

**1b. pair not written at all**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| sav_030325 | racquet ball #6 → moves away from → person #0 [1-4.5, 5.5-8, 10.5-13] | – | – |
| 1016_8J41CsGYhNI | ball #0 → approaches → tennis net #1 [9-10, 20-23] | – | – |
| sav_028579 | person #0 → wearing → cloth #2 [0-20] | – | – |
| sav_002789 | woman #1 → in front of → man #2 [0-14] | – | – |
| 551_VHxQVmG1pOA | display counter #23 → in front of → wall #14 [0-7] | – | – |
| 308_7WhzIsqPQW8 | country logo #7 → on → table #27 [0-23] | – | – |

**2. pair written, relation word wrong**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| sav_015587 | cat #4 → behind → litter box #9 [0-14] | in front of | – |
| 365_JFqiSr9A-Go | person #6 → looking at → keyboard #7 [3-6] | using | – |
| sav_010164 | man #2 → below → net #3 [0-17] | in front of | – |
| sav_037495 | cloth #0 → moves away from → tv set #6 [0-4, 8-11] | in front of | – |
| 1253_TPxVj7do42I | person #0 → pressing → switch #11 [6-8] | below | – |
| 1503_gwrvCEAZVl0 | excavator #4 → in front of → trees #6 [0-8.5] | above | – |

**3. word right, time wrong**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| sav_033373 | person #1 → on → pavement #6 [0-10] | rides along; on | – |
| 520_JbMXRRGOEkk | person #1 → approaches → post #6 [1-4] | approaching; moving away from; in front of | – |
| 670_JboU-y2LdkU | wheel #20 → under → car #10 [0-2, 5-6] | below | – |
| 365_JFqiSr9A-Go | person #6 → looking at → monitor #3 [0-3.5] | looking at; working on | – |
| sav_031935 | wristband #26 → on → hands #25 [0-5.5, 7-9] | on | – |
| sav_015763 | hand #6 → transfers → dough #7 [18-20] | holding; pressing; preparing; touching | – |

**4. relation right, an object name wrong (triplet only)**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| 1691_md-DpQ4HX7Q | ship #0 → in front of → trees #3 [0-8] | moves away from; in front of | – |
| 1308_-C_XboJfD0g | hand #1 → in front of → shelf #0 [0-6] | touching; moving away from; in front of | – |
| 551_VHxQVmG1pOA | girl #0 → wearing → glass #26 [0-7] | wearing | on |
| sav_004550 | bride #1 → in front of → wall #9 [0-14] | in front of | – |
| 987_g0mln-jiQTw | waterfalls #0 → on → rock #8 [0-23] | overlapping | – |
| 1691_md-DpQ4HX7Q | paddle wheel #15 → on → ship #0 [0-8] | on | has; in front of |

**relation and triplet right**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| 547_7E-Xian95Qk | toy donut #13 → in → tray #6 [0-7] | in | – |
| sav_023860 | person #0 → on → treadmill #12 [0-18] | on | – |
| 474_b-Qlvj48YQw | person #5 → wearing → coat #34 [0-8] | wearing | on |
| 1717_lh_2_1duNgw | player #2 → wearing → shoe #28 [0-8] | wearing | – |
| sav_023742 | dog #0 → jumping on → plastic mat #3 [3-9, 14-22] | standing on; on | – |
| 628_nQRJD435Fh4 | person #2 → in front of → wall #6 [0-23] | in front of | – |

### vidor

**0. object not given to TRASER**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| 4674481985 | adult #3 → watch → adult #1 [0.767433-0.967633s] | – | – |
| 9361705684 | adult #0 → watch → cellphone #4 [3.54521-4.42109s] | – | – |
| 4674481985 | adult #4 → watch → adult #0 [0.6006-1.03437s] | – | – |
| 5539388348 | adult #3 → carry → handbag #4 [2.66933-3.26993s] | – | – |
| 2697261300 | adult #5 → hold → camera #6 [24.2242-24.7247s] | – | – |
| 2435100235 | adult #23 → ride → bicycle #24 [41.8084-42.1755s] | – | – |

**1a. pair written only the other way round**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| 2796821016 | sofa #4 → next to → sofa #7 [0.133468-10.2103s, 45.3458-47.0142s] | – | in front of |
| 8505893258 | adult #2 → in front of → child #3 [0-31.031s] | – | dancing with; in front of |
| 5344655615 | table #4 → next to → adult #0 [18.018-21.021s] | – | in front of |
| 4688219212 | chair #10 → behind → child #0 [2.002-6.2062s, 20.6206-31.9653s] | – | moving away from; approaching; above |
| 8132842161 | duck #2 → in front of → child #7 [30.7307-36.8368s] | – | in front of |
| 4123915842 | child #1 → watch → adult #0 [5.13847-7.6076s, 22.8895-24.7247s] | – | holding; dressing; looking at; in front of; touching |

**1b. pair not written at all**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| 4798585428 | adult #3 → in front of → camera #9 [15.1151-22.1888s] | – | – |
| 3960291106 | bottle #8 → next to → cellphone #4 [38.8388-41.7751s] | – | – |
| 3972259774 | chair #7 → in front of → adult #4 [32.5742-34.9933s] | – | – |
| 3972259774 | adult #3 → next to → chair #7 [10.3437-42.7927s] | – | – |
| 13311361995 | toy #1 → in front of → screen/monitor #7 [0.4004-4.8048s] | – | – |
| 4688219212 | adult #3 → in front of → chair #7 [0.233567-2.96963s] | – | – |

**2. pair written, relation word wrong**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| 7921066748 | child #4 → next to → adult #5 [4.13747-5.87253s] | in front of | approaching |
| 2697261300 | dog #9 → next to → adult #1 [33.5001-35.0016s] | in front of | – |
| 2925298951 | adult #2 → inside → cup #0 [0-14.8065s] | holding; carrying | in front of; below |
| 3304386696 | adult #1 → in front of → adult #0 [4.004-9.009s] | looking at | holding hands with; dancing with; looking at; touching; overlapping |
| 3489439407 | adult #1 → next to → adult #0 [0-13.013s, 14.2142-15.7824s, 49.0156-55.0216s] | looking at | looking at; in front of |
| 2454242177 | baby #0 → next to → dog #2 [2.002-14.7814s] | in front of | – |

**3. word right, time wrong**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| 2495861393 | adult #5 → hold → vegetables #4 [28.4287-29.2295s] | holding | above |
| 7887764754 | dog #2 → watch → child #3 [10.0767-10.8775s, 12.3457-21.6883s, 34.1341-34.668s] | looking at; approaching; moving away from; in front of | looking at |
| 5913180144 | adult #4 → in front of → adult #7 [10.01-12.3123s, 16.016-27.027s] | in front of | – |
| 7572859950 | adult #1 → watch → baby #0 [12.1121-16.5832s] | holding; carrying; looking at; playing with | looking at; in front of; touching |
| 4761953886 | child #1 → watch → dog #0 [10.875-12.125s, 31.0833-31.75s] | petting; looking at; playing with; touching; in front of | looking at |
| 7996612680 | child #1 → watch → dog #0 [3.1031-4.03737s] | looking at | in front of |

**4. relation right, an object name wrong (triplet only)**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| 6836443264 | baby seat #4 → next to → baby #3 [0-2.86953s] | near | near |
| 4190655097 | adult #1 → in front of → cat #0 [1.45979-10.719s, 36.328-38.9973s] | petting; touching; in front of | – |
| 6827489358 | child #0 → next to → toy #1 [0.0667333-6.7067s, 7.44077-11.7117s, 11.9119-12.9796s] | approaches; moves away from; near; below | – |
| 4123915842 | adult #2 → touch → child #1 [0-0.133467s, 2.33567-4.13747s, 4.9049-18.2849s, 18.7187-19.8532s] | holding; looking at; behind | – |
| 4075791856 | adult #2 → behind → suitcase #4 [0-90s] | playing; looking at; performing with; near | in front of |
| 8313365386 | child #1 → next to → table #2 [6-8.875s] | looking at; touching | in front of; below |

**relation and triplet right**

| video | human relation | TRASER for this pair | reverse |
|---|---|---|---|
| 7416295940 | dog #1 → in front of → child #0 [60.06-73.073s] | in front of | approaches; pets; moves away from; plays with |
| 8968742990 | adult #3 → in front of → adult #1 [0-11.4583s] | in front of | – |
| 4626085492 | dog #0 → lean on → sofa #5 [0-8.67533s, 14.5479-19.386s] | on | – |
| 5586394125 | adult #2 → in front of → car #4 [0-14.0474s] | in front of | – |
| 3809031019 | adult #1 → next to → adult #4 [20.02-25.7924s] | next to | – |
| 4759861822 | adult #0 → next to → bat #8 [0.266933-10.5439s, 12.012-15.5489s, 19.4861-23.9239s] | holding; swinging; playing golf with; near | – |

