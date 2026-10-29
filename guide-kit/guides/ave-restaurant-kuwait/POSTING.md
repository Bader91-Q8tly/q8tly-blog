# POSTING: AVE (Salhiya) spotlight, EN + AR · PUBLISHED 29 Oct 2026 (see the end of this file)

**Gate:** create only after the Advisor's «window clear», and check `/tmp/q8tly-publish.lock` even then (one-writer rule).
Both go in as **drafts** (WPML twins), the owner reads them on the site, and they **publish only on his word**.
Target = **prod** (q8tly.com; staging is stale): `GUIDEKIT_SSH_HOST=baderlol44-pwgjm.wordpress.com@ssh.wp.com`,
`GUIDEKIT_SITE_URL=https://q8tly.com`.

## Files
| | Path | Lang | Status in file |
|---|---|---|---|
| EN | `guide-kit/guides/ave-restaurant-kuwait/article.md` | en | `draft` |
| AR | `drafts/ave-restaurant-kuwait_AR_2026-10-28.md` | ar | `draft` |
| Mock-up (approved 28 Oct 23:40) | `drafts/ave_MOCKUP_EN-AR_2026-10-28.md` | | |

## Images (`images/`, gitignored, local only)
All from the owner's folder `~/Desktop/new listing /Bader pending /Ave`. EXIF orientation applied, Display P3 converted to
sRGB, saved with **no metadata** (no EXIF, XMP or ICC). No people in any photo (the owner's Clean Up pass removed people only).
**D-180 override granted by the owner** (28 Oct 23:40) for the collage hero and the portrait body set, as for Bar Frès.

| Stem | Section | Source (owner's #) | Size | sha256 |
|---|---|---|---|---|
| hero | top | collage #19 `CAFB5301` (x 30–802) \| #12 `9635DE59` (x 120–892) \| #26 `F616AB80` (x 60–832), rows 1–1315, 10 px white gutters | 2336×1314, exact 16:9 | `1c530beafc67bef8cc3686b538b481d478098891ea56089c4db89de9794663bd` |
| inline-1 | §1 | #11 `8D00BCEF` booth under the lit tree | 1032×1445 | `e3aeabe231494eaf095112c2a4ee32bac1c8f5c90e33508c4c999b46aedaeb6c` |
| inline-2 | §1 | #03 `13B6F85A` dessert, chocolate pour | 1024×1434 | `37aae0a15676ee82f54aaf8a818ca48275a1b0e81f81b62cba7c664c7aecbc2e` |
| inline-3 | §2 | #13 `9E219076` neon boombox corner (replaces #02) | 849×1188 | `baa89c13ddf20782f931480a626bb1a791524e85e083e6a50116e5a4b1ac3a35` |
| inline-4 | §3 | #18 `BA581FD9` table for two, greenery wall | 941×1317 | `0d647bcf195e92359663329733afe3056bfe2241962419c02946c54769f3fa4c` |
| inline-5 | §4 | #29 `IMG_1210` rose-petal heart table | 1320×1848 | `d60fe7b911816883d7124b28406c3decc663ba1838320caff32bcfb25c067b71` |
| inline-6 | §6 | #10 `72074F6D` AVE tile sign | 941×1317 | `96cd6d90494d4c978ca0fa4854c12b5e73b2ae1d3c7aa32659dad1743b9899e8` |

Hero checked at the template's frames: 16:9 desktop as built; on phones (16:10, 117 px trimmed per side) the «اڤي» sign
and the "ave" logo stay fully in frame. Left out of the guide: #02 (person), #14 / #27 / #28 (his likeness), #25 (his video on a screen).

## SEO fields (in the frontmatter; the kit writes them)
| | EN | AR |
|---|---|---|
| slug | `ave-restaurant-kuwait` | same |
| title / H1 | AVE Restaurant Kuwait: Theme Nights, Live Shows and Celebrations on Salhiya Street | مطعم افي AVE في الكويت: عشا مع عرض، ثيمات الثمانينات، وأجواء رومانسية |
| seo_title | 50 chars | 47 chars |
| meta_description | 153 chars | 130 chars |
| topic / type | food-drink · guide | food-drink · guide |
| place_id | 2666 (AVE; card at the end of §6) | 2666 (resolves to AR 2754 on the AR page) |

**Rank Math focus keywords (set by hand after create):**
- EN: `ave restaurant kuwait, romantic restaurant kuwait, birthday restaurant kuwait, late night dinner kuwait`
- AR: `مطعم افي, مطاعم رومانسية في الكويت, مطعم رومانسي, مطعم عيد ميلاد, غبقة رمضان`

FAQ schema: not set (no FAQPage emitter for guides; routes to Builder via the Advisor, as before).

## Links (all 200 on 28 Oct)
- EN: `/places/kuwait-city/ave/`, `/places/category/fine-dining/`, `/places/tags/date-night/`
- AR: `/ar/places/مدينة-الكويت/ave/`, `/ar/places/category/مطاعم-راقية/`, `/ar/places/tags/ليلة-رومانسية/`
- The listing's Book Now button goes to their Eat page; that URL is never in the text.

## Order of operations (when the window is clear)
1. Check and take `/tmp/q8tly-publish.lock` (atomic `set -C` write, long-lived holder pid). Re-check the six links (200).
2. `python3 guide-kit/publish_guide.py guide-kit/guides/ave-restaurant-kuwait` with the prod env vars: dry-run, review.
3. Same with `--execute`. It backs up prod (logged to `BACKUP_LOG.md`), uploads hero + inline-1…6, creates EN as a
   **draft** (`status: draft` in the frontmatter). Record **E**, hero **H** and the six inline ids.
4. AR twin without the "+" (runbook §9-G): `wp_insert_post` draft, slug `ave-restaurant-kuwait` →
   `$sitepress->set_element_language_details(A,'post_guide_article',<trid of E>,'ar','en')` →
   `python3 guide-kit/populate_ar_twin.py drafts/ave-restaurant-kuwait_AR_2026-10-28.md --en-id E --media inline-1=…,inline-2=…,inline-3=…,inline-4=…,inline-5=…,inline-6=…,hero=H --draft`
   (dry-run, then `--execute`). **`--draft` is required**: without it the tool publishes. Zero raw `icl_*` writes.
5. Prove the WPML pair both ways (E → ar A, A → en E) and compare the AR row with a known-good twin (status 10, editor `wp`, translated 1).
6. Set the focus keywords on both. Touch + Rocket flush. Release the lock.
7. The owner reads both drafts: `https://q8tly.com/?post_type=guide_article&p=E&preview=true` and `https://q8tly.com/ar/?post_type=guide_article&p=A&preview=true`.
8. **Publish only on his word**: EN then AR (`wp post update <id> --post_status=publish`), touch + flush, then anonymous proofs
   (200, title/description, canonical, hreflang pair, og:image = hero, index/follow, sitemap, `/ar/places/` card on the AR page).
   For a body fix while still a draft, `reinject_en.py` now keeps the draft status (fixed 28 Oct); `--status publish` only on his word.

## Seasonal refresh
The **Ramadan ghabga** section (§5, «غبقة رمضان» 70/mo) must be refreshed before **Ramadan 2027** (expected early February
2027): refresh by **mid-January 2027**, with the owner's word on what AVE is doing that year. Update "Last updated" on both.

## Listing flags (route via the Advisor; not Blog's to change)
- No hours stored on 2666/2754 (the article says "open late", the owner's words, and "call ahead").
- The "Calm & Quiet" tag conflicts with the owner's "sometimes loud".
- The listing description's extras (cheesecake, polaroids, price) are not in the owner's review; the article leaves them out.

## ✅ POSTED AS DRAFTS: 29 Oct 2026, 00:46–00:56 Kuwait (Advisor «window clear»; under /tmp/q8tly-publish.lock 21:46:09Z → 21:55:55Z)
- EN **7776** (draft) · AR **7778** (draft) · trid **7185** · hero **7769** · inline-1…6 = **7770–7775** (shared by both).
- WPML proven: 7776 → ar 7778, 7778 → en 7776; AR row status 10 / translator 0 / needs_update 0 / editor `wp` / translated 1,
  same shape as matcha 7755; no NULL-element rows on trid 7185. Twin made without the "+"; zero raw `icl_*` writes.
- AR content: Arabic clean (no mojibake), «اڤي» present, 6 images + hero, card 2666, `rank_math_robots` empty (not fenced).
- Focus keywords set on both (values above). Both touched with status kept as draft; WP Rocket flushed.
- Anonymous: `/guide/ave-restaurant-kuwait/`, `/ar/guide/ave-restaurant-kuwait/` and `?p=7776` all 404 (drafts not public).
- Backups: `prod-20261028-214743-guide-…`, `prod-20261028-215150-pre-ar-shell-…`, `prod-20261028-215409-ar-twin-…` (BACKUP_LOG).
- Owner preview (logged in): EN https://q8tly.com/?post_type=guide_article&p=7776&preview=true · AR https://q8tly.com/ar/?post_type=guide_article&p=7778&preview=true
- **NOT published. Publish only on the owner's word** (step 8 above).

## ✅ PUBLISHED: 29 Oct 2026, ~01:00 Kuwait (owner's word; under the lock 21:59:06Z → 22:00:42Z)
- Backup `prod-20261028-215923-pre-publish-ave-restaurant-kuwait.sql.gz`, then EN 7776 → AR 7778 published, one Rocket flush; twins still linked.
- Live: https://q8tly.com/guide/ave-restaurant-kuwait/ · https://q8tly.com/ar/guide/ave-restaurant-kuwait/
- Anonymous proofs (one request at a time, 5 s apart): both 200; served <title> = seo_title; meta description = set (153 / 130);
  canonical = URL; hreflang ar/en/x-default pair; og:image = hero (`guidekit-ave-restaurant-kuwait-hero.jpg` via i0.wp.com);
  robots index,follow; 6 body images render, no raw shortcode; listing link per language (`/places/kuwait-city/ave/`,
  `/ar/places/مدينة-الكويت/ave/`); both URLs in `guide_article-sitemap.xml`.
- Next touch: the Ramadan §5 refresh by mid-January 2027.

## AR meta description changed: 29 Oct 2026, ~19:13 Kuwait (owner's instruction; under the lock)
The new romantic-restaurants guide (7850/7852) now owns «مطاعم رومانسية في الكويت», so the AVE AR description leads with «مطعم افي».
- 7778 `rank_math_description` **and** `post_excerpt` (the schema reads the excerpt) → «مطعم افي AVE بشارع الصالحية: عشا مع عرض حي، ثيمات الثمانينات، بكجات عيد ميلاد وعيد زواج، غبقات رمضان، ويفتح لين وقت متأخر.» (122)
- Was: «تدور مطاعم رومانسية في الكويت؟ مطعم افي AVE بشارع الصالحية: عشا مع عرض، ثيمات الثمانينات، بكجات عيد ميلاد وعيد زواج، وغبقات رمضان.» (130)
- Backup `prod-20261029-161227-pre-ave-ar-meta-7778.sql.gz`. Content unchanged; EN 7776 untouched. Proof in
  `guide-kit/guides/romantic-restaurants-kuwait/POSTING.md`.
