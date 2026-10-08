"""Score TRASER's predictions like Table 2 of the SVG2 paper: object accuracy, relation recall and
triplet recall, lenient semantic criterion, temporal IoU > 0.5.

What the paper says (Sec. 5, "Evaluation Setup") and how it is done here:
  - Models get the human object trajectories, so TRASER's "object k" IS a human object (via the mask
    column it was given, ``stats["mask_columns"][k - 1]``). No object matching is needed.
  - An LLM judge puts each (human label, predicted label) pair into one of five categories:
    identical, synonym, hypernym/hyponym, semantic overlap, mismatch. Lenient = anything but mismatch.
    The paper's judge is GPT-4o-mini with an unreleased prompt; ours is Kimi K3 (NVIDIA NIM) with the
    prompt below, written from the paper's description. Strict = the same text after normalising
    (lower case, "_" -> " ", "(uncertain)" removed).
  - Object accuracy: a human object is right if the label TRASER gave it is not a mismatch.
  - Relation recall: a human relation is right if TRASER has a relation between the same two objects,
    in the same direction, whose predicate is not a mismatch and whose time spans overlap the human
    ones with temporal IoU > threshold (paper: "interval IoU > threshold"; spans as unions of intervals;
    IoU of total lengths).
  - Triplet recall: the relation is right AND both objects' labels are right (the camera, id -1,
    counts as right).
  - Not stated in the paper, our choice (reported): pooled over all human objects/relations of a
    dataset ("micro"); the per-video average ("macro") is reported next to it.

Time units: TRASER answers in indices of its ~1 fps sampled frames ("seconds"); [a, b] inclusive
becomes [a, b + 1). For PVSG and VidOR (human spans in seconds) this is scaled by the real seconds per
sampled frame (duration / sampled frames; 1.0 for videos up to 128 s). SVG2test's human spans are in
the same index unit, so no scaling there.

    python tools/bench_eval.py                 # all datasets with predictions; writes results/traser_bench/README.md
    python tools/bench_eval.py --compare       # <dataset>/COMPARE.md: human labels vs TRASER, video by video
"""
import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))
RESULTS = REPO / "results" / "traser_bench"
DATASETS = ["pvsg", "vidor", "svg2test"]
PAPER = {  # Table 2, TRASER row (lenient, tIoU 0.5)
    "triplet": {"pvsg": 16.1, "vidor": 22.9, "svg2test": 16.7},
    "relation": {"pvsg": 16.9, "vidor": 25.0, "svg2test": 18.7},
    "object": {"pvsg": 72.7, "vidor": 91.4, "svg2test": 79.0},
}
SPLIT_SIZE = {"pvsg": 62, "vidor": 835, "svg2test": 100}
CATEGORIES = ["identical", "synonym", "hypernym/hyponym", "semantic overlap", "mismatch"]

JUDGE_PROMPT = """You are a strict lexical matcher for evaluating video scene graphs. For each item you get a
REFERENCE label (from human annotators) and a PREDICTED label (from a model) for the same object, or for
the relation between the same two objects. Classify how the PREDICTED label relates to the REFERENCE label:
- "identical": the same label, ignoring case, plural/singular, spelling variants and word order
- "synonym": different words with the same meaning (person / human, couch / sofa, on top of / on)
- "hypernym/hyponym": one is a more general or more specific term for the other (plant / tree,
  vehicle / car, child / baby, holding / grasping, next to / near)
- "semantic overlap": clearly overlapping meaning but none of the above (table / countertop,
  walking with / walking beside)
- "mismatch": a different thing or a different relation (child / grass, car / ground, in front of / behind)
Judge only the two labels; do not guess what the video shows.
Answer only with JSON: {"results": [{"i": <item number>, "category": "<one of the five>"}]}

ITEMS: %s"""


# ----------------------------------------------------------------------------- parsing
def norm(label):
    s = str(label).lower().replace("_", " ")
    s = re.sub(r"\(\s*uncertain\s*\)", "", s)
    return re.sub(r"\s+", " ", s).strip()


OBJ_RE = re.compile(r'"object[ _](\d+)"\s*:\s*"((?:[^"\\]|\\.)*)"')
REL_RE = re.compile(r'\[\s*(-?\d+)\s*,\s*"((?:[^"\\]|\\.)*)"\s*,\s*(-?\d+)\s*,\s*(\[\s*(?:\[[^\[\]]*\]\s*,?\s*)*\])\s*\]')


def to_spans(x):
    """[[a, b], ...] (or a single [a, b]) -> list of [float, float]; anything malformed is dropped."""
    if isinstance(x, list) and len(x) == 2 and all(isinstance(v, (int, float)) for v in x):
        x = [x]
    out = []
    for s in x if isinstance(x, list) else []:
        try:
            if isinstance(s, list) and len(s) == 2:
                out.append([float(s[0]), float(s[1])])
        except (TypeError, ValueError):
            continue
    return out


def parse_prediction(text):
    """{"objects": {k: label}, "relations": [(s, pred, o, [[a, b], ...])], "json_ok": bool}.
    Invalid JSON (e.g. cut off at the token limit) is salvaged item by item."""
    objects, relations = {}, []
    try:
        g = json.loads(text)
        for o in g.get("objects", []):
            for key, val in o.items():
                m = re.fullmatch(r"object[ _](\d+)", key)
                if m:
                    objects[int(m.group(1))] = str(val)
        for r in g.get("relationships", []):
            if isinstance(r, list) and len(r) >= 4:
                try:
                    relations.append((int(r[0]), str(r[1]), int(r[2]), to_spans(r[3])))
                except (TypeError, ValueError):
                    continue
        return {"objects": objects, "relations": relations, "json_ok": True}
    except (json.JSONDecodeError, TypeError, ValueError, AttributeError):
        pass
    for m in OBJ_RE.finditer(text):
        objects[int(m.group(1))] = m.group(2)
    for m in REL_RE.finditer(text):
        try:
            relations.append((int(m.group(1)), m.group(2), int(m.group(3)), to_spans(json.loads(m.group(4)))))
        except (json.JSONDecodeError, ValueError):
            continue
    return {"objects": objects, "relations": relations, "json_ok": False}


# ----------------------------------------------------------------------------- time
def merge(spans):
    out = []
    for a, b in sorted((float(a), float(b)) for a, b in spans if b > a):
        if out and a <= out[-1][1]:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return out


def length(spans):
    return sum(b - a for a, b in spans)


def tiou(gt_spans, pred_spans):
    g, p = merge(gt_spans), merge(pred_spans)
    inter = sum(max(0.0, min(b1, b2) - max(a1, a2)) for a1, b1 in g for a2, b2 in p)
    union = length(g) + length(p) - inter
    return inter / union if union > 0 else 0.0


def pred_spans(spans, gt, stats):
    if gt["time_unit"] == "index":
        return [[a, b + 1] for a, b in spans]
    scale = stats["duration_s"] / max(1, stats["sampled_frames"])
    return [[a * scale, (b + 1) * scale] for a, b in spans]


# ----------------------------------------------------------------------------- judge
class Judge:
    """Kimi K3 on NVIDIA NIM. Every answer is cached in results/traser_bench/judge_cache.json."""
    def __init__(self, model="moonshotai/kimi-k3", cache=RESULTS / "judge_cache.json"):
        self.model, self.cache_path = model, Path(cache)
        self.cache = json.load(open(self.cache_path)) if self.cache_path.exists() else {}
        self.client = None

    @staticmethod
    def key(kind, ref, pred):
        return f"{kind}\t{norm(ref)}\t{norm(pred)}"

    def ask_all(self, pairs, chunk=50, log=print):
        todo = sorted({self.key(*p) for p in pairs if norm(p[1]) != norm(p[2])} - set(self.cache))
        if not todo:
            return
        from nim import ask, nim_client
        self.client = self.client or nim_client(timeout=180)
        parts = [todo[i:i + chunk] for i in range(0, len(todo), chunk)]
        done = 0
        while parts:
            part = parts.pop(0)
            items = [{"i": n, "type": k.split("\t")[0], "reference": k.split("\t")[1], "predicted": k.split("\t")[2]}
                     for n, k in enumerate(part)]
            try:
                reply = ask(self.client, self.model, [{"role": "user", "content": JUDGE_PROMPT % json.dumps(items)}],
                            dict(temperature=0.0), max_tokens=4096)
                got = {int(x.get("i", -1)): str(x.get("category", "")).lower()
                       for x in reply.get("results", []) if isinstance(x, dict)}
            except (RuntimeError, ValueError, TypeError) as e:
                got, err = {}, e
            new = 0
            for n, k in enumerate(part):
                if got.get(n) in CATEGORIES:
                    self.cache[k] = got[n]
                    new += 1
            self.save()
            left = [k for k in part if k not in self.cache]
            done += new
            if left and len(left) > 5:          # a failed or partial answer: ask again in smaller pieces
                log(f"  {len(left)} pairs without an answer ({'call failed' if not got else 'partial answer'}); "
                    "asking again in smaller groups")
                parts = [left[:len(left) // 2], left[len(left) // 2:]] + parts
            elif left:
                log(f"  {len(left)} pairs stay unjudged for now: {[k.replace(chr(9), ' | ') for k in left]}")
            log(f"  judged {done}/{len(todo)} new pairs")

    def category(self, kind, ref, pred):
        if norm(ref) == norm(pred):
            return "identical"
        return self.cache.get(self.key(kind, ref, pred))       # None = not judged (yet)

    def save(self):
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.cache_path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.cache, indent=0, sort_keys=True))
        tmp.replace(self.cache_path)


def is_right(category, criterion):
    if criterion == "strict":
        return category == "identical"
    return category is not None and category != "mismatch"


# ----------------------------------------------------------------------------- one video
def load_video(dataset, video_id):
    gt = json.load(open(RESULTS / dataset / "gt" / f"{video_id}.json"))
    p = RESULTS / dataset / "preds" / f"{video_id}.json"
    if not p.exists():
        return gt, None, None
    stats = json.load(open(RESULTS / dataset / "preds" / f"{video_id}.stats.json"))
    return gt, parse_prediction(p.read_text()), stats


def video_pairs(gt, pred, stats):
    """The (kind, human label, predicted label) pairs this video needs judged."""
    gt_of_col = {o["col"]: o for o in gt["objects"]}
    to_gt = {k + 1: gt_of_col[c]["gt_id"] for k, c in enumerate(stats["mask_columns"]) if c in gt_of_col}
    to_gt[-1] = -1
    name = {o["gt_id"]: o["name"] for o in gt["objects"]}
    pred_name = {to_gt[k]: v for k, v in pred["objects"].items() if k in to_gt}
    pairs = [("object", name[g], pred_name[g]) for g in name if g in pred_name]
    by_pair = {}
    for s, p, o, spans in pred["relations"]:
        if s in to_gt and o in to_gt:
            by_pair.setdefault((to_gt[s], to_gt[o]), []).append((p, spans))
    for r in gt["relations"]:
        pairs += [("relation", r["pred"], p) for p, _ in by_pair.get((r["subj"], r["obj"]), [])]
    return pairs, name, pred_name, by_pair


def score_video(gt, pred, stats, judge, criterion="lenient", thr=0.5):
    """Counts for one video. pred=None (no prediction) scores every human item as wrong."""
    n_obj, n_rel = len(gt["objects"]), len(gt["relations"])
    out = {"objects": n_obj, "relations": n_rel, "object_ok": 0, "relation_ok": 0, "triplet_ok": 0,
           "relation_ok_any_time": 0, "unjudged": 0}
    if pred is None:
        return out
    _, name, pred_name, by_pair = video_pairs(gt, pred, stats)

    def ok(kind, ref, hyp):
        c = judge.category(kind, ref, hyp)
        out["unjudged"] += c is None
        return is_right(c, criterion)

    obj_ok = {g: (g in pred_name and ok("object", name[g], pred_name[g])) for g in name}
    obj_ok[-1] = True
    out["object_ok"] = sum(v for g, v in obj_ok.items() if g != -1)
    for r in gt["relations"]:
        cands = [(p, pred_spans(sp, gt, stats)) for p, sp in by_pair.get((r["subj"], r["obj"]), [])]
        word_ok = [(p, sp) for p, sp in cands if ok("relation", r["pred"], p)]
        timed = [1 for _, sp in word_ok if tiou(r["spans"], sp) > thr]
        out["relation_ok_any_time"] += bool(word_ok)
        if timed:
            out["relation_ok"] += 1
            out["triplet_ok"] += bool(obj_ok.get(r["subj"]) and obj_ok.get(r["obj"]))
    return out


# ----------------------------------------------------------------------------- looking at videos
def _fmt_spans(spans, unit):
    u = "s" if unit == "seconds" else ""
    return ", ".join(f"{a:g}-{b:g}{u}" for a, b in merge(spans)) or "-"


def _show_table(rows, title):
    print(title)
    if not rows:
        print("   (none)\n")
        return
    try:
        import pandas as pd
        from IPython.display import display
        display(pd.DataFrame(rows).style.hide(axis="index").set_properties(**{"text-align": "left"}))
    except Exception:  # noqa: BLE001  (plain text outside a notebook)
        cols = list(rows[0])
        width = {c: min(40, max(len(c), *(len(str(r[c])) for r in rows))) for c in cols}
        print("   " + "  ".join(c.ljust(width[c]) for c in cols))
        for r in rows:
            print("   " + "  ".join(str(r[c])[:40].ljust(width[c]) for c in cols))
    print()


def video_report(gt, pred, stats, judge, thr=0.5):
    """Tables for one predicted video: human labels next to TRASER's (lenient, tIoU > thr).
    A verdict the judge has not given yet is None ("?")."""
    unit = gt.get("time_unit", "seconds")
    _, name, pred_name, by_pair = video_pairs(gt, pred, stats)
    name_of = {g: f"{n} #{g}" for g, n in name.items()}          # ids: a video often has two "adult"s
    name_of[-1] = "camera"
    mark = lambda x: "✓" if x else ("?" if x is None else "✗")
    obj_ok, objects = {-1: True}, []
    for o in gt["objects"]:
        g, hyp = o["gt_id"], pred_name.get(o["gt_id"])
        cat = judge.category("object", o["name"], hyp) if hyp is not None else "mismatch"
        obj_ok[g] = None if cat is None else is_right(cat, "lenient")
        objects.append({"id": g, "human label": o["name"], "TRASER label": hyp if hyp is not None else "-",
                        "verdict": (cat or "not judged yet") if hyp is not None else "no label from TRASER",
                        "right": mark(obj_ok[g])})
    relations, n_rel, n_tri, n_unj = [], 0, 0, 0
    for r in gt["relations"]:
        cands = [(p, pred_spans(sp, gt, stats)) for p, sp in by_pair.get((r["subj"], r["obj"]), [])]
        best = None
        for p, sp in cands:
            cat = judge.category("relation", r["pred"], p)
            t = tiou(r["spans"], sp)
            key = (is_right(cat, "lenient") and t > thr, cat is None and t > thr, is_right(cat, "lenient"), t)
            if best is None or key > best[0]:
                best = (key, p, sp, cat, t)
        rel_ok = True if best and best[0][0] else (None if best and best[0][1] else False)
        parts = [rel_ok, obj_ok.get(r["subj"], False), obj_ok.get(r["obj"], False)]
        tri_ok = False if False in parts else (None if None in parts else True)
        n_rel += rel_ok is True
        n_tri += tri_ok is True
        n_unj += rel_ok is None or tri_ok is None
        relations.append({
            "human: subject - predicate - object": f"{name_of.get(r['subj'], r['subj'])} - {r['pred']} - "
                                                   f"{name_of.get(r['obj'], r['obj'])}",
            "human time": _fmt_spans(r["spans"], unit),
            "TRASER (same two objects)": (best[1] + (f" (+{len(cands) - 1} more)" if len(cands) > 1 else ""))
                                         if best else "nothing for this pair",
            "TRASER time": _fmt_spans(best[2], unit) if best else "-",
            "word": (best[3] or "not judged yet") if best else "-",
            "tIoU": f"{best[4]:.2f}" if best else "-",
            "relation": mark(rel_ok), "triplet": mark(tri_ok)})
    known = {(r["subj"], r["obj"]) for r in gt["relations"]}
    extra = [f"{name_of.get(a, a)} - {p} - {name_of.get(b, b)} [{_fmt_spans(pred_spans(sp, gt, stats), unit)}]"
             for (a, b), lst in by_pair.items() if (a, b) not in known for p, sp in lst]
    n_obj = len(name)
    return {
        "header": f"{stats.get('duration_s')} s, {stats.get('sampled_frames')} frames read | human: {n_obj} objects, "
                  f"{len(gt['relations'])} relations | TRASER: {len(pred['objects'])} objects, "
                  f"{len(pred['relations'])} relations, "
                  f"{'valid JSON' if pred['json_ok'] else 'cut-off answer (salvaged)'}, {stats.get('new_tokens')} tokens",
        "objects": objects, "relations": relations, "extra": extra,
        "counts": {"objects": n_obj, "object_ok": sum(obj_ok[g] is True for g in name),
                   "object_unjudged": sum(obj_ok[g] is None for g in name), "relations": len(gt["relations"]),
                   "relation_ok": n_rel, "triplet_ok": n_tri, "relation_unjudged": n_unj}}


def _recent(dataset, last):
    done = sorted((p for p in (RESULTS / dataset / "preds").glob("*.json") if not p.name.endswith(".stats.json")),
                  key=lambda p: p.stat().st_mtime)
    return [p.stem for p in (done if last is None else done[-last:])]


def show(dataset, videos=None, last=3, ask_judge=False, thr=0.5, log=print):
    """Human labels next to TRASER's answer for a few videos: objects, relations, triplets.
    videos: list of video ids (default: the `last` most recently predicted). Verdicts come from the
    judge cache (or identical text); ask_judge=True asks Kimi K3 for the missing ones (needs the key)."""
    videos = videos or _recent(dataset, last)
    judge = Judge()
    loaded = {v: load_video(dataset, v) for v in videos}
    if ask_judge:
        judge.ask_all([p for gt, pred, st in loaded.values() if pred is not None
                       for p in video_pairs(gt, pred, st)[0]], log=log)
    for v, (gt, pred, stats) in loaded.items():
        print("=" * 100)
        if pred is None:
            print(f"{dataset}/{v}: no prediction yet\n")
            continue
        rep = video_report(gt, pred, stats, judge, thr)
        c = rep["counts"]
        print(f"{dataset}/{v}   {rep['header']}")
        _show_table(rep["objects"], f"OBJECTS: {c['object_ok']}/{c['objects']} right"
                                    + (f", {c['object_unjudged']} not judged yet (?)" if c["object_unjudged"] else ""))
        _show_table(rep["relations"], f"RELATIONS: {c['relation_ok']}/{c['relations']} right   |   TRIPLETS: "
                                      f"{c['triplet_ok']}/{c['relations']} right   (lenient, tIoU > {thr})"
                                      + (f"   |   {c['relation_unjudged']} wait for the judge (?)"
                                         if c["relation_unjudged"] else ""))
        if rep["extra"]:
            print(f"TRASER relations between pairs the humans did not annotate: {len(rep['extra'])}, e.g. "
                  + "; ".join(rep["extra"][:5]) + "\n")


def _md_table(rows):
    if not rows:
        return "(none)\n"
    esc = lambda x: str(x).replace("|", "/").replace("\n", " ")
    cols = list(rows[0])
    return ("| " + " | ".join(cols) + " |\n|" + "---|" * len(cols) + "\n"
            + "".join("| " + " | ".join(esc(r[c]) for c in cols) + " |\n" for r in rows))


def pair_report(gt, pred, stats, judge, thr=0.5):
    """Object pairs of one video: which pairs the humans annotated, which TRASER talked about, and what each
    said. A pair is (subject, object) in that direction; TRASER's "object k" is the human object it was given."""
    unit = gt.get("time_unit", "seconds")
    _, name, pred_name, by_pair = video_pairs(gt, pred, stats)
    tag = lambda g: "camera" if g == -1 else f"{name.get(g, '?')} #{g}"
    human = {}
    for r in gt["relations"]:
        human.setdefault((r["subj"], r["obj"]), []).append((r["pred"], r["spans"]))
    rows, counts = [], {"both": 0, "missed": 0, "reversed": 0, "extra": 0}
    for pair in sorted(set(human) | set(by_pair), key=lambda p: (p not in human, p)):
        h = human.get(pair, [])
        t = [(p, pred_spans(sp, gt, stats)) for p, sp in by_pair.get(pair, [])]
        if h and t:
            status = "✓ TRASER has this pair"
            counts["both"] += 1
        elif h and (pair[1], pair[0]) in by_pair:
            status = "↔ TRASER has it reversed"
            counts["reversed"] += 1
        elif h:
            status = "✗ TRASER missed this pair"
            counts["missed"] += 1
        else:
            status = "+ only TRASER"
            counts["extra"] += 1
        right = []
        for p, sp in h:                  # is one of TRASER's relations right for this human relation?
            ok = [is_right(judge.category("relation", p, q), "lenient") and tiou(sp, qs) > thr for q, qs in t]
            und = [judge.category("relation", p, q) is None for q, _ in t]
            right.append("✓" if any(ok) else ("?" if any(und) else ("✗" if t else "-")))
        rows.append({"pair (subject → object)": f"{tag(pair[0])} → {tag(pair[1])}",
                     "human said": "; ".join(f"{p} [{_fmt_spans(sp, unit)}]" for p, sp in h) or "-",
                     "TRASER said": "; ".join(f"{p} [{_fmt_spans(sp, unit)}]" for p, sp in t) or "-",
                     "pair": status,
                     "relation right? (lenient, tIoU > 0.5)": " ".join(right) if h else "-"})
    objects = [{"id": o["gt_id"], "human label": o["name"], "TRASER label": pred_name.get(o["gt_id"], "- (not given to TRASER)")}
               for o in gt["objects"]]
    counts.update(human_pairs=len(human), traser_pairs=len(by_pair),
                  human_relations=len(gt["relations"]), traser_relations=len(pred["relations"]))
    return objects, rows, counts


def write_pairs(dataset, videos=None, n=10, seed=0, thr=0.5, path=None):
    """<dataset>/PAIRS.md: for n random videos (fixed seed), every object pair the humans or TRASER mention,
    side by side, so one can see which pairs TRASER covers, misses, reverses or adds."""
    import random
    judge = Judge()
    done = [v for v in video_ids(dataset) if (RESULTS / dataset / "preds" / f"{v}.json").exists()]
    videos = videos or sorted(random.Random(seed).sample(done, min(n, len(done))))
    path = Path(path or RESULTS / dataset / "PAIRS.md")
    overview, sections = [], []
    for v in videos:
        gt, pred, stats = load_video(dataset, v)
        objects, rows, c = pair_report(gt, pred, stats, judge, thr)
        anchor = re.sub(r"[^a-z0-9_-]", "", v.lower())
        overview.append({"video": f"[{v}](#{anchor})", "human pairs": c["human_pairs"], "TRASER pairs": c["traser_pairs"],
                         "pairs in both": c["both"], "missed by TRASER": c["missed"], "reversed": c["reversed"],
                         "only TRASER": c["extra"]})
        sections.append(
            f"## {v}\n\n{stats.get('duration_s')} s video; humans: {len(gt['objects'])} objects, {c['human_relations']} "
            f"relations on {c['human_pairs']} pairs; TRASER: {c['traser_relations']} relations on {c['traser_pairs']} pairs"
            f"{'' if pred['json_ok'] else ' (answer cut off at the token limit, read up to there)'}.\n\n"
            f"**Pairs:** {c['both']} in both, {c['missed']} missed by TRASER, {c['reversed']} reversed, "
            f"{c['extra']} only TRASER\n\n<details><summary>objects (human label vs TRASER label)</summary>\n\n"
            f"{_md_table(objects)}\n</details>\n\n{_md_table(rows)}\n")
    tot = {k: sum(o[k] for o in overview) for k in ("human pairs", "TRASER pairs", "pairs in both", "missed by TRASER",
                                                    "reversed", "only TRASER")}
    text = (f"# {dataset}: which object pairs TRASER talks about ({len(overview)} random videos, seed {seed})\n\n"
            "TRASER is given the human objects (masks) and writes its own list of relations; it is not told which "
            "pairs to describe. Each row is one ordered pair (subject → object) that the humans or TRASER mention.\n\n"
            "- **✓ TRASER has this pair**: TRASER wrote at least one relation for the same two objects, same direction\n"
            "- **✗ TRASER missed this pair**: humans annotated it, TRASER said nothing about these two objects\n"
            "- **↔ reversed**: TRASER only has the other direction (object → subject); scored as missed\n"
            "- **+ only TRASER**: TRASER describes a pair the humans did not annotate (ignored by the scores)\n"
            "- last column, one mark per human relation of the pair: ✓ word right and tIoU > 0.5, ✗ not, "
            "? the judge has not compared the words yet\n\n"
            f"**Total over these videos:** {tot['human pairs']} human pairs, {tot['TRASER pairs']} TRASER pairs; "
            f"{tot['pairs in both']} in both, {tot['missed by TRASER']} missed, {tot['reversed']} reversed, "
            f"{tot['only TRASER']} only TRASER.\n\n" + _md_table(overview) + "\n" + "\n".join(sections))
    path.write_text(text)
    return path


def write_compare(dataset, thr=0.5, path=None):
    """results/traser_bench/<dataset>/COMPARE.md: every predicted video, human labels next to TRASER's
    (objects, relations, triplets), readable on GitHub. Verdicts from the judge cache ("?" = not judged yet)."""
    judge = Judge()
    path = Path(path or RESULTS / dataset / "COMPARE.md")
    videos = sorted(_recent(dataset, None))
    overview, sections = [], []
    for v in videos:
        gt, pred, stats = load_video(dataset, v)
        if pred is None or not (RESULTS / dataset / "gt" / f"{v}.json").exists():
            continue
        rep = video_report(gt, pred, stats, judge, thr)
        c = rep["counts"]
        overview.append({"video": f"[{v}](#{re.sub(r'[^a-z0-9_-]', '', v.lower())})",
                         "objects right": f"{c['object_ok']}/{c['objects']}",
                         "relations right": f"{c['relation_ok']}/{c['relations']}",
                         "triplets right": f"{c['triplet_ok']}/{c['relations']}",
                         "not judged yet (?)": c["object_unjudged"] + c["relation_unjudged"]})
        sections.append(f"## {v}\n\n{rep['header']}\n\n**Objects: {c['object_ok']}/{c['objects']} right**\n\n"
                        f"{_md_table(rep['objects'])}\n**Relations: {c['relation_ok']}/{c['relations']} right, "
                        f"triplets: {c['triplet_ok']}/{c['relations']} right** (lenient, tIoU > {thr})\n\n"
                        f"{_md_table(rep['relations'])}\n"
                        + (f"TRASER relations between pairs the humans did not annotate ({len(rep['extra'])}): "
                           + "; ".join(rep["extra"][:10]) + "\n\n" if rep["extra"] else ""))
    tot = lambda k: sum(int(o[k].split("/")[0]) for o in overview)
    den = lambda k: sum(int(o[k].split("/")[1]) for o in overview)
    text = (f"# {dataset}: human labels vs TRASER, video by video\n\n"
            f"{len(overview)} videos with a prediction. Lenient criterion, temporal IoU > {thr}. "
            "✓ right, ✗ wrong, ? = the judge (Kimi K3) has not compared these two labels yet "
            "(identical text counts as right without the judge). Relation = same two objects, predicate not a "
            "mismatch, tIoU > 0.5; triplet = relation right and both object labels right. Made by "
            "`tools/bench_eval.py write_compare`.\n\n"
            + (f"**So far: objects {tot('objects right')}/{den('objects right')}, relations "
               f"{tot('relations right')}/{den('relations right')}, triplets "
               f"{tot('triplets right')}/{den('triplets right')}** (unjudged pairs count as not right; scores in README.md)\n\n"
               if overview else "")
            + _md_table(overview) + "\n" + "\n".join(sections))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


# ----------------------------------------------------------------------------- whole run
def video_ids(dataset):
    d = RESULTS / dataset / "gt"
    return sorted(p.stem for p in d.glob("*.json")) if d.exists() else []


def evaluate(datasets=DATASETS, judge=None, ask=True, log=print):
    judge = judge or Judge()
    loaded = {ds: {v: load_video(ds, v) for v in video_ids(ds)} for ds in datasets}
    if ask:
        pairs = [p for ds in loaded for gt, pred, st in loaded[ds].values() if pred is not None
                 for p in video_pairs(gt, pred, st)[0]]
        log(f"{len(pairs)} label pairs to judge ({len(set(Judge.key(*p) for p in pairs))} distinct)")
        judge.ask_all(pairs, log=log)
    report = {}
    for ds, vids in loaded.items():
        if not vids:
            continue
        done = {v: x for v, x in vids.items() if x[1] is not None}
        failed = sorted(p.name[:-len(".error.txt")] for p in (RESULTS / ds / "preds").glob("*.error.txt")) \
            if (RESULTS / ds / "preds").exists() else []
        rep = {"videos_prepared": len(vids), "videos_predicted": len(done), "split_size": SPLIT_SIZE[ds],
               "failed": [v for v in failed if v not in done],
               "json_invalid": sum(not x[1]["json_ok"] for x in done.values()), "scores": {}}
        for criterion in ("lenient", "strict"):
            for thr in (0.5, 0.1):
                rows = [score_video(*x, judge, criterion, thr) for x in done.values()]
                tot = {k: sum(r[k] for r in rows) for k in rows[0]} if rows else {}
                pct = lambda a, b: round(100 * a / b, 1) if b else None  # noqa: E731
                macro = lambda k, d: round(100 * sum(r[k] / r[d] for r in rows if r[d]) / max(1, sum(1 for r in rows if r[d])), 1)  # noqa: E731
                rep["scores"][f"{criterion}@{thr}"] = {
                    "object": pct(tot.get("object_ok", 0), tot.get("objects", 0)),
                    "relation": pct(tot.get("relation_ok", 0), tot.get("relations", 0)),
                    "triplet": pct(tot.get("triplet_ok", 0), tot.get("relations", 0)),
                    "relation_any_time": pct(tot.get("relation_ok_any_time", 0), tot.get("relations", 0)),
                    "macro_object": macro("object_ok", "objects") if rows else None,
                    "macro_relation": macro("relation_ok", "relations") if rows else None,
                    "macro_triplet": macro("triplet_ok", "relations") if rows else None,
                    "counts": tot}
        cats = {}
        for gt, pred, st in done.values():
            for kind, ref, hyp in video_pairs(gt, pred, st)[0]:
                c = judge.category(kind, ref, hyp) or "not judged"
                cats.setdefault(kind, {}).setdefault(c, 0)
                cats[kind][c] += 1
        rep["judge_categories"] = cats
        report[ds] = rep
    return report


def write_report(report, path=RESULTS / "README.md"):
    def cell(ds, metric, key="lenient@0.5"):
        v = report.get(ds, {}).get("scores", {}).get(key, {}).get(metric)
        return "–" if v is None else f"{v:.1f}"

    ds = [d for d in DATASETS]
    head = ("| | " + " | ".join(f"Triplet {d}" for d in ds) + " | " + " | ".join(f"Relation {d}" for d in ds)
            + " | " + " | ".join(f"Object {d}" for d in ds) + " |")
    sep = "|---" * (1 + 3 * len(ds)) + "|"
    paper = "| TRASER, paper | " + " | ".join(str(PAPER[m][d]) for m in ("triplet", "relation", "object") for d in ds) + " |"
    ours = "| **TRASER, ours** | " + " | ".join(cell(d, m) for m in ("triplet", "relation", "object") for d in ds) + " |"
    L = ["# TRASER on PVSG, VidOR and SVG2test: regenerating Table 2", "",
         "Released checkpoint `UWGZQ/TRASER`, official inference settings (1 fps, at most 128 frames, at most 40 objects, greedy), "
         "float16 on Kaggle T4s. Lenient semantic criterion, temporal IoU > 0.5; scores over the videos with a prediction (see Coverage); judge: Kimi K3 (NVIDIA NIM) instead of the paper's GPT-4o-mini.",
         "", head, sep, paper, ours, "",
         "## Coverage", "", "| | test videos | prepared | predicted | failed | answers not valid JSON (salvaged) |", "|---|---|---|---|---|---|"]
    for d in ds:
        r = report.get(d)
        if r:
            L.append(f"| {d} | {r['split_size']} | {r['videos_prepared']} | {r['videos_predicted']} | "
                     f"{len(r['failed'])} | {r['json_invalid']} |")
    L += ["", "## Other settings (same predictions)", "",
          "| setting | " + " | ".join(f"{m} {d}" for m in ("Triplet", "Relation", "Object") for d in ds) + " |",
          "|---" * (1 + 3 * len(ds)) + "|"]
    for key, label in (("lenient@0.5", "lenient, tIoU 0.5 (main)"), ("lenient@0.1", "lenient, tIoU 0.1"),
                       ("strict@0.5", "strict, tIoU 0.5"), ("strict@0.1", "strict, tIoU 0.1")):
        L.append(f"| {label} | " + " | ".join(cell(d, m, key) for m in ("triplet", "relation", "object") for d in ds) + " |")
    L.append("| lenient, tIoU 0.5, per-video average | " +
             " | ".join(cell(d, f"macro_{m}") for m in ("triplet", "relation", "object") for d in ds) + " |")
    L.append("| lenient, relation ignoring time | – | – | – | " + " | ".join(cell(d, "relation_any_time") for d in ds) + " | – | – | – |")
    L += ["", "## Judge answers (lenient = everything but mismatch)", ""]
    for d in ds:
        if d in report:
            L.append(f"- **{d}**: " + "; ".join(f"{kind}: " + ", ".join(f"{c} {n}" for c, n in sorted(v.items(), key=lambda x: -x[1]))
                                              for kind, v in report[d]["judge_categories"].items()))
    L += ["", "## How it is scored", "", "See the docstring of `tools/bench_eval.py`. Differences from the paper that we know of:",
          "- judge: Kimi K3 with our prompt (the paper's GPT-4o-mini prompt is not released);",
          "- float16 on a T4 instead of bfloat16 on an A100 (greedy decoding can change a few tokens);",
          "- VidOR masks: SAM 2.1 from VidOR's boxes on the frames TRASER reads (the paper also used SAM 2, details not given);",
          "- videos longer than 128 s are read at fewer than 1 frame per second (released code caps at 128 frames);",
          "- pooled over all human items (the per-video average is also shown)."]
    Path(path).write_text("\n".join(L) + "\n")
    with open(Path(path).with_name("scores.json"), "w") as f:
        json.dump(report, f, indent=1)
    for d in report:                     # the video-by-video pages, with the verdicts just judged
        if video_ids(d):
            write_compare(d)
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--datasets", nargs="*", default=DATASETS)
    ap.add_argument("--no_judge", action="store_true", help="use cached judge answers only")
    ap.add_argument("--pairs", type=int, default=0, help="only write <dataset>/PAIRS.md for this many random videos")
    ap.add_argument("--compare", action="store_true",
                    help="only write <dataset>/COMPARE.md (human vs TRASER per video, cached verdicts), no scoring")
    args = ap.parse_args()
    if args.pairs:
        for ds in args.datasets:
            if video_ids(ds):
                print("wrote", write_pairs(ds, n=args.pairs))
        return
    if args.compare:
        for ds in args.datasets:
            if video_ids(ds):
                print("wrote", write_compare(ds))
        return
    print(write_report(evaluate(args.datasets, ask=not args.no_judge)))


if __name__ == "__main__":
    main()
