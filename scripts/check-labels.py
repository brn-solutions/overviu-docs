#!/usr/bin/env python3
"""
Bold in the guides is only for labels on Overviu's screens. This lists every **bold** phrase in the given MDX files
that doesn't appear in the app's Blade views, PHP code or seeders, so a misspelled or outdated label is caught before a host
looks for a button that isn't there.

With --lang hu the labels are the Hungarian ones: the values of the app's lang/hu.json, which is every Hungarian
string the app shows. "A → B" passes when each part does.

Usage: python3 scripts/check-labels.py ~/Sites/overviu get-started/*.mdx
       python3 scripts/check-labels.py --lang hu ~/Sites/overviu hu/get-started/*.mdx
"""
import json
import pathlib
import re
import sys

args = sys.argv[1:]
lang = "en"
if args[:1] == ["--lang"]:
    lang, args = args[1], args[2:]

app = pathlib.Path(args[0]).expanduser()
if lang == "en":
    # Seeders hold the labels of the reference lists, like property types and fee types.
    sources = [*(app / "resources/views").rglob("*.blade.php"), *(app / "app").rglob("*.php"), *(app / "database/seeders").rglob("*.php")]
    corpus = "\n".join(path.read_text(errors="ignore") for path in sources).replace("\\'", "'")
else:
    corpus = "\n".join(json.loads((app / f"lang/{lang}.json").read_text()).values())
    # Plan names (Solo, Host, Pro) are shown as they are in every language.
    corpus += "\n" + "\n".join(re.findall(r"'name' => '([^']+)'", (app / "config/billing.php").read_text()))

missing = []
for name in args[1:]:
    for phrase in re.findall(r"\*\*([^*]+)\*\*", pathlib.Path(name).read_text()):
        if phrase not in corpus and not all(part in corpus for part in phrase.split(" → ")):
            missing.append(f"{name}: {phrase}")

print("\n".join(missing))
print(f"{len(missing)} bold phrase(s) not found in the app")
sys.exit(1 if missing else 0)
