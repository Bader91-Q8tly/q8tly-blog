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

| Title | URL (`/{lang}/guide/…`) | guide_article | Live date | Internal links placed |
|-------|--------------------------|---------------|-----------|------------------------|
| Anosha Beauty Salon — Sabah Al-Salem | `/guide/anosha-beauty-salon-sabah-al-salem/` | 2189 | 2026-06-20 | ✓ `/places/sabah-al-salem/` + `/places/category/salons/` (2026-06-24) |
| Naranj — Salmiya | `/guide/naranj-salmiya/` | 2251 | 2026-06-22 | ✓ `/places/salmiya/` + `/places/category/restaurants/` (2026-06-24) |
| South Avenue Salon & Spa — Sabah Al-Salem | `/guide/south-avenue-salon-sabah-al-salem/` | 2339 | 2026-06-23 | ✓ `/places/sabah-al-salem/` + `/places/category/salons/` + `/places/category/spas-massage/` (2026-06-24) |
| MizuMesa (Nikkei) — Sharq / KIPCO Tower | `/guide/mizumesa-sharq/` | 2362 | 2026-06-24 | ✓ `/places/sharq/` + `/places/category/restaurants/` (at publish) · ext: mizumesa.com reservations |
