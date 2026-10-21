"""Judge the relation words of the pair experiment with the benchmark's judge (Kimi K3 on NVIDIA NIM), so its tables
can count a word as right under the lenient criterion, as the main benchmark does.

Every (human word, TRASER's word) combination in the saved top-5 lists of experiments 2 and 2b
(results/traser_bench/interp/raw/e2*/), and the object names of 2b, that is not in results/traser_bench/judge_cache.json yet is asked once and
added to that cache. Runs anywhere with internet (no GPU); the key comes from $NVIDIA_API_KEY or ~/.svg2_keys.
If Kimi K3 does not answer, the next model of bench_eval.JUDGES that does is used: its verdicts go to their own file
(judge_cache_<model>.json), count only for words Kimi K3 never judged, and it is first checked on 200 words Kimi K3
judged.

    python3 tools/interp/judge_pairs.py            # ask the judge
    python3 tools/interp/judge_pairs.py --count    # only count what is missing
    python3 tools/interp/judge_pairs.py --judge z-ai/glm-5.3    # a given model instead of Kimi K3 (or the next that answers)
"""
import argparse
import glob
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import bench_eval as E  # noqa: E402
from interp import common as C  # noqa: E402
from interp import pairs_lenient as PL  # noqa: E402


def tops(x):
    """Every top-5 word list inside one tested pair (any experiment, input and context)."""
    if isinstance(x, dict):
        if isinstance(x.get("top"), list):
            yield [t[0] for t in x["top"] if t]
        for v in x.values():
            yield from tops(v)


def needed(raw, results):
    """(kind, human, TRASER) combinations of the saved results: relation words (experiments 2 and 2b, top 5) and
    objects (2b: the human object's name vs the names of the other objects it picked, top 5)."""
    pairs = set()
    for f in glob.glob(str(Path(raw) / "e2*" / "*" / "*.json")):
        d = json.load(open(f))
        for group in ("missed", "written"):
            for p in d.get(group, []):
                for words in tops({k: v for k, v in p.items() if k != "words"}):
                    pairs.update(("relation", h, w) for h in p.get("words", []) for w in words)
    for ds in C.DATASETS:
        for d, names in PL.load(raw, results, ds):
            for p in d.get("missed", []) + d.get("written", []):
                t = names.get(p["o_k"])
                for ctx in ("fresh", "answer"):
                    for r in p.get(ctx, {}).values():
                        pairs.update(("object", t, names[o]) for o in PL.object_picks(r, 5)
                                     if t and o != p["o_k"] and names.get(o))
    return pairs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=str(C.OUT / "raw"))
    ap.add_argument("--results", default=str(C.RESULTS))
    ap.add_argument("--count", action="store_true", help="only count the word pairs not judged yet")
    ap.add_argument("--judge", default="auto", help="model to ask (auto: Kimi K3, else the next of bench_eval.JUDGES that answers)")
    args = ap.parse_args()
    cache = Path(args.results) / "judge_cache.json"
    pairs = needed(args.raw, args.results)
    missing = lambda j: sum(j.category(*p) is None for p in pairs)  # noqa: E731
    judge = E.Judge(cache=cache, others=True)
    print(f"{len(pairs)} (human word, TRASER word) combinations in the saved results; {missing(judge)} not judged yet")
    if args.count or not missing(judge):
        return 0
    judge = E.pick_judge(cache, args.judge)
    judge.check()
    judge.ask_all(sorted(pairs))
    judge.save()
    print(f"saved {judge.cache_path}; still not judged: {missing(judge)}")
    if judge.note():
        print(judge.note())
    return 0

if __name__ == "__main__":
    sys.exit(main())
