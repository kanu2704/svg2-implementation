"""Interpretability, probes (CPU): where in TRASER is the information about relations, contact, motion and time?

A probe is a small logistic-regression classifier trained on TRASER's internal vectors. If it predicts a property
on videos it was not trained on (5-fold, split by video), the vectors at that stage carry that property.
The same questions are asked at every stage, so a drop shows where the information is lost:

    vision  the vision encoder + merger tokens of the object (mean)        (encode_stage feats)
    otr     the 32 OTR latents (mean)        twr  the TWR latents (mean over the object's windows)
    lm_L    the language model's hidden states over the object's latents, after layer L   (lm_stage p1)

Questions (labels from the human annotation, the masks, or TRASER's answer):
    pair  related   do humans relate subject -> object?          pair  touch    do the two masks touch?
    pair  action    (related pairs) any action word, or only position words?
    pair  written   did TRASER write this pair?
    obj   in_human  is the object in any human relation?         obj   moving   fast vs slow box centre (top vs bottom third)
    win   active    (human-related pairs, windows both are in) is the relation happening in this 4-second window?

Pair features are [a, b, a*b] of the two objects' vectors (each reduced to 64 numbers by PCA). Score: ROC AUC
(0.5 = chance, 1 = perfect). Controls: the same probe on shuffled labels, and a probe on geometry only
(time on screen together, gap, touching, sizes, motion, tokens kept, person/animal).

    python3 tools/interp/probe.py --work /kaggle/tmp/interp_work      -> results/traser_bench/interp/probes.json
"""
import argparse
import collections
import json
import random
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent))
from interp import common as C  # noqa: E402


def log(msg):
    print(f"{time.strftime('%H:%M:%S')} [probe] {msg}", flush=True)


def lm_layers(n_layers):
    return sorted({int(x) for x in np.linspace(0, n_layers, 13).round()})


def load_video(ds, v, work, results):
    import bench_eval as E
    import error_analysis as A
    p = C.work_paths(work, ds, v)
    if not (p["layout"].exists() and p["feats"].exists()):
        return None
    lay = C.read_json(p["layout"])
    f = np.load(p["feats"])
    hid = np.load(p["hidden"]) if p["hidden"].exists() else None
    gt = C.read_json(Path(results, ds, "gt", f"{v}.json"))
    pred = E.parse_prediction(Path(results, ds, "preds", f"{v}.json").read_text())
    gids = lay["gt_ids"]
    n = len(gids)
    win_mask = f["win_mask"]
    twr_mean = np.stack([f["twr_win"][i][win_mask[i]].astype(np.float32).mean(0) if win_mask[i].any()
                         else np.zeros(f["twr_win"].shape[-1], np.float32) for i in range(n)])
    stages = {"vision": f["vis_obj"].astype(np.float32), "otr": f["otr"].astype(np.float32), "twr": twr_mean}
    win_stages = {"vision": f["vis_win"].astype(np.float32), "twr": f["twr_win"].astype(np.float32)}
    if hid is not None:
        for l in lm_layers(hid["obj_mean"].shape[1] - 1):
            stages[f"lm_{l:02d}"] = hid["obj_mean"][:, l].astype(np.float32)
        for j, l in enumerate(hid["win_layers"].tolist()):
            win_stages[f"lm_{int(l):02d}"] = hid["win"][:, :, j].astype(np.float32)
    names = {o["gt_id"]: o["name"] for o in gt["objects"]}
    human = collections.defaultdict(list)
    for r in gt["relations"]:
        human[(r["subj"], r["obj"])].append(r)
    k_to_gid = {k + 1: g for k, g in enumerate(gids)}
    written = {(k_to_gid.get(s), k_to_gid.get(o)) for s, _, o, _ in pred["relations"]}
    unit = lay["seconds_per_frame"] if gt["time_unit"] != "index" else 1.0   # human spans -> TRASER's time index
    geo = lay["geometry"]
    return {"ds": ds, "v": v, "gids": gids, "n": n, "stages": stages, "win_stages": win_stages, "win_mask": win_mask,
            "human": human, "written": written, "names": names, "unit": unit, "geo": geo,
            "tokens": lay["tokens_per_object"], "is_position": A.is_position, "is_living": A.is_living}


def samples(V, rng, neg_ratio=10):
    """Pair, object and window samples of one video: (indices, labels per question)."""
    n, gids = V["n"], V["gids"]
    pairs, objs, wins = [], [], []
    in_human = {g for p in V["human"] for g in p}
    pos = [(i, j) for i in range(n) for j in range(n) if i != j and (gids[i], gids[j]) in V["human"]]
    neg = [(i, j) for i in range(n) for j in range(n) if i != j and (gids[i], gids[j]) not in V["human"]]
    neg = rng.sample(neg, min(len(neg), neg_ratio * max(1, len(pos))))
    for i, j in pos + neg:
        a, b = gids[i], gids[j]
        rel = V["human"].get((a, b), [])
        gp = V["geo"]["pairs"].get(",".join(str(x) for x in sorted((a, b))), {})
        pairs.append({"i": i, "j": j, "related": int(bool(rel)),
                      "action": (int(any(not V["is_position"](r["pred"]) for r in rel)) if rel else None),
                      "touch": (int(gp.get("touch_s", 0) > 0) if gp.get("co_s", 0) > 0 else None),
                      "written": int((a, b) in V["written"]), "geo": gp})
    speeds = [V["geo"]["motion"].get(str(g), {}).get("speed") for g in gids]
    for i in range(n):
        objs.append({"i": i, "in_human": int(gids[i] in in_human), "speed": speeds[i]})
    W = V["win_mask"].shape[1]
    for (a, b), rels in V["human"].items():
        if a not in gids or b not in gids:
            continue
        i, j = gids.index(a), gids.index(b)
        active = set()
        for r in rels:
            for s, e in r["spans"]:
                s, e = s / V["unit"], e / V["unit"]
                active |= set(range(int(s // C.WINDOW_S), int(max(s, e - 1e-6) // C.WINDOW_S) + 1))
        for w in range(W):
            if V["win_mask"][i, w] and V["win_mask"][j, w]:
                wins.append({"i": i, "j": j, "w": w, "active": int(w in active)})
    return pairs, objs, wins


def auc_cv(X, y, groups, seed=0):
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import roc_auc_score
    from sklearn.model_selection import GroupKFold
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    y = np.asarray(y)
    if len(set(y.tolist())) < 2 or len(set(groups)) < 3 or min(np.bincount(y)) < 5:
        return None, None
    oof = np.zeros(len(y))
    for tr, te in GroupKFold(n_splits=min(5, len(set(groups)))).split(X, y, groups):
        if len(set(y[tr].tolist())) < 2:
            return None, None
        clf = make_pipeline(StandardScaler(), LogisticRegression(C=0.5, max_iter=2000, class_weight="balanced"))
        clf.fit(X[tr], y[tr])
        oof[te] = clf.predict_proba(X[te])[:, 1]
    return round(float(roc_auc_score(y, oof)), 4), oof


def reduce(videos, stage, key, dims=64, seed=0):
    """PCA (fit on all objects / windows of the dataset) -> per video arrays of `dims` numbers."""
    from sklearn.decomposition import PCA
    if key == "obj":
        mats = [V["stages"][stage] for V in videos]
        allx = np.concatenate(mats)
    else:
        mats = [V["win_stages"][stage] for V in videos]
        allx = np.concatenate([m[V["win_mask"]] for m, V in zip(mats, videos)])
    allx = np.nan_to_num(allx)
    pca = PCA(n_components=min(dims, allx.shape[0] - 1, allx.shape[1]), random_state=seed).fit(allx)
    if key == "obj":
        return [pca.transform(np.nan_to_num(m)) for m in mats]
    return [pca.transform(np.nan_to_num(m.reshape(-1, m.shape[-1]))).reshape(m.shape[0], m.shape[1], -1) for m in mats]


def geo_features(V, p):
    gp, gids = p["geo"], V["gids"]
    m = V["geo"]["motion"]
    o = V["geo"]["objects"]
    a, b = gids[p["i"]], gids[p["j"]]
    sp = lambda g: (m.get(str(g), {}).get("speed") or 0.0)  # noqa: E731
    return [gp.get("co_s", 0.0), gp.get("gap", 1.0) if gp.get("gap") is not None else 1.0, gp.get("touch_s", 0.0),
            o.get(str(a), {}).get("area", 0.0), o.get(str(b), {}).get("area", 0.0), sp(a), sp(b),
            np.log1p(V["tokens"][p["i"]]), np.log1p(V["tokens"][p["j"]]),
            float(V["is_living"](V["names"].get(a, ""))), float(V["is_living"](V["names"].get(b, ""))), V["n"]]


def run_dataset(ds, videos, seed=0):
    rng = random.Random(seed)
    per = [samples(V, rng) for V in videos]
    stages = [s for s in videos[0]["stages"] if all(s in V["stages"] for V in videos)]
    win_stages = [s for s in videos[0]["win_stages"] if all(s in V["win_stages"] for V in videos)]
    res = {"videos": len(videos), "stages": stages, "window_stages": win_stages, "auc": collections.defaultdict(dict),
           "n": {}, "controls": {}, "knows": {}}
    best_related = (None, -1, None)
    for st in stages:
        Z = reduce(videos, st, "obj", seed=seed)
        X, groups, rows = [], [], []
        for vi, (V, (pairs, _, _)) in enumerate(zip(videos, per)):
            for p in pairs:
                a, b = Z[vi][p["i"]], Z[vi][p["j"]]
                X.append(np.concatenate([a, b, a * b]))
                groups.append(vi)
                rows.append(p)
        X = np.asarray(X)
        for task in ("related", "action", "touch", "written"):
            keep = [k for k, r in enumerate(rows) if r[task] is not None]
            auc, oof = auc_cv(X[keep], [rows[k][task] for k in keep], [groups[k] for k in keep], seed)
            res["auc"][task][st] = auc
            res["n"][task] = [len(keep), int(sum(rows[k][task] for k in keep))]
            if task == "related" and auc is not None and auc > best_related[1]:
                best_related = (st, auc, (oof, [rows[k] for k in keep], X[keep], [groups[k] for k in keep]))
        # objects
        Xo, yo, go, ys, gs = [], [], [], [], []
        speeds = [o["speed"] for _, objs, _ in per for o in objs if o["speed"] is not None]
        lo, hi = (np.percentile(speeds, 33), np.percentile(speeds, 67)) if speeds else (0, 0)
        for vi, (_, objs, _) in enumerate(per):
            for o in objs:
                Xo.append(Z[vi][o["i"]])
                yo.append(o["in_human"])
                go.append(vi)
                if o["speed"] is not None and (o["speed"] <= lo or o["speed"] >= hi):
                    ys.append((len(Xo) - 1, int(o["speed"] >= hi)))
        Xo = np.asarray(Xo)
        res["auc"]["in_human"][st], _ = auc_cv(Xo, yo, go, seed)
        res["n"]["in_human"] = [len(yo), int(sum(yo))]
        if ys:
            idx = [k for k, _ in ys]
            res["auc"]["moving"][st], _ = auc_cv(Xo[idx], [y for _, y in ys], [go[k] for k in idx], seed)
            res["n"]["moving"] = [len(ys), int(sum(y for _, y in ys))]
    for st in win_stages:
        Z = reduce(videos, st, "win", seed=seed)
        X, y, g = [], [], []
        for vi, (_, _, wins) in enumerate(per):
            for w in wins:
                a, b = Z[vi][w["i"], w["w"]], Z[vi][w["j"], w["w"]]
                X.append(np.concatenate([a, b, a * b]))
                y.append(w["active"])
                g.append(vi)
        if X:
            res["auc"]["active"][st], _ = auc_cv(np.asarray(X), y, g, seed)
            res["n"]["active"] = [len(y), int(sum(y))]
    # controls and "knows but doesn't say" at the best stage for "related"
    st, auc, pack = best_related
    if pack is not None:
        oof, rows, X, groups = pack
        y = np.array([r["related"] for r in rows])
        shuffled = y.copy()
        np.random.default_rng(seed).shuffle(shuffled)
        res["controls"]["shuffled_labels"] = {"stage": st, "auc": auc_cv(X, shuffled.tolist(), groups, seed)[0]}
        G = np.asarray([geo_features(videos[gi], r) for r, gi in zip(rows, groups)], dtype=np.float32)
        res["controls"]["geometry_only"] = {"auc": auc_cv(G, y.tolist(), groups, seed)[0]}
        res["controls"]["geometry_plus_best_stage"] = {"stage": st, "auc": auc_cv(np.concatenate([G, X], 1), y.tolist(), groups, seed)[0]}
        thr = float(np.percentile(oof[y == 0], 90))
        missed = [o for o, r in zip(oof, rows) if r["related"] and not r["written"]]
        wrote = [o for o, r in zip(oof, rows) if r["related"] and r["written"]]
        res["knows"] = {"stage": st, "auc": auc, "threshold_90pct_of_unrelated": round(thr, 4),
                        "missed_pairs": len(missed), "missed_above": round(float(np.mean([m > thr for m in missed])), 4) if missed else None,
                        "written_pairs": len(wrote), "written_above": round(float(np.mean([m > thr for m in wrote])), 4) if wrote else None}
    res["auc"] = {k: dict(v) for k, v in res["auc"].items()}
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True)
    ap.add_argument("--results", default=str(C.RESULTS))
    ap.add_argument("--out", default=str(C.OUT))
    ap.add_argument("--datasets", nargs="+", default=C.DATASETS)
    ap.add_argument("--n", type=json.loads, default={})
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    import bench_eval as E
    E.RESULTS = Path(args.results)
    out = C.read_json(Path(args.out) / "probes.json", {})     # the datasets not run this time stay as they are
    for ds in args.datasets:
        vids = C.select_videos(ds, args.n.get(ds), args.seed, args.results)
        videos = [V for V in (load_video(ds, v, args.work, args.results) for v in vids) if V is not None]
        have_lm = sum("lm_00" in V["stages"] for V in videos)
        if len(videos) < 5:
            log(f"{ds}: only {len(videos)} encoded videos, skipped")
            continue
        if have_lm < len(videos):
            videos = [V for V in videos if "lm_00" in V["stages"]] if have_lm >= 5 else [
                dict(V, stages={k: s for k, s in V["stages"].items() if not k.startswith("lm_")},
                     win_stages={k: s for k, s in V["win_stages"].items() if not k.startswith("lm_")}) for V in videos]
        t0 = time.time()
        log(f"{ds}: {len(videos)} videos ...")
        out[ds] = run_dataset(ds, videos, args.seed)
        log(f"{ds}: done in {time.time() - t0:.0f} s; related: " + ", ".join(
            f"{k} {v}" for k, v in out[ds]["auc"].get("related", {}).items()))
    C.write_json(Path(args.out) / "probes.json", out)
    log(f"wrote {Path(args.out) / 'probes.json'}")


if __name__ == "__main__":
    main()
