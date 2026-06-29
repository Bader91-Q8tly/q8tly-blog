# Handoff — MizuMesa (Sharq / KIPCO) editorial spotlight (2026-06-24)

**Session:** Module 8 (Editorial / Guide). Author: Claude Blog.

## ✅ DONE — live as a real `guide_article` (via the Guide Ingestion Kit)
Fourth guide shipped through `guide-kit/` (after Anosha, Naranj, South Avenue).
Built the drop from Bader's raw drop (`~/Desktop/Mizu/`: intake `.md` + 15 photos),
dry-ran, `--execute`. Clean end to end. **Listing already existed** this time
(no blocker).

- **guide_article ID 2362** — published, English.
  - Live: `https://staging-e1ff-baderlol44-pwgjm.wpcomstaging.com/guide/mizumesa-sharq/`
  - Edit: `…/wp-admin/post.php?post=2362&action=edit`
  - Verify: renders 200, house chrome (kicker/deck/byline/hero), no double title,
    hero present. ✓ Both shortcodes **rendered** (zero raw `[q8tly_*]`), **zero mojibake**.
- **Drop folder:** `guide-kit/guides/mizumesa-sharq/` (`article.md` + `images/`).
- **Body = plain prose + shortcodes:** `[q8tly_place id="2354"]` + `[q8tly_map ids="2354"]`
  (map pin rendered — coords on the listing). **717 words.**
- **Meta:** `deck`, `article_type=guide`, `word_count=717`, `hero_alt`, `hero_caption`,
  `rank_math_title`/`_description`. **Topic:** Food & Drink (term **1715**, `primary_topic`).
- **Backup:** `staging-20260624-182816-guide-mizumesa-sharq.sql.gz` (1,706,283 B, logged).
- **Run handoff:** `guide-kit/runs/mizumesa-sharq.md`.

## Source of truth
- **Listing:** **gd_place 2354** (`mizumesa`, `/places/sharq/mizumesa/`), category
  Restaurants (1487), coords 29.3758468 / 47.9864084 (Khalid Ibn Al-Waleed St, Sharq).
  Created by the data pass before this session.
- **Field drop:** `~/Desktop/Mizu/` — intake `mizumesa-restaurant.md` + 15 photos.
- **Concept (from the menu's own story card, photo 15.47.01):** Nikkei = Japanese
  technique + Peruvian ingredients; **mizu** = "water" (Japanese), **mesa** = "table"
  (Spanish/Peru). Upscale, ~13 KD/head, lunch + dinner 1–11 PM, +965 2207 0777,
  KNET/Visa-MC/Cash, family section, groups 6+, no valet (park in KIPCO Tower).
  **Standout = the beef.**

## Internal + external links (placed at publish)
- **Money-page links baked into the body:** `restaurants` → /places/category/restaurants/ ·
  `Sharq` → /places/sharq/. (Root-relative, cutover-safe.) Verified live, both 200.
- **Reservations (Bader's request):** 4 links to `https://mizumesa.com/index.html`
  (their site; resolves 200, SevenRooms booking behind it). Framed as "recommended,
  walk-ins welcome" in Good-to-know, the facts table, and FAQ. Verified live.

## 📸 Photos — DONE (hero + 3 inlines; all 15 sources portrait)
- **hero = 2358** (gold MizuMesa logo on brick wall) — Featured + `hero_photo_id`.
- inline-1 = **2359** (green velvet banquette + greenery, warm light) — "The room".
- inline-2 = **2360** (dragon-style avocado roll) — "The food: Nikkei".
- inline-3 = **2361** (beef on crisp rice, logo-marked board) — "Don't miss the beef".
- **Excluded `17.04.08 (2)`** (outdoor benches): intake says **no outdoor seating**
  (likely the shared tower terrace) — left out so the guide doesn't imply outdoor dining.
- Plenty of unused strong food/interior shots remain in `~/Desktop/Mizu/` if we want
  more inlines later. ⚠ Hero is a portrait crop (no landscape source) — fine, swap later if wanted.

## Facts discipline
- **No "daily" claim** on hours — intake gave hours without days; wrote "1:00 PM – 11:00 PM
  (lunch & dinner)" without asserting every day. Confirm days with Bader to add "daily".
- **No Arabic / accents / en-dash in meta** (CHARSET.md: json.dumps→PHP double-quote would
  store literal `\u…`). Body uses safe UTF-8 (em-dashes clean, verified 0 mojibake).
- Did not claim outdoor/delivery/WiFi/shisha/valet (intake = No on all).

## Open / for Bader
- **Hours days** — confirm whether 1–11 PM is daily.
- **Homepage rotation** — still the approved 3 (Anosha/Naranj/South Avenue); MizuMesa is
  a strong candidate if you want to swap one in.
- **AR** parked; production frozen. Optional: landscape hero; more food inlines.
