# vLLM vs Hugging Face: the same 10 vidor videos

Same checkpoint, same input sequence; answers written once by Hugging Face `generate` (one video at a time) and once by vLLM (many at once). Made by `tools/vllm_check.py`.

**8 of 10 answers are identical.** Right (Hugging Face / vLLM): objects 39 / 39 of 49, relations 23 / 24 of 254, triplets 14 / 14 of 254 (314 label pairs not judged yet).

| video | identical | same_until | tokens_hf | tokens_vllm | json_hf | json_vllm | objects_right | relations_right | triplets_right | unjudged |
|---|---|---|---|---|---|---|---|---|---|---|
| 2478735417 | True | end | 137 | 137 | True | True | 2 / 2 of 2 | 1 / 1 of 5 | 1 / 1 of 5 | 10 |
| 2716277960 | True | end | 480 | 480 | True | True | 4 / 4 of 6 | 3 / 3 of 30 | 1 / 1 of 30 | 16 |
| 2726497009 | False | 951/1600 characters (59%) | 648 | 648 | True | True | 8 / 8 of 8 | 5 / 5 of 25 | 5 / 5 of 25 | 48 |
| 3489439407 | True | end | 509 | 509 | True | True | 4 / 4 of 6 | 0 / 0 of 38 | 0 / 0 of 38 | 28 |
| 4217422838 | True | end | 480 | 480 | True | True | 3 / 3 of 4 | 7 / 7 of 30 | 3 / 3 of 30 | 90 |
| 4740074365 | True | end | 461 | 461 | True | True | 5 / 5 of 5 | 3 / 3 of 35 | 3 / 3 of 35 | 46 |
| 5017166671 | True | end | 530 | 530 | True | True | 6 / 6 of 6 | 1 / 1 of 14 | 1 / 1 of 14 | 12 |
| 7308042410 | True | end | 177 | 177 | True | True | 2 / 2 of 2 | 0 / 0 of 8 | 0 / 0 of 8 | 38 |
| 8224492254 | False | 772/1535 characters (50%) | 564 | 543 | True | True | 2 / 2 of 6 | 3 / 4 of 56 | 0 / 0 of 56 | 12 |
| 9441605497 | True | end | 315 | 315 | True | True | 3 / 3 of 4 | 0 / 0 of 13 | 0 / 0 of 13 | 14 |
