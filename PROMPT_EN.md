# Google AI Studio Prompt — SG Baby Savings Simulator
## 模拟养娃存钱 · Singapore

**Copy everything below the line into Google AI Studio (Build mode). One language only: English. The app UI itself must be bilingual EN / 中文 with a toggle.**

---

Build a single-file web app called **“SG Baby Savings Simulator — 模拟养娃存钱”**.

It is a gamified savings tool for Singapore: the player simulates raising a child, selects the real expenses they *would* pay at each stage, and each selected expense is treated as money *actually saved* into a separate savings pot. Virtual spend = real saving. The point is to build a savings habit and to feel, concretely, what raising a child in Singapore costs.

### 1. Tech — must follow exactly

- Output ONE file only: `index.html`. No build step, no backend, no login, no database.
- It must run as-is on Vercel as a static site: drag `index.html` (plus `prices.json` in the same repo) to Vercel and it works.
- Use vanilla HTML + CSS + JavaScript in that one file. You may use a CDN for Tailwind and for charts (Chart.js), but the app MUST still load and show the core ledger if the CDN is offline — do not make the app depend on a CDN to render.
- Responsive: phone-first, works on mobile and desktop. Large tap targets, no horizontal scroll on a 360px phone.
- All data is stored in the browser with `localStorage`. No data leaves the device. Add Export / Import JSON backup.
- Language: the UI is fully bilingual. Every label, button, item name, category, stage, help text and empty state exists in BOTH English and Chinese in one `I18N` dictionary in the code. A top-right toggle `EN | 中文` switches the whole UI instantly, and the choice is saved in `localStorage`. Default language: English. Do NOT auto-translate with an API — use the dictionary only.
- Currency is SGD everywhere. Format as `S$1,234.56`.

### 2. Price data — do NOT invent prices

Use the price database supplied in `prices.json` (version 1.0.0, researched 20 Nov 2026, SGD). Embed a copy of that data as a `const PRICES` object inside `index.html` as the fallback.

On load, the app must ALSO try to fetch the latest price file from GitHub:
`https://raw.githubusercontent.com/<YOUR_USERNAME>/<YOUR_REPO>/main/prices.json`
- If the fetch succeeds AND `meta.version` is newer than the embedded version, use the fetched prices and show a small banner: “Prices updated to vX.Y.Z (20 Nov 2026) · Source: GitHub” / “价格已更新至 vX.Y.Z”.
- If the fetch fails, is offline, or the version is the same, silently use the embedded copy and show “Offline prices — embedded v1.0.0” in the Sources page. Never block the app on a failed fetch. Never show a price with no source.
- Every item in the app must show, on tap / on its detail row: price, source name, source URL (as a link), `last_checked` date, and a badge `Verified` / `Estimate` / `Unverified — do not hard-code`. For items in `not_verified_do_not_hardcode` in `prices.json`, show them as editable ranges or as “—” with the note, never as a fake exact price.

Key facts from `prices.json` you must respect in the logic:
- MOH delivery bills are **median transacted bills for Singapore Citizens, 1 Jan–31 Dec 2023, incl. GST, before MediSave**. Public-hospital figures are AFTER government subsidy; private figures are NOT subsidised.
- A hospital “maternity package” price covers **hospital charges ONLY — professional fees excluded**. It is NOT the total delivery bill. Never present a package price as the total.
- Delivery: use the MOH median for the chosen hospital + ward. Vaginal (uncomplicated) examples: KKH Ward C S$1,385, KKH Ward B2 S$1,486, NUH Ward C S$946, Thomson 1-bedded S$10,802, Mount Elizabeth Orchard 1-bedded S$12,597. C-section (uncomplicated): KKH Ward B2 S$2,733, KKH Ward C S$3,148, Thomson 1-bedded S$15,074, Mount Elizabeth Orchard 1-bedded S$19,494. Show the range (25th–75th percentile) next to the median where given.
- Epidural is an extra: public subsidised is included/minimal, KKH B1 ~S$800–1,200, KKH A ~S$1,000–1,500, private S$1,200–2,000. Anaesthetist benchmark S$817.50–1,090. Show it as a range, editable.
- Antenatal: 8–10 visits. Public subsidised visit S$37.20–101.49 (KKH, first visit), private S$111.40–222.14. OSCAR (11–14w) is optional, S$200 public / S$300–400 private. NIPT is optional, self-funded, NOT MediSave-claimable, S$680 public / S$1,200–1,400 private (Harmony/Panorama). Detailed anomaly/TIFFA scan (18–22w) is routine, ~S$150 public / ~S$350 private. OGTT (24–28w) is routine, S$35 public / S$90 private. GBS swab (35–37w) is routine and reported as included — show S$0 / included, do not invent a price.
- Subsidies, Option B (net cost): the player first chooses identity — SC / PR / Foreigner — and birth order (1st / 2nd / 3rd / 4th / 5th+), and a simulated birth date.
  - MediSave Maternity Package (SC + PR only): pre-delivery up to S$900, vaginal S$1,120, assisted vaginal S$1,390, C-section S$2,380, hospital S$1,130/day for the first 2 days, S$400/day from day 3. Worked max: vaginal 2-day stay S$4,280; C-section 3-day stay S$5,940.
  - MediSave Grant for Newborns: S$5,000 for SC newborns born on/after 1 Apr 2025. It is MediSave, NOT cash — show it separately, do NOT subtract it from cash cost.
  - Baby Bonus (babies born BEFORE 1 Apr 2027, child must be SC): 1st child Cash Gift S$11,000 total, CDA First Step S$5,000, CDA co-matching cap S$4,000. 3rd+ child: Cash Gift S$13,000, First Step S$10,000, co-matching cap S$9,000. Cash Gift is staggered (only S$3,000 at birth for 1st/2nd) — do not show it as all-at-birth. CDA is ring-fenced, not cash.
  - SG Child Support Package (babies born ON/AFTER 1 Apr 2027): up to S$62,000 total regardless of birth order. The app must switch tables by simulated birth date. Do NOT mix the two schemes.
  - Show three separate totals everywhere: **Gross cost / MediSave + subsidies used / Net cash out-of-pocket**, and separately **Cash received (Baby Bonus cash) vs Ring-fenced (CDA + MediSave Grant)**. Never subtract CDA/MGN from cash cost.
  - PR: lower subsidy than SC; Baby Bonus/CDA/MGN only if the CHILD is SC. Foreigner: no subsidy, no MediSave, no Baby Bonus/CDA/MGN — pay unsubsidised A/B1 rates at public hospitals or private rates.

### 3. Game structure — stages

Stages, in order, modular so a 7–12y stage can be added later without rewriting the app:
1. **Pregnancy — 孕期 (10 months / ~40 weeks)**
2. **Newborn — 新生儿期 0–1y**
3. **Toddler — 幼儿期 1–3y**
4. **Preschool — 学龄前期 3–6y (to kindergarten graduation)**

Each stage has its own item list from `prices.json`, grouped by category (Antenatal / Feeding / Diapers / Gear / Healthcare / Childcare / Enrichment / Clothing / Food / Confinement).
Each item shows: name (EN + ZH), category, `Mandatory 必须` or `Optional 可选` tag, `Public 公立` price vs `Private 私立` price, frequency (one-off / monthly / per visit / per term), source, and a checkbox / “Save this” button.

Per-item hospital choice: the player chooses Public or Private **per item**, not once for the whole game, because in real life you can switch freely. Keep the last choice as the default for the next item, but always allow changing it.

### 4. Delivery — the most important choice

At the end of Pregnancy, show a dedicated Delivery screen:
- Choose delivery mode: **Vaginal 自然产** or **Elective C-section 剖腹产**. Show the MOH median + range for the chosen hospital + ward for that mode.
- Choose hospital: KKH / NUH / SGH / Thomson / Mount Elizabeth Orchard / Mount Elizabeth Novena / Gleneagles / Parkway East / Raffles / Mt Alvernia.
- Choose ward/room: public C (5–6 bedded, subsidised) / B2 (5–6 bedded, subsidised) / B1 (4-bedded, unsubsidised) / A (1-bedded, unsubsidised) / private 4-bedded / 2-bedded / 1-bedded.
- Choose epidural: Yes / No, with its extra cost shown.
- **Emergency event (random, default 8%):** if the player attempted Vaginal, roll once at delivery. On an emergency, show a clear event card: “Attempted vaginal → Emergency C-section 转紧急剖腹产”, charge the **C-section median for the SAME hospital/ward, NOT vaginal + C-section**, add the longer stay (3–4 days vs 2 days), and explain why. The 8% probability must be editable in Settings. Do not invent a separate “emergency surcharge” price — there is no published one.
- After delivery, apply MediSave Maternity Package automatically, show gross vs MediSave used vs net cash, then show Baby Bonus / CDA / MGN as a separate “Government support received” panel with its staggered timing.

### 5. Two play modes — player chooses, can switch any time, progress is shared

- **Real-Time Mode 真实模式:** 1 real month = 1 game month. The player checks in daily. Show a daily check-in button, a streak counter, and the current game month. In-app reminder when the app is open. If the browser grants Notification permission, schedule a local reminder; if not, show a gentle in-app banner instead. Do NOT claim push notifications work when the browser is closed — a pure static Vercel site cannot push when closed without a backend. State that honestly in the Help page.
- **Simulation Mode 模拟模式:** a “Next month 下个月” button fast-forwards one game month. The player can play the whole 0–6y journey in one sitting. Monthly recurring items (formula, diapers, childcare) are auto-added each month in both modes, with a monthly review screen where the player can uncheck / change brand / change quantity before confirming.
- Switching modes never resets progress. Show the current mode clearly at the top.

### 6. Random events — as realistic as possible

Trigger random events by month, with the probabilities in `prices.json` (`random_events`). Examples, with their real Singapore costs:
- Baby fever — polyclinic S$9 (SC) / GP S$40–80 — 8%/month
- HFMD / ear infection — paediatrician S$80–150 all-in — 4%/month
- Fall / injury — KKH Children’s Emergency S$176 flat — 2%/month
- Growth spurt — new clothes S$50–100 — 6%/month
- Birthday party (once a year, age 3–6) — S$490–860 typical
- Dental filling — polyclinic S$20.20–36.10 tooth-coloured, private S$80–250
Each event is a card with a story (“宝宝发烧了…”), the cost, the source, and two buttons: “Pay / Save this amount 存下这笔” and “Skip 跳过 (record as skipped)”. Skipped events are logged, not silently dropped. Event history is exportable.

### 7. Savings ledger, summaries and export — core of the app

- **Ledger:** every confirmed item/event is one ledger entry: date (game date + real date), stage, category, item name, Public/Private, Mandatory/Optional, amount SGD, running total, note/source.
- **Dashboard (home):** total saved so far (big number), this month saved, this stage saved, breakdown by category (donut/bar chart), breakdown by stage, and a monthly bar chart. No savings target by default — the goal field is empty and optional; if the player sets one, show a progress bar, otherwise hide it.
- **Monthly view:** for the current game month, list what was saved / “spent” that month, with a per-category subtotal.
- **Export CSV:** one button “Export CSV 导出 CSV”. Columns, in this exact order: `date,stage,category,item,hospital_type,mandatory,amount_sgd,cumulative_sgd,source,notes`. UTF-8 with BOM so Excel opens Chinese correctly. Filename: `baby-savings-YYYY-MM-DD.csv`.
- **Export / Import JSON backup:** full backup including player price edits and custom items.
- **Player-editable prices:** every item has Edit. The player can change price, quantity/tins per month, and frequency; can add a custom item (name, price, stage, category); can delete a custom item; can “Reset to default price 恢复默认价”. Edits are saved in `localStorage` and survive a price-file update — show a badge “Edited by you 你改过价” and never silently overwrite a player edit when `prices.json` updates.

### 8. Design

- Clean, warm, friendly. Soft colours, rounded cards, no dark / clinical look. Use system fonts so Chinese renders well on iOS/Android/desktop.
- Home has 4 clear tabs: **Home 首页 / Play 玩 / Ledger 账本 / Sources 出处**.
- Sources page lists every price source used, with link, `last_checked`, and the disclaimer: “Prices are for a savings-simulation game only, as published on 20 Nov 2026. They are not quotes. Verify with the hospital / retailer before a real decision.” in both languages.
- Help page explains the game in 5 steps, the two modes, the reminder limit, and that CDA / MediSave Grant are ring-fenced, not cash.
- All buttons have both languages. Numbers are always SGD. No placeholder text like “Lorem ipsum” or “Coming soon” — every screen must work.

### 9. Repo structure to generate (for the GitHub / Vercel project)

Generate the app as `index.html`, and ALSO output the following files as separate code blocks in your reply so I can save them:
- `prices.json` — use the supplied data, do not re-invent prices.
- `scripts/check_prices.py` — a Python script that reads `prices.json`, does a HEAD/GET on every `source_url`, reports dead links / redirects / HTTP errors, checks `last_checked` is not older than 180 days, and writes `docs/price-check-report.md`. It must NEVER auto-change a price — it only reports, a human approves the update.
- `.github/workflows/check-prices.yml` — GitHub Actions, runs `scripts/check_prices.py` monthly (cron `0 0 1 * *`) and on demand.
- `docs/README.md`, `docs/PRICE_SOURCES.md`, `docs/WIKI.md` — documentation: how to run locally, how to deploy to Vercel (static, no build), how prices are researched, the full source table (item / price / source / reason / verified status), how to update a price, and the version history.

### 10. Quality checks before you finish

- Test mentally: create a new SC player, 1st child, public route, vaginal, KKH B2 — the dashboard total, the delivery screen, and the CSV export must all agree. Do the same for a private Thomson 1-bedded C-section player and confirm MediSave is capped at S$5,940 for a 3-day C-section, not the full bill.
- No invented prices. If a price is missing in `prices.json`, show “—” and “Unverified”, not a guessed number.
- No broken links, no empty screens, no console errors on load. The app must work from `file://` as well as from Vercel (except the GitHub fetch, which falls back to embedded prices).
- End your reply with a short checklist in English and Chinese: what was built, how to deploy to Vercel in 3 steps, and what still needs a human to check.

---
**End of prompt. Build it now.**

## v1.1 Addendum — 20 Nov 2026 (all added, still v1)

Use `prices.json` v1.1.0. Add these, all optional toggles in Settings unless stated:

**Multiples:** Roll at conception: twins 1.5%, triplets 0.03% (ICA 2015–2024: 5,161 twin pairs ~1.4%, 86 triplet sets ~0.025%. IVF toggle: single embryo <1%, two embryos 20%). Reveal at ~12-week scan. Twins ×2 recurring costs, 2 cots / 2 car seats / double stroller, confinement +S$1,200–1,800.

**Child status (Tamagotchi-like):** Three bars 0–100, start Health 80 / Happiness 80 / Development 50. Health falls if vaccines skipped or illness untreated; illness probability rises when Health <50. Happiness falls if birthday gift / toys / party skipped (-10 for skipped birthday gift); rises with play, party, gifts. Development rises with books, enrichment, play. Show a face + the three bars on Home. All starting values editable.

**Gifts & celebrations (all optional, parent chooses):** Birthday present S$30–70/year, Christmas gift S$30–70, CNY angbao TO own child S$88 (range S$68–188, avoid 4), Full-month home modest S$1,344 (boxes 30×S$11.90 + catering 30×S$22.90 + cake S$100 + decor S$200), Full-month gift box S$5.90–30.90/box, 100-day same as full-month (choose one or both, do not double-count by default), Zhuazhou set S$5–20 second-hand — Zhuazhou is 1st birthday, NOT 100-day. Birthday party venue S$490–860 for ~10 children, cake S$65–100 separate (most venue packages exclude cake).

**Medicine cabinet:** Monthly allowance S$10–30 WITHOUT daily probiotic, S$60–75 WITH daily probiotic. Items: Panadol Children S$9.75, KoolFever S$7.08, Sterimar S$19.55, DDROPS Vitamin D S$37.30/90 drops (~S$12.43/mo), BioGaia S$50.15. Linkage (game rule, label as such): if the player does NOT stock the cabinet, a fever/illness event costs +30% more (late-night pharmacy / forced GP visit instead of home care). Thermometer S$12 one-off, not monthly.

**Jaundice:** 60% of newborns get some jaundice (flavour, no cost). 10% need phototherapy (secondary estimate, flag it): hospital public S$200–400/day ×1–2 days, private S$500–1,000+/day, or home rental S$298–399/3D2N (Doctor Anywhere S$298, Baby Specialist S$299–399).

**Preterm / NICU:** Preterm roll 8.5% at delivery (MOH 2024). Do NOT price NICU per day. Use MOH DRG total bills by birth-weight tier, Ward C median: late preterm no problem S$721, 2000–2499g other problem S$1,331, major problem S$4,885, 1500–1999g S$5,534, 1250–1499g S$17,030. Show MediShield Life + S$5,000 MediSave Grant separately.

**Pregnancy complications:** GDM 20% roll after OGTT 24–28w, extra ~S$500 (secondary, editable), Thomson HOPE S$380. Preeclampsia 4% roll after 20w (twins 7.5%, triplets 19.4%): mild = extra monitoring, severe = early delivery + C-section median as proxy. No invented insulin / bed-rest price — show as extra visits only, flagged.

**End simulation — Option A only:** No random miscarriage/abortion roll. A player-initiated “End this simulation” button in Pregnancy, quiet settlement screen, no score penalty, restart option, respectful language only. Context rate (KKH: early miscarriage up to 1 in 5) is for documentation only.

**Feeding choice:** Breastfeeding vs Formula toggle. Fully breastfeeding saves ~S$150–190/mo in Year 1 (derived: S$220 formula saved minus pump amortised S$32–67/mo minus pads/bags S$30–50/mo). Show pump + consumables — “breastfeeding is free” is false. Nursing bras 3×S$45=S$135 one-off.

**Second-hand:** Per gear item, player picks New / Used / Free. Generic gear 40–60% off RRP, premium/bundle 50–90% off. Cleaning refresh S$48–85. Warning on used car seats: check expiry / crash history, do NOT present as equivalent to new.

**Helper / maid:** Monthly choice. Filipino S$650–900/mo, Indonesian S$550–800, Myanmar S$450–800, levy standard S$300/mo, concessionary S$60/mo if SC child <16 (MOM rule is <16, not <7), agency total S$1,000–3,000, food/utilities S$180–300/mo, all-in ~S$1,205–1,430/mo. If chosen, it replaces/reduces childcare cost — do not charge both in full without a toggle.

**Economy:** Inflation default 2.0%/year (MAS forecast 2026 headline ~2.0%, 2025 was 0.9%), applied at each simulated birthday, editable. Savings interest default 2.5%/year (CPF OA floor, SSB 2.25% avg), applied monthly as 2.5%/12 on the pot, labelled as a simulation assumption, NOT a bank rate (real bank base is 0.05%, top tier up to 4.10% only with conditions).
