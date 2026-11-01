#!/usr/bin/env python3
"""
Prints a complete prompt for translating one Hungarian page (hu/...) from English, ready to paste into a chat
assistant: the rules, hu/GLOSSARY.md, the page's screen labels with their exact Hungarian text from the app's
lang/hu.json, and the page. The page under hu/ starts as a copy of the English one; paste the answer over it.

Usage: python3 scripts/translation-prompt.py ~/Sites/overviu hu/bookings/create-a-booking.mdx | pbcopy
"""
import json
import pathlib
import re
import sys

app = pathlib.Path(sys.argv[1]).expanduser()
page = pathlib.Path(sys.argv[2])
english = pathlib.Path(*page.parts[1:]) if page.parts[0] == "hu" else page
docs = pathlib.Path(__file__).resolve().parent.parent
hungarian = json.loads((app / "lang/hu.json").read_text())


def label(phrase):
    """The app's Hungarian for an English screen label; "A → B" is looked up a part at a time."""
    if phrase in hungarian:
        return hungarian[phrase]
    parts = phrase.split(" → ")
    if len(parts) > 1 and all(part in hungarian for part in parts):
        return " → ".join(hungarian[part] for part in parts)
    return None


phrases = list(dict.fromkeys(re.findall(r"\*\*([^*]+)\*\*", (docs / english).read_text())))
known = [(phrase, label(phrase)) for phrase in phrases if label(phrase) is not None]
unknown = [phrase for phrase in phrases if label(phrase) is None]

labels = "\n".join(f"| {en} | {hu} |" for en, hu in known) or "| (none) | |"
unknown_note = (
    "\nThese bold labels have no Hungarian text in the app's translation file. Keep them exactly as they are, in "
    "bold, and list them after the code block so they can be checked: " + ", ".join(unknown) + "\n"
    if unknown else ""
)

print(f"""Translate this page of Overviu's help docs (docs.overviu.app) from English into Hungarian. Overviu is an app
for running holiday rentals; the readers are hosts using its Hungarian interface.

Return the whole translated file in a single ```mdx code block and nothing else{", apart from the list of unknown labels" if unknown else ""}.

## Rules

1. Register: formal "Ön" everywhere ("Kattintson", "Nyissa meg", "Az Ön foglalási weboldala"). Never "te"
   ("kattints", "fiókod").
2. Bold is only for labels on Overviu's screens. Replace every **bold** English label with its Hungarian label from the
   table below, character for character, keeping the capital letters. Never put a suffix inside the bold and never
   inflect a label: write "kattintson a **Mentés** gombra", "a **Foglalások** oldalon", not "**Mentés**re". Rephrase the
   sentence around the label instead (add "gomb", "oldal", "menü", "mező", "kapcsoló", "fül" as Hungarian needs).
   Don't make anything else bold.
3. Keep the MDX exactly as it is: the frontmatter keys, the components and their attribute names (<Steps>, <Step>,
   <Note>, <Warning>, <Tip>, <Card>, <CardGroup>, <Accordion>, <Frame>), every link URL and href (already pointing at
   /hu/...), code blocks, `inline code`, placeholders such as {{guest_first_name}} or {{listing}}, and the line and
   paragraph structure. Translate the frontmatter title and description, the title="..." of steps, cards and
   accordions, headings, link text and the body.
4. Terms: use the glossary below and nothing else for its concepts, even where another word seems more natural: a
   listing is a "szálláshirdetés" (not "szálláshely"), the host a "szállásadó" (not "házigazda"), the dashboard
   "Műszerfal" (not "irányítópult"), reports "Jelentések" (not "kimutatások"), the inbox "Beérkezett üzenetek". Keep brand and technical names (Airbnb,
   Booking.com, Stripe, Wi-Fi, API, CNAME, Webhook) as they are.
5. Formats: dates as "2026. október 15.", short dates as "okt. 15.", money with a space between thousands, a decimal
   comma and the currency after the amount ("1 200,50 EUR", "12 000 Ft"). Convert the English examples
   ("€120.00" → "120,00 EUR", "15 October 2026" → "2026. október 15.").
6. Write natural Hungarian a host would expect from a well-made app, not word for word. Keep every fact, number,
   condition and warning; add nothing and leave nothing out. Headings in Hungarian sentence case.

## Screen labels on this page

| English | Hungarian (use exactly) |
|---|---|
{labels}
{unknown_note}
## Glossary

{(docs / "hu/GLOSSARY.md").read_text().strip()}

## The page

```mdx
{page.read_text().strip()}
```""")
