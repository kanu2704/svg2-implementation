"""Table 2 for the repeated TRASER baseline runs (notebooks/traser_repeat_run.py): every run scored exactly as the paper
describes (lenient semantic criterion, temporal IoU > 0.5; tools/bench_eval.py score_video), with one judge's
verdicts alone (rejudge.py: same prompt, five categories, temperature 0, 50 words per request), then the mean and the
standard deviation over the runs. Words the judge has not seen yet (new words in the new answers) are asked first.

    python3 tools/repeat_report.py                 # judge the new words (NVIDIA key), write results/traser_repeats/README.md
    python3 tools/repeat_report.py --count         # only count the words not judged yet
    python3 tools/repeat_report.py --no_ask        # scores from the saved verdicts only (unjudged words count as wrong)
"""
import argparse
import json
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bench_eval as E  # noqa: E402
import rejudge as R  # noqa: E402

JUDGE = "nvidia/nemotron-3.5-super-vl-120b-a12b"
DATASETS = ["pvsg", "vidor", "svg2test"]
NAMES = {"pvsg": "PVSG", "vidor": "VidOR", "svg2test": "SVG2test"}
METRICS = ["triplet", "relation", "object"]
PAPER = {"triplet": (16.1, 22.9, 16.7), "relation": (16.9, 25.0, 18.7), "object": (72.7, 91.4, 79.0)}


def videos(root, ds):
    d = Path(root) / ds / "preds"
    return sorted(p.stem for p in d.glob("*.json") if not p.name.endswith(".stats.json")) if d.exists() else []


def load(root, ds, vids):
    return {v: E.load_video(ds, v, root) for v in vids}


def score(loaded, judge):
    rows = [E.score_video(gt, pred, st, judge, "lenient", 0.5) for gt, pred, st in loaded.values() if pred is not None]
    t = {k: sum(r[k] for r in rows) for k in rows[0]} if rows else {}
    pct = lambda a, b: round(100 * a / b, 1) if b else None  # noqa: E731
    return {"videos": len(rows), "triplet": pct(t.get("triplet_ok", 0), t.get("relations", 0)),
            "relation": pct(t.get("relation_ok", 0), t.get("relations", 0)),
            "object": pct(t.get("object_ok", 0), t.get("objects", 0)), "unjudged": t.get("unjudged", 0)}


def same_answers(runs, ds, vids):
    """Videos whose raw answer text is identical in every run."""
    texts = [{v: (Path(r) / ds / "preds" / f"{v}.json").read_text() for v in vids} for r in runs]
    return sum(all(t[v] == texts[0][v] for t in texts[1:]) for v in vids)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(E.REPO / "results" / "traser_repeats"), help="folder with run1/, run2/, ...")
    ap.add_argument("--judge", default=JUDGE)
    ap.add_argument("--count", action="store_true", help="only count the words not judged yet")
    ap.add_argument("--no_ask", action="store_true", help="do not ask the judge; unjudged words count as wrong")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--earlier", action=argparse.BooleanOptionalAction, default=True,
                    help="also score the published run (results/traser_bench) as a reference row (default: yes)")
    args = ap.parse_args()
    root = Path(args.root)
    runs = sorted((p for p in root.glob("run*") if p.is_dir()), key=lambda p: int(p.name[3:]) if p.name[3:].isdigit() else 0)
    if not runs:
        raise SystemExit(f"no runs in {root} (run notebooks/traser_repeat_run.py first)")
    # the same videos in every run: those every run answered
    common = {ds: sorted(set.intersection(*[set(videos(r, ds)) for r in runs])) for ds in DATASETS}
    loaded = {(r.name, ds): load(r, ds, common[ds]) for r in runs for ds in DATASETS if common[ds]}
    earlier = E.RESULTS if args.earlier else None       # the published run (Kaggle T4s, float16): a reference row
    if earlier:
        for ds in DATASETS:
            if common[ds] and all((earlier / ds / "preds" / f"{v}.json").exists() for v in common[ds]):
                loaded[("earlier", ds)] = load(earlier, ds, common[ds])
    judge = R.Solo(args.judge)
    keys = {E.Judge.key(*p) for x in loaded.values() for gt, pred, st in x.values() if pred is not None
            for p in E.video_pairs(gt, pred, st)[0]}
    keys = {k for k in keys if k.split("\t")[1] != k.split("\t")[2]}
    judge.mine().update({k: "mismatch" for k in keys if R.UNNAMED.fullmatch(k.split("\t")[2])})
    todo = sorted(k for k in keys if k not in judge.mine())
    print(f"{len(runs)} runs; videos in every run: " + ", ".join(f"{ds} {len(common[ds])}" for ds in DATASETS))
    print(f"{len(keys)} different word pairs; {len(keys) - len(todo)} judged by {args.judge} already, {len(todo)} to ask")
    if args.count:
        return 0
    if todo and not args.no_ask:
        client = R.key_from_env()
        R.test(client, args.judge)
        try:
            R.judge_all(judge, todo, client, args.workers)
        except KeyboardInterrupt:
            judge.save()
            raise SystemExit("\nstopped; every answer so far is saved: run the same command again to continue")
        judge.save()

    res = {r.name: {ds: score(loaded[(r.name, ds)], judge) for ds in DATASETS if common[ds]} for r in runs}
    ref = {ds: score(loaded[("earlier", ds)], judge) for ds in DATASETS if ("earlier", ds) in loaded}
    dss = [ds for ds in DATASETS if common[ds]]
    mean_sd = {}
    for ds in dss:
        for m in METRICS:
            vals = [res[r.name][ds][m] for r in runs]
            mean_sd[(ds, m)] = (statistics.mean(vals), statistics.stdev(vals) if len(vals) > 1 else 0.0)
    unjudged = sum(res[r.name][ds]["unjudged"] for r in runs for ds in dss) + sum(x["unjudged"] for x in ref.values())

    L = [f"# TRASER baseline, {len(runs)} runs: Table 2 with mean and standard deviation", "",
         "Each run: the released `UWGZQ/TRASER` with the paper's official inference settings (1 fps, at most 128 frames, "
         "at most 40 objects, coverage 0.5, 4 s windows, greedy decoding; `notebooks/traser_repeat_run.py`). Scored as in "
         "the paper's Table 2: lenient semantic criterion (anything but a mismatch), temporal IoU > 0.5 for relations and "
         f"triplets, pooled over all human objects / relations of a dataset. Judge: **{args.judge}** alone, with the "
         "paper's lenient setup (`tools/rejudge.py`). Mean ± sample standard deviation (n − 1) over the runs. "
         "Made by `tools/repeat_report.py`.", ""]
    if unjudged:
        L += [f"**{unjudged} word pairs are not judged yet** (they count as wrong): run `python3 tools/repeat_report.py` "
              "again.", ""]
    head = [f"{m.capitalize()} {NAMES[ds]}" for m in METRICS for ds in dss]
    L += ["| | " + " | ".join(head) + " |", "|---|" + "---|" * len(head)]
    L.append("| TRASER, paper | " + " | ".join(f"{PAPER[m][DATASETS.index(ds)]}" for m in METRICS for ds in dss) + " |")
    for r in runs:
        L.append(f"| {r.name} | " + " | ".join(f"{res[r.name][ds][m]}" for m in METRICS for ds in dss) + " |")
    L.append(f"| **mean ± sd ({len(runs)} runs)** | " + " | ".join(
        f"**{mean_sd[(ds, m)][0]:.1f} ± {mean_sd[(ds, m)][1]:.1f}**" for m in METRICS for ds in dss) + " |")
    if ref:
        L.append("| earlier run (Kaggle T4s, float16; not in the mean) | " + " | ".join(
            f"{ref[ds][m]}" if ds in ref else "-" for m in METRICS for ds in dss) + " |")
    L += ["", "## Coverage and how much the runs differ", "",
          "| dataset | videos in every run | videos with the same answer text in every run |", "|---|---|---|"]
    for ds in dss:
        n = same_answers(runs, ds, common[ds])
        L.append(f"| {NAMES[ds]} | {len(common[ds])} | {n} ({100 * n / len(common[ds]):.0f}%) |")
    L += ["", "*Greedy decoding has no randomness, so the runs can only differ through numerical differences on the "
          "GPU; identical answers give a standard deviation of 0.*", ""]
    root.mkdir(parents=True, exist_ok=True)
    (root / "README.md").write_text("\n".join(L) + "\n")
    (root / "scores.json").write_text(json.dumps({"judge": args.judge, "runs": res, "earlier_run": ref, "mean_sd": {
        f"{ds}/{m}": v for (ds, m), v in mean_sd.items()}}, indent=1))
    print("\n".join(L[L.index("| | " + " | ".join(head) + " |"):]))
    print(f"wrote {root / 'README.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
