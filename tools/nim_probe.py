"""Probe NVIDIA NIM models for SVG2 stages 5 (text -> JSON) and 6 (several video frames in one request).

    python3 tools/nim_probe.py            # asks for the NVIDIA key in a hidden prompt (or reads $NVIDIA_API_KEY)

Uses the real stage-5 prompt (their build_structure_prompt) on DAM's real descriptions from
data/stage4/, and real frames of sav_000001.mp4. Writes notes/stage56/nim_probe.md and
notes/stage56/nim_models.txt. The key is never printed or written anywhere.
"""
import base64
import getpass
import json
import os
import re
import sys
import time

import cv2

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "third_party/SVG2/pipeline"))
import svg2_pipeline as P  # noqa: E402
from openai import OpenAI  # noqa: E402

DESC = os.path.join(REPO, "data/stage4/sav_000001_first120_descriptions.json")
VIDEO = os.path.join(REPO, "third_party/SVG2/pipeline/examples/sav_000001.mp4")
OUT = os.path.join(REPO, "notes/stage56")
THINK_ON = {"chat_template_kwargs": {"enable_thinking": True}}
THINK_OFF = {"chat_template_kwargs": {"enable_thinking": False}}

# (label, model id, extra request settings)
TEXT_MODELS = [
    ("lightning-30b thinking ON (NVIDIA's example settings)", "nvidia/nemotron-3.5-lightning-30b-a3b",
     dict(temperature=1.0, top_p=0.95, extra_body=THINK_ON)),
    ("lightning-30b thinking OFF, temp 0.6", "nvidia/nemotron-3.5-lightning-30b-a3b",
     dict(temperature=0.6, top_p=0.95, extra_body=THINK_OFF)),
    ("nemotron-3-super-120b", "nvidia/nemotron-3-super-120b-a12b", dict(temperature=0.6, top_p=0.95)),
    ("nemotron-3-ultra-550b", "nvidia/nemotron-3-ultra-550b-a55b", dict(temperature=0.6, top_p=0.95)),
    ("kimi-k3", "moonshotai/kimi-k3", dict(temperature=0.6)),
]
VISION_MODELS = [
    "meta/llama-3.2-90b-vision-instruct",
    "google/gemma-4-31b-it",
    "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning",
    "moonshotai/kimi-k3",
    "google/gemma-3-12b-it",
    "microsoft/phi-3-vision-128k-instruct",
]


def extract_json(text):
    """Reasoning models may wrap the JSON in thoughts or ```json fences: take the first {...} block that parses."""
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


def call(client, model, messages, settings, response_format=None, max_tokens=4096):
    kw = dict(model=model, messages=messages, max_tokens=max_tokens, **settings)
    if response_format:
        kw["response_format"] = response_format
    t0 = time.time()
    r = client.chat.completions.create(**kw)
    msg = r.choices[0].message
    return (msg.content or ""), (getattr(msg, "reasoning_content", None) or ""), time.time() - t0


def frame_url(frame_rgb, width=336):
    h, w = frame_rgb.shape[:2]
    small = cv2.resize(frame_rgb, (width, int(h * width / w)))
    ok, buf = cv2.imencode(".jpg", cv2.cvtColor(small, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, 80])
    return "data:image/jpeg;base64," + base64.b64encode(buf.tobytes()).decode()


def main():
    key = os.environ.get("NVIDIA_API_KEY") or getpass.getpass("NVIDIA key (hidden): ")
    client = OpenAI(base_url="https://integrate.api.nvidia.com/v1", api_key=key, timeout=180)
    os.makedirs(OUT, exist_ok=True)
    R = ["# NIM probe for stages 5–6", ""]

    ids = sorted(m.id for m in client.models.list().data)
    open(os.path.join(OUT, "nim_models.txt"), "w").write("\n".join(ids) + "\n")
    print(f"{len(ids)} models → notes/stage56/nim_models.txt")
    R += [f"{len(ids)} models available to this key (full list: `nim_models.txt`).", ""]

    # ---------------- stage 5: real prompt, real DAM descriptions ----------------
    desc = {d["object_id"]: d["description"] for d in json.load(open(DESC))["objects"]}
    R += ["## Stage 5: paragraph → JSON (their prompt, DAM's real paragraphs)", "",
          "id 1 = the boy; id 0 = the floor, which DAM described as a person (P44).", ""]
    schema_fmt = {"type": "json_schema", "json_schema": {"name": "scene_graph", "schema": P.SCENE_GRAPH_SCHEMA, "strict": True}}
    for label, model, settings in TEXT_MODELS:
        if model not in ids:
            R += [f"### {label}: `{model}` not available to this key", ""]
            continue
        for oid in (1, 0):
            messages = [{"role": "system", "content": P.STRUCTURE_SYSTEM_PROMPT},
                        {"role": "user", "content": P.build_structure_prompt(desc[oid])}]
            result, mode, err = None, None, None
            for fmt_name, fmt in (("strict json_schema", schema_fmt), ("json_object", {"type": "json_object"}), ("plain text", None)):
                try:
                    content, reasoning, dt = call(client, model, messages, settings, fmt)
                    parsed = extract_json(content)
                    if parsed is not None:
                        result, mode = (parsed, content, reasoning, dt), fmt_name
                        break
                    err = f"{fmt_name}: no JSON in reply: {content[:200]!r}"
                except Exception as e:  # noqa: BLE001
                    err = f"{fmt_name}: {type(e).__name__}: {str(e)[:200]}"
            line = f"### {label}, object {oid}"
            if result:
                parsed, content, reasoning, dt = result
                rec = P._validate_scene_graph(parsed)
                R += [line, "", f"OK via **{mode}** in {dt:.1f} s" + (f"; reasoning {len(reasoning)} chars" if reasoning else ""),
                      "", "```json", json.dumps(rec, indent=1), "```", ""]
                print(f"[text] {label} | obj {oid}: OK ({mode}, {dt:.1f}s) → object = {rec['Object']!r}")
            else:
                R += [line, "", f"FAILED: {err}", ""]
                print(f"[text] {label} | obj {oid}: FAILED {err}")

    # ---------------- stage 6 feasibility: several frames in ONE request ----------------
    frames, _, _, _ = P.read_video_frames(VIDEO)
    picks = [0, 24, 48, 72, 96]
    urls = [frame_url(frames[f]) for f in picks]
    R += ["## Stage 6 feasibility: can the model read 5 frames in one request?", "",
          f"Frames {picks} of sav_000001 (336 px wide JPEG). Question: how many images, plus one sentence each.", ""]
    q = ("You are given {n} images (video frames in order). First line: 'N = <number of images you received>'. "
         "Then one short sentence per image describing it.")
    for model in VISION_MODELS:
        if model not in ids:
            R += [f"### `{model}`: not available", ""]
            continue
        for n in (1, 5):
            content = []
            for u in urls[:n]:
                content.append({"type": "image_url", "image_url": {"url": u}})
            content.append({"type": "text", "text": q.format(n=n)})
            try:
                text, reasoning, dt = call(client, model, [{"role": "user", "content": content}],
                                           dict(temperature=0.2), max_tokens=1024)
                R += [f"### `{model}`, {n} image(s): {dt:.1f} s", "", "```", text.strip()[:1200], "```", ""]
                print(f"[vision] {model} | {n} img: OK ({dt:.1f}s) {text.strip()[:90]!r}")
            except Exception as e:  # noqa: BLE001
                R += [f"### `{model}`, {n} image(s): FAILED", "", f"`{type(e).__name__}: {str(e)[:300]}`", ""]
                print(f"[vision] {model} | {n} img: FAILED {type(e).__name__}: {str(e)[:150]}")

    open(os.path.join(OUT, "nim_probe.md"), "w").write("\n".join(R) + "\n")
    print("\nwrote notes/stage56/nim_probe.md")


if __name__ == "__main__":
    main()
