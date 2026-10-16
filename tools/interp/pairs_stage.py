"""Interpretability, pair experiment (GPU, TRASER's language model): why are human-related pairs never written?

Every human relation whose two objects TRASER received is a "relevant pair". For the pairs TRASER did not write,
four explanations compete:
    A  didn't see       the pair's information is not inside the model
    B  didn't choose    it is inside, but the writing step does not pick the pair
    C  stopped early    it would write the pair, but ends the list first / stops looking at the video as it writes
    D  habit            the pair (or its word) comes from usual combinations, not from this video

Phases (one JSON per video and phase under results/traser_bench/interp/raw/<phase>/<dataset>/<video>.json):
  e2  fill-in ("perception bypass", Do VLMs Actually See?): we write the subject for it and score every relation
      word together with the human object, `[s, "<word>", o, [[`. Three inputs: the video, the video hidden (all
      latents blank: habit only), the pair hidden (only the two objects' latents blank). Also the object it picks
      after the subject and the human word. Missed pairs, written pairs, and non-related pairs as a control.
  e3  keep writing (C): from where TRASER closed its list, re-open it ("," + "[") up to 3 times and let it write;
      start a relation with the missed pair's subject and let it finish; ask again as a new user turn
      ("List more relationships of object s", the multi-turn fix of VisualSwap). Which missed pairs come back?
      Swap halfway (VisualSwap): after k of TRASER's own relations, the visual contents of two objects are swapped
      in the input; do the next relations follow the swapped video or TRASER's own earlier text?
  e4  where it looks (VisualSwap's visual attention score): attention of the tokens that write each relation's
      subject and object numbers, by position in the list and layer: to the subject's / object's / other latents,
      labels, the answer so far, the prompt; and at the point where it closes the list, to the objects of the
      missed pairs. Computed row by row, so long inputs fit.
  e6  push (causal check of B): at the position that writes the object number (after the human subject and word),
      add the object's own hidden-state direction, a little more each time, in the middle layers; how much push
      until the human object becomes the first choice, for missed pairs vs non-related objects (control)?

    CUDA_VISIBLE_DEVICES=0 python3 tools/interp/pairs_stage.py --lm /kaggle/tmp/traser_lm \
        --work /kaggle/tmp/interp_work --shard 0 --nshards 2
"""
import argparse
import collections
import json
import random
import re
import sys
import time
import traceback
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent))
from interp import common as C  # noqa: E402
from interp.lm_stage import (LM, STOP_IDS, Context, Video, attach, blank, human_relations, layer_out,  # noqa: E402
                             replace_out, vocabulary)

PHASES = ["e2", "e3", "e4", "e6"]
LOOSE_REL = re.compile(r'\[\s*(-?\d+)\s*,\s*"((?:[^"\\]|\\.)*)"\s*,\s*(-?\d+)\s*,')
REASK = ("<|im_end|>\n<|im_start|>user\nList more relationships of object {s}, in the same format "
         "[subject, \"relation\", object, [[start, end]]].<|im_end|>\n<|im_start|>assistant\n")


def log(msg, tag=""):
    print(f"{time.strftime('%H:%M:%S')} {tag}{msg}", flush=True)


# ----------------------------------------------------------------------------- pairs of a video
def video_pairs(V, judge, n_missed, n_written, n_control, seed=0):
    """Relevant (human) pairs with TRASER's object numbers, grouped: missed / written; plus non-related pairs."""
    groups = collections.OrderedDict()
    for h in human_relations(V, judge):
        if h["s_k"] == h["o_k"]:
            continue
        g = groups.setdefault((h["s_k"], h["o_k"]), {"s_k": h["s_k"], "o_k": h["o_k"], "words": [],
                                                       "written": h["pair_written"], "reverse_written": h["reverse_written"]})
        if h["pred"] not in g["words"]:
            g["words"].append(h["pred"])
    rng = random.Random(seed)
    missed = [g for g in groups.values() if not g["written"]]
    written = [g for g in groups.values() if g["written"]]
    related = {(a, b) for a, b in groups} | {(b, a) for a, b in groups}
    free = [(i, j) for i in range(1, V.n + 1) for j in range(1, V.n + 1) if i != j and (i, j) not in related]
    control = [{"s_k": i, "o_k": j, "words": [], "written": None, "reverse_written": None}
               for i, j in rng.sample(free, min(n_control, len(free)))]
    return (rng.sample(missed, min(n_missed, len(missed))), rng.sample(written, min(n_written, len(written))), control,
            {"relevant_pairs": len(groups), "missed_pairs": len(missed), "written_pairs": len(written)})


def list_open(V):
    """Text up to where TRASER closed its relation list, re-opened for one more relation."""
    end = C.list_end(V.text)
    if end is None:
        return None
    prefix = V.text[:end]
    return prefix + (", [" if C.answer_relations(V.text) else "[")


# ----------------------------------------------------------------------------- greedy writing from a context
def greedy(ctx, prefix, max_new, stop=None, penalty=1.05):
    """TRASER's decoding (greedy, repetition penalty 1.05 over the answer's tokens) continued from `prefix`.
    Leaves ctx at `prefix`. stop(new_text) -> True ends early."""
    lm, torch = ctx.lm, ctx.lm.torch
    ctx.goto(prefix)
    ids = list(ctx.ids)
    n0 = len(ids)
    ctx.cache.crop(ctx.L + n0 - 1)
    nxt, new = [ids[-1]], []
    seen = set(ids)
    try:
        for step in range(max_new):
            with torch.no_grad():
                h = lm.body(lm.embed(nxt), ctx.cache)[-1]
            logits = torch.nn.functional.linear(h, lm.W).float()
            idx = torch.tensor(sorted(seen), device=logits.device)
            s = logits[idx]
            logits[idx] = torch.where(s < 0, s * penalty, s / penalty)
            t = int(logits.argmax())
            if t in STOP_IDS:
                break
            new.append(t)
            seen.add(t)
            nxt = [t]
            if stop is not None and step % 3 == 2 and stop(lm.tok.decode(new)):
                break
    finally:
        ctx.cache.crop(ctx.L + n0)
    return lm.tok.decode(new)


def new_relations(full_text, start):
    """Relations of full_text that begin at or after character `start`."""
    return [r for r in C.answer_relations(full_text) if r["range"][0] >= start - 1]


# ----------------------------------------------------------------------------- e2
E2_CONDS = ["clean", "video_hidden", "pair_hidden"]


def e2_fill(lm, V, judge, vocab, picks):
    """conditions: clean = the video; video_hidden = every latent blank; pair_hidden = the two objects' latents blank."""
    open_text = list_open(V)
    if open_text is None:
        return {"skipped": "answer cut off (no end of the relation list)"}
    objs = list(range(1, V.n + 1)) + [-1]
    out = {kind: [dict(p) for p in pairs] for kind, pairs in picks.items()}
    import bench_eval as E
    every = blank(V.inp, C.latent_positions(V.layout))
    for cname in E2_CONDS:
        ctx = None if cname == "pair_hidden" else Context(lm, V.inp if cname == "clean" else every)
        for kind, pairs in out.items():
            for p in pairs:
                if cname == "pair_hidden":
                    ks = [k for k in (p["s_k"], p["o_k"]) if k >= 1]
                    ctx = Context(lm, blank(V.inp, [t for k in ks for t in C.latent_positions(V.layout, k)]))
                s, o = p["s_k"], p["o_k"]
                words = p["words"] or [vocab[0]]
                head = open_text + f'{s}, "'
                ctx.goto(head)
                res = ctx.rank([f'{w}", {o}, [[' for w in vocab], [f'{w}", {o}, [[' for w in words[:3]])
                r = {"pair_lp": None, "word_rank": None, "word_lp": None, "top": None, "equivalent_in_top5": None}
                if res:
                    r["top"] = [[t[:t.index('"')], v] for t, v in res["top"]]
                    r["pair_lp"] = res["top"][0][1] if res["top"] else None
                    if p["words"]:
                        best = min(res["targets"].values(), key=lambda x: x["rank"])
                        r["word_rank"], r["word_lp"] = best["rank"], best["lp"]
                        r["equivalent_in_top5"] = any(
                            E.is_right(judge.category("relation", w, t[0]), "lenient") for w in p["words"] for t in r["top"])
                if p["words"] and cname in ("clean", "video_hidden"):
                    ctx.goto(head + f'{p["words"][0]}", ')
                    ob = ctx.rank([f"{k}, [[" for k in objs if k != s], [f"{o}, [["])
                    t = ob["targets"].get(f"{o}, [[") if ob else None
                    r["object_rank"], r["object_lp"] = (t["rank"], t["lp"]) if t else (None, None)
                p[cname] = r
        del ctx
        if lm.torch.cuda.is_available():
            lm.torch.cuda.empty_cache()
    return {"conditions": E2_CONDS, "vocabulary": len(vocab), **out}


# ----------------------------------------------------------------------------- e3
def swap_objects(lm, inp, layout, a, b):
    """The input with the visual contents (OTR + windows with their labels) of objects a and b exchanged."""
    torch = lm.torch
    seg = {o["k"]: (o["otr"][0], o["block"][1] - 2) for o in layout["objects"] if o["k"] in (a, b)}
    (s1, e1), (s2, e2) = sorted(seg.values())
    return torch.cat([inp[:, :s1], inp[:, s2:e2], inp[:, e1:s2], inp[:, s1:e1], inp[:, e2:]], 1)


def pair_set(rels, involve):
    return {(r["s"], r["o"]) for r in rels if r["s"] in involve or r["o"] in involve}


def e3_continue(lm, V, picks, max_rounds=3, max_tokens=450, max_new_rel=12, cue_tokens=40, reask_subjects=3,
                reask_tokens=160, swap_ks=(0, 3, 8), swap_rel=4, swap_tokens=180):
    open_text = list_open(V)
    if open_text is None:
        return {"skipped": "answer cut off (no end of the relation list)"}
    missed = picks["missed"]
    ctx = Context(lm, V.inp)
    gid = {k + 1: g for k, g in enumerate(V.layout["gt_ids"])} | {-1: -1}

    def closes(base):
        return lambda new: C.list_end(base + new) is not None

    # 1. keep writing: re-open the list whenever it closes
    text, extra, used = open_text, [], 0
    for _ in range(max_rounds):
        gen = greedy(ctx, text, max_tokens - used, stop=closes(text))
        used += len(lm.encode(gen))
        full = text + gen
        got = new_relations(full, len(text))
        extra += [{"s": r["s"], "pred": r["pred"], "o": r["o"]} for r in got]
        end = C.list_end(full)
        if end is None or used >= max_tokens or len(extra) >= max_new_rel or not got:
            break
        text = full[:end] + ", ["
    written = {(r["s"], r["o"]) for r in extra}
    # 2. start the missed pair's relation with its subject
    cued = []
    for p in missed:
        head = open_text + f'{p["s_k"]}, "'
        gen = greedy(ctx, head, cue_tokens, stop=lambda new: bool(re.search(r'"\s*,\s*-?\d+\s*,', new)))
        m = re.match(r'((?:[^"\\]|\\.)*)"\s*,\s*(-?\d+)', gen)
        cued.append({"s_k": p["s_k"], "o_k": p["o_k"], "word": m.group(1) if m else None,
                     "object": int(m.group(2)) if m else None, "hit": bool(m) and int(m.group(2)) == p["o_k"]})
    # 3. a new user turn: "List more relationships of object s"
    reask = []
    subjects = [s for s, _ in collections.Counter(p["s_k"] for p in missed).most_common(reask_subjects)]
    for s in subjects:
        head = V.text + REASK.format(s=s)
        gen = greedy(ctx, head, reask_tokens)
        found = [(int(a), w, int(b)) for a, w, b in LOOSE_REL.findall(gen)]
        reask.append({"s_k": s, "relations": found[:20],
                      "hits": [p["o_k"] for p in missed if p["s_k"] == s and any(a == s and b == p["o_k"] for a, _, b in found)]})
    for p in missed:
        p_rea = [r for r in reask if r["s_k"] == p["s_k"]]
        p["kept_writing"] = (p["s_k"], p["o_k"]) in written
        p["kept_writing_reverse"] = (p["o_k"], p["s_k"]) in written
        p["cued"] = next((c["hit"] for c in cued if c["s_k"] == p["s_k"] and c["o_k"] == p["o_k"]), None)
        p["reasked"] = (p["o_k"] in p_rea[0]["hits"]) if p_rea else None
    human = {(p["s_k"], p["o_k"]) for p in picks["missed"] + picks["written"]}
    # 4. swap halfway
    rels = C.answer_relations(V.text)
    swap = None
    names = {}
    try:
        import bench_eval as E
        names = E.parse_prediction(V.text)["objects"]
    except Exception:  # noqa: BLE001
        pass
    count = collections.Counter(k for r in rels for k in (r["s"], r["o"]) if 1 <= k <= V.n)
    order = [k for k, _ in count.most_common()]
    if len(order) >= 2:
        a = order[0]
        b = next((k for k in order[1:] if names.get(k) != names.get(a)), order[1])
        ctx_sw = Context(lm, swap_objects(lm, V.inp, V.layout, a, b))
        ren = {a: b, b: a}
        steps = []
        for k in [k for k in swap_ks if k < len(rels)]:
            prefix = V.text[:rels[k]["range"][0] + 1]
            stop_n = lambda base: (lambda new: C.list_end(base + new) is not None  # noqa: E731
                                   or len(new_relations(base + new, len(base))) >= swap_rel)
            g_clean = new_relations(prefix + greedy(ctx, prefix, swap_tokens, stop=stop_n(prefix)), len(prefix))[:swap_rel]
            g_swap = new_relations(prefix + greedy(ctx_sw, prefix, swap_tokens, stop=stop_n(prefix)), len(prefix))[:swap_rel]
            old = pair_set(g_clean, (a, b))
            new = {(ren.get(s, s), ren.get(o, o)) for s, o in old}
            sw = pair_set(g_swap, (a, b))
            steps.append({"k": k, "clean": [[r["s"], r["pred"], r["o"]] for r in g_clean],
                          "swapped": [[r["s"], r["pred"], r["o"]] for r in g_swap],
                          "follows_new": len([x for x in sw if x in new and x not in old]),
                          "follows_old": len([x for x in sw if x in old and x not in new]),
                          "involving": len(sw)})
        swap = {"a": a, "b": b, "names": [names.get(a), names.get(b)], "steps": steps}
        del ctx_sw
    return {"kept_writing": extra, "kept_writing_tokens": used,
            "kept_writing_human": len([1 for r in extra if (r["s"], r["o"]) in human]),
            "kept_writing_gt": len([1 for r in extra if (gid.get(r["s"]), gid.get(r["o"])) in
                                    {(x["subj"], x["obj"]) for x in V.gt["relations"]}]) if V.gt else None,
            "cued": cued, "reask": reask, "swap": swap, **picks}


# ----------------------------------------------------------------------------- e4
def rotate_half(x):
    import torch
    h = x.shape[-1] // 2
    return torch.cat([-x[..., h:], x[..., :h]], -1)


class RowAttention:
    """Pre-hooks on every attention module: from the layer's input (after its norm) and rotary embeddings,
    the attention of a few query rows over all keys, reduced to category masses by `reduce(layer, att[Q, T])`."""

    def __init__(self, lm, qpos, reduce):
        self.lm, self.qpos, self.reduce = lm, qpos, reduce

    def hook(self, li):
        torch = self.lm.torch

        def f(module, args, kwargs):
            hs = kwargs.get("hidden_states", args[0] if args else None)
            pe = kwargs.get("position_embeddings", args[1] if len(args) > 1 else None)
            cos, sin = pe
            cfg = module.config
            H, KV = cfg.num_attention_heads, cfg.num_key_value_heads
            d = getattr(module, "head_dim", cfg.hidden_size // H)
            q_idx = torch.tensor(self.qpos, device=hs.device)
            T = hs.shape[1]
            q = module.q_proj(hs[0, q_idx]).view(len(self.qpos), H, d).transpose(0, 1).float()
            k = module.k_proj(hs[0]).view(T, KV, d).transpose(0, 1).float()
            c, s = cos[0].float(), sin[0].float()
            q = q * c[q_idx][None] + rotate_half(q) * s[q_idx][None]
            k = k * c[None] + rotate_half(k) * s[None]
            k = k.repeat_interleave(H // KV, 0)
            sc = torch.einsum("hqd,htd->hqt", q, k) * getattr(module, "scaling", d ** -0.5)
            mask = torch.arange(T, device=hs.device)[None] > q_idx[:, None]
            sc = sc.masked_fill(mask[None], float("-inf"))
            att = torch.softmax(sc, -1).mean(0)                     # heads averaged: [Q, T]
            self.reduce(li, att)
            return None
        return f

    def run(self, x):
        torch = self.lm.torch
        hooks = [layer.self_attn.register_forward_pre_hook(self.hook(li), with_kwargs=True)
                 for li, layer in enumerate(self.lm.layers)]
        try:
            with torch.no_grad():
                self.lm.body(x)
        finally:
            for h in hooks:
                h.remove()


E4_REL = ["subject_latents", "object_latents", "other_latents", "labels", "answer", "prompt"]
E4_END = ["missed_pair_latents", "other_latents", "labels", "answer", "prompt"]


def e4_attention(lm, V, picks, n_relations=40):
    torch = lm.torch
    lay = V.layout
    L = V.inp.shape[1]
    rels = [r for r in V.rels if (r["s_k"] == -1 or 1 <= r["s_k"] <= V.n) and (r["o_k"] == -1 or 1 <= r["o_k"] <= V.n)][:n_relations]
    end_c = C.list_end(V.text)
    end_tok = C.tokens_in(V.offs, end_c, end_c + 1) if end_c is not None else []
    end_tok = end_tok[0] if end_tok and end_tok[0] < len(V.ids) else None
    if not rels and end_tok is None:
        return {"skipped": "no relation inside the first answer tokens"}
    last = max([max(r["tok"]["o"]) for r in rels] + ([end_tok] if end_tok is not None else []))
    ids = V.ids[:last + 1]
    T = L + len(ids)
    kind = np.zeros(T, np.int8)          # 0 prompt, 1 label/marker, 2 latent, 5 answer
    obj = np.zeros(T, np.int16)
    for o in lay["objects"]:
        a, b = o["block"]
        kind[a:b], obj[a:b] = 1, o["k"]
        kind[o["otr"][0]:o["otr"][1]] = 2
        for w in o["windows"]:
            kind[w["twr"][0]:w["twr"][1]] = 2
    kind[L:] = 5
    lat = kind == 2
    missed_objs = {k for p in picks["missed"] for k in (p["s_k"], p["o_k"])}
    queries, masks, meta = [], [], []
    for r in rels:
        for which in ("s", "o"):
            sk, ok_ = r["s_k"], r["o_k"]
            queries.append(L - 1 + r["tok"][which][0])
            masks.append([lat & (obj == sk), lat & (obj == ok_), lat & (obj != sk) & (obj != ok_),
                          kind == 1, kind == 5, kind == 0])
            meta.append({"type": which, "relation": r["i"], "s_k": sk, "o_k": ok_})
    if end_tok is not None:
        mo = np.isin(obj, list(missed_objs))
        queries.append(L - 1 + end_tok)
        masks.append([lat & mo, lat & ~mo, kind == 1, kind == 5, kind == 0])
        meta.append({"type": "list_end", "missed_objects": sorted(missed_objs)})
    ncat = max(len(m) for m in masks)
    M = torch.zeros(len(queries), ncat, T, device=lm.device)
    for i, m in enumerate(masks):
        for c, mm in enumerate(m):
            M[i, c] = torch.from_numpy(mm.astype(np.float32)).to(lm.device)
    mass = np.zeros((lm.n_layers, len(queries), ncat), np.float32)

    def reduce(li, att):
        mass[li] = torch.einsum("qt,qct->qc", att, M[:, :, :att.shape[1]]).cpu().numpy()

    x = torch.cat([V.inp, lm.embed(ids)], 1)
    RowAttention(lm, queries, reduce).run(x)
    # the share each category would get if attention were spread evenly over the earlier positions
    causal = (torch.arange(T, device=lm.device)[None] <= torch.tensor(queries, device=lm.device)[:, None]).float()
    share = ((M * causal[:, None]).sum(-1) / causal.sum(-1, keepdim=True)).cpu().numpy()
    return {"queries": meta, "categories": {"relation": E4_REL, "list_end": E4_END}, "tokens": T,
            "mass": np.round(mass, 5).tolist(), "share": np.round(share, 5).tolist()}


# ----------------------------------------------------------------------------- e6
def push_layers(n_layers):
    return list(range(int(round(0.45 * n_layers)), int(round(0.65 * n_layers)) + 1))


def e6_push(lm, V, picks, alphas=(0.0, 0.05, 0.1, 0.2, 0.4), n_pairs=4, seed=0):
    from transformers import DynamicCache
    torch = lm.torch
    open_text = list_open(V)
    if open_text is None:
        return {"skipped": "answer cut off (no end of the relation list)"}
    rng = random.Random(seed)
    gt_pairs = {(p["s_k"], p["o_k"]) for p in picks["missed"] + picks["written"]}
    gt_pairs |= {(b, a) for a, b in gt_pairs}
    tests = []
    for p in [p for p in picks["missed"] if p["words"] and p["o_k"] >= 1][:n_pairs]:
        others = [k for k in range(1, V.n + 1) if k not in (p["s_k"], p["o_k"]) and (p["s_k"], k) not in gt_pairs]
        tests.append(("missed", p, p["o_k"]))
        if others:
            tests.append(("control", p, rng.choice(others)))
    if not tests:
        return {"skipped": "no missed pair to push"}
    layers = push_layers(lm.n_layers)
    cands = [k for k in list(range(1, V.n + 1)) + [-1]]
    lat_all = C.latent_positions(V.layout)
    out = []
    for kind, p, target in tests:
        head = open_text + f'{p["s_k"]}, "{p["words"][0]}", '
        pids = lm.encode(head)
        cand_ids = {}
        for k in cands:
            if k == p["s_k"]:
                continue
            j = lm.encode(head + f"{k},")
            if j[:len(pids)] == pids and len(j) > len(pids):
                cand_ids[k] = j[len(pids):]
        if target not in cand_ids:
            continue
        tpos = C.latent_positions(V.layout, target)
        x = torch.cat([V.inp, lm.embed(pids)], 1)
        T = x.shape[1]
        res = {"kind": kind, "s_k": p["s_k"], "o_k": p["o_k"], "target": target, "word": p["words"][0], "layers": layers,
               "alphas": list(alphas), "rank": [], "lp": [], "top": []}
        for a in alphas:
            def push(li):
                def f(m, args, output):
                    Hs = layer_out(output)
                    h = Hs[0, T - 1]
                    d = Hs[0, tpos].float().mean(0) - Hs[0, lat_all].float().mean(0)
                    Hn = Hs.clone()
                    Hn[0, T - 1] = (h.float() + a * h.float().norm() * d / (d.norm() + 1e-6)).to(Hs.dtype)
                    return replace_out(output, Hn)
                return f
            cache = DynamicCache()
            with torch.no_grad(), attach([(lm.layers[li], push(li)) for li in layers] if a else []):
                h = lm.body(x, cache)
            first = lm.logprob_rows(h[-1:])[0]
            lps = {}
            for k, cid in cand_ids.items():
                lp = float(first[cid[0]])
                if len(cid) > 1:
                    cache.crop(T)
                    with torch.no_grad():
                        hh = lm.body(lm.embed(cid[:-1]), cache)
                    lp += float(lm.token_logprobs(hh, cid[1:]).sum())
                lps[k] = lp
            order = sorted(lps, key=lambda k: -lps[k])
            res["rank"].append(order.index(target) + 1)
            res["lp"].append(round(lps[target], 3))
            res["top"].append(order[:3])
            del cache
        out.append(res)
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    return {"tested": out}


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
    ap.add_argument("--missed", type=int, default=8, help="missed relevant pairs tested per video")
    ap.add_argument("--written", type=int, default=3, help="written relevant pairs per video (comparison)")
    ap.add_argument("--control", type=int, default=3, help="non-related pairs per video (control)")
    ap.add_argument("--vocab", type=int, default=40, help="most common human + TRASER words per dataset (candidates)")
    ap.add_argument("--push_videos", type=int, default=12, help="per dataset (first videos of the sample)")
    args = ap.parse_args()
    tag = f"[pairs {args.shard + 1}/{args.nshards}] "
    import bench_eval as E
    E.RESULTS = Path(args.results)

    jobs = []
    for ds in args.datasets:
        vids = C.select_videos(ds, args.n.get(ds), args.seed, args.results)
        for rank_, v in enumerate(vids):
            if rank_ % args.nshards != args.shard or not C.work_paths(args.work, ds, v)["embeds"].exists():
                continue
            phases = [p for p in args.phases if not C.out_path(p, ds, v, args.out).exists()
                      and not (p == "e6" and rank_ >= args.push_videos)]
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
        if not V.same:
            for ph in phases:
                C.write_json(C.out_path(ph, ds, v, args.out), {"skipped": "objects differ from the saved run", "dataset": ds, "video": v})
            continue
        missed, written, control, counts = video_pairs(V, judge, args.missed, args.written, args.control, args.seed)
        picks = {"missed": missed, "written": written, "control": control}
        for ph in phases:
            t0 = time.time()
            try:
                if ph == "e2":
                    if ds not in vocab:
                        vocab[ds] = vocabulary(ds, args.results, args.vocab)[0]
                    res = e2_fill(lm, V, judge, vocab[ds], {k: [dict(p) for p in x] for k, x in picks.items()})
                elif ph == "e3":
                    res = e3_continue(lm, V, {k: [dict(p) for p in x] for k, x in picks.items()})
                elif ph == "e4":
                    res = e4_attention(lm, V, picks)
                elif ph == "e6":
                    res = e6_push(lm, V, picks, seed=args.seed)
                res = dict(res, **counts, dataset=ds, video=v, seconds=round(time.time() - t0, 1),
                           input_tokens=int(V.inp.shape[1]), answer_tokens=len(V.ids), objects=V.n)
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
