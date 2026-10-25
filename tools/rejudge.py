"""Judge every word again with one model from build.nvidia.com, then redo the tables with that model's verdicts alone.

The judging is the same as before, and as the paper describes it (Sec. 5, "Evaluation Setup"): the same prompt and five
categories (identical, synonym, hypernym/hyponym, semantic overlap, mismatch; tools/bench_eval.py JUDGE_PROMPT), the
human label as the reference and the model's as the prediction, temperature 0, 50 words per request; lenient = anything
but a mismatch, and a relation also needs temporal IoU > 0.5. The same text after normalising is "identical" without
asking, as before. Only the judge model changes: the paper's is GPT-4o-mini (its prompt is not released); ours so far
was Kimi K3 (retired by NVIDIA on 15 Oct 2026), with Claude for the words Kimi K3 never judged.

Nothing runs on a GPU again: the answers are the saved ones (Table 2: results/traser_bench/<dataset>/preds and
results/qwen7b_bench/<dataset>/preds; experiment 2: results/traser_bench/interp/raw; fine-tuning:
results/traser_bench/finetune/<model>). The verdicts are saved to results/traser_bench/judge_cache_<model>.json after
every request, so a stopped run continues where it stopped. The pages go to results/judge_rerun/<model>/.

    python3 tools/rejudge.py --list [nemotron]                    # the models your key can use (names with "nemotron")
    python3 tools/rejudge.py --model <name> --check 200           # first: 200 words Kimi K3 judged, how often it agrees
    python3 tools/rejudge.py --model <name>                       # judge every word, then write the pages
    python3 tools/rejudge.py --model <name> --count               # only count what is judged / left
    python3 tools/rejudge.py --model <name> --pages               # only rewrite the pages from the saved verdicts

The key comes from $NVIDIA_API_KEY or ~/.svg2_keys (NVIDIA_API_KEY=...), else a hidden prompt; it is never printed or saved.
"""
import argparse
import concurrent.futures as cf
import getpass
import json
import os
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bench_eval as E  # noqa: E402
import qwen_bench_report as Q  # noqa: E402
from finetune import common as F  # noqa: E402
from finetune import score as S  # noqa: E402
from interp import common as IC  # noqa: E402
from interp import judge_pairs as JP  # noqa: E402
from interp import pairs_lenient as PL  # noqa: E402

CHUNK = 50                                      # words per request, as before
SETTINGS = dict(temperature=0.0)                # as before
MAX_TOKENS = 16384      # only a cap on the reply: a thinking model (Nemotron) reasons before the JSON; Kimi K3 had 4096
TIMEOUT = 600           # seconds to wait for one reply
OUT = E.REPO / "results" / "judge_rerun"
FATAL = [(("410", "end of life", "End of Life"), "the model was retired by NVIDIA; choose another model"),
         (("401", "403", "Unauthorized", "Forbidden"), "the key was refused; check it (python3 tools/rejudge.py --list)"),
         (("404",), "this key cannot use the model; python3 tools/rejudge.py --list shows the ones it can")]
UNNAMED = re.compile(r"object ?\d+")         # Qwen's unnamed objects ("object 3"): a mismatch, as in the earlier tables
EARLIER = {"claude"}                            # the other verdicts behind the published tables (with Kimi K3's)
TEST = [{"i": 0, "type": "relation", "reference": "holding", "predicted": "grasping"},
        {"i": 1, "type": "object", "reference": "dog", "predicted": "table"}]


class Solo(E.Judge):
    """Only `model`'s verdicts (judge_cache_<model>.json): no Kimi K3, no Claude, no other order."""
    def __init__(self, model, cache=E.RESULTS / "judge_cache.json"):
        super().__init__(model, cache, others=True)

    def verdict_by_key(self, k):
        v = self.mine()
        return (v[k], self.model) if k in v else (None, None)

    def note(self):
        return f"Every word judged by {self.model} alone."


# ----------------------------------------------------------------------------- the words
def words():
    """{source: set of judge keys} for every saved answer the tables score (the same text after normalising left out)."""
    src = {}
    loaded = Q.load(Q.DATASETS)
    for m, name in (("traser", "Table 2, TRASER"), ("qwen7b", "Table 2, Qwen-7B")):
        src[name] = {E.Judge.key(*p) for ds in loaded.values() for gt, pred, st in ds[m].values() if pred is not None
                     for p in E.video_pairs(gt, pred, st)[0]}
    src["experiment 2"] = {E.Judge.key(*p) for p in JP.needed(str(IC.OUT / "raw"), str(IC.RESULTS)) if all(p)}
    ft = set()
    for ds, vids, models in ft_sets():
        for v in vids:
            gt = E.load_video(ds, v, IC.RESULTS)[0]
            for m in models:
                ft |= {E.Judge.key(*p) for p in E.video_pairs(gt, *S.answer(ds, v, S.root(m, F.OUT), gt)[1:])[0]}
    src["fine-tuning"] = ft
    return {s: {k for k in ks if k.split("\t")[1] != k.split("\t")[2]} for s, ks in src.items()}


class Spy(E.Judge):
    """A judge that only notes which word pairs a table looks up."""
    def __init__(self):
        super().__init__()
        self.into = set()

    def verdict_by_key(self, k):
        self.into.add(k)
        return None, None


def parts(src):
    """{part of the tables: the word pairs it needs}, in the order they are judged: experiment 2's relation word
    (setting 0, 1, 2), Table 2, fine-tuning, then experiment 2's objects and the remaining words."""
    spy, out = Spy(), {}
    groups = [("experiment 2, setting 0 (its own answer): relation word", None, None),
              ("experiment 2, setting 1 (fresh): relation word", "fresh", "relation"),
              ("experiment 2, setting 2 (after its own answer): relation word", "answer", "relation")]
    for ds in DS_NAME:
        vids = PL.load(str(IC.OUT / "raw"), str(IC.RESULTS), ds)
        for name, ctx, what in groups + [("experiment 2, setting 1 (fresh): object", "fresh", "object"),
                                         ("experiment 2, setting 2 (after its own answer): object", "answer", "object")]:
            spy.into = out.setdefault(name, set())
            if ctx is None:
                setting0(spy, vids, ds)
            else:
                for k in (1, 5):
                    e2_counts(spy, vids, what, k, rows=[r for r in E2_ROWS if r[0] == ctx])
    order = [g for g, _, _ in groups] + list(src)[:2] + ["fine-tuning", "experiment 2, setting 1 (fresh): object",
                                                         "experiment 2, setting 2 (after its own answer): object"]
    out.update({s: src[s] for s in src if s != "experiment 2"})
    out = {g: {k for k in out[g] if k.split("\t")[1] != k.split("\t")[2]} for g in order}
    out["other words (older experiment 2 runs, extra top-5 words)"] = set().union(*src.values()) - set().union(*out.values())
    return out


def ft_models():
    return [m for m in S.NAMES if m == "traser" or (F.OUT / m).exists()]


def ft_sets():
    models = ft_models()
    for ds in ["vidor", "svg2test", "pvsg"]:
        have = [set(IC.answered(ds, S.root(m, F.OUT))) for m in models]
        vids = sorted(set.intersection(*have)) if have and len(models) > 1 else []
        if vids:
            yield ds, vids, models


# ----------------------------------------------------------------------------- asking
def key_from_env():
    from nim import nim_client
    try:
        return nim_client(timeout=TIMEOUT)
    except SystemExit:
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("NVIDIA key from build.nvidia.com (hidden, starts with nvapi-): ").strip()
        return nim_client(timeout=TIMEOUT)


def parse(reply, n):
    got = {int(x.get("i", -1)): str(x.get("category", "")).lower()
           for x in reply.get("results", []) if isinstance(x, dict) and str(x.get("i", "")).lstrip("-").isdigit()}
    return {i: c for i, c in got.items() if 0 <= i < n and c in E.CATEGORIES}


def request(client, model, part):
    """One request about `part` (judge keys): {key: category} for the ones it answered, or raises RuntimeError."""
    from nim import ask
    items = [{"i": n, "type": k.split("\t")[0], "reference": k.split("\t")[1], "predicted": k.split("\t")[2]}
             for n, k in enumerate(part)]
    reply = ask(client, model, [{"role": "user", "content": E.JUDGE_PROMPT % json.dumps(items)}], dict(SETTINGS),
                max_tokens=MAX_TOKENS)
    return {part[i]: c for i, c in parse(reply, len(part)).items()}


def test(client, model):
    from nim import ask
    print(f"testing {model} on 2 easy words (a thinking model can take a minute) ...", flush=True)
    for attempt in range(2):
        try:
            reply = ask(client, model, [{"role": "user", "content": E.JUDGE_PROMPT % json.dumps(TEST)}], dict(SETTINGS),
                        max_tokens=MAX_TOKENS, tries=1)
        except RuntimeError as e:
            if attempt:
                raise SystemExit(f"{model} does not answer: {str(e)[:300]}\n(python3 tools/rejudge.py --list shows the "
                                 "models your key can use)")
            continue
        got = parse(reply, 2)
        if got.get(0) not in (None, "mismatch") and got.get(1) == "mismatch":
            print("  ok: holding/grasping =", got[0], "| dog/table =", got[1], flush=True)
            return
    raise SystemExit(f"{model} answers, but wrongly on 2 easy words ({got}); choose another model")


def judge_all(judge, todo, client, workers):
    """Ask about every key in todo, `workers` requests at a time; saved after every answer. A failed or partial
    answer is asked again in halves (down to single words, 3 tries each); a rate limit waits a minute."""
    mine, tries = judge.mine(), {}
    queue = [todo[i:i + CHUNK] for i in range(0, len(todo), CHUNK)]
    t0, done, gave_up = time.time(), 0, []
    with cf.ThreadPoolExecutor(workers) as pool:
        running = {}
        while queue or running:
            while queue and len(running) < workers:
                part = queue.pop(0)
                running[pool.submit(request, client, judge.model, part)] = part
            fin, _ = cf.wait(running, return_when=cf.FIRST_COMPLETED)
            for f in fin:
                part = running.pop(f)
                try:
                    got, err = f.result(), ""
                except Exception as e:  # noqa: BLE001
                    got, err = {}, str(e)
                for codes, why in (FATAL):
                    if any(c in err for c in codes):
                        pool.shutdown(cancel_futures=True)
                        judge.save()
                        raise SystemExit(f"stopped: {why} ({err[:200]})")
                if any(c in err.lower() for c in ("429", "ratelimit", "rate limit", "too many requests")):
                    print("  rate limit: waiting a minute", flush=True)
                    time.sleep(60)
                    queue.insert(0, part)
                    continue
                mine.update(got)
                done += len(got)
                left = [k for k in part if k not in got]
                for k in left:
                    tries[k] = tries.get(k, 0) + 1
                left_ok = [k for k in left if tries[k] < 3]
                gave_up += [k for k in left if tries[k] >= 3]
                if len(left_ok) > 1:
                    queue += [left_ok[:len(left_ok) // 2], left_ok[len(left_ok) // 2:]]
                elif left_ok:
                    queue.append(left_ok)
                judge.save()
                rate = done / max(1e-9, time.time() - t0)
                rest = len(todo) - done - len(gave_up)
                print(f"  {done}/{len(todo)} judged" + (f", {len(left)} not answered this time" if left else "")
                      + f" | {time.strftime('%H:%M')} | about {rest / max(rate, 1e-9) / 60:.0f} min left", flush=True)
    if gave_up:
        print(f"{len(gave_up)} words got no answer in 3 tries; run the same command again to ask about them again")


# ----------------------------------------------------------------------------- agreement
def agreement(new, old):
    """On the words both judged (`old`, `new`: {key: category}): same right/wrong, and per side."""
    both = [k for k in new if k in old]
    acc = [k for k in both if E.is_right(old[k], "lenient")]
    rej = [k for k in both if not E.is_right(old[k], "lenient")]
    return dict(both=len(both), same=sum(E.is_right(old[k], "lenient") == E.is_right(new[k], "lenient") for k in both),
                accepted=len(acc), also_accepted=sum(E.is_right(new[k], "lenient") for k in acc),
                rejected=len(rej), also_rejected=sum(not E.is_right(new[k], "lenient") for k in rej),
                same_category=sum(old[k] == new[k] for k in both))


def check(judge, todo_all, n, workers):
    """Ask about n words Kimi K3 judged (half accepted, half rejected; fixed sample) and print the agreement."""
    import random
    kimi = E.Judge().cache
    have = sorted(k for k in set(todo_all) & set(kimi) if not UNNAMED.fullmatch(k.split("\t")[2]))
    rng = random.Random(0)
    acc = [k for k in have if E.is_right(kimi[k], "lenient")]
    rej = [k for k in have if not E.is_right(kimi[k], "lenient")]
    sample = rng.sample(acc, min(n // 2, len(acc))) + rng.sample(rej, min(n - n // 2, len(rej)))
    todo = [k for k in sample if k not in judge.mine()]
    if todo:
        client = key_from_env()
        test(client, judge.model)
        judge_all(judge, todo, client, workers)
    a = agreement({k: judge.mine()[k] for k in sample if k in judge.mine()}, kimi)
    print(f"\non {a['both']} words Kimi K3 judged: same right/wrong {a['same']} ({pct(a['same'], a['both'])}); "
          f"Kimi K3 accepted {a['accepted']}, {judge.model} accepts {a['also_accepted']} of them; "
          f"Kimi K3 rejected {a['rejected']}, {judge.model} rejects {a['also_rejected']} of them; "
          f"same category {a['same_category']}")
    print("(Claude on 200 such words: accepted 79 of Kimi K3's 100 accepted, rejected 98 of its 100 rejected)")
    diff = [k for k in sample if k in judge.mine() and E.is_right(kimi[k], "lenient") != E.is_right(judge.mine()[k], "lenient")]
    for k in diff[:15]:
        kind, ref, pred = k.split("\t")
        print(f"  {kind}: {ref} / {pred}: Kimi K3 {kimi[k]}, {judge.model} {judge.mine()[k]}")
    return 0


# ----------------------------------------------------------------------------- experiment 2
E2_ROWS = [("fresh", "all human pairs", "setting 1, all {n}"), ("fresh", "missed", "↳ missed {n}"),
           ("fresh", "written", "↳ written {n}"), ("fresh", "same", "setting 1 on the {n}"),
           ("answer", "missed", "setting 2, same {n}")]
INPUTS = [("clean", "with video"), ("zeros", "video blanked"), ("other_video", "other video")]
DS_NAME = {"pvsg": "PVSG", "svg2test": "SVG2test", "vidor": "VidOR"}


def setting0(judge, vids, ds):
    """(human pairs, pairs TRASER wrote in its own answer with a word the judge accepts for one of the human words)."""
    n = ok = 0
    for d, _ in vids:
        pred = E.parse_prediction(Path(IC.RESULTS, ds, "preds", f"{d['video']}.json").read_text())
        said = {}
        for s, w, o, _ in pred["relations"]:
            said.setdefault((s, o), []).append(w)
        for p in d.get("missed", []) + d.get("written", []):
            n += 1
            ok += any(E.is_right(judge.category("relation", h, w), "lenient") for w in said.get((p["s_k"], p["o_k"]), [])
                      for h in p["words"])
    return n, ok


def e2_counts(judge, vids, what, k, rows=None):
    """{row label: (pairs, {input: right})}, selected as pairs_lenient.table selects them; "same" = the missed pairs
    that setting 2 also tested (their answer was not cut off), asked fresh."""
    out = {}
    for ctx, group, label in rows or E2_ROWS:
        items = []
        for d, names in vids:
            pairs = d.get("missed", []) + d.get("written", []) if group == "all human pairs" else \
                d.get("missed" if group == "same" else group, [])
            for p in pairs:
                res = p.get(ctx, {})
                if not p.get("words") or not all(res.get(c, {}).get("top") for c, _ in PL.CONDS):
                    continue
                if group == "same" and not all(p.get("answer", {}).get(c, {}).get("top") for c, _ in PL.CONDS):
                    continue
                if what == "object" and not all("object_top" in res[c] for c, _ in PL.CONDS):
                    continue
                items.append((p, res, names))
        if not items:
            continue
        right = {}
        for c, _ in PL.CONDS:
            if what == "relation":
                st = [PL.rel_state(judge, p["words"], [t[0] for t in res[c]["top"]][:k]) for p, res, _ in items]
            else:
                st = [PL.obj_state(judge, p["o_k"], names, PL.object_picks(res[c], k)) for p, res, names in items]
            right[c] = st.count("right")
        out[label] = (len(items), right)
    return out


# ----------------------------------------------------------------------------- pages
def pct(a, b):
    return f"{100 * a / b:.0f}%" if b else "-"


def page(model, judge, old, src, left):
    n_all = len(set().union(*src.values()))
    L = [f"# Every word judged again by {model}", "",
         f"{n_all} different (human word, predicted word) pairs from the saved answers, all judged again by **{model}** "
         "alone, with the same judging as before and as the paper describes it (Sec. 5): the same prompt and five "
         "categories (identical, synonym, hypernym/hyponym, semantic overlap, mismatch), human label as the reference, "
         "temperature 0, 50 words per request; **lenient = anything but a mismatch**, relations also need **temporal IoU "
         "> 0.5**. The same text after normalising counts as identical without asking, and an object Qwen left unnamed "
         "(\"object 3\") as a mismatch, both as before. Only the judge model differs: "
         "the paper used GPT-4o-mini (prompt not released); the earlier tables used Kimi K3, and Claude for the words "
         "Kimi K3 never judged. Made by `tools/rejudge.py`; verdicts in "
         f"`results/traser_bench/{judge.other_path(model).name}`.", ""]
    if left:
        L += [f"**{left} words are not judged yet** (they count as wrong): run `python3 tools/rejudge.py --model {model}` "
              "again to finish.", ""]
    L += ["| words from | pairs |", "|---|---|"] + [f"| {s} | {len(ks)} |" for s, ks in src.items()] + [""]

    L += ["## How often it agrees with the earlier judges", "",
          "| earlier judge | words both judged | same right/wrong | earlier right → it says right too | "
          "earlier wrong → it says wrong too | same category |", "|---|---|---|---|---|---|"]
    mine = judge.mine()
    for name, verdicts in [("Kimi K3", old.cache)] + [(m, v) for m, v in old.other.items() if m != model]:
        a = agreement(mine, verdicts)
        if a["both"]:
            L.append(f"| {name} | {a['both']} | {a['same']} ({pct(a['same'], a['both'])}) | {a['also_accepted']} of "
                     f"{a['accepted']} ({pct(a['also_accepted'], a['accepted'])}) | {a['also_rejected']} of {a['rejected']} "
                     f"({pct(a['also_rejected'], a['rejected'])}) | {a['same_category']} ({pct(a['same_category'], a['both'])}) |")
    L += ["", "Each table below: **earlier judges → this model**.", ""]

    L += ["## Table 2 (lenient, temporal IoU > 0.5)", ""]
    loaded = Q.load(Q.DATASETS)
    res = {name: Q.scores(loaded, j) for name, j in (("old", old), ("new", judge))}
    dss = [ds for ds in Q.DATASETS if ds in loaded]
    head = ["triplet", "relation", "object"]
    L += ["| | " + " | ".join(f"{h} {ds}" for h in head for ds in dss) + " |", "|---|" + "---|" * (len(head) * len(dss))]
    idx = {ds: Q.DATASETS.index(ds) for ds in dss}
    L.append("| TRASER, paper | " + " | ".join(f"{Q.PAPER['TRASER, paper'][h][idx[ds]]}" for h in head for ds in dss) + " |")
    for m, name in (("traser", "TRASER, ours"), ("qwen7b", "Qwen-7B in TRASER's pipeline, ours")):
        L.append(f"| {name} | " + " | ".join(f"{res['old'][ds][m][h]} → **{res['new'][ds][m][h]}**" for h in head for ds in dss) + " |")
    L += [""]

    sets = list(ft_sets())
    if sets:
        L += ["## Fine-tuning (lenient, temporal IoU > 0.5)", "",
              "| dataset | model | videos | triplet | relation | object |", "|---|---|---|---|---|---|"]
        r = {name: S.score(ft_models(), [ds for ds, _, _ in sets], F.OUT, j, False) for name, j in (("old", old), ("new", judge))}
        for ds, vids, models in sets:
            for m in models:
                o, n = r["old"][ds][m]["lenient"], r["new"][ds][m]["lenient"]
                L.append(f"| {ds} | {S.NAMES[m]} | {len(vids)} | " + " | ".join(f"{o[h]} → **{n[h]}**" for h in head) + " |")
        L += [""]

    L += ["## Experiment 2 (TRASER fills in the relation word of a human pair)", "",
          "Setting 0: its own answer (the pair written, with a right word). Setting 1 (fresh): its own object list, no "
          "relations; every human pair of every video. Setting 2 (after its own answer): its relation list re-opened; "
          "the missed pairs of the answers that were not cut off. Each row: the same pairs with all three inputs. "
          "Every column of these tables, by the judge: [`PAIRS_LENIENT.md`](PAIRS_LENIENT.md).", ""]
    data = {ds: PL.load(str(IC.OUT / "raw"), str(IC.RESULTS), ds) for ds in DS_NAME if ds in IC.DATASETS}
    data = {ds: v for ds, v in data.items() if v}
    counts = {(ds, what, k, name): e2_counts(j, vids, what, k) for ds, vids in data.items()
              for what in ("relation", "object") for k in (1, 5) for name, j in (("old", old), ("new", judge))}
    L += ["### How much was tested", "", "| | videos | human pairs | missed | written | setting 2 |", "|---|---|---|---|---|---|"]
    for ds, vids in data.items():
        c = counts[(ds, "relation", 1, "new")]
        n = lambda label: c[label][0] if label in c else 0  # noqa: E731
        L.append(f"| {DS_NAME.get(ds, ds)} | {len(vids)} | {n('setting 1, all {n}'):,} | {n('↳ missed {n}'):,} | "
                 f"{n('↳ written {n}'):,} | {n('setting 2, same {n}'):,} |")
    L += [""]
    num = lambda a, b: f"{a:,} ({pct(a, b)})"  # noqa: E731
    for what, k, title in (("relation", 1, "Relation word: 1st choice right"), ("relation", 5, "Relation word: right word in its top 5"),
                           ("object", 1, "Object: 1st choice right"), ("object", 5, "Object: right object in its top 5")):
        L += [f"### {title}", "", "| | pairs | " + " | ".join(name for _, name in INPUTS) + " |", "|---|---|---|---|---|"]
        for ds, vids in data.items():
            o, n = counts[(ds, what, k, "old")], counts[(ds, what, k, "new")]
            first = f"**{DS_NAME.get(ds, ds)}**"
            if what == "relation" and k == 1:
                (cnt, a), (_, b) = setting0(old, vids, ds), setting0(judge, vids, ds)
                L.append(f"| {first} | setting 0, its own answer {cnt:,} | {num(a, cnt)} → **{num(b, cnt)}** | - | - |")
                first = ""
            for label, (cnt, right) in n.items():
                L.append(f"| {first} | {label.format(n=f'{cnt:,}')} | " + " | ".join(
                    f"{num(o[label][1][c], cnt)} → **{num(right[c], cnt)}**" for c, _ in INPUTS) + " |")
                first = ""
        L += [""]
    return "\n".join(L) + "\n"


def pairs_page(model, judge):
    """pairs_lenient.py's page, every table with this model's verdicts alone."""
    L = [f"# Experiment 2b, every word judged by {model}", "",
         "As `results/traser_bench/interp/PAIRS_LENIENT.md` (read it for what the columns mean), with every verdict "
         f"from {model} alone (`tools/rejudge.py`). Lenient: anything but a mismatch.", ""]
    for ds in IC.DATASETS:
        vids = PL.load(str(IC.OUT / "raw"), str(IC.RESULTS), ds)
        if not vids:
            continue
        n_pairs = sum(len(d.get("missed", [])) + len(d.get("written", [])) for d, _ in vids)
        L += [f"## {ds}: {len(vids)} videos, {n_pairs} human pairs", ""]
        for title, what, k in (("Relation word, TRASER's 1st choice", "relation", 1), ("Relation word, any of its top 5", "relation", 5),
                               ("Object, TRASER's 1st choice", "object", 1), ("Object, any of its top 5", "object", 5)):
            if what == "object" and not any('"object_top"' in json.dumps(d) for d, _ in vids):
                continue
            L += [f"### {title}", ""] + PL.table(judge, vids, what, k) + [""]
    return "\n".join(L) + "\n"


def write_pages(model, judge, src):
    old = E.Judge(others=True)                  # the published tables: Kimi K3, then Claude
    old.other = {m: v for m, v in old.other.items() if m in EARLIER}
    left = sum(1 for k in set().union(*src.values()) if k not in judge.mine())
    out = OUT / model.replace("/", "__")
    out.mkdir(parents=True, exist_ok=True)
    (out / "README.md").write_text(page(model, judge, old, src, left))
    (out / "PAIRS_LENIENT.md").write_text(pairs_page(model, judge))
    print(f"wrote {out / 'README.md'} and {out / 'PAIRS_LENIENT.md'}")


# ----------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--model", help="a model of build.nvidia.com, e.g. nvidia/<name> (see --list)")
    ap.add_argument("--list", nargs="?", const="", default=None, metavar="TEXT",
                    help="list the models your key can use (only names containing TEXT), and stop")
    ap.add_argument("--check", type=int, default=0, metavar="N",
                    help="only judge N words Kimi K3 judged (half it accepted, half it rejected) and show how often "
                         "the model agrees; they count for the full run too")
    ap.add_argument("--count", action="store_true", help="only count the words judged / left")
    ap.add_argument("--pages", action="store_true", help="only write the pages from the saved verdicts")
    ap.add_argument("--workers", type=int, default=4, help="requests at a time (default 4)")
    ap.add_argument("--max_tokens", type=int, default=MAX_TOKENS, help=f"cap on one reply (default {MAX_TOKENS})")
    args = ap.parse_args()
    globals()["MAX_TOKENS"] = args.max_tokens
    if args.list is not None:
        client = key_from_env()
        ids = sorted(m.id for m in client.models.list().data)
        shown = [m for m in ids if args.list.lower() in m.lower()]
        print(f"models your key can use{f' with {args.list!r} in the name' if args.list else ''}:\n  "
              + ("\n  ".join(shown) or "none"))
        print(f"({len(ids)} models in all; Kimi K3 = moonshotai/kimi-k3 was retired on 15 Oct 2026)")
        return 0
    if not args.model:
        ap.error("--model is needed (python3 tools/rejudge.py --list shows the models)")
    if args.model == E.JUDGES[0]:
        raise SystemExit(f"{args.model} made the earlier verdicts (and was retired); choose another model")
    src = words()
    todo_all = sorted(set().union(*src.values()))
    judge = Solo(args.model)
    judge.mine().update({k: "mismatch" for k in todo_all if UNNAMED.fullmatch(k.split("\t")[2])})
    groups = parts(src)
    first = {}
    for i, ks in enumerate(groups.values()):
        for k in ks:
            first.setdefault(k, i)
    todo = sorted((k for k in todo_all if k not in judge.mine()), key=lambda k: (first.get(k, len(groups)), k))
    print(f"{len(todo_all) - len(todo)} of {len(todo_all)} word pairs judged by {args.model}, {len(todo)} left "
          f"({-(-len(todo) // CHUNK)} requests of {CHUNK} words). By part, in the order they are judged:")
    for g, ks in groups.items():
        done = sum(k in judge.mine() for k in ks)
        print(f"  {g}: {done} of {len(ks)}" + (" (all judged)" if done == len(ks) else ""))
    if args.count:
        return 0
    if args.check:
        return check(judge, todo_all, args.check, args.workers)
    if todo and not args.pages:
        client = key_from_env()
        test(client, args.model)
        try:
            judge_all(judge, todo, client, args.workers)
        except KeyboardInterrupt:
            judge.save()
            raise SystemExit("\nstopped; every answer so far is saved: run the same command again to continue")
    write_pages(args.model, judge, src)
    return 0


if __name__ == "__main__":
    sys.exit(main())
