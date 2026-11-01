#!/usr/bin/env python3
"""
Lists the translated pages (hu/...) whose English page has changed since the translation was last committed, and the
English guides that have no translation yet, so a language isn't published out of step with English.

Usage: python3 scripts/check-drift.py hu
"""
import json
import pathlib
import subprocess
import sys

lang = sys.argv[1]
docs = pathlib.Path(__file__).resolve().parent.parent


def git(*args):
    return subprocess.run(["git", *args], cwd=docs, capture_output=True, text=True, check=True).stdout.strip()


navigation = json.loads((docs / "docs.json").read_text())["navigation"]
english = next(entry for entry in navigation["languages"] if entry["language"] == "en")
guides = [page for tab in english["tabs"] if not tab["tab"].startswith("API") for group in tab["groups"] for page in group.get("pages", [])]

problems = []
for page in guides:
    source, translation = f"{page}.mdx", f"{lang}/{page}.mdx"
    translated_at = git("log", "-1", "--format=%H", "--", translation)
    if not translated_at:
        problems.append(f"{translation}: not translated yet")
    elif git("log", "--format=%h %s", f"{translated_at}..HEAD", "--", source):
        problems.append(f"{translation}: {source} changed since ({git('log', '-1', '--format=%h', f'{translated_at}..HEAD', '--', source)})")
    elif git("status", "--porcelain", "--", source):
        problems.append(f"{translation}: {source} has uncommitted changes")

print("\n".join(problems))
print(f"{len(problems)} {lang} page(s) out of step with English")
sys.exit(1 if problems else 0)
