"""TRASER's Table 2 baseline N times on Kaggle (2 x T4), with the paper's official settings (tools/bench_run.py: released
UWGZQ/TRASER, 1 fps, at most 128 frames, at most 40 objects, coverage 0.5, 4 s windows, greedy decoding), on the same
videos as the published run. For a terminal in the Kaggle session (e.g. VS Code through a tunnel). Each run's answers
go to results/traser_repeats/run<k>/<dataset>/ and are pushed to GitHub every 20 minutes, so a session that ends loses
at most 20 minutes of work; in the next session run the same commands and it continues where it stopped.

    git clone -b claude/traser-interpretability https://github.com/kanu2704/svg2-implementation /kaggle/working/svg2-implementation
    cd /kaggle/working/svg2-implementation
    read -s SVG2_GH_TOKEN && export SVG2_GH_TOKEN          # GitHub token, typed hidden (needed to push)
    REPEAT_DATASETS=pvsg nohup python3 notebooks/traser_repeat_kaggle.py >> /kaggle/working/repeat.log 2>&1 &
    tail -f /kaggle/working/repeat.log

REPEAT_DATASETS   pvsg, vidor, svg2test, comma-separated, in that order (default: pvsg,svg2test,vidor)
REPEAT_RUNS       how many runs (default 3)
REPEAT_LM         traser (default) or traser_meanpool (TRASER with its two resamplers replaced by plain averaging)
REPEAT_OUT        where the answers go (default results/traser_repeats; results/<REPEAT_LM> for another model)
SAV_LINKS         SVG2test: path of Meta's SA-V links file (uploaded to the session), for its 33 SA-V videos;
                  without it only the 67 VSPW videos run
VSPW_DIR          SVG2test: a folder with your own copy of VSPW (VSPW_data.tar_aa ... or one archive), if Google Drive
                  refuses the download; otherwise it is downloaded (full resolution, ~43 GB)

Scores afterwards (anywhere, NVIDIA key): python3 tools/repeat_report.py. On the server the same runs are made by
notebooks/traser_repeat_run.py (there the data is already prepared).
"""
import glob
import os
import queue
import shutil
import subprocess
import sys
import threading
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRANCH = "claude/traser-interpretability"
N_RUNS = int(os.environ.get("REPEAT_RUNS", "3"))
LM = os.environ.get("REPEAT_LM", "traser")          # traser_meanpool: TRASER with its resamplers replaced by averaging
OUT = os.environ.get("REPEAT_OUT", "results/traser_repeats" if LM == "traser" else f"results/{LM}")
DATASETS = [d.strip() for d in os.environ.get("REPEAT_DATASETS", "pvsg,svg2test,vidor").split(",") if d.strip()]
SAVE_EVERY_MIN = 20


def step(msg):
    print(f"{time.strftime('%H:%M:%S')}  {msg}", flush=True)


def git(*args):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0", GIT_ASKPASS="", SSH_ASKPASS="")   # never ask for a login
    return subprocess.run(["git", *args], capture_output=True, text=True, cwd=REPO, env=env)


os.chdir(REPO)
os.environ["HF_HOME"] = "/tmp/hf_cache"
BIG = "/kaggle/tmp" if os.path.isdir("/kaggle/tmp") else "/tmp"            # big downloads: not in the repo
BENCH = os.path.join(BIG, "traser_bench")                                   # prepared videos (masks + labels)
RUNS = os.path.join(BIG, "traser_repeat_runs")                              # worker logs and progress
PREP = os.path.join(BIG, "prep_results")                                    # labels written while preparing
REP = os.path.join(REPO, OUT)
for d in (BENCH, RUNS, PREP, REP):
    os.makedirs(d, exist_ok=True)
step(f"code: {REPO} @ " + git("log", "--oneline", "-1").stdout.strip() + f"; --lm {LM}, datasets {DATASETS}, {N_RUNS} runs -> {OUT}")

# ----------------------------------------------------------------------------- setup
step("installing packages + the official SVG2 code (1-2 min) ...")
r = subprocess.run("bash setup_kaggle.sh", shell=True, capture_output=True, text=True)
print("\n".join("    " + l for l in r.stdout.strip().splitlines()[-4:]), flush=True)
if any(l.lstrip().startswith("!!") for l in (r.stdout + r.stderr).splitlines()):
    print("    !! a setup step failed:\n", r.stderr[-800:], flush=True)
subprocess.run("python3 -m pip install -q openai huggingface_hub 'gdown>=5'", shell=True, capture_output=True)
sys.path.insert(0, os.path.join(REPO, "tools"))
import bench_data as B  # noqa: E402
import pvsg_data  # noqa: E402
from interp import common as IC  # noqa: E402

# ----------------------------------------------------------------------------- GitHub (to save the answers)
if not git("config", "user.name").stdout.strip():
    git("config", "user.name", "kanu2704")
    git("config", "user.email", "kanu2704@users.noreply.github.com")
token = os.environ.pop("SVG2_GH_TOKEN", "").strip()
if token:
    git("config", "--global", "credential.helper", "store")
    cred = os.path.expanduser("~/.git-credentials")
    with open(cred, "a") as f:
        f.write(f"https://kanu2704:{token}@github.com\n")
    os.chmod(cred, 0o600)
del token
PUSH = git("push", "--dry-run", "origin", f"HEAD:{BRANCH}").returncode == 0
step("GitHub: push works ✓" if PUSH else "!! GitHub: no push access (set SVG2_GH_TOKEN, see the top of this file): "
     "the answers stay in this session only, push them yourself before it ends")


def answered(root, ds):
    return {os.path.basename(p)[:-5] for p in glob.glob(os.path.join(root, ds, "preds", "*.json")) if not p.endswith(".stats.json")}


def summary():
    return ", ".join(f"run{k} " + "/".join(f"{ds} {len(answered(os.path.join(REP, f'run{k}'), ds))}" for ds in DATASETS)
                     for k in range(1, N_RUNS + 1))


def save():
    """git add + commit + push results/traser_repeats (after pulling what others pushed)."""
    if not PUSH:
        return
    git("add", OUT)
    if git("diff", "--cached", "--quiet").returncode == 0:
        return
    git("commit", "-q", "-m", f"{OUT} (Kaggle T4, --lm {LM}): {summary()}")
    for _ in range(3):
        git("pull", "--rebase", "--autostash", "-q", "origin", BRANCH)
        r = git("push", "-q", "origin", f"HEAD:{BRANCH}")
        if r.returncode == 0:
            step(f"saved to GitHub ✓ ({summary()})")
            return
        time.sleep(15)
    step("!! push failed: " + (r.stderr.strip().splitlines() or ["?"])[-1][:200] + " (committed here; push by hand: "
         f"cd {REPO} && git push origin HEAD:{BRANCH})")


# ----------------------------------------------------------------------------- data (once per session)
def prepare(ds):
    """Download what this dataset needs; returns (videos to run, extra bench_run arguments)."""
    want = IC.select_videos(ds, 0)                          # the videos of the published run
    if ds == "pvsg":
        root = os.path.join(BIG, "pvsg")
        paths = pvsg_data.download(root, sources=("vidor", "epic_kitchen", "ego4d"))
        shutil.copy(paths["pvsg.json"], os.path.join(root, "pvsg.json"))
        anno = pvsg_data.load_anno(root)
        vids = [v for v in want if v in set(B.pvsg_val_ids(anno))]
        new = [v for v in vids if not os.path.exists(os.path.join(root, pvsg_data.video_source(anno, v), "videos", f"{v}.mp4"))]
        if new:
            pvsg_data.extract_videos(root, {os.path.basename(p): p for p in paths.values()}, anno, new)
        return vids, f"--pvsg_root {root}"
    if ds == "vidor":
        root = os.path.join(BIG, "vidor")
        B.download_vidor(root)
        have = B.vidor_index({"videos": os.path.join(root, "videos"), "anno": os.path.join(root, "anno")})
        return [v for v in want if v in have], f"--vidor_root {root}"
    if ds == "svg2test":
        root = os.path.join(BIG, "svg2")
        B.download_svg2test(root)
        rows, masks = B.svg2test_rows(root), B.svg2test_masks(root)
        def from_vipseg(v):          # made by the old version of this script (VIPSeg, a third of the frames): redo
            g = B.load_gt(BENCH, ds, v)
            return g["source"] == "vipseg" and g["n_frames"] != g["mask_frames"]
        todo = [v for v in want if v in rows and (not B.item_ready(BENCH, ds, v) or from_vipseg(v))]
        vip = [v for v in todo if rows[v]["split"] == "vipseg"]
        sav = [v for v in todo if rows[v]["split"] == "sav"]
        out = os.path.join(BIG, "svg2test_videos")
        videos, fallback = {}, {}
        if vip:
            # As the published run (notebooks/full_pairs_run.py) and the paper: VSPW's own frames, one per mask frame, at
            # 6 fps. Not VIPSeg: it keeps only every 3rd frame, so its videos would be a third as long and the human
            # relation times (mask frame / 6) would not match the video.
            vdir = os.path.join(BIG, "svg2test_vspw_videos")
            if os.environ.get("VSPW_DIR"):
                parts = sorted(glob.glob(os.path.join(os.environ["VSPW_DIR"], "*")))
            elif max(masks[v][0][0]["size"][0] for v in vip) <= 480:
                parts = B.download_vspw(BIG, "480p")
            else:
                step("SVG2test: downloading full-resolution VSPW (6 parts, ~43 GB) ...")
                try:
                    parts = B.download_vspw(BIG, "full_parts")
                except Exception as e:  # noqa: BLE001
                    step(f"!! Google Drive refused the full VSPW ({str(e)[:150]}); using 480p, scaled up to the mask size")
                    parts = B.download_vspw(BIG, "480p")
            found = B.extract_vspw_frames(parts if len(parts) > 1 else parts[0], vip, os.path.join(BIG, "vspw_frames"),
                                          log=print)
            if set(vip) - found:
                step(f"!! VSPW frames not found for {sorted(set(vip) - found)}")
            for v in sorted(found):
                fdir = os.path.join(BIG, "vspw_frames", v)
                h, w = masks[v][0][0]["size"]
                p = os.path.join(vdir, f"{v}.mp4")
                if not os.path.exists(p):
                    B.frames_to_mp4(fdir, p, fps=6, size=(w - w % 2, h - h % 2))
                videos[v] = p
                if len(glob.glob(os.path.join(fdir, "*.jpg"))) != len(masks[v]):   # not expected: nearest frame
                    fallback[v] = fdir
        if sav and os.environ.get("SAV_LINKS"):
            missing = B.fetch_sav_videos(B.sav_links(os.environ["SAV_LINKS"]), sav, out)
            if missing:
                step(f"!! SA-V videos not found: {sorted(missing)}")
            videos.update({v: os.path.join(out, f"{v}.mp4") for v in sav if os.path.exists(os.path.join(out, f"{v}.mp4"))})
        elif sav:
            step(f"!! {len(sav)} SA-V videos skipped: set SAV_LINKS to Meta's links file to run them")
        for v, p in sorted(videos.items()):
            B.prepare_svg2test(v, rows[v], masks[v], p, BENCH, PREP, vipseg_frames=fallback.get(v))
        return [v for v in want if B.item_ready(BENCH, ds, v)], ""
    raise SystemExit(f"unknown dataset {ds}")


def run_live(cmds, label):
    """Run the workers side by side, print their output live, save to GitHub every SAVE_EVERY_MIN minutes."""
    q, procs, last = queue.Queue(), [], time.time()
    for c in cmds:
        p = subprocess.Popen(c, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, cwd=REPO)
        procs.append(p)
        threading.Thread(target=lambda p=p: [q.put(l) for l in p.stdout], daemon=True).start()
    while any(p.poll() is None for p in procs) or not q.empty():
        try:
            line = q.get(timeout=5).rstrip()
            if "Warning" not in line and "warn(" not in line:
                print("    " + line, flush=True)
        except queue.Empty:
            pass
        if time.time() - last > SAVE_EVERY_MIN * 60:
            save()
            last = time.time()
    bad = [i for i, p in enumerate(procs) if p.returncode]
    step(f"{label}: finished" + (f" (!! worker {bad} exited with an error, see above)" if bad else ""))


out = subprocess.run(["nvidia-smi", "-L"], capture_output=True, text=True).stdout
GPUS = [str(i) for i in range(len([l for l in out.splitlines() if l.startswith("GPU ")]))] or ["0"]
step(f"GPUs: {GPUS} (one worker each)")
t_all = time.time()
for ds in DATASETS:
    t0 = time.time()
    step(f"{ds}: downloading / preparing (this session only) ...")
    vids, extra = prepare(ds)
    step(f"{ds}: {len(vids)} videos ready ({(time.time() - t0) / 60:.0f} min)")
    for k in range(1, N_RUNS + 1):
        root = os.path.join(REP, f"run{k}")
        todo = [v for v in vids if v not in answered(root, ds)]
        step(f"run {k}, {ds}: {len(vids) - len(todo)} answered before, {len(todo)} to answer")
        if not todo:
            continue
        t1, cmds = time.time(), []
        for i, g in enumerate(GPUS):
            part = todo[i::len(GPUS)]
            if part:
                qfile = os.path.join(RUNS, f"run{k}_{ds}_gpu{i}.queue")
                open(qfile, "w").write("\n".join(part))
                cmds.append(f"CUDA_VISIBLE_DEVICES={g} HF_HOME={os.environ['HF_HOME']} python3 tools/bench_run.py "
                            f"--results {root} --bench {BENCH} --dataset {ds} --runs {RUNS} --gpu_name run{k}_gpu{i} --lm {LM} "
                            f"{extra} --videos $(cat {qfile})")
        run_live(cmds, f"run {k}, {ds}")
        step(f"run {k}, {ds}: {len(answered(root, ds))} of {len(vids)} answered ({(time.time() - t1) / 3600:.1f} h)")
        save()
step(f"===== done in {(time.time() - t_all) / 3600:.1f} h: {summary()}")
save()
step("next (anywhere, NVIDIA key): python3 tools/repeat_report.py")
