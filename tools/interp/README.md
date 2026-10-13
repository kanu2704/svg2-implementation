# Interpretability of TRASER (`tools/interp/`)

Why does TRASER lose its points (pairs never written, short actions, crowded videos, small objects; see
`results/traser_bench/diagnosis/ERRORS.md`)? These tools open the released model and test it directly.
Everything works on TRASER's released checkpoint and its own saved answers.

| step | file | needs | what it does | output |
|---|---|---|---|---|
| stage 1 | `encode_stage.py` | GPU, TRASER checkpoint, prepared videos | the language model's exact input per video, where every object / OTR / window / time label sits in it, each object's vectors before the language model (vision encoder, OTR, TWR), mask geometry (sizes, motion, gaps, touching) | `<work>/<dataset>/<video>.{embeds.pt, layout.json, feats.npz}` |
| stage 2 | `lm_stage.py` | GPU, `tools/export_lm.py` export | **p0** harness check · **p1** hidden states per object at every layer · **p2a** forced continuation ("knows but doesn't say") · **p2b** interventions (blank all / OTR / TWR latents, one object, a relation's windows; reversed time labels) · **p2c** activation patching per layer · **p3** attention of time / object-number / word tokens | `results/traser_bench/interp/raw/<phase>/<dataset>/<video>.json`, `<work>/.../<video>.hidden.npz` |
| probes | `probe.py` | CPU | logistic-regression probes at every stage (vision → OTR/TWR → each LM layer): related pair, written pair, action vs position, touching, moving, in a human relation, relation active in a window; controls (shuffled labels, geometry only) | `results/traser_bench/interp/probes.json` |
| report | `report.py` | CPU | one page with every table and figure | `results/traser_bench/interp/REPORT.md`, `figs/*.png` |

Sample: a fixed random set of the answered videos (`common.DEFAULT_N`: SVG2test 40, PVSG 25, VidOR 60; the same on every
machine). Every step skips what is already done, so it can be stopped and run again.

## On Kaggle
Notebook `notebooks/traser_eval.ipynb`: run 0a-0d, prepare the videos (1a+1b PVSG, 2a-2d SVG2test, 3a VidOR), then
**block 6** (one cell). It uses every GPU and pushes the results while it runs.

## On your own GPU server (SSH)
Easiest: the same notebook. Open it from a clone on the server (VS Code Remote-SSH, kernel = a Python
environment with torch), set `BIG_DIR` in cell 0a to a folder with ~150 GB free and `GPUS` in block 6 to the GPUs you
may use, then run 0a-0d, the preparation cells, and block 6. Only block 6 uses the GPU.

## On another GPU machine, from a terminal
```bash
git clone -b claude/traser-implementation-guide-xlshit https://github.com/kanu2704/svg2-implementation && cd svg2-implementation
bash setup_kaggle.sh                      # official SVG2 code + transformers 4.54.1 + decord + SAM 2 (works on any Linux)
pip install scikit-learn matplotlib
# prepared videos are needed under $BENCH (<dataset>/<video>/{video.mp4, gt.json, masks.json}); see tools/bench_data.py
python3 tools/export_lm.py --model UWGZQ/TRASER --out $BIG/traser_lm
for g in 0 1; do CUDA_VISIBLE_DEVICES=$g python3 tools/interp/encode_stage.py --bench $BENCH --work $BIG/interp_work --shard $g --nshards 2 & done; wait
for g in 0 1; do CUDA_VISIBLE_DEVICES=$g python3 tools/interp/lm_stage.py --lm $BIG/traser_lm --work $BIG/interp_work --shard $g --nshards 2 & done; wait
python3 tools/interp/probe.py --work $BIG/interp_work && python3 tools/interp/report.py
git add results/traser_bench/interp && git commit -m "interp results" && git push origin HEAD:claude/traser-implementation-guide-xlshit
```
On GPUs with bfloat16 (A100/H100) the defaults stay float16, the format that produced the saved answers; pass
`--dtype bfloat16` to both stages to use the paper's format instead.
