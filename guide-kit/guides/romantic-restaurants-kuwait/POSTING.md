# POSTING: 7 romantic restaurants in Kuwait, AR (lead) + EN · READY TO POST (drafts only, nothing on q8tly.com)

**Gate:** create only after the Advisor's «window clear», and only under `/tmp/q8tly-publish.lock` (never while another lane
holds it). Both go in as **drafts** (WPML twins), the owner reads them on the site, and they **publish only on his word**.
Target = **prod**: `GUIDEKIT_SSH_HOST=baderlol44-pwgjm.wordpress.com@ssh.wp.com`, `GUIDEKIT_SITE_URL=https://q8tly.com`.

## Files
| | Path | Lang | Status in file |
|---|---|---|---|
| EN | `guide-kit/guides/romantic-restaurants-kuwait/article.md` | en | `draft` |
| AR (lead) | `drafts/romantic-restaurants-kuwait_AR_2026-10-29.md` | ar | `draft` |
| Mock-up (approved 29 Oct 18:40) | `drafts/romantic-restaurants_MOCKUP_AR-EN_2026-10-29.md` | | |

## Owner + Advisor decisions (29 Oct 18:40)
1. Hero = Solange Maison's lamp-lit table for two. 2. One photo per restaurant; **D-180 override granted for Nōya and Roka**
(as for AVE). 3. AVE = the listing's own line + a pointer to the AVE guide. 4. AR headings = each restaurant's AR title exactly as
stored (all seven are Latin), no new Arabic spellings. 5. Grouped by occasion. Plus: replace the AVE guide's AR meta description
(below), and add `rel="nofollow"` support to the kit (done: `publish_guide.py` `md_link()`, README §1).

## Images (`images/`, gitignored, local only)
All from the owner's folders in `~/Desktop/new listing /` except inline-7 (MizuMesa has no folder there; its June photo from
`guide-kit/guides/mizumesa-sharq/images/inline-1.jpeg` is the owner's). EXIF orientation applied, Display P3 → sRGB, saved with
**no metadata** (no EXIF, XMP or ICC). No people in any photo. AVE's IMG_1210 carries the owner's Clean Up pass (people only, 28 Oct).

| Stem | Restaurant | Source | Size | sha256 |
|---|---|---|---|---|
| hero | Solange Maison | `Completed by folder/Fine dining…/solage/optimized images/IMG_4010.webp`, 16:9 band rows 670–1570 | 1600×900 | `00febe5cffe878381e03336fa13582d7d9eb524ade62785ac816ab40c958484e` |
| inline-1 | Nōya | `Completed/_processed/Noya/9BA89F7F…jpg` sunset over the city (**override**) | 941×1176 | `090beee6438ef0889abe7a3c93165227157cfb6c5c61e4aad71e4b832abf9baa` |
| inline-2 | Amimoto | `Completed/Amimoto/IMG_2286.HEIC` window table, sea view (from 4032×3024) | 2000×1500 | `cac4a0b1dca7c0d6e6b30436d951e3ea156f4e543b0f6cdcb386e0f8b31f2f0a` |
| inline-3 | Piatti | `Completed/_processed/Piatti/IMG_3241.heic` "Happy Birthday" cake (from 2219×2774) | 1600×2000 | `67edd58b1cc32f55c1b1e30e19e484546b4418b6b7e8cb7e9a55bd960f8acc34` |
| inline-4 | Roka | `Completed/_processed/Roka/BA0E7D54…jpg` window table (**override**) | 941×1176 | `daec24809077dafccaf5da1b084d51a6c5830734e34d3b53cc8e088655125200` |
| inline-5 | AVE | `Completed/Ave/IMG_1210.jpg` rose-petal heart table (also AVE guide inline-5) | 1320×1848 | `e6d50f78c23578aac1a64d69757c7e88f699c31eb674bc03162ab2cb5eb789fd` |
| inline-6 | Solange Maison | `…/solage/optimized images/IMG_4003.webp` table under the tiled mural | 1600×2844 | `951193d455259b9e41d0538bfbd3ad1a4a8c4a724fd1fc141893307f28ee6792` |
| inline-7 | MizuMesa | `guide-kit/guides/mizumesa-sharq/images/inline-1.jpeg` green booth | 1536×2048 | `9980124b8359bfd1e313f9e3b49f0793c6587741be71f9480657feef4e2c1083` |

Hero at the template's frames: 16:9 desktop as built; on phones (16:10, ~80 px trimmed per side) the lamp and both place
settings stay in frame. Body photos render whole (max 540 px tall desktop, 420 phone). The kit has no inline reuse, so inline-5
and inline-7 upload as new copies (as on earlier guides).

## SEO fields (in the frontmatter; the kit writes them)
| | AR (lead) | EN |
|---|---|---|
| slug | `romantic-restaurants-kuwait` | same (404 on 29 Oct = free) |
| title / H1 | مطعم رومانسي في الكويت: 7 مطاعم رومانسية للعشاء | Romantic Restaurants in Kuwait: 7 Places for a Date Night Dinner |
| seo_title | 47 chars | 50 chars |
| meta_description | 146 chars | 150 chars |
| topic / type | food-drink · guide | food-drink · guide |
| place_id | 4025 (Solange Maison, the hero's listing; no card in the body) | 4025 |

**Rank Math focus keywords (set by hand after create):**
- AR: `مطعم رومانسي الكويت, مطاعم رومانسية في الكويت`
- EN: `romantic restaurants in kuwait, date night kuwait`

FAQ schema: not set (no FAQPage emitter for guides; routes to Builder via the Advisor, as before).

## Links (all checked 29 Oct: 20 unique per article, every page 200 with no redirect)
- The 7 (EN / AR listing ids): Nōya 7386/7387 · Amimoto 3125/3144 · Piatti 7408/7409 · Roka 7474/7475 · AVE 2666/2754 ·
  Solange Maison 4025/4040 · MizuMesa 2354/2405.
- **Booking** `https://q8tly.com/go/book/<slug>?from=web&lang=<en|ar>`, written with `rel="nofollow"` by the kit. All 14 302 to the
  venue: Nōya noya.live · Amimoto **the shared Kuwait Towers restaurants page** (the text says to choose Amimoto) · Piatti, Solange,
  MizuMesa SevenRooms · Roka rokarestaurant.com (The Avenues branch; Cloudflare blocks automated checks) · AVE Eat App.
- Date Night tag: EN `/places/tags/date-night/` · AR `/ar/places/tags/ليلة-رومانسية/` (41 places). Fine Dining: EN
  `/places/category/fine-dining/` · AR `/ar/places/category/مطاعم-راقية/` (30). **All four already index, follow,**
  self-canonical, hreflang-paired, in `tags-sitemap.xml` / `gd_placecategory-sitemap.xml`.
- Guides: AVE (7776/7778) from AVE's block + FAQ 3 · Solange Maison and MizuMesa spotlights from their blocks · best restaurants
  in Kuwait (6307/6309) from the closing section.

## Order of operations (when the window is clear)
1. Check and take `/tmp/q8tly-publish.lock` (atomic `set -C`, long-lived holder pid). Re-check every link (200; booking 302s).
2. `python3 guide-kit/publish_guide.py guide-kit/guides/romantic-restaurants-kuwait` with the prod env vars: dry-run, review
   (expect 7 `rel="nofollow"` links in the body).
3. Same with `--execute`: backs up prod, uploads hero + inline-1…7, creates EN as a **draft**. Record **E**, hero **H** and
   the seven inline ids **I1…I7**.
4. AR twin without the "+": `wp_insert_post` draft, slug `romantic-restaurants-kuwait` →
   `$sitepress->set_element_language_details(A,'post_guide_article',<trid of E>,'ar','en')` (backup first) →
   `python3 guide-kit/populate_ar_twin.py drafts/romantic-restaurants-kuwait_AR_2026-10-29.md --en-id E --media hero=H,inline-1=I1,…,inline-7=I7 --draft`
   (dry-run, then `--execute`). **`--draft` is required.** Zero raw `icl_*` writes.
5. Prove the WPML pair both ways and compare the AR row with a known-good twin (status 10, editor `wp`, translated 1).
6. Focus keywords on both; touch with status kept as draft; Rocket flush; check the served HTML of both previews carries
   `rel="nofollow"` on the 7 booking links; release the lock.
7. Owner reads: `https://q8tly.com/?post_type=guide_article&p=E&preview=true` · `https://q8tly.com/ar/?post_type=guide_article&p=A&preview=true`.
8. **Publish only on the owner's word**, under the lock: backup, EN then AR, then the AVE meta change below, flush, anonymous
   proofs (200, title, description, canonical, hreflang, og:image, index, sitemap) on both new pages and on the AVE AR page.

## AVE guide: AR meta description (owner's instruction, 29 Oct 18:40)
Done in step 8, in the same publish window, so «مطاعم رومانسية في الكويت» moves from AVE to this guide in one go (AVE doesn't
lose the phrase before this guide is live). Backup first; AR post **7778** only; EN 7776 untouched.
- **Now** (130): «تدور مطاعم رومانسية في الكويت؟ مطعم افي AVE بشارع الصالحية: عشا مع عرض، ثيمات الثمانينات، بكجات عيد ميلاد وعيد زواج، وغبقات رمضان.»
- **New** (122): «مطعم افي AVE بشارع الصالحية: عشا مع عرض حي، ثيمات الثمانينات، بكجات عيد ميلاد وعيد زواج، غبقات رمضان، ويفتح لين وقت متأخر.»
- How: read and record the current `rank_math_description` of 7778 → `update_post_meta(7778,'rank_math_description',…)` from a
  UTF-8 PHP file streamed over SSH (never inline shell quoting for Arabic) → `wp post update 7778` (touch, status stays publish)
  → Rocket flush → anonymous check of `<meta name="description">` and `og:description` on `/ar/guide/ave-restaurant-kuwait/`.
  Also update the AVE row in the calendar and `ave-restaurant-kuwait/POSTING.md`.

## Refresh rule
**By 7 February 2027** (before 14 February), and whenever any of the 7 changes: re-read the listings (hours, booking links,
closure), update EN + AR together (table + blocks + FAQ), bump "Last updated". Use `reinject_en.py` / `populate_ar_twin.py`
(both keep the status).

## Listing flags (route via the Advisor → Pipeline; not Blog's to change)
- **AVE (2666):** no hours stored; the "Calm & Quiet" tag conflicts with "sometimes loud" in the owner's review (flagged 28 Oct).
- **Amimoto (3125):** booking lands on the shared Kuwait Towers page, not an Amimoto-only page. The text's "lower floor of
  Kuwait Towers" reads like ground level, while the owner's photos look down on the coast from high in the tower; the
  wording is ambiguous, so the guide leaves the floor out.
- **Nōya (7386):** the title is «Nōya», the text says "Noya" (EN and AR).
- **MizuMesa (2354):** city field Sharq, text "KIPCO area of Kuwait City" (both true; the guide says Sharq, as the URL does).
- **Photos:** Roka's and Nōya's venue shots top out at 1034 / 941 px wide. Larger originals would remove the override.
