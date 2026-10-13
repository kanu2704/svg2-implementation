"""Interpretability report: reads results/traser_bench/interp/raw/<phase>/... and probes.json, writes
results/traser_bench/interp/REPORT.md (+ figures in figs/). Runs anywhere (CPU), on whatever is there so far.

    python3 tools/interp/report.py
"""
import argparse
import collections
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent))
from interp import common as C  # noqa: E402

GROUPS = [("s", "subject number"), ("pred", "relation word"), ("o", "object number"), ("time", "times")]


def load(out, phase):
    d = Path(out) / "raw" / phase
    res = collections.defaultdict(list)
    if d.exists():
        for f in sorted(d.glob("*/*.json")):
            res[f.parent.name].append(json.load(open(f)))
    return res


def pct(x):
    return "–" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{100 * x:.0f}%"


def num(x, d=2):
    return "–" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:.{d}f}"


def mean(xs):
    xs = [x for x in xs if x is not None]
    return float(np.mean(xs)) if xs else None


def median(xs):
    xs = [x for x in xs if x is not None]
    return float(np.median(xs)) if xs else None


def figure(path, draw):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        return None
    fig = draw(plt)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=120, bbox_inches="tight")
    plt.close(fig)
    return path


# ----------------------------------------------------------------------------- sections
def sec_p0(out):
    data = load(out, "p0")
    L = ["## 0. Check: the harness reproduces TRASER", "",
         "The language model alone (exported weights) on the saved input sequences, compared with TRASER's saved answers. "
         "*Greedy*: how many of the first 300 tokens it writes again identically. *Teacher-forced*: how often its most "
         "likely next token is TRASER's token, over the whole answer. High values mean every experiment below works on "
         "the same model and input that produced the answers.", "",
         "| dataset | video | greedy: same first tokens | teacher-forced agreement |", "|---|---|---|---|"]
    for ds, rows in data.items():
        for r in rows:
            L.append(f"| {ds} | {r['video']} | {r.get('greedy_same_prefix')}/{r.get('compared')} | {pct(r.get('teacher_forced_argmax_agreement'))} |")
    if not data:
        L.append("| – | not run yet | | |")
    return L


def sec_probes(out, figs):
    P = C.read_json(Path(out) / "probes.json", {})
    L = ["", "## 1. Where is the information? (probes)", "",
         "ROC AUC of a small classifier trained on TRASER's vectors at each stage (0.5 = chance, 1 = perfect; tested on "
         "videos it was not trained on). `vision` = vision encoder tokens of the object, `otr` / `twr` = the two "
         "resamplers' latents, `lm_L` = the language model after layer L (over the object's latents). Where a row drops, "
         "the information is lost; where it stays high but TRASER still misses relations, the information is there and "
         "not used.", ""]
    if not P:
        return L + ["Not run yet."]
    tasks = [("related", "pair: do humans relate subject → object"), ("written", "pair: did TRASER write the pair"),
             ("action", "pair (related): action word vs only position words"), ("touch", "pair: do the masks touch"),
             ("in_human", "object: in any human relation"), ("moving", "object: moving fast vs slow"),
             ("active", "window: is the relation happening in this 4-second window")]
    for ds, R in P.items():
        stages = R["stages"]
        L += [f"### {ds} ({R['videos']} videos)", "", "| question | n (positives) | " + " | ".join(stages) + " |",
              "|---" * (2 + len(stages)) + "|"]
        for t, label in tasks:
            if t not in R["auc"]:
                continue
            row = R["auc"][t]
            cells = [num(row.get(s)) if s in row else "" for s in stages]
            if t == "active":
                cells = [num(row.get(s)) if s in row else "·" for s in stages]
            n = R["n"].get(t, ["", ""])
            L.append(f"| {label} | {n[0]} ({n[1]}) | " + " | ".join(cells) + " |")
        c, k = R.get("controls", {}), R.get("knows", {})
        if c:
            L += ["", f"Controls for *related*: shuffled labels {num(c.get('shuffled_labels', {}).get('auc'))}; "
                  f"geometry only (on screen together, gap, touching, sizes, motion, tokens, person/animal) "
                  f"{num(c.get('geometry_only', {}).get('auc'))}; geometry + `{c.get('geometry_plus_best_stage', {}).get('stage')}` "
                  f"{num(c.get('geometry_plus_best_stage', {}).get('auc'))}."]
        if k:
            L += ["", f"**Known but not written?** At `{k['stage']}` (best stage for *related*), "
                  f"{pct(k.get('missed_above'))} of the {k.get('missed_pairs')} human pairs TRASER did *not* write score above "
                  f"90% of unrelated pairs, vs {pct(k.get('written_above'))} of the {k.get('written_pairs')} pairs it did write."]
        L.append("")

    def draw(plt):
        tasks_fig = [t for t, _ in tasks if any(t in R["auc"] for R in P.values())]
        fig, axes = plt.subplots(1, len(tasks_fig), figsize=(3.2 * len(tasks_fig), 3), squeeze=False)
        for ax, t in zip(axes[0], tasks_fig):
            for ds, R in P.items():
                row = R["auc"].get(t, {})
                xs = [s for s in R["stages"] if row.get(s) is not None] if t != "active" else \
                     [s for s in R["window_stages"] if row.get(s) is not None]
                ax.plot(range(len(xs)), [row[s] for s in xs], marker="o", label=ds)
                ax.set_xticks(range(len(xs)))
                ax.set_xticklabels(xs, rotation=90, fontsize=6)
            ax.axhline(0.5, color="grey", lw=0.5)
            ax.set_title(t, fontsize=9)
            ax.set_ylim(0.4, 1.0)
        axes[0][0].legend(fontsize=7)
        return fig
    f = figure(figs / "probes.png", draw)
    if f:
        L += ["![probe AUC by stage](figs/probes.png)", ""]
    return L


def rank_stats(rows, key):
    r = [x[key]["rank"] for x in rows if x.get(key)]
    return len(r), median(r), (np.mean([v <= 1 for v in r]) if r else None), (np.mean([v <= 3 for v in r]) if r else None), \
        (np.mean([v <= 5 for v in r]) if r else None)


def sec_p2a(out, figs):
    data = load(out, "p2a")
    L = ["", "## 2. Does it know relations it does not write? (forced continuation)", "",
         "After TRASER's last relation we start one more, with the subject of a human relation, and score every possible "
         "next piece exactly: the subject number among all objects, the relation word among the dataset's common words, the "
         "object number among all objects. *missed* = human relations whose pair TRASER never wrote; *written* = ones it "
         "wrote with the right word (should rank high); *control* = a random other object / word in the same slot.", ""]
    if not data:
        return L + ["Not run yet."]
    L += ["| dataset | relations | subject: median rank (control) | word: in top 5 (control) | word: same-meaning word in top 5 | "
          "object: rank 1 (control) | object: top 3 (control) | **all three** (control) |", "|---|---|---|---|---|---|---|---|"]
    stops = {}
    for ds, vids in data.items():
        tested = [t for v in vids for t in v.get("tested", [])]
        stops[ds] = [v.get("p_stop_after_each", []) for v in vids if v.get("p_stop_after_each")]
        for kind in ("missed", "written"):
            rows = [t for t in tested if t["kind"] == kind]
            if not rows:
                continue
            s, sc = rank_stats(rows, "subject"), rank_stats(rows, "subject_control")
            w, wc = rank_stats(rows, "word"), rank_stats(rows, "word_control")
            o, oc = rank_stats(rows, "object"), rank_stats(rows, "object_control")
            eq = mean([float(t["word_equivalent_in_top5"]) for t in rows if t.get("word_equivalent_in_top5") is not None])

            def all3(t, ctrl=False):
                sk, wk, ok = ("subject_control", "word_control", "object_control") if ctrl else ("subject", "word", "object")
                if not (t.get(sk) and t.get(wk) and t.get(ok)):
                    return None
                wtop = t[wk]["rank"] <= 5 or (not ctrl and t.get("word_equivalent_in_top5"))
                return float(t[sk]["rank"] <= 3 and wtop and t[ok]["rank"] <= 3)
            L.append(f"| {ds} {kind} | {len(rows)} | {num(s[1], 0)} ({num(sc[1], 0)}) | {pct(w[4])} ({pct(wc[4])}) | {pct(eq)} | "
                     f"{pct(o[2])} ({pct(oc[2])}) | {pct(o[3])} ({pct(oc[3])}) | "
                     f"**{pct(mean([all3(t) for t in rows]))}** ({pct(mean([all3(t, True) for t in rows]))}) |")
    ends = {ds: [v.get("p_stop_at_end") for v in vids if v.get("p_stop_at_end") is not None] for ds, vids in data.items()}
    L += ["", "*all three* = subject in the top 3, word in the top 5 (or a same-meaning word), object in the top 3.", "",
          "**Stopping.** Probability that TRASER closes its relation list, at the point where it did: " +
          "; ".join(f"{ds} mean {pct(mean(v))}" for ds, v in ends.items()) + "."]

    def draw(plt):
        fig, ax = plt.subplots(figsize=(5, 3))
        for ds, seqs in stops.items():
            m = max((len(s) for s in seqs), default=0)
            ys = [mean([s[i] for s in seqs if len(s) > i]) for i in range(min(m, 40))]
            ax.plot(range(1, len(ys) + 1), ys, label=ds)
        ax.set_xlabel("after TRASER's relation number")
        ax.set_ylabel("P(stop here)")
        ax.legend(fontsize=7)
        return fig
    if any(stops.values()):
        f = figure(figs / "stop.png", draw)
        if f:
            L += ["", "![probability of stopping after each relation](figs/stop.png)"]
    return L


def sec_p2b(out):
    import error_analysis as A
    data = load(out, "p2b")
    L = ["", "## 3. What does each part of the input do? (interventions)", "",
         "Change in log-probability (nats; negative = TRASER's own answer became less likely) of each part of its relations "
         "when part of the input is removed (set to zero). Teacher-forced on TRASER's answer, so the answer itself does not change.", ""]
    if not data:
        return L + ["Not run yet."]
    conds = [("blank_all", "all visual latents"), ("blank_otr", "OTR latents only (whole-video summary)"),
             ("blank_twr", "TWR latents only (4-second windows)"), ("labels_reversed", "time labels reversed")]
    L += ["| dataset | removed | " + " | ".join(g for _, g in GROUPS) + " | relations |", "|---|---|" + "---|" * (len(GROUPS) + 1)]
    for ds, vids in data.items():
        vids = [v for v in vids if "logprobs" in v]
        for c, label in conds:
            deltas = collections.defaultdict(list)
            for v in vids:
                for a, b in zip(v["logprobs"]["clean"], v["logprobs"].get(c, [])):
                    for g, _ in GROUPS:
                        deltas[g].append(b[g] - a[g])
            L.append(f"| {ds} | {label} | " + " | ".join(num(mean(deltas[g])) for g, _ in GROUPS) + f" | {len(deltas['s'])} |")
    # by word type
    L += ["", "**Which relation words need the video?** Change of the relation word's log-probability with all visual latents removed:", "",
          "| dataset | position words | other words | top words (change) |", "|---|---|---|---|"]
    for ds, vids in data.items():
        by = collections.defaultdict(list)
        per_word = collections.defaultdict(list)
        for v in (x for x in vids if "logprobs" in x):
            for r, a, b in zip(v["relations"], v["logprobs"]["clean"], v["logprobs"]["blank_all"]):
                d = b["pred"] - a["pred"]
                by["position" if A.is_position(r["pred"]) else "other"].append(d)
                per_word[r["pred"].lower()].append(d)
        common = sorted(per_word.items(), key=lambda x: -len(x[1]))[:8]
        L.append(f"| {ds} | {num(mean(by['position']))} | {num(mean(by['other']))} | " +
                 ", ".join(f"{w} {num(mean(d))}" for w, d in common) + " |")
    # one object
    L += ["", "**Removing one object.** Mean change for relations that involve the removed object vs relations that do not "
          "(if the model reads each object from its own latents, only the first should drop):", "",
          "| dataset | involving it: object number | involving it: word | not involving it: object number | not involving it: word |",
          "|---|---|---|---|---|"]
    for ds, vids in data.items():
        inv_o, inv_w, oth_o, oth_w = [], [], [], []
        for v in (x for x in vids if "logprobs" in x):
            for k in v.get("objects_blanked", []):
                for r, a, b in zip(v["relations"], v["logprobs"]["clean"], v["logprobs"].get(f"blank_object_{k}", [])):
                    if k in (r["s_k"], r["o_k"]):
                        inv_o.append(b["o"] - a["o"])
                        inv_w.append(b["pred"] - a["pred"])
                    else:
                        oth_o.append(b["o"] - a["o"])
                        oth_w.append(b["pred"] - a["pred"])
        L.append(f"| {ds} | {num(mean(inv_o))} | {num(mean(inv_w))} | {num(mean(oth_o))} | {num(mean(oth_w))} |")
    # time
    L += ["", "**Where do the times come from?** The time labels `<a - b sec>` are reversed (the first window gets the last "
          "label, ...) while the video latents stay. We compare TRASER's times with the same times moved to where the reversed "
          "labels would put them. If times are read from the labels, the moved times become the more likely ones.", "",
          "| dataset | relations | clean labels: original times preferred | reversed labels: moved times preferred | "
          "mean preference for moved times (clean → reversed, nats) |", "|---|---|---|---|---|"]
    for ds, vids in data.items():
        a_, b_, d0, d1 = [], [], [], []
        for v in (x for x in vids if "logprobs" in x):
            lp = v["logprobs"]
            for j in range(v.get("mapped_relations", 0)):
                c0, c1 = lp["clean"][j]["time"], lp["clean_mapped_answer"][j]["time"]
                r0, r1 = lp["labels_reversed"][j]["time"], lp["labels_reversed_mapped_answer"][j]["time"]
                if c0 == c1 and r0 == r1:
                    continue                              # times that do not move (middle window)
                a_.append(float(c0 > c1))
                b_.append(float(r1 > r0))
                d0.append(c1 - c0)
                d1.append(r1 - r0)
        L.append(f"| {ds} | {len(a_)} | {pct(mean(a_))} | {pct(mean(b_))} | {num(mean(d0))} → {num(mean(d1))} |")
    L += ["", "**Windows of a relation.** Removing the TWR latents of both objects in the windows where the relation happens, "
          "vs in the same number of other windows of the same two objects:", "",
          "| dataset | tests | times: own windows | times: other windows | word: own windows | word: other windows |", "|---|---|---|---|---|---|"]
    for ds, vids in data.items():
        rows = collections.defaultdict(list)
        for v in (x for x in vids if "logprobs" in x):
            lp = v["logprobs"]
            for t in v.get("window_tests", []):
                j = t["relation"]
                base = lp["clean"][j]
                for side in ("own", "other"):
                    x = lp[t["name"] + "_" + side][j]
                    rows["time_" + side].append(x["time"] - base["time"])
                    rows["pred_" + side].append(x["pred"] - base["pred"])
        L.append(f"| {ds} | {len(rows['time_own'])} | {num(mean(rows['time_own']))} | {num(mean(rows['time_other']))} | "
                 f"{num(mean(rows['pred_own']))} | {num(mean(rows['pred_other']))} |")
    return L


def sec_p2c(out, figs):
    data = load(out, "p2c")
    L = ["", "## 4. Where is the object decided? (activation patching)", "",
         "One object of a relation TRASER wrote is removed (its latents set to zero), which makes the object number less likely. "
         "Then its clean hidden states are put back at one layer only: *at its latents* (does the model still need the object's "
         "own positions at that layer?) or *at the position that writes the number* (has the decision been assembled there by "
         "that layer?). Recovery = share of the lost log-probability that comes back (1 = all).", ""]
    if not data:
        return L + ["Not run yet."]
    curves = {}
    for ds, vids in data.items():
        rows = [t for v in vids for t in v.get("tested", []) if t["lp_clean"] - t["lp_corrupt"] > 0.5]
        if not rows:
            L.append(f"{ds}: no relation lost more than 0.5 nats when its object was removed.")
            continue
        layers = rows[0]["layers"]
        rec = {k: [mean([(t[k][i] - t["lp_corrupt"]) / (t["lp_clean"] - t["lp_corrupt"]) for t in rows]) for i in range(len(layers))]
               for k in ("lp_patch_object", "lp_patch_decision")}
        curves[ds] = (layers, rec)
        L += [f"**{ds}** ({len(rows)} relations; mean drop when removed {num(mean([t['lp_clean'] - t['lp_corrupt'] for t in rows]))} nats)", "",
              "| layer | " + " | ".join(str(x) for x in layers) + " |", "|---" * (1 + len(layers)) + "|",
              "| at its latents | " + " | ".join(num(x) for x in rec["lp_patch_object"]) + " |",
              "| at the writing position | " + " | ".join(num(x) for x in rec["lp_patch_decision"]) + " |", ""]

    def draw(plt):
        fig, axes = plt.subplots(1, 2, figsize=(8, 3))
        for ds, (layers, rec) in curves.items():
            axes[0].plot(layers, rec["lp_patch_object"], marker="o", label=ds)
            axes[1].plot(layers, rec["lp_patch_decision"], marker="o", label=ds)
        axes[0].set_title("patched at the object's latents", fontsize=9)
        axes[1].set_title("patched at the writing position", fontsize=9)
        for ax in axes:
            ax.set_xlabel("layer")
            ax.set_ylim(-0.1, 1.1)
        axes[0].set_ylabel("recovery")
        axes[0].legend(fontsize=7)
        return fig
    if curves:
        f = figure(figs / "patching.png", draw)
        if f:
            L += ["![recovery by layer](figs/patching.png)", ""]
    return L


def sec_p3(out, figs):
    data = load(out, "p3")
    L = ["", "## 5. Where do the written tokens look? (attention)", "",
         "Attention (averaged over heads) from the position that writes each token. Shown as *enrichment*: the share of "
         "attention a part of the input gets divided by its share of the positions (1 = no preference, 10 = ten times more than "
         "its size). Only answers + inputs up to the length limit.", ""]
    if not data:
        return L + ["Not run yet."]
    curves = {}
    for qtype, title in (("time", "Tokens that write a **time**"), ("object_id", "Tokens that write an **object number**"),
                         ("word", "Tokens that write a **relation word**")):
        L += [f"**{title}** (middle and last layers; mass / enrichment)", ""]
        for ds, vids in data.items():
            vids = [v for v in vids if "mass" in v]
            if not vids:
                continue
            cats = vids[0]["categories"][qtype]
            n_layers = len(vids[0]["mass"])
            mass = collections.defaultdict(list)
            enr = collections.defaultdict(list)
            for v in vids:
                M = np.array(v["mass"])
                S = np.array(v["share"])
                for qi, (t, _) in enumerate(v["queries"]):
                    if t != qtype:
                        continue
                    for ci, c in enumerate(cats):
                        for li in range(n_layers):
                            mass[(c, li)].append(M[li, qi, ci])
                            if S[qi, ci] > 0:
                                enr[(c, li)].append(M[li, qi, ci] / S[qi, ci])
            layers = sorted({n_layers // 2, n_layers - 1})
            L += [f"*{ds}* ({len(vids)} videos)", "", "| part of the input | " + " | ".join(f"layer {li}" for li in layers) + " |",
                  "|---" * (1 + len(layers)) + "|"]
            for c in cats:
                L.append(f"| {c.replace('_', ' ')} | " + " | ".join(f"{pct(mean(mass[(c, li)]))} / {num(mean(enr[(c, li)]), 1)}×"
                                                                     for li in layers) + " |")
            L.append("")
            if qtype == "time":
                curves[ds] = [mean(enr[("own_window_latents", li)]) for li in range(n_layers)], \
                             [mean(enr[("own_window_label", li)]) for li in range(n_layers)], \
                             [mean(enr[("other_windows_latents", li)]) for li in range(n_layers)]
    inv = sum(len(v.get("invalid_object_numbers", [])) for vids in data.values() for v in vids)
    L.append(f"Relations naming an object number that is not in the input: {inv} (in the videos with attention).")

    def draw(plt):
        fig, axes = plt.subplots(1, len(curves), figsize=(4 * len(curves), 3), squeeze=False)
        for ax, (ds, (own, lab, other)) in zip(axes[0], curves.items()):
            ax.plot(own, label="own window latents")
            ax.plot(lab, label="own window label")
            ax.plot(other, label="other windows latents")
            ax.set_title(f"{ds}: time tokens", fontsize=9)
            ax.set_xlabel("layer")
            ax.set_ylabel("enrichment")
            ax.legend(fontsize=6)
        return fig
    if curves:
        f = figure(figs / "attention_time.png", draw)
        if f:
            L += ["", "![attention of time tokens by layer](figs/attention_time.png)"]
    return L


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(C.OUT))
    args = ap.parse_args()
    out = Path(args.out)
    figs = out / "figs"
    L = ["# TRASER interpretability report", "",
         "Made by `tools/interp/` (stage 1 `encode_stage.py`, stage 2 `lm_stage.py`, `probe.py`, this `report.py`). "
         "Raw results per video are in `raw/<phase>/<dataset>/`. Everything is measured on TRASER's released checkpoint and "
         "its own saved answers.", ""]
    L += sec_p0(out) + sec_probes(out, figs) + sec_p2a(out, figs) + sec_p2b(out) + sec_p2c(out, figs) + sec_p3(out, figs)
    (out / "REPORT.md").write_text("\n".join(L) + "\n")
    print("wrote", out / "REPORT.md")


if __name__ == "__main__":
    main()
