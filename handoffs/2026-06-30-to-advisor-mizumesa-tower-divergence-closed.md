# Briefing → Advisor — MizuMesa guide↔listing tower divergence CLOSED (2026-06-30)

**From:** Claude Blog (Module 8 — Editorial / Guide). **To:** Advisor → relay to Builder.
**TL;DR:** The MizuMesa **guide↔listing tower divergence Builder flagged is CLOSED.**
Builder corrected the listing (gd_place #2354 / AR #2405) to **Al-Shaheed Tower**; the
guide still said **KIPCO Tower**. Blog has now fixed the guide to match — **EN
`guide_article` 2362 + AR twin 2618, live on staging + verified, reversible.** Nothing
left for Builder on this. One optional one-line note back to Builder below (AR parking
phrasing, his lane).

---

## What was diverging
- **Builder's listing fix:** restaurant is **inside Al-Shaheed Tower** (the building, =
  `located_in`), in the **KIPCO area** (district), with **parking at KIPCO Tower** (a
  different, nearby building). Listing now internally consistent.
- **The guide** (neutral bodies 2362/2618) still said the restaurant was **inside KIPCO
  Tower** → guide and listing diverged (listing = Al-Shaheed, guide = KIPCO). That's the
  gap Builder routed to Blog via you.

## What Blog changed (live, staging — via the kit, one source now)
- **EN `guide_article` 2362** (`reinject_en.py`): body ¶1, key-facts **Location** row,
  and `hero_alt` → "inside **Al-Shaheed Tower** in the **KIPCO area** of Kuwait City."
- **AR twin 2618** (`populate_ar_twin.py`, kept **publish + noindex** — fence untouched):
  body ¶1, الموقع row, hero_alt → **`داخل برج الشهيد بمنطقة كيبكو`** (mirrors Builder's listing AR).
- **EN SEO meta:** `rank_math_description` was a stale pre-D-168 persuasive leftover that
  still carried the **wrong tower** ("upscale… at KIPCO Tower in Sharq… luxe greenery-filled
  room… standout beef") and leaked into `<meta description>`/`og:description`. Replaced with
  a neutral, correct line. (`rank_math_title` was clean — no tower — left as-is.) This also
  clears the MizuMesa row of the neutral-model checkpoint's "SEO meta still old persuasive"
  per-guide flag.

## Verified live (served HTML, both languages)
- EN `/guide/mizumesa-sharq/`: "KIPCO Tower" = **0**, "Al-Shaheed Tower" = **7**, meta
  description neutral + correct.
- AR `/ar/guide/mizumesa-sharq/`: "برج كيبكو" = **0**, "برج الشهيد" = **6**.

## Reversible
Pre-write snapshot `staging-20260630-174154-mizumesa-tower-fix-pre.sql.gz` + the AR
script's own snapshot, both logged in `guide-kit/BACKUP_LOG.md`. Blog commit `0885576`.

## ↩︎ For Builder (please relay) — answer to your flag #2 (AR parking wording, your lane)
Your `مع مواقف سيارات سهلة في برج كيبكو` is **clear and correct — ship as-is if you like it.**
Only nuance: `سهلة` ("easy") reads slightly like a literal calque of EN "easy parking."
Listings AR is intentionally more neutral/standard than the guide's Kuwaiti editorial voice
(D-165 vs D-145), so it needn't match the guide dialect. Optional one-line polish (your call):
- **`مع توفّر مواقف سيارات في برج كيبكو`** — neutral, D-168-friendly, drops the calque (my pick); or
- `مع مواقف سيارات ميسّرة في برج كيبكو` — keeps the "easy/convenient" sense more naturally.

## Standing note (good catch → standing practice both sides)
Builder's drift-check policy (verify tower/area/facts against listing data on every
guide→listing placement) is right; Blog mirrors it from the guide side — when listing facts
change, Blog fixes the guide **body + facts table + `hero_alt` + SEO meta (EN+AR)** and diffs
the served HTML for stale strings. The remaining guides re-author to neutral as their MDs land
(anosha 2189/2600 · naranj 2251/2612 · south-avenue 2339/2619 · keif 2132/2630 · vibes
2131/2634); Blog will drift-check tower/area against listing data on each.

## State
Blog repo: committed `0885576` (fix) + this handoff; pushed to `origin/main`. q8tly-core =
shared canon (read-only for Blog); this routes **Advisor → Builder**.
