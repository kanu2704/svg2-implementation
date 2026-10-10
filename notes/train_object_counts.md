# Objects per video in TRASER's training data (the 40-object question)

Made by `tools/train_object_counts.py` from the released SVG2 annotations. `objects` = annotated objects of a video, which is the `obj_list` that `traser/data/prepare_svg2.py` writes and the data loader gives to the model (objects without a mask on the sampled frames are dropped later, so the real number can be a little lower). The training code itself has no object cap; docs/DATA.md applies `--max_object 40` to pvd only.

| split | used for | cap in DATA.md | videos | median objects | max objects | videos with > 40 | % videos > 40 | max objects given to TRASER |
|---|---|---|---|---|---|---|---|---|
| cleaned/sav | training (`svg2_sav`) | none | 42906 | 15 | 40 | 0 | 0.0 | 40 |
| cleaned/pvd | training (`svg2_pvd`) | first 40 | 546935 | 7 | 60 | 11248 | 2.1 | 40 |
| academic_datasets/vipseg | training (`vipseg`) | none | 2750 | 10 | 108 | 82 | 3.0 | 108 |
| academic_datasets/vidor | training (`vidor`) | none | 7000 | 4 | 30 | 0 | 0.0 | 30 |
| academic_datasets/vidvrd | training (`vidvrd`) | none | 800 | 2 | 14 | 0 | 0.0 | 14 |
| academic_datasets/lvvis | training (`lvvis`) | none | 3054 | 4 | 45 | 2 | 0.1 | 45 |
| academic_datasets/ovis | training (`ovis`) | none | 607 | 5 | 44 | 1 | 0.2 | 44 |
| SVG2_test/sav | test | none | 33 | 36 | 63 | 12 | 36.4 | 63 |
| SVG2_test/vipseg | test | none | 67 | 25 | 89 | 19 | 28.4 | 89 |

**Training videos with more than 40 objects outside the capped pvd split: 85.** So the released checkpoint did see samples with more than 40 objects in training.

## Files in the model repo `UWGZQ/TRASER`

- `.gitattributes`
- `README.md`
- `added_tokens.json`
- `chat_template.jinja`
- `config.json`
- `example/2401075277.mp4`
- `example/2401075277_rle.json`
- `generation_config.json`
- `inference.py`
- `merges.txt`
- `model-00001-of-00002.safetensors`
- `model-00002-of-00002.safetensors`
- `model.safetensors.index.json`
- `modeling_traser.py`
- `qwen_vl_vsg_utils/src/qwen_vl_utils/__init__.py`
- `qwen_vl_vsg_utils/src/qwen_vl_utils/__pycache__/__init__.cpython-310.pyc`
- `qwen_vl_vsg_utils/src/qwen_vl_utils/__pycache__/vision_process.cpython-310.pyc`
- `qwen_vl_vsg_utils/src/qwen_vl_utils/vision_process.py`
- `resampler_utils/token_arrangement.py`
- `resampler_utils/token_selection.py`
- `special_tokens_map.json`
- `static/image.png`
- `tokenizer_config.json`
- `vocab.json`
