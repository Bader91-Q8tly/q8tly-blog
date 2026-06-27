# Handoff — EN→AR guide workflow runbook (2026-06-28)

**Session:** Module 8 (Editorial / Guide). Author: Claude Blog.
**Task (from Advisor):** Define the EN→AR new-guide workflow, commit it as a
standing runbook, answer the classification question, flag held items. **No
content authored, no WPML writes** — definition + verification only.

## Deliverable
- **`guide-kit/GUIDE_AR_WORKFLOW.md`** — the standing AR-twin runbook. Quick-start
  at top; classification; 4 rails; verified gate state; EN/AR lifecycle (Phase
  A/B/C); WPML twin mechanism (rail-#1 proof); fallback + the held owner decision;
  `/ar/` routing + the `/ar/en/` trap; plain-body gotcha; flags to Advisor.
- Pointers wired so a cold start finds it first: **`CLAUDE.md`** (new AR section)
  and **`guide-kit/README.md`** (cross-link).
- Memory updated: `…/memory/guide-publishing-workflow.md` (AR pointer + the
  not-translatable blocker).

## Classification answer (Advisor's first question)
**"Blogs" = the existing guide/editorial system, NOT a new content type.** One
type only: the `guide_article` CPT (`/guide/{slug}/`); 6 live on staging. Role-brief
forbids `/blog/`. Existing rulings cover it (D-145 human translation, S2-19 WPML
gate). One correction to Advisor's rail #3: guides are the **`guide_article`
CPT**, not the WP `post` type — matters because WPML translatability is per post
type. The "not directory listings" intent of the rail is correct and kept.

## Key finding — verified live on staging over SSH (read-only), corrects stale docs
- **WPML 4.9.5 IS active on staging** (default `en`, active `ar,en`, directory
  negotiation; EN no-prefix, AR `/ar/` = HTTP 200). The 2026-06-20 handoff
  ("WPML not active on staging") and role-brief/calendar ("gated on WPML in
  production") are **stale on this point**.
- **Real blocker:** `guide_article` is **NOT set Translatable in WPML**
  (`guide_article_sync = NOT SET`; only `post`/`page` = `1`). `topic` taxonomy
  also not translatable. So the WPML "+" twin control does not appear on guides →
  no rail-#1-honoring way to make an AR twin yet. `anosha` 2189 has no WPML
  language record, confirming it.
- Calendar drift: `keif-restaurant-al-kout-mall` + `vibes-coffee-roastery-al-kout-mall`
  are live but not in the Published table.

## Flags routed to Advisor (also in runbook §9)
- **A (blocker):** set `guide_article` + `topic` Translatable in WPML — cross-module
  /global-state change; who/when? Nothing AR proceeds until done.
- **B:** reconcile S2-19's current meaning centrally (WPML *is* on staging now).
- **C:** confirm `[q8tly_place]`/`[q8tly_map]` emit `/ar/place/…` (not `/ar/en/…`)
  on AR pages — Module 2/Builder; verify on first twin.
- **D:** kit gap — `publish_guide.py` only creates; AR needs an update-only
  `--into <ar_id>` mode (never `wp post create` for AR).
- **E (HELD, owner's call):** AR-complete-to-launch vs EN-fallback-behind-fence —
  mapped to the WPML `guide_article` translation option (1 vs 2); slot marked.

## Not done (out of scope this pass)
- No blog content authored. No WPML writes. Did not flip `guide_article`
  translatable (cross-module — routed to Advisor). Did not edit the central
  Decision Log (single-sourced; reported up instead).

## Next session
- If Advisor clears flag A: dry-run the AR twin path on staging (fenced), convert
  the Anosha AR draft to plain-body format (§8), verify shortcode `/ar/` URLs (C).
