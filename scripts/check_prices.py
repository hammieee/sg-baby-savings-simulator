#!/usr/bin/env python3
"""
check_prices.py — SG Baby Savings Simulator
Check every source_url in prices.json. Report only. NEVER auto-change a price.

Usage:
  python3 scripts/check_prices.py
  python3 scripts/check_prices.py --prices prices.json --out docs/price-check-report.md

What it does:
  1. Loads prices.json, collects every source_url (items + delivery + subsidies + random_events).
  2. HEAD/GET each URL with a browser User-Agent, timeout 15s.
  3. Reports: OK (200), redirect (301/302 -> final URL), dead (404/403/timeout/DNS), stale last_checked > 180 days.
  4. Writes a Markdown report to docs/price-check-report.md and prints a summary.
  5. Exit code 0 if all OK, 1 if any dead/stale link found (so GitHub Actions fails visibly).

What it does NOT do:
  - It does NOT scrape a new price from a page.
  - It does NOT edit prices.json.
  - A human must approve any price change, update prices.json + PRICE_SOURCES.md,
    bump meta.version (e.g. 1.0.0 -> 1.1.0), and update last_checked.
"""
import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

STALE_DAYS = 180
TIMEOUT = 15
UA = {"User-Agent": "Mozilla/5.0 (SG-Baby-Savings-Price-Checker/1.0)"}


def collect_urls(data):
    """Return list of (label, url). Deduplicate by url, keep first label."""
    seen = {}
    def add(label, url):
        if url and isinstance(url, str) and url.startswith("http"):
            seen.setdefault(url, label)
    for item in data.get("items", []):
        add(f"item:{item.get('id')}", item.get("source_url"))
    for key, table in data.get("delivery_moh_median", {}).items():
        if isinstance(table, list):
            for row in table:
                add(f"delivery:{key}", data.get("delivery_moh_median", {}).get("source"))
        elif isinstance(table, str):
            pass
    # subsidies
    for group in data.get("subsidies", {}).values():
        if isinstance(group, dict):
            add("subsidy", group.get("source"))
    for ev in data.get("random_events", []):
        add(f"event:{ev.get('id')}", ev.get("source"))
    # also the top-level delivery source
    add("delivery", data.get("delivery_moh_median", {}).get("source"))
    return [(label, url) for url, label in seen.items()]


def check_url(url):
    try:
        req = Request(url, headers=UA, method="HEAD")
        with urlopen(req, timeout=TIMEOUT) as r:
            return r.status, r.geturl(), ""
    except HTTPError as e:
        # Some sites block HEAD — retry with GET, no body read
        if e.code in (403, 405):
            try:
                req = Request(url, headers=UA, method="GET")
                with urlopen(req, timeout=TIMEOUT) as r:
                    return r.status, r.geturl(), "GET fallback after HEAD blocked"
            except Exception as e2:
                return getattr(e2, "code", 0), url, str(e2)
        return e.code, url, str(e)
    except URLError as e:
        return 0, url, str(e.reason)
    except Exception as e:
        return 0, url, str(e)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prices", default="prices.json")
    ap.add_argument("--out", default="docs/price-check-report.md")
    args = ap.parse_args()

    prices_path = Path(args.prices)
    data = json.loads(prices_path.read_text(encoding="utf-8"))
    meta = data.get("meta", {})
    last = meta.get("last_checked", "")
    try:
        last_d = datetime.strptime(last, "%Y-%m-%d").date()
        age = (date.today() - last_d).days
    except Exception:
        age = 9999
    stale = age > STALE_DAYS

    urls = collect_urls(data)
    rows = []
    dead = 0
    for label, url in sorted(urls, key=lambda x: x[1]):
        status, final, note = check_url(url)
        ok = status == 200
        if not ok:
            dead += 1
        rows.append((label, url, status, final, note, ok))

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    lines.append("# Price Check Report — SG Baby Savings Simulator\n")
    lines.append(f"- Checked: {date.today().isoformat()}\n")
    lines.append(f"- prices.json version: {meta.get('version','?')} · last_checked: {last} ({age} days ago, stale={stale})\n")
    lines.append(f"- URLs checked: {len(rows)} · OK: {len(rows)-dead} · Problem: {dead}\n")
    lines.append("\n## Results\n")
    lines.append("| Status | Label | URL | HTTP | Note |")
    lines.append("|---|---|---|---|---|")
    for label, url, status, final, note, ok in rows:
        mark = "OK" if ok else "CHECK"
        lines.append(f"| {mark} | {label} | {url} | {status} | {note} |")
    lines.append("\n## Action needed\n")
    if dead:
        lines.append("- [ ] Review every `CHECK` row above. Open the URL manually. If the page moved, update `source_url` in prices.json. If the price changed, update the price + PRICE_SOURCES.md with the reason, bump `meta.version`, and set `last_checked` to today.\n")
    else:
        lines.append("- No dead links found. Still check: are any prices >180 days old? If yes, re-verify the top 10 highest-impact prices (delivery, childcare, formula) manually.\n")
    if stale:
        lines.append(f"- [ ] prices.json is {age} days old (> {STALE_DAYS} days). Re-verify before the next release.\n")
    lines.append("\n> This script never edits prices.json. A human approves every price change.\n")
    out.write_text("\n".join(lines), encoding="utf-8")

    print(f"Checked {len(rows)} URLs: {len(rows)-dead} OK, {dead} problem. Report: {out}")
    if stale:
        print(f"WARNING: last_checked {last} is {age} days old.")
    return 1 if (dead or stale) else 0


if __name__ == "__main__":
    sys.exit(main())
