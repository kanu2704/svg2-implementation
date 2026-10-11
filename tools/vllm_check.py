"""Does vLLM write the same answers as the Hugging Face path? Run before trusting vLLM for a whole dataset.

The same videos are answered twice from the same checkpoint and the same input: once by tools/bench_run.py
(Hugging Face generate, one video at a time, written to --hf_results) and once by tools/vllm_generate.py
(written to the normal results folder). Compared per video: identical text?, where the first difference is,
answer lengths, valid JSON, and the scores (lenient, tIoU > 0.5) of both answers. Small differences are
possible: float16 rounding differs between the two (other GPU kernels, several videos at once), and greedy
decoding can then pick another token on a long answer.
Writes <hf_results>/CHECK.md and check.json (README.md shows the summary).

    python3 tools/vllm_check.py --dataset vidor --hf_results results/traser_bench/hf_check [--ask_judge]
"""
import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))
import bench_eval as E  # noqa: E402


def first_difference(a, b):
    n = min(len(a), len(b))
    for i in range(n):
        if a[i] != b[i]:
            return i
    return None if len(a) == len(b) else n


def compare(dataset, hf_root, vllm_root=None, ask_judge=False, log=print):
    hf_root, vllm_root = Path(hf_root), Path(vllm_root or E.RESULTS)
    videos = sorted(p.name[:-5] for p in (hf_root / dataset / "preds").glob("*.json") if not p.name.endswith(".stats.json"))
    pairs, loaded = [], []
    for v in videos:
        if not (vllm_root / dataset / "preds" / f"{v}.json").exists():
            log(f"{v}: no vLLM answer yet, skipped")
            continue
        h, w = E.load_video(dataset, v, hf_root), E.load_video(dataset, v, vllm_root)
        loaded.append((v, h, w))
        pairs += E.video_pairs(*h)[0] + E.video_pairs(*w)[0]
    judge = E.Judge()
    if ask_judge:
        judge.ask_all(pairs, log=log)
    rows = []
    for v, (gt, ph, sh), (_, pw, sw) in loaded:
        th = (hf_root / dataset / "preds" / f"{v}.json").read_text()
        tw = (vllm_root / dataset / "preds" / f"{v}.json").read_text()
        d = first_difference(th, tw)
        a, b = E.score_video(gt, ph, sh, judge), E.score_video(gt, pw, sw, judge)
        rows.append({"video": v, "identical": d is None,
                     "same_until": "end" if d is None else f"{d}/{max(len(th), len(tw))} characters ({100 * d / max(len(th), len(tw), 1):.0f}%)",
                     "tokens_hf": sh.get("new_tokens"), "tokens_vllm": sw.get("new_tokens"),
                     "json_hf": ph["json_ok"], "json_vllm": pw["json_ok"],
                     "objects_right": f"{a['object_ok']} / {b['object_ok']} of {a['objects']}",
                     "relations_right": f"{a['relation_ok']} / {b['relation_ok']} of {a['relations']}",
                     "triplets_right": f"{a['triplet_ok']} / {b['triplet_ok']} of {a['relations']}",
                     "unjudged": a["unjudged"] + b["unjudged"],
                     "_hf": a, "_vllm": b, "_hf_s": sh.get("generate_s"), "_vllm_s": sw.get("generate_batch_s")})
    tot = lambda key, k: sum(r[key][k] for r in rows)  # noqa: E731
    summary = {"videos": len(rows), "identical": sum(r["identical"] for r in rows),
               "hf": {k: tot("_hf", k) for k in ("object_ok", "relation_ok", "triplet_ok", "objects", "relations")},
               "vllm": {k: tot("_vllm", k) for k in ("object_ok", "relation_ok", "triplet_ok", "objects", "relations")},
               "unjudged": sum(r["unjudged"] for r in rows)}
    return rows, summary


def write(rows, summary, hf_root, dataset):
    hf_root = Path(hf_root)
    clean = [{k: v for k, v in r.items() if not k.startswith("_")} for r in rows]
    json.dump({"dataset": dataset, "summary": summary, "videos": clean}, open(hf_root / "check.json", "w"), indent=1)
    h, w = summary["hf"], summary["vllm"]
    L = [f"# vLLM vs Hugging Face: the same {summary['videos']} {dataset} videos", "",
         "Same checkpoint, same input sequence; answers written once by Hugging Face `generate` (one video at a time) "
         "and once by vLLM (many at once). Made by `tools/vllm_check.py`.", "",
         f"**{summary['identical']} of {summary['videos']} answers are identical.** Right (Hugging Face / vLLM): "
         f"objects {h['object_ok']} / {w['object_ok']} of {h['objects']}, relations {h['relation_ok']} / {w['relation_ok']} "
         f"of {h['relations']}, triplets {h['triplet_ok']} / {w['triplet_ok']} of {h['relations']}"
         + (f" ({summary['unjudged']} label pairs not judged yet)" if summary["unjudged"] else "") + ".", "",
         E._md_table(clean)]
    (hf_root / "CHECK.md").write_text("\n".join(L))
    return hf_root / "CHECK.md"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", default="vidor")
    ap.add_argument("--hf_results", default=str(E.RESULTS / "hf_check"))
    ap.add_argument("--ask_judge", action="store_true", help="judge label pairs not judged yet (needs the NIM key)")
    args = ap.parse_args()
    rows, summary = compare(args.dataset, args.hf_results, ask_judge=args.ask_judge)
    if not rows:
        print("nothing to compare yet")
        return 1
    path = write(rows, summary, args.hf_results, args.dataset)
    print(path.read_text())
    return 0


if __name__ == "__main__":
    sys.exit(main())
