# POSTING: Laptop-friendly / study cafés in Kuwait, EN + AR · PUBLISHED 29 Oct 2026 (see the end of this file)

**Gate:** create only after the Advisor's «window clear», and only under `/tmp/q8tly-publish.lock` (never while another lane
holds it). Both go in as **drafts** (WPML twins), the owner reads them on the site, and they **publish only on his word**.
Target = **prod**: `GUIDEKIT_SSH_HOST=baderlol44-pwgjm.wordpress.com@ssh.wp.com`, `GUIDEKIT_SITE_URL=https://q8tly.com`.

## Files
| | Path | Lang | Status in file |
|---|---|---|---|
| EN | `guide-kit/guides/laptop-friendly-cafes-kuwait/article.md` | en | `draft` |
| AR | `drafts/laptop-friendly-cafes-kuwait_AR_2026-10-29.md` | ar | `draft` |
| Mock-up (approved 29 Oct 01:20) | `drafts/laptop-cafes_MOCKUP_EN-AR_2026-10-29.md` | | |

## Hero (`images/hero.jpg`, gitignored, local only)
KODO Roastery's own Q8tly gallery photo `kodo-roastery-03.jpg` (attachment **1524**, native 1600×1200 landscape): the seating
area with an open laptop. 16:9 crop rows 150–1050 → **1600×900**, Display P3 → sRGB, saved with no metadata (no EXIF/XMP/ICC).
sha256 `c49f0d0f06d796694236db745274b15f348461c9afe1c1e8da0ff09af32dd20c`. No people; the laptop screen is illegible.
On phones (16:10) the laptop stays in frame. No owner folder exists; no body photos (as for matcha/coffee).

Gallery survey of the 7 (29 Oct): native landscape ≥1520 only at **KODO** (13 × 1600×1200) and **Espresso Lab** (11 × 1600×1200).
Forest, His Majesty and Huna have portrait photos ≥1600 wide (16:9-croppable); Hoffee (max 1093) and Secret Brunch (900) don't qualify.
Note: KODO is also the specialty-coffee guide's hero venue (that one is the night facade, a different photo).

## SEO fields (in the frontmatter; the kit writes them)
| | EN | AR |
|---|---|---|
| slug | `laptop-friendly-cafes-kuwait` | same |
| title / H1 | Laptop-Friendly Cafés in Kuwait: 7 Study Cafés, Area by Area | كافيهات للدراسة في الكويت: 7 كوفيهات تناسب اللابتوب |
| seo_title | 46 chars | 49 chars |
| meta_description | 123 chars | 115 chars |
| topic / type | food-drink · guide | food-drink · guide |
| place_id | 3172 (KODO, the hero's listing; no card in the body) | 3172 |

**Rank Math focus keywords (set by hand after create):**
- EN: `laptop-friendly cafes in kuwait, study cafes in kuwait`
- AR: `كافيهات للدراسة في الكويت`

FAQ schema: not set (no FAQPage emitter for guides; routes to Builder via the Advisor, as before).

## Links
- The 7: Hoffee 7344/7345 · Secret Brunch 7532/7533 · Huna 4698/4717 · Forest 6497/6512 · His Majesty The Coffee (Bneid Al Gar)
  6465/6466 · KODO Roastery 3172/3188 · Espresso Lab — Marina Mall 4107/4128 (EN/AR listing ids).
- Closing line (no claims): Mug The Coast 4584 · Toby's Jabriya 1849 · Maroon 7645 · Limu 7740 · Gathio 7704 · Altitude 7686 ·
  Coffee Bean The Coast 4417 · EQ 1945.
- Tag archives (read from the site): EN `/places/tags/laptop-friendly/` (66), `/places/tags/study-spot/` (41); AR
  `/ar/places/tags/مناسب-للعمل-على-اللابتوب/`, `/ar/places/tags/ركن-الدراسة/`. **All four already index, follow,** self-canonical,
  hreflang-paired, in `tags-sitemap.xml` (29 Oct).
- Specialty-coffee guide: `/guide/specialty-coffee-kuwait/` (7760) · `/ar/guide/specialty-coffee-kuwait/` (7762), linked from Hoffee,
  Forest, KODO, Espresso Lab and the closing section.

## Order of operations (when the window is clear)
1. Check and take `/tmp/q8tly-publish.lock` (atomic `set -C`, long-lived holder pid). Re-check every link (200, no redirect).
2. `python3 guide-kit/publish_guide.py guide-kit/guides/laptop-friendly-cafes-kuwait` with the prod env vars: dry-run, review.
3. Same with `--execute`: backs up prod, uploads the hero, creates EN as a **draft**. Record **E** and hero **H**.
4. AR twin without the "+": `wp_insert_post` draft, slug `laptop-friendly-cafes-kuwait` →
   `$sitepress->set_element_language_details(A,'post_guide_article',<trid of E>,'ar','en')` (backup first) →
   `python3 guide-kit/populate_ar_twin.py drafts/laptop-friendly-cafes-kuwait_AR_2026-10-29.md --en-id E --media hero=H --draft`
   (dry-run, then `--execute`). **`--draft` is required.** Zero raw `icl_*` writes.
5. Prove the WPML pair both ways and compare the AR row with a known-good twin (status 10, editor `wp`, translated 1).
6. Focus keywords on both; touch with status kept as draft; Rocket flush; release the lock.
7. Owner reads: `https://q8tly.com/?post_type=guide_article&p=E&preview=true` · `https://q8tly.com/ar/?post_type=guide_article&p=A&preview=true`.
8. **Publish only on his word**, under the lock: backup, EN then AR, flush, anonymous proofs (200, title, description, canonical,
   hreflang, og:image, index, sitemap).

## Refresh rule
Update "Last updated" on both whenever any of the 7 changes (hours, Wi-Fi, closure). The At-a-glance table and each café block
must change together.

## Listing flags (route via the Advisor → Pipeline; not Blog's to change)
- **Espresso Lab (4107):** stored hours carry an extra 00:00–01:00 slot on Thursday and Friday (read literally, that's Wednesday
  and Thursday nights). The article says "6 AM to midnight daily".
- **Wi-Fi not recorded** for Secret Brunch, KODO Roastery and Espresso Lab (the article says "not listed").
- Among the 8 in the closing line: **Maroon** text says 10 PM, stored hours say 11:59 PM; **EQ** text says Essa Tower, Salem
  Al-Mubarak St, street field says Arabian Gulf St; **Altitude Roasters** has no stored hours; **Toby's Jabriya, Maroon, Limu,
  Gathio, Altitude** carry the Laptop-Friendly tag but their text says nothing about laptop or study use.

## ✅ POSTED AS DRAFTS: 29 Oct 2026, 01:59–02:08 Kuwait (Advisor «window clear»; under /tmp/q8tly-publish.lock 22:59:35Z → 23:08:06Z)
- Lock was free when checked (the Pipeline had released it). All 36 links re-checked: 200, no redirects.
- EN **7807** (draft) · AR **7809** (draft) · trid **7194** · hero attachment **7806** (shared). No body images.
- WPML proven: 7807 → ar 7809, 7809 → en 7807; AR row status 10 / translator 0 / needs_update 0 / editor `wp` / translated 1,
  same shape as matcha 7755; no NULL-element rows on trid 7194. Twin made without the "+"; zero raw `icl_*` writes.
- EN: table + 10 H2 + 3 H3, SEO title/description set, no mojibake. AR: same structure, 31 links all `/ar/` (written absolute
  by the AR tool), 0 bare `/places/`, Arabic clean, `rank_math_robots` empty (not fenced).
- Focus keywords set on both. Both touched with status kept as draft; WP Rocket flushed. Anonymous: both public URLs 404.
- Backups: `prod-20261028-230411-guide-…`, `prod-20261028-230528-pre-ar-shell-…`, `prod-20261028-230627-ar-twin-…` (BACKUP_LOG).
- Owner preview (logged in): EN https://q8tly.com/?post_type=guide_article&p=7807&preview=true · AR https://q8tly.com/ar/?post_type=guide_article&p=7809&preview=true
- **NOT published. Publish only on the owner's word** (step 8 above).

## ✅ PUBLISHED: 29 Oct 2026, ~02:33 Kuwait (owner's word; under the lock 23:31:44Z → released after proofs)
- The owner's word came while the Pipeline (P-415 photo-relink) held the lock; its holder pid was already gone, but the lock was
  left alone until the Pipeline released it (23:31:38Z). Both drafts re-checked unchanged and linked, hero 7806 intact.
- Backup `prod-20261028-233201-pre-publish-laptop-friendly-cafes-kuwait.sql.gz`, then EN 7807 → AR 7809 published, one Rocket flush.
- Live: https://q8tly.com/guide/laptop-friendly-cafes-kuwait/ · https://q8tly.com/ar/guide/laptop-friendly-cafes-kuwait/
- Anonymous proofs (one request at a time, 5 s apart): both 200; <title> = seo_title; meta description = set (123 / 115);
  canonical = URL; hreflang ar/en/x-default pair; og:image = hero (via i0.wp.com); robots index,follow; table renders; no raw
  shortcode; all 15 listings linked in the right language on each page; both URLs in `guide_article-sitemap.xml`.
