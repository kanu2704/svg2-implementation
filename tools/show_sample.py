"""Phase 1.5: look at one training sample with your own eyes.

Reads an annotation file written by the official converter (traser/data/prepare_svg2.py),
then draws:
  - a few video frames with every object's mask overlaid in its own colour, labelled
    "N: name" (N = the object's id in the annotation, i.e. its column in the mask file);
  - a timeline of the relations (one bar per span, in seconds);
and writes a companion Markdown file with the objects, attributes and relations as text.

    python tools/show_sample.py --ann data/traser/svg2_pvd.json --index 0
    python tools/show_sample.py --ann data/traser/svg2_pvd.json --video_id 103151160
"""
import argparse
import colorsys
import json
import os

import cv2
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from decord import VideoReader
from pycocotools import mask as mask_utils


def colours(n):
    return [tuple(int(255 * c) for c in colorsys.hsv_to_rgb(i / max(n, 1), 0.85, 1.0)) for i in range(n)]


def load_entry(args):
    with open(args.ann) as f:
        entries = json.load(f)
    if args.video_id:
        for e in entries:
            if os.path.splitext(os.path.basename(e["video"]))[0] == args.video_id:
                return e
        raise SystemExit(f"{args.video_id} not in {args.ann}")
    return entries[args.index]


def decode(rle, h, w):
    """Absent objects are stored as all-zero RLEs; check the area before decoding (dataset card)."""
    if not rle or mask_utils.area(rle) == 0:
        return None
    m = mask_utils.decode(rle)
    if m.ndim == 3:
        m = m[:, :, 0]
    if m.shape != (h, w):
        m = cv2.resize(m, (w, h), interpolation=cv2.INTER_NEAREST)
    return m.astype(bool)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ann", default="data/traser/svg2_pvd.json")
    ap.add_argument("--index", type=int, default=0)
    ap.add_argument("--video_id", default=None)
    ap.add_argument("--frames", type=int, default=4)
    ap.add_argument("--out_dir", default="notes/figs")
    args = ap.parse_args()

    e = load_entry(args)
    vid = os.path.splitext(os.path.basename(e["video"]))[0]
    prompt = e["conversations"][0]["value"].split("\n")[0]
    target = json.loads(e["conversations"][1]["value"])
    objects = target.get("objects", [])
    rels = target.get("relationships", [])
    names = {}
    for ob in objects:
        key = next(k for k in ob if k.startswith("object_"))
        names[int(key.split("_")[1])] = ob[key]

    with open(e["mask_json"]) as f:
        masks = json.load(f)
    vr = VideoReader(e["video"])
    fps = vr.get_avg_fps()
    n_frames = min(len(vr), len(masks))
    frame_ids = np.linspace(0, n_frames - 1, args.frames).astype(int)
    frames = vr.get_batch(frame_ids).asnumpy()
    h, w = frames.shape[1:3]
    obj_ids = e["obj_list"]
    cols = dict(zip(obj_ids, colours(len(obj_ids))))

    n_rel_rows = min(len(rels), 30)
    fig = plt.figure(figsize=(4 * args.frames, 4.2 + 0.25 * max(n_rel_rows, 4)))
    grid = fig.add_gridspec(2, args.frames, height_ratios=[3, 0.25 * max(n_rel_rows, 4) + 0.5])
    for k, (fid, img) in enumerate(zip(frame_ids, frames)):
        canvas = img.astype(np.float32)
        labels = []
        for oid in obj_ids:
            m = decode(masks[fid][oid] if oid < len(masks[fid]) else None, h, w)
            if m is None:
                continue
            canvas[m] = 0.5 * canvas[m] + 0.5 * np.array(cols[oid], dtype=np.float32)
            ys, xs = np.nonzero(m)
            labels.append((xs.mean(), ys.mean(), f"{oid}: {names.get(oid, '?')}", cols[oid]))
        ax = fig.add_subplot(grid[0, k])
        ax.imshow(canvas.astype(np.uint8))
        for x, y, text, c in labels:
            ax.text(x, y, text, fontsize=7, color="black", ha="center",
                    bbox=dict(facecolor=np.array(c) / 255, alpha=0.8, pad=1, lw=0))
        ax.set_title(f"frame {fid}  (t = {fid / fps:.1f} s)", fontsize=9)
        ax.axis("off")

    ax = fig.add_subplot(grid[1, :])
    duration = len(vr) / fps
    for row, r in enumerate(rels[:n_rel_rows]):
        s_id, pred, o_id, spans = r[0], r[1], r[2], r[3]
        colour = np.array(cols.get(s_id, (128, 128, 128))) / 255
        for s, t in spans:
            ax.barh(row, (t + 1) - s, left=s, color=colour, height=0.7)  # [s, t] inclusive seconds
        sname = "camera" if s_id == -1 else names.get(s_id, "?")
        oname = "camera" if o_id == -1 else names.get(o_id, "?")
        ax.text(0.2, row, f"{s_id}:{sname}  {pred}  {o_id}:{oname}", va="center", fontsize=7)
    ax.set_xlim(0, max(duration, 1))
    ax.set_ylim(-0.5, max(n_rel_rows, 1) - 0.5)
    ax.invert_yaxis()
    ax.set_yticks([])
    ax.set_xlabel("seconds (bars drawn with the training convention: [s, e] inclusive = s … e+1)")
    ax.set_title(f"{len(rels)} relations (first {n_rel_rows} shown)", fontsize=9)
    fig.suptitle(f"{vid} — {len(objects)} objects, {duration:.1f} s @ {fps:.1f} fps — prompt: {prompt}", fontsize=10)
    fig.tight_layout()

    os.makedirs(args.out_dir, exist_ok=True)
    png = os.path.join(args.out_dir, f"sample_{vid}.png")
    fig.savefig(png, dpi=70)

    md = [f"# Sample {vid}", "", f"![]({os.path.basename(png)})", "",
          f"- video: {duration:.1f} s, {len(vr)} frames @ {fps:.2f} fps; mask frames: {len(masks)}",
          f"- prompt: `{prompt}`", "", "## Objects", "", "| id | label | attributes |", "|---|---|---|"]
    for ob in objects:
        key = next(k for k in ob if k.startswith("object_"))
        md.append(f"| {key.split('_')[1]} | {ob[key]} | {', '.join(ob.get('attributes', []))} |")
    md += ["", "## Relations", "", "| subject | predicate | object | spans (s) |", "|---|---|---|---|"]
    for r in rels:
        sname = "camera" if r[0] == -1 else names.get(r[0], "?")
        oname = "camera" if r[2] == -1 else names.get(r[2], "?")
        md.append(f"| {r[0]}: {sname} | {r[1]} | {r[2]}: {oname} | {r[3]} |")
    with open(os.path.join(args.out_dir, f"sample_{vid}.md"), "w") as f:
        f.write("\n".join(md) + "\n")
    print(f"wrote {png} and sample_{vid}.md")


if __name__ == "__main__":
    main()
