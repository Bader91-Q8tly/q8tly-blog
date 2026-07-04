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

## AR twin — BUILT + injected (fenced) — later same session

Bader made the WPML "+" on 2800; the shell came up as a **clean editable
WP-editor draft** (post **2808**, lang `ar`, trid 4743, empty body, title "a") —
the right state, not an ATE-only slot. Blog then injected:

- **AR twin LIVE (fenced): `guide_article` 2808** at
  `/ar/guide/odachi-kuwait-city/`, **publish + noindex**. Injected from
  `drafts/odachi-kuwait-city_AR_2026-07-04.md` (Bader's verbatim Kuwaiti AR) via
  `populate_ar_twin.py --en-id 2800 --media hero=2796,inline-1=2797,inline-2=2798,inline-3=2799`
  (images **reused**, no re-upload). Backup
  `staging-20260704-190246-ar-twin-odachi-kuwait-city.sql.gz` logged.
- **Verify PASS:** Arabic title no mojibake; place-card →
  `/ar/places/مدينة-الكويت/odachi/` (AR-prefixed, listing 2432); no bare
  `/places/` (no EN-under-AR); no `/ar/en/` double-prefix; noindex fence
  present. (The one bare `/places/category/casual-dining/` in the page is the
  global mega-menu chrome = untranslated category term, the known Pipeline/
  Chrome backlog item — NOT the guide body.)

**Still open — D-145 review while fenced (same track every twin rides):**
  1. **One-word twin mismatch:** AR says **"هادي"** (quiet), locked EN About
     says **"cozy"**. Injected верbatim as هادي (Bader's own intake word); his
     call whether to leave it or move EN/AR into agreement.
  2. **Staged AR captions + hero_alt are Blog-drafted, not Bader-authored**
     (روبيان مقلي مع سلطة / إحدى الجلسات / طبق نودلز / أوداتشي من الخارج) —
     need his D-145 read, same as the other twins' checklists.
  The twin stays noindex-fenced regardless; the D-145 review is a quality gate,
  not a go-live (rail #4). Unfences with the whole corpus at the site-wide flip.

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

1. **Bader (quality gate, not blocking):** D-145 read of the AR twin 2808 while
   fenced — rule on هادي vs cozy, and approve/adjust the 4 Blog-drafted AR
   captions/hero_alt. Twin stays noindex either way.
2. Unchanged: neutral re-authors for south-avenue (2339), keif (2132), vibes
   (2131) still gated on their approved MDs.

**Corpus status after this session:** 7 EN guides live; **7 of 7 AR twins built
+ fenced** (odachi 2808 joins anosha 2600, naranj 2612, mizumesa 2618, keif
2630, vibes 2634, south-avenue 2619). All ride the site-wide AR-public flip
together.

---

## Follow-up (same session): photo re-crop + Sushi tag verified

**Problem Bader flagged:** the guide photos "looked weird — only part of the
shrimp / noodles showed." **Root cause (confirmed by measuring the live render):**
the guide-single template **center-crops inline photos to a fixed landscape box**
(~1.4:1 / 7:5 on desktop, ~1:1 on mobile; the hero is 16:9), with
`object-fit: cover`. The drop photos were all **tall portrait phone shots**, so
their tops/bottoms got guillotined — the shrimp bowl and noodle bowl lost their
bottoms.

**Fix (all in Blog's lane — no Builder dependency):** pre-cropped each photo to
the template's box, centered on the subject, so nothing important is sliced:
- **Hero** swapped from the dark glass-reflection shot to the **bright storefront
  sign** photo (01.03.55), cropped 16:9.
- **inline-1 (shrimp)** cropped 7:5 to the shrimp plate alone — the cluttering
  second salad bowl is now out of frame, so the caption changed
  **"Fried shrimp and a salad" → "Fried shrimp"** (AR: "روبيان مقلي مع سلطة" →
  "روبيان مقلي").
- **inline-2 (seating)** and **inline-3 (noodles)** cropped 7:5, centered.

Uploaded 4 new WebP attachments (**hero 2811, inline-1 2812, inline-2 2813,
inline-3 2814**), re-injected EN 2800 via `reinject_en.py` and re-populated AR
2808 via `populate_ar_twin.py` (both --media pointed at the new IDs; backups
`20260704-200746` EN + `20260704-200917` AR logged), then **trashed the 4 old
sliced attachments (2796–2799)**. Re-screenshotted mobile + desktop — **every
photo now reads whole and clean.** Kit `images/` folder + `article.md` caption +
AR draft caption updated to match; hero_alt updated to the storefront-sign shot.

**Workflow lesson (worth baking into the kit):** guide photos should be composed
/ pre-cropped **landscape** before publish — hero ≈ 16:9, inline ≈ 7:5 — because
the template hard-crops to those boxes. Portrait phone shots must be cropped
first or they lose their tops/bottoms. Flagging to add to `guide-kit/README.md`
(and a possible Advisor note if the template's forced crop should instead be
portrait-aware — but pre-cropping is the clean fix and needs no cross-lane change).

**Sushi tag — VERIFIED (was the open ⚠).** Pulled the actual menu PDF
(`storage3.me-qr.com/pdf/eed540ce…pdf`, behind the QR-service JS shell) and
rendered its embedded images: the menu has an **extensive sushi section** —
nigiri, sashimi, hand rolls, and a large range of maki/uramaki rolls. So the
`Sushi` / سوشي tag is accurate and clears to ship.

**Tags are LISTING tags, not guide tags** (all guides carry an empty `guide_tag`;
the settled Japanese / Omakase / Sushi / Date-Night live on `gd_place` 2432).
Listing 2432 currently has `gd_place_tags = "Japanese, Reservations Accepted"` —
so **Omakase, Sushi, Date-Night still need adding, and "Reservations Accepted"
(not in the settled four) needs reconciling.** That's a **Pipeline data-pass**
(gd_place), not Blog's lane — flag to Pipeline via Advisor; Blog did not write to
the listing.
