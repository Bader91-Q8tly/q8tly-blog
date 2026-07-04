# Session handoff — Odachi published (born-neutral); AR twin staged, pending Bader's "+" (2026-07-04)

## What shipped

**EN guide LIVE: Odachi → `guide_article` 2800** at `/guide/odachi-kuwait-city/`
(staging). Published via `publish_guide.py` (dry-run → execute), backup
`staging-20260704-183756-guide-odachi-kuwait-city.sql.gz` logged. Verify green:
renders 200, house chrome, hero present, no double title, no raw shortcode,
place card resolves to `/places/kuwait-city/odachi/` (listing **2432**, the slug
the intake predicted). Topic `food-drink`, term 1715 assigned.

**Firsts worth knowing:**
- **First guide born on the D-168 neutral model** — published straight through
  `publish_guide.py` with the neutral body (Bader-locked About verbatim + 3
  captioned photos + 6-row key-facts table + `[[place]]`; no `[[map]]`, no FAQ,
  no sections). No spotlight-era body ever existed, so no `reinject_en.py` pass
  will be needed.
- **First WebP image set.** Bader pre-optimized the photos
  (`…/Odashi /optimized/`, WebP ~15–37% lighter than the JPEGs) and staged them
  into the kit slots himself; verified byte-identical to the optimizer output
  before publish. Uploaded: hero **2796** ("Outside Odachi") + inline
  **2797/2798/2799** ("Fried shrimp and a salad" / "One of the seating areas" /
  "A noodle dish"). `extra-1..3.webp` stay local (kit skips unreferenced stems)
  — available to the listing lane. Note: og:image is now a `.webp` (hero
  fallback); fine for FB/Twitter cards, worth a glance if WhatsApp previews ever
  look blank — not flagged as a defect.
- `deck` note: `publish_guide.py` hard-requires a non-empty deck, so 2800 has a
  factual one-liner deck (restates locked-About facts only) — the re-authored
  neutral guides (2362/2251) currently carry empty deck meta. Cosmetic
  divergence, template shows deck under title; flag if house style settles on
  empty.

## AR twin — staged, NOT built (waiting on Bader's "+")

Per `GUIDE_AR_WORKFLOW.md` sequencing (approved AR MD ready → **"+"** → inject →
fence), the twin is deliberately not created yet:

- AR MD staged: **`drafts/odachi-kuwait-city_AR_2026-07-04.md`** — Bader's
  hand-written Kuwaiti AR from the intake, verbatim (D-145-clean), converted to
  the kit's plain-body + markers format, neutral-model shape mirroring EN.
- **Bader's step (cued to him this session):** open EN guide **2800** in
  wp-admin → Language box → click **"+"** next to العربية (WP-editor path, as
  with the six existing twins). Then Blog runs `populate_ar_twin.py` to inject +
  fence noindex.
- **Two calls for Bader at/before injection:**
  1. **One-word twin mismatch (from the intake's own flag):** AR says
     **"هادي"** (quiet), locked EN About says **"cozy"**. Keep as-is, or swap AR
     to "مريح" — his call as author; the draft carries هادي verbatim.
  2. **Staged AR captions + hero_alt are Blog-drafted, not Bader-authored**
     (روبيان مقلي مع سلطة / إحدى الجلسات / طبق نودلز / أوداتشي من الخارج) —
     need his read, same D-145 checklist treatment as the other twins.

## Listing-lane flags (Pipeline's, not ours — from the intake's NEEDS-BADER)

Coordinates missing (stored pin/Directions), phone +965 9333 4444 WhatsApp?,
menu URL is a third-party QR link (may rot), `Sushi` tag to verify from the
menu before shipping. Listing 2432 is live; these ride the Pipeline lane.

## Repo state

- `guide-kit/guides/odachi-kuwait-city/` — `article.md` + `source-…-EN-AR.md`
  committed; images gitignored (text-only policy; WebP set lives in the desktop
  drop folder + kit folder locally).
- `calendar/editorial-calendar.md` — rotation table updated (Odachi newest →
  auto-featured), Published entry + table row added, AR-corpus note now "6 of 7".
- Kit run handoff: `guide-kit/runs/odachi-kuwait-city.md`.

## Next actions

1. **Bader:** the WPML "+" on 2800 (and rule on هادي/cozy + the AR captions).
2. **Blog (next session):** `populate_ar_twin.py` inject → fence noindex →
   D-145 checklist → calendar AR column.
3. Unchanged: neutral re-authors for south-avenue (2339), keif (2132), vibes
   (2131) still gated on their approved MDs.
