#!/usr/bin/env python3
"""
Lists links to a #anchor that no heading on the target page answers to: a heading's own slug, or its custom ID
({#channels}). Translated headings keep the English anchor as a custom ID, so links stay the same in every language.
`mint broken-links` checks pages, not anchors.

Usage: python3 scripts/check-anchors.py hu/**/*.mdx
"""
import pathlib
import re
import sys

docs = pathlib.Path(__file__).resolve().parent.parent


def anchors(page):
    found = set()
    for heading in re.findall(r"^#{2,6} (.+)$", page.read_text(), re.M):
        custom = re.search(r"\{#([^}]+)\}\s*$", heading)
        found.add(custom.group(1) if custom else re.sub(r"\s+", "-", re.sub(r"[^\w\s-]", "", heading.lower())).strip("-"))
    return found


broken = []
for name in sys.argv[1:]:
    page = pathlib.Path(name)
    for path, anchor in re.findall(r'(?:\]\(|href=")(/[^)#"]*)?#([^)"]+)', page.read_text()):
        target = docs / f"{path[1:]}.mdx" if path else page
        if target.exists() and anchor not in anchors(target):
            broken.append(f"{name}: {path or ''}#{anchor}")

print("\n".join(broken))
print(f"{len(broken)} link(s) to a missing anchor")
sys.exit(1 if broken else 0)
