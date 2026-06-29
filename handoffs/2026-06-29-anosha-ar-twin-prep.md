# Handoff — Anosha AR twin: unblocked, prepped, awaiting the WPML "+" (2026-06-29)

**Session:** Module 8 (Editorial / Guide). Author: Claude Blog.

## Context
Advisor green-lit AR twins: Builder's WPML flip is live and Builder's shortcode
fix shipped (v1.14.175 — `[q8tly_place]`/`[q8tly_map]` now resolve to the page's
language, emitting `/ar/places/…` on AR pages with EN-fallback). Pre-twin
duplicate-surface risk closed. Build human-translated (D-145), noindex-fenced.

## ✅ Done this session
- **Flip re-verified over SSH (ground truth):** `guide_article`, `topic`, `guide_tag`
  all **Translatable = 1 ("only show translated")**; `post` = 1 (sanity). The "+"
  twin button now renders on guides. Note: guide_article is already at the Option-A
  display value.
- **Anosha AR draft converted + staged:** `drafts/anosha-beauty-salon-sabah-al-salem_AR_2026-06-29.md`
  — runbook §8 chrome→plain conversion of the 2026-06-20 human AR (D-145; prose
  reused verbatim, NOT machine-translated). Verified to mirror live EN 2189 (price
  tables match exactly). Plain body + `[[image]]`/`[[place]]`/`[[map]]` markers +
  `/ar/places/…` links. Old HTML-chrome draft marked SUPERSEDED.
- **Repo binary policy enforced:** text-only `.gitignore` for images; cleared
  dangling drop/run audit-trail debt (naranj/south/mizu article.md, runs/,
  CHARSET, BACKUP_LOG). Commits `8d165ae`, `be7510d`, `1c8c576`, `c4b3e3f`.
- **Docs reconciled to canon:** flip live + S2-19 (necessary-but-not-sufficient;
  AR-public = D-160 + owner track + D-157 cutover + 7-G) across runbook, role-brief,
  README, calendar.

## ⛔ OPEN — the one step Blog can't do via SSH
**Twin SHELL creation = WPML "+" in wp-admin (rail #1).** Cannot be clicked over
SSH/CLI, and `wp post create` for AR is forbidden (orphans `/ar/`). Needs either:
- **(A, recommended)** Bader clicks WPML "+" → العربية on EN guide 2189 in wp-admin
  to create the linked AR shell; then Blog populates over SSH (reuse media
  2192/2193/2194 + EN hero; `[q8tly_place id="2147"]`/`[q8tly_map ids="2147"]`),
  fences noindex, and **verifies the place-card emits `/ar/places/…` on the real
  twin** (Advisor's first-twin check). Arabic body/meta via wp-admin paste or a
  charset-safe SSH path (NOT the kit's python→PHP meta writer — CHARSET mojibake).
- **(B)** Explicit Advisor/owner blessing to create+link the shell via WPML's API
  over SSH (`wpml_set_element_language_details`) — deviates from "creation = UI
  only," so not done without sign-off.

## Next
Get the shell created (A or B) → populate → fence → verify `/ar/places/…` →
human review (D-145) → owner sign-off → unfence. AR-public still behind the full
gate (D-160 + owner track + D-157 cutover + 7-G). Then repeat for naranj/south/mizu
(those need human AR first — only Anosha has a human translation today).
