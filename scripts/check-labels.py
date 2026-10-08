#!/usr/bin/env python3
"""
Bold in the guides is only for labels on Overviu's screens. This lists every **bold** phrase in the given MDX files
that doesn't appear in the app's Blade views or PHP code, so a misspelled or outdated label is caught before a host
looks for a button that isn't there.

Usage: python3 scripts/check-labels.py ~/Sites/overviu get-started/*.mdx
"""
import pathlib
import re
import sys

app = pathlib.Path(sys.argv[1]).expanduser()
sources = [*(app / "resources/views").rglob("*.blade.php"), *(app / "app").rglob("*.php")]
corpus = "\n".join(path.read_text(errors="ignore") for path in sources).replace("\\'", "'")

missing = []
for name in sys.argv[2:]:
    for phrase in re.findall(r"\*\*([^*]+)\*\*", pathlib.Path(name).read_text()):
        if phrase not in corpus:
            missing.append(f"{name}: {phrase}")

print("\n".join(missing))
print(f"{len(missing)} bold phrase(s) not found in the app")
sys.exit(1 if missing else 0)
