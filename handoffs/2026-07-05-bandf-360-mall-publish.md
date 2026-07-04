# Session handoff — B+F (360 Mall) guide published EN; AR twin staged, pending Bader's "+" (2026-07-05)

## What shipped

**EN guide LIVE: B+F → `guide_article` 2918** at `/guide/bandf-360-mall/` (staging).
Born straight on the D-168 neutral model via `publish_guide.py` (dry-run → execute).
Backup `staging-20260704-215916-guide-bandf-360-mall.sql.gz` logged. Verify green:
renders 200, house chrome, hero present, no double title, no raw shortcode. Topic
`food-drink`, term 1715.

**Verified against the two pipeline-live corrections (both applied):**
- **Price = $$$** — the source doc said `$$ · around 15 KD`; owner ruled $$$ after the
  doc was written and the listing is live at $$$. Guide key-facts renders
  **`$$$ · around 15 KD per person`** (KD figure unchanged). EN + AR both corrected.
- **Slug/district = Zahra** — place card resolves to **`/places/zahra/bf-360-mall/`**
  (listing **2664**), confirmed in the rendered HTML. `place_id=2664` in `[[place]]`.

**About paragraph — verbatim match confirmed.** Pulled the live listing 2664 About over
SSH before publishing; the guide About is word-for-word identical (EN), and the AR draft
matches listing twin 2730's About (AR). Ready for the Pipeline parity check.

**NEEDS-BADER kept OUT of guide prose (per the doc):** no Burger/Steakhouse/"Restaurant
inside Mall" labels; the mall-provided services are carried only as the
**"Via 360 Mall (not venue amenities): valet (paid) · WiFi · prayer rooms (men's &
women's)"** key-facts line. Named dishes limited to musakhan rolls + beef plates.

## Photos — pre-cropped landscape (the Odachi lesson), stronger set than the doc default

All 7 drop photos were **portrait** (3:4) — the guide template hard-crops inline photos to
a landscape box (~7:5 desktop / ~1:1 mobile; hero 16:9), so raw portraits would lose their
tops/bottoms (exactly the Odachi "weird pictures" problem). Pre-cropped each to the box,
centered on the subject. Uploaded: **hero 2914 + inline 2915/2916/2917.**

Inline set (a swap from the doc's default interior/court, within the offered swap pool):
- **inline-1 = musakhan rolls** (named dish #1) — "Musakhan rolls"
- **inline-2 = beef plate** (from `extra-2`, named dish #2 — brighter/more appetizing than
  the doc's dark interior shot) — "Beef plates"
- **inline-3 = Solar Garden terrace** (from `extra-1`) — "The terrace in the Solar Garden"
  (chosen over the doc's court shot, which featured a neighbouring brand — GODIVA —
  prominently; the terrace is brighter, cleaner, on-brief for "greenery / outdoor seating")

Hero = the bright B+F storefront-sign facade. Re-screenshotted mobile — every photo reads
whole and clean, no slicing. Kit `images/` folder holds the cropped landscape WebPs
(gitignored; the portrait originals were overwritten in place).

## AR twin — BUILT + injected (fenced) — Bader did the "+"; Blog populated

Bader clicked the WPML "+" on 2918 → clean editable WP-editor shell **2924** (lang `ar`,
trid 4805, empty body). Blog injected:
- **AR twin LIVE (fenced): `guide_article` 2924** at `/ar/guide/bandf-360-mall/`,
  **publish + noindex**. From `drafts/bandf-360-mall_AR_2026-07-05.md` via
  `populate_ar_twin.py --en-id 2918 --media hero=2914,inline-1=2915,inline-2=2916,inline-3=2917`
  (images reused, no re-upload). Backup `staging-20260704-223255-ar-twin-bandf-360-mall.sql.gz`.
- **Verify PASS:** Arabic title (Latin brand "B+F"); place-card → `/ar/places/الزهراء/bf-360-mall/`
  (twin 2730); no bare `/places/`; no `/ar/en/`; price `حوالي 15 د.ك` ($$$); noindex fence present.
- **Still open (D-145 while fenced):** AR brand-name kept Latin "B+F" (confirm); Blog-drafted
  AR captions (رولات مسخّن / أطباق لحم / جلسات السولار جاردن الخارجية + hero_alt) need his read.

### (original staging note, for the record)
Per `GUIDE_AR_WORKFLOW.md` sequencing the twin can't be created by Blog (rail #1 — only the
WPML "+" makes the linked twin). At EN-publish time trid 4805 had only the EN side (2918);
Bader then did the "+" and Blog populated (above).

- AR MD staged: **`drafts/bandf-360-mall_AR_2026-07-05.md`** — Bader's verbatim Kuwaiti AR
  from the source doc (matches listing twin 2730's About), neutral-model shape, price
  corrected to $$$, captions mirroring the EN set.
- **Bader's step:** open EN guide **2918** in wp-admin → Language box → click **"+"** next
  to العربية (WP-editor path). Then Blog runs
  `populate_ar_twin.py drafts/bandf-360-mall_AR_2026-07-05.md --en-id 2918 --media hero=2914,inline-1=2915,inline-2=2916,inline-3=2917 --execute`
  → injects + fences noindex (images reused, no re-upload).
- **Pending Bader at/before injection (D-145 quality gate, twin stays fenced regardless):**
  1. **AR brand name** — kept Latin "B+F" for the AR guide title (matches the AR prose,
     which writes the brand Latin; NEEDS-BADER flagged confirming the AR name stays Latin).
  2. **Staged AR captions + hero_alt are Blog-drafted** (رولات مسخّن / أطباق لحم /
     جلسات السولار جاردن الخارجية / the hero alt) — need his read.

## Tags (from the prompt's ruling) — LISTING lane, not the guide

The ruling (Burgers + Multi-Cuisine/International + romance→Date-Night) applies to the
`gd_place` listing tags (Pipeline), not the guide (guides carry an empty `guide_tag` by
design). Blog did not touch the listing. Noted for Pipeline's tag pass on 2664/2730.

## Repo state / next actions

- `guide-kit/guides/bandf-360-mall/` (article.md + source) + `drafts/…_AR_…md` +
  `guide-kit/runs/bandf-360-mall.md` committed; images gitignored.
- Calendar Published table + rotation updated; AR corpus note.
- **Next:** Bader → WPML "+" on 2918 (+ AR-name/captions call) → Blog populates AR twin →
  fence → report AR URL. Then Pipeline runs the guide↔listing parity check.
