# D-145 Human Review Checklist — Anosha AR twin (`guide_article` 2600)

> **Purpose: QUALITY GATE, not go-live.** Confirm the human Arabic renders right.
> **2600 stays `noindex` regardless of the outcome** — per Bader (2026-06-29), we do
> NOT unfence individual guides ahead of the **site-wide AR-public flip** (D-160 +
> owner track + D-157 cutover + 7-G). This twin rides that flip with everything else.
> A "pass" here means *the Arabic is correct and ready*, not *publish it now*.

- **Review on the live fenced page (RTL):** https://staging-e1ff-baderlol44-pwgjm.wpcomstaging.com/ar/guide/anosha-beauty-salon-sabah-al-salem/
- **Compare against EN source:** `/guide/anosha-beauty-salon-sabah-al-salem/` (guide_article 2189)
- **AR source of prose:** human translation `drafts/…_AR_2026-06-20.md` (reused verbatim; the
  2026-06-29 file is its plain-body conversion). **No machine translation was used.**
- Reviewer: **Bader** · Date: **2026-06-29** · Outcome: **☑ APPROVED — PASS** (Arabic reads clean & clear on the fenced page; content gate cleared).
  - Owner decisions resolved: **#1 "Best for" → kept as prose** · **#2 deck → kept (reused kicker)** (content accepted as rendered).
  - **Stays `noindex`.** D-145 = quality gate, not go-live; 2600 rides the site-wide flip (D-160 + owner track + D-157 cutover + 7-G). `rank_math_robots` NOT flipped.

---

## A. Section-by-section fidelity (EN 2189 → AR 2600)

| EN section | AR section (rendered) | Present? | Reads right? | Notes |
|---|---|---|---|---|
| (intro, 2 paras) | (intro, 2 paras) | ☐ | ☐ | links: الصالونات → /ar/places/category/salons/, صباح السالم → /ar/places/sabah-al-salem/ |
| What stood out | ما الذي لفت الانتباه | ☐ | ☐ | incl. review quote «صراحة شيء رائع…» |
| A small thing worth mentioning | تفصيلة تستحق الذكر | ☐ | ☐ | prayer-space hospitality |
| What Anosha offers | ماذا يقدّم أنوشة | ☐ | ☐ | intro line + the 4 tables below |
| · Hair | · الشعر | ☐ | ☐ | 8 rows — numbers match EN |
| · Nails | · الأظافر | ☐ | ☐ | 5 rows — numbers match EN |
| · Lashes, brows & more | · رموش وحواجب وأكثر | ☐ | ☐ | 5 rows |
| · Occasions & bridal | · المناسبات والعرائس | ☐ | ☐ | 3 rows (incl. VIP 650) |
| Who it's for | لمن يناسب | ☐ | ☐ | **DECISION #1 below** (EN has a "Best for" bullet list; AR is prose only) |
| Know before you go | قبل أن تذهبي | ☐ | ☐ | area, hours (daily incl. Fri), phone, IG, $$, payment, women-only/AC/parking |
| FAQ (7 Q) | أسئلة شائعة (7 Q) | ☐ | ☐ | all 7 questions + answers |

> The listing **card** (`[q8tly_place]`) and **map** (`[q8tly_map]`) render between
> "لمن يناسب" and "قبل أن تذهبي" / after it — confirm the card shows the **Arabic**
> name + district and its link is `/ar/places/…`.

## B. Language quality (the core of D-145)
- ☐ Natural Arabic, not stilted/MT-sounding; tone matches the EN's calm/editorial voice.
- ☐ Spelling, grammar, diacritics correct.
- ☐ Service/term names read correctly (سشوار روسي, جل بوليش, إكستنشن, etc.).
- ☐ No untranslated English left in the body; no AR claim that contradicts EN facts.

## C. Rendering / RTL / layout
- ☐ Page is RTL; text alignment + punctuation direction correct.
- ☐ Tables render cleanly RTL (headers الخدمة / تبدأ من; columns aligned).
- ☐ 3 inline images show with correct **Arabic captions**; hero shows; alt text sensible.
- ☐ Review blockquote renders.
- ☐ No broken markup, no leftover `[[ ]]` markers, no raw `[q8tly_*]` (auto-check: 0 ✓), no mojibake (auto-check: clean ✓).

## D. Body links & facts (body only — chrome is out of scope)
- ☐ الصالونات → `/ar/places/category/salons/` (resolves).
- ☐ صباح السالم → `/ar/places/sabah-al-salem/` (resolves).
- ☐ Card/map link to `/ar/places/…` (auto-check: body = 4 `/ar/places/`, 0 EN-leak ✓).
- ☐ Phone `+965 6566 5028`, Instagram `@anosha_salon` correct.
- ☐ Hours/payment/area/"women-only" match the listing — no overclaims.
- ⓘ The mega-menu/footer `/places/` (non-`/ar`) links are **chrome term-backlog (Pipeline/Chrome)**, NOT this guide — ignore for D-145.

## E. SEO/meta (rendered)
- ☐ AR `<title>`: «صالون أنوشة صباح السالم | شعر وأظافر ورموش» reads right.
- ☐ Meta description (AR) reads right.
- ☐ `noindex` present (fence) — **must stay on; do not unfence.**

---

## Owner decisions (need a human Arabic call — I will NOT auto-write Arabic, D-145)
1. **"Best for" list.** EN "Who it's for" ends with a 4-bullet "Best for" list; the AR
   renders the human translation as **prose only** (no bullet list). Keep prose, or add
   an AR bullet list? (If add → please provide the Arabic bullets; I'll place them.)
2. **Deck.** AR `deck` currently reuses the old kicker line
   «نظرة مباشرة على صالون في صباح السالم يتقن التفاصيل الصغيرة». Keep, or replace with
   a different AR deck? (Provide the Arabic if replacing.)

## How edits get applied (if any)
Give me the corrected Arabic (inline or marked-up), and I re-run `populate_ar_twin.py`
against 2600 (update-only, backup-first, charset-safe, re-fences noindex). It stays
`noindex` after — unfencing only happens at the site-wide flip.
