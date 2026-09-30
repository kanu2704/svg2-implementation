"""Phase 1.3: audit the SVG2 annotations (no masks, no videos needed).

Answers the questions raised by the Phase 1.2 inspection and writes notes/phase1_audit.md:

  A. Train/test overlap: do SVG2_test videos also appear in any training split? (plot hole P19)
  B. raw -> cleaned: what did cleaning (SAM3 verification) remove, and is it the "(uncertain)" objects? (P15, P20)
  C. Label hygiene of the training targets: underscores, "a/b" labels, capitals, "(uncertain)".
  D. Attributes: how many are appearance vs position/action/subjective? Test attribute types.
  E. Relations: predicate vocabulary, left/right predicates, duplicate spans.
  F. SVG2_test object levels: which labels are parts (L2/L3)?

The PVD splits are large, so B-E use a sample of PVD videos (--pvd_sample, default 20000).

    python tools/audit_annotations.py
"""
import argparse
import glob
import json
import os
import re
import time
from collections import Counter, defaultdict

import pyarrow.parquet as pq

ROOT = "data/SVG2/data"
TRAIN_SPLITS = ["cleaned/sav", "cleaned/pvd", "academic_datasets/vipseg", "academic_datasets/vidor",
                "academic_datasets/vidvrd", "academic_datasets/lvvis", "academic_datasets/ovis"]
TEST_SPLITS = ["SVG2_test/sav", "SVG2_test/vipseg"]

# Words that describe impression or quality rather than something visible in the pixels.
SUBJECTIVE = ["elegant", "well-maintained", "well maintained", "sturdy", "robust", "classic", "modern",
              "charm", "pristine", "well-crafted", "durable", "stylish", "beautiful", "aesthetic",
              "well-defined", "well-preserved", "unblemished", "inviting", "cozy", "sophisticated",
              "functional", "practical", "vibrant", "rich", "subtle", "muted", "neat", "tidy", "clean"]
POSITION_WORDS = ["left", "right", "top", "bottom", "front", "behind", "background", "foreground",
                  "center", "middle", "on the", "in the", "in a ", "near", "corner"]
LEFT_RIGHT = re.compile(r"\b(left|right)\b")


def files_of(split):
    return sorted(glob.glob(os.path.join(ROOT, split, "*.parquet")))


def parse(value):
    if value is None:
        return []
    if isinstance(value, str):
        return json.loads(value) if value else []
    return value


def iter_rows(split, limit=None, only_ids=None):
    """Stream (video_id, objects, relationships) without loading a whole split into memory."""
    n = 0
    for f in files_of(split):
        pf = pq.ParquetFile(f)
        for batch in pf.iter_batches(columns=["video_id", "objects", "relationships"], batch_size=2048):
            d = batch.to_pydict()
            for vid, o, r in zip(d["video_id"], d["objects"], d["relationships"]):
                if only_ids is not None and vid not in only_ids:
                    continue
                yield vid, parse(o), parse(r)
                n += 1
                if limit is not None and n >= limit:
                    return


def video_ids(split):
    ids = set()
    for f in files_of(split):
        ids.update(pq.read_table(f, columns=["video_id"]).column("video_id").to_pylist())
    return ids


def obj_key(ob):
    return next((k for k in ob if k.startswith("object")), None)


def obj_id(ob):
    k = obj_key(ob)
    return int(k.split("_")[1]) if k and "_" in k and k.split("_")[1].isdigit() else None


def label_of(ob):
    k = obj_key(ob)
    return str(ob[k]) if k else ""


def base_label(label):
    return label.replace("(uncertain)", "").strip().lower()


def pct(a, b):
    return f"{100.0 * a / b:.1f}%" if b else "–"


# --------------------------------------------------------------------------- A
def section_overlap(out):
    out += ["## A. Train/test overlap (plot hole P19)", ""]
    ids = {s: video_ids(s) for s in TRAIN_SPLITS + TEST_SPLITS + ["raw/sav"] if files_of(s)}
    out += ["| test split | test videos | " + " | ".join(s for s in TRAIN_SPLITS + ["raw/sav"] if s in ids) + " |",
            "|---|---|" + "---|" * len([s for s in TRAIN_SPLITS + ["raw/sav"] if s in ids])]
    for t in TEST_SPLITS:
        if t not in ids:
            continue
        cells = [str(len(ids[t] & ids[s])) for s in TRAIN_SPLITS + ["raw/sav"] if s in ids]
        out.append(f"| {t} | {len(ids[t])} | " + " | ".join(cells) + " |")

    # VIPSeg ids look like "<clip>_<youtubeId>": also compare the YouTube id alone.
    if "SVG2_test/vipseg" in ids and "academic_datasets/vipseg" in ids:
        yt = lambda s: {v.split("_", 1)[1] for v in s if "_" in v}
        shared_yt = yt(ids["SVG2_test/vipseg"]) & yt(ids["academic_datasets/vipseg"])
        out += ["", f"VIPSeg: test videos whose **YouTube source video** also appears in VIPSeg training "
                    f"(different clip, same source): {len(shared_yt)} of {len(yt(ids['SVG2_test/vipseg']))}"]
    for t in TEST_SPLITS:
        for s in TRAIN_SPLITS:
            if t in ids and s in ids and ids[t] & ids[s]:
                out.append(f"- `{t}` ∩ `{s}` examples: {sorted(ids[t] & ids[s])[:10]}")
    out.append("")


# --------------------------------------------------------------------------- B
def section_raw_vs_cleaned(out, source, sample):
    raw_split, clean_split = f"raw/{source}", f"cleaned/{source}"
    if not (files_of(raw_split) and files_of(clean_split)):
        return set()
    t0 = time.time()
    raw = {}
    for vid, objs, _ in iter_rows(raw_split, limit=sample):
        raw[vid] = {obj_id(o): o for o in objs}
    clean = {vid: {obj_id(o): o for o in objs} for vid, objs, _ in iter_rows(clean_split, only_ids=set(raw))}

    n_raw_obj = sum(len(v) for v in raw.values())
    n_clean_obj = sum(len(v) for v in clean.values())
    dropped_videos = len(set(raw) - set(clean))

    same_id_same_label = same_attrs = cleaned_total = 0
    kept_by_certainty = {True: [0, 0], False: [0, 0]}  # uncertain -> [kept, total]
    label_kept, label_total = Counter(), Counter()
    for vid, robjs in raw.items():
        cobjs = clean.get(vid, {})
        for oid, co in cobjs.items():
            cleaned_total += 1
            ro = robjs.get(oid)
            if ro is not None and base_label(label_of(ro)) == base_label(label_of(co)):
                same_id_same_label += 1
                same_attrs += (ro.get("attributes") or []) == (co.get("attributes") or [])
        for oid, ro in robjs.items():
            unc = "uncertain" in label_of(ro)
            kept = oid in cobjs and base_label(label_of(cobjs[oid])) == base_label(label_of(ro))
            kept_by_certainty[unc][0] += kept
            kept_by_certainty[unc][1] += 1
            b = base_label(label_of(ro))
            label_total[b] += 1
            label_kept[b] += kept

    out += [f"## B. raw → cleaned for `{source}` ({len(raw)} raw videos{' (sample)' if sample else ''})", "",
            f"- videos dropped entirely by cleaning: {dropped_videos} ({pct(dropped_videos, len(raw))})",
            f"- objects: raw {n_raw_obj} → cleaned {n_clean_obj} (kept {pct(n_clean_obj, n_raw_obj)})",
            f"- cleaned objects whose id exists in raw with the same label: {pct(same_id_same_label, cleaned_total)}"
            f"  (high = ids are preserved, so the per-object numbers below are meaningful)",
            f"- …and with identical attributes: {pct(same_attrs, cleaned_total)}",
            f"- keep rate of raw objects labelled '(uncertain)': {pct(*kept_by_certainty[True])} "
            f"of {kept_by_certainty[True][1]}",
            f"- keep rate of raw objects without '(uncertain)': {pct(*kept_by_certainty[False])} "
            f"of {kept_by_certainty[False][1]}", ""]
    common = [(l, label_total[l]) for l in label_total if label_total[l] >= 200]
    by_rate = sorted(common, key=lambda x: label_kept[x[0]] / x[1])
    out.append("Most-removed labels (≥200 raw occurrences): " +
               ", ".join(f"{l} {pct(label_kept[l], n)} kept" for l, n in by_rate[:20]))
    out.append("")
    out.append("Most-kept labels (≥200 raw occurrences): " +
               ", ".join(f"{l} {pct(label_kept[l], n)} kept" for l, n in by_rate[::-1][:20]))
    out.append(f"\n({time.time() - t0:.0f}s)\n")
    return set(clean)


# --------------------------------------------------------------------------- C-E
def collect(split, limit=None, only_ids=None):
    labels, attrs, preds = Counter(), Counter(), Counter()
    typed = Counter()
    levels = defaultdict(Counter)
    dup_span_rels = n_rels = 0
    for vid, objs, rels in iter_rows(split, limit=limit, only_ids=only_ids):
        for ob in objs:
            labels[label_of(ob)] += 1
            for a in ob.get("attributes") or []:
                attrs[str(a)] += 1
            for t in ob.get("attributes_typed") or []:
                typed[str(t.get("name", "")).lower()] += 1
            if "level" in ob:
                levels[ob["level"]][label_of(ob)] += 1
        for r in rels:
            n_rels += 1
            preds[str(r[1])] += 1
            spans = [tuple(s) for s in (r[3] if len(r) > 3 else [])]
            dup_span_rels += len(spans) != len(set(spans))
    return dict(labels=labels, attrs=attrs, preds=preds, typed=typed, levels=levels,
                dup_span_rels=dup_span_rels, n_rels=n_rels)


def section_labels(out, data):
    out += ["## C. Label hygiene of object labels", "",
            "| split | objects | distinct | with `_` | with `/` or ' or ' | starts uppercase | '(uncertain)' | examples of odd labels |",
            "|---|---|---|---|---|---|---|---|"]
    for split, d in data.items():
        L = d["labels"]
        tot = sum(L.values())
        f = lambda cond: sum(n for l, n in L.items() if cond(l))
        odd = [l for l, _ in L.most_common() if "_" in l or "/" in l or " or " in l or l[:1].isupper()][:6]
        out.append(f"| {split} | {tot} | {len(L)} | {pct(f(lambda l: '_' in l), tot)} "
                   f"| {pct(f(lambda l: '/' in l or ' or ' in l), tot)} | {pct(f(lambda l: l[:1].isupper()), tot)} "
                   f"| {pct(f(lambda l: 'uncertain' in l), tot)} | {', '.join(odd)} |")
    out.append("")


def section_attributes(out, data):
    out += ["## D. Attributes", "",
            "Keyword heuristics, a first rough look (not a verdict): *subjective* = impression words "
            "such as 'elegant', 'sturdy', 'clean'; *position* = words such as 'left', 'on the', 'background'.", "",
            "| split | attributes | distinct | multi-word | subjective | position-like | top 20 |",
            "|---|---|---|---|---|---|---|"]
    for split, d in data.items():
        A = d["attrs"]
        tot = sum(A.values())
        if not tot:
            continue
        f = lambda cond: sum(n for a, n in A.items() if cond(a.lower()))
        out.append(f"| {split} | {tot} | {len(A)} | {pct(f(lambda a: ' ' in a), tot)} "
                   f"| {pct(f(lambda a: any(w in a for w in SUBJECTIVE)), tot)} "
                   f"| {pct(f(lambda a: any(w in a for w in POSITION_WORDS)), tot)} "
                   f"| {', '.join(a for a, _ in A.most_common(20))} |")
    for split, d in data.items():
        if d["typed"]:
            tot = sum(d["typed"].values())
            out.append(f"\n`{split}` attribute types (human-annotated): " +
                       ", ".join(f"{k} {pct(n, tot)}" for k, n in d["typed"].most_common(15)))
    out.append("")


def section_relations(out, data):
    out += ["## E. Relations", "",
            "| split | relations | distinct predicates | 'left'/'right' predicates | relations with duplicate spans | top 25 predicates |",
            "|---|---|---|---|---|---|"]
    for split, d in data.items():
        P = d["preds"]
        if not d["n_rels"]:
            continue
        lr = sum(n for p, n in P.items() if LEFT_RIGHT.search(p.lower()))
        out.append(f"| {split} | {d['n_rels']} | {len(P)} | {pct(lr, d['n_rels'])} "
                   f"| {pct(d['dup_span_rels'], d['n_rels'])} | {', '.join(p for p, _ in P.most_common(25))} |")
    # Vocabulary overlap: how many test predicates / labels were ever seen in training?
    train_preds = set().union(*(d["preds"] for s, d in data.items() if not s.startswith("SVG2_test")))
    train_labels = set().union(*(d["labels"] for s, d in data.items() if not s.startswith("SVG2_test")))
    for t in TEST_SPLITS:
        if t in data:
            P, L = data[t]["preds"], data[t]["labels"]
            out.append(f"\n`{t}`: test predicates seen verbatim in training: "
                       f"{pct(sum(n for p, n in P.items() if p in train_preds), sum(P.values()))} of occurrences; "
                       f"test object labels seen verbatim in training: "
                       f"{pct(sum(n for l, n in L.items() if l in train_labels), sum(L.values()))}")
    out.append("")


def section_levels(out, data):
    out += ["## F. SVG2_test object levels", ""]
    for t in TEST_SPLITS:
        if t in data:
            for lvl, c in sorted(data[t]["levels"].items()):
                out.append(f"- `{t}` {lvl} ({sum(c.values())}): {', '.join(f'{l} {n}' for l, n in c.most_common(20))}")
    out.append("")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pvd_sample", type=int, default=20000)
    ap.add_argument("--out", default="notes/phase1_audit.md")
    args = ap.parse_args()

    out = ["# Phase 1.3: SVG2 annotation audit", "",
           f"Generated by `tools/audit_annotations.py` (PVD sample: {args.pvd_sample} videos).", ""]
    t0 = time.time()
    section_overlap(out)
    print(f"A overlap done ({time.time() - t0:.0f}s)")
    section_raw_vs_cleaned(out, "sav", None)
    print(f"B sav done ({time.time() - t0:.0f}s)")
    pvd_ids = section_raw_vs_cleaned(out, "pvd", args.pvd_sample)
    print(f"B pvd done ({time.time() - t0:.0f}s)")

    data = {}
    for split in TRAIN_SPLITS + TEST_SPLITS:
        if not files_of(split):
            continue
        if split == "cleaned/pvd":
            data[split] = collect(split, only_ids=pvd_ids or None, limit=None if pvd_ids else args.pvd_sample)
        else:
            data[split] = collect(split)
        print(f"collected {split} ({time.time() - t0:.0f}s)")
    section_labels(out, data)
    section_attributes(out, data)
    section_relations(out, data)
    section_levels(out, data)

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "w") as f:
        f.write("\n".join(out) + "\n")
    print(f"\nReport written to {args.out} ({time.time() - t0:.0f}s total)")


if __name__ == "__main__":
    main()
