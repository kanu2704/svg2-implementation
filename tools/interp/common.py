"""Shared pieces of the interpretability analysis: paths, which videos, the layout of TRASER's input sequence,
relations in an answer with their character positions, and the time mapping used by the label-swap test.

TRASER's language model reads one sequence (token_arrangement.py):

    system + user prompt ... | per object k:  <obj_traj_start> "Object k: " <|vision_start|>
                                                [OTR: 32 latents, the whole video]
                                                "<0 - 4 sec>" [TWR: 32 latents]  "<4 - 8 sec>" [TWR: 32 latents] ...
                                                (only the 4-second windows the object appears in)
                                              <|vision_end|> <obj_traj_end>
                             | ... <|im_end|> <|im_start|>assistant\\n   -> the answer (JSON) follows

`parse_layout` recovers every position's role from the arranged token ids (latent slots carry the video token
id, labels carry their text tokens), so the experiments can read or change exactly the OTR / TWR latents of one
object or one window, or the time labels.
"""
import json
import os
import random
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
RESULTS = REPO / "results" / "traser_bench"
OUT = RESULTS / "interp"                         # pushed to GitHub: per-video JSON, probe results, report
DATASETS = ["svg2test", "pvsg", "vidor"]
DEFAULT_N = {"svg2test": 40, "pvsg": 25, "vidor": 60}
WINDOW_S = 4                                     # TRASER's temporal window (seconds of its ~1 fps sample)

REL_RE = re.compile(r'\[\s*(-?\d+)\s*,\s*"((?:[^"\\]|\\.)*)"\s*,\s*(-?\d+)\s*,\s*(\[\s*(?:\[[^\[\]]*\]\s*,?\s*)*\])\s*\]')
NUM_RE = re.compile(r"-?\d+(?:\.\d+)?")


# ----------------------------------------------------------------------------- files
def write_json(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".part")
    tmp.write_text(json.dumps(obj))
    tmp.replace(path)


def read_json(path, default=None):
    path = Path(path)
    return json.load(open(path)) if path.exists() else default


def answered(dataset, results=RESULTS):
    d = Path(results, dataset, "preds")
    return sorted(p.name[:-len(".stats.json")] for p in d.glob("*.stats.json")
                  if (d / (p.name[:-len(".stats.json")] + ".json")).exists())


def select_videos(dataset, n=None, seed=0, results=RESULTS):
    """A fixed random sample of the videos TRASER answered (same sample on every machine and every run)."""
    vids = answered(dataset, results)
    base_n = DEFAULT_N.get(dataset, 50)
    n = base_n if n is None else n
    if n and n < len(vids):
        if n <= base_n:
            return sorted(random.Random(seed).sample(vids, n))
        # a bigger sample keeps the default one inside it, so the videos already done are reused
        base = select_videos(dataset, base_n, seed, results)
        rest = sorted(set(vids) - set(base))
        vids = sorted(base + random.Random(seed).sample(rest, n - len(base)))
    return vids


def shard(items, k, n):
    return [x for i, x in enumerate(items) if i % n == k]


def work_paths(work, dataset, video_id):
    """Big per-video files kept on the machine (not pushed): input sequence, layout, features."""
    d = Path(work) / dataset
    return {"embeds": d / f"{video_id}.embeds.pt", "layout": d / f"{video_id}.layout.json",
            "feats": d / f"{video_id}.feats.npz", "hidden": d / f"{video_id}.hidden.npz"}


def out_path(phase, dataset, video_id, out=OUT):
    return Path(out) / "raw" / phase / dataset / f"{video_id}.json"


# ----------------------------------------------------------------------------- layout of the input sequence
def parse_layout(ids, start_id, end_id, video_id, vs_id, ve_id, n_otr, n_twr, decode):
    """ids: arranged token ids [L] (list of ints). decode(list of ids) -> text (for the "<a - b sec>" labels).
    Returns {"L", "prefix_end", "suffix_start", "objects": [{"k", "block": [a, b], "label": [a, b],
    "otr": [a, b], "windows": [{"w", "text", "label": [a, b], "twr": [a, b]}]}]} (half-open ranges)."""
    L = len(ids)
    objects, i = [], 0
    while i < L:
        if ids[i] != start_id:
            i += 1
            continue
        a = i
        j = i + 1
        while ids[j] != vs_id:
            j += 1
        label = [i + 1, j]
        j += 1
        otr = [j, j + n_otr]
        assert all(ids[t] == video_id for t in range(*otr)), f"OTR slots expected at {otr}"
        j += n_otr
        windows = []
        while ids[j] != ve_id:
            t0 = j
            while ids[j] != video_id:
                j += 1
            text = decode(ids[t0:j])
            m = re.search(r"<\s*(\d+)\s*-\s*(\d+)\s*sec\s*>", text)
            assert m, f"window label expected, got {text!r}"
            twr = [j, j + n_twr]
            assert all(ids[t] == video_id for t in range(*twr)), f"TWR slots expected at {twr}"
            windows.append({"w": int(m.group(1)) // WINDOW_S, "text": text.strip(), "label": [t0, j], "twr": twr})
            j += n_twr
        assert ids[j + 1] == end_id, "<obj_traj_end> expected after <|vision_end|>"
        objects.append({"k": len(objects) + 1, "block": [a, j + 2], "label": label, "otr": otr, "windows": windows})
        i = j + 2
    return {"L": L, "prefix_end": objects[0]["block"][0] if objects else L,
            "suffix_start": objects[-1]["block"][1] if objects else L, "objects": objects}


def latent_positions(layout, k=None, kind="all", windows=None):
    """Positions of the visual latents: of object k (None = all objects), kind "otr" / "twr" / "all",
    only the given window indices (TWR)."""
    pos = []
    for o in layout["objects"]:
        if k is not None and o["k"] != k:
            continue
        if kind in ("otr", "all"):
            pos += list(range(*o["otr"]))
        if kind in ("twr", "all"):
            for w in o["windows"]:
                if windows is None or w["w"] in windows:
                    pos += list(range(*w["twr"]))
    return pos


def label_positions(layout):
    return [p for o in layout["objects"] for w in o["windows"] for p in range(*w["label"])]


# ----------------------------------------------------------------------------- relations in an answer
def answer_relations(text):
    """Relations of an answer with the character ranges of their parts:
    [{"s", "pred", "o", "spans": [[a, b], ...], "range", "s_range", "pred_range", "o_range", "time_ranges"}]."""
    out = []
    start = text.find('"relationships"')
    if start < 0:
        return out
    for m in REL_RE.finditer(text, start):
        nums = [(n.start() + m.start(4), n.end() + m.start(4), float(n.group())) for n in NUM_RE.finditer(m.group(4))]
        spans = [[nums[i][2], nums[i + 1][2]] for i in range(0, len(nums) - 1, 2)]
        out.append({"s": int(m.group(1)), "pred": m.group(2), "o": int(m.group(3)), "spans": spans,
                    "range": [m.start(), m.end()], "s_range": [m.start(1), m.end(1)],
                    "pred_range": [m.start(2), m.end(2)], "o_range": [m.start(3), m.end(3)],
                    "spans_range": [m.start(4), m.end(4)], "time_ranges": [[a, b] for a, b, _ in nums]})
    return out


def list_end(text):
    """Character index of the "]" that closes the relationships list (None if the answer was cut off)."""
    rels = answer_relations(text)
    i = text.find('"relationships"')
    if i < 0:
        return None
    j = text.find("[", i)
    pos = rels[-1]["range"][1] if rels else j + 1
    rest = text[pos:]
    m = re.match(r"\s*\]", rest)
    return pos + m.end() - 1 if m else None


def tokens_in(offsets, a, b):
    """Token indices whose character offsets overlap [a, b)."""
    return [i for i, (s, e) in enumerate(offsets) if s < b and e > a and e > s]


# ----------------------------------------------------------------------------- label swap (time test)
def reversed_window_map(n_windows):
    """Window w gets the label of window n-1-w."""
    return {w: n_windows - 1 - w for w in range(n_windows)}


def map_time(t, n_windows):
    """Where a time point lands if the labels are reversed: same offset inside the window, mirrored window."""
    w = min(int(t // WINDOW_S), n_windows - 1)
    return (n_windows - 1 - w) * WINDOW_S + (t - w * WINDOW_S)


def fmt_spans(spans):
    num = lambda v: str(int(v)) if float(v).is_integer() else str(v)  # noqa: E731
    return "[" + ", ".join(f"[{num(a)}, {num(b)}]" for a, b in spans) + "]"


def mapped_answer(text, n_windows):
    """The answer with every relation's time spans moved to where reversed labels would put them."""
    pieces, last = [], 0
    for r in answer_relations(text):
        new = []
        for a, b in r["spans"]:
            x, y = map_time(a, n_windows), map_time(b, n_windows)
            new.append([min(x, y), max(x, y)])
        a, b = r["spans_range"]
        pieces += [text[last:a], fmt_spans(new)]
        last = b
    pieces.append(text[last:])
    return "".join(pieces)


def env_info():
    import torch
    return {"gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu",
            "torch": torch.__version__, "pid": os.getpid()}
