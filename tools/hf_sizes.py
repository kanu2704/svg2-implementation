"""Size of every folder in a Hugging Face repo, so we only download what we can afford.

    python tools/hf_sizes.py                                   # the SVG2 dataset (Phase 1.1)
    python tools/hf_sizes.py facebook/PE-Video --depth 1       # any other dataset repo
    python tools/hf_sizes.py UWGZQ/TRASER --type model
"""
import argparse
from collections import defaultdict

from huggingface_hub import HfApi


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo", nargs="?", default="UWGZQ/Synthetic_Visual_Genome2")
    ap.add_argument("--type", default="dataset", choices=["dataset", "model"])
    ap.add_argument("--depth", type=int, default=3, help="group files by this many path components")
    ap.add_argument("--examples", type=int, default=2, help="example file names to show per folder")
    args = ap.parse_args()

    api = HfApi()
    info = (api.dataset_info if args.type == "dataset" else api.model_info)(args.repo, files_metadata=True)
    print(f"{args.repo}: gated={getattr(info, 'gated', None)}  private={getattr(info, 'private', None)}")

    sizes, counts, examples = defaultdict(int), defaultdict(int), defaultdict(list)
    for f in info.siblings:
        folder = "/".join(f.rfilename.split("/")[:args.depth])
        sizes[folder] += f.size or 0
        counts[folder] += 1
        if len(examples[folder]) < args.examples:
            examples[folder].append(f.rfilename)

    total = 0
    for folder in sorted(sizes):
        total += sizes[folder]
        print(f"{sizes[folder] / 2**30:9.2f} GB  {counts[folder]:6d} files  {folder}   e.g. {examples[folder]}")
    print(f"{total / 2**30:9.2f} GB  TOTAL")


if __name__ == "__main__":
    main()
