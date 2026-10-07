"""Push results/traser_bench to GitHub every few minutes, in the background, independent of any notebook cell.

    nohup python3 tools/autosave.py >> /kaggle/working/autosave.log 2>&1 &
    tail /kaggle/working/autosave.log          # what it did

Saves right away, then every --every minutes when something changed. Only results/traser_bench is committed.
Needs push access (the token from notebook cell 0c, or any git credentials). Stop it with: pkill -f autosave.py
"""
import argparse
import os
import subprocess
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
BRANCH = "claude/traser-implementation-guide-xlshit"
PATH = "results/traser_bench"


def git(*args):
    return subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True,
                          env=dict(os.environ, GIT_TERMINAL_PROMPT="0"))


def log(msg):
    print(f"{time.strftime('%H:%M:%S')} {msg}", flush=True)


def save():
    n = len([p for p in (REPO / PATH).glob("*/preds/*.json") if not p.name.endswith(".stats.json")])
    for _ in range(3):                                   # the notebook's save() may hold the git lock
        r = git("add", PATH)
        if r.returncode == 0:
            break
        time.sleep(5)
    if git("diff", "--cached", "--quiet", "--", PATH).returncode:
        r = git("commit", "-m", f"TRASER bench: results ({n} predictions)", "--", PATH)
        if r.returncode:
            log(f"commit failed: {(r.stderr or r.stdout).strip()[-200:]}")
            return
    if not git("log", f"origin/{BRANCH}..HEAD", "--oneline").stdout.strip():
        git("fetch", "-q", "origin", BRANCH)
        if not git("log", f"origin/{BRANCH}..HEAD", "--oneline").stdout.strip():
            return                                        # nothing new to push
    r = git("push", "origin", f"HEAD:{BRANCH}")
    if r.returncode and ("rejected" in r.stderr or "fetch first" in r.stderr):
        git("pull", "--rebase", "--autostash", "origin", BRANCH)
        r = git("push", "origin", f"HEAD:{BRANCH}")
    if r.returncode == 0:
        log(f"saved to GitHub ✓ ({n} predictions)")
    else:
        log("push FAILED (results stay committed here): " + (r.stderr.strip().splitlines() or ["?"])[-1][:200])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--every", type=float, default=10, help="minutes between saves")
    args = ap.parse_args()
    if not git("config", "user.name").stdout.strip():
        git("config", "user.name", "kanu2704")
        git("config", "user.email", "kanu2704@users.noreply.github.com")
    log(f"autosave started: {REPO / PATH} → GitHub every {args.every:g} min")
    while True:
        try:
            save()
        except Exception as e:  # noqa: BLE001  (keep saving whatever happens)
            log(f"error: {e}")
        time.sleep(args.every * 60)


if __name__ == "__main__":
    main()
