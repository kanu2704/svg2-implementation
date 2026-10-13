"""Interpretability, stage 2 (GPU, TRASER's language model): experiments on the saved input sequences.

TRASER's language model is an ordinary Qwen2 decoder over the arranged sequence (plain positions 0..L-1), so it
is loaded alone from tools/export_lm.py's export (the checkpoint's own weights; same outputs, checked in p0) and
fed the sequences tools/interp/encode_stage.py saved. Every experiment works on TRASER's own answer (the saved
predictions), read back token by token ("teacher forcing"): how likely the model finds each part of it, and how
that changes when the input is changed.

Phases (one JSON per video and phase under results/traser_bench/interp/raw/<phase>/<dataset>/<video>.json):
  p0   check: the exported model + saved input reproduce TRASER's answer (greedy tokens, teacher-forced argmax)
  p1   hidden states per object (mean over its latents, and its last token) at every layer, per window at some
       layers -> <work>/<video>.hidden.npz for the probes (tools/interp/probe.py)
  p2a  "knows but doesn't say": after TRASER's last relation, start one more with a human subject and score
       every subject / relation word / object; also how likely it was to stop after each relation
  p2b  interventions: blank all / OTR / TWR latents, blank one object, reverse the time labels, blank the
       windows of a relation; change in log-probability of each relation's subject, word, object and times
  p2c  activation patching: blank an object, put back its clean hidden states one layer at a time
       (at its latents, or at the position that writes the object number); which layers restore it
  p3   attention (short inputs): where the tokens that write times, object numbers and relation words look

    CUDA_VISIBLE_DEVICES=0 python3 tools/interp/lm_stage.py --lm /kaggle/tmp/traser_lm \
        --work /kaggle/tmp/interp_work --shard 0 --nshards 2
"""
import argparse
import collections
import contextlib
import json
import math
import random
import sys
import time
import traceback
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent))
from interp import common as C  # noqa: E402

PHASES = ["p0", "p1", "p2b", "p2a", "p2c", "p3"]
STOP_IDS = [151645, 151643]
K_ROWS = 16              # log-prob rows kept at the end of a scored context (tokenization can merge across it)


def log(msg, tag=""):
    print(f"{time.strftime('%H:%M:%S')} {tag}{msg}", flush=True)


# ----------------------------------------------------------------------------- model
class LM:
    def __init__(self, path, dtype="float16", device=None):
        import torch
        from transformers import AutoTokenizer, Qwen2ForCausalLM
        self.torch = torch
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        if torch.cuda.is_available() and torch.cuda.get_device_capability()[0] < 8:
            import transformers.integrations.sdpa_attention as sdpa      # see run_traser.avoid_math_attention
            sdpa.use_gqa_in_sdpa = lambda *a, **k: False
        self.model = Qwen2ForCausalLM.from_pretrained(path, torch_dtype=getattr(torch, dtype),
                                                      attn_implementation="sdpa").to(self.device).eval()
        self.model.requires_grad_(False)           # no gradients anywhere in stage 2
        torch.set_grad_enabled(False)
        self.dtype = self.model.dtype
        self.tok = AutoTokenizer.from_pretrained(path)
        self.emb = self.model.get_input_embeddings()
        self.W = self.model.lm_head.weight
        self.layers = self.model.model.layers
        self.n_layers = len(self.layers)

    def encode(self, text):
        return self.tok(text, add_special_tokens=False)["input_ids"]

    def encode_offsets(self, text):
        if getattr(self.tok, "is_fast", False):
            enc = self.tok(text, add_special_tokens=False, return_offsets_mapping=True)
            return enc["input_ids"], [tuple(o) for o in enc["offset_mapping"]]
        ids = self.encode(text)                    # slow tokenizer: offsets from decoding growing prefixes
        offs, prev = [], 0
        for i in range(len(ids)):
            end = len(self.tok.decode(ids[:i + 1]))
            offs.append((prev, end))
            prev = end
        return ids, offs

    def embed(self, ids):
        torch = self.torch
        return self.emb(torch.tensor([ids], device=self.device, dtype=torch.long))

    def body(self, x, cache=None):
        out = self.model.model(inputs_embeds=x, past_key_values=cache, use_cache=cache is not None)
        return out.last_hidden_state[0]

    def logprob_rows(self, h):
        torch = self.torch
        return torch.log_softmax(torch.nn.functional.linear(h, self.W).float(), dim=-1)

    def token_logprobs(self, h, targets, chunk=256):
        torch = self.torch
        out = []
        for c in range(0, len(targets), chunk):
            rows = self.logprob_rows(h[c:c + chunk])
            t = torch.tensor(targets[c:c + chunk], device=rows.device)
            out.append(rows.gather(1, t[:, None])[:, 0].cpu())
            del rows
        return torch.cat(out).numpy() if out else np.zeros(0, np.float32)

    def teacher_force(self, inp, ids, hooks=()):
        """log P(ids[t] | input, ids[:t]) for every answer token; inp [1, L, D]."""
        torch = self.torch
        x = torch.cat([inp, self.embed(ids)], 1) if ids else inp
        with torch.no_grad(), attach(hooks):
            h = self.body(x)
        L = inp.shape[1]
        return self.token_logprobs(h[L - 1:L - 1 + len(ids)], ids)


@contextlib.contextmanager
def attach(hooks):
    handles = [m.register_forward_hook(f) for m, f in hooks]
    try:
        yield
    finally:
        for h in handles:
            h.remove()


def layer_out(output):
    return output[0] if isinstance(output, tuple) else output


def replace_out(output, new):
    return (new,) + tuple(output[1:]) if isinstance(output, tuple) else new


class Context:
    """Input sequence + an answer text so far, with the model's cache; can move to any other text (shares the
    common token prefix) and score continuations exactly: log P(cont | text), with the tokenization of
    text + cont (tokens can merge across the boundary; the boundary's own log-prob is taken out)."""

    def __init__(self, lm, inp):
        from transformers import DynamicCache
        self.lm, self.L = lm, inp.shape[1]
        self.cache = DynamicCache()
        with lm.torch.no_grad():
            h = lm.body(inp, self.cache)
        self.ids, self.text = [], ""
        self.rows = {0: lm.logprob_rows(h[-1:])[0]}

    def _run(self, ids, first_index):
        """Append ids (answer tokens first_index...) to the cache; keep rows for the last K_ROWS tokens."""
        with self.lm.torch.no_grad():
            h = self.lm.body(self.lm.embed(ids), self.cache)
        keep_from = max(0, len(ids) - K_ROWS - 1)
        rows = self.lm.logprob_rows(h[keep_from:])
        for j in range(keep_from, len(ids)):
            self.rows[first_index + j + 1] = rows[j - keep_from]

    def goto(self, text):
        new = self.lm.encode(text)
        cl = 0
        while cl < min(len(new), len(self.ids)) and new[cl] == self.ids[cl]:
            cl += 1
        if cl < len(self.ids):
            self.cache.crop(self.L + cl)
            self.rows = {t: r for t, r in self.rows.items() if t <= cl}
        if len(new) > cl:
            self._run(new[cl:], cl)
        self.ids, self.text = new, text
        need = [t for t in range(max(0, len(new) - K_ROWS), len(new) + 1) if t not in self.rows]
        if need:                                  # rows lost when cropping: recompute the tail
            t0 = max(min(need) - 1, 0)
            self.cache.crop(self.L + t0)
            self.rows = {t: r for t, r in self.rows.items() if t <= t0}
            self._run(new[t0:], t0)
        return self

    def score(self, cont, bound=None):
        """(log P(cont | text), exact). With bound: stops at the first token if that already falls below it."""
        joint = self.lm.encode(self.text + cont)
        cl = 0
        while cl < min(len(joint), len(self.ids)) and joint[cl] == self.ids[cl]:
            cl += 1
        if cl < len(self.ids) - K_ROWS or not joint[cl:]:
            return None, False
        base = sum(float(self.rows[t][self.ids[t]]) for t in range(cl, len(self.ids)))
        new = joint[cl:]
        lp = float(self.rows[cl][new[0]]) - base
        if bound is not None and lp < bound:
            return lp, False
        if len(new) > 1:
            torch = self.lm.torch
            if cl < len(self.ids):
                self.cache.crop(self.L + cl)
            with torch.no_grad():
                h = self.lm.body(self.lm.embed(new[:-1]), self.cache)
            lp += float(self.lm.token_logprobs(h, new[1:]).sum())
            self.cache.crop(self.L + cl)
            if cl < len(self.ids):                # restore the text's own tail
                with torch.no_grad():
                    self.lm.body(self.lm.embed(self.ids[cl:]), self.cache)
        return lp, True

    def rank(self, candidates, targets, top=5, max_rank=20):
        """Exact ranks of each target text among the candidates (+ the targets), their log-probs, and the exact
        top list. log P(cont) <= log P(its first token), so candidates whose first token is already below every
        target and below the current top list are never scored in full."""
        scored = {}
        for t in targets:
            lp, ok = self.score(t)
            if ok:
                scored[t] = lp
        if not scored:
            return None
        bounds = []
        for c in candidates:
            if c in scored:
                continue
            b, _ = self.score(c, bound=float("inf"))         # first-token log-prob only
            if b is not None:
                bounds.append((b, c))
        bounds.sort(reverse=True)
        floor = min(scored.values())
        for b, c in bounds:
            ranked = sorted(scored.values(), reverse=True)
            kth = ranked[top - 1] if len(ranked) >= top else -float("inf")
            if b < floor and b < kth:
                break
            if all(sum(v > scored[t] for v in scored.values()) > max_rank for t in scored) and b < kth:
                break
            lp, ok = self.score(c)
            if ok:
                scored[c] = lp
        cand_set = set(candidates)
        best = sorted(((c, v) for c, v in scored.items() if c in cand_set or c == targets[0]), key=lambda x: -x[1])[:top]
        out = {}
        for t in targets:
            if t in scored:
                above = sum(v > scored[t] for c, v in scored.items() if c != t and c in cand_set)
                out[t] = {"rank": min(above + 1, max_rank + 1), "lp": round(scored[t], 3)}
        return {"targets": out, "top": [[c, round(v, 3)] for c, v in best]}


# ----------------------------------------------------------------------------- inputs
def blank(inp, positions):
    x = inp.clone()
    if positions:
        x[0, positions] = 0
    return x


def relabel(lm, inp, layout, mapping):
    """The input with each window label replaced by the label of window mapping[w] (lengths may change)."""
    torch = lm.torch
    segs = sorted((w["label"][0], w["label"][1], w["w"]) for o in layout["objects"] for w in o["windows"])
    pieces, last = [], 0
    for a, b, w in segs:
        t = mapping.get(w, w)
        pieces += [inp[:, last:a], lm.embed(lm.encode(f"<{t * C.WINDOW_S} - {(t + 1) * C.WINDOW_S} sec>"))]
        last = b
    pieces.append(inp[:, last:])
    return torch.cat(pieces, 1)


def answer_tokens(lm, text, max_tokens):
    ids, offs = lm.encode_offsets(text)
    return ids[:max_tokens], offs[:max_tokens]


def relation_groups(text, offs):
    """Per relation fully inside the (cut) tokens: token indices of subject, word, object, times."""
    out = []
    n = len(offs)
    end = offs[-1][1] if offs else 0
    for i, r in enumerate(C.answer_relations(text)):
        if r["range"][1] > end:
            break
        g = {"s": C.tokens_in(offs, *r["s_range"]), "pred": C.tokens_in(offs, *r["pred_range"]),
             "o": C.tokens_in(offs, *r["o_range"]), "time": [t for a, b in r["time_ranges"] for t in C.tokens_in(offs, a, b)]}
        if all(g.values()) and max(max(v) for v in g.values()) < n:
            out.append({"i": i, "s_k": r["s"], "o_k": r["o"], "pred": r["pred"], "spans": r["spans"], "tok": g})
    return out


def group_sums(lp, rels):
    return [{k: round(float(lp[v].sum()), 4) for k, v in r["tok"].items()} for r in rels]


# ----------------------------------------------------------------------------- per-video data
class Video:
    def __init__(self, ds, v, work, results, max_answer_tokens, lm):
        import torch
        p = C.work_paths(work, ds, v)
        self.ds, self.v, self.paths = ds, v, p
        self.layout = C.read_json(p["layout"])
        self.inp = torch.load(p["embeds"]).to(lm.device, dtype=lm.dtype)[None]
        self.text = Path(results, ds, "preds", f"{v}.json").read_text()
        self.stats = C.read_json(Path(results, ds, "preds", f"{v}.stats.json"), {})
        self.gt = C.read_json(Path(results, ds, "gt", f"{v}.json"))
        self.ids, self.offs = answer_tokens(lm, self.text, max_answer_tokens)
        self.cut_text = self.text[:self.offs[-1][1]] if self.offs else ""
        self.rels = relation_groups(self.text, self.offs)
        self.n = len(self.layout["objects"])
        self.k_of_gid = {g: k + 1 for k, g in enumerate(self.layout["gt_ids"])}
        self.same = bool(self.layout.get("same_objects_as_answer", True))


# ----------------------------------------------------------------------------- p0
def p0_check(lm, V, n_tokens=300):
    torch = lm.torch
    with torch.no_grad():
        g = lm.model.generate(inputs_embeds=V.inp, attention_mask=torch.ones(V.inp.shape[:2], dtype=torch.long, device=lm.device),
                              max_new_tokens=n_tokens, do_sample=False, repetition_penalty=1.05,
                              eos_token_id=STOP_IDS, pad_token_id=STOP_IDS[1])
    gen = g[0].tolist()
    ref = V.ids[:n_tokens]
    same = 0
    while same < min(len(gen), len(ref)) and gen[same] == ref[same]:
        same += 1
    x = torch.cat([V.inp, lm.embed(V.ids)], 1)
    with torch.no_grad():
        h = lm.body(x)
    L = V.inp.shape[1]
    arg = []
    for c in range(0, len(V.ids), 256):
        arg += (torch.nn.functional.linear(h[L - 1 + c:L - 1 + min(c + 256, len(V.ids))], lm.W).argmax(-1)).tolist()
    agree = float(np.mean([a == b for a, b in zip(arg, V.ids)])) if V.ids else None
    return {"greedy_same_prefix": same, "compared": len(ref), "teacher_forced_argmax_agreement": round(agree, 4),
            "answer_tokens_used": len(V.ids), "generated_start": lm.tok.decode(gen[:60])}


# ----------------------------------------------------------------------------- p1
def win_layers(n_layers):
    return sorted({round(x) for x in np.linspace(0, n_layers, 7)})


def p1_hidden(lm, V):
    import torch
    lay = V.layout
    obj_pos = [torch.tensor(C.latent_positions(lay, o["k"]), device=lm.device) for o in lay["objects"]]
    end_pos = torch.tensor([o["block"][1] - 1 for o in lay["objects"]], device=lm.device)
    W = lay["n_windows"]
    wl = win_layers(lm.n_layers)
    win_pos = [[(o["k"] - 1, w["w"], torch.tensor(list(range(*w["twr"])), device=lm.device))
                for w in o["windows"] if w["w"] < W] for o in lay["objects"]]
    n, D = len(obj_pos), V.inp.shape[-1]
    obj_mean = np.zeros((n, lm.n_layers + 1, D), np.float16)
    obj_end = np.zeros((n, lm.n_layers + 1, D), np.float16)
    win = np.zeros((n, W, len(wl), D), np.float16)

    def take(H, layer):
        for i, idx in enumerate(obj_pos):
            obj_mean[i, layer] = H[idx].float().mean(0).cpu().numpy()
        obj_end[:, layer] = H[end_pos].float().cpu().numpy()
        if layer in wl:
            j = wl.index(layer)
            for group in win_pos:
                for i, w, idx in group:
                    win[i, w, j] = H[idx].float().mean(0).cpu().numpy()

    take(V.inp[0], 0)
    hooks = [(layer, (lambda l: lambda m, a, out: take(layer_out(out)[0], l + 1))(li)) for li, layer in enumerate(lm.layers)]
    with torch.no_grad(), attach(hooks):
        lm.body(V.inp)
    tmp = V.paths["hidden"].with_name(V.paths["hidden"].name + ".part.npz")
    np.savez_compressed(tmp, obj_mean=obj_mean, obj_end=obj_end, win=win, win_layers=np.array(wl))
    tmp.replace(V.paths["hidden"])
    return {"objects": n, "layers": lm.n_layers + 1, "window_layers": wl}


# ----------------------------------------------------------------------------- p2a
def human_relations(V, judge):
    """Human relations of this video with TRASER's numbers and whether TRASER wrote the pair / the word."""
    import bench_eval as E
    gt, pred, st = E.load_video(V.ds, V.v)
    _, name, pname, by_pair = E.video_pairs(gt, pred, st)
    out = []
    for r in gt["relations"]:
        s, o = r["subj"], r["obj"]
        sk = -1 if s == -1 else V.k_of_gid.get(s)
        ok_ = -1 if o == -1 else V.k_of_gid.get(o)
        if sk is None or ok_ is None:
            continue
        cands = by_pair.get((s, o), [])
        word_ok = any(E.is_right(judge.category("relation", r["pred"], p), "lenient") for p, _ in cands)
        out.append({"s": s, "o": o, "s_k": sk, "o_k": ok_, "pred": r["pred"], "pair_written": bool(cands),
                    "reverse_written": (o, s) in by_pair, "word_right": word_ok})
    return out


def vocabulary(ds, results, n=60):
    """Candidate relation words: the n most common human words and the n most common TRASER words of the dataset."""
    import bench_eval as E
    hw, tw = collections.Counter(), collections.Counter()
    for v in C.answered(ds, results):
        g = C.read_json(Path(results, ds, "gt", f"{v}.json"))
        hw.update(r["pred"] for r in g["relations"])
        tw.update(r[1] for r in E.parse_prediction(Path(results, ds, "preds", f"{v}.json").read_text())["relations"])
    words, seen = [], set()
    for w, _ in hw.most_common(n) + tw.most_common(n):
        if w.lower() not in seen and '"' not in w and "\\" not in w:
            seen.add(w.lower())
            words.append(w)
    return words, [w for w, _ in hw.most_common(n)]


def p2a_forced(lm, V, judge, vocab, human_vocab, n_missed=10, n_written=5, seed=0):
    if not V.same:
        return {"skipped": "objects differ from the saved run"}
    end = C.list_end(V.text)
    if end is None:
        return {"skipped": "answer cut off (no end of the relation list)"}
    rng = random.Random(seed)
    prefix = V.text[:end]
    has_rel = bool(C.answer_relations(V.text))
    ctx = Context(lm, V.inp)
    ctx.goto(prefix)
    stop_end, _ = ctx.score("]}")
    cont_end, _ = ctx.score(", [" if has_rel else "[")
    # stop vs continue after each of TRASER's relations
    stops = []
    for r in C.answer_relations(V.text)[:40]:
        ctx.goto(V.text[:r["range"][1]])
        a, _ = ctx.score("]}")
        b, _ = ctx.score(", [")
        if a is not None and b is not None:
            stops.append(round(1 / (1 + math.exp(b - a)), 4))
    hum = human_relations(V, judge)
    missed = [h for h in hum if not h["pair_written"]]
    written = [h for h in hum if h["pair_written"] and h["word_right"]]
    pick = [("missed", h) for h in rng.sample(missed, min(n_missed, len(missed)))] + \
           [("written", h) for h in rng.sample(written, min(n_written, len(written)))]
    objs = list(range(1, V.n + 1))
    open_text = prefix + (", [" if has_rel else "[")
    out = []
    for kind, h in pick:
        others = [k for k in objs if k not in (h["s_k"], h["o_k"])]
        ctrl_s = rng.choice(others) if others else None
        ctrl_w = rng.choice([w for w in human_vocab if w.lower() != h["pred"].lower()] or [None])
        ctrl_o = rng.choice(others) if others else None
        ctx.goto(open_text)
        s_t, s_c = f'{h["s_k"]}, "', (f'{ctrl_s}, "' if ctrl_s else None)
        subj = ctx.rank([f'{k}, "' for k in objs + [-1]], [t for t in (s_t, s_c) if t])
        ctx.goto(open_text + s_t)
        w_t, w_c = f'{h["pred"]}", ', (f'{ctrl_w}", ' if ctrl_w else None)
        word = ctx.rank([f'{w}", ' for w in vocab], [t for t in (w_t, w_c) if t])
        equiv = None
        if word:
            import bench_eval as E
            equiv = any(E.is_right(judge.category("relation", h["pred"], c[:-3]), "lenient") for c, _ in word["top"])
        ctx.goto(open_text + s_t + w_t)
        o_t, o_c = f'{h["o_k"]}, [[', (f"{ctrl_o}, [[" if ctrl_o else None)
        obj = ctx.rank([f"{k}, [[" for k in objs + [-1] if k != h["s_k"]], [t for t in (o_t, o_c) if t])

        def pick_(res, t):
            return None if not res or t not in res["targets"] else res["targets"][t]

        out.append({"kind": kind, "s_k": h["s_k"], "o_k": h["o_k"], "pred": h["pred"], "reverse_written": h["reverse_written"],
                    "subject": pick_(subj, s_t), "subject_control": pick_(subj, s_c),
                    "word": pick_(word, w_t), "word_control": pick_(word, w_c), "word_top": word["top"] if word else None,
                    "word_equivalent_in_top5": equiv, "object": pick_(obj, o_t), "object_control": pick_(obj, o_c),
                    "n_objects": V.n, "vocabulary": len(vocab)})
    return {"p_stop_at_end": (None if stop_end is None or cont_end is None else
                              round(1 / (1 + math.exp(cont_end - stop_end)), 4)),
            "p_stop_after_each": stops, "relations_written": len(C.answer_relations(V.text)),
            "human_relations": len(hum), "missed": len(missed), "tested": out}


# ----------------------------------------------------------------------------- p2b
def p2b_interventions(lm, V, n_objects=5, n_windows=3, seed=0):
    if not V.same:
        return {"skipped": "objects differ from the saved run"}
    rels = V.rels
    if not rels:
        return {"skipped": "no relation inside the first answer tokens"}
    lay = V.layout
    conds = {}

    def run(name, inp, ids=None, groups=None):
        lp = lm.teacher_force(inp, ids if ids is not None else V.ids)
        conds[name] = group_sums(lp, groups if groups is not None else rels)

    run("clean", V.inp)
    run("blank_all", blank(V.inp, C.latent_positions(lay)))
    run("blank_otr", blank(V.inp, C.latent_positions(lay, kind="otr")))
    run("blank_twr", blank(V.inp, C.latent_positions(lay, kind="twr")))
    # time labels reversed, with TRASER's answer and with its times moved where the labels would put them
    W = lay["n_windows"]
    mapping = C.reversed_window_map(W)
    rev = relabel(lm, V.inp, lay, mapping)
    mapped = C.mapped_answer(V.cut_text, W)
    m_ids, m_offs = answer_tokens(lm, mapped, len(V.ids) + 64)
    m_rels = relation_groups(mapped, m_offs)
    pairs = min(len(m_rels), len(rels))
    run("labels_reversed", rev)
    run("labels_reversed_mapped_answer", rev, m_ids, m_rels[:pairs])
    run("clean_mapped_answer", V.inp, m_ids, m_rels[:pairs])
    # one object at a time
    count = collections.Counter(k for r in rels for k in (r["s_k"], r["o_k"]) if 1 <= k <= V.n)
    blanked = [k for k, _ in count.most_common(n_objects)]
    for k in blanked:
        run(f"blank_object_{k}", blank(V.inp, C.latent_positions(lay, k)))
    # the windows of a relation vs other windows of the same two objects
    rng = random.Random(seed)
    win_of = {o["k"]: {w["w"] for w in o["windows"]} for o in lay["objects"]}
    tests = []
    for j, r in enumerate(rels):
        if len(tests) >= n_windows or not (1 <= r["s_k"] <= V.n and 1 <= r["o_k"] <= V.n):
            continue
        both = win_of[r["s_k"]] & win_of[r["o_k"]]
        span_w = {int(t // C.WINDOW_S) for a, b in r["spans"] for t in np.arange(a, b + 1)} & both
        other = sorted(both - span_w)
        if not span_w or len(span_w) > 2 or len(other) < len(span_w):
            continue
        ctrl = sorted(rng.sample(other, len(span_w)))
        name = f"windows_rel{j}"
        run(name + "_own", blank(V.inp, C.latent_positions(lay, r["s_k"], "twr", span_w) + C.latent_positions(lay, r["o_k"], "twr", span_w)))
        run(name + "_other", blank(V.inp, C.latent_positions(lay, r["s_k"], "twr", set(ctrl)) + C.latent_positions(lay, r["o_k"], "twr", set(ctrl))))
        tests.append({"relation": j, "own_windows": sorted(span_w), "other_windows": ctrl, "name": name})
    return {"relations": [{k: r[k] for k in ("i", "s_k", "o_k", "pred", "spans")} | {"tokens": {g: len(t) for g, t in r["tok"].items()}}
                          for r in rels],
            "mapped_relations": pairs, "n_windows": W, "objects_blanked": blanked, "window_tests": tests, "logprobs": conds}


# ----------------------------------------------------------------------------- p2c
def patch_layers(n_layers, n=10):
    return sorted({int(round(x)) for x in np.linspace(0, n_layers - 1, n)})


def p2c_patching(lm, V, n_relations=2):
    import torch
    if not V.same:
        return {"skipped": "objects differ from the saved run"}
    picks = [r for r in V.rels if 1 <= r["o_k"] <= V.n][:n_relations]
    layers = patch_layers(lm.n_layers)
    out = []
    for r in picks:
        t_obj = r["tok"]["o"]
        ids = V.ids[:max(t_obj) + 1]
        obj_pos = C.latent_positions(V.layout, r["o_k"])
        L = V.inp.shape[1]
        decision = L + min(t_obj) - 1
        clean_store = {}

        def grab(li):
            def f(m, a, output):
                H = layer_out(output)[0]
                clean_store[li] = (H[obj_pos].clone(), H[decision].clone())
            return f

        lp_clean = lm.teacher_force(V.inp, ids, hooks=[(lm.layers[li], grab(li)) for li in layers])[t_obj].sum()
        corrupt = blank(V.inp, obj_pos)
        lp_corr = lm.teacher_force(corrupt, ids)[t_obj].sum()
        res = {"relation": r["i"], "s_k": r["s_k"], "o_k": r["o_k"], "pred": r["pred"],
               "lp_clean": round(float(lp_clean), 4), "lp_corrupt": round(float(lp_corr), 4), "layers": layers,
               "lp_patch_object": [], "lp_patch_decision": []}
        for li in layers:
            for where, key in ((obj_pos, "lp_patch_object"), ([decision], "lp_patch_decision")):
                stored = clean_store[li][0] if key == "lp_patch_object" else clean_store[li][1][None]

                def put(m, a, output, where=where, stored=stored):
                    H = layer_out(output).clone()
                    H[0, where] = stored
                    return replace_out(output, H)

                lp = lm.teacher_force(corrupt, ids, hooks=[(lm.layers[li], put)])[t_obj].sum()
                res[key].append(round(float(lp), 4))
        out.append(res)
        del clean_store
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    return {"tested": out}


# ----------------------------------------------------------------------------- p3
ATTN_TIME = ["own_window_latents", "own_window_label", "other_windows_latents", "own_otr", "other_labels",
             "other_objects", "object_markers", "answer", "prompt"]
ATTN_ID = ["named_object_block", "other_objects", "answer", "prompt"]
ATTN_WORD = ["subject_and_object", "other_objects", "labels_and_markers", "answer", "prompt"]


def p3_attention(lm, V, max_len=5000, n_relations=30):
    import torch
    if not V.same:
        return {"skipped": "objects differ from the saved run"}
    L = V.inp.shape[1]
    lay = V.layout
    rels = V.rels[:n_relations]
    if not rels:
        return {"skipped": "no relation inside the first answer tokens"}
    last = max(max(max(v) for v in r["tok"].values()) for r in rels)
    ids = V.ids[:last + 1]
    T = L + len(ids)
    if T > max_len:
        return {"skipped": f"input + answer is {T} tokens (> {max_len})"}
    kind = np.zeros(T, np.int8)        # 0 prompt, 1 object label, 2 OTR, 3 TWR, 4 window label, 5 answer
    obj = np.zeros(T, np.int16)
    win = np.full(T, -1, np.int16)
    for o in lay["objects"]:
        a, b = o["block"]
        kind[a:b], obj[a:b] = 1, o["k"]
        kind[o["otr"][0]:o["otr"][1]] = 2
        for w in o["windows"]:
            kind[w["twr"][0]:w["twr"][1]], win[w["twr"][0]:w["twr"][1]] = 3, w["w"]
            kind[w["label"][0]:w["label"][1]], win[w["label"][0]:w["label"][1]] = 4, w["w"]
    kind[L:] = 5
    queries, masks, meta = [], [], []
    latent = (kind == 2) | (kind == 3)
    for r in rels:
        so = (obj == r["s_k"]) | (obj == r["o_k"])
        first = lambda key: L - 1 + r["tok"][key][0]  # noqa: E731  (the position whose output is that token)
        if r["spans"]:
            w_star = int(r["spans"][0][0] // C.WINDOW_S)
            m = [so & (kind == 3) & (win == w_star), so & (kind == 4) & (win == w_star), so & (kind == 3) & (win != w_star),
                 so & (kind == 2), (kind == 4) & ~(so & (win == w_star)), latent & ~so, kind == 1, kind == 5, kind == 0]
            queries.append(first("time"))
            masks.append(m)
            meta.append(("time", r["i"]))
        own = obj == r["o_k"]
        queries.append(first("o"))
        masks.append([own & (kind > 0) & (kind < 5), (kind > 0) & (kind < 5) & ~own, kind == 5, kind == 0])
        meta.append(("object_id", r["i"]))
        queries.append(first("pred"))
        masks.append([so & latent, latent & ~so, (kind == 1) | (kind == 4), kind == 5, kind == 0])
        meta.append(("word", r["i"]))
    q = torch.tensor(queries, device=lm.device)
    ncat = max(len(m) for m in masks)
    M = torch.zeros(len(queries), ncat, T, device=lm.device, dtype=torch.float32)
    for i, m in enumerate(masks):
        for c, mm in enumerate(m):
            M[i, c] = torch.from_numpy(mm.astype(np.float32))
    causal = (torch.arange(T, device=lm.device)[None] <= q[:, None]).float()
    share = ((M * causal[:, None]).sum(-1) / causal.sum(-1, keepdim=True)).cpu().numpy()
    mass = np.zeros((lm.n_layers, len(queries), ncat), np.float32)

    def hook(li):
        def f(m, a, output):
            w = output[1]
            if w is None:
                return output
            rows = w[0, :, q].float().mean(0)          # heads averaged: [Q, T]
            mass[li] = torch.einsum("qk,qck->qc", rows, M).cpu().numpy()
            return (output[0], None) + tuple(output[2:])
        return f

    cfg = lm.model.config
    old = cfg._attn_implementation
    cfg._attn_implementation = "eager"
    try:
        x = torch.cat([V.inp, lm.embed(ids)], 1)
        with torch.no_grad(), attach([(layer.self_attn, hook(li)) for li, layer in enumerate(lm.layers)]):
            lm.body(x)
    finally:
        cfg._attn_implementation = old
    return {"queries": meta, "categories": {"time": ATTN_TIME, "object_id": ATTN_ID, "word": ATTN_WORD},
            "mass": np.round(mass, 5).tolist(), "share": np.round(share, 5).tolist(), "tokens": T,
            "invalid_object_numbers": [r["i"] for r in rels if not (1 <= r["o_k"] <= V.n) or not (r["s_k"] == -1 or 1 <= r["s_k"] <= V.n)]}


# ----------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lm", required=True, help="TRASER's language model exported by tools/export_lm.py")
    ap.add_argument("--work", required=True)
    ap.add_argument("--results", default=str(C.RESULTS))
    ap.add_argument("--out", default=str(C.OUT))
    ap.add_argument("--datasets", nargs="+", default=C.DATASETS)
    ap.add_argument("--n", type=json.loads, default={})
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--shard", type=int, default=0)
    ap.add_argument("--nshards", type=int, default=1)
    ap.add_argument("--phases", nargs="+", default=PHASES)
    ap.add_argument("--dtype", default="float16")
    ap.add_argument("--max_answer_tokens", type=int, default=2000)
    ap.add_argument("--p0_videos", type=int, default=2, help="per dataset (first videos of the sample)")
    ap.add_argument("--p2a_missed", type=int, default=10)
    ap.add_argument("--p2a_written", type=int, default=5)
    ap.add_argument("--p2b_objects", type=int, default=5)
    ap.add_argument("--p2b_windows", type=int, default=3)
    ap.add_argument("--patch_videos", type=int, default=12, help="per dataset (first videos of the sample)")
    ap.add_argument("--patch_relations", type=int, default=2)
    ap.add_argument("--attn_videos", type=int, default=20, help="per dataset")
    ap.add_argument("--attn_max_len", type=int, default=5000)
    args = ap.parse_args()
    tag = f"[lm {args.shard + 1}/{args.nshards}] "
    sys.path.insert(0, str(HERE.parent))
    import bench_eval as E
    E.RESULTS = Path(args.results)

    jobs = []
    for ds in args.datasets:
        vids = C.select_videos(ds, args.n.get(ds), args.seed, args.results)
        for rank_, v in enumerate(vids):
            if rank_ % args.nshards != args.shard or not C.work_paths(args.work, ds, v)["embeds"].exists():
                continue
            phases = [p for p in args.phases if not (p == "p0" and rank_ >= args.p0_videos)
                      and not (p == "p2c" and rank_ >= args.patch_videos) and not (p == "p3" and rank_ >= args.attn_videos)]
            phases = [p for p in phases if not C.out_path(p, ds, v, args.out).exists()]
            if phases:
                jobs.append((ds, v, phases))
    log(f"{len(jobs)} videos with phases to run", tag)
    if not jobs:
        return 0
    lm = LM(args.lm, args.dtype)
    judge = E.Judge()
    vocab = {}
    t_all = time.time()
    for i, (ds, v, phases) in enumerate(jobs, 1):
        try:
            V = Video(ds, v, args.work, args.results, args.max_answer_tokens, lm)
        except Exception as e:  # noqa: BLE001
            log(f"{ds}/{v}: cannot load ({type(e).__name__}: {e})", tag)
            continue
        for ph in phases:
            t0 = time.time()
            try:
                if ph == "p0":
                    res = p0_check(lm, V)
                elif ph == "p1":
                    res = p1_hidden(lm, V)
                elif ph == "p2a":
                    if ds not in vocab:
                        vocab[ds] = vocabulary(ds, args.results)
                    res = p2a_forced(lm, V, judge, *vocab[ds], n_missed=args.p2a_missed, n_written=args.p2a_written, seed=args.seed)
                elif ph == "p2b":
                    res = p2b_interventions(lm, V, args.p2b_objects, args.p2b_windows, args.seed)
                elif ph == "p2c":
                    res = p2c_patching(lm, V, args.patch_relations)
                elif ph == "p3":
                    res = p3_attention(lm, V, args.attn_max_len)
                res = dict(res, dataset=ds, video=v, seconds=round(time.time() - t0, 1), input_tokens=int(V.inp.shape[1]),
                           answer_tokens=len(V.ids), objects=V.n)
                C.write_json(C.out_path(ph, ds, v, args.out), res)
                log(f"{ds}/{v} {ph} done in {time.time() - t0:.0f} s" + (f" ({res['skipped']})" if "skipped" in res else ""), tag)
            except Exception as e:  # noqa: BLE001
                log(f"{ds}/{v} {ph} FAILED: {type(e).__name__}: {str(e)[:300]}\n{traceback.format_exc()[-1500:]}", tag)
            finally:
                if lm.torch.cuda.is_available():
                    lm.torch.cuda.empty_cache()
        log(f"video {i}/{len(jobs)} finished ({(time.time() - t_all) / 60:.1f} min so far)", tag)
    log(f"finished ({(time.time() - t_all) / 60:.1f} min)", tag)
    return 0


if __name__ == "__main__":
    sys.exit(main())
