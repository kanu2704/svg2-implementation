"""Experiment 2b (every human pair) under the benchmark's lenient judge (Kimi K3), for the relation word and the object.

For each human pair, input (real video / another video's input / video blanked) and context (fresh / after its own
answer), TRASER's 1st choice and its top 5 are checked with the judge:
  relation  right if the judge does not call (human word, TRASER's word) a mismatch, for any of the pair's human words;
  object    right if TRASER picks the human object itself, or an object whose human name the judge accepts for the
            human object's name (e.g. another "adult" when the human pair names one adult).
A combination the judge was never asked counts as wrong (as in the benchmark) and is counted in the "unjudged" column;
`judge_pairs.py` asks the judge about them (another model when Kimi K3 does not answer, for the words Kimi K3 never
judged; the page says which and how often it agrees with Kimi K3). The judge's verdicts are listed too, so they can be
checked by eye.

    python3 tools/interp/pairs_lenient.py    -> results/traser_bench/interp/PAIRS_LENIENT.md + judge_check_*.csv
"""
import argparse
import collections
import csv
import glob
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import bench_eval as E  # noqa: E402
from interp import common as C  # noqa: E402

CONDS = [("clean", "real video"), ("other_video", "another video's input"), ("zeros", "video blanked")]
ROWS = [("fresh", "all human pairs"), ("fresh", "missed"), ("fresh", "written"), ("answer", "missed")]
CTX = {"fresh": "fresh", "answer": "after its own answer"}


def object_names(results, ds, v):
    """TRASER's object number -> the human name of that object (from the saved run's mask columns)."""
    gt = C.read_json(Path(results, ds, "gt", f"{v}.json"), None)
    st = C.read_json(Path(results, ds, "preds", f"{v}.stats.json"), None)
    if not gt or not st or "mask_columns" not in st:
        return {}
    by_col = {o["col"]: o["name"] for o in gt["objects"]}
    return {k + 1: by_col.get(c) for k, c in enumerate(st["mask_columns"])}


def load(raw, results, ds):
    out = []
    for f in sorted(glob.glob(str(Path(raw, "e2all", ds, "*.json")))):
        d = json.load(open(f))
        if "skipped" not in d:
            out.append((d, object_names(results, ds, d.get("video", Path(f).stem))))
    return out


def object_picks(r, k):
    return [o for o, _ in r.get("object_top", [])][:k]


def rel_state(judge, words, picks):
    cats = [judge.category("relation", h, w) for w in picks for h in words]
    if any(E.is_right(c, "lenient") for c in cats):
        return "right"
    return "unjudged" if any(c is None for c in cats) else "wrong"


def obj_state(judge, target, names, picks):
    if target in picks:
        return "right"
    t = names.get(target)
    cats = [judge.category("object", t, names[o]) for o in picks if t and names.get(o)]
    if any(E.is_right(c, "lenient") for c in cats):
        return "right"
    return "unjudged" if any(c is None for c in cats) else "wrong"


def table(judge, vids, what, k):
    """Rows of one table: (context, group) x inputs -> right / unjudged, and the paired flips."""
    lines = [f"| context | pairs | {' | '.join(n for _, n in CONDS)} | only real / only another | only real / only blanked | "
             f"unjudged (real video){' | same object, exact (real video)' if what == 'object' else ''} |",
             "|---|---|---|---|---|---|---|---|" + ("---|" if what == "object" else "")]
    for ctx, group in ROWS:
        items = []
        for d, names in vids:
            pairs = d.get("missed", []) + d.get("written", []) if group == "all human pairs" else d.get(group, [])
            for p in pairs:
                res = p.get(ctx, {})
                if not p.get("words") or not all(res.get(c, {}).get("top") for c, _ in CONDS):
                    continue
                if what == "object" and not all("object_top" in res[c] for c, _ in CONDS):
                    continue
                items.append((p, res, names))
        if not items:
            continue
        st = {}
        for c, _ in CONDS:
            if what == "relation":
                st[c] = [rel_state(judge, p["words"], [t[0] for t in res[c]["top"]][:k]) for p, res, _ in items]
            else:
                st[c] = [obj_state(judge, p["o_k"], names, object_picks(res[c], k)) for p, res, names in items]
        n = len(items)
        ok = {c: [s == "right" for s in st[c]] for c in st}
        cells = [f"{sum(ok[c])} ({100 * sum(ok[c]) / n:.0f}%)" for c, _ in CONDS]
        flip = lambda c: f"{sum(a and not b for a, b in zip(ok['clean'], ok[c]))} / {sum(b and not a for a, b in zip(ok['clean'], ok[c]))}"  # noqa: E731
        row = f"| {CTX[ctx]} | {group} ({n}) | " + " | ".join(cells) + f" | {flip('other_video')} | {flip('zeros')} | {st['clean'].count('unjudged')} |"
        if what == "object":
            exact = sum(p["o_k"] in object_picks(res["clean"], k) for p, res, _ in items)
            row += f" {exact} ({100 * exact / n:.0f}%) |"
        lines.append(row)
    return lines


def checks(judge, vids):
    """Every (human word, TRASER's word) and (human object, another object it picked) among the 1st choices and top 5
    (every input and context), with how often it occurs and the judge's verdict."""
    rel, obj = collections.Counter(), collections.Counter()
    for d, names in vids:
        for p in d.get("missed", []) + d.get("written", []):
            for ctx in ("fresh", "answer"):
                for c, _ in CONDS:
                    r = p.get(ctx, {}).get(c, {})
                    for t in r.get("top", [])[:5]:
                        for h in p.get("words", []):
                            rel[(h, t[0])] += 1
                    for o in object_picks(r, 5):
                        if o != p["o_k"] and names.get(p["o_k"]) and names.get(o):
                            obj[(names[p["o_k"]], names[o])] += 1

    def verdict(kind, a, b):
        c, m = judge.verdict_of(kind, a, b)
        by = f", by {m}" if m and m != E.JUDGES[0] else ""
        return "not judged yet" if c is None else (f"{c} (right{by})" if E.is_right(c, "lenient") else f"{c} (wrong{by})")

    return ([(a, b, n, verdict("relation", a, b)) for (a, b), n in rel.most_common()],
            [(a, b, n, verdict("object", a, b)) for (a, b), n in obj.most_common()])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=str(C.OUT / "raw"))
    ap.add_argument("--results", default=str(C.RESULTS))
    ap.add_argument("--out", default=str(C.OUT))
    ap.add_argument("--show", type=int, default=25, help="judge verdicts listed per dataset (the CSVs have all)")
    args = ap.parse_args()
    E.RESULTS = Path(args.results)
    judge = E.Judge(cache=Path(args.results) / "judge_cache.json", others=True)
    L = ["# Experiment 2b under the lenient judge", "",
         "Every human pair whose two objects TRASER received (`pairs_stage.py --phases e2all`), checked with the benchmark's "
         "judge (Kimi K3, lenient: anything but a mismatch). **Relation**: TRASER's 1st choice / any of its top 5 words for "
         "the pair is accepted for one of the human words. **Object**: given the subject and the human word, the object it "
         "picks first / any of its top 5 is the human object or an object whose human name the judge accepts for it. "
         "Inputs: the real video, another video's input in its place, the video blanked. Context: *fresh* (no earlier "
         "relation) or *after its own answer* (its relation list re-opened; missed pairs only). *only real / only another*: "
         "pairs right with the real video but not the other input / the other way round. *unjudged*: combinations the "
         "judge was never asked, counted as wrong (`python3 tools/interp/judge_pairs.py` asks it).", ""]
    if judge.note():
        L += [f"**Judge.** {judge.note()} Kimi K3's own verdicts always come first.", ""]
    rel_rows, obj_rows = [], []
    for ds in C.DATASETS:
        vids = load(args.raw, args.results, ds)
        if not vids:
            continue
        n_pairs = sum(len(d.get("missed", [])) + len(d.get("written", [])) for d, _ in vids)
        with_obj = sum(1 for d, _ in vids if '"object_top"' in json.dumps(d))
        L += [f"## {ds}: {len(vids)} videos, {n_pairs} human pairs", ""]
        for title, what, k in (("Relation word, TRASER's 1st choice", "relation", 1), ("Relation word, any of its top 5", "relation", 5),
                               ("Object, TRASER's 1st choice", "object", 1), ("Object, any of its top 5", "object", 5)):
            L += [f"### {title}", ""]
            if what == "object" and not with_obj:
                L += ["*Not available yet: these results were made before the run saved the objects it picks "
                      "(re-run `pairs_stage.py --phases e2all`; old files are redone automatically).*", ""]
                continue
            if what == "object" and with_obj < len(vids):
                L += [f"*Objects on {with_obj} of {len(vids)} videos so far (the rest were made before the run saved them).*", ""]
            L += table(judge, vids, what, k) + [""]
        r, o = checks(judge, vids)
        rel_rows += [(ds, *x) for x in r]
        obj_rows += [(ds, *x) for x in o]
        for title, rows in (("relation words", r), ("objects (another object than the human one)", o)):
            if not rows:
                continue
            L += [f"### Check the judge: {title}, most frequent", "",
                  "| human | TRASER | times | judge (Kimi K3) |", "|---|---|---|---|"]
            L += [f"| {a} | {b} | {n} | {v} |" for a, b, n, v in rows[:args.show]] + [""]
            todo = sum(1 for *_, v in rows if v == "not judged yet")
            L += [f"{len(rows)} different combinations, {todo} not judged yet; all of them in `judge_check_*.csv`.", ""]
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "PAIRS_LENIENT.md").write_text("\n".join(L))
    for name, rows, head in (("judge_check_relations.csv", rel_rows, ["dataset", "human word", "TRASER word", "times", "judge"]),
                             ("judge_check_objects.csv", obj_rows, ["dataset", "human object", "picked object", "times", "judge"])):
        with open(out / name, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(head)
            w.writerows(rows)
    print(f"wrote {out / 'PAIRS_LENIENT.md'} and judge_check_*.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
