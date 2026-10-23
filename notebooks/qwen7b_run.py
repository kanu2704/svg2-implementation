"""Table 2 again with TRASER's language model replaced by an off-the-shelf Qwen2.5-VL-7B-Instruct (not fine-tuned), in
TRASER's own pipeline (tools/run_traser.py load_qwen), for a terminal (inside tmux on the server). It waits until
overnight_run.py and full_pairs_run.py are not running (they share the GPU), then answers every prepared video of
PVSG, SVG2test and VidOR (tools/bench_run.py --lm qwen7b) and writes results/qwen7b_bench/README.md
(tools/qwen_bench_report.py). Every step skips videos already answered: run it again after an interruption.
Setup part made from notebooks/full_pairs_run.py (cells 0a-0c of traser_pairs.ipynb): edit those, not this part.

    tmux new -s qwen
    source /media/data_dump/conda/miniconda3/etc/profile.d/conda.sh && conda activate /media/nas_mount/kanupriya/envs/traser
    cd /media/nas_mount/kanupriya/svg2-implementation && python3 notebooks/qwen7b_run.py 2>&1 | tee -a /media/nas_mount/kanupriya/qwen7b.log

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

# ----------------------------------------------------------------------------- wait for the other runs (same GPU)
for _name in ("overnight_run", "full_pairs_run"):
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


# ----------------------------------------------------------------------------- Qwen2.5-VL-7B in TRASER's pipeline
import threading, queue
from huggingface_hub import snapshot_download
QWEN_ID = "Qwen/Qwen2.5-VL-7B-Instruct"
step(f"downloading {QWEN_ID} (~16 GB, only the first time) ...")
qwen7b_dir = snapshot_download(QWEN_ID)
QRES = os.path.join(REPO, "results", "qwen7b_bench")        # answers + table (pushed to GitHub)
RUNS_Q = os.path.join(RUNS, "qwen7b")                        # worker logs and progress files
os.makedirs(RUNS_Q, exist_ok=True)
sys.path.insert(0, os.path.join(REPO, "tools"))
import bench_data as B
from interp import common as IC
GPUS = [x.strip() for x in os.environ.get("CUDA_VISIBLE_DEVICES", "0").split(",") if x.strip()]
SAVE_EVERY_MIN = 20
QDATASETS = ["pvsg", "svg2test", "vidor"]                    # short ones first

def answered(ds):
    return {os.path.basename(p)[:-5] for p in glob.glob(os.path.join(QRES, ds, "preds", "*.json")) if not p.endswith(".stats.json")}

def save_q(quiet=False):
    """git add + commit + push results/qwen7b_bench."""
    git("add", "results/qwen7b_bench")
    if git("diff", "--cached", "--quiet").returncode:
        git("commit", "-m", "Qwen2.5-VL-7B in TRASER's pipeline: " + ", ".join(f"{ds} {len(answered(ds))}" for ds in QDATASETS))
    r = git("push", "origin", f"HEAD:{BRANCH}")
    if r.returncode and ("rejected" in r.stderr or "fetch first" in r.stderr):
        git("pull", "--rebase", "--autostash", "origin", BRANCH)
        r = git("push", "origin", f"HEAD:{BRANCH}")
    if r.returncode:
        print(f"!! push failed: {r.stderr.strip().splitlines()[-1] if r.stderr.strip() else '?'} (committed locally; "
              f"push from a terminal: cd {REPO} && git push origin HEAD:{BRANCH})", flush=True)
    elif not quiet:
        step("saved to GitHub ✓ (results/qwen7b_bench)")

def run_live(cmds, label):
    """Run the commands side by side, print their output live, save to GitHub every SAVE_EVERY_MIN minutes."""
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
            save_q(quiet=True); last = time.time()
    bad = [i for i, p in enumerate(procs) if p.returncode]
    step(f"{label}: finished" + (f" (!! process {bad} exited with an error, see above)" if bad else ""))

def report():
    r = subprocess.run(["python3", "tools/qwen_bench_report.py"], capture_output=True, text=True, cwd=REPO)
    print("\n".join("    " + l for l in (r.stdout + r.stderr).strip().splitlines()[-6:]), flush=True)

t_all = time.time()
for ds in QDATASETS:
    vids = [v for v in IC.select_videos(ds, 0) if os.path.exists(os.path.join(B.item_dir(BENCH, ds, v), "gt.json"))]
    todo = [v for v in vids if v not in answered(ds)]
    step(f"{ds}: {len(vids)} videos prepared here, {len(vids) - len(todo)} answered before, {len(todo)} to answer")
    if not todo:
        continue
    cmds = []
    for i, g in enumerate(GPUS):
        part = todo[i::len(GPUS)]
        if part:
            qfile = os.path.join(RUNS_Q, f"{ds}_gpu{i}.queue")
            open(qfile, "w").write("\n".join(part))
            cmds.append(f"CUDA_VISIBLE_DEVICES={g} HF_HOME={os.environ['HF_HOME']} python3 tools/bench_run.py --lm qwen7b "
                        f"--qwen_model {qwen7b_dir} --results {QRES} --bench {BENCH} --dataset {ds} --runs {RUNS_Q} "
                        f"--gpu_name qwen_gpu{i} --videos $(cat {qfile})")
    run_live(cmds, f"Qwen2.5-VL-7B answers, {ds}")
    report()
    save_q()
step(f"answers done in {(time.time() - t_all) / 3600:.1f} h; " + ", ".join(f"{ds} {len(answered(ds))}" for ds in QDATASETS))
report()
save_q()
step("===== all done: results/qwen7b_bench/README.md =====")
