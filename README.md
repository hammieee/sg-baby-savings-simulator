# SG Baby Savings Simulator — 模拟养娃存钱

Gamified savings for Singapore: simulate raising a child, pick the real expenses you *would* pay, and each pick is money *actually saved*. Virtual spend = real saving.

**Stack:** single `index.html` (no build, no backend, no login) + `prices.json` · **Deploy:** Vercel static · **UI:** EN / 中文 toggle · **Data:** localStorage only

## Files in this folder

| File | What it is |
|---|---|
| `PROMPT_EN.md` | The full English prompt to paste into Google AI Studio (Build mode). Single language only, as requested. |
| `prices.json` | Price database v1.1.0, researched 2026-11-20, SGD, with source + verified status per item. The app embeds a copy and fetches this file from GitHub for updates. |
| `PRICE_SOURCES.md` | Every price: price / source / date / why this price / verified status. Plus the “do not hard-code” list. |
| `scripts/check_prices.py` | Price checker. Reads `prices.json`, HEAD/GETs every source URL, writes `docs/price-check-report.md`. Report only — never auto-changes a price. |
| `.github/workflows/check-prices.yml` | Runs the checker monthly (1st of month) + on demand. See below. |
| `docs/` | See `docs/WIKI.md` for the wiki structure. |

## Quick start — 3 steps to Vercel

1. Paste `PROMPT_EN.md` into Google AI Studio, attach `prices.json`, generate. Save the result as `index.html` in this repo.
2. Push to GitHub: `index.html`, `prices.json`, `scripts/`, `docs/`, `.github/`.
3. Vercel → Add New Project → Import the GitHub repo → Framework: **Other / Static**, no build command, output = root. Deploy. Done.

Edit the GitHub raw URL in `index.html` (`<YOUR_USERNAME>/<YOUR_REPO>`) so the app can fetch `prices.json` updates. If the fetch fails, the app falls back to the embedded copy.

## How the game works (decisions you made, 20 Nov 2026)

- **Identity:** player chooses SC / PR / Foreigner at setup. Subsidies change accordingly.
- **Subsidies:** net cost (Option B). MediSave Maternity Package, MediSave Grant S$5,000, Baby Bonus (pre-1 Apr 2027) vs SG Child Support Package (from 1 Apr 2027, switched by simulated birth date). Cash vs ring-fenced (CDA + MediSave Grant) shown separately — never subtract CDA/MGN from cash cost.
- **Hospital:** per-item Public / Private choice, not once for the whole game.
- **Delivery:** choose vaginal / elective C-section, hospital, ward/room, epidural yes/no. Emergency conversion: default **8%** if vaginal attempted → charge C-section median for the same hospital/ward, not vaginal + C-section.
- **Stages:** Pregnancy (10m) → 0–1y → 1–3y → 3–6y (to kindergarten graduation). 7–12y is a later update — the data is modular, see WIKI.
- **Modes:** Real-Time (1 real month = 1 game month, daily check-in) **and** Simulation (click “Next month” to fast-forward). Switch any time, progress shared. Reminder limit, stated honestly: a pure static Vercel site cannot push when the browser is closed — v1 uses in-app + browser Notification when open + calendar. True push needs a backend (v2).
- **Random events:** yes, with real costs — fever, HFMD, A&E S$176, growth spurt, birthday party, dental filling, etc.
- **No target amount** by default. Goal field is optional.
- **Player-editable prices:** every item editable, custom items allowed, “Reset to default” button. Player edits survive price updates and are badged “Edited by you”.
- **Export:** CSV with columns `date,stage,category,item,hospital_type,mandatory,amount_sgd,cumulative_sgd,source,notes` (UTF-8 BOM for Excel Chinese), plus JSON backup Export/Import.
- **Prompt language:** English only (one version). App UI is bilingual EN/中文.

## Price checker

```bash
python3 scripts/check_prices.py
# writes docs/price-check-report.md
# exit 1 if any dead link or last_checked > 180 days
```

Manual process for a price change:
1. Run the checker, open the `CHECK` URLs by hand.
2. If a price really changed, update `prices.json` + `PRICE_SOURCES.md` with the new price, source, date and reason.
3. Bump `meta.version` (1.0.0 → 1.1.0) and set `last_checked` to today.
4. Commit. The app will pick up the new `prices.json` from GitHub on next load (if the version is newer).

## GitHub Actions — monthly check

`.github/workflows/check-prices.yml` (create this file):

```yaml
name: Check prices
on:
  schedule:
    - cron: '0 0 1 * *'  # 1st of month, UTC
  workflow_dispatch: {}
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - run: python3 scripts/check_prices.py
      - uses: actions/upload-artifact@v4
        with:
          name: price-check-report
          path: docs/price-check-report.md
```

## Docs / Wiki structure

See `docs/WIKI.md`. Short version:
- `docs/README.md` — this file, copied to `docs/`
- `docs/PRICE_SOURCES.md` — the full source table (same as root `PRICE_SOURCES.md`)
- `docs/WIKI.md` — Home / How to play / Price policy / How to update a price / Version history / Roadmap (7–12y stage, true push reminders)
- `docs/price-check-report.md` — generated by the checker, do not edit by hand

## What still needs a human to check

- After AI Studio generates `index.html`, run the checklist at the end of `PROMPT_EN.md`: SC public KKH B2 vaginal vs private Thomson 1-bedded C-section totals, MediSave cap S$5,940 for a 3-day C-section, CSV columns, EN/中文 toggle on every screen.
- Prices are 20 Nov 2026 public prices. MOH delivery medians are 2023 transacted bills — they may be higher in 2026. Re-run the checker monthly.
- If you want, I can help with the 7–12y stage later — the stages are modular, so it is an add-on, not a rewrite.
