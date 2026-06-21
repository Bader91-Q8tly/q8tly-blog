# Handoff — Anosha Beauty Salon editorial spotlight (2026-06-20)

**Session:** Module 8 (Editorial / Guide). Author: Claude Blog.

## What I did
- Wrote the **"editorial of the week" spotlight** for **Anosha Beauty Salon** (Sabah Al-Salem, Mubarak Al-Kabeer) as a place spotlight.
  - EN (review-ready): `drafts/anosha-beauty-salon-sabah-al-salem_EN_2026-06-20.md`
  - AR (STAGED, do-not-publish): `drafts/anosha-beauty-salon-sabah-al-salem_AR_2026-06-20.md`
- Logged it in `calendar/editorial-calendar.md` (this-week rotation slot 1 + pipeline row).

## Source of truth
- Built from the blogger-lane intake (first-party visit by Bader's sister):
  `q8tly-listings-pipeline/intake/bloggers/_processed/Sabah Al-Salem-Anosha-2026-06-20/`
  (`fieldkit.md` + `_ingest_notes.md`). Listing already enriched + live on staging (**post 2147**, `verified_by_q8tly=1`).
- Confirmed facts used: women-only · by appointment · daily 10:00–20:00 incl. Friday · price `$$` · KNET + Visa/Mastercard · IG @anosha_salon · phone +965 6566 5028 · strong A/C · easy parking behind the building · third floor.

## Facts discipline (carried from the ingest flags)
- **No cash claim** — cash acceptance unconfirmed; only KNET + cards stated.
- **Prayer space = on-request hospitality, in prose only.** NOT tagged/written as a "Prayer room" facility.
- No services/prices invented; the visitor left "unforgettable detail" / "if you go" blank → not fabricated.

## Update — photos + price data received (later same day)
- Bader dropped 16 photos in `Desktop/Anosha ` (trailing space). Processed:
  - **4 ambiance shots** embedded in EN + AR drafts (signage hero, hair-wash lounge, nail bar, welcome coffee).
  - **12 official price-list cards** (full service menu with KD prices).
- Optimized to WebP + JPG (1200×1600 ambiance; ~1400px cards) in the repo:
  - `assets/anosha-beauty-salon/` (ambiance) · `assets/anosha-beauty-salon/price-list/` (menu cards).
- **SEO pass done** on EN draft: keyword-tuned title/meta, `<figure>`+`<picture>` (WebP+JPG, width/height for CLS, lazy/eager+fetchpriority), services-and-prices section, FAQ, and JSON-LD (**BeautySalon** w/ geo+hours+offers, **BreadcrumbList**, **FAQPage** — all validated as parseable JSON) + OG/Twitter tags. AR mirrored (still gated).
- **Social card:** generated a 1200×630 landscape OG image (`anosha-beauty-salon-sabah-al-salem-og.jpg/.webp`) from the signage since all originals are portrait; wired into og:image + twitter:image.
- New data resolves fieldkit **F2 (price)**: real menu confirms `$$` for everyday services (manicure 6 KD, blow-dry 6 KD, colour from 35 KD; bridal up to 650 KD).
- **Salon owner/brand name:** signage reads "Anosha Beauty Salon — Nora Abul" (used as editorial colour; not asserted as a schema role).

## ✅ FINAL (2026-06-21) — live as a real `guide_article`
Core fixed the guide REST base (BIR-078, `rest_base=guides`). Recreated clean per Core's recipe **via WP-CLI over SSH** (`…@ssh.wp.com`), NOT the WordPress.com MCP (MCP can't touch the CPT).
- **guide_article ID 2189** — published, English (WPML default = no prefix).
  - Live: `https://staging-e1ff-baderlol44-pwgjm.wpcomstaging.com/guide/anosha-beauty-salon-sabah-al-salem/`
  - Edit: `…/wp-admin/post.php?post=2189&action=edit`
  - Renders with template chrome (kicker "Neighborhoods · Guide · 4 min read", byline "By Q8tly Editorial", deck, hero, share, related). No double-render. Shows on the `/guide/` hub as a card. ✓
- **Body = plain content + shortcodes** (`drafts/anosha_guide_body_EN.html`): `[q8tly_place id="2147"]` (listing card) + `[q8tly_map ids="2147"]` (map pin). No hand-built chrome.
- **Meta set:** `deck`, `article_type=guide`, `primary_topic=1716`, `word_count=767`, `hero_alt`, `hero_caption`. **Topic term:** Neighborhoods (1716).
  - ⚠ Topic = **Neighborhoods** is my judgment call (the 4 locked topics have no "Beauty"; it's a place-in-an-area spotlight). Change with `wp post term set 2189 topic <slug> --by=slug` if you prefer.
- **Old Page 2185 → trashed.** **301** added via Rank Math (redirect #1): `/anosha-beauty-salon-sabah-al-salem/` → `/guide/anosha-beauty-salon-sabah-al-salem/`. Verified: OLD=301→new, NEW=200. Caches flushed (object + WP Rocket `rocket_clean_domain`).

### 📸 Photos — ALL DONE (2026-06-21)
- **Guide hero + 3 inline + listing photo all live.** Hero = attachment 2190 (Featured + `hero_photo_id`); inline = 2192 (wash, after "What stood out"), 2193 (nail, in "What Anosha offers"), 2194 (welcome, after the coffee paragraph). Listing (gd_place 2147) photo = GD attachment 769 via `GeoDir_Media::insert_attachment` + `geodir_save_post_meta(featured_image)`; the `[q8tly_place]` card + listing page now show it. Uploads done by streaming files over SSH → `wp media import` (the API-can't-upload-binaries problem, solved).

### 🧰 Guide Ingestion Kit built (2026-06-21) — `guide-kit/`
Standing setup so future guides are turnkey (drop a folder → published guide_article). `README.md` (contract+runbook+photo-path answer), `guide.template.md`, `publish_guide.py` (dry-run default / `--execute`), `config.sh`, `BACKUP_LOG.md`, worked example `guides/_example-anosha/`. **Photo step IS automated** (SSH stream + `wp media import`). Dry-run verified.

### (original hero note)
- **HERO — DONE (2026-06-21).** Bader's editor upload didn't persist (no attachment was created; 2189 meta stayed empty). Re-did it via WP-CLI: transferred `anosha-beauty-salon-sabah-al-salem-signage.jpg` over SSH → `wp media import --post_id=2189 --featured_image` → **attachment 2190**; set `hero_photo_id=2190` + `_thumbnail_id=2190`. Hero renders (16:9 `q8-hero`), and og:image is now the hero (was the default site logo).
  - ⚠ **Edge cache gotcha:** wp-cli meta writes don't trigger the WordPress.com Atomic edge purge. `wp post update 2189` (a touch) purges it; `rocket_clean_domain()` alone wasn't enough. Use a touch after any wp-cli-only meta change.
- **Inline images — still optional (not added).** Files ready in `assets/anosha-beauty-salon/`. Same reliable path now exists (SSH → `wp media import`), so I can add these on request:
  - after “What stood out” → `anosha-beauty-salon-hair-wash-lounge.jpg`
  - in “What Anosha offers” → `anosha-beauty-salon-nail-bar.jpg`
  - near the welcome-coffee paragraph → `anosha-beauty-salon-welcome-coffee.jpg`
- The `[q8tly_place]` card + listing 2147 still show a placeholder until a photo is added to the **listing** (separate from this guide).

### AR (parked)
- Same plain-body rule applies when AR is published (WPML translation of 2189). Draft staged in `drafts/..._AR_...md`.

### (superseded) earlier same-day attempt
Originally shipped as a standard **Page 2185** (MCP can't create the CPT) — now trashed + redirected. Below entries describe that interim step.
- Full article as Gutenberg blocks (intro, What stood out, services price tables, FAQ, know-before-you-go, disclosure). Saved clean (no _content_warnings).
- SEO via native Jetpack fields: `jetpack_seo_html_title`, `advanced_seo_description`, `jetpack_seo_schema_type=article`.
- Internal link fixed to the REAL listing URL: `/places/sabah-al-salem/anosha-beauty-salon/` (GeoDirectory `gd_place`, post 2147).

### ⚠ Structural reality discovered on staging (differs from role-brief IA)
- **No `/en/` prefix — WPML not active on staging.** No `guide` CPT exists. So `/en/guide/...` is NOT a real path yet; published as a root-slug **page** instead. Building the real `/{lang}/guide/` structure (WPML + guide CPT) is Module 6 / Advisor territory — flagged, not done here.
- Kept it a **draft** (production frozen + photos pending). Flip to publish on Bader's word.

### Restyled to match the guide flow (2026-06-20, later)
- Studied existing guides: they are a **`guide_article` CPT** at `/guide/<slug>/` (e.g. `/guide/keif-restaurant-al-kout-mall/`, id 2132), with category line · byline · read-time · hero · themed sections · inline captioned images · "Best for" list · CTA · related. Categories: Food & Drink, Neighborhoods, Culture & Heritage, Seasonal.
- Rewrote page 2185 to mirror that flow: top meta line ("Beauty · Q8tly Guide · 3 min read · By Q8tly Editorial · 20 June 2026"), house pullquote (`q8tly-about__pullquote` class, matching the About page), "Best for" list, CTA to the listing. Removed broken empty image blocks → page renders clean (verified via fetch).

### ⚠ TWO things need wp-admin (API can't do them)
1. **Right post type:** page 2185 is a standard **Page**, NOT a `guide_article`. The content-authoring API only creates post/page, so it can't publish into the real `/guide/` CPT. To appear in the Guide archive/cards, recreate this as a **Guide Article** in wp-admin (copy the body from page 2185 or `drafts/..._EN_...md`), then trash the stand-in page 2185.
2. **Photos** — see below.

### Photos — NOT uploaded via API (do by drag-drop)
- Tried API upload (base64) — fails: data corrupts/truncates passing through the model ("not valid base64"). Not reliable; abandoned.
- The WordPress.com MCP only accepts media as base64; image files are too large to round-trip reliably through the model (data truncates) → risk of corrupt upload at high cost. Did NOT brute-force it.
- The page has **4 labeled photo drop-zones** (each figcaption names the exact file). To add: open Edit link → click each image block → upload from `assets/anosha-beauty-salon/` (`-signage`, `-nail-bar`, `-hair-wash-lounge`, `-welcome-coffee`; use `-og` as featured image). 20 seconds.
- Custom BeautySalon/Breadcrumb/FAQ JSON-LD (in the EN markdown draft) is NOT in the WP page — WP strips `<script>`. Add via an SEO plugin or theme head if richer schema is wanted; Jetpack `article` schema is set meanwhile.

## ➡ ROUTE to listings/data pass (NOT Module 8 to write)
- The 12 price-list cards = listing field data (Module 1/2). Hand the full service menu + prices to the listings pipeline to enrich listing **post 2147** (services, price menu). Module 8 only used a representative subset as editorial colour.

## ⚠ Open items before publish
1. ~~PHOTOS~~ **DONE** — 4 ambiance shots embedded; price cards archived in assets. On WP: upload to Media and swap `../assets/...` paths for WP media URLs.
2. **DOMAIN:** replace `https://q8tly.com` placeholder (canonical + OG + JSON-LD) with the confirmed production domain.
3. **Internal links — confirm 3 paths at build:**
   - listing → `/en/place/anosha-beauty-salon` (post 2147) — exact place URL pattern is Module 1/2; confirm.
   - area hub → `/en/sabah-al-salem` (area slug `sabah-al-salem` confirmed).
   - category → `/en/category/beauty` (confirm Salons vs Beauty slug).
   - Also add the **reverse links** from the area hub + category page back to this spotlight.
3. **Publish path:** `/{lang}/guide/anosha-beauty-salon-sabah-al-salem` — never `/blog/`. Staging only.
4. **AR gate:** do NOT publish AR until WPML is on production (S2-19) **and** a human reviews the translation. AR file is staged + flagged.

## Out of scope (routed, not touched)
- Listing data (already written by the listings pipeline), the homepage editorial widget (Module 6 — we feed it, we curate the rotation, we don't build it), and the q8tly-core plugin.

## Next session
- Drop photos in, confirm the 3 internal-link slugs, place reverse links, then move EN to "EN staged" and publish to staging under `/en/guide/`.
