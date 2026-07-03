# Handoff — Anosha Beauty Salon neutral re-author, EN + AR (2026-07-01)

**Session:** Module 8 (Editorial / Guide). Author: Claude Blog.

## ✅ DONE — Anosha now matches the Mezo/Naranj neutral model (D-168 / D-145)

Same treatment as MizuMesa and Naranj this session, applied to the third
guide. Source content: Bader's `anosha-guide-EN-AR.md` intake drop (Project
Brief v2.4).

- **EN — guide_article 2189** (`/guide/anosha-beauty-salon-sabah-al-salem/`):
  body replaced via `reinject_en.py`. Old spotlight structure fully removed —
  H2 sections ("What stood out," "A small thing worth mentioning," "What
  Anosha offers" incl. the full 12-row service price menu, "Who it's for"),
  pull-quote, "Know before you go" table, FAQ, "Explore more" links. New
  body: neutral title ("Anosha Beauty Salon"), one About paragraph, 3 reused
  inline photos with short captions, a clean 6-row **Key facts** table,
  `[[place]]` only. `deck` cleared to `""`. `rank_math_description` set
  directly via SSH (was previously empty on 2189; script doesn't manage SEO
  meta).
- **AR — twin post 2600** (`/ar/guide/anosha-beauty-salon-sabah-al-salem/`,
  WPML trid 4656): repopulated via `populate_ar_twin.py` with matching
  Arabic. Stays `publish` + `noindex` (content-only update, fence unchanged).
  Proof re-ran clean: Arabic title renders, `[q8tly_place]` emits
  `/ar/places/…`, no EN leak, no `/ar/en/` double-prefix, single H1, noindex
  present.
- **Photos: untouched, all 4 reused** (hero 2190, inline 2192/2194/2193 — same
  order as the old live body) — no re-upload, no deletion. Captions shortened
  to the neutral vibe: "Outside Anosha Beauty Salon" / "Hair-wash lounge" /
  "Welcome coffee on arrival" / "The nail bar" (AR equivalents).
- **Drafts:** `drafts/anosha-beauty-salon-sabah-al-salem_EN_2026-07-01.md`,
  `..._AR_2026-07-01.md`. Original publish-time files
  (`_EN_2026-06-20.md`, `_AR_2026-06-20.md`, the D145-REVIEW note) left as
  historical record.
- **Verified live:** EN 200, single H1, all 4 captions present, zero raw
  shortcode literals, no leftover persuasive copy, no leftover price-menu
  rows. AR 200, single H1 "أنوشا", all 4 AR captions present, noindex meta
  present.

## Decision made with Bader this session
- **Price tier ($2 vs $$$):** intake flagged this as an open call ("did NOT
  pick — that's a call, not data"). Bader confirmed **keep `$$`**, matching
  what was already live on the guide/listing — no new claim asserted, just
  carried forward. Recorded in the Key Facts table as `$$`.

## Backup discipline
Pre-write snapshot taken manually before the EN reinject this time
(`staging-20260701-201848-guide-anosha-en-reinject-pre.sql.gz`), closing the
`reinject_en.py` gap flagged in last session's Naranj handoff. AR twin
populate took its own automatic pre-write snapshot as usual. Both logged in
`BACKUP_LOG.md`.

## Open items (out of Blog's lane — not touched here)
- **Listing About paragraph** at `/places/sabah-al-salem/anosha-beauty-salon/`
  — Pipeline/Builder scope per the intake's routing note, not a
  `guide_article` change. Not done here.
- **NEEDS BADER flags carried from the intake** (listing-data scope, not
  blocking the guide re-author done here): F1 hours (staff-stated,
  Friday/day-of-week unconfirmed — the new guide body sidesteps this by
  omitting the "daily/Friday" claim, just states the time range), F3 payment
  (resolved: not cash-only, KNET + cards), F6 area/governorate confirmation
  for the area-hub/pill, AR business name branding confirmation (أنوشا used
  as placeholder — note the AR twin's `hero_alt`/`hero_caption` metadata
  still carry the previously-published "أنوشة" spelling; only the new
  title/body prose use "أنوشا" per the intake — reconcile once branding is
  confirmed).
- **Full service/price menu** (12 rows: hair, nails, lashes, bridal, etc.)
  from the old EN draft — routed to the listing pipeline per the intake note
  ("Module 8 doesn't write listing data"), not reintroduced into the guide
  body.
