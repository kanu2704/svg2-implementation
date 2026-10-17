"""Fine-tuning TRASER's language model (Qwen2.5-VL-3B's decoder): shared pieces.

What is trained: TRASER = vision encoder + two resamplers (they build the input sequence) + the Qwen2.5-VL-3B
language model (it writes the answer). The vision part stays frozen; its output for each video is computed once
(tools/interp/encode_stage.py, the exact sequence TRASER's language model reads) and the language model is
trained on top of it with LoRA (small extra weights in every layer). TRASER gives the language model plain
positions 0..L-1 (tools/export_lm.py), so it is an ordinary Qwen2 decoder over the saved sequence.

The target answer for a training video is built from the human labels, in TRASER's own answer format:
    {"objects": [{"object 1": "floor"}, ...], "relationships": [[9, "holding", 14, [[24, 27]]], ...]}
Object k is the k-th object TRASER was given (its k-th mask column); times are indices of the ~1 fps frames
TRASER reads, [a, b] inclusive, as in its answers (bench_eval.pred_spans is the inverse). The attributes TRASER
writes for every object are left out: the human labels have none, and the scores do not use them.
"""
import json
import math
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent))
from interp import common as IC  # noqa: E402

REPO = HERE.parents[1]
OUT = REPO / "results" / "traser_bench" / "finetune"
STOP_IDS = [151645, 151643]          # <|im_end|>, <|endoftext|>
END_TEXT = "<|im_end|>"
LORA_TARGETS = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]


def log(msg, tag=""):
    import time
    print(f"{time.strftime('%H:%M:%S')} {tag}{msg}", flush=True)


# ----------------------------------------------------------------------------- videos
def pvsg_train_ids(anno, exclude=()):
    """PVSG training videos (all three sources), minus those whose VidOR id is in `exclude` (PVSG takes part of
    its videos from VidOR, so a VidOR test video can also be a PVSG training video)."""
    ids = [v for source in anno["split"] for v in anno["split"][source].get("train", [])]
    ex = set(exclude)
    return sorted(v for v in ids if v not in ex and v.split("_")[-1] not in ex)


def load_layout(work, ds, v):
    p = IC.work_paths(work, ds, v)
    return IC.read_json(p["layout"]) if p["layout"].exists() and p["embeds"].exists() else None


def load_embeds(work, ds, v, device, dtype):
    import torch
    return torch.load(IC.work_paths(work, ds, v)["embeds"], map_location="cpu").to(device, dtype=dtype)[None]


# ----------------------------------------------------------------------------- target answer from the human labels
def to_index(spans, scale, n_frames):
    """Human spans in seconds [a, b) -> TRASER's frame-index spans [i, j] inclusive (merged)."""
    out = []
    for a, b in sorted(spans):
        i = min(n_frames - 1, max(0, int(math.floor(a / scale + 1e-6))))
        j = min(n_frames - 1, max(i, int(math.ceil(b / scale - 1e-6)) - 1))
        if out and i <= out[-1][1] + 1:
            out[-1][1] = max(out[-1][1], j)
        else:
            out.append([i, j])
    return out


def given_relations(gt, layout):
    """The human relations between objects TRASER was given, as (k_subj, word, k_obj, index spans), merged per
    (subject, word, object). Object numbers are TRASER's (1..n)."""
    import bench_eval as E
    gt = E.merge_occurrences(gt)
    k_of = {g: k + 1 for k, g in enumerate(layout["gt_ids"])}
    k_of[-1] = -1
    unit = gt.get("time_unit", "seconds")
    scale = 1.0 if unit == "index" else layout["duration_s"] / max(1, layout["sampled_frames"])
    n = max(1, layout["sampled_frames"])
    rels = {}
    for r in gt["relations"]:
        if r["subj"] in k_of and r["obj"] in k_of:
            key = (k_of[r["subj"]], str(r["pred"]).replace("_", " ").strip(), k_of[r["obj"]])
            spans = [[a, b] for a, b in r["spans"]] if unit != "index" else [[a, b + 1] for a, b in r["spans"]]
            rels.setdefault(key, []).extend(spans)
    out = [(s, p, o, to_index(sp, scale, n)) for (s, p, o), sp in rels.items()]
    return sorted(out, key=lambda r: (r[3][0][0] if r[3] else 0, r[0], r[2], r[1]))


def target_text(gt, layout):
    name = {o["gt_id"]: str(o["name"]).replace("_", " ").strip() for o in gt["objects"]}
    objects = [{f"object {k + 1}": name.get(g, "object")} for k, g in enumerate(layout["gt_ids"])]
    rels = [[s, p, o, sp] for s, p, o, sp in given_relations(gt, layout)]
    return json.dumps({"objects": objects, "relationships": rels})


# ----------------------------------------------------------------------------- reward (GRPO) and quick scores
WORD = re.compile(r"[a-z]+")
STOP = {"a", "an", "the", "is", "are", "of", "to", "with"}


def stem(w):
    for suf in ("ing", "es", "s", "ed"):
        if len(w) > len(suf) + 2 and w.endswith(suf):
            w = w[: -len(suf)]
            if suf == "ing" and len(w) > 2 and w[-1] == w[-2]:
                w = w[:-1]                       # sitting -> sit
            break
    return w


def word_key(label):
    import bench_eval as E
    return " ".join(stem(w) for w in WORD.findall(E.norm(label)) if w not in STOP)


class WordMatch:
    """Relation words: the same after normalising + stemming (holds / holding), or judged "not a mismatch" in the
    judge's cache (results/traser_bench/judge_cache.json; no API calls here)."""
    def __init__(self, cache=None):
        import bench_eval as E
        p = Path(cache or E.RESULTS / "judge_cache.json")
        self.cache = json.load(open(p)) if p.exists() else {}

    def __call__(self, ref, hyp):
        import bench_eval as E
        if word_key(ref) == word_key(hyp):
            return True
        c = self.cache.get(E.Judge.key("relation", ref, hyp))
        return c is not None and c != "mismatch"


def f1(p, r):
    return 0.0 if p + r == 0 else 2 * p * r / (p + r)


def answer_scores(text, gold, match, thr=0.1):
    """gold = given_relations(...). Scores of one answer against the human relations (TRASER's object numbers,
    frame-index times): triplet = same pair + matching word + time IoU > thr; pair = the pair is mentioned."""
    import bench_eval as E
    pred = E.parse_prediction(text)["relations"]
    to_s = lambda sp: [[a, b + 1] for a, b in sp]  # noqa: E731
    gold_pairs = {(s, o) for s, _, o, _ in gold}
    pred_pairs = {(s, o) for s, _, o, _ in pred}
    hit_gold, hit_pred = set(), set()
    for gi, (s, w, o, sp) in enumerate(gold):
        for pi, (ps, pw, po, psp) in enumerate(pred):
            if (ps, po) == (s, o) and match(w, pw) and E.tiou(to_s(sp), to_s(psp)) > thr:
                hit_gold.add(gi)
                hit_pred.add(pi)
    rec = len(hit_gold) / len(gold) if gold else 0.0
    prec = len(hit_pred) / len(pred) if pred else 0.0
    prec_pair = len(pred_pairs & gold_pairs) / len(pred_pairs) if pred_pairs else 0.0
    rec_pair = len(pred_pairs & gold_pairs) / len(gold_pairs) if gold_pairs else 0.0
    return {"triplet_recall": rec, "triplet_precision": prec, "triplet_f1": f1(prec, rec),
            "pair_recall": rec_pair, "pair_precision": prec_pair, "pair_f1": f1(prec_pair, rec_pair),
            "relations": len(pred)}


def reward(text, gold, match, ended=True):
    """GRPO reward: triplet F1 + 0.5 x pair F1 (F1, not recall, so listing every pair does not pay), 0 for an
    answer that never closes its JSON."""
    if not ended:
        return 0.0, {}
    sc = answer_scores(text, gold, match)
    return sc["triplet_f1"] + 0.5 * sc["pair_f1"], sc


# ----------------------------------------------------------------------------- model
def load_lm(path, dtype="bfloat16", device=None, train=False):
    import torch
    from transformers import AutoTokenizer, Qwen2ForCausalLM
    if torch.cuda.is_available() and torch.cuda.get_device_capability()[0] < 8:
        import transformers.integrations.sdpa_attention as sdpa     # see run_traser.avoid_math_attention
        sdpa.use_gqa_in_sdpa = lambda *a, **k: False
    device = device or ("cuda" if torch.cuda.is_available() else "cpu")
    model = Qwen2ForCausalLM.from_pretrained(path, torch_dtype=getattr(torch, dtype), attn_implementation="sdpa").to(device)
    tok = AutoTokenizer.from_pretrained(path)
    model.train(train)
    return model, tok


def add_lora(model, r=16, alpha=32, dropout=0.05):
    import torch
    from peft import LoraConfig, get_peft_model
    model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})
    model.config.use_cache = False
    model = get_peft_model(model, LoraConfig(r=r, lora_alpha=alpha, lora_dropout=dropout, target_modules=LORA_TARGETS,
                                             task_type="CAUSAL_LM"))
    for p in model.parameters():
        if p.requires_grad:
            p.data = p.data.to(torch.float32)       # LoRA weights in float32, the frozen model in bfloat16
    return model


def merge_and_save(model, tok, src_lm, out):
    """LoRA folded into the weights -> a plain Qwen2 folder like tools/export_lm.py's (generate.py loads it)."""
    import shutil
    out = Path(out)
    merged = model.merge_and_unload()
    merged = merged.to(next(p for p in merged.parameters()).dtype)
    merged.config.use_cache = True
    merged.save_pretrained(out, safe_serialization=True)
    tok.save_pretrained(out)
    for name in ("generation_config.json", "chat_template.jinja", "chat_template.json"):
        if (Path(src_lm) / name).exists():
            shutil.copyfile(Path(src_lm) / name, out / name)
    return out


def hidden(model, x):
    """Last hidden states of the decoder for inputs_embeds x [1, L, D] (works with and without LoRA)."""
    base = model.get_base_model() if hasattr(model, "get_base_model") else model
    return base.model(inputs_embeds=x, use_cache=False).last_hidden_state[0]


def token_logprobs(model, h, targets):
    """log P(target) for rows h [T, D] (one row per target), in float32."""
    import torch
    base = model.get_base_model() if hasattr(model, "get_base_model") else model
    logits = base.lm_head(h).float()
    return torch.log_softmax(logits, -1).gather(1, targets[:, None])[:, 0]
