"""How much does TRASER place relations in time? Its relation recall with its own time spans, against the same answers
with every relation's time replaced by the whole video, and with time ignored (right pair and word at any time).
Lenient, temporal IoU > 0.5, one judge's verdicts alone (rejudge.py).

    python3 tools/time_baseline.py [--judge nvidia/nemotron-3.5-super-vl-120b-a12b]   -> results/traser_bench/TIME.md
"""
import argparse
import copy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bench_eval as E  # noqa: E402
import rejudge as R  # noqa: E402

NAMES = {"pvsg": "PVSG", "vidor": "VidOR", "svg2test": "SVG2test"}


def whole_video(pred, st):
    out = copy.deepcopy(pred)
    out["relations"] = [(s, w, o, [[0, st["sampled_frames"] - 1]]) for s, w, o, _ in pred["relations"]]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--judge", default="nvidia/nemotron-3.5-super-vl-120b-a12b")
    args = ap.parse_args()
    judge = R.Solo(args.judge)
    L = ["# Does TRASER place relations in time?", "",
         f"Relation recall (lenient, judge: {args.judge} alone): a human relation is found when TRASER has the same two "
         "objects with a right word, and its time spans overlap the human ones with temporal IoU > 0.5. **Whole video**: "
         "the same answers with every relation's time replaced by the whole video. **Any time**: time not checked (the "
         "most timing could give). \"Spanning the video\": total length ≥ 90% of the video. Made by `tools/time_baseline.py`.", "",
         "| dataset | human relations spanning the video | TRASER's relations spanning the video | relation recall, whole video "
         "| relation recall, its own times | relation recall, any time |", "|---|---|---|---|---|---|"]
    for ds in NAMES:
        done = [x for x in (E.load_video(ds, v) for v in E.video_ids(ds)) if x[1] is not None]
        full_p = n_p = full_h = n_h = 0
        own, whole = [], []
        for gt, pred, st in done:
            length = st["sampled_frames"] if gt["time_unit"] == "index" else st["duration_s"]
            for _, _, _, sp in pred["relations"]:
                n_p += 1
                full_p += E.length(E.merge(E.pred_spans(sp, gt, st))) >= 0.9 * length
            for r in gt["relations"]:
                n_h += 1
                full_h += E.length(E.merge(E.to_spans(r.get("spans", [])))) >= 0.9 * length
            own.append(E.score_video(gt, pred, st, judge, "lenient", 0.5))
            whole.append(E.score_video(gt, whole_video(pred, st), st, judge, "lenient", 0.5))
        t = {k: sum(r[k] for r in own) for k in own[0]}
        w = {k: sum(r[k] for r in whole) for k in whole[0]}
        pct = lambda a, b: f"{100 * a / b:.1f}%"  # noqa: E731
        L.append(f"| {NAMES[ds]} | {pct(full_h, n_h)} | {pct(full_p, n_p)} | {pct(w['relation_ok'], w['relations'])} | "
                 f"**{pct(t['relation_ok'], t['relations'])}** | {pct(t['relation_ok_any_time'], t['relations'])} |")
    out = E.RESULTS / "TIME.md"
    out.write_text("\n".join(L) + "\n")
    print("\n".join(L[-4:]))
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
