"""Write answers with a fine-tuned language model on the test videos (greedy, like TRASER's own run).

Input per video: the saved sequence from tools/interp/encode_stage.py (the same input TRASER's answers came from).
Output, in the format bench_eval reads:
    results/traser_bench/finetune/<name>/<dataset>/preds/<video>.json         the answer
    results/traser_bench/finetune/<name>/<dataset>/preds/<video>.stats.json   TRASER's run stats for the video
                                                                              (object numbers -> masks, duration)
Videos already answered are skipped, so it can be stopped and run again.

    CUDA_VISIBLE_DEVICES=0 python3 tools/finetune/generate.py --lm $BIG/ft_sft --name sft --work $BIG/interp_work \
        --datasets vidor svg2test pvsg --n '{"vidor": 300, "svg2test": 0, "pvsg": 0}'
"""
import argparse
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent))
from finetune import common as F  # noqa: E402
from interp import common as IC  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lm", required=True, help="model folder (sft.py / grpo.py output)")
    ap.add_argument("--name", required=True, help="results folder name, e.g. sft or grpo")
    ap.add_argument("--work", required=True, help="encode_stage output of the test videos")
    ap.add_argument("--results", default=str(IC.RESULTS), help="TRASER's run (stats per video)")
    ap.add_argument("--out", default=str(F.OUT))
    ap.add_argument("--datasets", nargs="+", default=["vidor", "svg2test", "pvsg"])
    ap.add_argument("--n", type=json.loads, default={})
    ap.add_argument("--max_new_tokens", type=int, default=4096)
    ap.add_argument("--repetition_penalty", type=float, default=1.05, help="TRASER's generation_config")
    ap.add_argument("--dtype", default="bfloat16")
    ap.add_argument("--shard", type=int, default=0)
    ap.add_argument("--nshards", type=int, default=1)
    args = ap.parse_args()
    tag = f"[generate {args.name} {args.shard + 1}/{args.nshards}] "
    todo = []
    for ds in args.datasets:
        for v in IC.shard(IC.select_videos(ds, args.n.get(ds), 0, args.results), args.shard, args.nshards):
            if not Path(args.out, args.name, ds, "preds", f"{v}.json").exists() and F.load_layout(args.work, ds, v):
                todo.append((ds, v))
    F.log(f"{len(todo)} videos to answer", tag)
    if not todo:
        return 0
    import torch
    model, tok = F.load_lm(args.lm, args.dtype)
    model.eval()
    torch.set_grad_enabled(False)
    t_all = time.time()
    for i, (ds, v) in enumerate(todo, 1):
        t0 = time.time()
        try:
            x = F.load_embeds(args.work, ds, v, model.device, model.dtype)
            out = model.generate(inputs_embeds=x, attention_mask=torch.ones(x.shape[:2], dtype=torch.long, device=x.device),
                                 do_sample=False, max_new_tokens=args.max_new_tokens,
                                 repetition_penalty=args.repetition_penalty, eos_token_id=F.STOP_IDS,
                                 pad_token_id=F.STOP_IDS[1])
            text = tok.decode(out[0], skip_special_tokens=True)
            d = Path(args.out, args.name, ds, "preds")
            d.mkdir(parents=True, exist_ok=True)
            stats = IC.read_json(Path(args.results, ds, "preds", f"{v}.stats.json"), {})
            stats.update(engine="hf", model=args.name, new_tokens=int(out.shape[1]), generate_s=round(time.time() - t0, 1),
                         cut_off=int(out[0, -1]) not in F.STOP_IDS)
            IC.write_json(d / f"{v}.stats.json", stats)
            (d / f"{v}.json").write_text(text)
            F.log(f"{ds}/{v} ({i}/{len(todo)}): {out.shape[1]} tokens, {time.time() - t0:.0f} s"
                  f"{' (cut off)' if stats['cut_off'] else ''}", tag)
            del x, out
            torch.cuda.empty_cache()
        except Exception as e:  # noqa: BLE001
            F.log(f"{ds}/{v} FAILED: {type(e).__name__}: {str(e)[:300]}", tag)
    F.log(f"finished ({(time.time() - t_all) / 60:.0f} min)", tag)
    return 0


if __name__ == "__main__":
    sys.exit(main())
