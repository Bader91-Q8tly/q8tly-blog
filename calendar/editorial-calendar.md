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
| **Featured** (editorial of the week) | B+F — 360 Mall (Solar Garden) / Zahra | `bandf-360-mall` | newest (2026-07-05) → auto-featured ✓; born-neutral (D-168) |
| 2 | Odachi — Kuwait City / Khaleejia Tower | `odachi-kuwait-city` | live EN · AR fenced |
| 3 | MizuMesa (Nikkei) — Sharq / KIPCO | `mizumesa-sharq` | live EN · AR fenced |
| 4 | South Avenue Salon & Spa — Sabah Al-Salem | `south-avenue-salon-sabah-al-salem` | live EN · AR fenced |
| 5 | Naranj — Salmiya | `naranj-salmiya` | live EN · AR fenced — rotates off if the block caps at 4 |

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
**Refined 2026-06-30 (v2, per Bader):** photos restored with short neutral captions
(hero 2358 "Outside MizuMesa" + inline 2359/2360/2361 = "Inside MizuMesa" / "One of the
rolls" / "A beef dish"; AR mirrors); key facts now render as the **TABLE** (the old
"before you go" look — content-only, no facts-card CSS exists, no Builder), 5 clean rows.
Final = About → 3 captioned photos → key-facts table → listing card. AR fenced. EN via
new `guide-kit/reinject_en.py` (EN counterpart to populate_ar_twin.py; no fence).
Photo-orphan flag RESOLVED. Remaining flags: SEO meta still old; AR listing slug numeric.
**Naranj NEUTRAL re-author 2026-07-01:** EN **2251** + AR **2612** bodies replaced with the
same short/neutral model (D-168) — About + 3 captioned photos (hero 2247 "Outside Naranj" +
inline 2248/2249/2250 = "Inside Naranj" / "Mezze and meat arayes" / "Dessert at the end of
the meal"; AR mirrors) + key-facts **table** (6 rows) + place card; no `[[map]]`. Faithful
inject of Bader's approved MD (`drafts/naranj-salmiya_{EN,AR}_2026-07-01.md`). EN published
(indexable), AR stays noindex-fenced (content-only update, fence untouched). `rank_math_description`
set to match (EN only, via SSH — the AR precedent leaves AR's blank on a fenced twin).
**Anosha NEUTRAL re-author 2026-07-01:** EN **2189** + AR **2600** bodies replaced with the
same model — About + 3 captioned photos (hero 2190 "Outside Anosha Beauty Salon" + inline
2192/2194/2193 = "Hair-wash lounge" / "Welcome coffee on arrival" / "The nail bar"; AR
mirrors) + key-facts table (6 rows) + place card; old 12-row service/price menu, FAQ, and
"Know before you go" table all dropped (price menu is listing-pipeline scope, not guide
prose). Faithful inject of Bader's approved MD (`drafts/anosha-beauty-salon-sabah-al-salem_{EN,AR}_2026-07-01.md`).
Price tier ($$) confirmed by Bader (intake had left it an open call). EN published, AR stays
noindex-fenced.
**Tool: `reinject_en.py` FORMALIZED 2026-07-01** — the EN counterpart to `populate_ar_twin.py`
is no longer a one-off: auto-backup before every write (self-logged to `BACKUP_LOG.md`), a
hard target guard (refuses unless the post is a `guide_article` with WPML lang `en`/untranslated
— never touches the AR twin or `icl_translations`), a built-in idempotency diff against the
live body, and conditional SEO-meta sync. No-op verified against MizuMesa (post 2362) —
generated body byte-identical to live, full backup→update→verify pipeline clean, AR twin
(2618) confirmed untouched. Documented in `guide-kit/README.md` §6.
**NEUTRAL ROLLOUT STATUS (2026-07-02): 3 of 6 done** — mizumesa, naranj, anosha. **3 remain**
on the old persuasive body: south-avenue-salon-sabah-al-salem (2339/2619), keif-restaurant-al-kout-mall
(2132/2630), vibes-coffee-roastery-al-kout-mall (2131/2634) — same flow, gated on their
approved MDs landing from the Content Writer. (Corrects the "5 remaining" figure carried in
the 2026-06-30 checkpoint and in shared STATE.md — 2 of those 5 are now done.)
**Keif AR twin LIVE (fenced) 2026-06-29:** `guide_article` **2630** at
`/ar/guide/keif-restaurant-al-kout-mall/`, publish + noindex, Bader-authored Kuwaiti
Arabic injected + verified (place-card → `/ar/places/الفحيحيل/مطعم-كيف/`). Parked fenced.
**Vibes AR twin LIVE (fenced) 2026-06-29:** `guide_article` **2634** at
`/ar/guide/vibes-coffee-roastery-al-kout-mall/`, publish + noindex, Kuwaiti AR injected +
verified (place-card → `/ar/places/الفحيحيل/vibes-coffee-roastery/`). Parked fenced.
**South Avenue AR twin LIVE (fenced) 2026-06-29:** `guide_article` **2619** at
`/ar/guide/south-avenue-salon-sabah-al-salem/`, publish + noindex, Kuwaiti AR injected +
verified (place-card → `/ar/places/صباح-السالم/صالون-ساوث-أفينيو/`). Parked fenced.

**✅ AR CORPUS: 7 of 8 fenced twins (2026-07-05)** — anosha 2600, naranj 2612,
mizumesa 2618, keif 2630, vibes 2634, south-avenue 2619, odachi 2808. All publish+noindex;
ride the site-wide AR-public flip together. **B+F (2918) is the 8th EN guide — its AR twin
is pending Bader's WPML "+"** (AR MD staged `drafts/bandf-360-mall_AR_2026-07-05.md`; then
`populate_ar_twin.py --en-id 2918 --media hero=2914,inline-1=2915,inline-2=2916,inline-3=2917`).

**B+F PUBLISHED (born-neutral) 2026-07-05:** EN `guide_article` **2918** at
`/guide/bandf-360-mall/` — Bader-locked About verbatim (matches live listing 2664) + 3
captioned photos (musakhan rolls / beef plate / Solar Garden terrace) + 8-row key-facts
table + place card. **Two pipeline-live corrections applied over the source doc:** price
band **$$ → $$$** (KD figure kept), and slug/district settled = **Zahra** (place card →
`/places/zahra/bf-360-mall/`, listing 2664). Mall services carried as the "Via 360 Mall
(not venue amenities)" line only; no Burger/Steakhouse/"Restaurant inside Mall" labels in
guide prose (NEEDS-BADER). Photos pre-cropped landscape (portrait originals would slice —
the Odachi lesson); hero 2914 + inline 2915/2916/2917. Kit run backup `20260704-215916`.
AR twin pending the "+".

**Odachi PUBLISHED (born-neutral) 2026-07-04:** EN `guide_article` **2800** at
`/guide/odachi-kuwait-city/` — **first guide shipped straight onto the D-168 neutral model
at publish time** (no spotlight-era body to re-author): Bader-locked About verbatim + 3
captioned photos + 6-row key-facts table + place card; no `[[map]]`. Kit run clean (backup
`20260704-183756`). Place card resolves `/places/kuwait-city/odachi/` (listing 2432).
**Photos re-cropped 2026-07-04 (post-publish, per Bader — "weird pictures"):** the
guide-single template center-crops inline photos to a fixed landscape box (~7:5 desktop /
~1:1 mobile; hero 16:9), so the original **portrait** phone shots lost their tops/bottoms
(shrimp & noodle bowls cut). Fixed in-lane by pre-cropping each to the template's box,
centered on the subject: hero swapped to the **bright storefront-sign** shot; shrimp crop
drops the second salad bowl (caption → "Fried shrimp"). New WebP attachments **hero 2811 +
inline 2812/2813/2814** (old 2796–2799 trashed); EN 2800 re-injected + AR 2808 re-populated
(backups `20260704-200746` / `20260704-200917`), verified clean on mobile + desktop.
**Kit lesson:** compose guide photos **landscape** before publish (hero 16:9, inline 7:5) —
the template hard-crops. **Sushi tag verified** from the menu PDF (extensive nigiri/sashimi/
maki section) — but tags are `gd_place` listing tags (Pipeline lane), not guide tags.
**Odachi AR twin LIVE (fenced) 2026-07-04:** `guide_article` **2808** (trid 4743) at
`/ar/guide/odachi-kuwait-city/`, publish + noindex. Bader made the WPML "+" (clean editable
WP-editor shell, 2808); Blog injected the Bader-authored Kuwaiti AR
(`drafts/odachi-kuwait-city_AR_2026-07-04.md`) via `populate_ar_twin.py` (backup
`20260704-190246`; images reused 2796/2797/2798/2799 — no re-upload). Verify PASS: Arabic
title no mojibake, place-card → `/ar/places/مدينة-الكويت/odachi/`, no bare `/places/`, no
`/ar/en/` double-prefix, noindex fence present. **Still open (D-145 review while fenced,
same as every twin):** one-word twin mismatch (AR "هادي" vs EN locked "cozy" — Bader rules);
staged AR captions/hero_alt are Blog-drafted, need Bader's D-145 read. Listing-lane flags
(coordinates, WhatsApp?, menu-link durability, Sushi tag) belong to Pipeline, not the guide.

| Title | URL (`/{lang}/guide/…`) | guide_article | Live date | Internal links placed |
|-------|--------------------------|---------------|-----------|------------------------|
| Anosha Beauty Salon — Sabah Al-Salem | `/guide/anosha-beauty-salon-sabah-al-salem/` | 2189 | 2026-06-20 | ✓ `/places/sabah-al-salem/` + `/places/category/salons/` (2026-06-24) |
| Naranj — Salmiya | `/guide/naranj-salmiya/` | 2251 | 2026-06-22 | ✓ `/places/salmiya/` + `/places/category/restaurants/` (2026-06-24) |
| South Avenue Salon & Spa — Sabah Al-Salem | `/guide/south-avenue-salon-sabah-al-salem/` | 2339 | 2026-06-23 | ✓ `/places/sabah-al-salem/` + `/places/category/salons/` + `/places/category/spas-massage/` (2026-06-24) |
| MizuMesa (Nikkei) — Sharq / KIPCO Tower | `/guide/mizumesa-sharq/` | 2362 | 2026-06-24 | ✓ `/places/sharq/` + `/places/category/restaurants/` (at publish) · ext: mizumesa.com reservations |
| Odachi — Kuwait City / Khaleejia Tower | `/guide/odachi-kuwait-city/` | 2800 | 2026-07-04 | — born-neutral body carries no internal links (parity with the other neutral bodies) |
| B+F — 360 Mall (Solar Garden) / Zahra | `/guide/bandf-360-mall/` | 2918 | 2026-07-05 | place-card → `/places/zahra/bf-360-mall/` (2664); price $$$; born-neutral, no internal links |
