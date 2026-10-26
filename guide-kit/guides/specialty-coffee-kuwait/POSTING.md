# POSTING — Specialty coffee pair (EN + AR) · ready to post, NOTHING on q8tly.com yet

**Gate:** create only after the Advisor's "window clear" (plugin release in flight; other sessions writing to prod).
Then both go in as **drafts** (EN/AR twins), the owner reads them on the site, and they **publish only on his word**.
Target = **prod** (q8tly.com; staging is stale): `GUIDEKIT_SSH_HOST` / `GUIDEKIT_SITE_URL` = prod.

## Files
| | Path | Lang | Status in file |
|---|---|---|---|
| EN | `guide-kit/guides/specialty-coffee-kuwait/article.md` | en | `draft` |
| AR | `drafts/specialty-coffee-kuwait_AR_2026-10-26.md` | ar | `draft` |
| Hero | `images/hero.jpg`: 1520×1086, EXIF-clean, sha256 `aece89dbebd5089bdf5e75ee81c3e80d2f03d275e192973c2192fb22b599c2a4` (gitignored, local only) | | |

Hero source: KODO Roastery `~/Desktop/new listing /Completed /Kodo /IMG_2315.HEIC` (5712×4284, night facade), edited as a
**local copy**. The original is untouched (sha256 `7b18b166ee6b6ae655624bed765f8c4803f1b241d8a6749800b5e7abca0fb15d`) and not
in any gallery. Edit: EXIF orientation applied, 7:5 crop (0,102)–(5712,4182), the person behind the glass blurred
(Gaussian, feathered mask, box (1990,2150)–(2520,2652) in crop px, stopping at the window frame), resized to 1520×1086,
metadata stripped. **Retouch on the owner's pass, D-254 (owner, 26 Oct 04:28).**

## SEO fields (all in the frontmatter; the kit writes them)
| | EN | AR |
|---|---|---|
| slug | `specialty-coffee-kuwait` | same (AR slug = EN slug) |
| title / H1 | The Specialty Coffee Shops of Kuwait: A Guide by Area | قهوة مختصة الكويت: المقاهي والمحامص حسب المنطقة |
| seo_title | Specialty Coffee Kuwait: Best Coffee Shops by Area (50) | قهوة مختصة الكويت: المقاهي والمحامص حسب المنطقة (47) |
| meta_description | 151 chars ("51 coffee shops…") | 109 chars ("51 كوفي…") |
| topic / type | food-drink · guide | food-drink · guide |
| place_id | 3172 (KODO Roastery, the hero's listing) | 3172 |
| hero_alt | set | set |

**Rank Math focus keywords (set by hand after create):**
- EN: `specialty coffee kuwait, best coffee shop in kuwait, coffee shop kuwait, v60 coffee`
- AR: `قهوة مختصة الكويت, محمصة قهوة الكويت, قهوة مختصة, قهوة v60`

FAQ schema: not set (no FAQPage emitter for guides, so this routes to Builder via Advisor).

## WPML twin mapping
- EN `guide_article` (new id = **E**) ↔ AR `guide_article` (new id = **A**), same trid, `ar` ← `en`.
- Hero: upload once with EN (attachment **H**); AR reuses it (`--media hero=H`).
- Links already per language. EN → `/places/…`, `/places/category/specialty-coffee/`, `/guide/best-restaurants-in-kuwait/` (6307).
  AR → `/ar/places/…`, `/ar/places/category/قهوة-مختصة/`, `/ar/guide/best-restaurants-in-kuwait/` (6309).
- Listings (51): the 53 Specialty Coffee listings (EN 1500 / AR 2030) minus Coffee Bean & Tea Leaf 4017, 4417, 4449,
  plus **Limu 7740 (EN) / 7741 (AR)**, live 26 Oct 04:29:
  `/places/shuwaikh/limu-shuwaikh/` · `/ar/places/الشويخ/limu-shuwaikh/`.

## Order of operations (when the window is clear)
1. Re-check: every listing link still 200 (EN + AR), Limu included.
2. Backup, then log it in `guide-kit/BACKUP_LOG.md` (correct the hardcoded `staging` label after a prod run).
3. `python3 guide-kit/publish_guide.py guide-kit/guides/specialty-coffee-kuwait`: dry-run, review. Then `--execute` (EN **draft** + hero). Record **E** and **H**.
4. AR twin, using the no-"+" recipe (runbook §9-G): `wp_insert_post` draft → `set_element_language_details(A,'post_guide_article',<trid of E>,'ar','en')`
   → `python3 guide-kit/populate_ar_twin.py drafts/specialty-coffee-kuwait_AR_2026-10-26.md --en-id E --media hero=H --draft` (dry-run, then `--execute`).
5. Set the Rank Math focus keywords on both. Then touch (`wp post update`) and flush the cache.
6. Owner reads both drafts on the site. **Publish only on his word.**

## ✅ POSTED AS DRAFTS — 26 Oct 2026, 04:47–04:50 Kuwait (Advisor "window clear" 04:35; under /tmp/q8tly-publish.lock 04:38:44 → 04:51:29)
- EN **7760** (draft) · AR **7762** (draft) · trid **7172** · hero attachment **7759** (shared).
- WPML proven: EN 7760 → ar 7762, AR 7762 → en 7760; AR row = the Bar Frès shape (10 / 0 / 0 / `wp` / 1). Zero raw `icl_*` writes.
- **Hero re-cut to 16:9, 1600×900** (template frame), same blur re-applied on the copy in original coordinates (1990,2252)–(2520,2754), crop y 200–3413 of 5712×4284 so the whole sign shows. sha256 `c69e817ea7f0be6668af077ecf9760c00f989e039dde57cb291c8e5565072f77`. Original still `7b18b166…fb15d`.
- Body: 60 links, Limu present, no mojibake. Focus keywords set on both; touched + Rocket flushed. Public URLs 404 (drafts). **Publish only on the owner's word.**
- Backups: `prod-20261026-014758-guide-…`, `prod-20261026-014950-ar-twin-…` (BACKUP_LOG).
