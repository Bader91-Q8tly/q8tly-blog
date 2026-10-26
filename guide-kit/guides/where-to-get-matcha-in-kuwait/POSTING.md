# POSTING — Matcha pair (EN + AR) · ready to post, NOTHING on q8tly.com yet

**Gate:** create only after the Advisor's "window clear" (plugin release in flight; other sessions writing to prod).
Then both go in as **drafts** (EN/AR twins), the owner reads them on the site, and they **publish only on his word**.
Target = **prod** (q8tly.com; staging is stale): `GUIDEKIT_SSH_HOST` / `GUIDEKIT_SITE_URL` = prod.

## Files
| | Path | Lang | Status in file |
|---|---|---|---|
| EN | `guide-kit/guides/where-to-get-matcha-in-kuwait/article.md` | en | `draft` |
| AR | `drafts/where-to-get-matcha-in-kuwait_AR_2026-10-26.md` | ar | `draft` |
| Hero | `images/hero.jpg`: 1520×1086, EXIF-clean, sha256 `5d76d49543cfee934026edd4ae78a937d056eed3a84f5345c8fd9d98101f5e82` (gitignored, local only) | | |

Hero source: Matcha Matcha Abu Halifa gallery photo `matcha-matcha-abu-halifa-08.jpg` (media 1115, 1920×2560), 7:5 crop
(0,499)–(1920,1870), resized to 1520×1086. No people in frame. Owner-approved 26 Oct 04:08 (Advisor's lean #1).

## SEO fields (all in the frontmatter; the kit writes them)
| | EN | AR |
|---|---|---|
| slug | `where-to-get-matcha-in-kuwait` | same (house convention: AR slug = EN slug) |
| title / H1 | Where to Get Matcha in Kuwait: Matcha Latte Spots by Area | ماتشا في الكويت: شنو هي، وشلون تنشرب، ووين تلقاها حسب المنطقة |
| seo_title | Where to Get Matcha in Kuwait: Matcha Latte by Area (51) | ماتشا في الكويت: وين تشربها حسب المنطقة (39) |
| meta_description | 154 chars | 116 chars |
| topic / type | food-drink · guide | food-drink · guide |
| place_id | 2669 (Matcha Matcha Abu Halifa, the hero's listing) | 2669 |
| hero_alt | set | set |

**Rank Math focus keywords (the kit doesn't write these; set by hand after create):**
- EN: `matcha latte, what is matcha, where to get matcha in kuwait, matcha powder kuwait`
- AR: `ماتشا, ماتشا بودر, بودرة ماتشا, ماتشا لاتيه`

FAQ schema: not set (guides have no FAQPage emitter, so this routes to Builder via Advisor, same as the best-of lists).

## WPML twin mapping
- EN `guide_article` (new id = **E**) ↔ AR `guide_article` (new id = **A**), same trid, `language_code=ar`, `source_language_code=en`.
- Hero: upload once with the EN post (attachment **H**); AR reuses it (`--media hero=H`).
- Links are already per language. EN → `/places/<area>/<slug>/`, `/places/tags/matcha/`, `/guide/best-restaurants-in-kuwait/` (6307).
  AR → `/ar/places/<area-ar>/<slug>/`, `/ar/places/tags/ماتشا/`, `/ar/guide/best-restaurants-in-kuwait/` (6309).
- Listings (19, EN slug = AR slug): 1831, 1948, 1945, 1833, 4561, 7220, 6465, 7452, 7645, 7686, 6193, 3275, 1852, 1864, 1849, 2669, 1875, 1949, 1906.

## Order of operations (when the window is clear)
1. Re-check: every listing link still 200 (EN + AR), and the Abu Halifa AR URL (it has a space in the area slug, linked as `%20`).
2. Backup, then log it in `guide-kit/BACKUP_LOG.md` (the kit hardcodes `staging` in the backup filename and env column; correct it after a prod run).
3. `python3 guide-kit/publish_guide.py guide-kit/guides/where-to-get-matcha-in-kuwait`: dry-run, review.
4. Same command with `--execute`. Creates EN as a **draft** with the hero. Record **E** and **H**.
5. AR twin, using the no-"+" recipe (runbook §9-G, as for Bar Frès): `wp_insert_post` draft → `$sitepress->set_element_language_details(A,'post_guide_article',<trid of E>,'ar','en')`
   → `python3 guide-kit/populate_ar_twin.py drafts/where-to-get-matcha-in-kuwait_AR_2026-10-26.md --en-id E --media hero=H --draft` (dry-run, then `--execute`). Zero raw `icl_*` writes.
6. Set the Rank Math focus keywords on both. Then `wp post update` (touch) and flush the cache.
7. Owner reads both drafts on the site. **Publish only on his word.**

## ✅ POSTED AS DRAFTS — 26 Oct 2026, 04:44–04:47 Kuwait (Advisor "window clear" 04:35; under /tmp/q8tly-publish.lock 04:38:44 → 04:51:29)
- EN **7753** (draft) · AR **7755** (draft) · trid **7169** · hero attachment **7752** (shared).
- WPML proven: EN 7753 → ar 7755, AR 7755 → en 7753; AR row status 10 / translator 0 / needs_update 0 / editor `wp` / translated 1 = the Bar Frès 6591 shape. Zero raw `icl_*` writes.
- **Hero re-cut to 16:9, 1600×900** before upload: the template renders `q8-hero` 1600×900 (hard crop) + CSS 16:9, so a 1520×1086 file would be CSS-cropped. Same source/framing (crop y 760–1840 of 1920×2560). sha256 `4f83f67c0cfc855333ededa6c5ef231db1d6dd9c9c3e574a907495c4f0e081c3`. (The 7:5 file is superseded.)
- Focus keywords set on both; touched + Rocket flushed. Public URLs 404 (drafts). **Publish only on the owner's word.**
- Backups: `prod-20261026-014407-guide-…`, `prod-20261026-014618-ar-twin-…` (BACKUP_LOG).
