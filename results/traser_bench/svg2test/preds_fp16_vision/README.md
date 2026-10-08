# Earlier answers, vision encoder + resamplers in float16

Moved here (not deleted) when the float16 T4 runs switched the vision encoder and both resamplers to float32
(`tools/run_traser.py: vision_in_float32`). These videos are re-run with that setting:

- `22cc4d54-…`, `P03_06` (and SVG2test `sav_009146`): the language model got inf/NaN inputs
  (`embeds_finite: false` in the stats) and wrote `!!!!…` (token 0) 8192 times.
- `c2e6d807-…_2`, `P05_05`, `1025_4615486172`: the answer loops (90–94 % repeated relations, all from one
  object) until the 8192-token limit. Re-run to see whether float16 caused the loop or TRASER loops anyway.

Compare the new answer in `../preds/` with the old one here.

SVG2test: all 19 SA-V answers from the first run (October 6, before the T4 fixes) are here as well, so that
all 100 SVG2test videos are run with the same settings (vision encoder and resamplers in float32).
