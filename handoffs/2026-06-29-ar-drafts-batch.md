# Handoff — AR draft batch (5 guides) + standing guide-AR workflow documented (2026-06-29)

**Session:** Module 8 (Editorial / Guide). Author: Claude Blog.

## Standing workflow — now documented in the runbook (§1.5)
`guide-kit/GUIDE_AR_WORKFLOW.md` §1.5 captures the two cases + rules so next session
inherits them without re-deriving:
- **Case A — NEW guide:** Bader hands EN + AR MD + images → build BOTH (kit-publish EN,
  then AR twin). AR MD is Bader-authored human Arabic.
- **Case B — EXISTING EN guide:** EN already published → build AR twin ONLY (EN untouched).
- **D-145:** guide Arabic is always human-authored (Bader / AR blogger), NEVER MT for
  publication. The tool injects human Arabic; it never translates. MT is allowed ONLY as
  a draft scaffold for Bader to rewrite. (Listings use DeepL; guides never.)
- **Sequencing:** approved AR MD ready → Bader does WPML "+" (clean editable shell) →
  `populate_ar_twin.py` injects → fence noindex. NEVER "+" before the AR content exists.

## The batch — 5 MT *draft* AR MDs on Bader's Desktop (for rewrite → approve)
These are **machine-assisted drafts, NOT D-145-clean.** Bader rewrites each into Kuwaiti
Arabic and approves; the approved version is the human AR we inject (Case B for all five —
EN guides already live). Listing IDs confirmed from the live EN bodies / gd_place.

| Desktop file | AR for EN guide | Listing id (shortcode) | Notes |
|---|---|---|---|
| `~/Desktop/naranj_AR_draft.md` | 2251 naranj-salmiya | 2239 | clean kit-format source |
| `~/Desktop/south-avenue_AR_draft.md` | 2339 south-avenue-salon-sabah-al-salem | 2334 | clean kit-format source |
| `~/Desktop/mizumesa_AR_draft.md` | 2362 mizumesa-sharq | 2354 | clean kit-format source |
| `~/Desktop/vibes_AR_draft.md` | 2131 vibes-coffee-roastery-al-kout-mall | **1872** | pre-kit guide — see ⚠ |
| `~/Desktop/keif_AR_draft.md` | 2132 keif-restaurant-al-kout-mall | **1942** | pre-kit guide — see ⚠ |

Media to reuse on injection (no re-upload, text-only repo):
- naranj/south/mizu: hero + inline-1/2/3 from each EN guide (same as EN).
- vibes: hero=2123, inline-1=2125, inline-2=2126, inline-3=2124.
- keif:  hero=2127, inline-1=2128, inline-2=2129, inline-3=2130.

⚠ **keif/vibes divergences flagged in their draft headers (Bader to confirm):**
1. EN guides have **no `[q8tly_place]`/`[q8tly_map]` card** — I added them (ids 1872/1942)
   per the "include shortcodes" instruction. Keep on AR (and maybe backfill EN) or drop?
2. EN closing area link was the inconsistent `/en/areas/fahaheel/`; drafts use
   `/ar/places/fahaheel/`. Confirm the canonical Fahaheel archive path.
3. Both are older/shorter format (no "Know before you go" table / FAQ) — drafts mirror EN.

## Corpus status (all 6 guides)
- **anosha** — AR twin LIVE: `guide_article` 2600, publish+noindex, D-145 PASS, parked fenced.
- **naranj** — AR twin LIVE: `guide_article` **2612**, publish+noindex, Bader-authored Kuwaiti
  Arabic (`drafts/naranj-salmiya_AR_2026-06-29.md`) injected + verified (place-card →
  `/ar/places/السالمية/نارنج/`), parked fenced. (Approved AR came from `~/Downloads/naranj_AR_kuwaiti_clean.md`.)
- **mizumesa** — AR twin LIVE: `guide_article` **2618**, publish+noindex, Bader-authored
  Kuwaiti Arabic (`drafts/mizumesa-sharq_AR_2026-06-29.md`) injected + verified (place-card →
  `/ar/places/شرق/2405/`), parked fenced. (Approved AR from `~/Desktop/AR blogs /mizumesa_AR_kuwaiti_clean.md`.)
- **south-avenue / vibes / keif** — AR drafts staged on Desktop, awaiting Bader's rewrite →
  approval. No twins created (twin creation waits for approved AR + "+").

> Minor for Pipeline/Chrome: mizumesa's AR *listing* twin (2405) has a numeric slug, so the
> card link is `/ar/places/شرق/2405/` (vs naranj's `/ar/places/السالمية/نارنج/`). Listings-lane
> slug detail; the guide twin is correct.

## Next (per guide, once Bader approves its AR)
approved AR MD → Bader does "+" on the EN guide (editable WP-editor shell) →
`populate_ar_twin.py <approved.md> --en-id <EN> --media …=… --execute` → fenced noindex →
D-145 quality-gate check → parked (rides the site-wide flip; no per-guide unfence).
