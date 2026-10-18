# Why does TRASER miss the relevant pairs? (pair experiment)

Relevant pair = a pair of objects that humans relate (ground truth) and that TRASER received. Code: `tools/interp/pairs_stage.py` (GPU) and `tools/interp/pairs_report.py` (this page). Ideas from *Are VLMs Seeing or Just Saying?* (swap the picture halfway, attention to the picture while writing, asking again as a new turn) and *Do Vision-Language Models Actually See?* (give the answer's structure as text to bypass seeing; easy-to-see things are found more often).

## The answer: why each missed pair was missed

![reasons](figs/pairs_reasons.png)

| dataset | tested missed pairs | A didn't see | B didn't choose | C stopped early | D habit |
|---|---|---|---|---|---|
| pvsg | 268 | 13% | 45% | 20% | 22% |
| vidor | 1171 | 4% | 15% | 46% | 36% |

How a pair gets its reason (first rule that fits): **C** it writes the pair when the list is re-opened, when its subject is started for it, or when asked again in a new turn · **D** it fills in the human word (top 5) also with the video hidden, and the video adds less than 1 nat · **B** it fills in the human word with the video, or the probe reads "related" from its vectors · **A** none of these.

## 1. Is the pair inside the model? (probe vs habit)

| dataset | stage | TRASER's vectors | object names only (habit) | both | tricky pairs* | vectors on tricky | habit on tricky |
|---|---|---|---|---|---|---|---|
| pvsg | lm_30 | 0.87 | 0.8224 | 0.8508 | 2088 (570 related) | 0.7437 | 0.5661 |
| vidor | lm_30 | 0.8195 | 0.5659 | 0.7833 | 6693 (3489 related) | 0.8137 | 0.5412 |

AUC: 0.5 = guessing, 1 = perfect. *Tricky pairs: the same two object names are related in some videos and not in others, so the names alone cannot tell. If TRASER's vectors beat the names there, it uses the video.

## 2. Give it the pair: does it fill in the right word?

We write `[subject, "` for it and score every relation word together with the human object. Human word (or an equivalent) in its top 5:

| dataset | pairs | with the video | video hidden | pair's objects hidden | picks the human object first (video / hidden) |
|---|---|---|---|---|---|
| pvsg | missed (268) | 63% | 57% | 57% | 37% / 25% |
| pvsg | written (131) | 73% | 70% | 70% | 53% / 45% |
| vidor | missed (1171) | 93% | 92% | 93% | 38% / 33% |
| vidor | written (741) | 96% | 95% | 96% | 50% / 47% |

Same answer with the video hidden = the word comes from habit. Good with the video but never written = it knew but did not choose.

## 3. Keep writing, and swap the video halfway

| dataset | videos | new relations when the list is re-opened | of them human pairs | missed pairs tested | come back: re-opened list | subject started for it | asked again (new turn) |
|---|---|---|---|---|---|---|---|
| pvsg | 51 | 394 | 45 | 268 | 9% | 12% | 3% |
| vidor | 300 | 1384 | 706 | 1171 | 15% | 32% | 18% |

![swap](figs/pairs_swap.png)


Swap: the visual contents of TRASER's two most-used objects are exchanged in the input after it has written k relations. Following the swapped video = it still looks; following its earlier text = it stopped looking (VisualSwap's finding).

| dataset | k | follows swapped video | follows old text | videos |
|---|---|---|---|---|
| pvsg | 0 | 9 | 32 | 51 |
| pvsg | 3 | 7 | 72 | 51 |
| pvsg | 8 | 3 | 79 | 51 |
| vidor | 0 | 104 | 233 | 300 |
| vidor | 3 | 55 | 346 | 269 |
| vidor | 8 | 38 | 229 | 165 |

## 4. Where does it look while writing?

![attention](figs/pairs_attention.png)

| dataset | relation no. | all video latents | the written object's latents | (if spread evenly) | answer so far | n |
|---|---|---|---|---|---|---|
| pvsg | 1-1 | 0.0403 | 0.0072 | 0.0624 | 0.5114 | 54 |
| pvsg | 2-3 | 0.0361 | 0.0053 | 0.0571 | 0.5576 | 108 |
| pvsg | 4-6 | 0.0324 | 0.0041 | 0.0591 | 0.5794 | 159 |
| pvsg | 7-10 | 0.0309 | 0.0043 | 0.0585 | 0.5888 | 198 |
| pvsg | 11-20 | 0.0268 | 0.0036 | 0.0559 | 0.6088 | 431 |
| pvsg | 21-40 | 0.0233 | 0.0025 | 0.0511 | 0.6285 | 402 |
| vidor | 1-1 | 0.0345 | 0.0134 | 0.1926 | 0.496 | 300 |
| vidor | 2-3 | 0.0281 | 0.01 | 0.1838 | 0.5444 | 585 |
| vidor | 4-6 | 0.0239 | 0.0074 | 0.161 | 0.5658 | 752 |
| vidor | 7-10 | 0.0216 | 0.0052 | 0.1252 | 0.5888 | 705 |
| vidor | 11-20 | 0.0191 | 0.0034 | 0.0855 | 0.6142 | 808 |
| vidor | 21-40 | 0.0178 | 0.0024 | 0.0529 | 0.6372 | 268 |

When it closes the list, attention to the objects of the pairs it missed:

| dataset | missed pairs' latents | (if spread evenly) | other latents | answer so far | n |
|---|---|---|---|---|---|
| pvsg | 0.0065 | 0.3106 | 0.0057 | 0.6796 | 33 |
| vidor | 0.0084 | 0.4482 | 0.0022 | 0.6332 | 299 |

## 5. Which relevant pairs are missed?

Miss rate in the lowest vs highest third of each fact (logistic-regression weight: + = more misses):

| dataset | fact | miss rate, low third | high third | weight |
|---|---|---|---|---|
| pvsg | time together | 70% | 63% | 0.498 |
| pvsg | gap | 69% | 50% | 0.072 |
| pvsg | touching | 71% | 55% | -0.164 |
| pvsg | size (subject) | 69% | 57% | 0.326 |
| pvsg | size (object) | 68% | 56% | -0.043 |
| pvsg | speed (subject) | 58% | 61% | 0.239 |
| pvsg | speed (object) | 52% | 66% | 0.022 |
| pvsg | tokens (subject) | 65% | 64% | -0.391 |
| pvsg | tokens (object) | 68% | 65% | -0.282 |
| pvsg | living (object) | 62% | 64% | 0.032 |
| pvsg | objects in video | 57% | 72% | 0.648 |
| pvsg | name pair is common | 62% | 67% | 0.242 |
| vidor | time together | 67% | 50% | -0.033 |
| vidor | gap | 47% | 70% | 0.124 |
| vidor | touching | 70% | 47% | -0.098 |
| vidor | size (subject) | 68% | 47% | 0.048 |
| vidor | size (object) | 62% | 55% | -0.036 |
| vidor | speed (subject) | 61% | 61% | -0.131 |
| vidor | speed (object) | 56% | 64% | 0.028 |
| vidor | tokens (subject) | 70% | 48% | -0.232 |
| vidor | tokens (object) | 63% | 56% | 0.011 |
| vidor | objects in video | 47% | 73% | 0.453 |
| vidor | action word | 64% | 41% | -0.192 |
| vidor | name pair is common | 56% | 64% | 0.194 |

**Caveats.** The human labels are incomplete, so some "unrelated" pairs are really related. Only a sample of missed pairs per video is tested (8 by default). The reasons are rules on these measurements, not certainties.
