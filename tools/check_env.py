"""Phase 0 check: versions, GPUs, dtype support, Hugging Face access."""
from collections import Counter

import huggingface_hub
import torch
import transformers
from huggingface_hub import HfApi

print("torch", torch.__version__, "| transformers", transformers.__version__,
      "| hub", huggingface_hub.__version__)

for i in range(torch.cuda.device_count()):
    p = torch.cuda.get_device_properties(i)
    print(f"GPU{i}: {p.name}, {p.total_memory / 2**30:.1f} GB, "
          f"compute capability {p.major}.{p.minor}")

# T4 = compute capability 7.5: fp16 is native, bf16 is not.
a = torch.randn(1024, 1024, device="cuda", dtype=torch.float16)
print("fp16 matmul ok:", torch.isfinite(a @ a).all().item())
print("bf16 reported supported:", torch.cuda.is_bf16_supported())

try:
    import decord
    print("video reader: decord", decord.__version__)
except ImportError as e:
    print("decord missing:", e)

api = HfApi()

print("\n--- UWGZQ/TRASER files ---")
for f in api.list_repo_files("UWGZQ/TRASER"):
    print(" ", f)

print("\n--- UWGZQ/Synthetic_Visual_Genome2 (folders + file counts) ---")
files = api.list_repo_files("UWGZQ/Synthetic_Visual_Genome2", repo_type="dataset")
counts = Counter("/".join(f.split("/")[:3]) for f in files)
for folder, n in sorted(counts.items()):
    print(f"  {n:5d}  {folder}")