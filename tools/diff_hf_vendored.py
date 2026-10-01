"""Phase 2: is the code shipped with the checkpoint the same as the code on GitHub?

The UWGZQ/TRASER model repo vendors its own copies of the model and the token
selection / arrangement code. If they differ from the GitHub release, the released
checkpoint may have been produced (or is meant to be run) with code that is not the
documented one. Writes notes/phase2_hf_vs_github.md with a unified diff per file, plus
the checkpoint's config.json and generation_config.json.

    python tools/diff_hf_vendored.py
"""
import difflib
import json
import os

from huggingface_hub import hf_hub_download

REPO = "UWGZQ/TRASER"
GH = "third_party/SVG2/traser"
PAIRS = [
    ("modeling_traser.py", f"{GH}/traser_train/train/modeling_traser.py"),
    ("resampler_utils/token_selection.py", f"{GH}/traser_train/train/token_selection.py"),
    ("resampler_utils/token_arrangement.py", f"{GH}/traser_train/train/token_arrangement.py"),
    ("inference.py", f"{GH}/inference.py"),
]


def main():
    out = ["# Phase 2: Hugging Face vendored code vs GitHub release", "",
           f"Model repo `{REPO}` vs `{GH}` (GitHub commit pinned in setup_kaggle.sh).", "",
           "| HF file | GitHub file | identical? | lines only in HF | lines only in GitHub |", "|---|---|---|---|---|"]
    details = []
    for hf_name, gh_path in PAIRS:
        hf_lines = open(hf_hub_download(REPO, hf_name)).read().splitlines()
        gh_lines = open(gh_path).read().splitlines()
        diff = list(difflib.unified_diff(gh_lines, hf_lines, fromfile=f"github:{gh_path}",
                                         tofile=f"hf:{hf_name}", lineterm="", n=2))
        plus = sum(1 for l in diff if l.startswith("+") and not l.startswith("+++"))
        minus = sum(1 for l in diff if l.startswith("-") and not l.startswith("---"))
        out.append(f"| `{hf_name}` | `{gh_path}` | {'yes' if not diff else 'no'} | {plus} | {minus} |")
        if diff:
            shown = diff[:400]
            details += ["", f"## `{hf_name}` vs `{gh_path}`", "", "```diff", *shown,
                        *(["... (truncated)"] if len(diff) > 400 else []), "```"]
    for name in ("config.json", "generation_config.json"):
        cfg = json.load(open(hf_hub_download(REPO, name)))
        if name == "config.json":
            # Keep the parts that matter here; the vision/text sub-configs are long.
            keep = {k: v for k, v in cfg.items() if not isinstance(v, dict)}
            keep["vision_config (keys)"] = sorted(cfg.get("vision_config", {}))
        else:
            keep = cfg
        details += ["", f"## `{name}`", "", "```json", json.dumps(keep, indent=1), "```"]

    os.makedirs("notes", exist_ok=True)
    with open("notes/phase2_hf_vs_github.md", "w") as f:
        f.write("\n".join(out + details) + "\n")
    print("\n".join(out))
    print("\nReport written to notes/phase2_hf_vs_github.md")


if __name__ == "__main__":
    main()
