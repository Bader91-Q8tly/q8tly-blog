# Session handoff — Cure (Shuwaikh) fine-dining guide LIVE ON PROD (2026-08-12)

## Status: ✅ PUBLISHED — `guide_article` 5025 · https://q8tly.com/guide/cure-shuwaikh/

**First Blog-lane write to production.** Bader gave the explicit prod go after the
staging blocker below surfaced. Sequence run: canon pre-write snapshot → kit `--execute`
→ verify → cache flush → calendar.

- **Post:** `guide_article` **5025**, `/guide/cure-shuwaikh/`, EN, publish, topic term 1715.
- **Listing:** Cure **3807** (`/places/shuwaikh/cure/`).
- **Media:** hero **5021** + inline **5022 / 5023 / 5024**.
- **Backups:** `prod-20260812-092224.sql.gz` (pre-write, canon `db-snapshot.sh prod`,
  integrity-checked) + `prod-20260812-092325-guide-cure-shuwaikh.sql.gz` (kit).
- **Verify green:** 200 · house chrome · hero · no double title · kicker
  *Food & Drink · Guide · **3 min read*** · deck + byline · place card →
  `/places/shuwaikh/cure/` · **0 raw shortcode leak** · breadcrumb → `/guide/topic/food-drink/`
  · captions "The dining room / A beef plate / The terrace".
- **Served-image proof:** all four re-downloaded from the CDN and re-verified —
  **1520×1086, ratio 1.3996, `orientation=none`**. The orientation fix holds through Photon.

### ⚠ Kit bug found on this run — prod backups mislabeled `staging`
`publish_guide.py` §1 hardcodes the literal `staging` in both the dump filename
(`f"staging-{ts}-guide-{slug}.sql.gz"`) and the `BACKUP_LOG.md` env column. The prod dump
landed named `staging-…`. Renamed to `prod-20260812-092325-…` and re-verified (gzip +
`Dump completed`), log corrected by hand. **Fix owed:** derive the label from the resolved
`--ssh-host`, not a literal — every future prod run mislabels its own audit trail otherwise.
Check `reinject_en.py` / `populate_ar_twin.py` for the same.

## The blocker that surfaced: this guide could NOT go to staging

`publish_guide.py` against the configured staging host hard-fails:
`❌ place_id 3807 is not a published gd_place (got 'nothing')`.

Verified over staging SSH: **staging has no Cure at all.** Its newest real `gd_place` is
ID 3563 (2026-07-27) plus `ZZ TEST Collision` fixtures; prod is out past 4659. Cure was
created on prod 2026-07-27 as **3807**. Staging is roughly a month behind and does not
carry the listing this guide is about — `[q8tly_place id=3807]` would render nothing.

**So the only viable target is prod (q8tly.com)**, which is also where the live 9-guide
corpus actually sits (`/wp-json/wp/v2/guides`).

### Doc conflict to resolve (Advisor)
- **Blog `CLAUDE.md`** still says *"Staging only; production (q8tly.com) is frozen."* — **STALE.**
- **Canon `q8tly-core/docs/STATE.md`**: prod LIVE + INDEXABLE since 2026-08-08 (Phase C),
  9 AR guide twins unfenced on prod. Canon wins per the squad sync model.
- **Canon `q8tly-core/bin/db-snapshot.sh:16`**: *"prod writes stay manual + gated."*

Blog `CLAUDE.md` needs updating for the post-flip world (target env + backup host), and
the prod-write gate needs an explicit owner ruling per guide or standing. Not Blog's call.

Prod SSH host (read-only verified this session): `baderlol44-pwgjm.wordpress.com@ssh.wp.com`.

## Photo gate (D-180 §0) — PASS, with a correction worth recording

Candidate pool of six was gated on landscape-crop width before any copy was written:

| Folder | Native landscape | Landscape-crop width | Verdict |
|---|---|---|---|
| **Cure** | **7 / 10** | 4032–5712 px | **PASS — selected** |
| Paparazzi | 5 / 32 | 1852–4032 | PASS but night storefront ~90% black → runner-up |
| Solange (`solage`) | 1 / 22 | 1 native + ~12 croppable | Conditional |
| Queens | 2 / 15 | both **1320 px (<1520)** | Portrait-rescue only, no native landscape hero |
| Nouga | 0 / 11 | — | Also a **café** (Cafes/Specialty Coffee `$$`), not fine dining |
| Odashi | 0 / 7 | **864–1200 px** | **FAIL** — re-shoot, not a fix. NOT Odachi (2432, already guide 2800); no prod listing under this name |

### ⚠ `sips -g` LIES ON HEIC ORIENTATION — first Blog-lane hit of the documented trap
Initial gate read Cure as 10/10 landscape. Wrong. `IMG_2367 / 2371 / 2372` carry EXIF
`Orientation=1` — `sips -g pixelWidth/pixelHeight` reports **stored** dims (4032×3024,
"landscape") while they **display** 3024×4032 portrait. A crop built on the sips numbers
produced a file stamped 1520×1086 that carried `Orientation=6` and rendered **sideways**
in-browser — precisely the `al-shemam-01` / OFK failure the Pipeline already fixed
(`scripts/convert_photos.py`, 2026-07-31, Bader's order ruling: **orientation → strip → resize**).

Caught pre-publish and redone order-correct. **D-180 §0's `sips` one-liner is unsafe as
written** — it screens on stored dims. Recommend the standard adds an orientation-aware
check (`PIL.ImageOps.exif_transpose`, or the Pipeline converter's `--verify`). Route to
Advisor as a D-180 amendment.

### Final image set — all 1520×1086, one ratio, EXIF-clean, verified
| Slot | Source | Note |
|---|---|---|
| hero | IMG_2364 (5712×4284 native landscape) | storefront, daylight, `cure` / كيور both legible |
| inline-1 | IMG_2368 (4032×3024 native landscape) | dining room |
| inline-2 | IMG_2372 (3024×4032 **portrait**) | **PORTRAIT RESCUE, D-180 §4 ledger entry** — landscape crop width 3024 ≥1520, plate whole in frame |
| inline-3 | IMG_2373 (5712×4284 native landscape) | terrace; anchored top. **Weakest frame** — grey counter dominates foreground. Flagged to Bader |

**REJECTED:** IMG_2371 (gold bowl) — any 7:5 crop clips the bowl at both edges, fails
§3B "whole and intentionally in frame". Both of Cure's food shots are portrait; a rescue
was unavoidable if the guide was to carry a dish at all.

Fitter used: `scratchpad/fit_guide_photo.py` (one-off, order-correct, `--verify` mode).
**Worth formalizing into `guide-kit/` as the standing D-180 fitter** — every guide needs
this exact operation and the sips path is now proven unsafe. Not done unasked.

## Register: this guide AMENDS D-168 — needs ratification before it publishes

Owner-specified voice (2026-08-12): *"the friend you ask before you go"* — who it suits,
when to go, an ordering steer, cost in feel, **and one honest drawback** ("a guide with no
drawback reads like an ad"). D-168's neutral model removed exactly those; the live corpus
has no second person, no recommendation, no drawback, and reads **1 min**. This one reads
**~2–3 min** (497 words).

**Structure is unchanged** from the shipped corpus — About prose → captioned inline photos
→ key-facts TABLE → `[[place]]`; no map, no FAQ. Only the register moves. Bader approved
it; flagged as a **D-168 amendment for the Decision Log via Advisor**, not a silent drift.

## Data discipline

**Asserted (all from live listing 3807):** cuisine Japanese/Fusion/Mediterranean · `$$$` ·
13:00–22:45 daily · indoor+outdoor · Design District, Street 28, Shuwaikh · `container_type`
Mall · reservations (SevenRooms) · menu URL · tags Date Night / Group-Friendly / Seasonal Items.

**NOT asserted — not recorded on the listing:**
- ⚠️ **`amenities` EMPTY — on EN *and* AR.** Also `payment_methods`, `smoking`, `phone`,
  `website`, `instagram`, `established_year` — all null.
- `price_kd_min` / `price_kd_max` null → the guide gives a **band, never a KD number**.
  MizuMesa (~13 KD) and B+F (~15 KD) both carry one; Cure is the outlier. **OWED.**
- Six seasonal-specials dishes come from the menu card in IMG_2367, not the listing →
  timestamped in-copy ("on the visit these photos come from").
- "the banquette side is the better seat" = photo-read judgement, Bader-approved.

### ⚠ TO PIPELINE (via Advisor) — reframes their open AR-amenities issue
Pipeline flagged *"AR twins carrying empty amenities"*. On Cure the field is **absent at
source on the EN listing**; AR is faithfully mirroring an empty EN field, not dropping data.
**The owed site-wide coverage check must cover EN, not just AR** — an AR-only sweep will
come back clean-ish and miss this class entirely.

## ✅ AR TWIN LIVE — `guide_article` 5032 · https://q8tly.com/ar/guide/cure-shuwaikh/

Bader-authored Kuwaiti Arabic (D-145), pasted 2026-08-12, injected faithfully. **Unfenced**
(`rank_math_robots` cleared post-run to match all 9 existing twins). **This also CLOSES the
English-leak issue below** — real Arabic now serves at that URL instead of the EN fallback.

Verified live, cache-busted: `<html lang="ar">` · **robots `index, follow`** · self-canonical ·
kicker «طعام وشراب · دليل · 3 دقايق من وقتك» · Arabic deck · body H2s
«من برا Cure / صالة المطعم / **شورت ريبز دونبوري** / التراس / معلومات سريعة» · 7-row facts table ·
place card → `https://q8tly.com/ar/places/الشويخ/cure/` · **0 bare `/places/`** · 0 shortcode
leak · no mojibake · hreflang ar/en/x-default correct · media 5022/5023/5024 reused.
EN side: inline-2 caption → **Short Ribs Donburi** (post 5025, backup `prod-20260812-094928`).
Backups: `prod-20260812-120708` (pre-write) + `prod-20260812-121047` (tool).

### ⚠️ THE BIG ONE — WPML's "+" does NOT create a post on prod; it opens an ATE job
Bader clicked "+" and nothing appeared. Root cause, confirmed in the DB:
`wp_icl_translate_job` had `editor='ate'`, `editor_job_id=207172644`, `translated=0`, and
`wp_icl_translation_status.status=2` (in progress) — the translation was sitting in **WPML's
Advanced Translation Editor cloud queue**, and `wp_icl_translations` held only a
**placeholder `ar` row with `element_id NULL`**. No WP post exists until an ATE job completes
and syncs back. **This is the §9-G ATE caveat, now confirmed live on prod.** The old runbook
line "the + creates the shell, then Blog populates" is **wrong while `editor=ate`**.

**Working recipe (owner-authorized, used here — reusable for every future twin):**
1. Snapshot prod.
2. `wp_insert_post` the AR post (empty body, title = business name, slug = EN slug, publish).
3. ⚠ `do_action('wpml_set_element_language_details', …)` is a **SILENT NO-OP** — it left the
   new post as **EN on its own new trid**. Do not trust it.
4. Delete the **NULL-element** `ar` placeholder row (job bookkeeping, not a translation link —
   no post loses its language), then call **`$sitepress->set_element_language_details($new,
   'post_guide_article', $trid, 'ar', 'en')`** directly. That works.
5. Re-point `icl_translation_status` at the new `translation_id` and convert the job row to the
   WP-editor shape — **target shape copied from the known-good Elysee twin 3122**:
   `status=10, translator_id=0, needs_update=0` · `editor='wp', editor_job_id=NULL, translated=1`.
6. `populate_ar_twin.py --en-id <EN>` (auto-discovers the twin), then **clear the fence**.

### ⚠️ `populate_ar_twin.py` still hardcodes the fence
Line ~171 sets `rank_math_robots=['noindex']` (rail #4, pre-flip). Post-flip that is **wrong** —
every twin on prod is unfenced. Cleared by hand here. **Fix owed: a `--no-fence` flag, or
invert the default.** Same env-mislabel bug as the other two tools (dump written as
`staging-…`; renamed to `prod-20260812-121047-…` and re-verified).

## 🚨 FOUND POST-PUBLISH (now CLOSED for Cure by the twin above, still OPEN as a class)
### an untranslated guide leaks ENGLISH into indexable `/ar/`

`https://q8tly.com/ar/guide/cure-shuwaikh/` returns **200** with **no AR twin in existence**, and:

- `<html lang="ar">`
- **`robots: index, follow`** (NOT noindex)
- **self-canonical** to `https://q8tly.com/ar/guide/cure-shuwaikh/`
- `hreflang` cluster declaring it the **`ar`** version of the EN guide
- and the body served is the **full English article**

So Google can index an English article as a distinct, canonical Arabic page. Duplicate
content plus a broken AR experience, on a live indexable site.

**Why this is new:** pre-flip every twin was noindex-fenced, and the other 9 guides all *have*
twins. **Cure is the first guide published to prod without one**, so it is the first to expose
this class. Any future EN-first guide does the same the moment it publishes.

**Not Blog's to fix** — it's WPML language-fallback/display config (cross-module) → **Advisor,
promptly**. Options for them: set `guide_article` display to *only show translated items*, or
noindex the untranslated `/ar/` fallback, or gate EN publication on the twin existing.
Blog's per-post Rank Math meta **cannot** reach this URL (there is no AR post to set it on).

**Interim mitigation available if Bader wants it now:** he supplies the Arabic and the twin
goes up same-day, which closes it for Cure specifically — but the class stays open for the
next guide until the config decision lands.

## AR twin
Not started. Waits entirely on Bader's Arabic (D-145, human-authored). Note prod AR twins
are now **unfenced** post-flip, so the old fenced/noindex staging path does not apply — the
AR procedure in `GUIDE_AR_WORKFLOW.md` needs a post-flip review before the next twin.

## Homepage featured block — the calendar's rule was wrong
The calendar claimed the block "auto-pulls newest-first and features the newest." **Verified
false on prod** (cache-busted, after Cure became newest): `q8-feat-guide` serves **MizuMesa**
(post 2362, June). Cure surfaced immediately in the **"Fresh from our editors"** strip
(position 2 of 5) and in `/guide/`, `/guide/topic/food-drink/`. Calendar corrected.
**Module 6 / Builder's widget — Blog feeds it, doesn't touch it** → Advisor: what drives the
featured slot, and is there a pin Blog can set?

## Done this session
1. ✅ Photo gate across all six candidates; Cure selected, Paparazzi runner-up.
2. ✅ Guide built, fitted, published to prod (5025), verified live incl. served images.
3. ✅ Calendar + homepage rotation updated (Cure is now auto-featured as newest);
   stale "staging only / AR fenced" wording in the calendar corrected with a provenance note.
4. ✅ `BACKUP_LOG.md` corrected for the prod run + kit bug recorded.

## Next / owed (NOT done — needs Bader or another lane)
1. **Advisor → Decision Log, three items:**
   - **D-168 amendment** — the "friend who went" register (owner-approved 2026-08-12). Cure is
     the first guide on it; the other 9 are still neutral. **Decide: is this the new house
     voice (→ re-author the corpus) or fine-dining-only?** Corpus is now mixed-register.
   - **D-180 amendment** — §0's `sips` screening one-liner is unsafe; must be orientation-aware.
   - **Pipeline reframe** — the empty-amenities class is **EN-source**, not AR-only.
2. **Blog `CLAUDE.md` is stale** — still says "Staging only; production is frozen", and points
   the kit at staging via `config.sh`. Needs a post-flip rewrite (prod target, prod SSH host,
   prod-write gate, AR-unfenced reality). Bader's call on wording.
3. **AR twin** — waits on Bader's Arabic (D-145). `GUIDE_AR_WORKFLOW.md` needs a **post-flip
   review first**: prod twins are unfenced, so the fenced/noindex staging path no longer applies.
4. **Listing 3807 data** — KD price figure + amenities owed (Pipeline).
5. **Runner-up Paparazzi (4643)** queued pending a daylight exterior shot.
6. Repo not committed this session — `guide-kit/guides/cure-shuwaikh/article.md`, this handoff,
   `guide-kit/runs/cure-shuwaikh.md`, calendar + backup-log edits are uncommitted. Images are
   gitignored per the binary policy (correct — they stay in the desktop drop folder).
