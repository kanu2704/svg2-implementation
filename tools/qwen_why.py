"""Why the untrained Qwen-7B scores so low in TRASER's pipeline, with no judge involved (exact names only):

  human pairs written  share of the human pairs (between objects it was given) that its answer mentions at all,
                       with any word (tools/finetune/score.py pair_recall);
  names                for each object it named: the human name of THIS object (exact, after normalising), or
                       instead the human name of ANOTHER object it was given in the same video (it named something
                       in the video, but put the name on the wrong object number).

    python3 tools/qwen_why.py      -> results/qwen7b_bench/WHY.md
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bench_eval as E  # noqa: E402
import qwen_bench_report as Q  # noqa: E402
from finetune import score as S  # noqa: E402

NAMES = {"pvsg": "PVSG", "vidor": "VidOR", "svg2test": "SVG2test"}


def counts(gt, pred, st):
    written, pairs = S.pair_recall(gt, pred, st)
    by_col = {o["col"]: E.norm(o["name"]) for o in gt["objects"]}
    human = {k + 1: by_col.get(c) for k, c in enumerate(st.get("mask_columns", []))}
    given = {h for h in human.values() if h}
    named = own = other = 0
    for k, h in human.items():
        p = pred["objects"].get(k) if h and isinstance(pred["objects"], dict) else None
        if p is None:
            continue
        p = E.norm(p)
        named += 1
        own += p == h
        other += p != h and p in given
    return dict(written=written, pairs=pairs, named=named, own=own, other=other)


def main():
    loaded = Q.load(Q.DATASETS)
    pct = lambda a, b: f"{100 * a / b:.0f}%" if b else "-"  # noqa: E731
    L = ["# Why Qwen-7B (not fine-tuned) fails in TRASER's pipeline", "",
         "No judge: exact names after normalising (lower case, \"_\" -> \" \"). **Human pairs written**: share of the human "
         "pairs between objects it was given that its answer mentions at all, with any word. **Own name**: the object "
         "got the human name of that very object. **Another object's name**: it got the human name of a different "
         "object it was given in the same video (the name is in the video, but on the wrong object number). Made by "
         "`tools/qwen_why.py`.", "",
         "| dataset | model | human pairs written | objects named | own name | another object's name |",
         "|---|---|---|---|---|---|"]
    for ds in Q.DATASETS:
        if ds not in loaded:
            continue
        for m, name in (("traser", "TRASER"), ("qwen7b", "Qwen-7B")):
            t = {}
            for gt, pred, st in loaded[ds][m].values():
                if pred is not None:
                    for k, v in counts(gt, pred, st).items():
                        t[k] = t.get(k, 0) + v
            L.append(f"| {NAMES[ds]} | {name} | {t['written']:,} of {t['pairs']:,} ({pct(t['written'], t['pairs'])}) | "
                     f"{t['named']:,} | {t['own']:,} ({pct(t['own'], t['named'])}) | {t['other']:,} ({pct(t['other'], t['named'])}) |")
    out = Q.QRES / "WHY.md"
    out.write_text("\n".join(L) + "\n")
    print("\n".join(L[-7:]))
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
