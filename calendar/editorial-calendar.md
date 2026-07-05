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
| **Featured** (editorial of the week) | Elysee Beauty Lounge & Queue Café — Mahboula (Park Inn rooftop) | `elysee-queue-cafe-mahboula` | newest (2026-07-05) → auto-featured ✓; **first COMBINED guide** (two venues, one feature) |
| 2 | B+F — 360 Mall (Solar Garden) / Zahra | `bandf-360-mall` | live EN · AR fenced |
| 3 | Odachi — Kuwait City / Khaleejia Tower | `odachi-kuwait-city` | live EN · AR fenced |
| 4 | MizuMesa (Nikkei) — Sharq / KIPCO | `mizumesa-sharq` | live EN · AR fenced |
| 5 | South Avenue Salon & Spa — Sabah Al-Salem | `south-avenue-salon-sabah-al-salem` | live EN · AR fenced — rotates off if the block caps at 4 |

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
**PHOTO FIX 2026-07-05 (first D-180 application, owner-approved):** the 4 portrait photos
(mixed 0.75/0.56 ratios) were re-cropped to **landscape 7:5 (1.407) at 1536px** — one ratio,
all ≥1200px — resolving the portrait/rhythm + sign-clip issues. **inline-2 swapped** (the
900px "One of the rolls" had no ≥1200px source) → a **1536px Nikkei fried-dish**, caption
"One of the rolls" → **"A Nikkei plate"** (AR "أحد أطباق الرول" → "طبق نيكي"). New landscape
attachments hero **3039** + inline **3040/3042/3043** (source: `Desktop/All /Mizu`); EN 2362
re-injected + AR twin 2618 re-populated (backups `20260705-112345` / `20260705-112512`); old
2358–2361 trashed. Verified clean landscape on mobile.
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

**✅ AR CORPUS COMPLETE — 8 of 8 fenced twins (2026-07-05)** — anosha 2600, naranj 2612,
mizumesa 2618, keif 2630, vibes 2634, south-avenue 2619, odachi 2808, **B+F 2924**. All
publish+noindex; ride the site-wide AR-public flip together (no per-guide unfence). EN
sides untouched.

**Elysee Beauty Lounge & Queue Café — COMBINED guide PUBLISHED (born-neutral) 2026-07-05:**
EN `guide_article` **3115** at `/guide/elysee-queue-cafe-mahboula/` — **first combined guide**
(two venues in one feature, owner-directed) and **first use of the D-180 Canva-interim PASS
path**. Two women-only spots sharing the 24th-floor rooftop of the Park Inn by Radisson,
Mahboula: **Elysee Beauty Lounge** (Beauty, listing 3066) + **Queue Café** (Cafés, listing
3067), framed as a salon-visit-plus-coffee day out. **Both place cards render** — `[[place]]`
= Queue 3067 + Elysee 3066 via an unquoted raw `[q8tly_place id=3066]` shortcode (WP
`shortcode_unautop` strips the wrapping `<p>` → clean card; verified 2 cards, 0 literal leak).
Photos: the intake's **22 originals were 4284–5712px** (native landscape) → the qualification
gate PASSED cleanly, and 5 were fitted to **7:5 1520×1086** (one ratio, all ≥1520px) — hero
3110 + inline 3111–3114 (rooftop lounge / Elysee sign / salon sea-view / Queue sign / café
interior). Voice neutral (D-168): owner's "fancy/breathtaking" rendered as facts (rooftop /
24th floor / floor-to-ceiling windows / sea views); **no fabrication** — Elysee salon
services/hours/price are unknown, so the salon is described only by confirmed facts. Kit
backup `20260705-205507`. **AR twin PENDING** — combined AR staged
`drafts/elysee-queue-cafe-mahboula_AR_2026-07-06.md` (assembled from Bader's verbatim AR;
combined arrangement + captions need his D-145 pass; then WPML "+" → populate). Open content
gaps (listing lane, not photos): Queue phone + coordinates; Elysee salon services/hours/price.

**B+F AR twin LIVE (fenced) 2026-07-05:** `guide_article` **2924** (trid 4805) at
`/ar/guide/bandf-360-mall/`, publish + noindex. Bader made the WPML "+" (clean editable
WP-editor shell 2924); Blog injected the verbatim Kuwaiti AR (`drafts/bandf-360-mall_AR_2026-07-05.md`,
matches listing twin 2730's About, price $$$) via `populate_ar_twin.py` (backup
`20260704-223255`; images reused 2914/2915/2916/2917 — no re-upload). Verify PASS: Arabic
title (Latin brand "B+F"), place-card → `/ar/places/الزهراء/bf-360-mall/` (twin 2730), no
bare `/places/`, no `/ar/en/`, noindex fence present. **Open (D-145 while fenced):** AR
brand-name kept Latin "B+F" (confirm); Blog-drafted AR captions need Bader's read.

**B+F PUBLISHED (born-neutral) 2026-07-05:** EN `guide_article` **2918** at
`/guide/bandf-360-mall/` — Bader-locked About verbatim (matches live listing 2664) + 3
captioned photos (musakhan rolls / beef plate / Solar Garden terrace) + 8-row key-facts
table + place card. **Two pipeline-live corrections applied over the source doc:** price
band **$$ → $$$** (KD figure kept), and slug/district settled = **Zahra** (place card →
`/places/zahra/bf-360-mall/`, listing 2664). Mall services carried as the "Via 360 Mall
(not venue amenities)" line only; no Burger/Steakhouse/"Restaurant inside Mall" labels in
guide prose (NEEDS-BADER). Photos pre-cropped landscape (portrait originals would slice —
the Odachi lesson); hero 2914 + inline 2915/2916/2917. Kit run backup `20260704-215916`.
**Canva-interim fit test 2026-07-05 (D-180): FAILED on sourcing, not framing.** The full
ORIGINAL B+F folder is the same size as the optimized set — the storefront/sign original is
**1086 px wide** (6 of 7 are 1086–1089 px; only the salad is 1200 px). A landscape 7:5 crop
maxes at the source width (1086 px) → under the 1200 bar; Canva reframes but can't upscale.
**Verdict: photo-SOURCING problem → B+F grandfathered as-is; fix = higher-res re-shoot
(≥1520 px, landscape), not Canva.** No guide change made.

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
