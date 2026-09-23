# Editorial Calendar — Q8tly Guides (Module 8)

Single source for what's planned, in progress, and live, plus the **weekly
rotation** the homepage editorial block pulls from. Publish under `/{lang}/guide/`.

Status legend: `idea` → `drafting` → `EN staged` → `AR staged` → `live`
(AR twins now buildable on staging as fenced drafts — 2026-06-29; AR goes *public*
only after the full gate clears — see Published note below).

---

## This Week — Homepage Rotation

> ⚠ **Observed on staging (2026-06-24):** the Module 6 homepage editorial block
> **auto-pulls live guides newest-first and features the newest as "editorial of
> the week."** It does NOT read this markdown list — curation here is effectively
> by *publish recency*. To pin a non-newest guide as the feature you'd need a
> Builder/Module 6 "featured" flag → **route to the Advisor** (don't touch the widget).

> ⚠ **ENV CHANGED 2026-08-08 — guides now publish to PROD (q8tly.com), not staging.**
> Phase C flipped prod live + indexable; the whole guide corpus and the AR twins live there,
> and the twins are **UNFENCED** (the "AR fenced" notes below are pre-flip history, kept for
> provenance). **Staging is stale** — newest real `gd_place` is 3563 (2026-07-27) vs prod past
> 4659 — so a guide about any recent listing hard-fails there. Run the kit with
> `--ssh-host baderlol44-pwgjm.wordpress.com@ssh.wp.com --site-url https://q8tly.com`.
> Blog `CLAUDE.md` still says "staging only / prod frozen" → **stale, owed a fix**.
> Canon: **prod writes stay manual + gated** — get Bader's word, snapshot prod first.

> ⚠ **CORRECTION 2026-08-12 — the "auto-features the newest" note above is WRONG on prod.**
> Verified cache-busted after publishing Cure (newest, 2026-08-12): the featured block
> (`q8-home-section--featured-guide` / `q8-feat-guide`) serves **MizuMesa** (post 2362, June),
> not the newest guide. So the block is **not** ordering by publish recency, whatever it did on
> staging in June. Cure did surface immediately in the **"Fresh from our editors"** strip.
> **Not Blog's widget** (Module 6 / Builder — we feed it, we don't touch it) → **route to the
> Advisor**: what actually drives the featured slot, and is there a pin/flag Blog can set?

**Live homepage state (verified cache-busted, 2026-08-12):**

| Slot | Guide | Slug | Note |
|------|-------|------|------|
| **Featured block** (`q8-feat-guide`) | MizuMesa (Nikkei) — Sharq | `mizumesa-sharq` | ⚠ **not the newest** — selection rule unknown, see correction above |
| Fresh from our editors · 1 | MizuMesa | `mizumesa-sharq` | |
| Fresh from our editors · 2 | **Solange Maison — Kuwait City / Salhia Complex** | `solange-maison-kuwait-city` | **5430**, live 2026-08-13. 2nd fine-dining guide. **First guide built to the four-H2 EN/AR mirror shape** (Cure EN still isn't — see Advisor note) |
| Fresh from our editors · 3 | **Cure — Shuwaikh / Design District** | `cure-shuwaikh` | **first prod-published guide**, first fine-dining guide, first in the "friend who went" register (D-168 amendment) |
| Fresh from our editors · 3 | Elysee Beauty Lounge & Queue Café — Mahboula | `elysee-queue-cafe-mahboula` | **first COMBINED guide** (two venues, one feature) |
| Fresh from our editors · 4 | B+F — 360 Mall (Solar Garden) / Zahra | `bandf-360-mall` | |
| Fresh from our editors · 5 | Odachi — Kuwait City / Khaleejia Tower | `odachi-kuwait-city` | |

Also live in the corpus (not in the homepage strip): `south-avenue-salon-sabah-al-salem`,
`naranj-salmiya`, `anosha-beauty-salon-sabah-al-salem`, `keif-restaurant-al-kout-mall`,
`vibes-coffee-roastery-al-kout-mall`.

---

## Pipeline

| Title | Type (best-of / area guide) | District / Category | EN | AR | Target | Notes |
|-------|-----------------------------|---------------------|----|----|--------|-------|
| **Bar Frès: How Kuwait's Parisian-Japanese Conveyor-Belt Restaurant Works** | spotlight | Restaurants / Fine Dining, Arraya Centre, Kuwait City (6443) | ✅ live **6589** | ✅ live **6591**, unfenced | 2026-09-23 | **DONE (EN+AR same day), NO PHOTOS YET** (held for the restaurant's permission → flat-plate hero). Bader's article verbatim + his edits: EN kids bullet → "Better for adults…"; AR listing/guide links → `/ar/`, invoice attribution → «في زيارة مدوّنة Q8tly بتاريخ ١٩ سبتمبر ٢٠٢٦» (body + FAQ). No Jabriya branch in our data. Text links kept (no card). Twin built without the "+". FAQ schema owed (Builder). |
| **The 11 Best Italian Restaurants in Kuwait (2026)** | **best-of list** #2 | Food & Drink / 11 Italian, country-wide | ✅ live **6313** | ✅ live **6315**, unfenced | 2026-09-22 | **DONE (EN+AR same day).** Verbatim + same build pattern as list #1 (11 cards + `[[map]]`); intro fix "opera house fountain" → "at the opera house, facing the museum fountain" (approved). Hero = Trapani listing photo fitted to 1520×1086 (new attachment 6312). ⚠ Rights unverified (`_rw_1920` looks like a portfolio image; Bader chose it knowingly). Links to list #1 both languages. AR = the file + 1 approved edit (Delfino booking "required"); twin again built without the "+". |
| **The 10 Best Restaurants in Kuwait (2026)** | **best-of list** (first one) | Food & Drink / 10 restaurants, country-wide | ✅ live **6307** | ✅ live **6309**, unfenced | 2026-09-22 | **DONE (EN+AR same day).** Bader's SEO article injected verbatim + 3 approved build changes (text links → 10 place cards, `[[map]]` of all 10, Solange booking "required" → "recommended"). Hero reuses Solange Maison dining room (5427). AR = Bader's Arabic + 3 approved edits (Solange "recommended", restored Chops hours/price + Amiti breakfast, hero alt); twin built **without the "+"** (WPML wrote the TM rows itself). FAQ schema owed (Builder). |
| ~~Cure — AR twin~~ | spotlight (AR side) | Fine Dining / Shuwaikh | ✅ live **5025** | ✅ live **5032**, unfenced | 2026-08-12 | **DONE.** Bader's Kuwaiti Arabic (D-145) injected + verified. Twin created via the **ATE workaround** — the WPML "+" opens an ATE cloud job, not a post; see the handoff for the working recipe. `GUIDE_AR_WORKFLOW.md` **still needs a post-flip rewrite** (ATE path + unfenced default). |
| **Paparazzi** | spotlight | Fine Dining / Italian, Kuwait City (4643) | idea | — | — | **Runner-up from the 2026-08-12 fine-dining gate.** Listing is well-populated (amenities recorded, unlike Cure). **Blocked on photos:** the only storefront shot is a night frame ~90% black → fails D-180 §3B exposure/composition. Needs a **daylight exterior**; the food shots (truffle tagliatelle) are already good. |
| Solange | spotlight | Fine Dining / Chinese, Salhia Complex (4025) | idea | — | — | `$$$$`. Photo set is 1 native landscape + ~12 croppable portraits → conditional PASS, would be a heavy rescue pass. |
| Queens | spotlight | Fine Dining / The Avenues (4659) | idea | — | — | Richest amenities of the pool. **Photos fail:** 2 landscape at 1320px (<1520), rest portrait → DEFER pending a re-shoot. |
| ~~Nouga~~ | — | — | — | — | — | **Not fine dining** — Cafes / Specialty Coffee `$$` (4362). Photo set is 0/11 landscape. Out of the fine-dining pool. |
| ~~Odashi~~ | — | — | — | — | — | **No prod listing under this name** (not Odachi 2432, already guided). Photos 864–1200px → **FAIL, re-shoot not a fix**. |

---

## Published

**Env note (2026-08-12):** entries below the Cure block were written pre-flip, when the corpus
was staging-only and prod was frozen. Post Phase-C (2026-08-08) the corpus lives on **prod**
(q8tly.com) with **AR twins unfenced**. Historical "staging / fenced" wording is kept as
provenance, not current state.

**BAR FRÈS (ARRAYA CENTRE) LIVE ON PROD 2026-09-23 — `guide_article` 6589**
at `https://q8tly.com/guide/bar-fres-arraya-centre/`. Single-place guide about listing 6443 (titled "Barfres" on the site). Text links, no card, no map. **No hero yet** (photos held for the restaurant's permission; D-180 gate owed when they land, and the Bar fres folder's PNGs are screenshots per Pipeline P-285). Rank Math title/description/focus keywords set. **AR twin 6591 live same day** at `/ar/guide/bar-fres-arraya-centre/` (links → `/ar/places/مدينة-الكويت/barfres/` + `/ar/guide/best-restaurants-in-kuwait/`, hreflang paired, indexable). Handoff: `handoffs/2026-09-23-bar-fres-guide.md`.

**THE 11 BEST ITALIAN RESTAURANTS IN KUWAIT (2026) LIVE ON PROD 2026-09-22 — `guide_article` 6313**
at `https://q8tly.com/guide/best-italian-restaurants-in-kuwait/`. 11 place cards (Trapani 1920 · Novikov 5368 · Paparazzi 4643 · Delfino 5059 · Delizio 6072 · Utopia 5905 · Eataly 6012 · NAC 3385 · Si 4224 · Select 3231 · OFK 4618) + `[q8tly_map]`. Hero 6312. Rank Math title/description/focus keywords set. **AR twin 6315 live same day** at `/ar/guide/best-italian-restaurants-in-kuwait/` (11 cards → `/ar/places/`, hreflang paired, indexable). AR later fixed in two rounds: SEO title/meta + H1 to Western digits, and «الاسم (Latin)» house style across the 11 H2s AND the table name column (0 em dashes left). Handoff: `handoffs/2026-09-22-best-italian-list.md`.

**THE 10 BEST RESTAURANTS IN KUWAIT (2026) LIVE ON PROD 2026-09-22 — `guide_article` 6307**
at `https://q8tly.com/guide/best-restaurants-in-kuwait/`. **First best-of list.** 10 place cards (MizuMesa 2354 · Solange 4025 · Naranj 2239 · Cure 3807 · Off the Coal 4330 · Amiti Noura 3145 · Chef Pillai 2818 · Kiwa 1939 · Queens 4659 · Chops 5575) + one `[q8tly_map]` of all 10. Hero = reused attachment 5427. Rank Math title/description/focus keywords set. **AR twin 6309 live same day** at `/ar/guide/best-restaurants-in-kuwait/` (10 cards → `/ar/places/`, hreflang paired, indexable). Later (3 passes): Western digits in H1/SEO/meta; the 10 headings AND the table name column on «الاسم (Latin)» with Bader-supplied spellings (ميزوميسا, شيف بيلاي); "Solange" → "Solange Maison" in EN+AR. Listing 4025/4040 then renamed to "Solange Maison" (slug kept) on Bader's instruction — a Pipeline-lane write by Blog, noted in `handoffs/2026-09-22-to-pipeline-solange-rename.md`; cards and pins now read "Solange Maison". Handoff: `handoffs/2026-09-22-best-restaurants-list.md`.

**SOLANGE MAISON (Salhia Complex, Kuwait City) LIVE ON PROD 2026-08-13 — `guide_article` 5430**
at `https://q8tly.com/guide/solange-maison-kuwait-city/`. Listing: Solange **4025**
(`/places/kuwait-city/solange/`, Fine Dining, `verified_by_q8tly`). Media hero **5426** +
inline **5427/5428/5429**; topic term 1715; kicker *Food & Drink · Guide · 3 min read* (559 words).
Verify green: 200 · house chrome · hero · no double title · **four body H2s** (The escalator /
The dining room / The ceiling / The food) + Key facts · 0 figcaptions · 0 shortcode leak ·
place card → `/places/kuwait-city/solange/` · served images 1520×1086 exif-clean.
Backups `prod-20260813-165435` (pre-write) + `prod-20260813-075517` (kit).

- **Name:** Bader ruled canonical = **Solange Maison** (their branding: solangemaison.com).
  ⚠ **The listing is still titled "Solange", so the place card renders "Solange" under a guide
  titled "Solange Maison"** — visible now, Pipeline's write.
- **First guide on the four-H2 EN/AR mirror shape.** ⚠ Cure's EN still has zero body H2s, so the
  "standard" doesn't match it — ruling + a Cure EN restructure owed (Advisor note 2026-08-13).
- **Photo gate: CONDITIONAL PASS, weakest set shipped.** Originals GONE — only the 1600px
  `optimized images/` set survives. All 16 sources portrait at 1600px → landscape-crop width
  1600, clearing 1520 by **5% with no headroom**; **every photo is a portrait rescue** (D-180 §4).
  Rejected: 5EAAC280 (1086px), IMG_3967, IMG_3985, IMG_3958.
- **⚠ LIVE DEFECT — alt text.** No-captions shape + `publish_guide.py:285` (`alt = cap or title`)
  ⇒ all three inline images carry `alt="Solange Maison"`. Kit fix owed (alt field on the marker).
- **⚠ `/ar/` English leak is LIVE** on this guide (200, `index, follow`, EN body under `lang="ar"`)
  until Bader's Arabic lands. Unruled class — Advisor.
- **Pack vs live disagreements** (resolved in favour of live, none asserted): valet parking
  (pack-only) · 15–19 KD per head (pack-only; `price_kd_min/max` null) · Restaurants parent
  category missing · Celebrations tag absent. AR twin amenities **DO** populate (not Cure's class),
  but the AR **description is still English**.
- **AR TWIN LIVE 2026-08-13 — `guide_article` 5436** at `/ar/guide/solange-maison-kuwait-city/`,
  **publish + UNFENCED (indexable)**. Bader's Kuwaiti Arabic (D-145) injected faithfully, same day
  as the EN. Verified: `lang="ar"` · `robots: index, follow` · self-canonical · kicker
  «طعام وشراب · دليل · 3 دقايق من وقتك» · **four body H2s** (من أول المصعد / الصالة / السقف / الأكل)
  + معلومات سريعة · 7-row table · place card → `/ar/places/مدينة-الكويت/solange/` · 0 bare
  `/places/` · 0 shortcode leak · no mojibake · hreflang ar/en/x-default. **This closes the
  `/ar/` English-leak for this guide** (the class stays open — Advisor).
  Backups `prod-20260813-171242` (pre-write) + `prod-20260813-081514` (tool).
- **🏆 FIRST FULLY-MIRRORED EN/AR PAIR** — 5430 and 5436 have identical four-H2 structure and
  matching 7-row facts tables. Cure (5025/5032) still doesn't mirror; ruling + restructure owed.
- **Twin created via the API path**, not the WPML "+" — Bader pressed "+" and it opened an
  **ATE cloud job** again (`editor='ate'`, `editor_job_id 207331742`, `translated=0`, NULL-element
  placeholder), exactly as on Cure. The documented recipe worked **first try, no strays**.
  **The "+" is a dead end; stop asking for it.**
- ✅ Two kit fixes confirmed landed this run: **env label** (`prod-…` + `| prod |`, no manual
  rename) and **the AR fence** (`populate_ar_twin.py` now ships unfenced by default).
  ⚠ Still open: `alt = cap or title` → `alt="Solange Maison"` ×3 on **both** sides.
- ⚠ Title call: Bader's AR draft headed the doc «سولانج ميزون»; shipped as **"Solange Maison"**
  (Latin) per his own "business names stay in the business's own script" rule + the Cure
  precedent (AR twin titled "Cure"). **One-line change if he wants the transliteration.**

**CURE (Shuwaikh) LIVE ON PROD 2026-08-12 — `guide_article` 5025** at
`https://q8tly.com/guide/cure-shuwaikh/`. **First Blog-lane write to production**, first
**fine-dining** guide, and the first guide in the **"friend you ask before you go"** register.
Listing: Cure **3807** (`/places/shuwaikh/cure/`, Fine Dining + Restaurants, `verified_by_q8tly`).
Media: hero **5021** + inline **5022/5023/5024**; topic term 1715; kicker serves
*Food & Drink · Guide · 3 min read* (497 words — the corpus norm is 1 min). Verify green:
200, house chrome, hero, no double title, deck + byline, place card → `/places/shuwaikh/cure/`,
0 shortcode leak, breadcrumb → `/guide/topic/food-drink/`. Backups
`prod-20260812-092224` (pre-write, canon script) + `prod-20260812-092325` (kit).

- **Register = a D-168 AMENDMENT, owner-approved, owed to the Decision Log via Advisor.**
  Structure unchanged from the corpus (About prose → captioned photos → key-facts TABLE →
  `[[place]]`; no map, no FAQ); only the voice moves — who it suits, when to go, an ordering
  steer, cost in feel, and **one honest drawback**.
- **Photo gate (D-180): PASS**, 7 of 10 sources native landscape at 4032–5712px, all fitted to
  7:5 1520×1086, one ratio, EXIF-clean, verified upright **on the served CDN files**.
  **inline-2 is a PORTRAIT RESCUE** (IMG_2372, 3024×4032 → crop width 3024 ≥1520, plate whole)
  — logged per D-180 §4. IMG_2371 (gold bowl) rejected: any 7:5 crop clips it at both edges.
- **⚠ `sips -g` LIES ON HEIC ORIENTATION** — reports stored dims, so `Orientation=1` files read
  as landscape but display portrait. First crop pass produced sideways-rendering files. Redone
  order-correct (orientation → strip → crop → resize, per the Pipeline's landed
  `convert_photos.py`). **D-180 §0's `sips` one-liner is unsafe as written → amendment owed.**
- **⚠ Kit mislabels prod backups as `staging`** (hardcoded literal) — corrected by hand this
  run; fix owed in `publish_guide.py` (and likely the two sibling tools).
- **Data owed on listing 3807:** `amenities` **EMPTY on EN *and* AR** (so Pipeline's
  "AR twins with empty amenities" is really an **EN-source** gap — their owed site-wide check
  must cover EN); also null `payment_methods`, `smoking`, `phone`, `website`, `instagram`,
  and **no KD figure** (`price_kd_min/max` null) → the guide gives a band, never a number.
- **AR twin: not started**, waits on Bader's Arabic (D-145).

---

All live on STAGING (English) via the Guide Ingestion Kit. Production frozen.
**AR (2026-06-29):** mechanism unblocked — Builder set `guide_article`/`topic`/
`guide_tag` WPML-Translatable, so AR twins can now be built on staging as
fenced/noindex human translations (D-145). Twin-building is paused only until
Builder's `[q8tly_place]`/`[q8tly_map]` AR-URL check returns. AR goes *public*
only after the full gate clears (S2-19/WPML-on-prod is necessary-but-not-sufficient;
also AR-perfect D-160 + owner track + D-157 cutover + 7-G flip).
**First AR twin LIVE (fenced) 2026-06-29:** Anosha → `guide_article` **2600** at
`/ar/guide/anosha-beauty-salon-sabah-al-salem/`, publish + noindex, **D-145 ✓ (PASS)**
— content-complete, parked fenced, rides the site-wide flip (not unfenced per-guide).
**Naranj AR twin LIVE (fenced) 2026-06-29:** `guide_article` **2612** at
`/ar/guide/naranj-salmiya/`, publish + noindex, Bader-authored Kuwaiti Arabic
injected + verified (place-card → `/ar/places/السالمية/نارنج/`). Parked fenced.
**MizuMesa AR twin LIVE (fenced) 2026-06-29:** `guide_article` **2618** at
`/ar/guide/mizumesa-sharq/`, publish + noindex, Bader-authored Kuwaiti Arabic
injected + verified (place-card → `/ar/places/شرق/2405/`). Parked fenced.
**MizuMesa NEUTRAL re-author 2026-06-30:** EN **2362** + AR **2618** bodies replaced with
the new short/neutral model (D-168) — About + Key facts + place card only; no data-table,
no FAQ. Faithful inject of Bader's locked MD (`drafts/mizumesa-sharq_{EN,AR}_2026-06-30.md`).
EN published (indexable), AR stays noindex-fenced. Open flags: inline photos 2359/2360/2361
orphaned (new MD has no inline images → hero 2358 only); SEO meta still old (EN rank_math
title+desc, AR desc); deck = auto-excerpt of the about; AR listing-card slug numeric (2405).
**Refined 2026-06-30 (v2, per Bader):** photos restored with short neutral captions
(hero 2358 "Outside MizuMesa" + inline 2359/2360/2361 = "Inside MizuMesa" / "One of the
rolls" / "A beef dish"; AR mirrors); key facts now render as the **TABLE** (the old
"before you go" look — content-only, no facts-card CSS exists, no Builder), 5 clean rows.
Final = About → 3 captioned photos → key-facts table → listing card. AR fenced. EN via
new `guide-kit/reinject_en.py` (EN counterpart to populate_ar_twin.py; no fence).
Photo-orphan flag RESOLVED. Remaining flags: SEO meta still old; AR listing slug numeric.
**PHOTO FIX 2026-07-05 (first D-180 application, owner-approved):** the 4 portrait photos
(mixed 0.75/0.56 ratios) were re-cropped to **landscape 7:5 (1.407) at 1536px** — one ratio,
all ≥1200px — resolving the portrait/rhythm + sign-clip issues. **inline-2 swapped** (the
900px "One of the rolls" had no ≥1200px source) → a **1536px Nikkei fried-dish**, caption
"One of the rolls" → **"A Nikkei plate"** (AR "أحد أطباق الرول" → "طبق نيكي"). New landscape
attachments hero **3039** + inline **3040/3042/3043** (source: `Desktop/All /Mizu`); EN 2362
re-injected + AR twin 2618 re-populated (backups `20260705-112345` / `20260705-112512`); old
2358–2361 trashed. Verified clean landscape on mobile.
**Naranj NEUTRAL re-author 2026-07-01:** EN **2251** + AR **2612** bodies replaced with the
same short/neutral model (D-168) — About + 3 captioned photos (hero 2247 "Outside Naranj" +
inline 2248/2249/2250 = "Inside Naranj" / "Mezze and meat arayes" / "Dessert at the end of
the meal"; AR mirrors) + key-facts **table** (6 rows) + place card; no `[[map]]`. Faithful
inject of Bader's approved MD (`drafts/naranj-salmiya_{EN,AR}_2026-07-01.md`). EN published
(indexable), AR stays noindex-fenced (content-only update, fence untouched). `rank_math_description`
set to match (EN only, via SSH — the AR precedent leaves AR's blank on a fenced twin).
**Anosha NEUTRAL re-author 2026-07-01:** EN **2189** + AR **2600** bodies replaced with the
same model — About + 3 captioned photos (hero 2190 "Outside Anosha Beauty Salon" + inline
2192/2194/2193 = "Hair-wash lounge" / "Welcome coffee on arrival" / "The nail bar"; AR
mirrors) + key-facts table (6 rows) + place card; old 12-row service/price menu, FAQ, and
"Know before you go" table all dropped (price menu is listing-pipeline scope, not guide
prose). Faithful inject of Bader's approved MD (`drafts/anosha-beauty-salon-sabah-al-salem_{EN,AR}_2026-07-01.md`).
Price tier ($$) confirmed by Bader (intake had left it an open call). EN published, AR stays
noindex-fenced.
**Tool: `reinject_en.py` FORMALIZED 2026-07-01** — the EN counterpart to `populate_ar_twin.py`
is no longer a one-off: auto-backup before every write (self-logged to `BACKUP_LOG.md`), a
hard target guard (refuses unless the post is a `guide_article` with WPML lang `en`/untranslated
— never touches the AR twin or `icl_translations`), a built-in idempotency diff against the
live body, and conditional SEO-meta sync. No-op verified against MizuMesa (post 2362) —
generated body byte-identical to live, full backup→update→verify pipeline clean, AR twin
(2618) confirmed untouched. Documented in `guide-kit/README.md` §6.
**NEUTRAL ROLLOUT STATUS (2026-07-02): 3 of 6 done** — mizumesa, naranj, anosha. **3 remain**
on the old persuasive body: south-avenue-salon-sabah-al-salem (2339/2619), keif-restaurant-al-kout-mall
(2132/2630), vibes-coffee-roastery-al-kout-mall (2131/2634) — same flow, gated on their
approved MDs landing from the Content Writer. (Corrects the "5 remaining" figure carried in
the 2026-06-30 checkpoint and in shared STATE.md — 2 of those 5 are now done.)
**Keif AR twin LIVE (fenced) 2026-06-29:** `guide_article` **2630** at
`/ar/guide/keif-restaurant-al-kout-mall/`, publish + noindex, Bader-authored Kuwaiti
Arabic injected + verified (place-card → `/ar/places/الفحيحيل/مطعم-كيف/`). Parked fenced.
**Vibes AR twin LIVE (fenced) 2026-06-29:** `guide_article` **2634** at
`/ar/guide/vibes-coffee-roastery-al-kout-mall/`, publish + noindex, Kuwaiti AR injected +
verified (place-card → `/ar/places/الفحيحيل/vibes-coffee-roastery/`). Parked fenced.
**South Avenue AR twin LIVE (fenced) 2026-06-29:** `guide_article` **2619** at
`/ar/guide/south-avenue-salon-sabah-al-salem/`, publish + noindex, Kuwaiti AR injected +
verified (place-card → `/ar/places/صباح-السالم/صالون-ساوث-أفينيو/`). Parked fenced.

**✅ AR CORPUS COMPLETE — 8 of 8 fenced twins (2026-07-05)** — anosha 2600, naranj 2612,
mizumesa 2618, keif 2630, vibes 2634, south-avenue 2619, odachi 2808, **B+F 2924**. All
publish+noindex; ride the site-wide AR-public flip together (no per-guide unfence). EN
sides untouched.

**Elysee Beauty Lounge & Queue Café — COMBINED guide PUBLISHED (born-neutral) 2026-07-05:**
EN `guide_article` **3115** at `/guide/elysee-queue-cafe-mahboula/` — **first combined guide**
(two venues in one feature, owner-directed) and **first use of the D-180 Canva-interim PASS
path**. Two women-only spots sharing the 24th-floor rooftop of the Park Inn by Radisson,
Mahboula: **Elysee Beauty Lounge** (Beauty, listing 3066) + **Queue Café** (Cafés, listing
3067), framed as a salon-visit-plus-coffee day out. **Both place cards render** — `[[place]]`
= Queue 3067 + Elysee 3066 via an unquoted raw `[q8tly_place id=3066]` shortcode (WP
`shortcode_unautop` strips the wrapping `<p>` → clean card; verified 2 cards, 0 literal leak).
Photos: the intake's **22 originals were 4284–5712px** (native landscape) → the qualification
gate PASSED cleanly, and 5 were fitted to **7:5 1520×1086** (one ratio, all ≥1520px) — hero
3110 + inline 3111–3114 (rooftop lounge / Elysee sign / salon sea-view / Queue sign / café
interior). Voice neutral (D-168): owner's "fancy/breathtaking" rendered as facts (rooftop /
24th floor / floor-to-ceiling windows / sea views); **no fabrication** — Elysee salon
services/hours/price are unknown, so the salon is described only by confirmed facts. Kit
backup `20260705-205507`. **AR twin LIVE (fenced) 2026-07-05:** `guide_article` **3122**
(trid 4923) at `/ar/guide/elysee-queue-cafe-mahboula/`, publish + noindex — Bader did the
WPML "+", Blog populated from `drafts/elysee-queue-cafe-mahboula_AR_2026-07-06.md` (backup
`20260705-224728`; images reused 3110–3114). Verify PASS: **both AR place cards render** →
`/ar/places/المهبولة/elysee-beauty-lounge/` (3066, raw shortcode) + `.../queue-cafe/` (3067,
`[[place]]`), 0 literal leak, noindex fence present. **Open (D-145 while fenced):** the
combined AR arrangement + connective phrasing + captions are Blog-assembled from Bader's
verbatim sentences — need his review/authoring on the fenced page. Open content gaps (listing
lane, not photos): Queue phone + coordinates; Elysee salon services/hours/price.
**Quality note (owner, 2026-07-05):** Pipeline rated the listings non-qualifying and the blog
~7/10 — the photos cleared the D-180 *technical* floor (≥1520px, 7:5) but are amateur phone
shots (angled/sideways-shot); **gate PASS = publishable floor, not a quality guarantee.** Kept
live as-is per owner. Lever to raise it = styled re-shoot + fuller Elysee intake.

**B+F AR twin LIVE (fenced) 2026-07-05:** `guide_article` **2924** (trid 4805) at
`/ar/guide/bandf-360-mall/`, publish + noindex. Bader made the WPML "+" (clean editable
WP-editor shell 2924); Blog injected the verbatim Kuwaiti AR (`drafts/bandf-360-mall_AR_2026-07-05.md`,
matches listing twin 2730's About, price $$$) via `populate_ar_twin.py` (backup
`20260704-223255`; images reused 2914/2915/2916/2917 — no re-upload). Verify PASS: Arabic
title (Latin brand "B+F"), place-card → `/ar/places/الزهراء/bf-360-mall/` (twin 2730), no
bare `/places/`, no `/ar/en/`, noindex fence present. **Open (D-145 while fenced):** AR
brand-name kept Latin "B+F" (confirm); Blog-drafted AR captions need Bader's read.

**B+F PUBLISHED (born-neutral) 2026-07-05:** EN `guide_article` **2918** at
`/guide/bandf-360-mall/` — Bader-locked About verbatim (matches live listing 2664) + 3
captioned photos (musakhan rolls / beef plate / Solar Garden terrace) + 8-row key-facts
table + place card. **Two pipeline-live corrections applied over the source doc:** price
band **$$ → $$$** (KD figure kept), and slug/district settled = **Zahra** (place card →
`/places/zahra/bf-360-mall/`, listing 2664). Mall services carried as the "Via 360 Mall
(not venue amenities)" line only; no Burger/Steakhouse/"Restaurant inside Mall" labels in
guide prose (NEEDS-BADER). Photos pre-cropped landscape (portrait originals would slice —
the Odachi lesson); hero 2914 + inline 2915/2916/2917. Kit run backup `20260704-215916`.
**Canva-interim fit test 2026-07-05 (D-180): FAILED on sourcing, not framing.** The full
ORIGINAL B+F folder is the same size as the optimized set — the storefront/sign original is
**1086 px wide** (6 of 7 are 1086–1089 px; only the salad is 1200 px). A landscape 7:5 crop
maxes at the source width (1086 px) → under the 1200 bar; Canva reframes but can't upscale.
**Verdict: photo-SOURCING problem → B+F grandfathered as-is; fix = higher-res re-shoot
(≥1520 px, landscape), not Canva.** No guide change made.

**Odachi PUBLISHED (born-neutral) 2026-07-04:** EN `guide_article` **2800** at
`/guide/odachi-kuwait-city/` — **first guide shipped straight onto the D-168 neutral model
at publish time** (no spotlight-era body to re-author): Bader-locked About verbatim + 3
captioned photos + 6-row key-facts table + place card; no `[[map]]`. Kit run clean (backup
`20260704-183756`). Place card resolves `/places/kuwait-city/odachi/` (listing 2432).
**Photos re-cropped 2026-07-04 (post-publish, per Bader — "weird pictures"):** the
guide-single template center-crops inline photos to a fixed landscape box (~7:5 desktop /
~1:1 mobile; hero 16:9), so the original **portrait** phone shots lost their tops/bottoms
(shrimp & noodle bowls cut). Fixed in-lane by pre-cropping each to the template's box,
centered on the subject: hero swapped to the **bright storefront-sign** shot; shrimp crop
drops the second salad bowl (caption → "Fried shrimp"). New WebP attachments **hero 2811 +
inline 2812/2813/2814** (old 2796–2799 trashed); EN 2800 re-injected + AR 2808 re-populated
(backups `20260704-200746` / `20260704-200917`), verified clean on mobile + desktop.
**Kit lesson:** compose guide photos **landscape** before publish (hero 16:9, inline 7:5) —
the template hard-crops. **Sushi tag verified** from the menu PDF (extensive nigiri/sashimi/
maki section) — but tags are `gd_place` listing tags (Pipeline lane), not guide tags.
**Odachi AR twin LIVE (fenced) 2026-07-04:** `guide_article` **2808** (trid 4743) at
`/ar/guide/odachi-kuwait-city/`, publish + noindex. Bader made the WPML "+" (clean editable
WP-editor shell, 2808); Blog injected the Bader-authored Kuwaiti AR
(`drafts/odachi-kuwait-city_AR_2026-07-04.md`) via `populate_ar_twin.py` (backup
`20260704-190246`; images reused 2796/2797/2798/2799 — no re-upload). Verify PASS: Arabic
title no mojibake, place-card → `/ar/places/مدينة-الكويت/odachi/`, no bare `/places/`, no
`/ar/en/` double-prefix, noindex fence present. **Still open (D-145 review while fenced,
same as every twin):** one-word twin mismatch (AR "هادي" vs EN locked "cozy" — Bader rules);
staged AR captions/hero_alt are Blog-drafted, need Bader's D-145 read. Listing-lane flags
(coordinates, WhatsApp?, menu-link durability, Sushi tag) belong to Pipeline, not the guide.

| Title | URL (`/{lang}/guide/…`) | guide_article | Live date | Internal links placed |
|-------|--------------------------|---------------|-----------|------------------------|
| Anosha Beauty Salon — Sabah Al-Salem | `/guide/anosha-beauty-salon-sabah-al-salem/` | 2189 | 2026-06-20 | ✓ `/places/sabah-al-salem/` + `/places/category/salons/` (2026-06-24) |
| Naranj — Salmiya | `/guide/naranj-salmiya/` | 2251 | 2026-06-22 | ✓ `/places/salmiya/` + `/places/category/restaurants/` (2026-06-24) |
| South Avenue Salon & Spa — Sabah Al-Salem | `/guide/south-avenue-salon-sabah-al-salem/` | 2339 | 2026-06-23 | ✓ `/places/sabah-al-salem/` + `/places/category/salons/` + `/places/category/spas-massage/` (2026-06-24) |
| MizuMesa (Nikkei) — Sharq / KIPCO Tower | `/guide/mizumesa-sharq/` | 2362 | 2026-06-24 | ✓ `/places/sharq/` + `/places/category/restaurants/` (at publish) · ext: mizumesa.com reservations |
| Odachi — Kuwait City / Khaleejia Tower | `/guide/odachi-kuwait-city/` | 2800 | 2026-07-04 | — born-neutral body carries no internal links (parity with the other neutral bodies) |
| B+F — 360 Mall (Solar Garden) / Zahra | `/guide/bandf-360-mall/` | 2918 | 2026-07-05 | place-card → `/places/zahra/bf-360-mall/` (2664); price $$$; born-neutral, no internal links |
