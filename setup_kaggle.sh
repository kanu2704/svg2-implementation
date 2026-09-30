#!/usr/bin/env bash
# Run at the start of EVERY Kaggle session:  source setup_kaggle.sh
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SVG2_COMMIT=77caa44f862727eeba6d8bacbb53f236ac75cd05

# Big downloads (model weights, datasets) go to the large temporary disk.
export HF_HOME=/tmp/hf_cache
mkdir -p "$HF_HOME"

# 1) Official SVG2 code, pinned to the exact commit the plan was written against.
if [ ! -d "$REPO_DIR/third_party/SVG2/.git" ]; then
  git clone -q https://github.com/uwGZQ/SVG2 "$REPO_DIR/third_party/SVG2" || echo "!! clone of SVG2 failed"
fi
git -C "$REPO_DIR/third_party/SVG2" checkout -q "$SVG2_COMMIT" || echo "!! checkout of SVG2 commit failed"
echo "SVG2 at $(git -C "$REPO_DIR/third_party/SVG2" rev-parse --short HEAD 2>/dev/null)"

# 2) Python packages. Keep Kaggle's torch; pin transformers to the repo's version.
pip install -q "transformers==4.54.1" "huggingface_hub>=0.34,<1.0" \
               pycocotools pyarrow einops "opencv-python-headless>=4.9" || echo "!! pip install failed"
pip install -q decord 2>/dev/null || pip install -q eva-decord || echo "!! no video reader installed"

echo "Setup done (check for !! lines above)."