# Does TRASER place relations in time?

Relation recall (lenient, judge: nvidia/nemotron-3.5-super-vl-120b-a12b alone): a human relation is found when TRASER has the same two objects with a right word, and its time spans overlap the human ones with temporal IoU > 0.5. **Whole video**: the same answers with every relation's time replaced by the whole video. **Any time**: time not checked (the most timing could give). "Spanning the video": total length ≥ 90% of the video. Made by `tools/time_baseline.py`.

| dataset | human relations spanning the video | TRASER's relations spanning the video | relation recall, whole video | relation recall, its own times | relation recall, any time |
|---|---|---|---|---|---|
| PVSG | 20.2% | 15.2% | 10.9% | **12.9%** | 24.9% |
| VidOR | 15.8% | 37.8% | 7.9% | **10.7%** | 18.2% |
| SVG2test | 71.5% | 75.3% | 24.5% | **24.8%** | 27.3% |
