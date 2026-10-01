# Plot-hole register

Every suspicious point found while re-implementing SVG2 / TraSeR, with its evidence and status.
**Status:** ✅ confirmed · ❌ rejected · 🟡 open (hypothesis, test planned) · 🔄 partly answered.
IDs follow the implementation plan (Part C); new ones are numbered from P25.

| ID | Claim or issue | Status | Evidence so far | Next test |
|---|---|---|---|---|
| P1 | Evaluation can't be reproduced from the release | ✅ | Repo has no eval, judge or baseline code | Build `eval/` (Phase 5) |
| P2 | Recall-only metrics reward over-generation | 🟡 | Paper reports only recall/accuracy | Add precision/F1 (Phase 5) |
| P3 | Lenient LLM judge inflates scores | 🟡 | TraSeR object acc. 72–91% lenient vs 29–42% strict (Tables 2, 9) | Judge category breakdown (Phase 5) |
| P4 | Attribute judge never validated | ✅ | Table 3 covers objects and relations only | Our own κ on attributes (Phase 5) |
| P5 | VQA gains within noise | ✅ | AGQA +0.4 over video-only, n=1000, SE≈1.4 | McNemar test (Phase 7) |
| P6 | Ablations single-seed, small deltas | ✅ | Tables 6, 11 | Re-run with seeds (Phase 6) |
| P7 | "Consistently improves with data" overstated | ✅ | Table 10 non-monotonic columns | Phase 6 |
| P8 | Resamplers can't see token order | 🔄 | Idefics2 Perceiver has no input positions | Shuffle test (Phase 3.5b) |
| P9 | Absolute spatial position removed (1D RoPE) | 🔄 | `token_arrangement.py:244-249` | Probe + ablation (Phases 3, 6) |
| P10 | No scene context outside object masks | ✅ | Unselected tokens dropped; example video: **53%** of video tokens belong to no object (`experiments/phase2/*.stats.json`) | Count dropped tokens (Phase 3.3c) |
| P11 | "Compact" depends on object count | 🔄 | Length formula (plan 3.4); example video 7,429 raw → 2,641 arranged tokens (9 objects); small objects are expanded (23 tokens → 32 + 32/window latents) | Length histogram (Phase 1.6/3) |
| P12 | 20K truncation cuts the answer | 🔄 | `trainer_insert.py:166-179` | Count truncations (Phase 4) |
| P13 | Long videos: 128-frame cap vs 1-fps timestamps | 🔄 | `inference.py:49`, `trainer_insert.py:122-142` vs paper App. E.4 | Effective-fps check (Phase 3.1) |
| P14 | Relation spans not in seconds | ❌ | `notes/phase1_durations.md`: SA-V spans end ≤ video length in 42,346 of 42,347 videos; implied fps ≈ 22–28 for SA-V and PVD; PVD spans reach 60 s | — |
| P15 | Released pipeline ≠ pipeline that built the data | ✅ | Code lacks SAM3 step, but `sam3_output/` is released; PVD spans reach 60 s although `run_full.yaml` caps relation frames at 24; parser model and DAM frame choice differ from paper | Phase 8 (optional) |
| P16 | Training details differ or are unstated | ✅ | Warmup 0.03 vs 0.01; relation type dropped; resampler wd 0 | — |
| P17 | Some Table 6 variants not runnable | ✅ | `use_resampler=False` crashes | Patches (Phase 6) |
| P18 | Comparison fairness (masks, +350M params, GPT-5-derived labels) | 🟡 | Setup confirmed | Phase 5 |
| P19 | Train/test video overlap | ❌ | `notes/phase1_audit.md` §A: 0 shared ids, 0 shared VIPSeg YouTube sources | PVSG vs VidOR still untested |
| P20 | Label quality/style leaks into the model | 🔄 | Training attributes 14.6% subjective words (SA-V) vs 1.7% test; academic labels `car_(automobile)`, `chair or seat`, `Vehical` | Phase 2 outputs |
| P21 | Perceiver latents initialised identical | ✅ | Idefics2 `latents.fill_(1.0)` | Latent diversity (Phase 3.5c) |
| P22 | [TRJ] notation vs code | ✅ | cosmetic | — |
| P23 | `lm_head.requires_grad` on module | ✅ | minor | — |
| P24 | Tracking AR numbers not reproducible | ✅ | no protocol, no code | — |
| **P25** | Span convention differs train vs test | ✅ | Training: `[a,b]` inclusive seconds (docs/DATA.md). Test card: frames `round(a·fps)`…`round(b·fps)−1` (end-exclusive); 103 test spans are `[x, x]` = zero frames; 7% of test endpoints are half-seconds | Evaluator must convert (Phase 5) |
| **P26** | Released checkpoint trained on different data than released `cleaned` | 🟡 | Reference output and our T4 run both have 2/9 labels with "(uncertain)"; cleaned has 0 (SA-V) / 0.04% (PVD). Cleaning *keeps* ~20–30% of raw "(uncertain)" objects but strips the suffix | Count "(uncertain)" in outputs (Phase 2) |
| **P27** | Test attributes include types the training data excludes | ✅ | Test typed attributes: motion 9–11%, position 7–10%, state 7–8%, action 4–5%; the parser prompt (paper Table 14) defines attributes as visual-only and puts actions/relations elsewhere; training has 8 attrs/object vs 3 in test | Per-type attribute recall (Phase 5) |
| **P28** | "636K videos" counts raw data; objects count cleaned data | ✅ | raw 636,855 videos; cleaned 589,841 videos / 6.55M objects; paper: 636K / 6.6M. Released relations 7.16M vs paper 6.7M | — |
| **P29** | Cleaning is a class-selective filter, not just noise removal | ✅ | Every cleaned object is an exact raw object (100% twin match), but keep rates vary by class: sky 92%, person-wear 80–85% vs surfboard 2%, remote control 2%, telephone wire 0%, street light 5%, skateboard 5–7%, mirror 9%. Thin/small classes SAM3 misses are removed | Does TraSeR fail on these classes? (Phase 5) |
| **P30** | Some academic mask files are shorter than their annotations | 🔄 | 35 VidOR and 4 VidVRD videos have only 30–65 mask frames but relations to 3–7 s (implied < 10 fps; these videos are normally ~30 fps) | Check against the real videos' frame counts; affects few samples |
| **P31** | Training targets contain noise the model is taught to reproduce | ✅ | `notes/figs/sample_*.md`: a garbled attribute (`"creed?"`, sample 109288954); overlapping duplicate spans from the converter's merge step (`[[2, 12], [2, 13]]`); inverse duplicates (`ring on hand` + `hand wearing ring`); instantaneous events spanning the whole clip (`hand picking up rind [[0, 17]]`, `hand put on ring [[2, 12]]`) | Count these patterns at scale (Phase 3/5) |
| **P32** | "Panoptic" masks leave large regions unlabelled | 🔄 | Samples: sleeve and ground (109288954), the other person's hand giving the banknotes (13997279), the watermelon flesh (126491052) have no mask, so their tokens are dropped and no relation can mention them; 109288954 has 5 objects for a whole scene | Measure the uncovered fraction of tokens (Phase 2 stats `tokens_dropped_fraction`, Phase 3) |
| **P33** | The Hub's standalone inference differs from GitHub inference and training | ✅ | `notes/phase2_hf_vs_github.md`: Hub `select_tokens` default τ = 0.7 and the Hub `inference.py` passes no threshold (paper/training: 0.5); Hub uses a modified `qwen_vl_utils` frame sampler instead of the training loader's | Done on 1 video: τ 0.7 drops 10% more tokens, output change ≈ numeric noise; needs many videos (Phase 5) |
| **P34** | `repetition_penalty 1.05` in the shipped generation config | 🟡 | `generation_config.json`; scene-graph JSON is repetitive by nature | Ablate 1.0 vs 1.05 (Phase 5) |
| **P35** | Outputs are sensitive to numerics | ✅ | Same video, same weights, greedy: fp16/T4 15/22, bf16/T4 17/22 relations identical to the A100 reference; attribute lists 4–6/9 identical; object labels always identical (`notes/phase2_findings.md`) | Metric variance across runs (Phase 5) |
