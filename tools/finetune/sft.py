"""SFT (supervised fine-tuning): teach TRASER's language model to write the human answer.

For every training video: input = the saved sequence TRASER's language model reads (video + objects, from
tools/interp/encode_stage.py), target = the human relations in TRASER's answer format (common.target_text).
Loss = cross-entropy on the target tokens only (the model copies the human answer token by token). Only LoRA
weights are trained; the vision part is frozen (its output is the saved sequence). At the end the LoRA weights
are folded into the model, which is saved as a plain Qwen2 folder for generate.py and grpo.py.

    CUDA_VISIBLE_DEVICES=0 python3 tools/finetune/sft.py --lm $BIG/traser_lm --work $BIG/finetune_work \
        --bench $BIG/finetune_bench --dataset pvsg --videos_file train.txt --out $BIG/ft_sft
"""
import argparse
import json
import random
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent))
import bench_data as B  # noqa: E402
from finetune import common as F  # noqa: E402


def examples(args, tok):
    out, skipped = [], {}
    for v in Path(args.videos_file).read_text().split():
        lay = F.load_layout(args.work, args.dataset, v)
        if lay is None:
            skipped["not encoded"] = skipped.get("not encoded", 0) + 1
            continue
        gt = B.load_gt(args.bench, args.dataset, v)
        text = F.target_text(gt, lay) + F.END_TEXT
        ids = tok(text, add_special_tokens=False)["input_ids"]
        if not F.given_relations(gt, lay):
            skipped["no human relation"] = skipped.get("no human relation", 0) + 1
            continue
        if lay["L"] + len(ids) > args.max_len:
            skipped["too long"] = skipped.get("too long", 0) + 1
            continue
        out.append({"video": v, "ids": ids, "L": lay["L"]})
    return out, skipped


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lm", required=True, help="TRASER's language model (tools/export_lm.py)")
    ap.add_argument("--work", required=True, help="encode_stage output of the training videos")
    ap.add_argument("--bench", required=True, help="prepared training videos (gt.json)")
    ap.add_argument("--dataset", default="pvsg")
    ap.add_argument("--videos_file", required=True)
    ap.add_argument("--out", required=True, help="folder for the fine-tuned model")
    ap.add_argument("--log", default=str(F.OUT / "logs" / "sft.jsonl"))
    ap.add_argument("--epochs", type=int, default=2)
    ap.add_argument("--lr", type=float, default=1e-4)
    ap.add_argument("--accum", type=int, default=8, help="videos per optimizer step")
    ap.add_argument("--lora_r", type=int, default=16)
    ap.add_argument("--max_len", type=int, default=40000, help="skip videos with a longer input + answer")
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    import torch
    torch.manual_seed(args.seed)
    model, tok = F.load_lm(args.lm, train=True)
    data, skipped = examples(args, tok)
    F.log(f"{len(data)} training videos (skipped: {skipped}); answer tokens: "
          f"{sum(len(d['ids']) for d in data) / max(1, len(data)):.0f} on average")
    if not data:
        raise SystemExit("no training videos")
    model = F.add_lora(model, r=args.lora_r)
    model.print_trainable_parameters()
    params = [p for p in model.parameters() if p.requires_grad]
    opt = torch.optim.AdamW(params, lr=args.lr, weight_decay=0.0)
    total = args.epochs * len(data) // args.accum + 1
    sched = torch.optim.lr_scheduler.LambdaLR(opt, lambda s: min(1.0, (s + 1) / 10) * max(0.0, 1 - s / total))
    Path(args.log).parent.mkdir(parents=True, exist_ok=True)
    logf = open(args.log, "w")
    emb = model.get_input_embeddings()
    step, t0, rng = 0, time.time(), random.Random(args.seed)
    for epoch in range(args.epochs):
        order = data[:]
        rng.shuffle(order)
        run_loss, run_n = 0.0, 0
        for i, d in enumerate(order, 1):
            x0 = F.load_embeds(args.work, args.dataset, d["video"], model.device, torch.bfloat16)
            ids = torch.tensor(d["ids"], device=model.device)
            x = torch.cat([x0, emb(ids[None]).to(torch.bfloat16)], 1)
            h = F.hidden(model, x[:, :-1])[x0.shape[1] - 1:]       # rows that predict the answer tokens
            loss = -F.token_logprobs(model, h, ids).mean()
            (loss / args.accum).backward()
            run_loss += float(loss)
            run_n += 1
            if i % args.accum == 0 or i == len(order):
                torch.nn.utils.clip_grad_norm_(params, 1.0)
                opt.step()
                sched.step()
                opt.zero_grad(set_to_none=True)
                step += 1
                rec = {"epoch": epoch + 1, "step": step, "videos": i, "loss": round(run_loss / run_n, 4),
                       "lr": sched.get_last_lr()[0], "minutes": round((time.time() - t0) / 60, 1)}
                logf.write(json.dumps(rec) + "\n")
                logf.flush()
                F.log(f"epoch {epoch + 1} step {step}: loss {rec['loss']} ({i}/{len(order)} videos, {rec['minutes']} min)")
                run_loss, run_n = 0.0, 0
            del x0, x, h, loss
            torch.cuda.empty_cache()
    F.log("folding LoRA into the model and saving ...")
    F.merge_and_save(model, tok, args.lm, args.out)
    json.dump({"method": "sft", "videos": [d["video"] for d in data], "args": vars(args)},
              open(Path(args.out) / "FINETUNE.json", "w"), indent=1)
    F.log(f"saved {args.out} ({(time.time() - t0) / 60:.0f} min)")


if __name__ == "__main__":
    sys.exit(main())
