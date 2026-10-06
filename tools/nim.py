"""Minimal NVIDIA NIM (OpenAI-compatible) client for the judge: no pipeline imports, so the scoring runs
anywhere (Kaggle CPU session, a laptop). The key comes from $NVIDIA_API_KEY or /root/.svg2_keys."""
import json
import logging
import os
import re
import time

log = logging.getLogger("nim")
NIM_URL = "https://integrate.api.nvidia.com/v1"


def nim_client(timeout=180):
    from openai import OpenAI
    for keys in ("/root/.svg2_keys", os.path.expanduser("~/.svg2_keys")):
        if not os.environ.get("NVIDIA_API_KEY") and os.path.exists(keys):
            for line in open(keys):
                k, _, v = line.strip().partition("=")
                if k and v:
                    os.environ.setdefault(k, v)
    if not os.environ.get("NVIDIA_API_KEY"):
        raise SystemExit("NVIDIA_API_KEY not set (environment, /root/.svg2_keys or ~/.svg2_keys)")
    return OpenAI(base_url=NIM_URL, api_key=os.environ["NVIDIA_API_KEY"], timeout=timeout)


def extract_json(text):
    """Some models wrap the JSON in thoughts or ``` fences: take the first {...} that parses."""
    if not text:
        return None
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.S)
    for m in re.finditer(r"\{", text):
        depth = 0
        for j in range(m.start(), len(text)):
            depth += {"{": 1, "}": -1}.get(text[j], 0)
            if depth == 0:
                try:
                    return json.loads(text[m.start():j + 1])
                except json.JSONDecodeError:
                    break
    return None


def ask(client, model, messages, settings, max_tokens=4096, tries=2):
    """JSON mode, then plain text; returns the parsed JSON or raises RuntimeError."""
    last = None
    for attempt in range(tries):
        for name, fmt in (("json_object", {"type": "json_object"}), ("plain", None)):
            kw = dict(model=model, messages=messages, max_tokens=max_tokens, **settings)
            if fmt:
                kw["response_format"] = fmt
            t0 = time.time()
            try:
                resp = client.chat.completions.create(**kw)
                if not getattr(resp, "choices", None):
                    raise RuntimeError(f"empty reply from the server: {str(resp)[:300]}")
                parsed = extract_json(resp.choices[0].message.content or "")
                if parsed is not None:
                    return parsed
                last = f"{name}: no JSON in reply"
            except Exception as e:  # noqa: BLE001
                last = f"{name}: {type(e).__name__}: {str(e)[:200]}"
            log.warning("%s attempt %d (%s) failed after %.0f s: %s", model, attempt + 1, name, time.time() - t0, last)
    raise RuntimeError(last)
