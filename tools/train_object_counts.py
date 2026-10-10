"""How many objects per video did TRASER train on? (the 40-object question)

The released training code has no object cap of its own: the data loader (traser_train/data/data_qwen.py)
gives the model every object in a sample's ``obj_list``. The only cap is in data preparation:
``traser/data/prepare_svg2.py --max_object 40``, which docs/DATA.md applies to the PE-Video (pvd) split
only ("oversized samples keep their first 40 objects"). So whether the checkpoint ever saw more than 40
objects depends on how many annotated objects the other training splits have. This script counts them
from the released annotations (only the small ``video_id`` and ``objects`` columns are read, straight
from the Hugging Face Hub; nothing large is downloaded) and lists the files of the model repo.

    python3 tools/train_object_counts.py               # writes notes/train_object_counts.md
    python3 tools/train_object_counts.py --local SVG2  # from a local snapshot instead of the Hub
"""
import argparse
import glob
import json
import os
import time

import numpy as np
import pyarrow.parquet as pq

REPO = "datasets/UWGZQ/Synthetic_Visual_Genome2"
MODEL = "UWGZQ/TRASER"
CAP = 40
# (SVG2 subdirectory, training registry name or None for the test set, cap applied by docs/DATA.md)
SPLITS = [("cleaned/sav", "svg2_sav", None), ("cleaned/pvd", "svg2_pvd", CAP),
          ("academic_datasets/vipseg", "vipseg", None), ("academic_datasets/vidor", "vidor", None),
          ("academic_datasets/vidvrd", "vidvrd", None), ("academic_datasets/lvvis", "lvvis", None),
          ("academic_datasets/ovis", "ovis", None),
          ("SVG2_test/sav", None, None), ("SVG2_test/vipseg", None, None)]


def log(msg):
    print(f"{time.strftime('%H:%M:%S')} {msg}", flush=True)


def parse(value):
    if value is None:
        return []
    return json.loads(value) if isinstance(value, str) else value


def shards(split, local):
    if local:
        return [(p, None) for p in sorted(glob.glob(os.path.join(local, "data", split, "*.parquet")))]
    from huggingface_hub import HfFileSystem
    fs = HfFileSystem()
    return [(p, fs) for p in sorted(fs.glob(f"{REPO}/data/{split}/*.parquet"))]


def read(path, fs):
    cols = ["video_id", "objects"]
    if fs is None:
        return pq.read_table(path, columns=cols).to_pydict()
    with fs.open(path, "rb", block_size=1 << 20) as f:
        return pq.ParquetFile(f, pre_buffer=False).read(columns=cols).to_pydict()


def count(split, local):
    """video_id -> number of annotated objects (= the obj_list prepare_svg2.py writes)."""
    n = {}
    files = shards(split, local)
    for i, (p, fs) in enumerate(files):
        d = read(p, fs)
        for vid, objs in zip(d["video_id"], d["objects"]):
            n[vid] = len(parse(objs))
        log(f"{split}: {i + 1}/{len(files)} files, {len(n)} videos so far")
    return n


def model_files():
    try:
        from huggingface_hub import HfApi
        return HfApi().list_repo_files(MODEL)
    except Exception as e:  # noqa: BLE001
        return [f"(could not list: {e})"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--local", default=None, help="local snapshot of the SVG2 dataset (has data/...)")
    ap.add_argument("--splits", nargs="*", default=[s for s, _, _ in SPLITS])
    ap.add_argument("--out", default="notes/train_object_counts.md")
    args = ap.parse_args()

    rows = []
    for split, name, cap in SPLITS:
        if split not in args.splits:
            continue
        n = count(split, args.local)
        if not n:
            log(f"{split}: no annotation files found, skipped")
            continue
        a = np.array(list(n.values()))
        seen = np.minimum(a, cap) if cap else a          # what the model was given after the cap
        rows.append({"split": split, "used for": f"training (`{name}`)" if name else "test",
                     "cap in DATA.md": f"first {cap}" if cap else "none",
                     "videos": len(a), "median objects": int(np.median(a)), "max objects": int(a.max()),
                     f"videos with > {CAP}": int((a > CAP).sum()),
                     f"% videos > {CAP}": f"{100 * (a > CAP).mean():.1f}",
                     f"max objects given to TRASER": int(seen.max())})
        log(f"{split}: {len(a)} videos, max {a.max()} objects, {(a > CAP).sum()} with more than {CAP}")

    cols = list(rows[0]) if rows else []
    table = ["| " + " | ".join(cols) + " |", "|---" * len(cols) + "|"]
    table += ["| " + " | ".join(str(r[c]) for c in cols) + " |" for r in rows]
    train = [r for r in rows if r["used for"].startswith("training")]
    over = sum(r["videos with > 40"] for r in train if r["cap in DATA.md"] == "none")
    files = model_files()
    out = ["# Objects per video in TRASER's training data (the 40-object question)", "",
           "Made by `tools/train_object_counts.py` from the released SVG2 annotations. "
           "`objects` = annotated objects of a video, which is the `obj_list` that "
           "`traser/data/prepare_svg2.py` writes and the data loader gives to the model "
           "(objects without a mask on the sampled frames are dropped later, so the real number can be a little lower). "
           "The training code itself has no object cap; docs/DATA.md applies `--max_object 40` to pvd only.", "",
           *table, "",
           f"**Training videos with more than {CAP} objects outside the capped pvd split: {over}.** "
           + ("So the released checkpoint did see samples with more than 40 objects in training."
              if over else "So the released checkpoint never saw more than 40 objects in one training sample."), "",
           f"## Files in the model repo `{MODEL}`", "", *[f"- `{f}`" for f in files], ""]
    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "w") as f:
        f.write("\n".join(out))
    print("\n".join(out))
    log(f"written to {args.out}")


if __name__ == "__main__":
    main()
