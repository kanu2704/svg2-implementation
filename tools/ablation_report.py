"""Is TRASER's fine-tuned language model "just the vocabulary"? On the same videos, next to TRASER itself:
  - TRASER's fine-tuned model alone (bench_run.py --lm traser_plain, run_plain.py): its weights as a standard
    Qwen2.5-VL, the whole video as ordinary video tokens and the objects' boxes as text, no TRASER pipeline;
  - TRASER with its two trained resamplers replaced by plain averaging (--lm traser_meanpool; same layout);
  - the untrained Qwen2.5-VL-7B in TRASER's pipeline with averaging (results/qwen7b_bench).
A model without answers for a dataset is left out of that dataset's table. Three kinds of numbers:

  Table 2      triplet / relation / object, lenient, temporal IoU > 0.5 (one judge alone, rejudge.py; default Nemotron)
  vocabulary   share of the answer's relation words / object names that are in the dataset's human label set (exact,
               after normalising), and how many different relation words it uses
  grounding    human pairs written (any word) and, per object, its own human name vs another object's (exact, no
               judge; qwen_why.py)

    python3 tools/ablation_report.py              # judge new words (NVIDIA key), write results/ablation/README.md
    python3 tools/ablation_report.py --no_ask     # saved verdicts only (unjudged words count as wrong)
"""
import argparse
import collections
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bench_eval as E  # noqa: E402
import qwen_why as W  # noqa: E402
import rejudge as R  # noqa: E402
import repeat_report as RR  # noqa: E402

NAMES = {"pvsg": "PVSG", "vidor": "VidOR", "svg2test": "SVG2test"}
OUT = E.REPO / "results" / "ablation"
RES = E.REPO / "results"


def models(ds):
    """(label, root) per model; TRASER from the repeat runs when they have this dataset (same code and GPU)."""
    rep = E.REPO / "results" / "traser_repeats" / "run1"
    traser = rep if RR.videos(rep, ds) else E.RESULTS
    out = [("TRASER (full pipeline)", traser),
           ("TRASER's fine-tuned model alone (video + boxes as text)", RES / "traser_plain" / "run1"),
           ("TRASER, resamplers replaced by averaging", RES / "traser_meanpool" / "run1"),
           ("Qwen-7B, not fine-tuned, averaging", RES / "qwen7b_bench")]
    return [(label, root) for label, root in out if RR.videos(root, ds)]


def human_vocab(ds):
    rel, obj = set(), set()
    for f in (E.RESULTS / ds / "gt").glob("*.json"):
        gt = json.load(open(f))
        rel |= {E.norm(r["pred"]) for r in gt["relations"]}
        obj |= {E.norm(o["name"]) for o in gt["objects"]}
    return rel, obj


def vocab_stats(loaded, rel_v, obj_v):
    rels, objs = collections.Counter(), collections.Counter()
    n_ans = valid = 0
    for gt, pred, st in loaded.values():
        if pred is None:
            continue
        n_ans += 1
        valid += bool(pred["json_ok"])
        rels.update(E.norm(w) for _, w, _, _ in pred["relations"])
        if isinstance(pred["objects"], dict):
            objs.update(E.norm(n) for n in pred["objects"].values())
    pct = lambda a, b: round(100 * a / b, 1) if b else None  # noqa: E731
    return {"answers": n_ans, "valid_json": valid, "relations_per_answer": round(sum(rels.values()) / max(1, n_ans), 1),
            "relation_words_in_human_vocab": pct(sum(n for w, n in rels.items() if w in rel_v), sum(rels.values())),
            "different_relation_words": len(rels),
            "object_names_in_human_vocab": pct(sum(n for w, n in objs.items() if w in obj_v), sum(objs.values())),
            "top_relation_words": [w for w, _ in rels.most_common(8)]}


def grounding(loaded):
    t = collections.Counter()
    for gt, pred, st in loaded.values():
        if pred is not None:
            t.update(W.counts(gt, pred, st))
    pct = lambda a, b: round(100 * a / b, 1) if b else None  # noqa: E731
    return {"pairs_written": pct(t["written"], t["pairs"]), "own_name": pct(t["own"], t["named"]),
            "another_objects_name": pct(t["other"], t["named"])}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--judge", default=RR.JUDGE)
    ap.add_argument("--no_ask", action="store_true")
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()
    data = {}
    for ds in NAMES:
        ms = models(ds)
        if len(ms) < 2:
            continue
        common = sorted(set.intersection(*[set(RR.videos(root, ds)) for _, root in ms]))
        if common:
            data[ds] = [(label, root, RR.load(root, ds, common)) for label, root in ms]
    if not data:
        raise SystemExit("no answers of results/traser_plain/run1 or results/traser_meanpool/run1 yet "
                         "(traser_repeat_kaggle.py / traser_repeat_run.py with REPEAT_LM=traser_plain REPEAT_RUNS=1)")
    judge = R.Solo(args.judge)
    keys = {E.Judge.key(*p) for ms in data.values() for _, _, x in ms for gt, pred, st in x.values() if pred is not None
            for p in E.video_pairs(gt, pred, st)[0]}
    keys = {k for k in keys if k.split("\t")[1] != k.split("\t")[2]}
    judge.mine().update({k: "mismatch" for k in keys if R.UNNAMED.fullmatch(k.split("\t")[2])})
    todo = sorted(k for k in keys if k not in judge.mine())
    print(f"{len(keys)} different word pairs; {len(todo)} not judged by {args.judge} yet")
    if todo and not args.no_ask:
        client = R.key_from_env()
        R.test(client, args.judge)
        R.judge_all(judge, todo, client, args.workers)
        judge.save()

    L = ["# Is TRASER's fine-tuned language model just the vocabulary?", "",
         "**TRASER's fine-tuned model alone**: the released checkpoint loaded as a standard Qwen2.5-VL-3B (vision "
         "encoder + fine-tuned language model, no resamplers), the whole video as ordinary video tokens and each object "
         "as text, `Object k: <0 - 4 sec> [x1, y1, x2, y2] ...` (its box in each 4 s window, from the cells TRASER "
         "selects for it), after TRASER's own prompt; same JSON answer (`bench_run.py --lm traser_plain`, "
         "`tools/run_plain.py`). ",
         "**TRASER, resamplers replaced by averaging**: the released TRASER (its vision encoder, fine-tuned language "
         "model and special tokens) with the same input layout (\"Object k:\" blocks, `<a - b sec>` window labels, 32 "
         "tokens per object and per window), the same prompt and the same output format, but its two trained "
         "resamplers (Object-Trajectory and Temporal-Window) replaced by plain averaging to the same number of tokens "
         "(`bench_run.py --lm traser_meanpool`). The untrained Qwen2.5-VL-7B ran in the same averaging pipeline "
         f"(`results/qwen7b_bench`). Same videos for all models. Judge: {args.judge} alone, lenient, temporal IoU > 0.5. "
         "Made by `tools/ablation_report.py`.", ""]
    res = {}
    for ds, ms in data.items():
        rel_v, obj_v = human_vocab(ds)
        n = len(next(iter(ms))[2])
        L += [f"## {NAMES[ds]} ({n} videos)", "",
              "| model | triplet | relation | object | relation words in the human vocabulary | different relation "
              "words | object names in the human vocabulary | human pairs written | own name | another object's name "
              "| valid JSON | relations per answer |", "|---|" + "---|" * 11]
        res[ds] = {}
        for label, root, x in ms:
            s, v, g = RR.score(x, judge), vocab_stats(x, rel_v, obj_v), grounding(x)
            res[ds][label] = {"root": str(root.relative_to(E.REPO)), **s, **v, **g}
            L.append(f"| {label} | {s['triplet']} | {s['relation']} | {s['object']} | {v['relation_words_in_human_vocab']}% "
                     f"| {v['different_relation_words']} | {v['object_names_in_human_vocab']}% | {g['pairs_written']}% | "
                     f"{g['own_name']}% | {g['another_objects_name']}% | {v['valid_json']}/{v['answers']} | "
                     f"{v['relations_per_answer']} |")
        L += ["", "Most frequent relation words: " + "; ".join(
            f"*{label}*: {', '.join(res[ds][label]['top_relation_words'])}" for label, _, _ in ms), ""]
        unj = sum(res[ds][label]["unjudged"] for label, _, _ in ms)
        if unj:
            L += [f"*{unj} word pairs not judged yet (counted as wrong): run the report again with the NVIDIA key.*", ""]
    L += ["**How to read it.** If a model without TRASER's pipeline still uses the dataset's words (high \"in the human vocabulary\") "
          "but writes the wrong pairs or puts names on the wrong objects (low \"pairs written\" / \"own name\", high "
          "\"another object's name\"), the fine-tuned language model carries the vocabulary and the resamplers carry the "
          "grounding. If it keeps TRASER's grounding too, the resamplers add little. Exact names are strict: \"adult\" vs "
          "\"person\" counts as another word.", ""]
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "README.md").write_text("\n".join(L) + "\n")
    (OUT / "scores.json").write_text(json.dumps(res, indent=1))
    print("\n".join(L[6:]))
    print(f"wrote {OUT / 'README.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
