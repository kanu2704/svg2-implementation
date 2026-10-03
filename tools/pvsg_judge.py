"""Lenient scoring for the PVSG evaluation: an LLM judge says how our open-vocabulary label relates
to the human label, like the SVG2 paper's semantic aligner (Sec. 5, five categories), with "broader"
and "narrower" kept apart.

    identical | synonym | broader | narrower | related | mismatch

close   = identical, synonym, broader, narrower   (the same thing named at another level of detail)
lenient = close + related                          (the paper's lenient score: everything but mismatch)
"""
import json

from pvsg_pipeline import ask, nim_client  # noqa: F401  (nim_client re-exported for the notebook)

CATEGORIES = ["identical", "synonym", "broader", "narrower", "related", "mismatch"]
CLOSE = {"identical", "synonym", "broader", "narrower"}
LENIENT = CLOSE | {"related"}

JUDGE_PROMPT = """You compare labels from an automatic video annotator with the labels human annotators gave to
the same object (or the same relation between two objects).
For each item, say how the PREDICTED label relates to the REFERENCE label:
- "identical": the same word or trivially the same (plural, spelling, word order)
- "synonym": a different word with the same meaning (person / human, couch / sofa, on top of / on)
- "broader": the predicted label is a more general term (plant for tree, vehicle for car, near for next to)
- "narrower": the predicted label is a more specific term (baby for child, sedan for car, grasping for holding)
- "related": overlapping meaning but neither of the above (countertop for table, tablecloth for table)
- "mismatch": a different thing (child for grass, car for ground, football for adult)
Judge the labels only. Answer only with JSON: {"results": [{"i": <item number>, "category": "<one of the six>"}]}

ITEMS: %s"""


def judge(client, model, pairs, chunk=60):
    """pairs: list of (kind, reference, predicted) -> list of categories (same order)."""
    out = ["mismatch"] * len(pairs)
    cache = {}
    todo = []
    for i, (kind, ref, pred) in enumerate(pairs):
        key = (kind, str(ref).strip().lower(), str(pred).strip().lower())
        if key[1] == key[2]:
            out[i] = "identical"
        elif key in cache:
            cache[key].append(i)
        else:
            cache[key] = [i]
            todo.append(key)
    for start in range(0, len(todo), chunk):
        part = todo[start:start + chunk]
        items = [{"i": n, "type": k, "reference": r, "predicted": p} for n, (k, r, p) in enumerate(part)]
        reply = ask(client, model, [{"role": "user", "content": JUDGE_PROMPT % json.dumps(items)}],
                    dict(temperature=0.0), max_tokens=4096)
        got = {int(x.get("i", -1)): x.get("category") for x in reply.get("results", []) if isinstance(x, dict)}
        for n, key in enumerate(part):
            cat = got.get(n) if got.get(n) in CATEGORIES else "mismatch"
            for i in cache[key]:
                out[i] = cat
    return out
