"""Write TRASER's answers with vLLM, from the input sequences tools/bench_run.py --mode encode saved.

Runs in its own Python environment (vLLM brings its own PyTorch), one process per GPU:

    CUDA_VISIBLE_DEVICES=0 /tmp/venv_vllm/bin/python tools/vllm_generate.py --lm /tmp/traser_lm \
        --embeds /tmp/traser_embeds --dataset vidor --videos v1 v2 ... --gpu_name gpu0
    /tmp/venv_vllm/bin/python tools/vllm_generate.py --lm /tmp/traser_lm --check     (does vLLM work here?)

--lm is TRASER's language model exported by tools/export_lm.py (the checkpoint's own weights). vLLM gets
each video's arranged embedding sequence as "prompt embeddings" (TRASER uses plain positions 0..L-1, so
this is exactly its language model) and decodes like the Hugging Face path: greedy, at most 8192 new
tokens, stop at <|im_end|> / <|endoftext|>, repetition penalty 1.05 (from the checkpoint's
generation_config.json, which Hugging Face's generate applies too). Many videos are decoded at once.

Writes exactly what tools/bench_run.py writes, so the scoring does not change:
    <results>/<dataset>/preds/<video_id>.json         the answer text
    <results>/<dataset>/preds/<video_id>.stats.json   the encode stats + engine "vllm", tokens, timing
    <results>/<dataset>/preds/<video_id>.error.txt    if it failed
Progress: <runs>/<dataset>_<gpu_name>.json (+ the log on stdout), same fields as bench_run's.
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
from answers import answer_stats  # noqa: E402

RESULTS = REPO / "results" / "traser_bench"
STOP_IDS = [151645, 151643]          # <|im_end|>, <|endoftext|> (TRASER's generation_config.json)


def pred_paths(results, dataset, video_id):
    d = Path(results) / dataset / "preds"
    return d / f"{video_id}.json", d / f"{video_id}.stats.json", d / f"{video_id}.error.txt"


def embeds_path(embeds, dataset, video_id):
    return Path(embeds) / dataset / f"{video_id}.pt"


def gpu_name():
    import torch
    return torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu"


def make_llm(args, dtype):
    from vllm import LLM
    kw = dict(model=args.lm, tokenizer=args.lm, dtype=dtype, enable_prompt_embeds=True,
              max_model_len=args.max_model_len, gpu_memory_utilization=args.gpu_memory_utilization,
              enforce_eager=args.enforce_eager, seed=0, generation_config="vllm", max_num_seqs=args.max_num_seqs)
    try:
        return LLM(**kw)
    except TypeError as e:                       # older vLLM without generation_config=
        if "generation_config" not in str(e):
            raise
        kw.pop("generation_config")
        return LLM(**kw)


def sampling(args, max_tokens=None, penalty=None):
    from vllm import SamplingParams
    return SamplingParams(temperature=0.0, max_tokens=max_tokens or args.max_new_tokens,
                          repetition_penalty=args.repetition_penalty if penalty is None else penalty,
                          stop_token_ids=STOP_IDS, skip_special_tokens=True, detokenize=False)


def progress_bar(on_update):
    """A tqdm class vLLM can use as its progress bar: reports every finished answer to on_update."""
    from tqdm import tqdm

    class Bar(tqdm):
        def __init__(self, *a, **k):
            k["file"] = open(os.devnull, "w")
            super().__init__(*a, **k)

        def update(self, n=1):
            r = super().update(n)
            on_update(self.n, self.total, str(self.postfix or ""))
            return r
    return Bar


def run_generate(llm, prompts, params, bar):
    try:
        return llm.generate(prompts, params, use_tqdm=bar)
    except TypeError:                            # older vLLM: use_tqdm must be a bool
        return llm.generate(prompts, params, use_tqdm=False)


def check(args):
    """Does vLLM start here (GPU, dtype, attention) and accept prompt embeddings? Same tokens from a
    tokenized prompt and from its embeddings, then a throughput test on 8 long random inputs."""
    import torch
    import vllm
    from safetensors import safe_open
    from transformers import AutoTokenizer
    t0 = time.time()
    cc = torch.cuda.get_device_capability(0)
    dtype = "half" if cc[0] < 8 else "bfloat16"
    print(f"vLLM {vllm.__version__}, torch {torch.__version__}, GPU {torch.cuda.get_device_name(0)} "
          f"(compute {cc[0]}.{cc[1]}), dtype {dtype}", flush=True)
    llm = make_llm(args, dtype)
    print(f"engine started in {time.time() - t0:.0f} s", flush=True)
    tok = AutoTokenizer.from_pretrained(args.lm, use_fast=False)
    ids = tok("Output the Video Scene Graph from the video and object trajectories:\n")["input_ids"]
    index = json.load(open(Path(args.lm) / "model.safetensors.index.json"))["weight_map"]
    with safe_open(str(Path(args.lm) / index["model.embed_tokens.weight"]), framework="pt") as f:
        table = f.get_tensor("model.embed_tokens.weight")
    pe = table[torch.tensor(ids)].to(torch.float16 if dtype == "half" else torch.bfloat16)
    sp = sampling(args, max_tokens=40, penalty=1.0)
    a = llm.generate({"prompt_token_ids": ids}, sp, use_tqdm=False)[0].outputs[0].token_ids
    b = llm.generate({"prompt_embeds": pe}, sp, use_tqdm=False)[0].outputs[0].token_ids
    same = list(a) == list(b)
    print(f"tokens from the text prompt:  {list(a)[:16]} ...\ntokens from its embeddings: {list(b)[:16]} ...\n"
          f"→ prompt embeddings {'give the same answer ✓' if same else 'give a DIFFERENT answer ✗'}", flush=True)
    g = torch.Generator().manual_seed(0)
    long = [{"prompt_embeds": (table[torch.randint(0, 151000, (4000,), generator=g)]).to(pe.dtype)} for _ in range(8)]
    t1 = time.time()
    outs = llm.generate(long, sampling(args, max_tokens=512, penalty=args.repetition_penalty), use_tqdm=False)
    n = sum(len(o.outputs[0].token_ids) for o in outs)
    dt = time.time() - t1
    print(f"throughput: 8 inputs of 4000 tokens, {n} tokens written in {dt:.0f} s = {n / dt:.0f} tokens/s "
          f"(Hugging Face, one video at a time on a T4: ~16 tokens/s)", flush=True)
    print("CHECK OK" if same else "CHECK FAILED", flush=True)
    return 0 if same else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lm", default="/tmp/traser_lm", help="folder from tools/export_lm.py")
    ap.add_argument("--embeds", default="/tmp/traser_embeds")
    ap.add_argument("--results", default=str(RESULTS))
    ap.add_argument("--runs", default="/kaggle/working/traser_bench_runs")
    ap.add_argument("--items", nargs="*", default=None, help="dataset/video_id ...")
    ap.add_argument("--dataset", default=None)
    ap.add_argument("--videos", nargs="*", default=None)
    ap.add_argument("--gpu_name", default="gpu0")
    ap.add_argument("--name", default=None, help="progress file name prefix (default: the dataset)")
    ap.add_argument("--batch", type=int, default=32, help="videos handed to vLLM at once")
    ap.add_argument("--max_new_tokens", type=int, default=8192)
    ap.add_argument("--repetition_penalty", type=float, default=1.05)
    ap.add_argument("--max_model_len", type=int, default=49152)
    ap.add_argument("--max_num_seqs", type=int, default=32)
    ap.add_argument("--gpu_memory_utilization", type=float, default=0.90)
    ap.add_argument("--enforce_eager", action="store_true", help="no CUDA graphs (slower, fewer surprises)")
    ap.add_argument("--check", action="store_true", help="only test that vLLM works here")
    args = ap.parse_args()
    if args.check:
        return check(args)

    items = [tuple(x.split("/", 1)) for x in (args.items or [])]
    if args.dataset and args.videos:
        items += [(args.dataset, v) for v in args.videos]
    if not items:
        raise SystemExit("nothing to run: give --items or --dataset with --videos")
    name = (f"{args.name}_{args.gpu_name}" if args.name else
            f"{args.dataset}_{args.gpu_name}" if args.dataset and not args.items else args.gpu_name)
    os.makedirs(args.runs, exist_ok=True)
    status_path = Path(args.runs, f"{name}.json")

    def log(msg):
        print(f"{time.strftime('%H:%M:%S')} [{args.gpu_name}] {msg}", flush=True)

    for ds in {d for d, _ in items}:
        (Path(args.results) / ds / "preds").mkdir(parents=True, exist_ok=True)
    done = [it for it in items if pred_paths(args.results, *it)[0].exists()]
    todo = [it for it in items if it not in done and embeds_path(args.embeds, *it).exists()]
    missing = [f"{d}/{v}" for d, v in items if (d, v) not in done and not embeds_path(args.embeds, d, v).exists()]
    status = {"total": len(items), "done": len(done), "failed": [], "current": None, "state": "starting vLLM",
              "stage_since": time.time(), "video_since": None, "attempt": 1, "recent": [], "avg_min": None,
              "started": time.strftime("%H:%M:%S"), "engine": "vllm"}

    def save_status(**kw):
        if "state" in kw and kw["state"] != status.get("state"):
            kw.setdefault("stage_since", time.time())
        status.update(kw, updated=time.strftime("%H:%M:%S"))
        tmp = status_path.with_suffix(".tmp")
        tmp.write_text(json.dumps(status, indent=1))
        tmp.replace(status_path)

    save_status()
    log(f"vLLM worker started: {len(todo)} videos to write, {len(done)} already done"
        + (f", {len(missing)} not encoded yet (skipped): {missing[:5]}" if missing else ""))
    if not todo:
        save_status(state="finished")
        log("nothing to do")
        return 0

    import torch
    import vllm
    from transformers import AutoTokenizer
    first = torch.load(embeds_path(args.embeds, *todo[0]), map_location="cpu")
    dtype = "half" if first["embeds"].dtype == torch.float16 else "bfloat16"
    del first
    t0 = time.time()
    save_status(state="loading the language model into vLLM")
    log(f"loading the exported TRASER language model into vLLM {vllm.__version__} ({dtype}) ...")
    llm = make_llm(args, dtype)
    tok = AutoTokenizer.from_pretrained(args.lm, use_fast=False)
    log(f"vLLM ready in {time.time() - t0:.0f} s ({gpu_name()})")
    params = sampling(args)
    chunks = [todo[i:i + args.batch] for i in range(0, len(todo), args.batch)]
    failed_chunks = 0
    for c, chunk in enumerate(chunks, 1):
        data, prompts, ok = [], [], []
        for ds, v in chunk:
            try:
                d = torch.load(embeds_path(args.embeds, ds, v), map_location="cpu")
                n_in = int(d["embeds"].shape[0])
                if n_in + args.max_new_tokens > args.max_model_len:
                    raise ValueError(f"input of {n_in} tokens + {args.max_new_tokens} new tokens is more than "
                                     f"--max_model_len {args.max_model_len}")
                data.append(d)
                prompts.append({"prompt_embeds": d["embeds"]})
                ok.append((ds, v))
            except Exception as e:  # noqa: BLE001
                pred_paths(args.results, ds, v)[2].write_text(f"{type(e).__name__}: {e}")
                status["failed"].append(f"{ds}/{v}")
                log(f"{ds}/{v} FAILED before vLLM: {e}")
        if not ok:
            continue
        n_tokens_in = sum(int(d["embeds"].shape[0]) for d in data)
        save_status(current=f"{len(ok)} videos (batch {c}/{len(chunks)})", video_since=time.time(),
                    state=f"writing answers: 0/{len(ok)} finished")
        log(f"batch {c}/{len(chunks)}: {len(ok)} videos ({n_tokens_in} input tokens) handed to vLLM")
        t1 = time.time()

        def on_update(n, total, postfix, _t=t1, _c=c):
            save_status(state=f"writing answers: {n}/{total} finished ({postfix.strip() or 'speed: -'})")
            if n == total or n % 8 == 0:
                log(f"batch {_c}/{len(chunks)}: {n}/{total} answers finished after {time.time() - _t:.0f} s  {postfix}")
        try:
            outs = run_generate(llm, prompts, params, progress_bar(on_update))
            failed_chunks = 0
        except Exception as e:  # noqa: BLE001  (e.g. out of memory: record it and go on)
            failed_chunks += 1
            msg = f"{type(e).__name__}: {e}\n{traceback.format_exc()}"
            for ds, v in ok:
                pred_paths(args.results, ds, v)[2].write_text(msg)
                status["failed"].append(f"{ds}/{v}")
            log(f"batch {c} FAILED: {type(e).__name__}: {str(e)[:300]}")
            save_status(state=f"batch {c} failed")
            if failed_chunks >= 2:
                log("two batches in a row failed: stopping (see the .error.txt files)")
                break
            continue
        dt = time.time() - t1
        n_new = 0
        for (ds, v), d, o in zip(ok, data, outs):
            out, stats_out, err_out = pred_paths(args.results, ds, v)
            out.parent.mkdir(parents=True, exist_ok=True)
            ids = list(o.outputs[0].token_ids)
            n_new += len(ids)
            text = tok.decode(ids, skip_special_tokens=True)
            stats = json.loads(d["stats"]) if isinstance(d["stats"], str) else dict(d["stats"])
            stats.update(engine="vllm", vllm_version=vllm.__version__, new_tokens=len(ids),
                         finish_reason=o.outputs[0].finish_reason, generate_batch=len(ok),
                         generate_batch_s=round(dt, 1), repetition_penalty=args.repetition_penalty,
                         generate_gpu=gpu_name())
            stats["total_s"] = round(stats.get("encode_s", 0) + dt / len(ok), 1)
            stats.update(answer_stats(text))
            stats_out.write_text(json.dumps(stats, indent=1))
            out.write_text(text)
            if err_out.exists():
                err_out.unlink()
            status["done"] += 1
            status["recent"] = (status["recent"] + [{"video": f"{ds}/{v}", "min": round(dt / len(ok) / 60, 2),
                                                     "tokens": len(ids), "objects": stats.get("objects")}])[-5:]
        status["avg_min"] = round(sum(r["min"] for r in status["recent"]) / len(status["recent"]), 2)   # per video, batched
        log(f"batch {c}/{len(chunks)} DONE in {dt / 60:.1f} min: {len(ok)} answers, {n_new} tokens "
            f"({n_new / max(dt, 1e-6):.0f} tokens/s)  ({status['done']}/{status['total']} done)")
        save_status(current=None, state="next batch")
    save_status(current=None, state="finished")
    log(f"finished: {status['done']} of {status['total']} done, failed: {status['failed'] or 'none'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
