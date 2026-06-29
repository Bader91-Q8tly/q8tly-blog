# Briefing → Advisor — Blog (Module 8) lane status + AR guide blocker (2026-06-29)

**From:** Claude Blog (Module 8 — Editorial / Guide). **To:** Advisor (new session, cold start).
**TL;DR:** EN guides ship fine and 6 are live on staging. **AR guide twins are
parked, blocked on one config flip that Builder is doing right now**
(`guide_article` + `topic` → WPML-Translatable). Once Builder confirms the flip,
I can create the AR twins (human-translated, fenced). Nothing else is in my way
technically. A few decisions below are yours.

---

## 1. Who I am / what this lane owns
- I produce and publish **guides** — best-of lists, area/district guides, single-place
  spotlights. They are the **`guide_article` CPT** at `/guide/{slug}/` (REST base
  `/wp/v2/guides`), **not** Pages and **not** directory listings.
- Everything ships through the repo's **Guide Ingestion Kit** (`guide-kit/`,
  `publish_guide.py`): validation → DB backup → image upload → CPT create →
  meta/topic/hero → 301 → verify → per-run handoff. Publish is **WP-CLI over SSH**
  (the WordPress.com MCP can't create the CPT). Staging only; **production is frozen**.
- Standing AR procedure lives in **`guide-kit/GUIDE_AR_WORKFLOW.md`** (verified
  against live staging 2026-06-28). New §3.5 there is the cross-lane mechanism map.

## 2. EN status — healthy, not blocked
6 guides live on staging: `anosha-beauty-salon-sabah-al-salem`, `naranj-salmiya`,
`south-avenue-salon-sabah-al-salem`, `mizumesa-sharq`, `keif-restaurant-al-kout-mall`,
`vibes-coffee-roastery-al-kout-mall`. EN is fully supported and repeatable today.

## 3. The AR blocker — what I'm waiting on (Builder)
- **What's blocked:** the Arabic twin of any guide. AR guides use **mechanism A
  (a twin page created by WPML)** — but **only after `guide_article` (and the
  `topic` taxonomy) are set Translatable in WPML.**
- **Current state (verified over SSH 2026-06-28):** WPML 4.9.5 *is* live on staging
  (EN no-prefix default, AR under `/ar/`, `/ar/` = HTTP 200), **but
  `guide_article_sync = NOT SET` and `topic` = NOT SET.** With those unset, the
  WPML "+ add translation" button does **not** appear on guides — there is no
  sanctioned way to create an AR twin.
- **What Builder is doing now:** flipping `guide_article` + `topic` → Translatable
  (WPML → Post Types Translation / Taxonomies Translation; properly via
  `wpml-config.xml`). This is a global-site/cross-module change, which is why it's
  Builder's, not mine.
- **Important nuance:** Builder is **not translating** the guides — Builder is
  *enabling the mechanism*. The Arabic copy itself is **human translation (D-145)**
  and stays in my lane. So I am waiting on Builder for the *config flip*, then I do
  the *content*.

## 4. What I do the moment the flip lands
1. Re-verify the WPML state over SSH (settings drift — runbook rule).
2. Stage the human Arabic per guide in the kit's plain-body + marker format
   (no DeepL, no listings controlled-term machinery — guides aren't listings).
3. Create each twin **through WPML's "+"** on the EN post (never `wp post create`
   an AR guide, never write `icl_translations`/`trid` by hand — that orphans `/ar/`).
4. Keep every twin **fenced (noindex/draft)** until human review → **owner sign-off**.

## 5. Mechanism map (so guides aren't confused with other AR surfaces)
Only **listings** and **(later) guides** become twin pages. Everything else is
strings or terms — **never a second page**:
- Search page + GD template pages → **String Translation** (routing, no twin).
- Filter labels / UI chrome → **String Translation**.
- Category / taxonomy archives → **translated term** (Pipeline's D-161 mapping), no twin.
- Guides → **twin via WPML**, human-translated (blocked until the flip).

## 6. Decisions / flags I'm routing to you (Advisor)
- **A — Confirm the flip scope.** Builder must set **both** `guide_article` **and**
  the `topic` taxonomy Translatable. `topic` alone or `post`/`page` alone does
  nothing for guides. Please confirm Builder's change covers both, and ping me when
  it's live so I can verify + proceed.
- **B — Reconcile S2-19's exact meaning.** Older repo docs (role-brief, calendar,
  Anosha handoff) say "WPML not active on staging / gated on WPML in production."
  Reality: WPML is live on staging. Is the public gate "WPML on prod" only, or also
  "guide_article made translatable," or "+ human review + owner unfence"? I've
  written the runbook to ground truth and flagged, not silently rewritten, decision IDs.
- **C — Held owner decision (needs a ruling).** For an `/ar/` guide whose twin isn't
  done yet: **Option A** = "only show translated" (AR-complete gates launch; nothing
  EN leaks under `/ar/`) vs **Option B** = EN-fallback under `/ar/` kept noindex.
  This maps directly to one WPML setting on `guide_article`. Safe default until ruled
  = Option A. Record in the Decision Log.
- **D — Route to Builder/Module 2.** Confirm the body shortcodes `[q8tly_place]` /
  `[q8tly_map]` emit **`/ar/place/…`** on AR pages (not `/place/…`, not malformed
  `/ar/en/…`). I'll verify on the first real AR twin and report any malformation.

## 7. Net: my ask
**Ping me when Builder's flip is live** (both `guide_article` + `topic` Translatable).
That's the one thing gating me. Everything downstream (staging the human Arabic,
creating fenced twins) is ready to go on my side. Public launch stays behind the
prod/WPML + owner-sign-off gate, separate from the staging technical gate.

---

## UPDATE (2026-06-29, later) — Advisor replied: UNBLOCKED, twins on HOLD

Advisor confirmed Builder's flip is **live and verified**: `guide_article`, `topic`,
and `guide_tag` all set Translatable (`guide_tag` included proactively so tags never
need a second flip). The WPML "+ add translation" button now renders on guides.
D-145 guard intact (Translate-Everything OFF, 0 twins, 0 DeepL jobs — mechanism
enabled, not MT-enrolled). **The mechanism is mine; human Arabic per D-145.**

Resolution of my four asks:
1. **Flip scope — CONFIRMED** (`guide_article` + `topic` + `guide_tag`, live). The
   one thing that was gating me. ✅
2. **Shortcode AR-URL emission — routed to Builder as a read-only check.** **HOLD
   building twins** until Advisor relays Builder's finding. We check the emitter
   *before* building so we don't make N twins against a broken URL builder.
3. **Display-mode (A vs B) — ratified value incoming**, leaning **Option A**
   (only-show-translated, per D-160 AR-perfect). It's a **global WPML setting** set
   at **project level** (Bader/Builder), **not by me, not per-guide.** Doesn't block
   twin creation — only fallback behavior. Build twins noindex-fenced meanwhile.
4. **S2-19 — reconciled to canon.** Public gate is **not** "WPML on prod" alone;
   WPML-on-prod is **necessary-but-not-sufficient** (also AR-perfect D-160 + owner
   track + D-157 cutover + 7-G flip). My lane's wording was **pre-D-160 drift
   (incomplete), not a direct contradiction.** Patched role-brief, README, calendar,
   runbook §3/§6/§9. Residual flag back to Advisor: I hold no S2-19 *source text*,
   only the paraphrase — if the central spec literally says WPML-on-prod is the
   whole gate, that contradicts D-160 and needs a central patch.

**My state now:** EN healthy/untouched. AR mechanism unblocked. **Building nothing
on AR twins until the shortcode check returns.** Docs reconciled; handoffs committed.
