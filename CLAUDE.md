# Q8tly Blog — Claude working notes

This is the **Module 8 Editorial / Guide** workspace for Q8tly (bilingual EN/AR
curated Kuwait directory). You produce and publish **guides** — best-of lists,
area/district guides, and single-place spotlights.

## To publish a new guide: use the Guide Ingestion Kit

**Everything is automated through `guide-kit/`.** Don't hand-build it.

1. The new guide arrives as one folder: `guide-kit/guides/<slug>/` with
   `article.md` (frontmatter + PLAIN prose body) and an `images/` subfolder
   (`hero.*`, optional `og.*`, `inline-*.*`). See `guide-kit/guide.template.md`
   and the worked `guide-kit/guides/_example-anosha/`.
   - If Bader instead just gives content + photos + the listing it's about, build
     that folder yourself from the template, then run the kit.
2. Dry-run, then execute:
   ```bash
   python3 guide-kit/publish_guide.py guide-kit/guides/<slug>            # validate + preview
   python3 guide-kit/publish_guide.py guide-kit/guides/<slug> --execute  # publish
   ```
   The kit handles: validation, DB backup, image upload, `guide_article`
   creation, meta + topic, featured image, Page→guide 301, verify, and a per-run
   handoff in `guide-kit/runs/`.

Full contract + runbook + the publishing gotchas: **`guide-kit/README.md`**.

## To add a guide's Arabic (AR) twin: use the AR workflow runbook

**Read `guide-kit/GUIDE_AR_WORKFLOW.md` FIRST** whenever Bader hands over a new
guide or says "add Arabic." It is the standing EN→AR procedure: how the Arabic
twin is created **through WPML** (never by hand — that orphans `/ar/`), human
translation only (D-145), `/ar/` routing, the fenced→reviewed→unfenced lifecycle,
and the open flags. **Ground-truth note (verified 2026-06-28):** WPML 4.9.5 *is*
live on staging (EN no-prefix, AR `/ar/`), but `guide_article` is **not yet set
Translatable in WPML** — so AR twins are blocked on that one config flag (a
cross-module change to route to Advisor). See the runbook §3.

## Hard rules (the kit enforces these; you should too)

- **Guides are the `guide_article` CPT** at `/guide/{slug}/` (REST base
  `/wp/v2/guides`). **Never publish a guide as a Page**, never the dead
  `/wp/v2/guide_article` base.
- **Publish via WP-CLI over SSH** (`config.sh`) — the WordPress.com MCP can't
  create the CPT.
- **Body is plain prose + `[q8tly_place]` / `[q8tly_map]` only** — the template
  owns kicker/byline/hero/share/related (hand-built chrome double-renders).
- **`topic` (one of food-drink|neighborhoods|culture-heritage|seasonal), `deck`,
  and a hero image must be set**, or the template falls back.
- **Staging only; production (q8tly.com) is frozen.** **AR stays parked** until
  Bader says publish (same plain-body rule when it does).
- **Backup before any write** → log in `guide-kit/BACKUP_LOG.md`.
- **After wp-cli meta writes, touch the post** (`wp post update`) + flush, or the
  WordPress.com edge cache serves stale.

## Where things are

- `role/role-brief.md` — full scope + what to route to the Advisor.
- `guide-kit/` — the publishing kit (start here for any guide).
- `drafts/` — markdown drafts (EN + AR). `handoffs/` — session handoffs (write one
  each session). `calendar/editorial-calendar.md` — pipeline + weekly rotation.
- `assets/` — **(legacy, now empty)**. The repo is **text-only** (binary policy,
  2026-06-29): guide images do NOT live in git. They sit in a per-guide folder on
  the owner's desktop and the kit reads them from the local drop folder at publish
  time. Images are gitignored.

First guide shipped this way: Anosha Beauty Salon (`/guide/anosha-beauty-salon-sabah-al-salem/`, guide_article 2189). See `handoffs/2026-06-20-anosha-spotlight.md`.
