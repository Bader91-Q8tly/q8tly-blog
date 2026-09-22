# Session handoff: "The 11 Best Italian Restaurants in Kuwait (2026)", EN live on prod (2026-09-22)

## Status: ✅ EN PUBLISHED, `guide_article` 6313 · https://q8tly.com/guide/best-italian-restaurants-in-kuwait/

Best-of list #2, same session as list #1 (`handoffs/2026-09-22-best-restaurants-list.md`, which has the
full method). Source: `~/Downloads/Q8tly-Best-Italian-Restaurants-Kuwait-English (1).md` (copy at
`guide-kit/guides/best-italian-restaurants-in-kuwait/source-best-italian-EN.md`).

- **Backup:** `prod-20260922-170719-guide-best-italian-restaurants-in-kuwait.sql.gz` (gzip-tested), kit-logged.
- **Meta:** food-drink (1715) · guide · 1470 words · deck = the brief's meta description · Rank Math
  title/description from the brief · focus keywords = the 4 from the brief (set post-run, touch + flush).

## Build changes (mechanically diffed; nothing else changed)
1. H1 + SEO block dropped.
2. 11 "See X on Q8tly" links became `[[place]]`/`[[place:ID]]` cards, plus `[[map]]` after the table. This is the pattern Bader chose for list #1,
   applied without re-asking.
3. **Intro fix (Bader-approved):** "a brasserie facing the opera house fountain" became "a brasserie at the opera
   house, facing the museum fountain", matching the Novikov section and listing 5368.
4. The brief's internal link to `/guide/best-restaurants-in-kuwait/` was kept. Confirmed live (EN 6307), per the
   brief's "internal link to check" note.

## Data check: all 11 listings pulled over prod SSH, every claim matches
Hours in the quick-list table (including Trapani's Thu–Sat 11:30, NAC's and OFK's Thu–Fri late closes, Delizio to 1 AM),
price tiers, KD figures (Novikov 15, Delfino 16, Delizio 9–10, Utopia 8–10, Select 15), seating, and the three
"booking required" claims (the Novikov/Paparazzi/Delfino listing About texts all say *required*). The "first seven are pure Italian"
line holds: those seven listings have cuisine = Italian only.
IDs: Trapani 1920 · Novikov 5368 · Paparazzi 4643 · Delfino 5059 · Delizio 6072 · Utopia 5905 · Eataly 6012 ·
NAC 3385 · Si 4224 · Select 3231 · OFK 4618.

## Hero: D-180 gate
No photos came with the article. I screened all 122 listing photos across the 11 listings by stored metadata dims, and 9 are native
landscape ≥1520px (Trapani 1, Eataly 5, Paparazzi 2, OFK 1; the Paparazzi/OFK ones only reach 1417/1440 wide
after a 7:5 crop, so CONDITIONAL). Bader picked **Trapani** (1920×1440 native landscape → PASS). Fitted
order-correct (exif_transpose → 7:5 crop, top 50px of plain ceiling trimmed → 1520×1086 → EXIF stripped).
Uploaded as **attachment 6312**. The served CDN copy was re-downloaded: 1520×1086, no orientation flag. Both signs
(Latin + Arabic) legible, domes whole.
⚠ **Rights unverified:** the source filename `…_rw_1920.jpg` is the Adobe Portfolio/Behance web-resize pattern,
so it's likely a designer's or photographer's shot, not a Q8tly visit photo. Bader chose it with that flagged. It's
already the listing's featured image (Pipeline sourced it); as the guide hero it's also the social share image.

## Verified live (cache-busted)
200 · title/description · `index, follow` · self-canonical · 1 H1 · deck · og:image = new hero · **11 cards, 0
tombstones**, hrefs correct · **map 11 pins + 11 Directions** · internal link present · 0 shortcode leak ·
1 table · 14 H2 / 5 H3 · no mojibake · Article schema. `/ar/…` fallback = `noindex` until the twin exists.

## Notes
- Select's card reads "**Select (Avenues)**" (that's the listing title). Cosmetic, listing-side.
- FAQ schema: same as list #1. Not settable (no FAQPage emitter for guides) → Builder via Advisor.
- Optional (not done, unasked): list #1 could link back here ("Looking for Italian?") for two-way internal linking.

## ✅ AR TWIN LIVE, `guide_article` 6315 · https://q8tly.com/ar/guide/best-italian-restaurants-in-kuwait/

Source: `~/Downloads/Q8tly-Best-Italian-Restaurants-Kuwait-Arabic.md` (copy beside the EN source),
handed over as the Arabic to publish (D-145 sign-off). Draft: `drafts/best-italian-restaurants-in-kuwait_AR_2026-09-22.md`.
The writer had already resolved the **Arabic** listing URLs and the Arabic first-list URL from hreflang, and all of them checked out.

**Build changes:** H1 dropped · the 11 links became the same `[[place]]`/`[[place:ID]]` cards (EN ids; the
shortcode resolves language at source) · `[[map]]` after the table. **Bader-approved edit:** Delfino
"يُفضّل ترتيب الحجز مسبقًا" → "والحجز المسبق مطلوب", matching EN + listing 5059. hero_alt Blog-drafted, approved.
Deck = the file's meta description. Slug = EN slug. SEO title/description + 4 focus keywords from the file.

**Deliberately not a mirror of the EN** (the file's own editor notes): an extra
«تبحث عن مطعم إيطالي بالأفنيوز؟» section, 6 FAQs including a cost question, and softened claims
(the photographer, the birthday cake, breakfast timing). Fact-checked against the live listings: nothing
contradicts a listing. The Arabic table's hours, KD figures and seating all match.
Its editor note #4 asks to correct the EN intro's "purely Italian" phrasing — **no change needed**: the EN
already says the first seven are Italian and the last four are mixed, which is what the listings show.

**Twin creation:** the no-"+" recipe again (snapshot `prod-20260922-212041` → `wp_insert_post` draft →
`set_element_language_details(6315,'post_guide_article',6577,'ar','en')` → `populate_ar_twin.py --en-id 6313
--media hero=6312`). WPML wrote rid 1506 `status=10, needs_update=0` · `editor='wp', translated=1` by itself —
second confirmation of the recipe. Tool backup: `prod-20260922-182140-ar-twin-…`.

**Verified live, cache-busted:** 200 · `lang="ar" dir="rtl"` · Arabic title/description · `index, follow` ·
self-canonical · hreflang ar/en/x-default · 1 H1 · hero alt + og:image · **11 cards all `/ar/places/…`**,
0 tombstones · map 11 pins all `/ar/` · internal link → `/ar/guide/best-restaurants-in-kuwait/` ·
0 bare `/places/` · 0 `/ar/en/` · 0 shortcode leak · 1 table · 15 H2 / 6 H3 · no mojibake ·
Delfino edit present, old phrasing gone · Article schema `inLanguage: ar`.

## Fix round on the AR twin (Bader-requested, same day) — re-injected via `populate_ar_twin.py`
Backups: `prod-20260922-212942.sql.gz` (canon, pre-write) + `prod-20260922-183043-ar-twin-…` (tool).
1. `rank_math_title` → «مطعم إيطالي بالكويت: أفضل 11 مطعم للبيتزا والباستا (2026) | Q8tly».
2. **Western digits in the SEO title + meta description** (11, 2026). Verified: zero Eastern-Arabic
   digits in either. The H1, deck and body keep Eastern-Arabic digits — that was not part of the request.
3. The 11 restaurant H2s: «الاسم — Latin:» → «الاسم (Latin):». Verified 11/11, 0 em dashes left in headings.
⚠ **The quick-list TABLE's name column still uses " — "** (11 cells, e.g. «تراباني — Trapani»). Only the
headings were requested; say the word and it's a one-line change to match.
Re-verified after: 11 cards all `/ar/places/`, 11 map pins, 1 table, 0 shortcode leak, no mojibake,
`index, follow`, the Delfino edit and the internal AR link both intact.

