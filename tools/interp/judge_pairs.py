"""Judge the relation words of the pair experiment with the benchmark's judge (Kimi K3 on NVIDIA NIM), so its tables
can count a word as right under the lenient criterion, as the main benchmark does.

Every (human word, TRASER's word) combination in the saved top-5 lists of experiments 2 and 2b
(results/traser_bench/interp/raw/e2*/) that is not in results/traser_bench/judge_cache.json yet is asked once and
added to that cache. Runs anywhere with internet (no GPU); the key comes from $NVIDIA_API_KEY or ~/.svg2_keys.

    python3 tools/interp/judge_pairs.py            # ask the judge
    python3 tools/interp/judge_pairs.py --count    # only count what is missing
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


def tops(x):
    """Every top-5 word list inside one tested pair (any experiment, input and context)."""
    if isinstance(x, dict):
        if isinstance(x.get("top"), list):
            yield [t[0] for t in x["top"] if t]
        for v in x.values():
            yield from tops(v)


def needed(raw):
    pairs = set()
    for f in glob.glob(str(Path(raw) / "e2*" / "*" / "*.json")):
        d = json.load(open(f))
        for group in ("missed", "written"):
            for p in d.get(group, []):
                for words in tops({k: v for k, v in p.items() if k != "words"}):
                    pairs.update(("relation", h, w) for h in p.get("words", []) for w in words)
    return pairs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=str(C.OUT / "raw"))
    ap.add_argument("--count", action="store_true", help="only count the word pairs not judged yet")
    args = ap.parse_args()
    judge = E.Judge()
    pairs = needed(args.raw)
    todo = sorted({judge.key(*p) for p in pairs if E.norm(p[1]) != E.norm(p[2])} - set(judge.cache))
    print(f"{len(pairs)} (human word, TRASER word) combinations in the saved results; {len(todo)} not judged yet")
    if args.count or not todo:
        return 0
    judge.ask_all(sorted(pairs))
    judge.save()
    left = sorted({judge.key(*p) for p in pairs if E.norm(p[1]) != E.norm(p[2])} - set(judge.cache))
    print(f"saved {judge.cache_path}; still not judged: {len(left)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
