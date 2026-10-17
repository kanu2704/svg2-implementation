"""GRPO (group relative policy optimisation): let the model try, score the tries, and favour the better ones.

For every training video: the model writes G answers (sampling), each answer gets a reward from the human
labels (common.reward: triplet F1 + 0.5 x pair F1, so it pays to write the right pairs, with the right word and
time, and not to list every pair), and each answer's advantage is its reward minus the group's mean, divided by
the group's std. Loss = - advantage x mean log-probability of the answer's tokens + beta x KL to the starting
model (k3 estimator per token). One update per group, so the PPO ratio is 1 and needs no clipping.
Only LoRA weights are trained (on top of --lm, by default the SFT model); "the starting model" is the same
network with LoRA switched off, so no second copy is kept. At the end LoRA is folded in and saved.

    CUDA_VISIBLE_DEVICES=0 python3 tools/finetune/grpo.py --lm $BIG/ft_sft --work $BIG/finetune_work \
        --bench $BIG/finetune_bench --dataset pvsg --videos_file train.txt --out $BIG/ft_grpo
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


def cut(ids):
    """Generated ids up to the first stop token; ended = a stop token was written."""
    for i, t in enumerate(ids):
        if t in F.STOP_IDS:
            return ids[:i + 1], True
    return ids, False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lm", required=True, help="starting model: the SFT model, or TRASER's exported language model")
    ap.add_argument("--work", required=True)
    ap.add_argument("--bench", required=True)
    ap.add_argument("--dataset", default="pvsg")
    ap.add_argument("--videos_file", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--log", default=str(F.OUT / "logs" / "grpo.jsonl"))
    ap.add_argument("--videos", type=int, default=150, help="training videos used (one group each per epoch)")
    ap.add_argument("--epochs", type=int, default=1)
    ap.add_argument("--group", type=int, default=4, help="G: answers written per video")
    ap.add_argument("--max_new_tokens", type=int, default=1536)
    ap.add_argument("--temperature", type=float, default=1.0)
    ap.add_argument("--lr", type=float, default=2e-5)
    ap.add_argument("--beta", type=float, default=0.04, help="KL weight (0 = no KL, faster)")
    ap.add_argument("--accum", type=int, default=2, help="videos per optimizer step")
    ap.add_argument("--lora_r", type=int, default=16)
    ap.add_argument("--max_len", type=int, default=40000)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    import torch
    torch.manual_seed(args.seed)
    rng = random.Random(args.seed)
    model, tok = F.load_lm(args.lm, train=True)
    match = F.WordMatch()
    vids = []
    for v in Path(args.videos_file).read_text().split():
        lay = F.load_layout(args.work, args.dataset, v)
        if lay is None or lay["L"] + args.max_new_tokens > args.max_len:
            continue
        gold = F.given_relations(B.load_gt(args.bench, args.dataset, v), lay)
        if gold:
            vids.append((v, gold))
    rng.shuffle(vids)
    vids = vids[:args.videos]
    F.log(f"{len(vids)} training videos, {args.group} answers each, up to {args.max_new_tokens} tokens")
    model = F.add_lora(model, r=args.lora_r)
    params = [p for p in model.parameters() if p.requires_grad]
    opt = torch.optim.AdamW(params, lr=args.lr, weight_decay=0.0)
    emb = model.get_input_embeddings()
    Path(args.log).parent.mkdir(parents=True, exist_ok=True)
    logf = open(args.log, "w")
    t0, step, n_done = time.time(), 0, 0
    for epoch in range(args.epochs):
        for i, (v, gold) in enumerate(vids, 1):
            x0 = F.load_embeds(args.work, args.dataset, v, model.device, torch.bfloat16)
            # 1) write G answers (no gradients; dropout off)
            model.eval()
            model.config.use_cache = True
            with torch.no_grad():
                gen = model.generate(inputs_embeds=x0, attention_mask=torch.ones(x0.shape[:2], dtype=torch.long, device=x0.device),
                                     do_sample=True, temperature=args.temperature, top_p=1.0, top_k=0,
                                     max_new_tokens=args.max_new_tokens, num_return_sequences=args.group,
                                     eos_token_id=F.STOP_IDS, pad_token_id=F.STOP_IDS[1])
            model.config.use_cache = False
            model.train()
            answers = [cut(row.tolist()) for row in gen.cpu()]
            del gen
            # 2) rewards and advantages
            texts = [tok.decode(ids, skip_special_tokens=True) for ids, _ in answers]
            scored = [F.reward(t, gold, match, ended) for t, (_, ended) in zip(texts, answers)]
            r = torch.tensor([s[0] for s in scored])
            adv = (r - r.mean()) / (r.std() + 1e-4) if len(r) > 1 else r * 0
            # 3) policy-gradient step on every answer with a non-zero advantage
            kl_sum, n_tok = 0.0, 0
            for (ids, _), a in zip(answers, adv.tolist()):
                if abs(a) < 1e-6 or not ids:
                    continue
                t = torch.tensor(ids, device=model.device)
                x = torch.cat([x0, emb(t[None]).to(torch.bfloat16)], 1)[:, :-1]
                L0 = x0.shape[1] - 1
                lp = F.token_logprobs(model, F.hidden(model, x)[L0:], t)
                loss = -a * lp.mean()
                if args.beta > 0:
                    with torch.no_grad(), model.disable_adapter():
                        ref = F.token_logprobs(model, F.hidden(model, x)[L0:], t)
                    d = ref - lp
                    kl = (torch.exp(d) - d - 1).mean()
                    loss = loss + args.beta * kl
                    kl_sum += kl.item() * len(ids)
                    n_tok += len(ids)
                (loss / (args.group * args.accum)).backward()
                del x, lp, loss
                torch.cuda.empty_cache()
            n_done += 1
            if n_done % args.accum == 0 or i == len(vids):
                torch.nn.utils.clip_grad_norm_(params, 1.0)
                opt.step()
                opt.zero_grad(set_to_none=True)
                step += 1
            rec = {"epoch": epoch + 1, "video": v, "i": i, "step": step, "reward_mean": round(float(r.mean()), 4),
                   "reward_max": round(float(r.max()), 4), "reward_std": round(float(r.std()), 4) if len(r) > 1 else 0,
                   "triplet_recall": round(sum(s[1].get("triplet_recall", 0) for s in scored) / len(scored), 4),
                   "pair_recall": round(sum(s[1].get("pair_recall", 0) for s in scored) / len(scored), 4),
                   "ended": sum(e for _, e in answers), "tokens": [len(ids) for ids, _ in answers],
                   "kl": round(kl_sum / n_tok, 5) if n_tok else None, "minutes": round((time.time() - t0) / 60, 1)}
            logf.write(json.dumps(rec) + "\n")
            logf.flush()
            F.log(f"video {i}/{len(vids)} {v}: reward {rec['reward_mean']} (max {rec['reward_max']}), "
                  f"{rec['ended']}/{args.group} answers closed, {rec['minutes']} min")
            del x0
            torch.cuda.empty_cache()
    F.log("folding LoRA into the model and saving ...")
    F.merge_and_save(model, tok, args.lm, args.out)
    json.dump({"method": "grpo", "videos": [v for v, _ in vids], "args": vars(args)},
              open(Path(args.out) / "FINETUNE.json", "w"), indent=1)
    F.log(f"saved {args.out} ({(time.time() - t0) / 60:.0f} min)")


if __name__ == "__main__":
    sys.exit(main())
