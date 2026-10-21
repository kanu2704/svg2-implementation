"""Score TRASER and the fine-tuned models on the same test videos; write results/traser_bench/finetune/FINETUNE.md.

Scores (tools/bench_eval.py, as in the main benchmark): triplet recall, relation recall, object accuracy, lenient
(the judge's verdicts on the words; new word pairs are judged only with --ask, which needs your own
NVIDIA_API_KEY) and strict (the same words after normalising). Plus: pair recall (share of the human pairs
between given objects that the answer mentions at all, the problem found by the pair experiment), relations
written per video, and answers cut off before the JSON closes.

    python3 tools/finetune/score.py --models traser sft grpo --train_dataset pvsg
"""
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent))
import bench_eval as E  # noqa: E402
from finetune import common as F  # noqa: E402
from interp import common as IC  # noqa: E402

NAMES = {"traser": "TRASER (no fine-tuning)", "sft": "+ SFT", "grpo": "+ SFT + GRPO", "grpo_only": "+ GRPO (no SFT)"}


def root(model, out):
    return IC.RESULTS if model == "traser" else Path(out, model)


def answer(ds, v, base, gt):
    d = Path(base, ds, "preds")
    return gt, E.parse_prediction((d / f"{v}.json").read_text()), json.load(open(d / f"{v}.stats.json"))


def pair_recall(gt, pred, stats):
    k_of = {c: k + 1 for k, c in enumerate(stats.get("mask_columns", []))}
    gid_k = {o["gt_id"]: k_of[o["col"]] for o in gt["objects"] if o["col"] in k_of}
    gid_k[-1] = -1
    pairs = {(gid_k[r["subj"]], gid_k[r["obj"]]) for r in gt["relations"] if r["subj"] in gid_k and r["obj"] in gid_k}
    said = {(s, o) for s, _, o, _ in pred["relations"]}
    return len(pairs & said), len(pairs)


def score(models, datasets, out, judge, ask):
    res = {}
    for ds in datasets:
        have = [set(IC.answered(ds, root(m, out))) for m in models]
        vids = sorted(set.intersection(*have)) if have else []
        if not vids:
            continue
        gt_of = {v: E.load_video(ds, v, IC.RESULTS)[0] for v in vids}         # one set of human labels for all
        loaded = {m: {v: answer(ds, v, root(m, out), gt_of[v]) for v in vids} for m in models}
        if ask:
            pairs = [p for m in models for v in vids for p in E.video_pairs(gt_of[v], *loaded[m][v][1:])[0]]
            judge.ask_all(pairs)
        res[ds] = {"videos": len(vids)}
        for m in models:
            row = {}
            for crit in ("lenient", "strict"):
                rows = [E.score_video(gt_of[v], loaded[m][v][1], loaded[m][v][2], judge, crit, 0.5) for v in vids]
                tot = {k: sum(r[k] for r in rows) for k in rows[0]}
                pct = lambda a, b: round(100 * a / b, 1) if b else None  # noqa: E731
                row[crit] = {"triplet": pct(tot["triplet_ok"], tot["relations"]), "relation": pct(tot["relation_ok"], tot["relations"]),
                             "object": pct(tot["object_ok"], tot["objects"]), "unjudged": tot["unjudged"]}
            pr = [pair_recall(gt_of[v], loaded[m][v][1], loaded[m][v][2]) for v in vids]
            row["pair_recall"] = round(100 * sum(a for a, _ in pr) / max(1, sum(b for _, b in pr)), 1)
            row["relations_per_video"] = round(sum(len(loaded[m][v][1]["relations"]) for v in vids) / len(vids), 1)
            row["cut_off"] = sum(not loaded[m][v][1]["json_ok"] for v in vids)
            res[ds][m] = row
    return res


def figures(out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    made = []
    figs = Path(out) / "figs"
    figs.mkdir(parents=True, exist_ok=True)
    for name, key, ylabel in (("sft", "loss", "training loss"), ("grpo", "reward_mean", "reward (mean of the group)")):
        p = Path(out) / "logs" / f"{name}.jsonl"
        if not p.exists():
            continue
        recs = [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
        if not recs:
            continue
        ys = [r[key] for r in recs]
        w = max(1, len(ys) // 20)
        smooth = [sum(ys[max(0, i - w):i + 1]) / len(ys[max(0, i - w):i + 1]) for i in range(len(ys))]
        fig, ax = plt.subplots(figsize=(4.5, 2.8))
        ax.plot(ys, alpha=0.3)
        ax.plot(smooth)
        ax.set_xlabel("optimizer step" if name == "sft" else "training video")
        ax.set_ylabel(ylabel)
        ax.set_title(name.upper())
        fig.tight_layout()
        fig.savefig(figs / f"{name}_curve.png", dpi=130)
        plt.close(fig)
        made.append(f"{name}_curve.png")
    return made


def page(res, models, train_ds, figs, judge_note=""):
    L = ["# Fine-tuning TRASER's language model: SFT and GRPO", "",
         f"Trained on **{train_ds}** (training split), tested on the other datasets (and on {train_ds}'s test split, "
         "marked *in-domain*). Only TRASER's language model (Qwen2.5-VL-3B's decoder) is trained, with LoRA; the "
         "vision encoder and resamplers stay frozen. Code: `tools/finetune/`.", "",
         "- **SFT**: copy the human answer (cross-entropy on the human relations written in TRASER's format).",
         "- **GRPO**: write 4 answers per video, reward = triplet F1 + 0.5 x pair F1 against the human labels, "
         "favour the answers better than the group's mean (started from the SFT model).", "",
         "Scores in % (lenient, temporal IoU > 0.5, as in the main benchmark). *pair recall* = human pairs (between "
         "objects it was given) that the answer mentions at all.", ""]
    for ds, r in res.items():
        L += [f"## {ds}" + (" (in-domain)" if ds == train_ds else " (not trained on)") + f", {r['videos']} videos", "",
              "| model | triplet | relation | object | strict triplet | pair recall | relations / video | cut off | unjudged words |",
              "|---|---|---|---|---|---|---|---|---|"]
        for m in models:
            x = r.get(m)
            if x:
                L.append(f"| {NAMES.get(m, m)} | {x['lenient']['triplet']} | {x['lenient']['relation']} | {x['lenient']['object']} | "
                         f"{x['strict']['triplet']} | {x['pair_recall']} | {x['relations_per_video']} | {x['cut_off']} | "
                         f"{x['lenient']['unjudged']} |")
        L.append("")
    for f in figs:
        L += [f"![{f}](figs/{f})", ""]
    L += ["**Notes.** Unjudged words count as wrong under lenient scoring (run with `--ask` and your own key to judge "
          "them). TRASER's answers are its saved run (float16, up to 8192 tokens, with attributes); the fine-tuned "
          "models write no attributes (the human labels have none) and up to 4096 tokens. PVSG training videos that "
          "are also VidOR test videos are left out of training." + (f" Judge: {judge_note}" if judge_note else "")]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="+", default=["traser", "sft", "grpo"])
    ap.add_argument("--datasets", nargs="+", default=["vidor", "svg2test", "pvsg"])
    ap.add_argument("--train_dataset", default="pvsg")
    ap.add_argument("--out", default=str(F.OUT))
    ap.add_argument("--ask", action="store_true", help="ask the judge about new word pairs (needs NVIDIA_API_KEY)")
    ap.add_argument("--judge", default="auto", help="with --ask: model to ask (auto: Kimi K3, else the next that answers)")
    args = ap.parse_args()
    judge = E.pick_judge(wanted=args.judge) if args.ask else E.Judge(others=True)
    if args.ask:
        judge.check()
    models = [m for m in args.models if m == "traser" or Path(args.out, m).exists()]
    res = score(models, args.datasets, args.out, judge, args.ask)
    IC.write_json(Path(args.out) / "finetune.json", res)
    figs = figures(args.out)
    (Path(args.out) / "FINETUNE.md").write_text(page(res, models, args.train_dataset, figs, judge.note()))
    print(f"wrote {Path(args.out) / 'FINETUNE.md'}")
    for ds, r in res.items():
        print(ds, {m: r[m]["lenient"]["triplet"] for m in models if m in r})


if __name__ == "__main__":
    sys.exit(main())
