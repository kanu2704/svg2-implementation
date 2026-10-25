"""Slide figures for experiment 2b (every human pair): setting 1 (fresh), setting 2 (after its own answer), the 3 inputs.

    python3 tools/interp/exp2_setup_figs.py results/traser_bench/interp/figs
"""
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = sys.argv[1]
OBJ = [("1 person", "#5B7FCF"), ("2 cup", "#6AAE96"), ("3 table", "#B07CC6"), ("4 dog", "#E0A050")]
GRAY, DARK, MONO = "#666666", "#1F2937", "DejaVu Sans Mono"


def box(ax, x, y, w, h, fc, ec="none", lw=1.2, r=0.012):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc, ec=ec, lw=lw))


def objects(ax, y, colors=None, labels=None, x0=0.02, w=0.083, h=0.075, txt="white"):
    for i, (name, c) in enumerate(OBJ):
        x = x0 + i * (w + 0.004)
        box(ax, x, y, w, h, (colors or {}).get(i, c), r=0.004)
        ax.text(x + w / 2, y + h / 2, (labels or {}).get(i, name), color=txt, ha="center", va="center", fontsize=11.5, weight="bold")
    return x0 + 4 * (w + 0.004)


def figure(title, subtitle, answer_pre, answer_post, cap_left, cap_right, score1, score2, note, path):
    fig = plt.figure(figsize=(15, 5.6), dpi=150)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    fig.patch.set_facecolor("white")
    ax.text(0.02, 0.93, title, fontsize=19, weight="bold", color=DARK, va="center")
    ax.text(0.02, 0.855, subtitle, fontsize=12, color=GRAY, va="center")
    ax.text(0.02, 0.765, "what TRASER reads:", fontsize=12, color=GRAY, va="center")
    y, h = 0.60, 0.085
    xe = objects(ax, y, h=h)
    ax.text(0.02 + (xe - 0.02) / 2, y - 0.06, "video (each object's tokens)", fontsize=11, color=GRAY, ha="center")
    box(ax, xe + 0.008, y, 0.135, h, "#F1F2F4", ec="#C9CDD3")
    ax.text(xe + 0.008 + 0.0675, y + h / 2, "question (prompt)", fontsize=12, ha="center", va="center", color="#333333")
    ax0 = xe + 0.155
    box(ax, ax0, y, 0.98 - ax0, h, "white", ec="#C9CDD3")
    t = ax.text(ax0 + 0.01, y + h / 2, answer_pre, fontsize=11.5, family=MONO, va="center", color="#333333")
    fig.canvas.draw()
    bb = t.get_window_extent().transformed(ax.transData.inverted())
    bx = bb.x1 + 0.006
    box(ax, bx, y + 0.012, 0.075, h - 0.024, "#FFF4B8", ec="#E3B23C", lw=1.6, r=0.003)
    ax.text(bx + 0.0375, y + h / 2 - 0.006, "_____", fontsize=12, ha="center", va="center", color="#333333")
    ax.text(bx + 0.081, y + h / 2, answer_post, fontsize=11.5, family=MONO, va="center", color="#333333")
    ax.text(ax0 + 0.01 + (bb.x1 - ax0 - 0.01) / 2, y - 0.06, cap_left, fontsize=11, color=GRAY, ha="center")
    for i, line in enumerate(cap_right.split("\n")):
        ax.text(bx + 0.0375, y - 0.06 - 0.05 * i, line, fontsize=11, color=GRAY, ha="center")
    box(ax, 0.02, 0.10, 0.96, 0.28, "#FFFCF2", ec="#E3B23C", lw=2, r=0.02)
    ax.text(0.04, 0.30, score1, fontsize=12.5, color="#333333", va="center")
    ax.text(0.04, 0.215, score2, fontsize=13, color="#111111", weight="bold", va="center")
    ax.text(0.04, 0.14, note, fontsize=12, color="#B45309", va="center", weight="bold")
    fig.savefig(path, facecolor="white")
    plt.close(fig)


SUB = 'Video: person, cup, table, dog. Humans: "person holding cup" (TRASER wrote it) and "person petting dog" (TRASER missed it). Illustrative.'
S1 = "We score the dataset's common relation words in the blank (PVSG 66, SVG2test 55, VidOR 74: holding, petting, next to, on, ...)."
S2 = 'Question: is the human word "petting" (or a word with the same meaning) TRASER\'s 1st choice? In its top 5?'
figure("Experiment 2b, setting 1 (fresh): TRASER fills in the word for every human pair", SUB,
       '{"objects": [...], "relationships": [[1, "', '", 4, [[',
       "its own object list, no relations", "+ we write: subject 1 (person)\nand object 4 (dog)", S1, S2,
       "Every human pair of every video: the missed ones AND the ones TRASER wrote (nothing to copy from).",
       f"{OUT}/exp2b_setting1_fresh.png")
figure("Experiment 2b, setting 2: we start the missed relation after its own answer", SUB,
       '[1, "holding", 2, [[0, 40]]], [1, "', '", 4, [[',
       "its own answer so far", "+ we write: subject 1 (person)\nand object 4 (dog)", S1, S2,
       "Every missed human pair (the written ones are already in its answer), in every video whose list ended.",
       f"{OUT}/exp2b_setting2_after_answer.png")

# the three inputs
fig = plt.figure(figsize=(15, 5.6), dpi=150)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
ax.text(0.02, 0.93, "Experiment 2b: the same question, three inputs", fontsize=19, weight="bold", color=DARK, va="center")
ax.text(0.02, 0.855, "Only the video tokens change; the prompt, the object numbers, the time labels and the question stay the same.",
        fontsize=12, color=GRAY, va="center")
rows = [("with video", None, None, "white", "the real tokens of each object"),
        ("other video's input", {0: "#9AA5B1", 1: "#8C9AA8", 2: "#A3ADB8", 3: "#95A1AD"},
         {0: "1 (other obj)", 1: "2 (other obj)", 2: "3 (other obj)", 3: "4 (other obj)"}, "white",
         "each object's tokens replaced by an object of another video:\nnormal-looking tokens, wrong content"),
        ("video blanked", {i: "#E5E7EB" for i in range(4)}, {i: f"{i + 1}  (zeros)" for i in range(4)}, "#6B7280",
         "every video token set to zero: nothing to see, only habit")]
for k, (name, col, lab, txt, expl) in enumerate(rows):
    y = 0.64 - k * 0.2
    ax.text(0.02, y + 0.04, name, fontsize=13, weight="bold", color=DARK, va="center")
    xe = objects(ax, y, colors=col, labels=lab, x0=0.2, txt=txt)
    ax.text(xe + 0.02, y + 0.04, expl, fontsize=12, color="#333333", va="center")
ax.text(0.02, 0.06, "Same answer start in all three: e.g. {\"objects\": [...], \"relationships\": [[1, \"_____\", 4, [[",
        fontsize=12, family=MONO, color=GRAY, va="center")
fig.savefig(f"{OUT}/exp2b_inputs.png", facecolor="white")
plt.close(fig)
print("ok")
