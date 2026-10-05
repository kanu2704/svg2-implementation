"""Run the released TRASER checkpoint over benchmark videos (one background worker per GPU).

    python tools/bench_run.py --dataset pvsg --bench /kaggle/tmp/bench --videos v1 v2 ... --gpu_name gpu0

For each video: prepare it if needed (PVSG: masks from PNGs; VidOR: masks from boxes with SAM 2;
SVG2test items are prepared in the notebook), then run TRASER with the official settings
(``tools/run_traser.infer``: 1 fps, at most 128 frames, coverage 0.5, 4 s windows, greedy, at most
40 objects) on all human objects, and write

    results/traser_bench/<dataset>/preds/<video_id>.json         TRASER's raw answer
    results/traser_bench/<dataset>/preds/<video_id>.stats.json   which mask column is "object k", timing, memory
    results/traser_bench/<dataset>/preds/<video_id>.error.txt    if it failed (e.g. out of GPU memory)

straight into the repo, so finished videos survive the Kaggle session once pushed. Videos with a
prediction are skipped, so a restarted worker continues where it stopped. Progress:
``<runs>/<dataset>_<gpu_name>.json``.
"""
import argparse
import json
import os
import sys
import time
import traceback
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))
RESULTS = REPO / "results" / "traser_bench"


def pred_paths(dataset, video_id):
    d = RESULTS / dataset / "preds"
    return d / f"{video_id}.json", d / f"{video_id}.stats.json", d / f"{video_id}.error.txt"


def is_done(dataset, video_id):
    return pred_paths(dataset, video_id)[0].exists()


class Preparer:
    """Makes bench items that do not exist yet (PVSG and VidOR)."""
    def __init__(self, args):
        self.args = args
        self.anno = self.vidor = self.box_to_mask = None

    def __call__(self, dataset, video_id):
        import bench_data as B
        if B.item_ready(self.args.bench, dataset, video_id):
            return
        if dataset == "pvsg":
            import pvsg_data
            if self.anno is None:
                self.anno = pvsg_data.load_anno(self.args.pvsg_root)
            B.prepare_pvsg(self.args.pvsg_root, self.anno, video_id, self.args.bench, RESULTS)
        elif dataset == "vidor":
            if self.vidor is None:
                self.vidor = B.vidor_index({"videos": os.path.join(self.args.vidor_root, "videos"),
                                            "anno": os.path.join(self.args.vidor_root, "anno")})
            if self.box_to_mask is None:
                self.box_to_mask = B.BoxToMask()
            ann, mp4 = self.vidor[video_id]
            B.prepare_vidor(ann, mp4, self.args.bench, RESULTS, self.box_to_mask)
        else:
            raise FileNotFoundError(f"{dataset}/{video_id} is not prepared (run the preparation cell)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", required=True, choices=["pvsg", "vidor", "svg2test"])
    ap.add_argument("--bench", required=True)
    ap.add_argument("--runs", default="/kaggle/working/traser_bench_runs")
    ap.add_argument("--videos", nargs="+", required=True)
    ap.add_argument("--gpu_name", default="gpu0")
    ap.add_argument("--pvsg_root", default=None)
    ap.add_argument("--vidor_root", default=None)
    ap.add_argument("--max_objects", type=int, default=40)
    ap.add_argument("--dtype", default="float16")
    args = ap.parse_args()

    import torch
    import bench_data as B
    from run_traser import infer, load_model

    os.makedirs(args.runs, exist_ok=True)
    status_path = Path(args.runs, f"{args.dataset}_{args.gpu_name}.json")
    todo = [v for v in args.videos if not is_done(args.dataset, v)]
    status = {"dataset": args.dataset, "total": len(args.videos), "done": len(args.videos) - len(todo),
              "failed": [], "current": None, "state": "loading model", "started": time.strftime("%H:%M:%S")}

    def save_status(**kw):
        status.update(kw, updated=time.strftime("%H:%M:%S"))
        tmp = status_path.with_suffix(".tmp")
        tmp.write_text(json.dumps(status, indent=1))
        tmp.replace(status_path)

    save_status()
    prepare = Preparer(args)
    model = processor = tokenizer = None
    for video_id in todo:
        out, stats_out, err_out = pred_paths(args.dataset, video_id)
        out.parent.mkdir(parents=True, exist_ok=True)
        try:
            save_status(current=video_id, state="preparing")
            prepare(args.dataset, video_id)
            if model is None:
                save_status(state="loading model")
                model, processor, tokenizer = load_model(dtype=args.dtype)
            gt = B.load_gt(args.bench, args.dataset, video_id)
            masks = json.load(open(Path(args.bench, args.dataset, video_id, "masks.json")))
            save_status(state="running TRASER")
            t0 = time.time()
            text, stats = infer(model, processor, tokenizer, gt["video"], masks,
                                objects=[o["col"] for o in gt["objects"]], max_objects=args.max_objects)
            stats["total_s"] = round(time.time() - t0, 1)
            stats_out.write_text(json.dumps(stats, indent=1))
            out.write_text(text)
            if err_out.exists():
                err_out.unlink()
            status["done"] += 1
        except Exception as e:  # noqa: BLE001  (one bad video must not stop the queue)
            msg = f"{type(e).__name__}: {e}\n{traceback.format_exc()}"
            err_out.write_text(msg)
            status["failed"].append(video_id)
            print(f"[{video_id}] FAILED: {msg}", file=sys.stderr, flush=True)
            if isinstance(e, torch.cuda.OutOfMemoryError):
                torch.cuda.empty_cache()
        save_status()
        print(f"[{video_id}] done ({status['done']}/{status['total']})", flush=True)
    save_status(current=None, state="finished")


if __name__ == "__main__":
    main()
