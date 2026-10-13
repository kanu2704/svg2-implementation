"""Diagnosis, part A: where TRASER loses its points (outputs only, no GPU).

Every human relation is followed through the steps it has to pass to be counted right, and the first step it
fails is recorded:

    0  not_given       one of the two objects was not given to TRASER (40-object cap, no mask on its frames)
    1a reversed_only   TRASER wrote the pair only the other way round (B -> A)
    1b pair_missing    TRASER wrote nothing for these two objects
    2  word_wrong      pair written, but no relation word matches (lenient judge)
    3  time_wrong      a word matches, but temporal IoU <= 0.5
    4  name_wrong      relation right, but an object name is a mismatch (fails the triplet only)
       right           relation and triplet right

Same rules as tools/bench_eval.py (lenient, tIoU > 0.5, VidOR occurrences merged): relation recall is
(name_wrong + right) / all and triplet recall right / all, so the README numbers come out again.

Next to each relation it records facts that may explain the failure (relation word and type, length, video
length, number of objects, tokens TRASER kept for each object, input position, names, cut-off answers,
loops) and, when tools/mask_features.py has been run on the machine with the masks, object sizes, time
on screen together and the gap between the two masks. It also sorts every relation TRASER wrote (matches a
human relation, human pair with another relation, reverse of a human pair, extra pair) with flags for the
extra ones.

    python3 tools/error_analysis.py            # writes results/traser_bench/diagnosis/{ERRORS.md, *.csv}
"""
import argparse
import collections
import csv
import json
import random
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))
import bench_eval as E  # noqa: E402

OUT = E.RESULTS / "diagnosis"
DATASETS = ["pvsg", "svg2test", "vidor"]

STEPS = [("not_given", "0. object not given to TRASER"),
         ("reversed_only", "1a. pair written only the other way round"),
         ("pair_missing", "1b. pair not written at all"),
         ("word_wrong", "2. pair written, relation word wrong"),
         ("time_wrong", "3. word right, time wrong"),
         ("name_wrong", "4. relation right, an object name wrong (triplet only)"),
         ("right", "relation and triplet right")]
WRITTEN = {"word_wrong", "time_wrong", "name_wrong", "right"}
WORD_OK = {"time_wrong", "name_wrong", "right"}
REL_OK = {"name_wrong", "right"}

# Pure position words (VidOR's own 8 spatial predicates include towards/away). Our list, used for grouping only.
POSITION = {"on", "in", "in front of", "behind", "above", "below", "under", "beneath", "inside", "beside", "next to",
            "near", "adjacent to", "over", "against", "on top of", "left of", "right of", "towards", "toward",
            "away", "in_front_of", "next_to", "close to", "underneath", "outside"}
LIVING = {"person", "people", "adult", "man", "woman", "men", "women", "child", "children", "kid", "baby", "boy", "girl",
          "toddler", "player", "human", "guy", "lady", "dog", "cat", "horse", "bird", "cow", "sheep", "elephant",
          "animal", "duck", "goose", "fish", "chicken", "monkey", "bear", "lion", "tiger", "zebra", "giraffe", "pig",
          "rabbit", "hamster", "penguin", "squirrel", "camel", "kangaroo", "turtle", "crab", "frog", "snake",
          "leopard", "panda", "antelope", "stingray", "puppy", "kitten", "hen", "deer", "goat", "parrot", "swan"}


def norm(w):
    return E.norm(w)


def is_position(word):
    return norm(word) in POSITION


def is_living(name):
    return any(t in LIVING for t in norm(name).replace("/", " ").replace("-", " ").split())


def bin_of(x, edges, labels):
    """labels[i] for the first edge with x < edge, else the last label; None stays None."""
    if x is None:
        return None
    for e, lab in zip(edges, labels):
        if x < e:
            return lab
    return labels[-1]


def load_mask_features(ds, root):
    d = Path(root, ds)
    return {p.stem: json.load(open(p)) for p in d.glob("*.json")} if d.exists() else {}


def mask_sources(datasets, root):
    """{dataset: {"masks": n videos, "boxes": n videos}} of the measurements on disk."""
    out = {}
    for ds in datasets:
        c = collections.Counter(f.get("source", "masks") for f in load_mask_features(ds, root).values())
        if c:
            out[ds] = dict(c)
    return out


def analyse(datasets, judge, mask_root=OUT / "mask_features"):
    """Rows for every human relation, every object TRASER was given and every relation TRASER wrote."""
    ok = lambda kind, a, b: E.is_right(judge.category(kind, a, b), "lenient")  # noqa: E731
    human_rows, object_rows, traser_rows = [], [], []
    for ds in datasets:
        mf_all = load_mask_features(ds, mask_root)
        loaded = {v: E.load_video(ds, v) for v in E.video_ids(ds)}
        loaded = {v: x for v, x in loaded.items() if x[1] is not None}
        word_count = collections.Counter(norm(r["pred"]) for gt, _, _ in loaded.values() for r in gt["relations"])
        rank = {w: i for i, (w, _) in enumerate(word_count.most_common())}
        for v, (gt, pred, st) in loaded.items():
            _, name, pname, by_pair = E.video_pairs(gt, pred, st)
            given = E.given_objects(gt, st)
            k_of_col = {c: k + 1 for k, c in enumerate(st["mask_columns"])}
            col_of = {o["gt_id"]: o["col"] for o in gt["objects"]}
            k_of = {g: k_of_col.get(c) for g, c in col_of.items()}
            tokens = st.get("tokens_per_object") or []
            tok_of = {g: (tokens[k - 1] if k and k - 1 < len(tokens) else None) for g, k in k_of.items()}
            n_given = len(st["mask_columns"])
            unit_s = st["duration_s"] / max(1, st["sampled_frames"]) if gt["time_unit"] == "index" else 1.0
            dur = st["duration_s"]
            name_ok = {g: (g in pname and ok("object", name[g], pname[g])) for g in name}
            name_ok[-1] = True
            used = {g for pair in by_pair for g in pair}
            human_pairs = collections.defaultdict(list)
            for r in gt["relations"]:
                human_pairs[(r["subj"], r["obj"])].append(r)
            raw = [(s, norm(p), o, json.dumps(sp)) for s, p, o, sp in pred["relations"]]
            loops = len(raw) != len(set(raw))
            cut = not pred["json_ok"]
            mf = mf_all.get(v, {})
            mobj, mpair = mf.get("objects", {}), mf.get("pairs", {})
            stuff = {o["gt_id"] for o in gt["objects"] if o.get("is_thing") is False}

            # ---- human relations
            for r in gt["relations"]:
                s, o = r["subj"], r["obj"]
                best_tiou, words = None, [p for p, _ in by_pair.get((s, o), [])]
                if not (s in given and o in given):
                    step = "not_given"
                elif (s, o) not in by_pair:
                    step = "reversed_only" if (o, s) in by_pair else "pair_missing"
                else:
                    word_ok = [E.pred_spans(sp, gt, st) for p, sp in by_pair[(s, o)] if ok("relation", r["pred"], p)]
                    if not word_ok:
                        step = "word_wrong"
                    else:
                        best_tiou = max(E.tiou(r["spans"], sp) for sp in word_ok)
                        step = ("time_wrong" if best_tiou <= 0.5 else
                                "name_wrong" if not (name_ok.get(s) and name_ok.get(o)) else "right")
                ks = [k_of.get(g) for g in (s, o) if g != -1]
                toks = [tok_of.get(g) for g in (s, o) if g != -1 and tok_of.get(g) is not None]
                areas = [mobj[str(g)]["area"] for g in (s, o) if str(g) in mobj]
                pk = mpair.get(",".join(str(x) for x in sorted((s, o))), {}) if -1 not in (s, o) else {}
                rel_s = E.length(E.merge(r["spans"])) * unit_s
                human_rows.append({
                    "dataset": ds, "video": v, "source": gt.get("source") or ds, "subj": s, "obj": o,
                    "subj_name": name.get(s, "camera"), "obj_name": name.get(o, "camera"), "pred": r["pred"],
                    "step": step, "pred_type": "position" if is_position(r["pred"]) else "action/other",
                    "pred_rank": rank[norm(r["pred"])] + 1, "rel_s": round(rel_s, 2),
                    "rel_share": round(rel_s / dur, 3) if dur else None, "video_s": round(dur, 1),
                    "n_objects": len(gt["objects"]), "n_given": n_given,
                    "subj_tokens": tok_of.get(s), "obj_tokens": tok_of.get(o), "min_tokens": min(toks) if toks else None,
                    "last_pos": round(max(ks) / n_given, 3) if ks and None not in ks and n_given else None,
                    "camera": -1 in (s, o), "subj_living": s == -1 or is_living(name.get(s, "")),
                    "subj_named_right": bool(name_ok.get(s)), "obj_named_right": bool(name_ok.get(o)),
                    "subj_used": s in used or s == -1, "obj_used": o in used or o == -1,
                    "answer_cut": cut, "answer_loops": loops, "best_tiou": None if best_tiou is None else round(best_tiou, 3),
                    "traser_words": "; ".join(words), "traser_reverse_words": "; ".join(p for p, _ in by_pair.get((o, s), [])),
                    "min_area": min(areas) if len(areas) == len([g for g in (s, o) if g != -1]) and areas else None,
                    "co_s": pk.get("co_s"), "gap": pk.get("gap"), "touch_s": pk.get("touch_s"),
                    "human_s": E._fmt_spans(r["spans"], gt["time_unit"])})

            # ---- objects TRASER was given
            in_human = {g for p in human_pairs for g in p}
            for g, k in k_of.items():
                if g not in given or g == -1 or k is None:
                    continue
                object_rows.append({
                    "dataset": ds, "video": v, "gt_id": g, "k": k, "name": name[g], "traser_name": pname.get(g, ""),
                    "named_right": bool(name_ok.get(g)), "tokens": tok_of.get(g), "pos": round(k / n_given, 3),
                    "in_human_relation": g in in_human, "in_traser_relation": g in used, "stuff": g in stuff,
                    "area": mobj.get(str(g), {}).get("area"), "visible_s": mobj.get(str(g), {}).get("visible_s")})

            # ---- relations TRASER wrote
            fan = collections.defaultdict(set)
            for s, p, o, _ in pred["relations"]:
                fan[(s, norm(p))].add(o)
            gid_of_col = {c: g for g, c in col_of.items()}
            to_gt = {k + 1: gid_of_col.get(c) for k, c in enumerate(st["mask_columns"])}
            to_gt[-1] = -1
            seen = set()
            for (s, p, o, sp), key in zip(pred["relations"], raw):
                gs, go = to_gt.get(s), to_gt.get(o)
                repeat = key in seen
                seen.add(key)
                if gs is None or go is None:
                    kind = "invalid object number"
                elif (gs, go) in human_pairs:
                    sp2 = E.pred_spans(sp, gt, st)
                    hit = any(ok("relation", r["pred"], p) and E.tiou(r["spans"], sp2) > 0.5 for r in human_pairs[(gs, go)])
                    kind = "matches a human relation" if hit else "human pair, other relation"
                elif (go, gs) in human_pairs:
                    kind = "reverse of a human pair"
                else:
                    kind = "extra pair"
                traser_rows.append({
                    "dataset": ds, "video": v, "subj_k": s, "obj_k": o, "subj": gs, "obj": go, "pred": p,
                    "kind": kind, "position_word": is_position(p),
                    "background": bool({gs, go} & stuff),
                    "misnamed": not (name_ok.get(gs, False) and name_ok.get(go, False)),
                    "repeat": repeat, "fan_out": len(fan[(s, norm(p))]) >= 5, "answer_cut": cut,
                    "subj_name": pname.get(gs, "camera" if gs == -1 else "?"), "obj_name": pname.get(go, "camera" if go == -1 else "?")})
    return human_rows, object_rows, traser_rows


# ----------------------------------------------------------------------------- report
FACTORS = [
    ("pred_type", "Relation type (our position-word list vs everything else)", ["position", "action/other"],
     lambda r: r["pred_type"]),
    ("pred_rank", "How common the relation word is in this dataset", ["top 10 words", "words 11-50", "rarer words"],
     lambda r: bin_of(r["pred_rank"], [11, 51], ["top 10 words", "words 11-50", "rarer words"])),
    ("rel_s", "Relation length", ["< 2 s", "2-5 s", "5-15 s", ">= 15 s"],
     lambda r: bin_of(r["rel_s"], [2, 5, 15], ["< 2 s", "2-5 s", "5-15 s", ">= 15 s"])),
    ("rel_share", "Relation length as a share of the video", ["< 25%", "25-50%", "50-90%", ">= 90%"],
     lambda r: bin_of(r["rel_share"], [0.25, 0.5, 0.9], ["< 25%", "25-50%", "50-90%", ">= 90%"])),
    ("video_s", "Video length", ["< 15 s", "15-40 s", "40-90 s", ">= 90 s"],
     lambda r: bin_of(r["video_s"], [15, 40, 90], ["< 15 s", "15-40 s", "40-90 s", ">= 90 s"])),
    ("n_objects", "Human objects in the video", ["<= 5", "6-10", "11-20", "21-40", "> 40"],
     lambda r: bin_of(r["n_objects"], [6, 11, 21, 41], ["<= 5", "6-10", "11-20", "21-40", "> 40"])),
    ("min_tokens", "Image tokens TRASER kept for the smaller object of the pair (before compression)",
     ["< 50", "50-200", "200-1000", ">= 1000"],
     lambda r: bin_of(r["min_tokens"], [50, 200, 1000], ["< 50", "50-200", "200-1000", ">= 1000"])),
    ("last_pos", "Input position of the later object (Object k of n)", ["first quarter", "second", "third", "last quarter"],
     lambda r: bin_of(r["last_pos"], [0.25001, 0.50001, 0.75001], ["first quarter", "second", "third", "last quarter"])),
    ("subj_living", "Subject is a person or animal (camera counts)", ["yes", "no"],
     lambda r: "yes" if r["subj_living"] else "no"),
    ("names", "TRASER named both objects right (lenient)", ["both", "one", "neither"],
     lambda r: ["neither", "one", "both"][int(r["subj_named_right"]) + int(r["obj_named_right"])]),
    ("answer_cut", "Answer cut off at 8,192 tokens", ["no", "yes"], lambda r: "yes" if r["answer_cut"] else "no"),
    ("answer_loops", "Answer repeats a relation word for word", ["no", "yes"], lambda r: "yes" if r["answer_loops"] else "no"),
    ("min_area", "Size of the smaller object (share of the frame; from the masks)", ["< 0.5%", "0.5-2%", "2-10%", ">= 10%"],
     lambda r: bin_of(r["min_area"], [0.005, 0.02, 0.10], ["< 0.5%", "0.5-2%", "2-10%", ">= 10%"])),
    ("co_s", "Seconds both objects are on screen together (from the masks)", ["0 s", "< 5 s", "5-15 s", ">= 15 s"],
     lambda r: None if r["co_s"] is None else "0 s" if r["co_s"] == 0 else bin_of(r["co_s"], [5, 15], ["< 5 s", "5-15 s", ">= 15 s"])),
    ("gap", "Closest gap between the two masks (share of the frame diagonal; from the masks)",
     ["touching (<= 1%)", "1-5%", "5-20%", ">= 20%"],
     lambda r: bin_of(r["gap"], [0.01001, 0.05, 0.20], ["touching (<= 1%)", "1-5%", "5-20%", ">= 20%"])),
]


def pct(a, b):
    return f"{100 * a / b:.0f}%" if b else "–"


def funnel(rows):
    c = collections.Counter(r["step"] for r in rows)
    return c, len(rows)


def report(human, objects, traser, datasets, seed=0, sources=None):
    by_ds = {ds: [r for r in human if r["dataset"] == ds] for ds in datasets}
    ds_cols = [d for d in datasets if by_ds[d]]
    L = ["# Where TRASER loses its points (diagnosis, part A)", "",
         "Made by `tools/error_analysis.py` from the saved answers (no GPU). Same scoring as `README.md`: lenient judge, "
         "temporal IoU > 0.5, VidOR occurrences merged. Every human relation is followed until the first step it fails. "
         "Row by row: `errors.csv` (human relations), `objects.csv` (objects TRASER was given), "
         "`traser_relations.csv` (every relation TRASER wrote).", ""]

    # 1. funnel
    L += ["## 1. Where each human relation fails", "",
          "| step | " + " | ".join(ds_cols) + " |", "|---" * (1 + len(ds_cols)) + "|"]
    fun = {d: funnel(by_ds[d]) for d in ds_cols}
    for key, label in STEPS:
        L.append(f"| {label} | " + " | ".join(f"{fun[d][0][key]} ({pct(fun[d][0][key], fun[d][1])})" for d in ds_cols) + " |")
    L.append("| **all human relations** | " + " | ".join(str(fun[d][1]) for d in ds_cols) + " |")
    L += ["", "Check against `README.md` (lenient, tIoU 0.5): relation = steps 4 + right, triplet = right only.", "",
          "| | " + " | ".join(ds_cols) + " |", "|---" * (1 + len(ds_cols)) + "|",
          "| Relation recall | " + " | ".join(pct(sum(fun[d][0][k] for k in REL_OK), fun[d][1]) for d in ds_cols) + " |",
          "| Triplet recall | " + " | ".join(pct(fun[d][0]["right"], fun[d][1]) for d in ds_cols) + " |"]

    # 2. the guesses in numbers
    L += ["", "## 2. The guesses (hypotheses) in numbers", ""]
    for d in ds_cols:
        rows = [r for r in by_ds[d] if r["step"] != "not_given"]
        c = collections.Counter(r["step"] for r in rows)
        notw = [r for r in rows if r["step"] in ("reversed_only", "pair_missing")]
        both_used = sum(r["subj_used"] and r["obj_used"] for r in notw)
        t = [x for x in traser if x["dataset"] == d]
        tk = collections.Counter(x["kind"] for x in t)
        extra = [x for x in t if x["kind"] == "extra pair"]
        matched = [x for x in t if x["kind"] == "matches a human relation"]
        written = [r for r in rows if r["step"] in WRITTEN]
        L += [f"**{d}** ({len(rows)} human relations whose objects TRASER was given)", "",
              f"- **H1 pair choice:** {pct(len(notw), len(rows))} never get their pair written "
              f"({pct(c['reversed_only'], len(rows))} only the other way round). In {pct(both_used, len(notw))} of those, "
              f"TRASER used *both* objects in other relations, just not together.",
              f"- **H2 habit:** position words are {pct(sum(x['position_word'] for x in extra), len(extra))} of TRASER's extra "
              f"relations vs {pct(sum(x['position_word'] for x in matched), len(matched))} of the ones that match a human relation; "
              f"{pct(tk['extra pair'], len(t))} of everything TRASER writes is an extra pair.",
              f"- **H3 time:** {pct(c['time_wrong'], len(written))} of written pairs have the right word but the wrong time.",
              f"- **H5 loops:** {pct(sum(x['repeat'] for x in t), len(t))} of TRASER's relations repeat an earlier one word "
              f"for word; {pct(sum(x['answer_cut'] for x in t), len(t))} come from answers cut off at 8,192 tokens.",
              f"- **H6 direction:** {pct(c['reversed_only'], len(rows))} of human relations are written only the other way round.", ""]
    L.append("H4 (small objects) is in section 5.")

    # 3. factors
    L += ["", "## 3. When does it fail?", "",
          "Human relations whose objects TRASER was given. Per group: **n**, **pair** = pair written (steps 2-4 and right), "
          "**word** = relation word right among written pairs, **rel.** = relation right (counts in the recall). "
          "The line under each table compares the first and last group of *pair written* (≈: within 5 points; "
          "groups with fewer than 30 relations left out).", "",
          "Measurements from the masks (size, time on screen together, gap): "
          + ("; ".join(f"{d}: " + ", ".join(f"{n} videos from {k}" for k, n in c.items()) for d, c in sources.items())
             if sources else "not made yet (run `tools/mask_features.py` where the masks are), so those tables are missing")
          + ".", ""]
    for key, title, labels, fn in FACTORS:
        groups = {d: collections.defaultdict(list) for d in ds_cols}
        for d in ds_cols:
            for r in by_ds[d]:
                if r["step"] == "not_given":
                    continue
                b = fn(r)
                if b is not None:
                    groups[d][b].append(r)
        if not any(groups[d] for d in ds_cols):
            continue
        L += [f"### {title}", "", "| group | " + " | ".join(f"{d} n | pair | word | rel." for d in ds_cols) + " |",
              "|---" + "|---|---|---|---" * len(ds_cols) + "|"]
        for lab in labels:
            cells = []
            for d in ds_cols:
                g = groups[d].get(lab, [])
                w = [r for r in g if r["step"] in WRITTEN]
                cells.append(f"{len(g)} | {pct(len(w), len(g))} | {pct(sum(r['step'] in WORD_OK for r in w), len(w))} | "
                             f"{pct(sum(r['step'] in REL_OK for r in g), len(g))}")
            L.append(f"| {lab} | " + " | ".join(cells) + " |")
        trend = []
        for d in ds_cols:
            big = [(lab, groups[d][lab]) for lab in labels if len(groups[d].get(lab, [])) >= 30]
            if len(big) < 2:
                trend.append(f"{d}: –")
                continue
            a = sum(r["step"] in WRITTEN for r in big[0][1]) / len(big[0][1])
            b = sum(r["step"] in WRITTEN for r in big[-1][1]) / len(big[-1][1])
            arrow = "≈" if abs(a - b) < 0.05 else ("↑" if b > a else "↓")
            trend.append(f"{d}: {100 * a:.0f}% → {100 * b:.0f}% {arrow}")
        L += ["", "Pair written, first → last group: " + "; ".join(trend), ""]

    # 4. relation words
    L += ["## 4. Relation words", "", "The 15 most common human relation words of each dataset (relations whose objects TRASER was given).", ""]
    for d in ds_cols:
        words = collections.defaultdict(list)
        for r in by_ds[d]:
            if r["step"] != "not_given":
                words[norm(r["pred"])].append(r)
        L += [f"**{d}**", "", "| word | n | pair written | word right (of written) | relation right |", "|---|---|---|---|---|"]
        for w, g in sorted(words.items(), key=lambda x: -len(x[1]))[:15]:
            wr = [r for r in g if r["step"] in WRITTEN]
            L.append(f"| {w} | {len(g)} | {pct(len(wr), len(g))} | {pct(sum(r['step'] in WORD_OK for r in wr), len(wr))} | "
                     f"{pct(sum(r['step'] in REL_OK for r in g), len(g))} |")
        L.append("")

    # 5. objects
    L += ["## 5. Objects: tokens kept, size, names (H4)", "",
          "Every object TRASER was given. **named right** = lenient judge; **in TRASER rel.** / **in human rel.** = the "
          "object appears in at least one relation of TRASER / of the humans.", ""]
    for key, title, edges, labels in (
            ("tokens", "Image tokens kept (before compression)", [50, 200, 1000], ["< 50", "50-200", "200-1000", ">= 1000"]),
            ("area", "Size (share of the frame, from the masks)", [0.005, 0.02, 0.10], ["< 0.5%", "0.5-2%", "2-10%", ">= 10%"])):
        if not any(o.get(key) is not None for o in objects):
            continue
        L += [f"### {title}", "", "| group | " + " | ".join(f"{d} n | named right | in TRASER rel. | in human rel." for d in ds_cols) + " |",
              "|---" + "|---|---|---|---" * len(ds_cols) + "|"]
        for lab in labels:
            cells = []
            for d in ds_cols:
                g = [o for o in objects if o["dataset"] == d and bin_of(o.get(key), edges, labels) == lab]
                cells.append(f"{len(g)} | {pct(sum(o['named_right'] for o in g), len(g))} | "
                             f"{pct(sum(o['in_traser_relation'] for o in g), len(g))} | {pct(sum(o['in_human_relation'] for o in g), len(g))}")
            L.append(f"| {lab} | " + " | ".join(cells) + " |")
        L.append("")

    # 6. what TRASER writes
    kinds = ["matches a human relation", "human pair, other relation", "reverse of a human pair", "extra pair", "invalid object number"]
    L += ["## 6. What TRASER writes", "", "Every relation in TRASER's answers (repeats included).", "",
          "| kind | " + " | ".join(ds_cols) + " |", "|---" * (1 + len(ds_cols)) + "|"]
    tby = {d: [x for x in traser if x["dataset"] == d] for d in ds_cols}
    for k in kinds:
        L.append(f"| {k} | " + " | ".join(f"{sum(x['kind'] == k for x in tby[d])} ({pct(sum(x['kind'] == k for x in tby[d]), len(tby[d]))})"
                                          for d in ds_cols) + " |")
    L += ["| **all** | " + " | ".join(str(len(tby[d])) for d in ds_cols) + " |", "",
          "Extra pairs, what they look like (one relation can have several flags):", "",
          "| flag | " + " | ".join(ds_cols) + " |", "|---" * (1 + len(ds_cols)) + "|"]
    for flag, label in (("position_word", "position word"), ("misnamed", "an object named wrong"),
                        ("background", "floor/wall/sky-type object (PVSG only)"), ("repeat", "repeats an earlier relation word for word"),
                        ("fan_out", "same subject and word written for 5+ objects"), ("answer_cut", "answer cut off")):
        ex = {d: [x for x in tby[d] if x["kind"] == "extra pair"] for d in ds_cols}
        L.append(f"| {label} | " + " | ".join(pct(sum(x[flag] for x in ex[d]), len(ex[d])) for d in ds_cols) + " |")

    # 7. examples
    rnd = random.Random(seed)
    L += ["", "## 7. Examples", "", "Six random human relations per step and dataset (seed 0). *TRASER for this pair* lists its "
          "relation words for the same two objects, *reverse* those for the other direction.", ""]
    for d in ds_cols:
        L += [f"### {d}", ""]
        for key, label in STEPS:
            g = [r for r in by_ds[d] if r["step"] == key]
            if not g:
                continue
            L += [f"**{label}**", "", "| video | human relation | TRASER for this pair | reverse |", "|---|---|---|---|"]
            for r in rnd.sample(g, min(6, len(g))):
                L.append(f"| {r['video']} | {r['subj_name']} #{r['subj']} → {r['pred']} → {r['obj_name']} #{r['obj']} "
                         f"[{r['human_s']}] | {r['traser_words'] or '–'} | {r['traser_reverse_words'] or '–'} |")
            L.append("")
    return "\n".join(L) + "\n"


def write_csv(path, rows):
    if not rows:
        return
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--datasets", nargs="+", default=DATASETS)
    ap.add_argument("--out", default=str(OUT))
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    human, objects, traser = analyse(args.datasets, E.Judge(), mask_root=out / "mask_features")
    write_csv(out / "errors.csv", human)
    write_csv(out / "objects.csv", objects)
    write_csv(out / "traser_relations.csv", traser)
    (out / "ERRORS.md").write_text(report(human, objects, traser, args.datasets,
                                          sources=mask_sources(args.datasets, out / "mask_features")))
    print(f"wrote {out / 'ERRORS.md'} ({len(human)} human relations, {len(objects)} objects, {len(traser)} TRASER relations)")


if __name__ == "__main__":
    main()
