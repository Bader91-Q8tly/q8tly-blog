# Session handoff: "The 10 Best Restaurants in Kuwait (2026)", EN live on prod (2026-09-22)

## Status: ✅ EN PUBLISHED, `guide_article` 6307 · https://q8tly.com/guide/best-restaurants-in-kuwait/

**First best-of list in the corpus.** Source: Bader's `~/Downloads/Q8tly-Best-Restaurants-Kuwait-English.md`
(copy at `guide-kit/guides/best-restaurants-in-kuwait/source-best-restaurants-EN.md`). Bader's
request included the go to publish ("after you finish the English…"). Prod target per the post-flip env.

- **Backup:** `prod-20260922-145424-guide-best-restaurants-in-kuwait.sql.gz` (3.2 MB, gzip-tested,
  `Dump completed`), logged `| prod |` by the kit.
- **Meta:** topic food-drink (1715) · article_type guide · word_count 1202 · deck = the brief's meta
  description · `rank_math_title` / `_description` from the brief · `rank_math_focus_keyword` =
  the focus keyword plus the 3 secondaries (set post-run, then touch + flush).
- **Hero:** reused attachment **5427** (Solange Maison dining room, 1520×1086, already D-180
  fitted). No photos came with the article; Bader picked this one. No inline images.

## Build changes (Bader-approved, the ONLY diffs from source; mechanically diffed)
1. H1 and the "SEO settings" block were dropped (the template renders the title; SEO went to frontmatter).
2. The 10 "See X on Q8tly" text links became **10 `[q8tly_place]` cards**, which give each entry a photo
   and resolve to `/ar/places/` on the AR twin automatically.
3. **`[q8tly_map]` of all 10** in list order, placed after the quick-list table. ⚠ It renders as a
   numbered **"On the map" list with Directions links**, not a tile map: interactive tiles are still
   deferred Builder work (Variant-E Leaflet chunk).
4. Solange: "**Booking is required**" became "**Booking is recommended**", and the FAQ line became
   "Solange recommends booking". This matches listing 4025 (tag *Reservations Accepted*) and the live
   Solange Maison guide ("Reservations: Available").

## Data check (all 10 listings pulled over prod SSH)
Every other claim matches the listings' About text and fields (area, price tier, hours, Chops'
8–10 KD, walk-in, breakfast 9–noon, etc.). The source's `/places/…` URLs all matched their live
listings exactly. IDs (EN): MizuMesa 2354 · Solange 4025 · Naranj 2239 · Cure 3807 · Off the Coal 4330 ·
Amiti Noura 3145 · Chef Pillai 2818 · Kiwa 1939 · Queens 4659 · Chops 5575.

## Verified live (cache-busted)
200 · `<title>` + meta description from the brief · `index, follow` · self-canonical · 1 H1 · deck +
byline · hero 5427 = og:image · **10 place cards, 0 tombstones**, all hrefs correct · **map 10 pins
+ 10 Directions** · 0 raw shortcode leak · 1 table · 13 H2 / 4 H3 · no mojibake · Article schema
headline correct. `/ar/guide/best-restaurants-in-kuwait/` (no twin yet) serves the EN fallback as
**`noindex`** (the v1.14.381 fallback fix is holding, so nothing leaks while the AR is pending).

## Kit changes (`publish_guide.py`, documented in README + template)
- **`[[place:ID]]` marker**: a card for another listing. Shared through `md_to_blocks`, so
  `populate_ar_twin.py` / `reinject_en.py` understand it too (the AR draft can use the same markers).
- **`hero_id:` frontmatter**: reuses an existing attachment as the hero, with no re-upload.
- Remote validation now checks **every** place ID (place_id + `[[place:ID]]` + `map_ids`), plus
  that `hero_id` is an attachment.

## Owed / routed
- **FAQ schema: NOT set (→ Builder via Advisor).** The brief asks for FAQPage schema on the FAQ.
  Guides have no FAQPage emitter: q8tly-core emits Article + BreadcrumbList for guide singles, and
  FAQPage only on category archives (`archive-seo.php`). Rank Math's own graph doesn't render on
  guides. Note: since 2023 Google shows FAQ rich results only for government and health sites, so
  the payoff is small.
- **Solange naming.** The article says "Solange", matching listing 4025, which is *still* titled
  "Solange" despite Bader's 2026-08-13 ruling (canonical = "Solange Maison", routed to Pipeline).
  The list and the card agree with each other but not with our own Solange Maison guide.
- Kiwa's card renders "**KIWA**" (the listing title is in caps); the article says "Kiwa". Cosmetic, listing-side.

## ✅ AR TWIN LIVE, `guide_article` 6309 · https://q8tly.com/ar/guide/best-restaurants-in-kuwait/

Source: Bader's `~/Downloads/Q8tly-Best-Restaurants-Kuwait-Arabic.md` (copy beside the EN source),
handed over as the Arabic to publish (D-145 sign-off). Draft: `drafts/best-restaurants-in-kuwait_AR_2026-09-22.md`.
Only the "ready to publish" section was used; the editor notes, Ahrefs keyword table and handoff steps were not published.
The AR is **not a strict mirror** of the EN. It's SEO-adapted: 6 FAQs vs 4, and an extra "for lunch" line.
Everything added was fact-checked against the listings (lunch service, baby chairs at Queens + Kiwa).

**Build changes:** H1 dropped · 10 "شاهد تفاصيل" links became the same `[[place]]`/`[[place:ID]]` cards
as the EN · `[[map]]` after the table. **Bader-approved text edits** (exact wording shown and picked):
Solange "يحتاج إلى حجز" became "يُنصح بالحجز" (body + FAQ) · restored Amiti Noura breakfast ٩–١٢, Chops hours
١٢:٣٠–١١:٣٠ and ٨–١٠ KD (the writer had dropped them "pending verification"; all three are on the live
listings) · hero_alt (Blog-drafted, approved). Deck = the file's meta description. Slug = EN slug (house convention;
the file's Arabic slug was marked "suggestion only"). SEO title/description from Bader's file; focus keywords = the file's 5.

**Twin creation, with NO "+" pressed** (new, cleaner variant, now in runbook §9-G):
`wp_insert_post` draft → `$sitepress->set_element_language_details(6309,'post_guide_article',6574,'ar','en')`
→ `populate_ar_twin.py --en-id 6307 --media hero=5427` (env `GUIDEKIT_SSH_HOST`/`GUIDEKIT_SITE_URL` = prod).
**WPML wrote the TM rows itself** on the populate save: rid 1505 `status=10, translator_id=0, needs_update=0` ·
job 287 `editor='wp', translated=1`. That's identical to good twin Cure 5032 (only `batch_id` 0 vs 54).
**Zero raw `icl_*` writes.**
Backups: `prod-20260922-185639.sql.gz` (canon, pre-create) + `prod-20260922-155801-ar-twin-…` (tool).

**Verified live, cache-busted:** 200 · `lang="ar" dir="rtl"` · title/description Arabic from Bader's file ·
`index, follow` · self-canonical · hreflang ar/en/x-default on **both** pages · kicker «طعام وشراب · دليل ·
7 دقايق من وقتك» · 1 H1 · hero alt · **10 cards all `/ar/places/…`**, CTA «عرض المكان», 0 tombstones ·
map «على الخريطة» 10 pins, all `/ar/` · 0 bare `/places/` · 0 `/ar/en/` · 0 shortcode leak · no mojibake ·
all 5 approved edits present, 0 "يحتاج إلى حجز" left · Article schema `inLanguage: ar`.

**Side notes (not blocking):**
- Chef Pillai's AR listing URL has a literal space in the district (`/ar/places/أبو حليفة/…`, `%20`). It resolves
  200, but every other district slug is hyphenated (`مدينة-الكويت`). Listing-side → Pipeline.
- Topic term: the twin carries EN term 1715 (same as Cure AR 5032). Solange AR 5436 carries 1715 **and**
  AR term 2368, so the corpus is inconsistent. The kicker renders Arabic either way.
- Solange AR 5436's TM row shows `needs_update=1` (WPML thinks it's stale vs EN 5430). Pre-existing, not touched.

## Fix round on the AR twin 6309 (Bader-requested, same day) — via `populate_ar_twin.py`
Backup: `prod-20260922-220451.sql.gz` (canon, pre-write) + the tool's own dump.
1. **Western digits** in `post_title`/H1, `rank_math_title` and `rank_math_description`
   («أفضل 10 مطاعم في الكويت (2026)»). Verified zero Eastern-Arabic digits in all three.
   The **deck and body keep Eastern-Arabic digits** by instruction, so the on-page deck reads ١٠
   while the search snippet reads 10.
2. **The 10 headings** moved to «الاسم العربي (Latin):», matching the Italian guide.
   ⚠ **Provenance:** this article contained NO Arabic name spellings (headings were Latin-only), and
   neither do the 10 AR listing twins (all Latin-titled). Only 2 of 10 existed anywhere in the corpus
   (نارنج 2612, ميزوميسا 2618). Rather than invent 8, Blog asked; **Bader supplied all 10 himself**
   (2026-09-22) and they were injected verbatim: ميزو ميسا · سولانج · نارنج · كيور · أوف ذا كول ·
   عمتي نورة · شيف بيلى · كيوا · كوينز · تشوبس.
   ⚠ **Corpus conflict:** Bader's «ميزو ميسا» (two words) differs from the live MizuMesa AR guide
   title «ميزوميسا» (2618). Not reconciled — owner's call which spelling is canonical.
3. **The quick-list table keeps Latin-only names** — Blog asked, no answer given, so not changed.
4. **Place cards still render Latin names** (Solange, Cure, …) because the AR *listings* are Latin-titled.
   Listing-side → Pipeline.
Re-verified: 10 cards all `/ar/places/`, 10 map pins, 1 table, 0 shortcode leak, no mojibake,
`index, follow`, self-canonical, and the three earlier approved edits (Solange booking, Amiti breakfast,
Chops price) all intact.

## Third fix round (Bader, same day) — EN 6307 **and** AR 6309
Backup: `prod-20260922-222816.sql.gz` (canon) + each tool's own dump
(`…-192933-en-guide-…`, `…-193037-ar-twin-…`). EN went through `reinject_en.py`
(idempotency diff shown before writing: 35 lines, all intended), AR through `populate_ar_twin.py`.
1. **ميزو ميسا → ميزوميسا** (one word), matching the sign and MizuMesa guide 2618. The two-word
   form from the 2nd pass is gone from the page.
2. **Quick-list table** name column moved to the bracket style, matching the headings (10 cells).
3. **شيف بيلى → شيف بيلاي.**
4. **"Solange" → "Solange Maison"** in BOTH flagship languages: EN heading, table, body, occasion
   list, 2 FAQ answers and `hero_alt`; AR heading + table («سولانج ميزون (Solange Maison)», the Arabic
   form taken from **Bader's own** Solange AR draft, not invented), 6 Latin prose mentions and `hero_alt`.
   The EN/AR flagships and the Solange Maison spotlight guide now agree on the name.
⚠ **Still "Solange" on both pages — but only in the place card and the map pin**, because listing
4025 is *still titled "Solange"*. Verified: 3 occurrences per page, all from the card/pin markup, none
from article text. That rename is the long-standing Pipeline item (routed 2026-08-13, still open).
Re-verified both pages: 10 cards + 10 pins each, 1 table, 0 shortcode leak, no mojibake,
EN and AR both `index, follow`, AR H1 «أفضل 10 مطاعم في الكويت (2026)».

