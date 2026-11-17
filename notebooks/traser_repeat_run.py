"""TRASER's Table 2 baseline again, N_RUNS times, with the official settings of the paper (tools/bench_run.py:
released UWGZQ/TRASER, 1 fps, at most 128 frames, at most 40 objects, coverage 0.5, 4 s windows, greedy decoding),
on every video of PVSG (62), SVG2test (100) and VidOR (835) that the published run answered. For a terminal, inside
tmux on the server. Each run's answers go to results/traser_repeats/run<k>/<dataset>/preds; the scores (mean and
standard deviation over the runs, Nemotron judge) come from tools/repeat_report.py afterwards.

    tmux new -s repeat
    cd /media/nas_mount/kanupriya/svg2-implementation
    /media/nas_mount/kanupriya/envs/traser/bin/python notebooks/traser_repeat_run.py 2>&1 | tee -a /media/nas_mount/kanupriya/repeat.log

REPEAT_RUNS=3 and REPEAT_WORKERS=2 in front of the command change the number of runs and of workers per GPU;
REPEAT_GPUS=2 uses that GPU (nvidia-smi's number) for this run instead of the GPU_IDS of svg2_settings.json;
REPEAT_DATASETS=svg2test,vidor runs only those; REPEAT_DTYPE=float16 uses Kaggle's T4 precision (default auto).
Every step skips videos already answered: after an interruption, run the same command again. Nothing is pushed:
push the results yourself at the end. Setup part made from notebooks/qwen7b_run.py (its cells 0a-0b).
"""
import os
N_RUNS = int(os.environ.get("REPEAT_RUNS", "3"))              # how many times the whole baseline is run
WORKERS_PER_GPU = int(os.environ.get("REPEAT_WORKERS", "2"))  # TRASER (3B, bfloat16) needs about 10 GB per worker; 2 fit
                        # on a 48 GB A6000. Start with REPEAT_WORKERS=1 in front of the command after "out of memory".
RUN_DATASETS = [d.strip() for d in os.environ.get("REPEAT_DATASETS", "pvsg,svg2test,vidor").split(",") if d.strip()]
DTYPE = os.environ.get("REPEAT_DTYPE", "auto")   # float16: as on Kaggle's T4s (vision in float32); auto: bfloat16 here

# ----------------------------------------------------------------------------- pairs 0a
import os, sys, json, glob, time, shutil, subprocess, getpass, random
BIG_DIR = ""        # your own server: a folder with ~150 GB free, e.g. "/data/kanu/svg2_big" (Kaggle: leave empty)
GPU_IDS = os.environ.get("REPEAT_GPUS", "")   # this run only, e.g. REPEAT_GPUS=2; empty: GPU_IDS of svg2_settings.json
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
def gpu_uuids(ids):
    """nvidia-smi's GPU numbers -> the cards' UUIDs. CUDA numbers only the GPUs that work, so once a GPU of the
    machine crashes, CUDA's numbers no longer match nvidia-smi's; a UUID always names the same card."""
    out = subprocess.run(["nvidia-smi", "--query-gpu=index,uuid,name,memory.total", "--format=csv,noheader"],
                         capture_output=True, text=True).stdout
    cards = {r[0]: r[1:] for r in (list(map(str.strip, l.split(","))) for l in out.splitlines()) if len(r) == 4}
    uuids = []
    for x in [x.strip() for x in ids.split(",") if x.strip()]:
        if x.startswith("GPU-"):
            uuids.append(x)
        elif x in cards:
            step(f"GPU {x}: {cards[x][1]}, {cards[x][2]} ({cards[x][0]})")
            uuids.append(cards[x][0])
        else:
            raise RuntimeError(f"GPU {x} of your settings is not working right now (nvidia-smi lists {sorted(cards)}). "
                               "Nothing was started: check nvidia-smi, then run this again.")
    return ",".join(uuids)

if GPU_IDS:
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # number the GPUs as nvidia-smi does (CUDA's default order differs)
    GPU_IDS = gpu_uuids(GPU_IDS)                     # by UUID: still the same card after another GPU of the machine crashes
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

# ----------------------------------------------------------------------------- wait for the other runs (same GPU)
for _name in ("overnight_run", "full_pairs_run", "qwen7b_run"):
    _first = True
    while subprocess.run(["pgrep", "-f", f"^[^ ]*python[^ ]* +[^ ]*{_name}[.]py"], capture_output=True).returncode == 0:
        if _first:
            step(f"{_name}.py is still running on the GPU: waiting for it to finish (checking every 5 minutes) ...")
            _first = False
        time.sleep(300)

# ----------------------------------------------------------------------------- wait for a working GPU
while True:
    _r = subprocess.run(["python3", "-c", "import torch; torch.zeros(1).cuda(); print(torch.cuda.get_device_name(0))"],
                        capture_output=True, text=True)
    if _r.returncode == 0:
        step("GPU works: " + _r.stdout.strip())
        break
    step("GPU not usable yet (" + ((_r.stderr.strip().splitlines() or ["?"])[-1])[:120] + "); trying again in 5 minutes")
    time.sleep(300)



# ----------------------------------------------------------------------------- TRASER, N_RUNS times
import threading, queue
from interp import common as IC
REP = os.path.join(REPO, "results", "traser_repeats")        # run<k>/<dataset>/preds + gt
RUNS_R = os.path.join(RUNS, "traser_repeats")                 # worker logs and progress files
os.makedirs(RUNS_R, exist_ok=True)
GPUS = [x.strip() for x in os.environ.get("CUDA_VISIBLE_DEVICES", "0").split(",") if x.strip()]
GB_PER_WORKER = 15      # TRASER's peak in the earlier run: up to 14 GB per video (PVSG), about 11 GB (SVG2test)


def parse_free(text):
    """nvidia-smi 'uuid, free MiB' lines -> {uuid: free GB}."""
    out = {}
    for line in text.splitlines():
        parts = [x.strip() for x in line.split(",")]
        if len(parts) == 2 and parts[1].isdigit():
            out[parts[0]] = int(parts[1]) / 1024
    return out


def free_gb():
    r = subprocess.run(["nvidia-smi", "--query-gpu=uuid,memory.free", "--format=csv,noheader,nounits"],
                       capture_output=True, text=True)
    free = parse_free(r.stdout)
    return {g: free.get(g, 999.0) for g in GPUS}    # a GPU nvidia-smi does not list by this id: do not wait for it


def wait_for_memory():
    """Worker slots for the next step: on each GPU as many workers (up to WORKERS_PER_GPU) as its free memory allows.
    Waits (checking every 5 minutes) while another job leaves no room for even one worker on a GPU."""
    last = 0
    while True:
        free = free_gb()
        n = {g: min(max(1, WORKERS_PER_GPU), int(f // GB_PER_WORKER)) for g, f in free.items()}
        if n and all(v >= 1 for v in n.values()):
            step("GPU memory free: " + ", ".join(f"{f:.0f} GB -> {n[g]} worker(s)" for g, f in free.items()))
            return [g for g in GPUS for _ in range(n[g])]
        if time.time() - last > 1800:
            step("waiting: another job is using the GPU (" + ", ".join(f"{f:.0f} GB free" for f in free.values()) +
                 f", {GB_PER_WORKER} GB needed per worker); checking every 5 minutes, starting by itself when there is room")
            last = time.time()
        time.sleep(300)


def answered(root, ds):
    return {os.path.basename(p)[:-5] for p in glob.glob(os.path.join(root, ds, "preds", "*.json")) if not p.endswith(".stats.json")}


def run_live(cmds, label):
    """Run the commands side by side and print their output live."""
    q, procs = queue.Queue(), []
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
    bad = [i for i, p in enumerate(procs) if p.returncode]
    step(f"{label}: finished" + (f" (!! worker {bad} exited with an error, see above)" if bad else ""))


step(f"{N_RUNS} runs x {RUN_DATASETS} ({DTYPE}), up to {WORKERS_PER_GPU} worker(s) per GPU on {GPUS}; answers -> {REP}/run<k>")
t_all = time.time()
for k in range(1, N_RUNS + 1):
    root = os.path.join(REP, f"run{k}")
    for ds in RUN_DATASETS:
        vids = [v for v in IC.select_videos(ds, 0) if os.path.exists(os.path.join(B.item_dir(BENCH, ds, v), "gt.json"))]
        todo = [v for v in vids if v not in answered(root, ds)]
        step(f"run {k}, {ds}: {len(vids)} videos, {len(vids) - len(todo)} answered before, {len(todo)} to answer")
        if not todo:
            continue
        SLOTS = wait_for_memory()
        t0, cmds = time.time(), []
        for i, g in enumerate(SLOTS):
            part = todo[i::len(SLOTS)]
            if part:
                qfile = os.path.join(RUNS_R, f"run{k}_{ds}_w{i}.queue")
                open(qfile, "w").write("\n".join(part))
                cmds.append(f"CUDA_VISIBLE_DEVICES={g} HF_HOME={os.environ['HF_HOME']} python3 tools/bench_run.py "
                            f"--results {root} --bench {BENCH} --dataset {ds} --runs {RUNS_R} --dtype {DTYPE} "
                            f"--gpu_name run{k}_w{i} --videos $(cat {qfile})")
        run_live(cmds, f"run {k}, {ds}")
        n = len(answered(root, ds))
        step(f"run {k}, {ds}: {n} of {len(vids)} answered ({(time.time() - t0) / 3600:.1f} h)")
step(f"===== all runs done in {(time.time() - t_all) / 3600:.1f} h: " + ", ".join(
    f"run{k} " + "/".join(str(len(answered(os.path.join(REP, f'run{k}'), ds))) for ds in RUN_DATASETS) for k in range(1, N_RUNS + 1)))
step("next: python3 tools/repeat_report.py (asks for the NVIDIA key; judges new words with Nemotron, writes the table)")
