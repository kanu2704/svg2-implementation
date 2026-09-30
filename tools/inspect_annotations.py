"""Phase 1.2: look inside the SVG2 annotation parquets (no masks, no videos needed).

For every folder under data/SVG2/data/<version>/<source>/ it prints the columns, the
number of videos, per-video object / attribute / relation statistics, relation types,
object levels (SVG2_test only), statistics of relation time spans, and one example row.

    python tools/inspect_annotations.py                       # every folder
    python tools/inspect_annotations.py --only SVG2_test sav  # folders whose path contains all given words
"""
import argparse
import glob
import json
import os
import time
from collections import Counter

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq

ROOT = "data/SVG2/data"


def parse(value):
    """Columns hold JSON strings; tolerate already-decoded values and nulls."""
    if value is None:
        return []
    if isinstance(value, str):
        return json.loads(value) if value else []
    return value


def load_folder(folder):
    files = sorted(glob.glob(os.path.join(folder, "*.parquet")))
    return pa.concat_tables([pq.read_table(f) for f in files]), len(files)


def pct(values, qs=(50, 90, 99, 100)):
    if not values:
        return "n/a"
    arr = np.asarray(values, dtype=float)
    return "  ".join(f"p{q}={np.percentile(arr, q):.1f}" for q in qs)


def summarize(folder):
    t0 = time.time()
    table, n_files = load_folder(folder)
    cols = table.column_names
    n = table.num_rows
    name = os.path.relpath(folder, ROOT)
    print("=" * 100)
    print(f"{name}   ({n_files} parquet files, {n} videos)")
    print(f"columns: {cols}")

    if "source" in cols:
        print("source:", dict(Counter(table.column("source").to_pylist())))

    objs_col = table.column("objects").to_pylist()
    rels_col = table.column("relationships").to_pylist()

    objs_per_video, attrs_per_obj, rels_per_video = [], [], []
    rel_len, rel_types, levels, obj_keys = Counter(), Counter(), Counter(), Counter()
    span_ends, span_lengths, n_spans_per_rel = [], [], []
    frac_endpoints = total_endpoints = 0
    camera_rels = uncertain_objs = 0
    labels = Counter()

    for o_raw, r_raw in zip(objs_col, rels_col):
        objs, rels = parse(o_raw), parse(r_raw)
        objs_per_video.append(len(objs))
        rels_per_video.append(len(rels))
        for ob in objs:
            key = next((k for k in ob if k.startswith("object")), None)
            obj_keys[key.split("_")[0] if key else "NO_OBJECT_KEY"] += 1
            if key:
                label = str(ob[key])
                labels[label] += 1
                uncertain_objs += "uncertain" in label
            attrs_per_obj.append(len(ob.get("attributes") or []))
            if "level" in ob:
                levels[ob["level"]] += 1
        for rel in rels:
            rel_len[len(rel)] += 1
            if len(rel) > 4:
                rel_types[rel[4]] += 1
            if -1 in (rel[0], rel[2]):
                camera_rels += 1
            spans = rel[3] if len(rel) > 3 else []
            n_spans_per_rel.append(len(spans))
            for s, e in spans:
                span_ends.append(e)
                span_lengths.append(e - s)
                for v in (s, e):
                    total_endpoints += 1
                    frac_endpoints += float(v) != int(v)

    n_obj, n_rel = sum(objs_per_video), sum(rels_per_video)
    print(f"objects: {n_obj}   per video: {pct(objs_per_video)}")
    print(f"attributes: {sum(attrs_per_obj)}   per object: {pct(attrs_per_obj)}   "
          f"objects with 0 attributes: {sum(a == 0 for a in attrs_per_obj)}")
    print(f"relations: {n_rel}   per video: {pct(rels_per_video)}   "
          f"camera (-1) relations: {camera_rels}")
    print(f"relation tuple lengths: {dict(rel_len)}")
    if rel_types:
        print(f"relation types: {dict(rel_types.most_common())}")
    if levels:
        print(f"object levels: {dict(levels)}")
    print(f"object key styles: {dict(obj_keys)}   labels containing 'uncertain': {uncertain_objs}")
    print(f"distinct object labels: {len(labels)}   top 15: {labels.most_common(15)}")
    print(f"spans per relation: {pct(n_spans_per_rel)}")
    print(f"span end (s): {pct(span_ends)}")
    print(f"span length end-start (s): {pct(span_lengths)}   "
          f"zero-length spans: {sum(l == 0 for l in span_lengths)}   negative: {sum(l < 0 for l in span_lengths)}")
    print(f"fractional endpoints: {frac_endpoints} / {total_endpoints}")

    # One example row, one line per object / relation, truncated so it stays readable.
    print("example row:")
    for c in cols:
        value = table.column(c)[0].as_py()
        if c in ("objects", "relationships"):
            items = parse(value)
            print(f"  {c}: {len(items)} items")
            for item in items[:5]:
                print("    ", json.dumps(item, ensure_ascii=False, default=str)[:250])
            if len(items) > 5:
                print("     ...")
        else:
            print(f"  {c}: {str(value)[:250]}")
    print(f"({time.time() - t0:.1f}s)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", default=[],
                    help="only folders whose path contains all of these words")
    args = ap.parse_args()

    folders = sorted({os.path.dirname(p) for p in glob.glob(os.path.join(ROOT, "**", "*.parquet"), recursive=True)})
    folders = [f for f in folders if all(w in f for w in args.only)]
    if not folders:
        raise SystemExit(f"No parquet files under {ROOT}. Download data/* first.")
    for f in folders:
        summarize(f)


if __name__ == "__main__":
    main()
