"""Compare two TRASER scene-graph outputs (exact match; no LLM judge).

    python tools/compare_graphs.py A.json B.json [C.json ...]     # every file against the first

Prints, per file: object labels identical?, objects with identical attributes, and the
relation overlap (identical tuples, plus how many differ only in their time spans).
"""
import json
import sys


def load(path):
    with open(path) as f:
        return json.load(f)


def label(o):
    return next(v for k, v in o.items() if k.startswith("object"))


def compare(a, b):
    la, lb = [label(o) for o in a["objects"]], [label(o) for o in b["objects"]]
    same_attr = sum(x.get("attributes") == y.get("attributes") for x, y in zip(a["objects"], b["objects"]))
    ra = {json.dumps(r) for r in a.get("relationships", [])}
    rb = {json.dumps(r) for r in b.get("relationships", [])}
    triple = lambda s: {tuple(json.loads(r)[:3]) for r in s}
    return {
        "objects": f"{len(lb)} vs {len(la)}; labels identical: {la == lb}",
        "identical attribute lists": f"{same_attr}/{min(len(la), len(lb))}",
        "relations": f"{len(rb)} vs {len(ra)}; identical: {len(ra & rb)}; "
                     f"same (subject, predicate, object) but other spans: {len((triple(ra) & triple(rb))) - len(ra & rb)}",
        "only in this file": sorted(rb - ra),
        "only in the first file": sorted(ra - rb),
    }


def main():
    paths = sys.argv[1:]
    if len(paths) < 2:
        raise SystemExit(__doc__)
    first = load(paths[0])
    for p in paths[1:]:
        print(f"=== {p}  vs  {paths[0]}")
        for k, v in compare(first, load(p)).items():
            if isinstance(v, list):
                print(f"  {k}: {len(v)}")
                for r in v:
                    print(f"      {r}")
            else:
                print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
