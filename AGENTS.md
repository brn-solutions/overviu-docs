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
- Don't edit `api-reference/openapi.json` by hand: the app's CI replaces it on every push to its `main`.
- Before committing: `npx mint validate` and `npx mint broken-links`.
