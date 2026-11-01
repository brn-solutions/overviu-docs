# Writing the Overviu docs

These docs are for hosts (the Guides tab) and developers using the Overviu API (the API reference tab). Nothing about
Overviu's internal code belongs here.

- One task per guide, in plain English: what it's for and when; "Before you start" only when needed; the steps in
  `<Steps>`; "What happens next"; "Related" links.
- **Bold is only for labels on Overviu's screens**, copied exactly from the app. `python3 scripts/check-labels.py
  ~/Sites/overviu <files>` must report 0.
- Check every fact against the app's code. When the app behaves surprisingly, say so plainly in a `<Note>` or
  `<Warning>`.
- Owner/admin-only screens open with `<Note>Only owners and admins can …</Note>`.
- Money is written with its currency (€120.00); dates as "15 October 2026".
- Hungarian pages (`hu/`) take their terms, register (formal "Ön") and date and money formats from
  `hu/GLOSSARY.md`, the same terms the app's `lang/hu.json` uses. Each mirrors the English page at the same path, with
  links into `/hu/...` (the API reference stays English). Their bold labels are the Hungarian ones, never inflected:
  "kattintson a **Mentés** gombra", not "**Mentés**re".
- A new or changed English guide needs its `hu/` page too, and both languages' navigation in `docs.json`.
  `python3 scripts/translation-prompt.py ~/Sites/overviu hu/<page>.mdx` prints a ready prompt for translating it
  (rules, glossary, the page's labels from `hu.json`).
- Before publishing Hungarian: `python3 scripts/check-labels.py --lang hu ~/Sites/overviu hu/**/*.mdx` (every bold
  phrase is a label in `hu.json`) and `python3 scripts/check-drift.py hu` (no `hu/` page behind its English one) must
  both report 0.
- Don't edit `api-reference/openapi.json` by hand: the app's CI replaces it on every push to its `main`.
- Before committing: `npx mint validate` and `npx mint broken-links`.
