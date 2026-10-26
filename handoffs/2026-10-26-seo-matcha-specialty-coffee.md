# Handoff — 26 Oct 2026 — SEO pairs: matcha + specialty coffee (drafts only)

**Brief:** Advisor's `~/Downloads/SEO_KEYWORDS_BLOGGER_BRIEF_2026-10-16.md` §3 (matcha) and §1 (specialty coffee / V60).
**State: READY TO POST** (owner 04:28 "finish it" done). Four final articles, both heroes ready, SEO fields filled, twin mapping in each guide's `POSTING.md`. **Nothing created on q8tly.com**
(plugin release in flight; the Advisor gives the window, then WPML-twinned drafts → owner review → publish on his word).

## Files (final)
- EN matcha → `guide-kit/guides/where-to-get-matcha-in-kuwait/article.md` · AR → `drafts/where-to-get-matcha-in-kuwait_AR_2026-10-26.md`
- EN coffee → `guide-kit/guides/specialty-coffee-kuwait/article.md` · AR → `drafts/specialty-coffee-kuwait_AR_2026-10-26.md`
  (EN files moved from `drafts/` into the kit drop folders; the kit needs `article.md` starting with `---`.)
- Posting runbooks + SEO + WPML mapping: `guide-kit/guides/<slug>/POSTING.md` (both slugs).
- Heroes (gitignored, local): `guide-kit/guides/<slug>/images/hero.jpg`, both 1520×1086, EXIF-clean.
- Mock-ups (approved 26 Oct 04:08): `drafts/matcha_MOCKUP_AR-EN_2026-10-26.md`, `drafts/specialty-coffee_MOCKUP_EN-AR_2026-10-26.md`
- Owner preview page (private, mock-up stage): https://claude.ai/artifact/QB5VYEJLVKhgbXMXFJZJq3

## Sourcing
- Places from the public catalogue only (`/wp-json/geodir/v2/places?lang=en|ar`, 5 s apart), read 26 Oct; EN/AR paired by slug.
- Matcha: 25 tagged → **19** after the owner's 03:41 cuts (Nouga, Kohi: tag without text; Costa, Kanemochi, Ever, Lean).
- Coffee: 53 in Specialty Coffee (EN 1500 / AR 2030) → **50** (three Coffee Bean & Tea Leaf branches cut, mock-up recommendation approved).
- Every place sentence is from the listing's own text. V60-tagged listings whose text doesn't say V60 are described as "tagged V60 on Q8tly".
- **Limu (Shuwaikh):** polled 04:29, EN `/places/shuwaikh/limu-shuwaikh/` (7740) + AR `/ar/places/الشويخ/limu-shuwaikh/` (7741) both 200 on try 1 → added to Shuwaikh in both coffee articles; count 50 → **51**.

## Heroes
- Matcha: Matcha Matcha Abu Halifa gallery photo `matcha-matcha-abu-halifa-08.jpg` (media 1115), 7:5 crop (0,499)-(1920,1870) →
  `guide-kit/guides/where-to-get-matcha-in-kuwait/images/hero.jpg`, 1520×1086, EXIF-clean (gitignored, local only).
  No q8tly.com photo fully met "landscape ≥1520 with matcha in frame"; #1 chosen with the Advisor's lean.
- Coffee: KODO Roastery `IMG_2315.HEIC` (night). Person behind the glass **blurred on a local copy** (owner's pass given 04:28, D-254); original untouched (sha256 7b18b166…fb15d). Hero sha256 aece89db…99c2a4.

## Open flags (route via Advisor)
- Abu Halifa AR listing URLs carry a space in the area slug (`/ar/places/أبو حليفة/…`); they resolve (200), hyphen form 301s to them. Articles link the `%20` form.
- Photo manifest maps folder `Matcha mahboula` to Matcha Matcha **Salmiya** (1831); the folder's own notes say **Abu Halifa** (2669).
- No live listing says it sells matcha powder or V60 equipment → powder section is buying advice only; equipment keywords not targeted.

## ✅ DRAFTS ON q8tly.com (26 Oct, 04:44–04:51 Kuwait) — awaiting the owner's read + publish word
| Guide | EN | AR | trid | hero att |
|---|---|---|---|---|
| matcha | 7753 | 7755 | 7169 | 7752 |
| specialty coffee | 7760 | 7762 | 7172 | 7759 |
- ⚠ The Advisor's "Pipeline idle" did not hold at 04:35: `/tmp/q8tly-publish.lock` was held by the Pipeline's live run (pid 45348, P-398 Tampopo). Waited for its release, took the lock 04:38:44, released 04:51:29.
- Link recheck: 34 pages crawled 200 (slow, ~15 s/page uncached) + all 114 listing links matched against a fresh catalogue read (600 published) + the 6 tag/category/flagship pages 200.
- Heroes re-cut to 16:9 1600×900 (template frame) before upload; details in each POSTING.md.
- To publish (owner's word only): `wp post update <id> --post_status=publish` for EN then AR, touch + Rocket flush, then check `/ar/places/` links render on the AR pages and both URLs 200.
