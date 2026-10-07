"""Run the released TRASER checkpoint over benchmark videos (one background worker per GPU).

    python tools/bench_run.py --bench <bench> --items svg2test/v1 pvsg/v2 vidor/v3 ... --gpu_name gpu0
    python tools/bench_run.py --bench <bench> --dataset pvsg --videos v1 v2 ...          (same, one dataset)

Items are the self-contained folders made by tools/bench_data.py (video.mp4, masks.json, gt.json). The
bench folder may be read-only (a Kaggle dataset): anything made here goes to --work (VidOR masks, made with
SAM 2 from VidOR's boxes) and --results (predictions).

For each item: make its masks if missing (VidOR), then run TRASER with the official settings
(``tools/run_traser.infer``: 1 fps, at most 128 frames, coverage 0.5, 4 s windows, greedy, at most
40 objects; bfloat16 on GPUs that have it, float16 otherwise) on all human objects, and write

    <results>/<dataset>/preds/<video_id>.json         TRASER's raw answer
    <results>/<dataset>/preds/<video_id>.stats.json   which mask column is "object k", timing, memory
    <results>/<dataset>/preds/<video_id>.error.txt    if it failed (e.g. out of GPU memory)
    <results>/<dataset>/gt/<video_id>.json            the human labels (for the evaluation)

<results> defaults to results/traser_bench in the repo. Items with a prediction are skipped, so a restarted
worker continues where it stopped. Offline: --model / --base_model / --sam2_ckpt point at local copies.
Progress: <runs>/<gpu_name>.json.
"""
import argparse
import faulthandler
import json
import os
import shutil
import sys
import threading
import time
import traceback
from pathlib import Path

os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")
os.environ.setdefault("PYTORCH_ALLOC_CONF", "expandable_segments:True")

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))
RESULTS = REPO / "results" / "traser_bench"


def pred_paths(dataset, video_id, results=None):
    d = Path(results or RESULTS) / dataset / "preds"
    return d / f"{video_id}.json", d / f"{video_id}.stats.json", d / f"{video_id}.error.txt"


def is_done(dataset, video_id, results=None):
    return pred_paths(dataset, video_id, results)[0].exists()


def timed_out(dataset, video_id, results=None):
    err = pred_paths(dataset, video_id, results)[2]
    return err.exists() and err.read_text().startswith("Timeout")


class Preparer:
    """Makes what an item is missing: VidOR masks (SAM 2 on the GPU); old-style PVSG/VidOR roots too."""
    def __init__(self, args):
        self.args = args
        self.anno = self.vidor = self.box_to_mask = None

    def sam2(self):
        import bench_data as B
        if self.box_to_mask is None:
            self.box_to_mask = B.BoxToMask(checkpoint=self.args.sam2_ckpt)
        return self.box_to_mask

    def __call__(self, dataset, video_id):
        import bench_data as B
        a = self.args
        if B.item_ready(a.bench, dataset, video_id, a.work):
            return
        item = B.item_dir(a.bench, dataset, video_id)
        if dataset == "vidor" and (item / "vidor_anno.json").exists():
            B.make_vidor_masks(a.bench, video_id, self.sam2(), out=a.work)
        elif dataset == "pvsg" and a.pvsg_root:
            import pvsg_data
            if self.anno is None:
                self.anno = pvsg_data.load_anno(a.pvsg_root)
            B.prepare_pvsg(a.pvsg_root, self.anno, video_id, a.bench, a.results)
        elif dataset == "vidor" and a.vidor_root:
            if self.vidor is None:
                self.vidor = B.vidor_index({"videos": os.path.join(a.vidor_root, "videos"),
                                            "anno": os.path.join(a.vidor_root, "anno")})
            ann, mp4 = self.vidor[video_id]
            B.prepare_vidor(ann, mp4, a.bench, a.results, self.sam2())
        else:
            raise FileNotFoundError(f"{dataset}/{video_id} is not prepared")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bench", required=True, help="folder with <dataset>/<video_id>/ items (may be read-only)")
    ap.add_argument("--items", nargs="*", default=None, help="dataset/video_id ...")
    ap.add_argument("--dataset", choices=["pvsg", "vidor", "svg2test"], default=None)
    ap.add_argument("--videos", nargs="*", default=None)
    ap.add_argument("--work", default=None, help="writable folder for masks made here (default: --bench)")
    ap.add_argument("--results", default=str(RESULTS))
    ap.add_argument("--runs", default="/kaggle/working/traser_bench_runs")
    ap.add_argument("--gpu_name", default="gpu0")
    ap.add_argument("--model", default=None, help="TRASER checkpoint (Hub id or local folder)")
    ap.add_argument("--base_model", default=None, help="Qwen2.5-VL-3B-Instruct processor (Hub id or local folder)")
    ap.add_argument("--sam2_ckpt", default=None, help="local sam2.1_hiera_large.pt (VidOR masks, offline)")
    ap.add_argument("--pvsg_root", default=None)
    ap.add_argument("--vidor_root", default=None)
    ap.add_argument("--max_objects", type=int, default=40)
    ap.add_argument("--dtype", default="auto")
    ap.add_argument("--timeout_min", type=float, default=20,
                    help="a video taking longer is recorded as failed (with where it hung) and the worker restarts")
    args = ap.parse_args()
    args.work = args.work or args.bench
    items = [tuple(x.split("/", 1)) for x in (args.items or [])]
    if args.dataset and args.videos:
        items += [(args.dataset, v) for v in args.videos]
    if not items:
        raise SystemExit("nothing to run: give --items or --dataset with --videos")

    os.makedirs(args.runs, exist_ok=True)
    name = f"{args.dataset}_{args.gpu_name}" if args.dataset and not args.items else args.gpu_name
    status_path = Path(args.runs, f"{name}.json")
    todo = [(ds, v) for ds, v in items if not is_done(ds, v, args.results) and not timed_out(ds, v, args.results)]
    hung = [f"{ds}/{v}" for ds, v in items if not is_done(ds, v, args.results) and timed_out(ds, v, args.results)]
    attempt = int(os.environ.get("BENCH_ATTEMPT", "1"))

    def log(msg):
        print(f"{time.strftime('%H:%M:%S')} [{args.gpu_name}] {msg}", flush=True)

    # finished videos of this queue (also from earlier runs): time per video, for the notebook's ETA
    recent = []
    for ds, v in items:
        st = pred_paths(ds, v, args.results)[1]
        if st.exists():
            try:
                s_ = json.loads(st.read_text())
                recent.append({"video": f"{ds}/{v}", "min": round(s_.get("total_s", 0) / 60, 1),
                               "tokens": s_.get("new_tokens"), "objects": s_.get("objects"), "t": st.stat().st_mtime})
            except (ValueError, OSError):
                pass
    recent.sort(key=lambda r: r.pop("t"))
    status = {"total": len(items), "done": len(items) - len(todo) - len(hung), "failed": hung, "current": None,
              "state": "starting (loading libraries)", "stage_since": time.time(), "video_since": None,
              "attempt": attempt, "recent": recent[-5:],
              "avg_min": round(sum(r["min"] for r in recent) / len(recent), 1) if recent else None,
              "started": time.strftime("%H:%M:%S")}
    last_write = [0.0]

    def save_status(force=True, **kw):
        if "state" in kw and kw["state"] != status.get("state"):
            kw.setdefault("stage_since", time.time())
        status.update(kw, updated=time.strftime("%H:%M:%S"))
        if not force and time.time() - last_write[0] < 3:
            return
        last_write[0] = time.time()
        tmp = status_path.with_suffix(".tmp")
        tmp.write_text(json.dumps(status, indent=1))
        tmp.replace(status_path)

    save_status()                      # before the slow imports, so the notebook sees the worker at once
    log(f"worker started (attempt {attempt}): {len(todo)} videos to run, {status['done']} already done, "
        f"{len(hung)} skipped (timed out before)")

    # watchdog: a video that hangs (seen on a few long Epic-Kitchens videos) must not block the queue.
    # Record where it hung, then restart this worker; the restarted worker skips timed-out videos.
    started = {}

    def watchdog():
        while True:
            time.sleep(10)
            if started and time.time() - started["t"] > args.timeout_min * 60:
                ds, v = started["item"]
                err = pred_paths(ds, v, args.results)[2]
                with open(err, "w") as f:
                    f.write(f"Timeout: no answer after {args.timeout_min:g} min (last step: {status['state']}); "
                            "stack at that moment:\n")
                    f.flush()
                    faulthandler.dump_traceback(file=f, all_threads=True)
                log(f"{ds}/{v} FAILED: timeout after {args.timeout_min:g} min (last step: {status['state']}) "
                    "-> skipping it, restarting the worker")
                os.execv(sys.executable, [sys.executable] + sys.argv)

    threading.Thread(target=watchdog, daemon=True).start()
    import torch
    import bench_data as B
    from run_traser import infer, load_model

    prepare = Preparer(args)
    model = processor = tokenizer = None
    oom = []
    for i, (dataset, video_id) in enumerate(todo, 1):
        item = f"{dataset}/{video_id}"
        out, stats_out, err_out = pred_paths(dataset, video_id, args.results)
        out.parent.mkdir(parents=True, exist_ok=True)
        try:
            save_status(current=item, video_since=time.time(), state="preparing")
            prepare(dataset, video_id)
            gt_copy = Path(args.results, dataset, "gt", f"{video_id}.json")
            if not gt_copy.exists():
                gt_copy.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(B.item_dir(args.bench, dataset, video_id) / "gt.json", gt_copy)
            if model is None:
                save_status(state="loading model")
                log("loading the TRASER model ...")
                t0 = time.time()
                model, processor, tokenizer = load_model(args.model, dtype=args.dtype, base_model=args.base_model)
                log(f"model loaded in {time.time() - t0:.0f} s ({getattr(model, 'dtype', '?')}, "
                    f"{torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'cpu'})")
            gt = B.load_gt(args.bench, dataset, video_id)
            masks = json.load(open(B.masks_path(args.bench, dataset, video_id, args.work)))
            log(f"{item} ({i}/{len(todo)}): {len(gt['objects'])} objects")
            started.update(t=time.time(), item=(dataset, video_id))
            save_status(video_since=time.time())
            last_logged = [0]

            def progress(stage, **info):
                if stage == "generating answer":
                    n = info.get("tokens", 0)
                    save_status(force=n == 0, state=f"generating answer: {n} tokens"
                                + (f" ({info['tokens_per_s']}/s)" if info.get("tokens_per_s") else ""))
                    if n == 0 or n - last_logged[0] >= 500:
                        last_logged[0] = n
                        log(f"{item}: generating answer, {n} tokens so far"
                            + (f" ({info['tokens_per_s']} tokens/s)" if info.get("tokens_per_s") else
                               f" (input: {info.get('input_tokens')} tokens)"))
                else:
                    extra = ", ".join(f"{k}={v}" for k, v in info.items())
                    save_status(state=stage + (f" ({extra})" if extra else ""))
                    log(f"{item}: {stage}" + (f" ({extra})" if extra else ""))

            t0 = time.time()
            text, stats = infer(model, processor, tokenizer, str(B.item_video(args.bench, gt)), masks,
                                objects=[o["col"] for o in gt["objects"]], max_objects=args.max_objects,
                                progress=progress)
            stats["total_s"] = round(time.time() - t0, 1)
            stats["gpu"] = torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu"
            stats_out.write_text(json.dumps(stats, indent=1))
            out.write_text(text)
            if err_out.exists():
                err_out.unlink()
            status["done"] += 1
            status["recent"] = (status["recent"] + [{"video": item, "min": round(stats["total_s"] / 60, 1),
                                                     "tokens": stats.get("new_tokens"),
                                                     "objects": stats.get("objects")}])[-5:]
            mins = [json.loads(pred_paths(d, v, args.results)[1].read_text()).get("total_s", 0) / 60
                    for d, v in items if pred_paths(d, v, args.results)[1].exists()]
            status["avg_min"] = round(sum(mins) / len(mins), 1) if mins else None
            log(f"{item} DONE in {stats['total_s'] / 60:.1f} min: {stats.get('new_tokens')} tokens, "
                f"{stats.get('objects')} objects, peak GPU memory {stats.get('peak_gpu_gb')} GB, "
                f"valid JSON: {stats.get('json_ok')}  ({status['done']}/{status['total']} done)")
        except Exception as e:  # noqa: BLE001  (one bad video must not stop the queue)
            msg = f"{type(e).__name__}: {e}\n{traceback.format_exc()}"
            err_out.write_text(msg)
            status["failed"].append(item)
            log(f"{item} FAILED: {type(e).__name__}: {str(e)[:300]}")
            if isinstance(e, torch.cuda.OutOfMemoryError):
                oom.append(item)
                torch.cuda.empty_cache()
        started.clear()
        save_status(current=None, state="next video")
    if oom and attempt == 1:
        # out of memory can depend on what the previous videos left behind: retry once in a fresh process
        save_status(state=f"retrying {len(oom)} out-of-memory videos in a fresh process")
        log(f"queue done; retrying {len(oom)} out-of-memory video(s) once in a fresh process: {oom}")
        os.execve(sys.executable, [sys.executable] + sys.argv, dict(os.environ, BENCH_ATTEMPT="2"))
    save_status(current=None, state="finished")
    log(f"finished: {status['done']} of {status['total']} done, failed: {status['failed'] or 'none'}")


if __name__ == "__main__":
    main()
