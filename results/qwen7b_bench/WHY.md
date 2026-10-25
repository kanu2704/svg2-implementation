# Why Qwen-7B (not fine-tuned) fails in TRASER's pipeline

No judge: exact names after normalising (lower case, "_" -> " "). **Human pairs written**: share of the human pairs between objects it was given that its answer mentions at all, with any word. **Own name**: the object got the human name of that very object. **Another object's name**: it got the human name of a different object it was given in the same video (the name is in the video, but on the wrong object number). Made by `tools/qwen_why.py`.

| dataset | model | human pairs written | objects named | own name | another object's name |
|---|---|---|---|---|---|
| PVSG | TRASER | 263 of 739 (36%) | 1,166 | 333 (29%) | 127 (11%) |
| PVSG | Qwen-7B | 29 of 739 (4%) | 1,060 | 33 (3%) | 210 (20%) |
| VidOR | TRASER | 4,629 of 11,157 (41%) | 3,973 | 1,270 (32%) | 61 (2%) |
| VidOR | Qwen-7B | 1,963 of 11,157 (18%) | 3,719 | 702 (19%) | 165 (4%) |
| SVG2test | TRASER | 985 of 2,570 (38%) | 2,820 | 755 (27%) | 417 (15%) |
| SVG2test | Qwen-7B | 203 of 2,570 (8%) | 1,688 | 113 (7%) | 425 (25%) |
