# Handoff — South Avenue Salon & Spa (Sabah Al-Salem) editorial spotlight (2026-06-23)

**Session:** Module 8 (Editorial / Guide). Author: Claude Blog.

## ✅ DONE — live as a real `guide_article` (via the Guide Ingestion Kit)
Third guide shipped through `guide-kit/` (after Anosha + Naranj). Built the drop
folder from Bader's raw drop (`~/Desktop/anfal/`: intake `.md` + 9 photos), waited
on the listing, then dry-ran + `--execute`. Clean end to end.

- **guide_article ID 2339** — published, English.
  - Live: `https://staging-e1ff-baderlol44-pwgjm.wpcomstaging.com/guide/south-avenue-salon-sabah-al-salem/`
  - Edit: `…/wp-admin/post.php?post=2339&action=edit`
  - Verify: renders 200, house chrome present (kicker/deck/byline/hero), no double
    title, hero present. ✓ Both shortcodes confirmed **rendered** on the live
    front-end (zero raw `[q8tly_*]` literals), **zero mojibake**.
- **Drop folder:** `guide-kit/guides/south-avenue-salon-sabah-al-salem/` (`article.md` + `images/`).
- **Body = plain prose + shortcodes:** `[q8tly_place id="2334"]` (listing card) +
  `[q8tly_map ids="2334"]` (map pin — district + directions rendered). **798 words.**
- **Meta set:** `deck`, `article_type=guide`, `word_count=798`, `hero_alt`,
  `hero_caption`, `rank_math_title`/`_description`. **Topic:** Neighborhoods (term
  **1716**, `primary_topic`) — shows as the kicker.
- **Run handoff:** `guide-kit/runs/south-avenue-salon-sabah-al-salem.md`. **Backup:**
  `staging-20260623-203957-guide-south-avenue-salon-sabah-al-salem.sql.gz` (1,725,240 B,
  logged in `BACKUP_LOG.md`).

## Source of truth
- **Listing (created by the DATA PASS this session, not Module 8):** **gd_place 2334**
  (`south-avenue-salon`), published 2026-06-23 23:27. Coordinates present in
  `wp_geodir_gd_place_detail` (**lat 29.2548594, lng 48.0827625**, Sabah Al-Salem) →
  `[[map]]` pin lights up. The guide was blocked on this until it existed (role
  brief: listing-data writes are the data pass's job).
- **Field drop:** `~/Desktop/anfal/` — intake `South_Avenue_Salon.md` (visit pack) + 9 photos.
- **Facts used (signage gave more than the intake sheet):** women-only "salon & spa
  for ladies", **2nd floor**, two Sabah Al-Salem branches (**Block 1 / قطعة 1** and
  **Block 3 / قطعة 3**) **plus an at-home service**. Hours daily 9 AM–10 PM (home
  service from 10 AM; Eid differs). Phones: Block 1 `50268000`/`50381000`, Block 3
  `65907896`, home service `50040004`. KNET / Visa-Mastercard / Cash. Indoor seating,
  strong A/C, easy self-parking, free WiFi, delivery/home service, good for groups
  (6+). Natural-treatment menu (herbal hair masks — coconut/coffee/rice/butter/
  moringa/henna — + scalp oils, per-session or packages); brand walls ORLY, essie,
  LUSH, L'Occitane, Rituals.

## 📸 Photos — DONE (hero + 3 inlines)
All 9 source shots were **portrait** (1152×2048). Used 4:
- **hero = attachment 2335** (gold entrance plaque "SOUTH AVENUE — 2nd Floor") — Featured + `hero_photo_id`.
- inline-1 = **2336** (lounge: product wall, nail wall, plant) — "What stood out".
- inline-2 = **2337** (ORLY polish wall) — "The nail bar".
- inline-3 = **2338** (premium product shelves — LUSH / L'Occitane / Rituals) — "Natural treatments".
- **Not used:** hours standee, essie posters, lattice-divider lounge shot, and two
  Arabic price-list documents (sideways/glare/redundant) — left out of the drop but
  **mined for facts** (branches, phones, the natural-treatment menu).
- ⚠ **Hero is a portrait crop** (no landscape source existed). It renders fine in the
  `guide-single__hero` band but a landscape hero would frame better — easy swap later
  if Bader sends one.

## Facts discipline
- **Prayer room** flagged "not confirmed" in the intake → **omitted** (no invented field).
- **Pricing** kept to an indicative "mid-range / value" note — the menu photos are in
  Arabic with glare; did **not** transcribe exact figures to avoid publishing a wrong
  price. (If Bader wants a price table, transcribe the two menu photos.)
- Did not claim valet / outdoor seating / shisha (intake = No on all three).

## Internal-linking pass (2026-06-24) — all 3 live guides
Placed contextual **guide → money-page** links (district + category archives) in
each guide body. Surgical first-occurrence edits to live `post_content` via
`wp_update_post` (WordPress context, charset-safe), backed up first
(`staging-20260624-165707-internal-links-guides.sql.gz`, logged), cache flushed.
**Root-relative URLs** (cutover-safe). Source `article.md` files synced; calendar
"Internal links placed" flipped to ✓.

| Guide | Links placed |
|-------|--------------|
| Anosha 2189 | `salons`→/places/category/salons/ · `Sabah Al-Salem`→/places/sabah-al-salem/ |
| Naranj 2251 | `restaurants`→/places/category/restaurants/ · `Salmiya`→/places/salmiya/ |
| South Avenue 2339 | `salons`→/places/category/salons/ · `spa`→/places/category/spas-massage/ · `Sabah Al-Salem`→/places/sabah-al-salem/ |

Verified live: all 7 anchors render, all 5 targets resolve 200, zero mojibake.

> **Direction note / for Advisor if wanted:** these are guide → archive links
> (in-scope Module 8). The *reverse* — surfacing these guides ON the district /
> category archive pages — is a Module 3–4 archive surface, **out of scope here**.
> Route to the Advisor if we want the money pages to feature the editorial.

## Open / for Bader
- **AR guide** — parked (same plain-body rule when it ships). AR business name +
  description on the **listing** is data-pass / WPML scope, not this guide.
- **Optional polish:** landscape hero swap; exact price table from the menu photos.
- Production (q8tly.com) frozen; AR parked until Bader says publish.
