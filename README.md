# Overviu documentation

The source of https://docs.overviu.app, deployed by Mintlify from `main`.

- Preview locally: `npx mint dev` (http://localhost:3000).
- Check before committing: `npx mint validate`, `npx mint broken-links`, `python3 scripts/check-labels.py ~/Sites/overviu <changed .mdx files>`.
- The API reference (`api-reference/openapi.json`) comes from the app: its `api-docs` GitHub workflow exports it and
  commits it here on every push to the app's `main`.
- Writing rules: `AGENTS.md`.
