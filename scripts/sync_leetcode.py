#!/usr/bin/env python3
"""Sync accepted LeetCode submissions into this repo.

Fetches every accepted submission for the logged-in account, keeps the
latest one per (problem, language), writes solution files into
per-language folders, regenerates the README index, and commits + pushes
if anything changed.

Auth comes from a `.session` file in the repo root (gitignored):

    LEETCODE_SESSION=eyJ...
    CSRF=...

Designed to run from cron:
    0 9 * * * /usr/bin/python3 <repo>/scripts/sync_leetcode.py >> ~/Library/Logs/leetcode_sync.log 2>&1

On session expiry it posts a macOS notification and exits 1.
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESSION_FILE = os.path.join(REPO, ".session")
META_CACHE = os.path.join(REPO, ".meta_cache.json")

LANG_INFO = {
    "python": ("python", "py"), "python3": ("python", "py"),
    "pythondata": ("pandas", "py"),
    "java": ("java", "java"), "c": ("c", "c"), "cpp": ("cpp", "cpp"),
    "csharp": ("csharp", "cs"), "javascript": ("javascript", "js"),
    "typescript": ("typescript", "ts"), "golang": ("go", "go"),
    "rust": ("rust", "rs"), "swift": ("swift", "swift"),
    "kotlin": ("kotlin", "kt"), "ruby": ("ruby", "rb"),
    "scala": ("scala", "scala"), "php": ("php", "php"),
    "mysql": ("sql", "sql"), "mssql": ("sql", "sql"), "oraclesql": ("sql", "sql"),
    "bash": ("bash", "sh"), "racket": ("racket", "rkt"),
    "erlang": ("erlang", "erl"), "elixir": ("elixir", "ex"),
    "dart": ("dart", "dart"),
}
COMMENT = {
    "python": "#", "pandas": "#", "java": "//", "c": "//", "cpp": "//",
    "csharp": "//", "javascript": "//", "typescript": "//", "go": "//",
    "rust": "//", "swift": "//", "kotlin": "//", "ruby": "#", "scala": "//",
    "php": "//", "sql": "--", "bash": "#", "racket": ";", "erlang": "%",
    "elixir": "#", "dart": "//",
}
LANG_NAMES = {
    "python": "Python", "pandas": "Pandas", "sql": "SQL", "cpp": "C++",
    "java": "Java", "c": "C", "csharp": "C#", "javascript": "JavaScript",
    "typescript": "TypeScript", "go": "Go", "rust": "Rust", "swift": "Swift",
    "kotlin": "Kotlin", "ruby": "Ruby", "scala": "Scala", "php": "PHP",
    "bash": "Bash", "racket": "Racket", "erlang": "Erlang",
    "elixir": "Elixir", "dart": "Dart",
}


def log(msg):
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}", flush=True)


def notify(title, text):
    try:
        subprocess.run(
            ["osascript", "-e",
             f'display notification "{text}" with title "{title}"'],
            check=False, capture_output=True,
        )
    except Exception:
        pass


def load_session():
    if not os.path.exists(SESSION_FILE):
        log(f"ERROR: no session file at {SESSION_FILE}")
        notify("LeetCode sync", "Missing .session file — sync skipped.")
        sys.exit(1)
    vals = {}
    with open(SESSION_FILE) as f:
        for line in f:
            if "=" in line:
                k, _, v = line.strip().partition("=")
                vals[k.strip()] = v.strip()
    if "LEETCODE_SESSION" not in vals or "CSRF" not in vals:
        log("ERROR: .session must define LEETCODE_SESSION and CSRF")
        sys.exit(1)
    return vals["LEETCODE_SESSION"], vals["CSRF"]


SESSION, CSRF = load_session()
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    ),
    "Referer": "https://leetcode.com/submissions/",
    "Origin": "https://leetcode.com",
    "x-csrftoken": CSRF,
    "Cookie": f"LEETCODE_SESSION={SESSION}; csrftoken={CSRF}",
    "Accept": "application/json",
}


def api(url, payload=None, retries=4):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(
        url, data=data, headers=dict(HEADERS),
        method="POST" if data else "GET",
    )
    if data:
        req.add_header("Content-Type", "application/json")
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code in (401, 403):
                log(f"AUTH ERROR: HTTP {e.code} — session likely expired")
                notify(
                    "LeetCode sync: session expired",
                    "Update LEETCODE_SESSION in the repo's .session file.",
                )
                sys.exit(1)
            if e.code == 429 and attempt < retries - 1:
                wait = 15 * (attempt + 1)
                log(f"rate limited, backing off {wait}s")
                time.sleep(wait)
                continue
            raise
    raise RuntimeError("retries exhausted")


def fetch_submissions():
    subs, offset = [], 0
    while True:
        page = api(f"https://leetcode.com/api/submissions/?offset={offset}&limit=20")
        dump = page.get("submissions_dump", [])
        subs.extend(dump)
        if not page.get("has_next") or not dump:
            return subs
        offset += 20
        time.sleep(1.5)


def question_meta(slug, cache):
    if slug not in cache:
        q = api(
            "https://leetcode.com/graphql",
            {
                "query": "query q($slug: String!) { question(titleSlug: $slug) "
                         "{ questionFrontendId title difficulty } }",
                "variables": {"slug": slug},
            },
        )["data"]["question"]
        cache[slug] = q
        time.sleep(0.8)
    return cache[slug]


def clean_title(title):
    return "_".join(re.sub(r"[^A-Za-z0-9 ]", "", title).split())


def write_readme(manifest):
    probs = {}
    for e in manifest:
        p = probs.setdefault(e["id"], {
            "title": e["title"], "slug": e["slug"],
            "difficulty": e["difficulty"], "files": [],
        })
        p["files"].append((e["folder"], e["file"]))
    langs = {}
    for e in manifest:
        langs[e["folder"]] = langs.get(e["folder"], 0) + 1
    diffs = {}
    for p in probs.values():
        diffs[p["difficulty"]] = diffs.get(p["difficulty"], 0) + 1

    lines = [
        "# LeetCode Solutions",
        "",
        f"Solutions to **{len(probs)}** LeetCode problems, organized by language. "
        f"Difficulty breakdown: {diffs.get('Easy', 0)} Easy · "
        f"{diffs.get('Medium', 0)} Medium · {diffs.get('Hard', 0)} Hard.",
        "",
        "| Language | Solutions |",
        "|----------|-----------|",
    ]
    for folder in sorted(langs, key=lambda k: -langs[k]):
        lines.append(f"| [{LANG_NAMES.get(folder, folder)}]({folder}/) | {langs[folder]} |")
    lines += ["", "## Index", "", "| # | Problem | Difficulty | Solution |",
              "|---|---------|------------|----------|"]
    for pid in sorted(probs):
        p = probs[pid]
        sols = " · ".join(
            f"[{LANG_NAMES.get(folder, folder)}]({file})"
            for folder, file in sorted(p["files"])
        )
        lines.append(
            f"| {pid} | [{p['title']}](https://leetcode.com/problems/{p['slug']}/) "
            f"| {p['difficulty']} | {sols} |"
        )
    lines.append("")
    path = os.path.join(REPO, "README.md")
    content = "\n".join(lines)
    old = open(path).read() if os.path.exists(path) else ""
    if content != old:
        open(path, "w").write(content)
        return True
    return False


def git(*args, check=True):
    return subprocess.run(
        ["git", *args], cwd=REPO, check=check,
        capture_output=True, text=True,
    )


def main():
    log("sync start")
    subs = fetch_submissions()
    accepted = [s for s in subs if s.get("status_display") == "Accepted"]
    log(f"{len(subs)} submissions, {len(accepted)} accepted")

    best = {}
    for s in accepted:
        folder = LANG_INFO.get(s["lang"], (s["lang"], "txt"))[0]
        key = (s["title_slug"], folder)
        if key not in best or int(s["timestamp"]) > int(best[key]["timestamp"]):
            best[key] = s

    cache = {}
    if os.path.exists(META_CACHE):
        cache = json.load(open(META_CACHE))

    manifest, changed = [], []
    for (slug, folder), s in best.items():
        q = question_meta(slug, cache)
        _, ext = LANG_INFO.get(s["lang"], (s["lang"], "txt"))
        fname = f"{q['questionFrontendId']}_{clean_title(q['title'])}.{ext}"
        rel = f"{folder}/{fname}"
        path = os.path.join(REPO, rel)
        cm = COMMENT.get(folder, "#")
        content = (
            f"{cm} {q['questionFrontendId']}. {q['title']}\n"
            f"{cm} https://leetcode.com/problems/{slug}/\n"
            f"{cm} Difficulty: {q['difficulty']} | Language: {s['lang']} | "
            f"Runtime: {s.get('runtime', '?')} | Memory: {s.get('memory', '?')}\n\n"
            + s["code"].rstrip() + "\n"
        )
        old = open(path).read() if os.path.exists(path) else None
        if content != old:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, "w").write(content)
            changed.append(rel)
        manifest.append({
            "id": int(q["questionFrontendId"]), "title": q["title"],
            "slug": slug, "difficulty": q["difficulty"],
            "folder": folder, "file": rel,
        })

    json.dump(cache, open(META_CACHE, "w"), indent=2)
    readme_changed = write_readme(manifest)

    if not changed and not readme_changed:
        log("no new solutions — nothing to do")
        return

    log(f"changed files: {changed or ['README.md']}")
    git("add", "-A")
    if not git("diff", "--cached", "--quiet", check=False).returncode:
        log("nothing staged after add — done")
        return
    n = len(changed)
    msg = f"Sync {n} solution{'s' if n != 1 else ''} from LeetCode (auto)" if n \
        else "Update README (auto sync)"
    git("commit", "-m", msg)
    git("pull", "--rebase", "origin", "main")
    git("push", "origin", "main")
    log(f"pushed: {msg}")
    if n:
        notify("LeetCode sync", f"Imported {n} new solution{'s' if n != 1 else ''}.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log(f"FAILED: {e}")
        notify("LeetCode sync failed", str(e)[:120])
        sys.exit(1)
