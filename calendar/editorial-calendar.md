# Editorial Calendar — Q8tly Guides (Module 8)

Single source for what's planned, in progress, and live, plus the **weekly
rotation** the homepage editorial block pulls from. Publish under `/{lang}/guide/`.

Status legend: `idea` → `drafting` → `EN staged` → `AR staged` → `live`
(AR twins now buildable on staging as fenced drafts — 2026-06-29; AR goes *public*
only after the full gate clears — see Published note below).

---

## This Week — Homepage Rotation

> ⚠ **Observed on staging (2026-06-24):** the Module 6 homepage editorial block
> **auto-pulls live guides newest-first and features the newest as "editorial of
> the week."** It does NOT read this markdown list — curation here is effectively
> by *publish recency*. To pin a non-newest guide as the feature you'd need a
> Builder/Module 6 "featured" flag → **route to the Advisor** (don't touch the widget).

**Live order on the homepage now (newest-first, verified):**

| Position | Guide | Slug | Note |
|----------|-------|------|------|
| **Featured** (editorial of the week) | MizuMesa (Nikkei) — Sharq / KIPCO | `mizumesa-sharq` | newest → auto-featured ✓ — and the strongest candidate |
| 2 | South Avenue Salon & Spa — Sabah Al-Salem | `south-avenue-salon-sabah-al-salem` | live EN (AR parked) |
| 3 | Naranj — Salmiya | `naranj-salmiya` | live EN (AR parked) |
| 4 | Anosha Beauty Salon — Sabah Al-Salem | `anosha-beauty-salon-sabah-al-salem` | flagship; live EN (AR parked) |

---

## Pipeline

| Title | Type (best-of / area guide) | District / Category | EN | AR | Target | Notes |
|-------|-----------------------------|---------------------|----|----|--------|-------|
| _empty — all spotlights shipped (see Published)_ | — | — | — | — | — | Anosha (2189), Naranj (2251), South Avenue (2339), MizuMesa (2362) are live EN. Pipeline needs seeding: next idea + a best-of/area guide. |

---

## Published

All live on STAGING (English) via the Guide Ingestion Kit. Production frozen.
**AR (2026-06-29):** mechanism unblocked — Builder set `guide_article`/`topic`/
`guide_tag` WPML-Translatable, so AR twins can now be built on staging as
fenced/noindex human translations (D-145). Twin-building is paused only until
Builder's `[q8tly_place]`/`[q8tly_map]` AR-URL check returns. AR goes *public*
only after the full gate clears (S2-19/WPML-on-prod is necessary-but-not-sufficient;
also AR-perfect D-160 + owner track + D-157 cutover + 7-G flip).
**First AR twin LIVE (fenced) 2026-06-29:** Anosha → `guide_article` **2600** at
`/ar/guide/anosha-beauty-salon-sabah-al-salem/`, publish + noindex, **D-145 ✓ (PASS)**
— content-complete, parked fenced, rides the site-wide flip (not unfenced per-guide).
**Naranj AR twin LIVE (fenced) 2026-06-29:** `guide_article` **2612** at
`/ar/guide/naranj-salmiya/`, publish + noindex, Bader-authored Kuwaiti Arabic
injected + verified (place-card → `/ar/places/السالمية/نارنج/`). Parked fenced.
**MizuMesa AR twin LIVE (fenced) 2026-06-29:** `guide_article` **2618** at
`/ar/guide/mizumesa-sharq/`, publish + noindex, Bader-authored Kuwaiti Arabic
injected + verified (place-card → `/ar/places/شرق/2405/`). Parked fenced.
**MizuMesa NEUTRAL re-author 2026-06-30:** EN **2362** + AR **2618** bodies replaced with
the new short/neutral model (D-168) — About + Key facts + place card only; no data-table,
no FAQ. Faithful inject of Bader's locked MD (`drafts/mizumesa-sharq_{EN,AR}_2026-06-30.md`).
EN published (indexable), AR stays noindex-fenced. Open flags: inline photos 2359/2360/2361
orphaned (new MD has no inline images → hero 2358 only); SEO meta still old (EN rank_math
title+desc, AR desc); deck = auto-excerpt of the about; AR listing-card slug numeric (2405).
**Keif AR twin LIVE (fenced) 2026-06-29:** `guide_article` **2630** at
`/ar/guide/keif-restaurant-al-kout-mall/`, publish + noindex, Bader-authored Kuwaiti
Arabic injected + verified (place-card → `/ar/places/الفحيحيل/مطعم-كيف/`). Parked fenced.
**Vibes AR twin LIVE (fenced) 2026-06-29:** `guide_article` **2634** at
`/ar/guide/vibes-coffee-roastery-al-kout-mall/`, publish + noindex, Kuwaiti AR injected +
verified (place-card → `/ar/places/الفحيحيل/vibes-coffee-roastery/`). Parked fenced.
**South Avenue AR twin LIVE (fenced) 2026-06-29:** `guide_article` **2619** at
`/ar/guide/south-avenue-salon-sabah-al-salem/`, publish + noindex, Kuwaiti AR injected +
verified (place-card → `/ar/places/صباح-السالم/صالون-ساوث-أفينيو/`). Parked fenced.

**✅ AR CORPUS COMPLETE (2026-06-29): all 6 guides have fenced AR twins** — anosha 2600,
naranj 2612, mizumesa 2618, keif 2630, vibes 2634, south-avenue 2619. All publish+noindex;
they ride the site-wide AR-public flip together (no per-guide unfence). EN sides untouched.

| Title | URL (`/{lang}/guide/…`) | guide_article | Live date | Internal links placed |
|-------|--------------------------|---------------|-----------|------------------------|
| Anosha Beauty Salon — Sabah Al-Salem | `/guide/anosha-beauty-salon-sabah-al-salem/` | 2189 | 2026-06-20 | ✓ `/places/sabah-al-salem/` + `/places/category/salons/` (2026-06-24) |
| Naranj — Salmiya | `/guide/naranj-salmiya/` | 2251 | 2026-06-22 | ✓ `/places/salmiya/` + `/places/category/restaurants/` (2026-06-24) |
| South Avenue Salon & Spa — Sabah Al-Salem | `/guide/south-avenue-salon-sabah-al-salem/` | 2339 | 2026-06-23 | ✓ `/places/sabah-al-salem/` + `/places/category/salons/` + `/places/category/spas-massage/` (2026-06-24) |
| MizuMesa (Nikkei) — Sharq / KIPCO Tower | `/guide/mizumesa-sharq/` | 2362 | 2026-06-24 | ✓ `/places/sharq/` + `/places/category/restaurants/` (at publish) · ext: mizumesa.com reservations |
