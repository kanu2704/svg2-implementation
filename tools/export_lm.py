"""Export the language model of the released TRASER checkpoint as a plain Qwen2 text model, for vLLM.

Nothing is retrained or changed: the weights are copied from the checkpoint as they are (and checked to be
identical afterwards). Only the names change, plus a Qwen2 config, so vLLM can load them.

Why this is the same model: TRASER = vision encoder + two resamplers (they build the input sequence) +
the Qwen2.5-VL language model (it writes the answer). TRASER gives that language model plain positions
0..L-1, the same number on all three rows of Qwen2.5-VL's 3-D rotary positions (token_arrangement.py). With
equal rows, the 3-D ("mrope") rotation is exactly the ordinary 1-D one, so the language model is an
ordinary Qwen2 decoder over the arranged embeddings. The vision encoder and resamplers stay in PyTorch
(tools/bench_run.py --mode encode); vLLM only writes the answers (tools/vllm_generate.py).

    python3 tools/export_lm.py --model <TRASER folder or UWGZQ/TRASER> --out /tmp/traser_lm
"""
import argparse
import json
import os
import shutil
import sys
import time
from pathlib import Path

DEFAULT_MODEL = "UWGZQ/TRASER"
TOKENIZER_FILES = ["tokenizer_config.json", "vocab.json", "merges.txt", "added_tokens.json",
                   "special_tokens_map.json", "tokenizer.json", "chat_template.jinja", "chat_template.json",
                   "generation_config.json"]
TEXT_KEYS = ["vocab_size", "hidden_size", "intermediate_size", "num_hidden_layers", "num_attention_heads",
             "num_key_value_heads", "hidden_act", "max_position_embeddings", "rms_norm_eps", "rope_theta",
             "attention_dropout", "bos_token_id", "eos_token_id", "max_window_layers", "initializer_range"]
LAYER_TENSORS = ["input_layernorm.weight", "post_attention_layernorm.weight",
                 "self_attn.q_proj.weight", "self_attn.q_proj.bias", "self_attn.k_proj.weight",
                 "self_attn.k_proj.bias", "self_attn.v_proj.weight", "self_attn.v_proj.bias",
                 "self_attn.o_proj.weight", "mlp.gate_proj.weight", "mlp.up_proj.weight", "mlp.down_proj.weight"]


def log(msg):
    print(f"{time.strftime('%H:%M:%S')} {msg}", flush=True)


def lm_key(key):
    """Checkpoint name -> Qwen2ForCausalLM name; None for the vision encoder and the resamplers.
    Handles the layouts transformers has used for Qwen2.5-VL checkpoints."""
    for prefix, new in (("model.language_model.", "model."), ("language_model.model.", "model."),
                        ("language_model.lm_head.", "lm_head."), ("language_model.", "model.")):
        if key.startswith(prefix):
            return new + key[len(prefix):]
    if key.startswith("lm_head."):
        return key
    if key.startswith("model.") and key.split(".")[1] in ("layers", "embed_tokens", "norm"):
        return key
    return None


def text_config(cfg, tie):
    """Qwen2ForCausalLM config from TRASER's Qwen2.5-VL config (text settings at the top level or in
    text_config). rope_scaling (the 3-D "mrope" split) is dropped on purpose, see the module docstring."""
    t = {k: v for k, v in cfg.items() if not isinstance(v, dict)}
    t.update(cfg.get("text_config") or {})
    out = {"architectures": ["Qwen2ForCausalLM"], "model_type": "qwen2"}
    out.update({k: t[k] for k in TEXT_KEYS if k in t})
    out.update(use_sliding_window=False, sliding_window=None, tie_word_embeddings=tie, use_cache=True,
               torch_dtype=t.get("torch_dtype") or "bfloat16")
    missing = [k for k in TEXT_KEYS[:10] if k not in out]
    if missing:
        raise ValueError(f"TRASER config has no {missing}")
    return out


def resolve(model):
    if os.path.isdir(model):
        return Path(model)
    from huggingface_hub import snapshot_download
    return Path(snapshot_download(model, allow_patterns=["*.json", "*.safetensors", "*.txt", "*.jinja"]))


def shards(src):
    index = src / "model.safetensors.index.json"
    if index.exists():
        weight_map = json.load(open(index))["weight_map"]
    else:
        from safetensors import safe_open
        with safe_open(str(src / "model.safetensors"), framework="pt") as f:
            weight_map = {k: "model.safetensors" for k in f.keys()}
    by_file = {}
    for k, f in weight_map.items():
        by_file.setdefault(f, []).append(k)
    return weight_map, by_file


def export(model=DEFAULT_MODEL, out="/tmp/traser_lm"):
    import torch
    from safetensors import safe_open
    from safetensors.torch import save_file
    src, out = resolve(model), Path(out)
    out.mkdir(parents=True, exist_ok=True)
    cfg = json.load(open(src / "config.json"))
    weight_map, by_file = shards(src)
    mapped = {k: lm_key(k) for k in weight_map}
    kept = {k: v for k, v in mapped.items() if v is not None}
    skipped = sorted({k.split(".")[0] + "." + k.split(".")[1] if "." in k else k for k, v in mapped.items() if v is None})
    log(f"checkpoint {src}: {len(weight_map)} tensors, {len(kept)} belong to the language model "
        f"(left out: {', '.join(skipped)})")

    n_layers = int({**cfg, **(cfg.get("text_config") or {})}["num_hidden_layers"])
    need = {"model.embed_tokens.weight", "model.norm.weight"} | {
        f"model.layers.{i}.{t}" for i in range(n_layers) for t in LAYER_TENSORS}
    have = set(kept.values())
    if need - have:
        raise ValueError(f"language-model tensors missing after renaming: {sorted(need - have)[:8]} ... "
                         f"(checkpoint names look like: {sorted(weight_map)[:6]})")
    extra = have - need - {"lm_head.weight"}
    if extra:
        raise ValueError(f"unexpected language-model tensors: {sorted(extra)[:8]}")

    def tensor(key):
        with safe_open(str(src / weight_map[key]), framework="pt") as f:
            return f.get_tensor(key)

    inv = {v: k for k, v in kept.items()}
    tie = "lm_head.weight" not in have
    if not tie:
        tie = torch.equal(tensor(inv["lm_head.weight"]), tensor(inv["model.embed_tokens.weight"]))
    log(f"output layer {'shares the input embedding (tied)' if tie else 'is its own matrix'}")

    new_map = {}
    for i, (fname, keys) in enumerate(sorted(by_file.items()), 1):
        part = {}
        with safe_open(str(src / fname), framework="pt") as f:
            for k in keys:
                new = kept.get(k)
                if new is None or (tie and new == "lm_head.weight"):
                    continue
                part[new] = f.get_tensor(k).contiguous()
        if not part:
            continue
        name = f"model-{i:05d}-of-{len(by_file):05d}.safetensors"
        save_file(part, str(out / name), metadata={"format": "pt"})
        new_map.update({k: name for k in part})
        log(f"  wrote {name}: {len(part)} tensors")
        del part
    total = sum(os.path.getsize(out / f) for f in set(new_map.values()))
    json.dump({"metadata": {"total_size": total}, "weight_map": new_map}, open(out / "model.safetensors.index.json", "w"), indent=1)
    json.dump(text_config(cfg, tie), open(out / "config.json", "w"), indent=1)
    copied = []
    for name in TOKENIZER_FILES:
        if (src / name).exists():
            shutil.copyfile(src / name, out / name)
            copied.append(name)

    # check: every exported tensor is bit-identical to the checkpoint's
    same = 0
    for name in sorted(set(new_map.values())):
        with safe_open(str(out / name), framework="pt") as f:
            for k in f.keys():
                if not torch.equal(f.get_tensor(k), tensor(inv[k])):
                    raise RuntimeError(f"exported {k} differs from the checkpoint's {inv[k]}")
                same += 1
    info = {"source": str(src), "tensors": same, "tied_output_layer": tie, "dtype": cfg.get("torch_dtype"),
            "dropped_config": [k for k in ("rope_scaling",) if k in cfg or k in (cfg.get("text_config") or {})],
            "copied": copied, "gb": round(total / 2**30, 2)}
    json.dump(info, open(out / "EXPORT.json", "w"), indent=1)
    log(f"exported to {out}: {same} tensors, all identical to the checkpoint ✓ ({info['gb']} GB; tokenizer files: "
        f"{', '.join(copied)})")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=DEFAULT_MODEL, help="TRASER checkpoint: local folder or Hub id")
    ap.add_argument("--out", default="/tmp/traser_lm")
    args = ap.parse_args()
    export(args.model, args.out)


if __name__ == "__main__":
    sys.exit(main())
