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

---

## ✅ DONE — FIRST AR GUIDE TWIN IS LIVE (2026-06-29)

**Twin = `guide_article` 2600** (linked to EN 2189, `back_to_en=2189`).
`https://staging-…/ar/guide/anosha-beauty-salon-sabah-al-salem/` — **publish + noindex (fenced)**.

- **ATE blocker (§9-G) resolved in practice:** the shell was created as a real,
  editable WP draft (Bader's click via the WordPress-editor path), while the global
  `doc_translation_method` stayed **ATE** — so **listings keep DeepL untouched**.
  Exact per-document/per-type mechanism is Builder's to confirm so we can repeat it
  for the next guides (the global is still ATE, so each guide twin must be created
  the same editable way, or Builder defaults guide_article to the WP editor).
- **Populated by `guide-kit/populate_ar_twin.py`** (update-only, never `wp post create`;
  charset-safe `ensure_ascii=False`; reuses EN media; auto-discovers + hard-verifies
  the trid link before writing). Backup taken + logged first.
- **First-twin proof PASSED** (independent fetch): 0 raw `[q8tly_*]` shortcodes,
  Arabic title (zero mojibake), hero 2190 + inline 2192/2193/2194 present, noindex
  meta present, no double title. **Guide BODY: 4 `/ar/places/` links, 0 bare
  `/places/`** → Builder's shortcode fix v1.14.175 holds on real AR content. ✓
- **Meta:** deck, `primary_topic=1716` (neighborhoods), `rank_math_robots=[noindex]`,
  rank_math title/desc (AR), featured 2190, slug matches EN.

### ⚠ Flag to Chrome/Pipeline (NOT a guide-body issue)
The page has 153 bare `/places/` links — **all in the global mega-menu/footer chrome**
(e.g. `/places/category/kunafa|landmarks|towers/`): category archives whose AR *term*
isn't translated yet, so they fall back to EN under `/ar/`. That's the term-translation
backlog (D-161 / Chrome), outside Module 8. My guide body is clean.

### Still pending (unchanged)
Human review (D-145) → owner sign-off → unfence (flip `rank_math_robots` off noindex).
AR-public still behind the full gate (D-160 + owner track + D-157 cutover + 7-G).
naranj/south/mizu need human AR before they can be twinned.
