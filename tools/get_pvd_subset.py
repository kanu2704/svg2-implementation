"""Phase 1.5: fetch a small, self-consistent PVD subset: videos + their SVG2 masks.

SVG2 does not ship videos. PVD videos come from facebook/PE-Video, packed as ~0.75 GB tar
shards; SVG2's PVD masks are packed in 550 parquet shards (~360 MB each). A random video's
masks can sit in any mask shard, so downloading whole shards would cost 100+ GB.

This script instead:
  1. downloads ONE PE-Video tar and keeps the videos that are in SVG2 cleaned/pvd;
  2. finds their rows in the mask shards using only the parquet footers (per-row-group
     min/max of video_id), confirming with the small video_id column where needed;
  3. fetches only those row groups and writes a mini mask shard with the original schema.

The result is laid out like the real dataset, so the official converter runs unchanged:

    data/SVG2_subset/data/cleaned/pvd   -> symlink to data/SVG2/data/cleaned/pvd
    data/SVG2_subset/masks/cleaned/pvd/subset.parquet
    data/videos/pvd/<video_id>.mp4

    python tools/get_pvd_subset.py --max_videos 50   # tries extended/000000-000002.tar
    python third_party/SVG2/traser/data/prepare_svg2.py --source pvd --svg2_root data/SVG2_subset \
        --video_root data/videos/pvd --out_dir data/traser --max_object 40
"""
import argparse
import glob
import json
import os
import tarfile
import time

import pyarrow as pa
import pyarrow.parquet as pq

SVG2_REPO = "UWGZQ/Synthetic_Visual_Genome2"
PEVIDEO_REPO = "facebook/PE-Video"
DATA_DIR = "data/SVG2/data/cleaned/pvd"
SUBSET_ROOT = "data/SVG2_subset"
VIDEO_OUT = "data/videos/pvd"
INDEX_CACHE = "data/SVG2/mask_meta/pvd_rowgroup_index.json"


def svg2_pvd_ids():
    ids = set()
    for f in sorted(glob.glob(os.path.join(DATA_DIR, "*.parquet"))):
        ids.update(pq.read_table(f, columns=["video_id"]).column("video_id").to_pylist())
    if not ids:
        raise SystemExit(f"No annotations under {DATA_DIR}; run the Phase 1.2 download first.")
    return ids


def candidate_keys(name, payload):
    """Possible video ids for a tar member: its file stem, plus scalar values in its JSON sidecar."""
    keys = {os.path.basename(name).split(".")[0]}
    if payload is not None:
        for v in payload.values():
            if isinstance(v, (str, int)) and len(str(v)) < 40:
                keys.add(str(v))
                keys.add(os.path.splitext(os.path.basename(str(v)))[0])
    return keys


def extract_videos(tar_path, wanted, max_videos):
    """Extract up to max_videos mp4s whose id is in `wanted`. Returns {video_id: path}."""
    os.makedirs(VIDEO_OUT, exist_ok=True)
    with tarfile.open(tar_path) as tar:
        members = tar.getmembers()
        print(f"tar has {len(members)} members, e.g. {[m.name for m in members[:6]]}")
        by_stem = {}
        for m in members:
            stem = m.name.rsplit(".", 1)[0]
            by_stem.setdefault(stem, {})[m.name.rsplit(".", 1)[-1].lower()] = m
        shown = False
        found = {}
        for stem, parts in by_stem.items():
            if "mp4" not in parts:
                continue
            payload = None
            if "json" in parts:
                payload = json.load(tar.extractfile(parts["json"]))
                if not shown:
                    print(f"example JSON sidecar for {stem}: {json.dumps(payload)[:400]}")
                    shown = True
            hit = candidate_keys(parts["mp4"].name, payload) & wanted
            if not hit:
                continue
            vid = sorted(hit)[0]
            out = os.path.join(VIDEO_OUT, f"{vid}.mp4")
            if not os.path.exists(out):
                with open(out, "wb") as f:
                    f.write(tar.extractfile(parts["mp4"]).read())
            found[vid] = out
            if len(found) >= max_videos:
                break
        n_mp4 = sum("mp4" in p for p in by_stem.values())
    print(f"{n_mp4} videos in the tar; {len(found)} kept (in SVG2 cleaned/pvd)")
    return found


def rowgroup_index(fs, shards):
    """Per shard, per row group: (min video_id, max video_id, rows), from parquet footers only."""
    if os.path.exists(INDEX_CACHE):
        with open(INDEX_CACHE) as f:
            cached = json.load(f)
        if len(cached) == len(shards):
            return cached
    index = {}
    t0 = time.time()
    for i, path in enumerate(shards):
        with fs.open(path, "rb", block_size=1 << 16) as f:
            md = pq.ParquetFile(f).metadata
        col = md.schema.names.index("video_id")
        groups = []
        for g in range(md.num_row_groups):
            st = md.row_group(g).column(col).statistics
            has = st is not None and st.has_min_max
            groups.append([str(st.min) if has else None, str(st.max) if has else None, md.row_group(g).num_rows])
        index[path] = groups
        print(f"  footers: {i + 1}/{len(shards)} ({time.time() - t0:.0f}s)", end="\r", flush=True)
    print()
    os.makedirs(os.path.dirname(INDEX_CACHE), exist_ok=True)
    with open(INDEX_CACHE, "w") as f:
        json.dump(index, f)
    return index


def id_index(fs, shards):
    """Fallback: read only the video_id column of every shard once; cache id -> (shard, row group)."""
    cache = INDEX_CACHE.replace("rowgroup_index", "id_index")
    if os.path.exists(cache):
        with open(cache) as f:
            return {k: tuple(v) for k, v in json.load(f).items()}
    where = {}
    t0 = time.time()
    for i, path in enumerate(shards):
        with fs.open(path, "rb", block_size=1 << 20) as f:
            pf = pq.ParquetFile(f, pre_buffer=False)
            for g in range(pf.metadata.num_row_groups):
                for vid in pf.read_row_group(g, columns=["video_id"]).column("video_id").to_pylist():
                    where[vid] = (path, g)
        print(f"  video_id scan: {i + 1}/{len(shards)} shards ({time.time() - t0:.0f}s)", end="\r", flush=True)
    print()
    with open(cache, "w") as f:
        json.dump(where, f)
    return where


def fetch_mask_rows(ids, max_candidates):
    from huggingface_hub import HfFileSystem

    fs = HfFileSystem()
    shards = sorted(fs.glob(f"datasets/{SVG2_REPO}/masks/cleaned/pvd/*.parquet"))
    index = rowgroup_index(fs, shards)

    # Candidate row groups per id: those whose [min, max] range contains the id.
    candidates = {}
    unknown = 0
    for path, groups in index.items():
        for g, (lo, hi, _) in enumerate(groups):
            if lo is None:
                unknown += 1
                continue
            for vid in ids:
                if lo <= vid <= hi:
                    candidates.setdefault((path, g), set()).add(vid)
    n_groups = sum(len(g) for g in index.values())
    print(f"{len(shards)} mask shards, {n_groups} row groups ({unknown} without min/max stats); "
          f"candidate row groups from footer stats: {len(candidates)}")
    if unknown or len(candidates) > max_candidates:
        print("Footer stats cannot narrow the search (shards not sorted by video_id); "
              "scanning the video_id column of every shard once (cached for later runs).")
        where = id_index(fs, shards)
        candidates = {}
        for vid in ids:
            if vid in where:
                candidates.setdefault(where[vid], set()).add(vid)

    tables, found = [], set()
    for n, ((path, g), vids) in enumerate(sorted(candidates.items())):
        vids = vids - found
        if not vids:
            continue
        with fs.open(path, "rb", block_size=1 << 20) as f:
            pf = pq.ParquetFile(f, pre_buffer=False)
            id_col = pf.read_row_group(g, columns=["video_id"]).column("video_id").to_pylist()
            hits = [i for i, v in enumerate(id_col) if v in vids]
            if hits:
                t = pf.read_row_group(g).take(pa.array(hits))
                tables.append(t)
                found.update(t.column("video_id").to_pylist())
        print(f"  checked {n + 1}/{len(candidates)} row groups, found {len(found)}/{len(ids)}", end="\r", flush=True)
    print()
    return (pa.concat_tables(tables) if tables else None), found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tar", nargs="+", default=["extended/000000.tar", "extended/000001.tar", "extended/000002.tar"],
                    help="PE-Video tar shards to try, in order, until --max_videos are found")
    ap.add_argument("--tar_path", default=None, help="use an already-downloaded tar instead")
    ap.add_argument("--max_videos", type=int, default=50)
    ap.add_argument("--max_candidates", type=int, default=2000)
    args = ap.parse_args()

    wanted = svg2_pvd_ids()
    print(f"SVG2 cleaned/pvd has {len(wanted)} video ids")

    videos = {}
    for tar in ([args.tar_path] if args.tar_path else args.tar):
        tar_path = tar
        if args.tar_path is None:
            from huggingface_hub import hf_hub_download
            try:
                tar_path = hf_hub_download(PEVIDEO_REPO, tar, repo_type="dataset")
            except Exception as e:  # gated repo, missing login, network
                raise SystemExit(f"Could not download {PEVIDEO_REPO}/{tar}: {e}\n"
                                 f"If it says 401/403 or 'gated': open https://huggingface.co/datasets/{PEVIDEO_REPO}, "
                                 f"accept the terms, then run `hf auth login` with a read token.")
        print(f"--- {tar}")
        videos.update(extract_videos(tar_path, wanted - set(videos), args.max_videos - len(videos)))
        if len(videos) >= args.max_videos:
            break
    if not videos:
        raise SystemExit("None of these tars has a video in SVG2 cleaned/pvd; try other --tar shards.")

    table, found = fetch_mask_rows(set(videos), args.max_candidates)
    missing = set(videos) - found
    for vid in missing:  # a video without masks cannot be used
        os.remove(videos[vid])
    if table is None:
        raise SystemExit("No mask rows found for these videos.")

    mask_dir = os.path.join(SUBSET_ROOT, "masks/cleaned/pvd")
    os.makedirs(mask_dir, exist_ok=True)
    pq.write_table(table, os.path.join(mask_dir, "subset.parquet"))
    data_link = os.path.join(SUBSET_ROOT, "data/cleaned/pvd")
    os.makedirs(os.path.dirname(data_link), exist_ok=True)
    if not os.path.exists(data_link):
        os.symlink(os.path.abspath(DATA_DIR), data_link)

    print(f"\nDone: {len(found)} videos with masks.")
    print(f"  videos: {VIDEO_OUT}/   masks: {mask_dir}/subset.parquet   annotations: {data_link} (symlink)")
    if missing:
        print(f"  dropped {len(missing)} videos whose masks were not found")


if __name__ == "__main__":
    main()
