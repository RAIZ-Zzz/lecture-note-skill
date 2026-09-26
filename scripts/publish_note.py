"""Publish a prepared lecture note (and its slide screenshots) into the Obsidian vault.

  python publish_note.py NOTE_MD "Lecture Notes/<course>/WEEK n.md" \
      --image SRC=weekN.P-topic-sNN.png|weekN-topic-anim-slug.svg [--image ...] \
      (--new | --baseline SAVED_COPY_OF_CURRENT_NOTE.md)

Safety rules:
  --new       the destination note must not exist yet.
  --baseline  the live note must still equal this saved copy (made right after you read it),
              so edits made in Obsidian meanwhile are never overwritten.
  An attachment name that already exists with different bytes is an error, never overwritten.
Afterwards the note is read back through cli-anything-obsidian and every ![[...]] embed is checked.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

VAULT = Path(os.environ.get("OBSIDIAN_VAULT", r"D:\obsidian\repo\NTULEARN"))


def cli(*args):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    run = subprocess.run(["cli-anything-obsidian", "--json", "--vault", str(VAULT), *args],
                         capture_output=True, text=True, encoding="utf-8", env=env)
    try:
        data = json.loads(run.stdout) if run.stdout.strip() else {}
    except json.JSONDecodeError:
        data = {"error": run.stdout.strip() or run.stderr.strip()}
    if run.returncode != 0 and "error" not in data:
        data["error"] = run.stderr.strip() or f"exit {run.returncode}"
    return data


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def fail(message):
    print(json.dumps({"ok": False, "error": message}, ensure_ascii=False))
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("note_file")
    parser.add_argument("vault_path")
    parser.add_argument("--image", action="append", default=[], help="SRC=ATTACHMENT_NAME")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--new", action="store_true")
    mode.add_argument("--baseline")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    vault_path = args.vault_path if args.vault_path.endswith(".md") else args.vault_path + ".md"
    body = Path(args.note_file).read_text(encoding="utf-8")
    attachments_dir = VAULT / Path(vault_path).parent / "attachments"

    current = cli("vault", "read", vault_path)
    exists = "content" in current
    if args.new and exists:
        fail(f"{vault_path} already exists; read it, save a baseline copy and use --baseline")
    if args.baseline:
        if not exists:
            fail(f"{vault_path} does not exist; use --new")
        if current["content"] not in (Path(args.baseline).read_text(encoding="utf-8"), body):
            fail(f"{vault_path} changed since the baseline was saved; re-read and merge first")

    plan = []
    for item in args.image:
        src, _, name = item.partition("=")
        if not name or not Path(src).is_file():
            fail(f"bad --image {item!r}")
        dest = attachments_dir / name
        if dest.exists() and digest(dest) != digest(src):
            fail(f"different attachment already exists: {dest}")
        plan.append((src, dest))
    attachments_dir.mkdir(parents=True, exist_ok=True)
    for src, dest in plan:
        if not dest.exists():
            shutil.copyfile(src, dest)

    if not exists:
        result = cli("vault", "create", vault_path, "--file", args.note_file)
    elif current["content"] != body:
        result = cli("vault", "update", vault_path, "--file", args.note_file)
    else:
        result = {}
    if result.get("error"):
        fail(f"write failed: {result['error']}")

    after = cli("vault", "read", vault_path)
    if after.get("content") != body:
        fail("saved content differs from the prepared note")
    missing = [e for e in re.findall(r"!\[\[([^\]|#]+)", body)
               if not (VAULT / e).exists() and not list(VAULT.rglob(Path(e).name))]
    if missing:
        fail(f"note saved, but these embeds do not resolve: {missing}")

    print(json.dumps({
        "ok": True,
        "note": vault_path,
        "action": "created" if not exists else ("updated" if current["content"] != body else "unchanged"),
        "chars": len(body),
        "attachments": [str(d) for _, d in plan],
    }, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
