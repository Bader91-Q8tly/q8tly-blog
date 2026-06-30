# Handoff — Blog (Module 8) checkpoint: AR corpus complete, workflow proven (2026-06-30)

**Blog is at:** all 6 guides are bilingual — EN live + AR twin built, D-145-clean,
fenced (noindex). The AR injection pipeline is proven end-to-end and documented.
Nothing pending on Blog's side except future new guides (await Bader's MD) and the
site-wide AR-public unfence (owner/Advisor).

## The 6 AR twins (all `publish` + `noindex`, fenced, parked)
| EN guide | → AR twin |
|---|---|
| anosha 2189 | **2600** (D-145 PASS, reviewed) |
| naranj 2251 | **2612** |
| mizumesa 2362 | **2618** |
| keif 2132 | **2630** |
| vibes 2131 | **2634** |
| south-avenue 2339 | **2619** |

All ride the **site-wide AR-public flip together — NOT unfenced per-guide.**
`rank_math_robots` stays `noindex` until that flip.

## Proven twin workflow (per guide)
approved AR MD → **Bader clicks WPML "+"** on the EN guide (native WP-editor shell) →
`guide-kit/populate_ar_twin.py --en-id <EN> --media inline-1=…,inline-2=…,inline-3=…,hero=… --execute`
→ backup → **charset-safe inject** (reuse EN media; `ensure_ascii=False`) → **fence
noindex** → verify (`/ar/places/…` emission, 0 raw shortcodes, no mojibake, hero+media).
Tool auto-discovers + hard-verifies the WPML trid link before writing; refuses if the
twin is missing/orphaned/EN-mismatch. Default fence = publish+noindex (so the page
renders for the proof); `--draft` to keep it draft.

## Two content cases
- **NEW guide:** Bader hands **EN + AR MD** (+ images) → build **both** (EN via the kit,
  `guide-kit/README.md` / `publish_guide.py`, then the AR twin).
- **EXISTING EN guide:** EN already live → build the **AR twin only**, EN untouched.

## Hard rules (D-145 + WPML)
- **AR is HUMAN-authored (D-145).** Bader writes/approves the Kuwaiti Arabic MD; Blog
  **injects**, never machine-translates guides. (Listings = DeepL = Pipeline's lane, not
  Blog's.) Approval signal = `_kuwaiti_clean` filename / Bader's explicit "ok" / handing
  the final `_kuwaiti` file. A raw MSA draft or an **unblessed** machine-Kuwaiti pass is
  NOT injectable — confirm before injecting.
- **Never `wp post create` an AR guide. Never hand-write `icl_translations`/`trid`.**
  WPML owns the link (the "+") or `/ar/` orphans.
- **The "+" comes right before injection, never before the AR content exists** (early "+"
  leaves stale/empty trid slots; under ATE it makes no editable post — see §9-G).
- **Twins stay noindex** until the site-wide AR-public flip (D-160 + owner track + D-157
  cutover + 7-G) — not per-guide.
- **Repo is text-only:** images live on Bader's desktop (gitignored); the kit reads them at
  publish; AR twins **reuse EN media** (no re-upload).

## Canonical tooling / docs
- `guide-kit/populate_ar_twin.py` — update-only AR injector (proven 6×).
- `guide-kit/GUIDE_AR_WORKFLOW.md` — full runbook; **§1.5** = the two cases + rules; §9-G = ATE caveat.
- `guide-kit/README.md` + `publish_guide.py` — EN publish kit.
- `calendar/editorial-calendar.md` — corpus status. `drafts/<slug>_AR_2026-06-29.md` — the approved AR per guide.

## In-flight / owner-owed
- **New guides:** await Bader's EN + AR MD (+ images on his desktop). None queued now.
- **Site-wide AR-public unfence:** owner/Advisor signal — not Blog, not per-guide.
- **Optional (Bader's call):** keif/vibes AR twins carry `[[place]]/[[map]]` cards their EN
  guides lack (added per instruction) — backfill EN to match, or leave.
- **Pipeline note (not Blog):** mizumesa's AR *listing* twin (2405) has a numeric slug → card
  path `/ar/places/شرق/2405/` (vs others' Arabic slugs).
- **Nav label `الأدلة → دليل` (Builder):** no impact on Blog — zero occurrences of either term
  in Blog's domain; AR guide bodies name the place type, not the section. No action.

## ATE caveat (runbook §9-G)
Site WPML editor is global **ATE** (listings need it for DeepL). Guide twins must be created
via the **WP-editor** path — Bader's "+" produced editable shells all 6× this session. Open
with Builder: set `guide_article` to WP-editor translation so every "+" is reliably editable
(global stays ATE for listings).
