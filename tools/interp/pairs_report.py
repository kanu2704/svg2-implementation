"""Interpretability, pair experiment (CPU): experiments 1 and 5, then every missed relevant pair gets its reason.

  e1  is the pair inside? A probe on TRASER's vectors (stage of the best "related pair" probe in probes.json)
      vs a "habit" probe that only sees the two object names; and both on the tricky pairs: name pairs that are
      related in some videos and not in others (habit alone cannot get these right).
  e5  which relevant pairs are missed? miss ~ size, time together, gap, touching, motion, tokens, living,
      action vs position word, how common the name pair is (logistic regression, standardized; miss rate by thirds).
  reasons  each tested missed pair (pairs_stage e2/e3) gets one reason:
      C stopped early  it writes the pair when the list is re-opened, when its subject is started, or when asked again
      D habit          it fills in the human word (top 5) also with the video hidden, and the video adds < 1 nat
      B didn't choose  it fills in the human word with the video, or the probe says "related"
      A didn't see     none of these

    python3 tools/interp/pairs_report.py --work /kaggle/tmp/interp_work
        -> results/traser_bench/interp/PAIRS.md, pairs.json, figs/pairs_*.png
"""
import argparse
import collections
import json
import random
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent))
from interp import common as C  # noqa: E402
from interp import probe as Pr  # noqa: E402

GEO = ["time together", "gap", "touching", "size (subject)", "size (object)", "speed (subject)", "speed (object)",
       "tokens (subject)", "tokens (object)", "living (subject)", "living (object)", "objects in video"]
REASONS = ["A didn't see", "B didn't choose", "C stopped early", "D habit"]
COLORS = ["#c0504d", "#4f81bd", "#f79646", "#9bbb59"]


def raw(phase, ds, out):
    d = Path(out) / "raw" / phase / ds
    return {p.stem: json.load(open(p)) for p in sorted(d.glob("*.json"))} if d.exists() else {}


# ----------------------------------------------------------------------------- e1 + e5
def name_features(V, p):
    a, b = V["gids"][p["i"]], V["gids"][p["j"]]
    na, nb = V["names"].get(a, "?").lower(), V["names"].get(b, "?").lower()
    return {f"s={na}": 1, f"o={nb}": 1, f"so={na}|{nb}": 1}, (na, nb)


def e1_e5(ds, videos, stage, seed=0):
    from sklearn.feature_extraction import DictVectorizer
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import roc_auc_score
    from sklearn.preprocessing import StandardScaler
    rng = random.Random(seed)
    per = [Pr.samples(V, rng) for V in videos]
    rows, groups = [], []
    for vi, (pairs, _, _) in enumerate(per):
        for p in pairs:
            rows.append(p)
            groups.append(vi)
    y = np.array([r["related"] for r in rows])
    out = {"stage": stage, "pairs": len(rows), "related": int(y.sum())}
    # habit probe
    dv = DictVectorizer(sparse=False)
    feats, keys = zip(*[name_features(videos[g], r) for r, g in zip(rows, groups)])
    Xh = dv.fit_transform(feats)
    auc_h, oof_h = Pr.auc_cv(Xh, y.tolist(), groups, seed)
    # video probe (TRASER's vectors at `stage`)
    oof_v, auc_v, auc_both = None, None, None
    if stage and all(stage in V["stages"] for V in videos):
        Z = Pr.reduce(videos, stage, "obj", seed=seed)
        Xv = np.asarray([np.concatenate([Z[g][r["i"]], Z[g][r["j"]], Z[g][r["i"]] * Z[g][r["j"]]]) for r, g in zip(rows, groups)])
        auc_v, oof_v = Pr.auc_cv(Xv, y.tolist(), groups, seed)
        auc_both, _ = Pr.auc_cv(np.concatenate([Xv, Xh], 1), y.tolist(), groups, seed)
    # tricky pairs: name pairs that are related in some samples and unrelated in others
    lab = collections.defaultdict(set)
    for k, yy in zip(keys, y):
        lab[k].add(int(yy))
    tricky = np.array([len(lab[k]) == 2 for k in keys])

    def sub_auc(oof):
        if oof is None or tricky.sum() < 10 or len(set(y[tricky].tolist())) < 2:
            return None
        return round(float(roc_auc_score(y[tricky], oof[tricky])), 4)

    out["e1"] = {"video_auc": auc_v, "habit_auc": auc_h, "video_plus_habit_auc": auc_both,
                 "tricky_pairs": int(tricky.sum()), "tricky_related": int(y[tricky].sum()),
                 "video_auc_tricky": sub_auc(oof_v), "habit_auc_tricky": sub_auc(oof_h)}
    # "knows" per relevant pair: above the 90th percentile of the unrelated pairs' scores
    knows = {}
    if oof_v is not None:
        thr = float(np.percentile(oof_v[y == 0], 90))
        for r, g, o in zip(rows, groups, oof_v):
            if r["related"]:
                V = videos[g]
                knows[(V["v"], r["i"] + 1, r["j"] + 1)] = bool(o > thr)
        out["e1"]["threshold"] = round(thr, 4)
    # e5: which relevant pairs are missed
    pos = [(r, g) for r, g in zip(rows, groups) if r["related"]]
    freq = collections.Counter(k for k, yy in zip(keys, y) if yy)
    X5, y5, g5 = [], [], []
    for r, g in pos:
        V = videos[g]
        _, k = name_features(V, r)
        X5.append(Pr.geo_features(V, r) + [float(r["action"] or 0), float(np.log1p(freq[k]))])
        y5.append(1 - r["written"])
        g5.append(g)
    names5 = GEO + ["action word", "name pair is common"]
    X5 = np.asarray(X5, dtype=np.float32)
    y5 = np.asarray(y5)
    e5 = {"relevant": len(y5), "missed": int(y5.sum())}
    if len(set(y5.tolist())) == 2 and len(y5) >= 20:
        Xs = StandardScaler().fit_transform(X5)
        clf = LogisticRegression(C=0.5, max_iter=2000, class_weight="balanced").fit(Xs, y5)
        e5["auc"], _ = Pr.auc_cv(X5, y5.tolist(), g5, seed)
        e5["coef"] = {n: round(float(c), 3) for n, c in zip(names5, clf.coef_[0])}
        thirds = {}
        for j, n in enumerate(names5):
            col = X5[:, j]
            lo, hi = np.percentile(col, 33), np.percentile(col, 67)
            if lo == hi:
                lo_m, hi_m = col <= lo, col > lo
            else:
                lo_m, hi_m = col <= lo, col >= hi
            if lo_m.sum() >= 5 and hi_m.sum() >= 5:
                thirds[n] = [round(float(y5[lo_m].mean()), 3), round(float(y5[hi_m].mean()), 3)]
        e5["miss_rate_low_vs_high"] = thirds
    out["e5"] = e5
    return out, knows


# ----------------------------------------------------------------------------- reasons
def word_ok(r):
    return bool(r) and ((r.get("word_rank") or 99) <= 5 or bool(r.get("equivalent_in_top5")))


def reasons(ds, out, knows):
    e2, e3 = raw("e2", ds, out), raw("e3", ds, out)
    rows = []
    for v, a in e2.items():
        b = e3.get(v, {})
        cont = {(p["s_k"], p["o_k"]): p for p in b.get("missed", [])}
        for p in a.get("missed", []):
            c, h = p.get("clean"), p.get("video_hidden")
            q = cont.get((p["s_k"], p["o_k"]), {})
            rec = bool(q.get("kept_writing") or q.get("cued") or q.get("reasked"))
            fill = word_ok(c)
            habit = fill and word_ok(h) and c.get("word_lp") is not None and h.get("word_lp") is not None \
                and c["word_lp"] - h["word_lp"] < 1.0
            kn = knows.get((v, p["s_k"], p["o_k"]))
            if rec:
                why = REASONS[2]
            elif habit:
                why = REASONS[3]
            elif fill or kn:
                why = REASONS[1]
            else:
                why = REASONS[0]
            rows.append({"video": v, "s_k": p["s_k"], "o_k": p["o_k"], "words": p["words"], "reason": why,
                         "recovered": rec, "kept_writing": q.get("kept_writing"), "cued": q.get("cued"), "reasked": q.get("reasked"),
                         "fill_ok": fill, "habit": bool(habit), "knows": kn})
    return rows


def fill_table(ds, out):
    """Share of pairs whose human word is in the top 5 (or an equivalent is), per kind and condition; mean pair_lp."""
    t = collections.defaultdict(lambda: collections.defaultdict(list))
    for a in raw("e2", ds, out).values():
        for kind in ("missed", "written", "control"):
            for p in a.get(kind, []):
                for cond in a.get("conditions", []):
                    r = p.get(cond)
                    if not r:
                        continue
                    if p["words"]:
                        t[(kind, cond)]["ok"].append(word_ok(r))
                    if kind in ("missed", "written") and cond in ("clean", "video_hidden") and r.get("object_rank"):
                        t[(kind, cond)]["obj1"].append(r["object_rank"] == 1)
                    if r.get("pair_lp") is not None:
                        t[(kind, cond)]["pair_lp"].append(r["pair_lp"])
    return {f"{k}|{c}": {m: (round(float(np.mean(x)), 3) if x else None) for m, x in d.items()} | {"n": max(len(x) for x in d.values())}
            for (k, c), d in t.items()}


def auc(pos, neg):
    if not pos or not neg:
        return None
    x = np.array(pos)[:, None] - np.array(neg)[None]
    return float((x > 0).mean() + 0.5 * (x == 0).mean())


def all_table(ds, out):
    """Experiment 2 on every human pair (pairs_stage e2all): per context, kind and input, the human word's rank
    (exact word: rank 1, top 5; or an equivalent in the top 5), the object picked first, how much the video
    raises the human word's log-prob over the same pair without it, and how well the best word's log-prob
    separates related from non-related pairs (AUC)."""
    acc = collections.defaultdict(lambda: collections.defaultdict(list))
    lp = collections.defaultdict(lambda: collections.defaultdict(list))
    videos = collections.Counter()
    for a in raw("e2all", ds, out).values():
        if "skipped" in a:
            continue
        for h in a.get("contexts", []):
            videos[h] += 1
            for kind in ("missed", "written", "control"):
                for p in a.get(kind, []):
                    rs = p.get(h, {})
                    c = rs.get("clean", {})
                    for cond, r in rs.items():
                        if r.get("pair_lp") is not None:
                            lp[(h, cond)]["control" if kind == "control" else "related"].append(r["pair_lp"])
                        if not p["words"] or r.get("word_rank") is None:
                            continue
                        for k in (kind, "related"):
                            t = acc[(h, k, cond)]
                            t["rank1"].append(r["word_rank"] == 1)
                            t["top5"].append(r["word_rank"] <= 5)
                            t["top5_eq"].append(word_ok(r))
                            t["rank"].append(r["word_rank"])
                            if r.get("object_rank"):
                                t["obj1"].append(r["object_rank"] == 1)
                            if cond != "clean" and c.get("word_lp") is not None:
                                d = c["word_lp"] - r["word_lp"]
                                t["gain"].append(d)
    res = {"videos": dict(videos)}
    for (h, k, cond), t in acc.items():
        g = t.pop("gain", [])
        res[f"{h}|{k}|{cond}"] = {"n": len(t["rank"]), "median_rank": float(np.median(t["rank"])),
                                  **{m: round(float(np.mean(x)), 3) for m, x in t.items() if m != "rank" and x},
                                  **({"video_raises": round(float(np.mean([x > 0 for x in g])), 3),
                                      "video_raises_1nat": round(float(np.mean([x > 1 for x in g])), 3),
                                      "mean_gain_nats": round(float(np.mean(g)), 3)} if g else {})}
    for (h, cond), d in lp.items():
        a = auc(d["related"], d["control"])
        res[f"{h}|auc|{cond}"] = None if a is None else round(a, 3)
    return res


def swap_table(ds, out):
    by_k = collections.defaultdict(lambda: [0, 0, 0])
    for a in raw("e3", ds, out).values():
        for s in (a.get("swap") or {}).get("steps", []):
            by_k[s["k"]][0] += s["follows_new"]
            by_k[s["k"]][1] += s["follows_old"]
            by_k[s["k"]][2] += 1
    return {k: {"follows_new": n, "follows_old": o, "videos": c, "share_new": round(n / (n + o), 3) if n + o else None}
            for k, (n, o, c) in sorted(by_k.items())}


def continue_table(ds, out):
    t = {"videos": 0, "new_relations": 0, "new_human": 0, "missed_tested": 0, "kept_writing": 0, "cued": 0, "reasked": 0}
    for a in raw("e3", ds, out).values():
        if "skipped" in a:
            continue
        t["videos"] += 1
        t["new_relations"] += len(a.get("kept_writing", []))
        t["new_human"] += a.get("kept_writing_human", 0)
        for p in a.get("missed", []):
            t["missed_tested"] += 1
            t["kept_writing"] += bool(p.get("kept_writing"))
            t["cued"] += bool(p.get("cued"))
            t["reasked"] += bool(p.get("reasked"))
    return t


def attention_table(ds, out, bins=(0, 1, 3, 6, 10, 20, 40)):
    """Mean over layers of the attention mass of the object-number tokens, by position of the relation in the list."""
    acc = collections.defaultdict(lambda: collections.defaultdict(list))
    end = collections.defaultdict(list)
    for a in raw("e4", ds, out).values():
        if "skipped" in a:
            continue
        mass = np.asarray(a["mass"])          # [layers, Q, cats]
        share = np.asarray(a["share"])
        m = mass.mean(0)
        for qi, q in enumerate(a["queries"]):
            if q["type"] == "o":
                b = max(i for i, x in enumerate(bins) if q["relation"] >= x)
                for ci, c in enumerate(a["categories"]["relation"]):
                    acc[b][c].append(float(m[qi, ci]))
                acc[b]["visual (all latents)"].append(float(m[qi, :3].sum()))
                acc[b]["object latents, if spread evenly"].append(float(share[qi, 1]))
            elif q["type"] == "list_end":
                for ci, c in enumerate(a["categories"]["list_end"]):
                    end[c].append(float(m[qi, ci]))
                end["missed latents, if spread evenly"].append(float(share[qi, 0]))
    label = lambda b: f"{bins[b] + 1}" + (f"-{bins[b + 1]}" if b + 1 < len(bins) else "+")  # noqa: E731
    return ({label(b): {c: round(float(np.mean(x)), 4) for c, x in d.items()} | {"n": len(d["answer"])} for b, d in sorted(acc.items())},
            {c: round(float(np.mean(x)), 4) for c, x in end.items()} | {"n": len(end.get("answer", []))})


def push_table(ds, out):
    t = collections.defaultdict(list)
    alphas = None
    for a in raw("e6", ds, out).values():
        for r in a.get("tested", []):
            alphas = r["alphas"]
            t[r["kind"]].append([x == 1 for x in r["rank"]])
    return {"alphas": alphas, **{k: [round(float(x), 3) for x in np.mean(v, 0)] + [len(v)] for k, v in t.items()}}


# ----------------------------------------------------------------------------- figures + page
def figures(res, figs):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    figs.mkdir(parents=True, exist_ok=True)
    dss = [d for d in res if res[d].get("reasons_count")]
    made = []
    if dss:
        fig, ax = plt.subplots(figsize=(5.5, 3.2))
        for di, d in enumerate(dss):
            cnt, left = res[d]["reasons_count"], 0
            tot = sum(cnt.values()) or 1
            for ri, r in enumerate(REASONS):
                w = cnt.get(r, 0) / tot
                ax.barh(di, w, left=left, color=COLORS[ri], label=r if di == 0 else None)
                if w > 0.06:
                    ax.text(left + w / 2, di, f"{100 * w:.0f}%", ha="center", va="center", color="white", fontsize=9)
                left += w
        ax.set_yticks(range(len(dss)), [f"{d} ({sum(res[d]['reasons_count'].values())})" for d in dss])
        ax.set_xlim(0, 1)
        ax.set_xlabel("share of the tested missed relevant pairs")
        ax.legend(ncol=2, fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.25))
        fig.tight_layout()
        fig.savefig(figs / "pairs_reasons.png", dpi=130)
        plt.close(fig)
        made.append("pairs_reasons.png")
    sw = {d: res[d]["swap"] for d in res if res[d].get("swap")}
    if sw:
        fig, ax = plt.subplots(figsize=(4.5, 3))
        for d, t in sw.items():
            ks = [k for k in t if t[k]["share_new"] is not None]
            ax.plot([int(k) for k in ks], [t[k]["share_new"] for k in ks], "o-", label=d)
        ax.axhline(0.5, color="grey", lw=0.8, ls=":")
        ax.set_ylim(0, 1)
        ax.set_xlabel("relations TRASER had written before the swap (k)")
        ax.set_ylabel("follows the swapped video")
        ax.legend()
        fig.tight_layout()
        fig.savefig(figs / "pairs_swap.png", dpi=130)
        plt.close(fig)
        made.append("pairs_swap.png")
    at = {d: res[d]["attention"] for d in res if res[d].get("attention")}
    if at:
        fig, ax = plt.subplots(figsize=(4.8, 3))
        for d, t in at.items():
            xs = list(t)
            ax.plot(range(len(xs)), [t[x]["visual (all latents)"] for x in xs], "o-", label=f"{d}: all video latents")
            ax.plot(range(len(xs)), [t[x]["object_latents"] for x in xs], "s--", label=f"{d}: the written object")
        ax.set_xticks(range(len(xs)), xs)
        ax.set_xlabel("relation number in TRASER's list")
        ax.set_ylabel("attention (mean over layers)")
        ax.legend(fontsize=7)
        fig.tight_layout()
        fig.savefig(figs / "pairs_attention.png", dpi=130)
        plt.close(fig)
        made.append("pairs_attention.png")
    pu = {d: res[d]["push"] for d in res if res[d].get("push", {}).get("alphas")}
    if pu:
        fig, ax = plt.subplots(figsize=(4.5, 3))
        for d, t in pu.items():
            for kind, ls in (("missed", "o-"), ("control", "s--")):
                if kind in t:
                    ax.plot(t["alphas"], t[kind][:-1], ls, label=f"{d}: {'missed human pair' if kind == 'missed' else 'unrelated (control)'}")
        ax.set_xlabel("push size (share of the hidden state's length)")
        ax.set_ylabel("object becomes first choice")
        ax.set_ylim(0, 1)
        ax.legend(fontsize=7)
        fig.tight_layout()
        fig.savefig(figs / "pairs_push.png", dpi=130)
        plt.close(fig)
        made.append("pairs_push.png")
    return made


def pct(x):
    return "-" if x is None else f"{100 * x:.0f}%"


def page(res, out):
    L = ["# Why does TRASER miss the relevant pairs? (pair experiment)", "",
         "Relevant pair = a pair of objects that humans relate (ground truth) and that TRASER received. "
         "Code: `tools/interp/pairs_stage.py` (GPU) and `tools/interp/pairs_report.py` (this page). Ideas from "
         "*Are VLMs Seeing or Just Saying?* (swap the picture halfway, attention to the picture while writing, "
         "asking again as a new turn) and *Do Vision-Language Models Actually See?* (give the answer's structure "
         "as text to bypass seeing; easy-to-see things are found more often).", ""]
    if (Path(out) / "figs" / "pairs_reasons.png").exists():
        L += ["## The answer: why each missed pair was missed", "", "![reasons](figs/pairs_reasons.png)", ""]
    L += ["| dataset | tested missed pairs | A didn't see | B didn't choose | C stopped early | D habit |", "|---|---|---|---|---|---|"]
    for d, r in res.items():
        cnt = r.get("reasons_count", {})
        tot = sum(cnt.values())
        if tot:
            L.append(f"| {d} | {tot} | " + " | ".join(pct(cnt.get(x, 0) / tot) for x in REASONS) + " |")
    L += ["", "How a pair gets its reason (first rule that fits): **C** it writes the pair when the list is re-opened, when "
          "its subject is started for it, or when asked again in a new turn · **D** it fills in the human word (top 5) "
          "also with the video hidden, and the video adds less than 1 nat · **B** it fills in the human word with the "
          "video, or the probe reads \"related\" from its vectors · **A** none of these.", ""]
    L += ["## 1. Is the pair inside the model? (probe vs habit)", "",
          "| dataset | stage | TRASER's vectors | object names only (habit) | both | tricky pairs* | vectors on tricky | habit on tricky |",
          "|---|---|---|---|---|---|---|---|"]
    for d, r in res.items():
        e = r.get("e1", {})
        if e:
            L.append(f"| {d} | {r.get('stage')} | {e.get('video_auc')} | {e.get('habit_auc')} | {e.get('video_plus_habit_auc')} | "
                     f"{e.get('tricky_pairs')} ({e.get('tricky_related')} related) | {e.get('video_auc_tricky')} | {e.get('habit_auc_tricky')} |")
    L += ["", "AUC: 0.5 = guessing, 1 = perfect. *Tricky pairs: the same two object names are related in some videos and "
          "not in others, so the names alone cannot tell. If TRASER's vectors beat the names there, it uses the video.", ""]
    L += ["## 2. Give it the pair: does it fill in the right word?", "",
          "We write `[subject, \"` for it and score every relation word together with the human object. Human word (or an "
          "equivalent) in its top 5:", "", "| dataset | pairs | with the video | video hidden | pair's objects hidden | "
          "picks the human object first (video / hidden) |", "|---|---|---|---|---|---|"]
    for d, r in res.items():
        f = r.get("fill", {})
        for kind in ("missed", "written"):
            g = lambda c, m="ok": f.get(f"{kind}|{c}", {}).get(m)  # noqa: E731
            if g("clean") is not None:
                L.append(f"| {d} | {kind} ({f.get(f'{kind}|clean', {}).get('n')}) | {pct(g('clean'))} | {pct(g('video_hidden'))} | "
                         f"{pct(g('pair_hidden'))} | {pct(g('clean', 'obj1'))} / {pct(g('video_hidden', 'obj1'))} |")
    L += ["", "Same answer with the video hidden = the word comes from habit. Good with the video but never written = it "
          "knew but did not choose.", ""]
    if any(r.get("all", {}).get("videos") for r in res.values()):
        L += ["### 2b. Every human pair of every video, with and without earlier text", "",
              "*fresh* = every human pair (missed + written, no sampling) with no earlier relation (`\"relationships\": "
              "[[s, \"`), so nothing can be copied from TRASER's own answer, which was written with the video; *answer* = "
              "the earlier setup: TRASER's answer re-opened, on every missed pair. Inputs: the video; every latent set to zero; every latent replaced by "
              "another video's latents (normal-looking vectors, wrong content). Human word: rank 1 / top 5 (exact word) / "
              "an equivalent in the top 5; object = the human object picked first after the human word; video raises = "
              "share of pairs where the video gives the human word a higher log-prob than this input (> 1 nat = 2.7x); "
              "AUC = the best word's log-prob separates related from non-related pairs.", "",
              "| dataset | context | pairs | input | rank 1 | top 5 | top 5 (equiv.) | median rank | object first | "
              "video raises | > 1 nat | AUC related vs not |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for d, r in res.items():
            t = r.get("all", {})
            for h in ("fresh", "answer"):
                for kind in ("related", "missed", "written"):
                    for cond in ("clean", "other_video", "zeros"):
                        x = t.get(f"{h}|{kind}|{cond}")
                        if not x:
                            continue
                        au = t.get(f"{h}|auc|{cond}") if kind == "related" else None
                        L.append(f"| {d} | {h} | {kind} ({x['n']}) | {cond.replace('_', ' ')} | {pct(x.get('rank1'))} | "
                                 f"{pct(x.get('top5'))} | {pct(x.get('top5_eq'))} | {x['median_rank']:g} | {pct(x.get('obj1'))} | "
                                 f"{pct(x.get('video_raises'))} | {pct(x.get('video_raises_1nat'))} | "
                                 f"{'-' if au is None else f'{au:.2f}'} |")
        L += ["", "If the video mattered little, *clean* and *other video* would look the same, also in the *fresh* "
              "context. A large gap only in *fresh* means the earlier text carries the video's information in *answer*.", ""]
    L += ["## 3. Keep writing, and swap the video halfway", "",
          "| dataset | videos | new relations when the list is re-opened | of them human pairs | missed pairs tested | "
          "come back: re-opened list | subject started for it | asked again (new turn) |", "|---|---|---|---|---|---|---|---|"]
    for d, r in res.items():
        t = r.get("continue")
        if t and t["videos"]:
            m = t["missed_tested"] or 1
            L.append(f"| {d} | {t['videos']} | {t['new_relations']} | {t['new_human']} | {t['missed_tested']} | "
                     f"{pct(t['kept_writing'] / m)} | {pct(t['cued'] / m)} | {pct(t['reasked'] / m)} |")
    if (Path(out) / "figs" / "pairs_swap.png").exists():
        L += ["", "![swap](figs/pairs_swap.png)", ""]
    L += ["", "Swap: the visual contents of TRASER's two most-used objects are exchanged in the input after it has written "
          "k relations. Following the swapped video = it still looks; following its earlier text = it stopped looking "
          "(VisualSwap's finding).", "", "| dataset | k | follows swapped video | follows old text | videos |", "|---|---|---|---|---|"]
    for d, r in res.items():
        for k, t in (r.get("swap") or {}).items():
            L.append(f"| {d} | {k} | {t['follows_new']} | {t['follows_old']} | {t['videos']} |")
    L += ["", "## 4. Where does it look while writing?", ""]
    if (Path(out) / "figs" / "pairs_attention.png").exists():
        L += ["![attention](figs/pairs_attention.png)", ""]
    L += ["| dataset | relation no. | all video latents | the written object's latents | (if spread evenly) | answer so far | n |", "|---|---|---|---|---|---|---|"]
    for d, r in res.items():
        for b, t in (r.get("attention") or {}).items():
            L.append(f"| {d} | {b} | {t.get('visual (all latents)')} | {t.get('object_latents')} | "
                     f"{t.get('object latents, if spread evenly')} | {t.get('answer')} | {t['n']} |")
    L += ["", "When it closes the list, attention to the objects of the pairs it missed:", "",
          "| dataset | missed pairs' latents | (if spread evenly) | other latents | answer so far | n |", "|---|---|---|---|---|---|"]
    for d, r in res.items():
        t = r.get("attention_end") or {}
        if t.get("n"):
            L.append(f"| {d} | {t.get('missed_pair_latents')} | {t.get('missed latents, if spread evenly')} | "
                     f"{t.get('other_latents')} | {t.get('answer')} | {t['n']} |")
    if any(r.get("e5") for r in res.values()):
        L += ["", "## 5. Which relevant pairs are missed?", "",
              "Miss rate in the lowest vs highest third of each fact (logistic-regression weight: + = more misses):", "",
              "| dataset | fact | miss rate, low third | high third | weight |", "|---|---|---|---|---|"]
        for d, r in res.items():
            e = r.get("e5", {})
            for n, (lo, hi) in (e.get("miss_rate_low_vs_high") or {}).items():
                L.append(f"| {d} | {n} | {pct(lo)} | {pct(hi)} | {e.get('coef', {}).get(n)} |")
    if any(r.get("push", {}).get("alphas") for r in res.values()):
        L += ["", "## 6. Push: how close was it?", "",
              "At the point where it writes the object number (after the human subject and word), the object's own direction "
              "is added in the middle layers. Share of pairs where the object becomes the first choice:", ""]
        if (Path(out) / "figs" / "pairs_push.png").exists():
            L += ["![push](figs/pairs_push.png)", ""]
        L += ["| dataset | push sizes | missed human pairs | unrelated objects (control) |", "|---|---|---|---|"]
        for d, r in res.items():
            t = r.get("push", {})
            if t.get("alphas"):
                L.append(f"| {d} | {t['alphas']} | {t.get('missed', ['-'])[:-1]} (n={t.get('missed', [0])[-1]}) | "
                         f"{t.get('control', ['-'])[:-1]} (n={t.get('control', [0])[-1]}) |")
        L += ["", "A missed human pair that becomes first with a smaller push than an unrelated object = it was close (B)."]
    L += ["",
          "**Caveats.** The human labels are incomplete, so some \"unrelated\" pairs are really related. Only a sample of "
          "missed pairs per video is tested (8 by default). The reasons are rules on these measurements, not certainties."]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True)
    ap.add_argument("--results", default=str(C.RESULTS))
    ap.add_argument("--out", default=str(C.OUT))
    ap.add_argument("--datasets", nargs="+", default=C.DATASETS)
    ap.add_argument("--n", type=json.loads, default={})
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--experiments", nargs="+", type=int, default=[1, 2, 3, 4, 5, 6], help="which experiments go on the page")
    ap.add_argument("--only_all", action="store_true",
                    help="only add experiment 2 on every pair (e2all) to the saved pairs.json; the rest stays as it was")
    args = ap.parse_args()
    import bench_eval as E
    E.RESULTS = Path(args.results)
    if args.only_all:
        res = C.read_json(Path(args.out) / "pairs.json", {})
        for ds in args.datasets:
            t = all_table(ds, args.out)
            if t.get("videos"):
                res.setdefault(ds, {})["all"] = t
                print(f"[pairs] {ds}: experiment 2 on every pair, {t['videos']} videos", flush=True)
        C.write_json(Path(args.out) / "pairs.json", res)
        (Path(args.out) / "PAIRS.md").write_text(page(res, args.out))
        print(f"[pairs] wrote {Path(args.out) / 'PAIRS.md'}")
        return
    probes = C.read_json(Path(args.out) / "probes.json", {})
    res = {}
    for ds in args.datasets:
        vids = C.select_videos(ds, args.n.get(ds), args.seed, args.results)
        videos = [V for V in (Pr.load_video(ds, v, args.work, args.results) for v in vids) if V is not None]
        r, knows = {}, {}
        if len(videos) >= 5:
            stage = probes.get(ds, {}).get("knows", {}).get("stage")
            if not stage or not all(stage in V["stages"] for V in videos):
                stage = "otr"
            print(f"[pairs] {ds}: probes on {len(videos)} videos (stage {stage}) ...", flush=True)
            r, knows = e1_e5(ds, videos, stage, args.seed)
        rows = reasons(ds, args.out, knows)
        r.update({"fill": fill_table(ds, args.out), "continue": continue_table(ds, args.out), "swap": swap_table(ds, args.out),
                  "all": all_table(ds, args.out),
                  "push": push_table(ds, args.out), "reasons": rows,
                  "reasons_count": dict(collections.Counter(x["reason"] for x in rows))})
        r["attention"], r["attention_end"] = attention_table(ds, args.out)
        if 5 not in args.experiments:
            r.pop("e5", None)
        if 6 not in args.experiments:
            r["push"] = {}
        if rows or r.get("e1") or r["all"].get("videos"):
            res[ds] = r
            print(f"[pairs] {ds}: {len(rows)} missed pairs sorted: {r['reasons_count']}", flush=True)
    C.write_json(Path(args.out) / "pairs.json", res)
    figures(res, Path(args.out) / "figs")
    (Path(args.out) / "PAIRS.md").write_text(page(res, args.out))
    print(f"[pairs] wrote {Path(args.out) / 'PAIRS.md'}")


if __name__ == "__main__":
    main()
