# Wiki — SG Baby Savings Simulator

## Home
Gamified savings for Singapore. Virtual spend = real saving. Single `index.html` + `prices.json`, Vercel static, EN/中文 toggle, localStorage only.

## How to play
1. Choose identity (SC / PR / Foreigner), birth order, simulated birth date.
2. Choose mode: Real-Time (1 real month = 1 game month, daily check-in) or Simulation (click Next month).
3. Each stage, pick items. Per item choose Public / Private. Mandatory vs Optional is tagged.
4. Delivery screen: mode, hospital, ward, epidural. 8% default emergency conversion if vaginal attempted.
5. Monthly review: recurring items auto-added, uncheck / change brand / quantity before confirming.
6. Random events appear as cards — Pay/Save or Skip (logged).
7. Dashboard shows total / this month / this stage / by category. Export CSV or JSON backup any time.

## Price policy
- Every price has a source + date + Verified / Estimate / Unverified badge.
- MOH delivery = 2023 median, not a quote, not a package price.
- CDA + MediSave Grant are ring-fenced, never subtracted from cash cost.
- Player edits are never silently overwritten by a price update.
- Unverified items show “—”, never a guessed number. Full list in `PRICE_SOURCES.md` §7.

## How to update a price
1. `python3 scripts/check_prices.py` — read `docs/price-check-report.md`.
2. Open CHECK links by hand, confirm the new price.
3. Edit `prices.json` + `PRICE_SOURCES.md` (price, source, date, reason).
4. Bump `meta.version`, set `last_checked` to today.
5. Commit + push. App fetches the new file if version is newer.

## Version history
- **v1.0.0 — 2026-11-20:** First researched version. Stages Pregnancy → 0–6y. MOH 2023 delivery medians; FairPrice/KKH/ECDA/CPF/MSF Nov 2026 prices.
- **v1.1.0 — 2026-11-20:** Added twins, jaundice, NICU tiers, GDM/preeclampsia, child status (Health/Happiness/Development), gifts, medicine cabinet, full-month/100-day/Zhuazhou, helper, breastfeeding, second-hand, inflation 2.0%, interest 2.5%. End-simulation is player-initiated only (Option A).

## Roadmap
- **v1.1:** 7–12y Primary stage (new module in `prices.json`, no rewrite — stages are modular).
- **v1.2:** True push reminders (needs a backend — out of scope for static Vercel v1).
- **v1.3:** Multi-child save slots (currently single-child; JSON backup already supports it).

## FAQ
- **Can I change a price?** Yes, in-app Edit, or edit `prices.json` directly.
- **What if GitHub is down?** App uses the embedded copy in `index.html`.
- **Is this financial advice?** No. It is a savings-simulation game. Verify real costs with the hospital/retailer.
