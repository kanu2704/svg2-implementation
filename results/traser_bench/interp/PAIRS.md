# Why does TRASER miss the relevant pairs? (pair experiment)

Relevant pair = a pair of objects that humans relate (ground truth) and that TRASER received. Code: `tools/interp/pairs_stage.py` (GPU) and `tools/interp/pairs_report.py` (this page). Ideas from *Are VLMs Seeing or Just Saying?* (swap the picture halfway, attention to the picture while writing, asking again as a new turn) and *Do Vision-Language Models Actually See?* (give the answer's structure as text to bypass seeing; easy-to-see things are found more often).

## The answer: why each missed pair was missed

![reasons](figs/pairs_reasons.png)

| dataset | tested missed pairs | A didn't see | B didn't choose | C stopped early | D habit |
|---|---|---|---|---|---|
| pvsg | 107 | 15% | 44% | 22% | 19% |
| vidor | 244 | 5% | 18% | 36% | 42% |

How a pair gets its reason (first rule that fits): **C** it writes the pair when the list is re-opened, when its subject is started for it, or when asked again in a new turn · **D** it fills in the human word (top 5) also with the video hidden, and the video adds less than 1 nat · **B** it fills in the human word with the video, or the probe reads "related" from its vectors · **A** none of these.

## 1. Is the pair inside the model? (probe vs habit)

| dataset | stage | TRASER's vectors | object names only (habit) | both | tricky pairs* | vectors on tricky | habit on tricky |
|---|---|---|---|---|---|---|---|
| pvsg | lm_30 | 0.8531 | 0.8165 | 0.8026 | 722 (219 related) | 0.7143 | 0.4865 |
| vidor | lm_30 | 0.7468 | 0.5021 | 0.703 | 1542 (668 related) | 0.7394 | 0.4996 |

AUC: 0.5 = guessing, 1 = perfect. *Tricky pairs: the same two object names are related in some videos and not in others, so the names alone cannot tell. If TRASER's vectors beat the names there, it uses the video.

## 2. Give it the pair: does it fill in the right word?

We write `[subject, "` for it and score every relation word together with the human object. Human word (or an equivalent) in its top 5:

| dataset | pairs | with the video | video hidden | pair's objects hidden | picks the human object first (video / hidden) |
|---|---|---|---|---|---|
| pvsg | missed (107) | 59% | 60% | 55% | 37% / 25% |
| pvsg | written (51) | 80% | 72% | 71% | 41% / 35% |
| vidor | missed (244) | 92% | 91% | 91% | 36% / 32% |
| vidor | written (144) | 94% | 94% | 94% | 44% / 45% |

Same answer with the video hidden = the word comes from habit. Good with the video but never written = it knew but did not choose.

## 3. Keep writing, and swap the video halfway

| dataset | videos | new relations when the list is re-opened | of them human pairs | missed pairs tested | come back: re-opened list | subject started for it | asked again (new turn) |
|---|---|---|---|---|---|---|---|
| pvsg | 20 | 175 | 25 | 107 | 9% | 16% | 3% |
| vidor | 60 | 309 | 121 | 244 | 10% | 24% | 13% |

![swap](figs/pairs_swap.png)


Swap: the visual contents of TRASER's two most-used objects are exchanged in the input after it has written k relations. Following the swapped video = it still looks; following its earlier text = it stopped looking (VisualSwap's finding).

| dataset | k | follows swapped video | follows old text | videos |
|---|---|---|---|---|
| pvsg | 0 | 4 | 15 | 20 |
| pvsg | 3 | 0 | 27 | 20 |
| pvsg | 8 | 1 | 33 | 20 |
| vidor | 0 | 25 | 37 | 60 |
| vidor | 3 | 15 | 70 | 53 |
| vidor | 8 | 13 | 48 | 36 |

## 4. Where does it look while writing?

![attention](figs/pairs_attention.png)

| dataset | relation no. | all video latents | the written object's latents | (if spread evenly) | answer so far | n |
|---|---|---|---|---|---|---|
| pvsg | 1-1 | 0.0405 | 0.0074 | 0.0597 | 0.5075 | 23 |
| pvsg | 2-3 | 0.0359 | 0.0057 | 0.0571 | 0.5571 | 46 |
| pvsg | 4-6 | 0.0322 | 0.0039 | 0.0607 | 0.5814 | 68 |
| pvsg | 7-10 | 0.0304 | 0.0037 | 0.0574 | 0.5906 | 78 |
| pvsg | 11-20 | 0.0267 | 0.0032 | 0.0524 | 0.6135 | 161 |
| pvsg | 21-40 | 0.0221 | 0.0024 | 0.0518 | 0.6343 | 167 |
| vidor | 1-1 | 0.0354 | 0.0133 | 0.1819 | 0.4958 | 60 |
| vidor | 2-3 | 0.0282 | 0.0093 | 0.1737 | 0.5472 | 118 |
| vidor | 4-6 | 0.0239 | 0.0067 | 0.136 | 0.569 | 144 |
| vidor | 7-10 | 0.0219 | 0.0051 | 0.1093 | 0.5889 | 151 |
| vidor | 11-20 | 0.0193 | 0.0034 | 0.0817 | 0.617 | 205 |
| vidor | 21-40 | 0.0177 | 0.0021 | 0.0469 | 0.6442 | 108 |

When it closes the list, attention to the objects of the pairs it missed:

| dataset | missed pairs' latents | (if spread evenly) | other latents | answer so far | n |
|---|---|---|---|---|---|
| pvsg | 0.007 | 0.3357 | 0.0061 | 0.6824 | 14 |
| vidor | 0.0078 | 0.4111 | 0.0027 | 0.6368 | 60 |

## 5. Which relevant pairs are missed?

Miss rate in the lowest vs highest third of each fact (logistic-regression weight: + = more misses):

| dataset | fact | miss rate, low third | high third | weight |
|---|---|---|---|---|
| pvsg | time together | 65% | 68% | 0.469 |
| pvsg | gap | 63% | 56% | -0.016 |
| pvsg | touching | 63% | 63% | -0.091 |
| pvsg | size (subject) | 72% | 53% | 0.373 |
| pvsg | size (object) | 55% | 67% | 0.301 |
| pvsg | speed (subject) | 56% | 55% | 0.223 |
| pvsg | speed (object) | 59% | 50% | -0.206 |
| pvsg | tokens (subject) | 77% | 45% | -0.879 |
| pvsg | tokens (object) | 58% | 74% | -0.386 |
| pvsg | living (object) | 60% | 65% | 0.194 |
| pvsg | objects in video | 54% | 70% | 0.679 |
| pvsg | action word | 72% | 55% | -0.246 |
| pvsg | name pair is common | 58% | 65% | 0.053 |
| vidor | time together | 69% | 43% | -0.005 |
| vidor | gap | 46% | 62% | 0.023 |
| vidor | touching | 64% | 44% | -0.008 |
| vidor | size (subject) | 68% | 48% | 0.38 |
| vidor | size (object) | 64% | 49% | -0.123 |
| vidor | speed (subject) | 60% | 58% | -0.125 |
| vidor | speed (object) | 48% | 63% | -0.014 |
| vidor | tokens (subject) | 71% | 41% | -0.544 |
| vidor | tokens (object) | 64% | 50% | -0.026 |
| vidor | objects in video | 48% | 65% | 0.378 |
| vidor | action word | 61% | 40% | -0.177 |
| vidor | name pair is common | 53% | 65% | 0.269 |

## 6. Push: how close was it?

At the point where it writes the object number (after the human subject and word), the object's own direction is added in the middle layers. Share of pairs where the object becomes the first choice:

![push](figs/pairs_push.png)

| dataset | push sizes | missed human pairs | unrelated objects (control) |
|---|---|---|---|
| pvsg | [0.0, 0.05, 0.1, 0.2, 0.4] | [0.29, 0.387, 0.419, 0.484, 0.226] (n=31) | [0.032, 0.097, 0.194, 0.355, 0.065] (n=31) |
| vidor | [0.0, 0.05, 0.1, 0.2, 0.4] | [0.4, 0.433, 0.467, 0.533, 0.067] (n=30) | [0.0, 0.0, 0.04, 0.4, 0.08] (n=25) |

A missed human pair that becomes first with a smaller push than an unrelated object = it was close (B).

**Caveats.** The human labels are incomplete, so some "unrelated" pairs are really related. Only a sample of missed pairs per video is tested (8 by default). The reasons are rules on these measurements, not certainties.
