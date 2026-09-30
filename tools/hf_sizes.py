"""Phase 1.1: size of every folder in the SVG2 dataset repo, so we only download what we can afford."""
from collections import defaultdict

from huggingface_hub import HfApi

REPO = "UWGZQ/Synthetic_Visual_Genome2"

info = HfApi().dataset_info(REPO, files_metadata=True)
sizes, counts = defaultdict(int), defaultdict(int)
for f in info.siblings:
    folder = "/".join(f.rfilename.split("/")[:3])
    sizes[folder] += f.size or 0
    counts[folder] += 1

total = 0
for folder in sorted(sizes):
    total += sizes[folder]
    print(f"{sizes[folder] / 2**30:9.2f} GB  {counts[folder]:5d} files  {folder}")
print(f"{total / 2**30:9.2f} GB  TOTAL")
