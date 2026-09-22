# → ADVISOR BRIEF — Blog (Module 8), 2026-08-13

**From:** Blog · **For:** Bader's discussion with the Advisor
**Shipped:** **Solange Maison** — EN `guide_article` **5430** + AR twin **5436**, both live on
prod, both verified. Listing: **Solange 4025**. Second fine-dining guide; **first fully-mirrored
EN/AR pair.** Also closed a corpus-wide Arabic SEO gap (see §C).

Blog needs **five rulings**. Everything else below is either already done or routed.

---

# A. DECISIONS NEEDED

### A1. The four-H2 EN/AR mirror — is it the house shape? *(blocks a Cure fix)*
Blog was told this rule was "established when Cure's English was restructured to match the
Arabic." **That restructure never happened.** Verified live:

| Guide | Body H2s | Captions |
|---|---|---|
| Cure EN (5025) | **none** | 3 figcaptions |
| Cure AR (5032) | **four** + معلومات سريعة | none |
| Solange Maison EN (5430) / AR (5436) | **four** + facts ✅ both sides | none ✅ |

So Solange complies and **Cure — the stated standard — does not.**
**Blog recommends:** ratify four-H2 + no-captions. Then Blog runs `reinject_en.py` on Cure EN —
one run, idempotency-diffed, same-day.

### A2. The D-168 register amendment *(outstanding since 2026-08-12, never ruled)*
Cure and Solange Maison are written in the owner-specified "friend who went" voice — who it
suits, when to go, an ordering steer, and **one honest drawback**. D-168's neutral model removed
exactly those. **The other nine guides are still neutral.** The corpus is split.
**Blog recommends:** ratify the friend-voice as house style, then schedule the other nine.
Either way this needs a Decision Log entry — it shouldn't keep drifting per-guide.

### A3. WPML `/ar/` fallback — the only item with live SEO consequences
A guide with **no AR twin** still serves **200** at `/ar/guide/<slug>/` with `<html lang="ar">`,
**`robots: index, follow`**, a self-canonical and an `hreflang` cluster declaring it the Arabic
version — **while the body is English.** Google can index English as canonical Arabic.

Currently closed for both guides that have twins, **but it recurs the moment any EN-first guide
publishes** — it was live on Solange Maison for the hours between the EN and AR runs.
**Not Blog-fixable** (WPML config, cross-module). Options: set `guide_article` to *only show
translated items* · noindex the untranslated `/ar/` fallback · gate EN publication on the twin.

### A4. AR SEO title convention — three patterns now in the corpus
- **8 twins** (all neutral-model, set today): «<Arabic name> <Latin name> | <Arabic descriptor>»
- **3 twins** never re-authored — Keif 2630, Vibes 2634, South Avenue 2619: «كيف، الكوت مول | Q8tly»

Blog left the three untouched rather than normalise without a ruling.
**Pick one and Blog aligns all eleven in one pass.**

### A5. H1 brand-name script — still inconsistent
`post_title` split: **Arabic (7)** أنوشا · نارنج · ميزوميسا · أوداتشي · كيف · فايبز · ساوث أفينيو —
**Latin (4)** B+F · Elysee · Cure · Solange Maison.
*(Correction on the record: Blog earlier told Bader Latin was "more consistent." That was wrong —
the majority is Arabic.)* No longer urgent for discovery, since the new SEO titles carry **both**
name forms, but it is an unresolved house-style question.

---

# B. ROUTED TO PIPELINE (listing 4025 + one standard)

Bader ruled canonical = **Solange Maison** (their branding: `solangemaison.com`, `@solange.maison`).

1. **Listing title is still "Solange"** → the place card on the live guide renders "Solange"
   under a guide titled "Solange Maison". **Visibly wrong right now — do this one first.**
2. **`amenities` = "Strong AC" only**; the intake pack claims **valet parking**. Not asserted in
   the guide. Reconcile.
3. **`price_kd_min`/`max` both NULL**; the pack says **15–19 KD/person**. Not asserted →
   **both** fine-dining guides now ship with a price band and no number.
4. **Category = `Fine Dining` only**, no `Restaurants` parent (Cure has both). Taxonomy gap?
5. **`smoking`, `website`, `established_year`** all null.
6. **AR listing `content` is still English** — amenities/payment *do* render Arabic, so this is
   **not** Cure's empty-field class, but an Arabic guide now sits above an English listing card.
7. **Listing is titled "Solange" on both language sides** → no Arabic name form listing-side
   either (same question as A5).

---

# C. CLOSED THIS SESSION — no action needed

- ✅ **Arabic corpus SEO gap.** All **8** neutral-model AR twins now carry a `rank_math_title` +
  `rank_math_description`. Previously **7 of 8 had a bare brand-name title and no description at
  all** while every EN guide had both — the whole Arabic half of the corpus was competing with no
  metadata. Descriptions are **Bader's own Arabic**, lifted verbatim from each twin's deck or first
  paragraph and cut at a sentence boundary (**D-145 clean — zero new authorship**). Titles were
  Bader-approved before writing. **H1s untouched**; old values logged for rollback.
  Snapshots `prod-20260813-213718` / `-220041`. *Correctly routed to Blog, not Builder —
  `guide_article` is Blog's CPT and Rank Math meta is post metadata, not plugin code.*
- ✅ **Kit env-label bug** — prod runs now write `prod-…` and log `| prod |`. No manual renames.
- ✅ **AR fence hardcode** — `populate_ar_twin.py` ships twins unfenced/indexable by default.

# D. STILL OWED, BLOG CAN DO IT (no ruling required)

- **`alt` text — live defect.** `publish_guide.py:285` does `alt = cap or fm["title"]`; under the
  no-captions shape every inline image gets `alt="<title>"` — on Solange Maison EN+AR and Cure AR.
  Needs an alt field on the marker across all three tools, then a reinject. Blog did **not**
  hand-patch the live bodies (a reinject would revert it). **Blog's priority fix.**
- **`populate_ar_twin.py` is silent about missing SEO meta** — it writes `seo_title`/
  `meta_description` only if the draft supplies them and otherwise ships a bare twin. That is
  exactly how seven twins went out. Should warn or refuse.

# E. D-180 AMENDMENTS OWED

- **`sips -g` lies on HEIC orientation** *(reported 2026-08-12, unruled)*. §0's screening
  one-liner reads *stored* dims, so `Orientation=1` files pass as landscape then render
  **sideways**. Must be orientation-aware (`PIL.ImageOps.exif_transpose`).
- **NEW — photo-retention rule.** Solange Maison's **originals no longer exist**; only a 1600px
  optimized set survived. All 16 sources were portrait at 1600px → landscape-crop width 1600,
  clearing the 1520 bar by **5% with no headroom**, and **every photo in the guide is a portrait
  rescue**. Cure had native landscape at 4032–5712px. **If the optimize step discards originals,
  guides inherit a hard 1600px ceiling and lose any ability to re-frame.** Keep originals until
  the guide ships.

# F. PROCESS NOTES

- **The WPML "+" is a dead end — stop asking Bader to press it.** It opens an **ATE cloud job**
  (`editor='ate'`, `translated=0`) plus a NULL-element placeholder; **no WordPress post is
  created.** Confirmed twice (Cure, Solange Maison). The twin is created via
  **`$sitepress->set_element_language_details()`** — note that
  `do_action('wpml_set_element_language_details')` is a **silent no-op** that leaves the post
  registered as EN on its own trid. Full recipe: `handoffs/2026-08-12-cure-shuwaikh-guide-built.md`.
- **WPML housekeeping, not Blog's:** four orphaned `icl_translation_status` rows predating this
  work — rids 458/459/461/462 → translation_ids 2775/2777/2779/2781, which no longer exist in
  `icl_translations`. Neither twin build produced them (rids 983 and 1126 are correctly pointed).

---

### Shortest path for Blog
**A1** → Cure EN restructured same-day · **A3** → the SEO bleed stops · **A4** → eleven titles
aligned in one pass · **B1** → the visible name mismatch goes away.
