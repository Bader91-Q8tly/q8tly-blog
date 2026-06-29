# Handoff — Naranj (Salmiya) editorial spotlight (2026-06-22)

**Session:** Module 8 (Editorial / Guide). Author: Claude Blog.

## ✅ DONE — live as a real `guide_article` (via the Guide Ingestion Kit)
Second guide shipped through `guide-kit/` (after Anosha). Built the drop folder
from Bader's raw drop, dry-ran, then `--execute`. Clean end to end.

- **guide_article ID 2251** — published, English.
  - Live: `https://staging-e1ff-baderlol44-pwgjm.wpcomstaging.com/guide/naranj-salmiya/`
  - Edit: `…/wp-admin/post.php?post=2251&action=edit`
  - Verify: renders 200, house chrome present, no double title, hero present. ✓
- **Drop folder:** `guide-kit/guides/naranj-salmiya/` (`article.md` + `images/`).
- **Body = plain prose + shortcodes:** `[q8tly_place id="2239"]` (listing card) +
  `[q8tly_map ids="2239"]` (map pin). 569 words. Both shortcodes confirmed
  **rendered** on the live front-end (zero raw `[q8tly_*]` literals), zero mojibake.
- **Meta set:** `deck`, `article_type=guide`, `word_count=569`, `hero_alt`,
  `hero_caption`, `rank_math_title`/`_description`. **Topic:** Food & Drink (term
  1715, `primary_topic`).
- **Run handoff:** `guide-kit/runs/naranj-salmiya.md`. **Backup:**
  `staging-20260621-235456-guide-naranj-salmiya.sql.gz` (logged in `BACKUP_LOG.md`).

## Source of truth
- **Listing intake:** `~/Desktop/narenj/Q8tly_Listing_Intake_Naranj_2026-06-22.md`
  (Bader field notes, pre-mapped to canonical vocab).
- **Listing already live on staging:** **gd_place 2239** (`/places/salmiya/naranj/`),
  with coordinates populated (lat 29.3480341, lng 48.0887774, Arabian Gulf St,
  Salmiya). Phone +965 2226 8666.
- Confirmed facts used: Syrian · Salmiya / Arabian Gulf St · daily 9:00 AM–12:00 AM
  (last order 11:30 PM) · price `$$$` · KNET / Visa-Mastercard / Cash · valet ·
  shisha · indoor+outdoor · IG @naranjkuwait · standout = meat arayes · free
  dessert to close · date-night audience.

## 📸 Photos — ALL DONE
- Bader dropped 10 photos in `~/Desktop/narenj/` (+ `optimized/` 2048×1536 set).
- Used 4 cleanly-oriented landscape shots (streamed over SSH → `wp media import`):
  - **hero = attachment 2247** (IMG_2153, branded arched entrance) — Featured + `hero_photo_id`.
  - inline-1 = **2248** (IMG_2159, interior lanterns/garden) — "The room".
  - inline-2 = **2249** (IMG_2158, mezze + meat arayes) — "The food".
  - inline-3 = **2250** (IMG_2160, complimentary dessert tray) — "Service, and a sweet ending".
- **Skipped IMG_2155 / 2161 / 2162** — shot sideways (would render rotated). 2151/2154 not in optimized set.

## Facts discipline (carried from the intake §Flags)
- **WhatsApp omitted.** Intake flagged the phone/WhatsApp split (51444999) as
  unconfirmed → guide lists only the confirmed landline (+965 2226 8666, matches
  the listing). Add WhatsApp later if Bader confirms.
- **Smoking section** = prose/FAQ only (venue has a smoking section; `No Smoking`
  does NOT apply). No invented "smoking area" field.
- **Free dessert + arayes** = body only (no dedicated field exists).
- **Topic = Food & Drink** (restaurant; Syrian is a cuisine tag, not the category).
- **Coordinates note:** intake §Flag #3 said the map pin was missing, but the
  listing pipeline has since populated lat/lng on 2239 → `[[map]]` included
  (pipeline state wins, per the intake's own routing note).

## Open / for Bader (listing-pipeline scope, not the guide)
- **AR business name** (نارنج?) + **AR description** — still parked (WPML
  copy-not-translate for the name). AR guide not built; same plain-body rule when it ships.
- **Phone vs WhatsApp split** — confirm 22268666 (landline) vs 51444999 (WhatsApp).
- Production (q8tly.com) frozen; AR parked until Bader says publish.
