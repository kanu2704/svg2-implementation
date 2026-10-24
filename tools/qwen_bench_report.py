"""Table 2 again, with TRASER's language model replaced by an off-the-shelf Qwen2.5-VL-7B-Instruct (no scene-graph
training) inside TRASER's own pipeline (tools/run_traser.py load_qwen; answers by tools/bench_run.py --lm qwen7b into
results/qwen7b_bench/<dataset>/preds/).

Scored exactly as the main benchmark (tools/bench_eval.py score_video: lenient, temporal IoU > 0.5), with TRASER's own
answers on the same videos next to it. A word no judge was asked about counts as wrong and is counted ("unjudged").

    python3 tools/qwen_bench_report.py                       # -> results/qwen7b_bench/README.md + scores.json
    python3 tools/qwen_bench_report.py --ask [--judge auto]  # judge the new words first (NVIDIA key)
    python3 tools/qwen_bench_report.py --unjudged words.json # list the words not judged yet (kind, human, predicted)
"""
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bench_eval as E  # noqa: E402

QRES = E.REPO / "results" / "qwen7b_bench"
DATASETS = ["pvsg", "vidor", "svg2test"]
MODELS = [("traser", "TRASER (released weights), ours", E.RESULTS),
          ("qwen7b", "Qwen2.5-VL-7B-Instruct in TRASER's pipeline (not fine-tuned), ours", QRES)]
# the paper's Table 2 (lenient, tIoU 0.5), for reference
PAPER = {"TRASER, paper": {"triplet": (16.1, 22.9, 16.7), "relation": (16.9, 25.0, 18.7), "object": (72.7, 91.4, 79.0)},
         "Qwen2.5-VL-3B (no fine-tuning), paper": {"triplet": (0.1, 0.2, 0.2), "relation": (0.1, 0.4, 0.3),
                                                   "object": (10.4, 45.0, 24.2)}}


def answered(root, ds):
    d = Path(root) / ds / "preds"
    return sorted(p.stem for p in d.glob("*.json") if not p.name.endswith(".stats.json")) if d.exists() else []


def load(datasets):
    """{dataset: {model: {video: (gt, pred, stats)}}} on the videos Qwen answered (TRASER on the same ones)."""
    out = {}
    for ds in datasets:
        vids = answered(QRES, ds)
        if vids:
            out[ds] = {m: {v: E.load_video(ds, v, root) for v in vids} for m, _, root in MODELS}
    return out


def needed(loaded):
    return [p for ds in loaded.values() for vids in ds.values() for gt, pred, st in vids.values() if pred is not None
            for p in E.video_pairs(gt, pred, st)[0]]


def scores(loaded, judge):
    res = {}
    for ds, models in loaded.items():
        res[ds] = {}
        for m, vids in models.items():
            done = [x for x in vids.values() if x[1] is not None]
            rows = [E.score_video(*x, judge, "lenient", 0.5) for x in done]
            tot = {k: sum(r[k] for r in rows) for k in rows[0]} if rows else {}
            pct = lambda a, b: round(100 * a / b, 1) if b else None  # noqa: E731
            res[ds][m] = {"videos": len(done), "json_ok": sum(bool(p["json_ok"]) for _, p, _ in done),
                          "triplet": pct(tot.get("triplet_ok", 0), tot.get("relations", 0)),
                          "relation": pct(tot.get("relation_ok", 0), tot.get("relations", 0)),
                          "object": pct(tot.get("object_ok", 0), tot.get("objects", 0)),
                          "relation_any_time": pct(tot.get("relation_ok_any_time", 0), tot.get("relations", 0)),
                          "unjudged": tot.get("unjudged", 0),
                          "answer_tokens": round(sum(st.get("new_tokens", 0) for _, _, st in done) / max(1, len(done)))}
    return res


def page(res, judge_note):
    ds_cols = [ds for ds in DATASETS if ds in res]
    L = ["# Table 2 with TRASER's language model replaced by an untrained Qwen2.5-VL-7B", "",
         "TRASER's pipeline (same frames, same masks, same token selection and trajectory-aligned arrangement, same "
         "window labels, same prompt) with **Qwen2.5-VL-7B-Instruct, not fine-tuned** as vision encoder and language "
         "model. TRASER's two trained resamplers only fit its own 3B model, so each is replaced by plain averaging to "
         "the same 32 tokens per object and per window (nothing learned); TRASER's own trained special tokens are left "
         "out. TRASER learned its answer format in training, so the prompt adds a description of that JSON format (as "
         "the paper's baselines got a JSON template). Code: `tools/run_traser.py` (`load_qwen`), "
         "`tools/bench_run.py --lm qwen7b`, this page `tools/qwen_bench_report.py`.", "",
         "Lenient semantic criterion, temporal IoU > 0.5, scored by `tools/bench_eval.py` exactly as TRASER's answers; "
         "TRASER's numbers are on the same videos as Qwen's.", ""]
    head = ["Triplet", "Relation", "Object"]
    L += ["| | " + " | ".join(f"{h} {ds}" for h in head for ds in ds_cols) + " |",
          "|---|" + "---|" * (len(head) * len(ds_cols))]
    idx = {ds: DATASETS.index(ds) for ds in ds_cols}
    for name, vals in PAPER.items():
        L.append(f"| {name} | " + " | ".join(f"{vals[h.lower()][idx[ds]]}" for h in head for ds in ds_cols) + " |")
    for m, name, _ in MODELS:
        cells = [res[ds][m][h.lower()] for h in head for ds in ds_cols]
        L.append(f"| **{name}** | " + " | ".join("-" if c is None else f"{c}" for c in cells) + " |")
    L += ["", "## Coverage", "",
          "| dataset | model | videos | answers that are valid JSON | answer tokens (mean) | relation word right at any time | unjudged words |",
          "|---|---|---|---|---|---|---|"]
    for ds in ds_cols:
        for m, name, _ in MODELS:
            r = res[ds][m]
            L.append(f"| {ds} | {name} | {r['videos']} | {r['json_ok']} | {r['answer_tokens']} | {r['relation_any_time']} | {r['unjudged']} |")
    L += ["", "*Unjudged words count as wrong (`--ask` or another judge fills them in). Qwen sometimes leaves an object "
          "unnamed (\"object 3\"): such a name was judged a mismatch.*" + (f" Judge: {judge_note}" if judge_note else "")]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--datasets", nargs="+", default=DATASETS)
    ap.add_argument("--ask", action="store_true", help="ask a judge about the words not judged yet (NVIDIA key)")
    ap.add_argument("--judge", default="auto", help="with --ask: the model (auto: Kimi K3, else the next that answers)")
    ap.add_argument("--unjudged", default=None, help="write the words not judged yet to this JSON file and stop")
    args = ap.parse_args()
    cache = E.RESULTS / "judge_cache.json"
    loaded = load(args.datasets)
    if not loaded:
        raise SystemExit(f"no Qwen answers yet in {QRES}/<dataset>/preds")
    judge = E.Judge(cache=cache, others=True)
    pairs = needed(loaded)
    todo = sorted({judge.key(*p) for p in pairs if judge.category(*p) is None})
    print(f"{len(set(judge.key(*p) for p in pairs))} (human, predicted) word pairs; {len(todo)} not judged yet")
    if args.unjudged:
        Path(args.unjudged).write_text(json.dumps(todo, indent=0))
        print(f"wrote {args.unjudged}")
        return 0
    if args.ask and todo:
        judge = E.pick_judge(cache, args.judge)
        judge.check()
        judge.ask_all(pairs)
        judge.save()
    res = scores(loaded, judge)
    QRES.mkdir(parents=True, exist_ok=True)
    (QRES / "scores.json").write_text(json.dumps(res, indent=1))
    (QRES / "README.md").write_text(page(res, judge.note()))
    print(f"wrote {QRES / 'README.md'}")
    for ds, r in res.items():
        print(ds, {m: (x["videos"], x["triplet"], x["relation"], x["object"]) for m, x in r.items()})
    return 0


if __name__ == "__main__":
    sys.exit(main())
