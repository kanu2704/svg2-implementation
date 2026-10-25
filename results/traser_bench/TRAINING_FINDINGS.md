# What TRASER's training teaches: 4 findings

TRASER = Qwen2.5-VL-3B + training. The training changes three things: the language model (fine-tuned), two resamplers
(small networks that turn each object's video tokens into 32 tokens, per time window and over its whole trajectory) and
special tokens that mark each object. Training data: SVG2, LV-VIS, OVIS, VIPSeg, VidOR, VidVRD (not PVSG).

Two experiments give the evidence:
- **Qwen-7B experiment:** TRASER's exact pipeline (same frames, masks, tokens, prompt) with an untrained Qwen2.5-VL-7B
  instead of TRASER's trained model (`results/qwen7b_bench/`).
- **Experiment 2:** for every human pair, we point TRASER at the pair and let it pick the relation word
  (`results/traser_bench/interp/PAIRS_LENIENT.md`). Setting 0 = its own answer; setting 1 = asked about the pair with
  nothing else written; setting 2 = asked after its own answer.

Judge: every word judged by one model, Nemotron 3.5 Super (`nvidia/nemotron-3.5-super-vl-120b-a12b`), with the paper's
lenient setup (`results/judge_rerun/nvidia__nemotron-3.5-super-vl-120b-a12b/`). It is stricter than the earlier judge
(Kimi K3): of the words Kimi K3 accepted it accepts 63%, of those Kimi K3 rejected it rejects 98%. The numbers drop a
little; every finding below holds with both judges.

---

## 1. It learns to link each object number to the right object in the video

**In one line:** TRASER's answer talks about "object 1", "object 2", ...; training teaches it which object in the video
each number is. Without that training, a model sees what is in the video but mixes up which number is which object.

**What we did:** gave the untrained Qwen-7B the same input as TRASER and checked the name it gives each object (exact
names, no judge).

**What we found:**

| | object gets **its own** human name | object gets **another** object's human name |
|---|---|---|
| PVSG: TRASER | 29% | 11% |
| PVSG: Qwen-7B | 3% | **20%** |
| SVG2test: TRASER | 27% | 15% |
| SVG2test: Qwen-7B | 7% | **25%** |

**What it means:** Qwen-7B names things that are in the video (a "cup", a "table"), but puts the name on the wrong
object number more often than on the right one. TRASER does the opposite. The link "object number ↔ that object's
video tokens" is learned in training.

---

## 2. It learns which pairs of objects to write about

**In one line:** an answer can only get a relation right if it mentions that pair of objects. Training teaches TRASER
to list the kind of pairs humans annotate; the untrained model lists very few of them.

**What we found:** share of the human pairs (between objects the model was given) that the answer mentions at all,
with any word:

| | PVSG | VidOR | SVG2test |
|---|---|---|---|
| TRASER | 36% | 41% | 38% |
| Qwen-7B (untrained) | **4%** | **18%** | **8%** |

**What it means:** most of the untrained model's relations are lost before any relation word is chosen: the pair is
simply not in its answer. Together with finding 1, this is why its relation recall is almost 0 (0.0 / 1.5 / 1.5%
against TRASER's 12.9 / 10.7 / 24.8%), the same as the paper's untrained 3B baseline (0.1 / 0.4 / 0.3%).

---

## 3. It learns each dataset's naming habits

**In one line:** on VidOR, TRASER picks the relation word mostly from the object names, hardly from what it sees: it
learned how VidOR usually labels such pairs.

**Background:** each dataset names relations its own way. VidOR uses a fixed list of about 50 words (`next_to`,
`in_front_of`, `behind`, `watch`, `hold`, ...); PVSG and SVG2 use other words. VidOR is in TRASER's training data.

**What we did (experiment 2, setting 1):** asked TRASER for the word of every human pair, once with the real video and
once with the video blanked (all visual tokens set to zero). Its object list ("object 1: adult", "object 4: car") is
still there as text.

**What we found** (1st choice right):

| | with video | video blanked | the video adds |
|---|---|---|---|
| PVSG | 54% | 46% | 8 points |
| SVG2test | 53% | 41% | 12 points |
| VidOR | 22% | 20% | **only 2 points** |

(With the earlier judge, Kimi K3, VidOR was even better blanked: 33% vs 29%.)

**What it means:** on PVSG and SVG2test it uses the video. On VidOR, the object names alone ("adult" and "car") are
enough for it to guess VidOR's usual word (`next_to`) almost as well as with the video. Part of what it learned is the
labelling habits of its training datasets. The paper calls TRASER open-vocabulary; on a new dataset with other naming
habits it may do worse. This fits Table 2 (TRASER scores higher on SVG2test, from its training data, than on PVSG, not
in it), but is not a proof: PVSG also has other kinds of video (first-person, kitchens).

---

## 4. It knows more relations than it writes

**In one line:** pointed at a pair, TRASER usually knows a right word; in its own answer it leaves out most pairs. The
weak spot is which pairs it writes, not the relation words.

**What we did (experiment 2):** on the same human pairs, compared its own answer (setting 0) with asking it about each
pair, with nothing else written (setting 1, the real video).

**What we found:**

| | setting 0: its own answer has the pair with a right word | setting 1: asked about the pair, 1st choice right | setting 1, only the pairs it left out of its answer |
|---|---|---|---|
| PVSG | 202 of 739 (27%) | **399 of 739 (54%)** | 220 of 476 (46%) |
| SVG2test | 788 of 2,519 (31%) | **1,338 of 2,519 (53%)** | 708 of 1,534 (46%) |
| VidOR | 2,615 of 11,157 (23%) | 2,469 of 11,157 (22%) | 1,118 of 6,528 (17%) |

(Earlier judge, Kimi K3: PVSG 30% → 61%, SVG2test 33% → 62%.)

**What it means:** on PVSG and SVG2test it picks a right word about twice as often when asked as it writes one in its
own answer (PVSG 54% vs 27%, SVG2test 53% vs 31%), and it knows a right word for almost half of the pairs it left out.
Its knowledge is there; its answer leaves much of it out, because it writes only about a third of the human pairs. On
VidOR the fresh question does not help (22% vs 23%), but asked after its own answer (setting 2) it gets 44% of the
left-out pairs right (2,857 of 6,528), likely helped by the words already in its own list.

**Fairness note:** when asked, it picks from a fixed list of words (66 / 55 / 74 per dataset) that always includes the
human word. That is easier than writing freely, but its 1st choice still has to beat all the other words.

---

## In short

TRASER's training mainly teaches it to **connect each object number to the right object** and to **write a
dataset-style list of pairs**, including the datasets' naming habits. For many pairs it already knows a right relation
word but does not write them: **the bottleneck is choosing which pairs to write, not knowing the relation.**

**Caveat:** in the Qwen-7B experiment, TRASER's trained resamplers were also replaced (by plain averaging, as they only
fit the 3B model), and Qwen is bigger (7B vs 3B). Findings 1 and 2 therefore compare TRASER's whole training, not the
language-model fine-tuning alone.
