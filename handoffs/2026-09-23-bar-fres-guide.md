# Session handoff: Bar Frès (Arraya Centre) guide, EN + AR live on prod (2026-09-23)

## Status: ✅ BOTH PUBLISHED, paired in WPML (trid 6699)

| | ID | URL |
|---|---|---|
| EN | `guide_article` **6589** | https://q8tly.com/guide/bar-fres-arraya-centre/ |
| AR | `guide_article` **6591** | https://q8tly.com/ar/guide/bar-fres-arraya-centre/ |

Single-place guide about listing **6443 (EN) / 6444 (AR)**, titled "Barfres" on the site.
Sources: Bader's `~/Downloads/Q8tly-Bar-Fres-Arraya-English.md` + `…-Arabic.md` (copies in
`guide-kit/guides/bar-fres-arraya-centre/source-bar-fres-{EN,AR}.md`). The Arabic file was handed over as the
Arabic to publish (D-145 sign-off). Drop: `guide-kit/guides/bar-fres-arraya-centre/article.md`; AR draft:
`drafts/bar-fres-arraya-centre_AR_2026-09-23.md`. Bader gave the go to publish on prod in the request.

## Build changes (mechanically diffed against the sources; nothing else changed)
Both: H1, SEO block and editor notes dropped (the template renders the title; SEO went into the frontmatter).
Listing links stay **text links**. Bader's instruction was about where the link points, so no `[[place]]` card was added.

**EN (Bader's edit):** the "Not suitable for kids" bullet became
"**Better for adults.** Close seating along the belt makes it less comfortable with young children."
(The first sentence is bold, matching the other bullets.) The FAQ kids answer was not in scope and is unchanged.

**AR (Bader's edits):**
1. Listing link → `https://q8tly.com/ar/places/مدينة-الكويت/barfres/` (AR 6444, 200); guide link →
   `https://q8tly.com/ar/guide/best-restaurants-in-kuwait/` (AR 6309, 200).
2. «بحسب الفاتورة المشار إليها في هذا الدليل والمؤرخة في **١٩ سبتمبر ٢٠٢٦**، كانت الأسعار كالتالي:» →
   «في زيارة مدوّنة Q8tly بتاريخ **١٩ سبتمبر ٢٠٢٦**، كانت الأسعار كالتالي:». The trailing «والمؤرخة في <date>»
   was part of the invoice phrase and would have repeated the date. FAQ: «تراوحت أسعار الأطباق الموثقة في الفاتورة
   المشار إليها من سبتمبر ٢٠٢٦ بين …» → «في زيارة مدوّنة Q8tly بتاريخ ١٩ سبتمبر ٢٠٢٦، تراوحت أسعار الأطباق بين …».
3. **Jabriya (editor note 8): ⚠ CORRECTED.** I first reported "no branch in our data", and that was **wrong**.
   There is **no Jabriya listing on the site**: prod has only the Arraya pair 6443/6444 (6447/6448 are their revisions),
   and no other listing shares the brand's website, Instagram or Google place_id. But the **Pipeline's run log does
   record one** (P-285 TASK-1): a second "bar fres" in **Jabriya, Building 51**, on Google Places and listed as their
   Jabriya branch on their own site, which the Pipeline deliberately did not build. My grep matched "fres" inside
   "fresh", and `head` cut the output off before that line. Told Bader the same evening. Neither guide mentions Jabriya,
   so nothing published changes.

**Left as written (not in scope; flagged to Bader):** two other AR mentions of the bill, both accurate:
the intro «وأسعار الأطباق المذكورة في فاتورة سبتمبر ٢٠٢٦» and «بلغ إجمالي الفاتورة لشخصين».

## Data check vs listing 6443 (prod SSH)
These match: ground floor of Arraya Centre, Kuwait City · daily 11:00–22:00 (the EN says "from 11 AM, check the listing
for closing"; the AR says check with the restaurant) · `$$$`, about 12 KD per person · indoor only · KNET / Visa/Mastercard / Cash ·
Parisian-Japanese.
**Not on the listing / soft conflicts (not blocking, reported):**
- The listing has **no smoking value**. "No smoking" is the article's claim, not the listing's.
- The listing still carries **Family-Friendly** (EN + AR tags). The guide now says "Better for adults"
  (Pipeline-side: EN editor note 2).
- **Name:** listing title = "Barfres" (owner ruling per Pipeline P-285, "their site's spelling"). The guide styles it
  "Bar Frès" / «بار فريس Bar Fres». This doesn't show on the guide itself because it has no card.

## Meta
- EN: food-drink (1715) · guide · 741 words · deck = meta description · Rank Math title/description from the
  brief · focus keywords `bar fres kuwait, conveyor belt sushi kuwait, arraya centre restaurant, sushi kuwait`.
- AR: food-drink (1715) · 744 words · deck = the file's meta description · SEO title/description from the
  file · focus keywords `بار فريس, Bar Fres, مجمع الراية, مطعم سوشي, مطعم ياباني, سوشي` · slug = EN slug.
- **FAQ schema: NOT set.** Same as the best-of lists: guides have no FAQPage emitter, so this goes to Builder via Advisor.

## Photos: HELD (Bader, pending the restaurant's permission)
Both pages use the **flat-plate hero** (no featured image; og:image = the site default). When permission lands, run the
D-180 gate first (`GUIDE_PHOTO_STANDARD.md`; measure the landscape crop width; order-correct exif_transpose →
crop → strip). Then upload the hero to the EN post and reuse it on the AR twin (`--media hero=<id>` via
`populate_ar_twin.py` / `reinject_en.py`). Candidates are in `~/Desktop/new listing /Bader pending /Bar fres/`.
**Record corrected (Bader, 2026-09-23):** the storefront (`AC25D4FA…jpg`, the "bar frès parisian·japanese" sign) is
the **blogger's own photo, with people removed** by AI for privacy. That's allowed under the photo rule (people may be removed
or blurred; the venue must not be changed; now in `GUIDE_PHOTO_STANDARD.md` §3-D). An earlier version of this note
called it an "AI-edited screenshot". That label came from Pipeline P-285's metadata reading (its XMP carries
`Credit=Apple Photos Clean Up`, and the file shares the 6 PNGs' 1078×1459 size), which I relayed without checking.
Pipeline's P-285 also inferred from that size that the 6 PNGs are cropped screenshots. Since then (P-292, 22:22 the same evening)
Bader had the listing gallery **replaced with all 8** (`optimized images/`), storefront featured, so the listing already
uses them. For the guide, the D-180 size/ratio gate still applies: all are portrait 1078×1459 or smaller, so a landscape
7:5 crop is only ~1078 px wide, under the 1200 floor. Expect a FAIL on resolution unless larger originals exist.

## Twin creation: the no-"+" recipe (third run, runbook §9-G)
Snapshot → `wp_insert_post` draft (6591) → `$sitepress->set_element_language_details(6591,'post_guide_article',6699,'ar','en')`
→ `populate_ar_twin.py --en-id 6589` (env `GUIDEKIT_SSH_HOST`/`GUIDEKIT_SITE_URL` = prod). WPML wrote
rid 1627 `status=10, translator_id=0, needs_update=0, batch_id=0` · job 300 `editor='wp', editor_job_id=NULL,
translated=1` by itself. **Zero raw `icl_*` writes.**

## Backups (all prod, logged in `guide-kit/BACKUP_LOG.md`)
`prod-20260923-225612.sql.gz` (canon, before any write) · `prod-20260923-195646-guide-bar-fres-arraya-centre` (kit) ·
`prod-20260923-225758.sql.gz` (canon, before the twin shell) · `prod-20260923-195920-ar-twin-bar-fres-arraya-centre` (tool).

## Verified live (cache-busted, both pages)
200 · EN `lang="en-US"`, AR `dir="rtl" lang="ar"` · titles and descriptions as set · `index, follow` · self-canonical ·
hreflang ar/en/x-default identical on both · 1 H1 · deck + kicker (Food & Drink · Guide · 4 min read /
طعام وشراب · دليل · 4 دقايق من وقتك) · 8 H2 / 5 H3 · 1 table · numbered steps as `<ol>` (AR with
`list-style-type:arabic-indic`, so ١. ٢. ٣. as written) · body links exactly the 2 intended per page · AR: 0 bare `/places/`,
0 `/ar/en/` · 0 shortcode leaks · 0 mojibake in the article · Article schema headline + `inLanguage` correct ·
both edits present, old phrasings gone.

## Kit changes (`publish_guide.py`, Blog-owned)
1. **Numbered lists.** `md_to_blocks` had no ordered-list rule, so the "How it works" steps would have merged into
   one paragraph. `1. ` → `<ol>`; `١. ` → `<ol style="list-style-type:arabic-indic">`. No existing guide
   body or draft has numbered lines, so earlier guides are unaffected.
2. **UTF-8 meta on the EN create path** (the latent CHARSET.md bug, now hit): `json.dumps` with its ASCII default
   would have stored the title as "Bar Frès". New `php_str()` = `ensure_ascii=False` + `$` escaped. Tested locally
   with PHP (accents, Arabic, `$$$`, `{$x}`, backslashes) and verified on prod (`è` = `C3A8`). CHARSET.md and the
   template were updated.

## Listing flags CLOSED the same evening (Bader's instruction; see `handoffs/2026-09-23-to-pipeline-bar-fres-listing-edit.md`)
Listing 6443/6444 is now titled **"Bar Frès"** (slug `barfres` kept, so both guides' links still resolve), **Casual Dining**
+ **Upscale**, **Family-Friendly removed**, Smoking = **non-smoking**. That closes the three soft conflicts listed under
"Data check" above: the name, the Family-Friendly tag, and "No smoking" missing from the listing. Hours stay 11:00–22:00 until
Bader confirms the close with the restaurant.
