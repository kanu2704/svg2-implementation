"""Experiment 2 on EVERY human pair of EVERY video (notebooks/traser_pairs.ipynb, section 4b), for a terminal
(inside tmux on the server). It first waits until notebooks/overnight_run.py (the fine-tuning) has finished, so the two
never share the GPU; pass `now` to start at once. Every step skips work that is already finished.
Made from notebooks/traser_pairs.ipynb (cells 0a-4 setup + 4b): edit the notebook, not this file.

    tmux new -s full
    source /media/data_dump/conda/miniconda3/etc/profile.d/conda.sh && conda activate /media/nas_mount/kanupriya/envs/traser
    cd /media/nas_mount/kanupriya/svg2-implementation && python3 notebooks/full_pairs_run.py 2>&1 | tee -a /media/nas_mount/kanupriya/full_pairs.log

It asks for the GitHub token once at the start (Enter = no pushing; results stay committed on the server).
"""

# ----------------------------------------------------------------------------- pairs 0a
import os, sys, json, glob, time, shutil, subprocess, getpass, random
BIG_DIR = ""        # your own server: a folder with ~150 GB free, e.g. "/data/kanu/svg2_big" (Kaggle: leave empty)
GPU_IDS = ""        # your own server: the only GPUs this notebook may touch, e.g. "6" or "6,7" (Kaggle: leave empty)
ENV = ""            # your own server: your Python environment's folder; 0a stops if the kernel is another one
# own server: instead of editing these lines, put them in svg2_settings.json next to the repo folder,
# {"BIG_DIR": "...", "GPU_IDS": "6", "ENV": "..."}; then a git pull never clashes with your edits
ON_KAGGLE = os.path.isdir("/kaggle/working")
BRANCH = "claude/traser-interpretability"
def step(msg): print(f"{time.strftime('%H:%M:%S')}  {msg}", flush=True)

def find_repo():
    """The clone this notebook was opened from (VS Code tells the notebook's path; else the working folder)."""
    is_repo = lambda d: os.path.isfile(os.path.join(d, "tools", "bench_data.py")) and os.path.isdir(os.path.join(d, ".git"))
    for start in (os.path.dirname(globals().get("__vsc_ipynb_file__") or ""), os.path.abspath("")):
        if not start:
            continue
        if is_repo(os.path.join(start, "svg2-implementation")):
            return os.path.join(start, "svg2-implementation")
        d = os.path.abspath(start)
        while d != os.path.dirname(d):
            if is_repo(d):
                return d
            d = os.path.dirname(d)
    return None

if ON_KAGGLE:
    REPO = "/kaggle/working/svg2-implementation"
else:
    REPO = find_repo()
    SETTINGS = os.path.join(os.path.dirname(REPO), "svg2_settings.json") if REPO else ""
    if SETTINGS and os.path.exists(SETTINGS):
        s = json.load(open(SETTINGS))
        BIG_DIR, GPU_IDS = BIG_DIR or s.get("BIG_DIR", ""), GPU_IDS or str(s.get("GPU_IDS", ""))
        ENV = ENV or s.get("ENV", "")
        step(f"settings from {SETTINGS}: BIG_DIR = {BIG_DIR}, GPU_IDS = {GPU_IDS}, ENV = {ENV or '-'}")
    REPO = REPO or os.path.join(os.path.dirname(os.path.abspath(BIG_DIR)) if BIG_DIR else os.path.expanduser("~"),
                                "svg2-implementation")
    step(f"kernel: {sys.executable}")
    if ENV and os.path.realpath(sys.prefix) != os.path.realpath(ENV):
        # packages are installed into the kernel's environment: never into someone else's
        raise RuntimeError(f"wrong kernel: this notebook runs in {sys.prefix}, your settings say {ENV}. "
                           "Pick that environment as the kernel (top right) and run 0a again. Nothing was installed.")
if GPU_IDS:
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # number the GPUs as nvidia-smi does (CUDA's default order differs)
    os.environ["CUDA_VISIBLE_DEVICES"] = GPU_IDS     # set before any GPU use: every cell and worker sees only these
elif not ON_KAGGLE:
    print("!! GPU_IDS is empty: every GPU of this machine is visible. On a shared server set it (see above).")
# every "python3" this notebook starts is the notebook's own Python (with its torch), also on a server
os.environ["PATH"] = os.path.dirname(sys.executable) + os.pathsep + os.environ.get("PATH", "")

if not os.path.isdir(REPO):
    step("cloning the repo ...")
    subprocess.run(["git", "clone", "-b", BRANCH, "https://github.com/kanu2704/svg2-implementation", REPO], check=True)
os.chdir(REPO)
step(f"code: {REPO} @ " + subprocess.run(["git", "log", "--oneline", "-1"], capture_output=True, text=True).stdout.strip())
BIG = BIG_DIR or ("/kaggle/tmp" if os.path.isdir("/kaggle/tmp") else "/tmp")    # big downloads (not in the repo)
os.makedirs(BIG, exist_ok=True)
os.environ["HF_HOME"] = "/tmp/hf_cache" if ON_KAGGLE else os.path.join(BIG, "hf_cache")
if BIG_DIR and not ON_KAGGLE:
    # temporary files and pip's downloads also go to the big folder (a server's system disk can be small or full)
    for var, sub in (("TMPDIR", "tmp"), ("PIP_CACHE_DIR", "pip_cache")):
        os.environ[var] = os.path.join(BIG, sub)
        os.makedirs(os.environ[var], exist_ok=True)
    import tempfile
    tempfile.tempdir = None
step("installing packages + the official SVG2 code (1-2 min) ...")
r = subprocess.run("bash setup_kaggle.sh", shell=True, capture_output=True, text=True)
print("\n".join("    " + l for l in r.stdout.strip().splitlines()[-4:]))
if any(l.lstrip().startswith("!!") for l in (r.stdout + r.stderr).splitlines()):
    print("    !! a setup step failed:\n", r.stderr[-800:])
r = subprocess.run("python3 -m pip install -q openai huggingface_hub 'gdown>=5'", shell=True, capture_output=True, text=True)
if r.returncode:
    print("    !! pip:", r.stderr[-400:])
sys.path.insert(0, os.path.join(REPO, "tools"))
import bench_data as B, bench_eval as E, pvsg_data
BENCH = os.path.join(BIG, "traser_bench")                             # prepared videos: video.mp4 + masks + labels
RUNS = "/kaggle/working/traser_bench_runs" if ON_KAGGLE else os.path.join(BIG, "traser_bench_runs")   # worker logs
for d in (BENCH, RUNS):
    os.makedirs(d, exist_ok=True)
step(f"ready. big data → {BIG} ({shutil.disk_usage(BIG).free // 2**30} GB free); worker logs → {RUNS}")

# ----------------------------------------------------------------------------- pairs 0c
def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, env=dict(os.environ, GIT_TERMINAL_PROMPT="0", GIT_ASKPASS="", SSH_ASKPASS=""))   # never ask for a login (e.g. VS Code's popup)

if not git("config", "user.name").stdout.strip():
    git("config", "user.name", "kanu2704")
    git("config", "user.email", "kanu2704@users.noreply.github.com")
cred = os.path.expanduser("~/.git-credentials")
if git("push", "--dry-run", "origin", f"HEAD:{BRANCH}").returncode == 0:
    step("GitHub: push access works already ✓")
else:
    token = getpass.getpass("GitHub token (hidden; Enter = skip): ").strip()
    if token and ON_KAGGLE:
        git("config", "--global", "credential.helper", "store")
        with open(cred, "a") as f:
            f.write(f"https://kanu2704:{token}@github.com\n")
        os.chmod(cred, 0o600)
    elif token:
        # shared server: git asks this repo-only helper, which reads the token from this notebook's environment
        os.environ["SVG2_GH_TOKEN"] = token
        git("config", "--local", "--unset-all", "credential.helper")
        git("config", "--local", "--add", "credential.helper", "")      # ignore the account's global helpers
        git("config", "--local", "--add", "credential.helper",
            '!f() { test "$1" = get && test -n "$SVG2_GH_TOKEN" && echo username=kanu2704 && echo "password=$SVG2_GH_TOKEN"; }; f')
    del token
    r = git("push", "--dry-run", "origin", f"HEAD:{BRANCH}")
    step("GitHub: push access works ✓" if r.returncode == 0 else
         "GitHub: no push access → saving will tell you the terminal commands. (" + r.stderr.strip().splitlines()[-1][:150] + ")")

# ----------------------------------------------------------------------------- wait for the fine-tuning (overnight_run.py) to finish
import subprocess as _sp
if "now" not in sys.argv[1:]:
    _first = True
    # only a Python process that runs overnight_run.py (not a shell or an editor that mentions it)
    while _sp.run(["pgrep", "-f", "^[^ ]*python[^ ]* +[^ ]*overnight_run[.]py"], capture_output=True).returncode == 0:
        if _first:
            step("the overnight run (fine-tuning) is still going: waiting for it to finish (checking every 5 minutes) ...")
            _first = False
        time.sleep(300)
    step("no overnight run going: starting")

# ----------------------------------------------------------------------------- wait for a working GPU
while True:
    _r = subprocess.run(["python3", "-c", "import torch; torch.zeros(1).cuda(); print(torch.cuda.get_device_name(0))"],
                        capture_output=True, text=True)
    if _r.returncode == 0:
        step("GPU works: " + _r.stdout.strip())
        break
    step("GPU not usable yet (" + ((_r.stderr.strip().splitlines() or ["?"])[-1])[:120] + "); trying again in 5 minutes")
    time.sleep(300)


# ----------------------------------------------------------------------------- pairs 0b
from huggingface_hub import snapshot_download
step("downloading the TRASER checkpoint (UWGZQ/TRASER) ...")
t0 = time.time()
traser_dir = snapshot_download("UWGZQ/TRASER", ignore_patterns=["example/*"])
step("downloading the Qwen2.5-VL processor files ...")
qwen_dir = snapshot_download("Qwen/Qwen2.5-VL-3B-Instruct", ignore_patterns=["*.safetensors", "*.bin", "*.pt", "*.pth"])
size = lambda d: sum(os.path.getsize(p) for p in glob.glob(os.path.join(d, "**"), recursive=True) if os.path.isfile(p)) / 2**30
step(f"TRASER: {size(traser_dir):.1f} GB | Qwen processor: {size(qwen_dir) * 1024:.0f} MB | {time.time() - t0:.0f} s")

import torch
print(f"\n{torch.cuda.device_count()} GPU(s):")
for i in range(torch.cuda.device_count()):
    p = torch.cuda.get_device_properties(i)
    cc = torch.cuda.get_device_capability(i)
    free, total = torch.cuda.mem_get_info(i)
    print(f"  GPU {i}: {p.name}, {total / 2**30:.1f} GB ({free / 2**30:.1f} GB free), compute {cc[0]}.{cc[1]} → "
          + ("bfloat16" if cc[0] >= 8 else "float16 + memory-saving attention"))
if torch.cuda.device_count() == 0:
    print("  !! no GPU: Settings → Accelerator → GPU T4 x2" if ON_KAGGLE else
          "  !! no usable GPU here (only block 6 needs one): check nvidia-smi and GPU_IDS")

# ----------------------------------------------------------------------------- pairs 0d
LAST_SAVE = {}

def n_done(dataset):
    return len([p for p in glob.glob(f"results/traser_bench/{dataset}/preds/*.json") if not p.endswith(".stats.json")])

def _procs(label=None):
    """Running workers (TRASER, vLLM, SAM 3); label = a dataset, or a stage name given with --name."""
    # only Python running one of the workers (or the bash that waits to start one), not any command that
    # merely mentions a worker's file name
    out = subprocess.run("pgrep -af 'python[^ ]* +[^ ]*tools/(bench_run|vllm_generate|sam3_masks)[.]py'", shell=True,
                         capture_output=True, text=True).stdout
    lines = [l for l in out.splitlines() if l.strip() and "pgrep" not in l]
    return [l for l in lines if label is None or f"--name {label} " in l
            or (f"--dataset {label} " in l and "--name " not in l)]

def bar(d, t, w=25):
    t = max(int(t or 0), 1); d = min(int(d or 0), t)
    return "█" * round(w * d / t) + "░" * (w - round(w * d / t)) + f" {d}/{t}"

def start_workers(dataset, videos, last=(), extra="", label=None, cmd=None, done=None):
    """One background worker per GPU. If other workers are still running, the new ones wait for them and
    start by themselves. `last`: videos to put at the end of the queue. label: name of this stage (its
    progress files; default the dataset); cmd(gpu, queue_file): the worker command (default: TRASER);
    done: videos already finished (default: those with a prediction)."""
    label = label or dataset
    if _procs(label):
        print(f"{label} workers are already running → use the watch cell"); return
    if done is None:
        done = {os.path.basename(p)[:-5] for p in glob.glob(f"results/traser_bench/{dataset}/preds/*.json")
                if not p.endswith(".stats.json")}
    todo = [v for v in videos if v not in done and v not in last] + [v for v in last if v in videos and v not in done]
    ids = [x.strip() for x in GPU_IDS.split(",") if x.strip()]     # own server: only these GPUs
    out = subprocess.run(["nvidia-smi"] + (["-i", ",".join(ids)] if ids else []) +
                         ["--query-gpu=index,memory.free", "--format=csv,noheader,nounits"], capture_output=True, text=True).stdout
    rows = [l.split(",") for l in out.splitlines() if l.count(",") == 1]
    gpus, free = [r[0].strip() for r in rows] or ["0"], [r[1].strip() for r in rows]
    step(f"{label}: {len(set(videos) & set(done))} videos done earlier, {len(todo)} to run, GPU(s) {gpus}, free MiB: {free}")
    if not todo:
        print("nothing to run"); return
    others = [l.split()[0] for l in _procs()]
    if others:
        print(f"  workers of another dataset are running → these start automatically when they finish")
    for p in glob.glob(os.path.join(RUNS, f"{label}_gpu*.*")):
        os.remove(p)                                          # old progress files and logs of this stage
    n_gpu = len(gpus)
    for i, g in enumerate(gpus):
        queue = todo[i::n_gpu]
        if not queue:
            continue
        qfile = os.path.join(RUNS, f"{label}_gpu{g}.queue")
        open(qfile, "w").write("\n".join(queue))
        run = cmd(g, qfile) if cmd else (
              f"CUDA_VISIBLE_DEVICES={g} HF_HOME={os.environ.get('HF_HOME', '/tmp/hf_cache')} python3 tools/bench_run.py --dataset {dataset} "
              f"--bench {BENCH} --runs {RUNS} --gpu_name gpu{g} {extra}"
              + (f" --name {label}" if label != dataset else "") + f" --videos $(cat {qfile})")
        if others:
            wait = " || ".join(f"kill -0 {pid} 2>/dev/null" for pid in others)
            run = f"while {wait}; do sleep 20; done; {run}"
        subprocess.run(f"nohup bash -c '{run}' >> {RUNS}/{label}_gpu{g}.log 2>&1 &", shell=True)
        print(f"  GPU {g}: {len(queue)} videos, first: {queue[0]}, log: {RUNS}/{label}_gpu{g}.log")
    print("→ run the watch cell to follow it live")

def _ago(t):
    return f"{(time.time() - t) / 60:.1f} min" if t else "-"

def status(dataset, total, log_lines=4, label=None, count=None):
    """One look at the workers of a dataset or stage (does not wait). count(): how many are finished."""
    label = label or dataset
    procs = _procs(label)
    n = count() if count else n_done(dataset)
    print(f"{time.strftime('%H:%M:%S')}   {label}: {bar(n, total)} finished   "
          f"| worker processes: {len(procs)}   | last GitHub save: {LAST_SAVE.get(dataset, 'not yet')}")
    gpus = subprocess.run("nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader,nounits",
                          shell=True, capture_output=True, text=True).stdout.strip().splitlines()
    print("   " + "   ".join(f"GPU {g.split(',')[0]}: {int(g.split(',')[1]) / 1024:.1f}/{int(g.split(',')[2]) / 1024:.0f} GB, "
                             f"{g.split(',')[3].strip()}% busy" for g in gpus if g.count(",") == 3))
    logs = sorted(glob.glob(os.path.join(RUNS, f"{label}_gpu*.log")))
    for log in logs:
        name = os.path.basename(log)[:-4]
        try:
            st = json.load(open(log[:-4] + ".json"))
        except (OSError, ValueError):
            st = None
        print()
        if st is None:
            waiting = any("kill -0" in l for l in procs)
            print(f"{name}: " + ("waiting for the other dataset's workers to finish" if waiting else "starting ..."))
        else:
            left = st["total"] - st["done"] - len(st["failed"])
            avg = st.get("avg_min")
            eta = f"~{avg * left:.0f} min left" if avg is not None else "time left: known after the first video"
            print(f"{name}: {bar(st['done'], st['total'])}   failed: {len(st['failed'])}   "
                  f"avg {'-' if avg is None else avg} min/video   {eta}   (attempt {st.get('attempt', 1)})")
            if st.get("current"):
                print(f"   now:   {st['current']}   ({_ago(st.get('video_since'))} on it)")
            print(f"   step:  {st['state']}   (for {_ago(st.get('stage_since'))}, updated {st.get('updated')})")
            for r in st.get("recent", [])[-3:]:
                print(f"   done:  {r['video']}   {r['min']} min, {r['tokens']} tokens, {r['objects']} objects")
            if st["failed"]:
                print("   failed:", ", ".join(st["failed"]))
        lines = open(log, errors="replace").read().splitlines()[-log_lines:]
        for l in lines:
            print("   │ " + l[:200])
    if not logs:
        print("\nno workers started for", label)
    return procs

def save(dataset, quiet=False):
    """git add + commit + push the results of a dataset ("score": the whole results folder)."""
    path = "results/traser_bench" if dataset == "score" else f"results/traser_bench/{dataset}"
    if not os.path.exists(path):
        print("nothing to save yet"); return False
    git("add", path)
    if git("diff", "--cached", "--quiet").returncode:
        git("commit", "-m", f"TRASER bench: {dataset} results ({n_done(dataset) if dataset not in ('score', 'diagnosis', 'interp') else dataset})")
    r = git("push", "origin", f"HEAD:{BRANCH}")
    if r.returncode and ("rejected" in r.stderr or "fetch first" in r.stderr):
        git("pull", "--rebase", "--autostash", "origin", BRANCH)
        r = git("push", "origin", f"HEAD:{BRANCH}")
    when = time.strftime("%H:%M")
    if r.returncode == 0:
        LAST_SAVE[dataset] = f"{when} ✓ ({n_done(dataset) if dataset not in ('score', 'diagnosis', 'interp') else dataset})"
        if not quiet:
            step(f"saved to GitHub ✓ ({path})")
        return True
    LAST_SAVE[dataset] = f"{when} ✗ push failed (committed locally)"
    print(f"!! push failed: {r.stderr.strip().splitlines()[-1] if r.stderr.strip() else '?'}\n"
          f"   the results are committed locally; push from a terminal:\n   cd {REPO} && git push origin HEAD:{BRANCH}")
    return False

def watch(dataset, total, every=15, autosave_min=15, label=None, count=None, autosave=True, errors=None):
    """Live view (refreshes every 15 s). Stopping this cell does NOT stop the workers.
    label/count: a stage other than "TRASER answers" (see status); autosave=False: nothing to push."""
    from IPython.display import clear_output
    label = label or dataset
    count = count or (lambda: n_done(dataset))
    last_save, saved_n, t_start = time.time(), count(), time.time()
    try:
        while True:
            clear_output(wait=True)
            procs = status(dataset, total, label=label, count=count)
            if autosave and count() > saved_n and time.time() - last_save > autosave_min * 60:
                save(dataset, quiet=True); last_save, saved_n = time.time(), count()
            if not procs and time.time() - t_start > 30:
                print(f"\n{time.strftime('%H:%M:%S')}  no {label} worker running any more: {count()} of {total} finished")
                for p in sorted(glob.glob(errors or f"results/traser_bench/{dataset}/preds/*.error.txt")):
                    print(f"   failed: {os.path.basename(p)[:-10]}: {open(p).readline().strip()[:160]}")
                if autosave:
                    save(dataset)
                return
            time.sleep(every)
    except KeyboardInterrupt:
        print("\nstopped watching; the workers keep running (run this cell again to look)")
print("helpers ready")

# ----------------------------------------------------------------------------- pairs 1 settings
DATASETS = ["pvsg", "vidor"]   # add "svg2test" once it is prepared (traser_eval.ipynb 2a-2d, needs the SA-V links file)
INTERP_N = {"svg2test": 0, "pvsg": 0, "vidor": 300}   # videos per dataset (0 = all); a bigger sample keeps the first run's videos (40 / 25 / 60) inside it
EXPERIMENTS = [1, 2, 3, 4, 5]      # experiments run and shown (6 is left out)
MISSED, WRITTEN, CONTROL = 8, 3, 3   # per video: missed human pairs tested, written human pairs and unrelated pairs (for comparison)
WORK = os.path.join(BIG, "interp_work")    # big per-video files (not pushed)
LM_DIR = os.path.join(BIG, "traser_lm")    # TRASER's language model alone
sys.path.insert(0, os.path.join(REPO, "tools"))
from interp import common as IC
SAMPLE = {ds: IC.select_videos(ds, INTERP_N.get(ds)) for ds in DATASETS}
for ds, vids in SAMPLE.items():
    print(f"{ds}: {len(vids)} videos in the sample")

# ----------------------------------------------------------------------------- pairs 2a PVSG download
if "pvsg" in DATASETS:
    t0 = time.time()
    PVSG_ROOT = os.path.join(BIG, "pvsg")
    step("downloading PVSG from Hugging Face (progress bars below; skipped if already here) ...")
    paths = pvsg_data.download(PVSG_ROOT, sources=("vidor", "epic_kitchen", "ego4d"))
    shutil.copy(paths["pvsg.json"], os.path.join(PVSG_ROOT, "pvsg.json"))
    anno = pvsg_data.load_anno(PVSG_ROOT)
    zips = {os.path.basename(p): p for p in paths.values()}
    for i, v in enumerate(SAMPLE["pvsg"], 1):
        src = pvsg_data.video_source(anno, v)
        if not (os.path.exists(os.path.join(PVSG_ROOT, src, "videos", f"{v}.mp4"))
                and glob.glob(os.path.join(PVSG_ROOT, src, "masks", v, "*.png"))):
            pvsg_data.extract_videos(PVSG_ROOT, zips, anno, [v])
        print(f"    {i:2}/{len(SAMPLE['pvsg'])} {v} extracted", flush=True)
    step(f"PVSG sample extracted ({time.time() - t0:.0f} s)")

# ----------------------------------------------------------------------------- pairs 2b PVSG prepare
if "pvsg" in DATASETS:
    for i, v in enumerate(SAMPLE["pvsg"], 1):
        if not B.item_ready(BENCH, "pvsg", v):
            B.prepare_pvsg(PVSG_ROOT, anno, v, BENCH, E.RESULTS)
    step(f"PVSG ready: {sum(B.item_ready(BENCH, 'pvsg', v) for v in SAMPLE['pvsg'])} of {len(SAMPLE['pvsg'])} videos")

# ----------------------------------------------------------------------------- pairs 3 VidOR
if "vidor" in DATASETS:
    t0 = time.time()
    VIDOR_ROOT = os.path.join(BIG, "vidor")
    step("downloading VidOR validation (videos + boxes) ...")
    B.download_vidor(VIDOR_ROOT)
    idx = B.vidor_index({"videos": os.path.join(VIDOR_ROOT, "videos"), "anno": os.path.join(VIDOR_ROOT, "anno")})
    for v in SAMPLE["vidor"]:
        if not os.path.exists(os.path.join(BENCH, "vidor", v, "gt.json")):
            B.prepare_vidor_item(*idx[v], BENCH, E.RESULTS)
    ready = sum(os.path.exists(os.path.join(BENCH, "vidor", v, "gt.json")) for v in SAMPLE["vidor"])
    step(f"VidOR ready: {ready} of {len(SAMPLE['vidor'])} videos ({time.time() - t0:.0f} s)")

# ----------------------------------------------------------------------------- pairs 4 GPU setup
import threading, queue, torch
SAVE_EVERY_MIN = 20
GPUS = None              # None = every GPU this notebook can see
if GPUS is None:
    seen = os.environ.get("CUDA_VISIBLE_DEVICES")
    GPUS = [int(x) for x in seen.split(",") if x.strip()] if seen else list(range(max(1, torch.cuda.device_count())))
N_GPU = len(GPUS)

def run_parallel(cmds, label):
    """Run one command per GPU, print their output live, save to GitHub every SAVE_EVERY_MIN minutes."""
    q, procs, last = queue.Queue(), [], time.time()
    for c in cmds:
        p = subprocess.Popen(c, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, cwd=REPO)
        procs.append(p)
        threading.Thread(target=lambda p=p: [q.put(l) for l in p.stdout], daemon=True).start()
    while any(p.poll() is None for p in procs) or not q.empty():
        try:
            print("    " + q.get(timeout=5).rstrip(), flush=True)
        except queue.Empty:
            pass
        if time.time() - last > SAVE_EVERY_MIN * 60:
            save("interp", quiet=True); last = time.time()
    bad = [i for i, p in enumerate(procs) if p.returncode]
    step(f"{label}: finished" + (f" (!! process {bad} exited with an error, see above)" if bad else ""))

try:
    import sklearn, matplotlib  # noqa: F401
except ImportError:
    subprocess.run("python3 -m pip install -q scikit-learn matplotlib", shell=True)
if not os.path.exists(os.path.join(LM_DIR, "config.json")):
    step("exporting TRASER's language model (~3 min) ...")
    r = subprocess.run(["python3", "tools/export_lm.py", "--model", traser_dir, "--out", LM_DIR], capture_output=True, text=True)
    print("\n".join("    " + l for l in (r.stdout + r.stderr).strip().splitlines()[-3:]))
step(f"ready: GPU(s) {GPUS}")

# ----------------------------------------------------------------------------- pairs 4b experiment 2 on every pair
ALL_DATASETS = ["pvsg", "vidor", "svg2test"]     # the ones not prepared here are left out
ALL_N = {ds: 0 for ds in ALL_DATASETS}          # 0 = every video TRASER answered
if "vidor" in ALL_DATASETS and "vidor" in DATASETS:
    for v in IC.select_videos("vidor", 0):
        if v in idx and not os.path.exists(os.path.join(BENCH, "vidor", v, "gt.json")):
            B.prepare_vidor_item(*idx[v], BENCH, E.RESULTS)
use = []
for ds in ALL_DATASETS:
    vids = IC.select_videos(ds, 0)
    ready = sum(os.path.exists(os.path.join(B.item_dir(BENCH, B.base_dataset(ds), v), "gt.json")) for v in vids)
    step(f"{ds}: {ready} of {len(vids)} videos prepared")
    if ready:
        use.append(ds)
n_all, ds_all = json.dumps({ds: 0 for ds in use}), " ".join(use)
t0 = time.time()
step(f"inputs for every video on GPU(s) {GPUS} (only the missing ones) ...")
run_parallel([f"CUDA_VISIBLE_DEVICES={gpu} python3 tools/interp/encode_stage.py --bench {BENCH} --masks_work {BENCH} --work {WORK} "
              f"--model {traser_dir} --base_model {qwen_dir} --datasets {ds_all} --n '{n_all}' --shard {i} --nshards {N_GPU}"
              for i, gpu in enumerate(GPUS)], "inputs")
step("experiment 2 on every pair ...")
run_parallel([f"CUDA_VISIBLE_DEVICES={gpu} python3 tools/interp/pairs_stage.py --lm {LM_DIR} --work {WORK} "
              f"--datasets {ds_all} --n '{n_all}' --control {CONTROL} --phases e2all --shard {i} --nshards {N_GPU}"
              for i, gpu in enumerate(GPUS)], "experiment 2 (every pair)")
save("interp", quiet=True)
run_parallel([f"python3 tools/interp/pairs_report.py --work {WORK} --datasets {' '.join(sorted(set(DATASETS) | set(use)))} "
              "--only_all"], "report (adds table 2b)")
save("interp")
step(f"done in {(time.time() - t0) / 3600:.1f} h → PAIRS.md, section 2b")

step('===== all done: results/traser_bench/interp/PAIRS.md, section 2b =====')
