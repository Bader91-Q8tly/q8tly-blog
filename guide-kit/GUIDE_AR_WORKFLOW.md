# Guide → Arabic (AR) Twin — Standing Workflow Runbook

> **Module 8 (Editorial / Guide).** The single, repeatable procedure for giving
> any guide its Arabic version. **Read this FIRST** whenever Bader hands over a
> new guide or says "add Arabic." It pairs with **`guide-kit/README.md`** (the
> EN publishing kit) — that one ships English; this one defines the EN→AR
> lifecycle and how the Arabic twin is made.
>
> Source of truth for the AR side. Last verified against live staging:
> **2026-06-28** (see §10). **Update 2026-06-29: the WPML translatable flip is
> LIVE** — `guide_article` + `topic` + `guide_tag` are now Translatable (Builder,
> confirmed via Advisor), so the AR-twin mechanism is unblocked and the "+ add
> translation" button renders on guides. **Twin-building is HELD** pending one
> read-only check — shortcode AR-URL emission (§7 / §9-C). When you act, re-verify
> the WPML state over SSH — settings drift.

---

## 0a. Cross-lane sync — Blog within the six-lane squad (q8tly-core = shared canon) · added 2026-06-30

Canonical six-lane workflow: **`q8tly-core/docs/WORKFLOW.md`** (Builder's repo / shared
GitHub `git@github.com:Bader91-Q8tly/q8tly-core.git`; cloned at `~/Desktop/q8tly-core`).
This runbook is Blog's **operational** lane; the rules below keep it in sync. **Augment,
never contradict.**

- **Source of truth.** q8tly-core is canonical for **shared truth** — the code +
  `docs/DECISIONS.md`, `docs/STATE.md`, `docs/BUILD_LOG.md`, `docs/WORKFLOW.md`. On any
  conflict about what was decided or the project's shared state, **q8tly-core wins.**
  Blog stays authoritative for its **own operational scope** — the guide-build process,
  the AR-twin injection workflow (`populate_ar_twin.py`), and its own repo's state.
- **Code/config caveat.** The guide system's **code** lives in q8tly-core: the
  `guide_article` CPT config, `[q8tly_place]`/`[q8tly_map]` shortcode resolution, the WPML
  Translatable + per-type-editor flags (`post_translation_editor_native_for_post_type['guide_article']=true`).
  Those are **q8tly-core-authoritative and Builder owns the edits.** **Blog owns the
  content + the injection; Builder owns the guide-system code.**
- **Sync direction (one-way).** Blog **READS** shared canon and **DEFERS** on shared
  decisions — esp. **D-145** (editorial = human AR, never machine), **D-163** (AR
  surface→mechanism map; only listings + guides twin; never hand-write `icl_translations`/
  `trid`), **D-161** (AR controlled terms = Pipeline's mapping, not Blog's), **D-167**
  (fragile zones). Blog **does NOT write to q8tly-core** (only Builder commits there); its
  own repo (`q8tly-blog`) stays its own.
- **Blog's hard rules ARE canon** (authoritative home = q8tly-core DECISIONS/WORKFLOW; this
  runbook reflects them): D-145 human AR; never `wp post create` an AR guide; never
  hand-write `icl_translations`/`trid` (D-163); "+" right-before-injection-never-before;
  per-type WP-editor for guides — **never flip the global `doc_translation_method`** (breaks
  listings DeepL); twins stay noindex until the site-wide AR-public flip.
- **Cross-lane changes route through the Advisor.** A decision affecting shared canon — a
  guide-system rule, a new D-number, anything touching Builder's code or another lane —
  goes **Advisor → ratified → Builder commits.** Blog proposes/flags; never self-ratifies
  or edits q8tly-core.
- **Advisor is the connector.** Handoffs go **through the Advisor**, who verifies the prior
  lane's done-signal before relaying. Blog does **not** coordinate directly with Pipeline /
  Builder / Chrome.
- **If this runbook ever diverges from canon, canon wins** — update the local reflection
  here (§3.5 mirrors D-163; §1.5/§2 mirror D-145 + WORKFLOW safety rules), never the
  reverse. *(Resolved in canon: WORKFLOW "per-type editor" + STATE confirm `guide_article`
  is on the WP-editor path — the §9-G ATE concern is closed; global stays ATE for listings.)*

---

## 0. Classification — what "blog" means here (answer to Advisor's first question)

**"Blogs" = the EXISTING guide / editorial system. There is no separate "blog"
content type, and we are NOT introducing one.**

What the repo actually contains:

- One content type: the **`guide_article` Custom Post Type** (REST base
  `/wp/v2/guides`), front-end `/guide/{slug}/`. Six are live on staging:
  `anosha-beauty-salon-sabah-al-salem`, `naranj-salmiya`,
  `south-avenue-salon-sabah-al-salem`, `mizumesa-sharq`,
  `keif-restaurant-al-kout-mall`, `vibes-coffee-roastery-al-kout-mall`.
- The publishing kit `guide-kit/` that ships them.
- The role-brief **forbids `/blog/`** ("Publish them under `/{lang}/guide/`,
  never `/blog/`").

So when Advisor says "blog," map it to **guide**. **Existing rulings already
cover this lane** — D-145 (editorial = human translation) and S2-19 (the WPML /
AR-publishing gate). No new content type and no new "is-this-a-blog" ruling is
needed.

> ⚠ **Correction to one of Advisor's four rails (factual, not directional).**
> Rail #3 says *"blogs are WP posts, not directory listings."* The
> **"not directory listings"** half is exactly right and load-bearing — keep it.
> But they are **not the WP `post` type**; they are the **`guide_article` CPT**.
> This matters for WPML: translatability is configured **per post type**, so the
> Arabic twin must be enabled on `guide_article` specifically — enabling it on
> `post` does nothing for us (see §3, the current blocker). The *intent* of the
> rail (simple model — an item and its translated twin, none of the listings
> machinery) holds perfectly; only the type name is corrected.

---

## 1. Quick start — "Bader handed me a new guide" (cold-start, one glance)

```
EN (do today, fully supported):
  1. Build/receive the drop folder  guide-kit/guides/<slug>/  (article.md + images/)
  2. python3 guide-kit/publish_guide.py guide-kit/guides/<slug>            # dry run
  3. python3 guide-kit/publish_guide.py guide-kit/guides/<slug> --execute  # publish EN
     -> live at /guide/<slug>/   (record the guide_article ID)

AR (the twin — see §3 GATE before executing):
  4. PREREQUISITE (one-time): guide_article + topic [+ guide_tag] WPML-Translatable.
     -> DONE 2026-06-29 (Builder; confirmed via Advisor). The WPML "+" twin button
     now renders on guides. Re-confirm over SSH before your first twin (re-verify).
  5. CURRENT GATE before building ANY twin: Builder's read-only check that
     [q8tly_place]/[q8tly_map] emit /ar/place/... on AR pages (not /place/... and
     not /ar/en/...). HOLD twin-building until Advisor relays that finding (§7,§9-C).
  6. Stage the human Arabic in drafts/<slug>_AR_<date>.md, converted to the
     kit's PLAIN-body + markers format (§8 — current AR drafts are old HTML chrome).
  7. In wp-admin, on the EN guide, click WPML "+" next to Arabic to create the
     LINKED AR twin (§5). NEVER `wp post create` an AR guide. NEVER touch icl_*.
  8. Paste/populate the reviewed AR body + meta into that twin; keep it noindex
     (fenced). Human review (D-145) -> owner sign-off -> unfence (§ Phase C).

If unsure which step you're at: EN is unblocked; the flip (step 4) is DONE;
AR twin-building is paused on step 5 (Builder's shortcode-URL check).
```

---

## 1.5. The two standing cases + the D-145 & sequencing rules (READ FIRST)

Guide AR work is always one of two cases. **Bader provides the human Arabic; the
tool injects it — the tool NEVER translates** (D-145).

**Case A — NEW guide (doesn't exist yet).** Bader hands **two MD files (EN + AR)**
+ the images. You build **BOTH**: publish the EN guide via the kit, then build the
AR twin. The AR MD is **Bader-authored human Arabic** (D-145-clean — Bader is a
native Kuwaiti, the human author).
  → EN: kit publish (`guide-kit/README.md`). → AR: Bader does WPML "+" on the new
  EN guide → `populate_ar_twin.py` injects the AR MD → fence noindex.

**Case B — EXISTING EN guide needs AR** (e.g. naranj 2251 / south-avenue 2339 /
mizumesa 2362 / keif 2132 / vibes 2131). The EN guide is **already published — do
NOT recreate it.** Build the **AR twin ONLY**; the EN side is untouched.
  → Bader hands the **approved AR MD** → Bader does WPML "+" on the existing EN
  guide → `populate_ar_twin.py` injects → fence noindex.

**D-145 rule (non-negotiable):** guide Arabic is **always human-authored** — by
Bader (native Kuwaiti) or an AR blogger — **never machine-translated for
publication**. The tool injects human Arabic; it never translates. (Listings use
DeepL; **guides never do.**) Machine/working Arabic is allowed **only as a draft
scaffold** for Bader to rewrite (e.g. `*_AR_draft.md` on his Desktop) — not
publishable until Bader rewrites + approves it. The approved rewrite is the
D-145-clean AR we inject.

**Sequencing rule (critical — avoids stale/empty WPML slots):** the WPML "+" comes
**right before injection, NOT before the AR content exists.** Order per guide:
**approved AR MD ready → Bader does "+" (clean native shell) → tool injects →
fence.** Never "+" first — an early "+" (esp. under ATE) leaves a stale/empty trid
slot (we hit exactly this on 2189's first attempt). See §9-G for the ATE caveat
(the "+" must create an *editable* WP-editor shell, not an ATE job).

---

## 2. The four hard rails (non-negotiable — bake these into every action)

1. **WPML owns the Arabic twin. You NEVER write the linkage yourself.** The
   EN↔AR connection (WPML's `trid` in `icl_translations`) is created **only** by
   WPML — via the "+ add translation" control in wp-admin. Never `INSERT` into
   `icl_translations`, never `wp post create` a standalone AR guide. Writing the
   rows by hand (or creating an unlinked AR post) **orphans `/ar/` and breaks
   Arabic routing**. This is the single most important boundary. (§5 is the proof
   this is honored.)
2. **Blog Arabic is HUMAN translation, not machine (D-145).** Editorial —
   guides, articles, About, legal — is human-translation-only. *Listings* use
   DeepL for bodies; **guides do not.** Flow = author EN → WPML makes the twin
   shell → a human writes/reviews the Arabic → live on review. No auto-translate
   step for guide bodies, ever.
3. **Guides are the `guide_article` CPT, not directory listings.** None of the
   listings machinery applies — no controlled-term mapping, no area-binding, no
   business-name COPY. The model is just: a `guide_article` and its translated
   twin. (See §0 for the one correction to this rail's wording.)
4. **Arabic stays fenced (noindex) — and a per-guide sign-off does NOT unfence it.**
   An AR twin is created noindex and **stays noindex**. The D-145 human review +
   owner sign-off is a **quality gate** (confirm the human Arabic renders right),
   **NOT a go-live** (clarified by Bader 2026-06-29): we do **not** flip individual
   twins to indexable ahead of the **site-wide AR-public flip** — unfencing one guide
   ahead of the site gains nothing and creates inconsistency. All AR twins unfence
   **together** at the site-wide flip (**D-160 + owner track + D-157 cutover + 7-G**),
   Advisor-owned. Setting the per-twin noindex (Rank Math robots) is ours; flipping it
   off happens only as part of that site-wide flip.

---

## 3. Current state of the gate (verified, and where it really stands)

**This section corrects stale repo docs. Verify before trusting.**

What the older docs say (now partly stale): the role-brief, calendar, and the
2026-06-20 Anosha handoff state *"WPML not active on staging"* / *"AR publishing
GATED on WPML being on production (S2-19)."*

**What is actually true on staging today (verified 2026-06-28 over SSH):**

| Fact | Verified value |
|---|---|
| WPML active on staging | **YES — v4.9.5** (`sitepress-multilingual-cms`, `wpml-string-translation`, `geodir-multilingual`) |
| Languages | default **`en`**, active **`ar, en`** |
| URL format | **directories** (`language_negotiation_type=1`); EN = no prefix, AR = `/ar/`; `/ar/` returns **HTTP 200** |
| `guide_article` translatable in WPML | **YES (flipped 2026-06-29)** — was `NOT SET` on 2026-06-28; Builder set it Translatable, confirmed via Advisor. Re-confirm over SSH at first-twin build. |
| `topic` taxonomy translatable | **YES (flipped 2026-06-29)** — flipped with `guide_article`. |
| `guide_tag` taxonomy translatable | **YES (flipped 2026-06-29)** — included proactively by Builder so tags don't need a second flip later. |
| `post` / `page` translatable | yes, both = `1` ("only show translated items") |
| `anosha` (2189) language record | **none** — WPML doesn't track it (because the CPT isn't translatable) |

**RESOLVED 2026-06-29.** The former blocker — `guide_article` (and `topic`) not set
Translatable — is cleared: Builder flipped `guide_article` + `topic` + `guide_tag`
Translatable (D-145 guard confirmed intact: WPML Translate-Everything **OFF**, 0
guide twins, 0 DeepL jobs — mechanism *enabled*, **not** MT-enrolled), confirmed via
Advisor. The WPML "+" twin button now renders on guides; the rail-#1 sanctioned
creation path exists. **New active gate before building any twin:** Builder's
read-only check that the body shortcodes emit correct `/ar/` URLs (§7, §9-C) — Blog
**holds twin-building** until Advisor relays that finding. (Translatability is per
post type — enabling EN→AR on `post` never helped us; §0.)

**Who flips it:** Setting a CPT/taxonomy translatable is a **WPML / global-site
config change** (WPML → Settings → *Post Types Translation* and *Taxonomies
Translation*). Per the role-brief, global-state / cross-module changes **route to
Advisor / Builder (Module 6)** — do **not** flip it silently from Module 8.
**This is flag §9-A.**

**Two distinct gates, kept separate:**

- **Technical (staging):** once `guide_article` + `topic` are Translatable, the
  full AR-twin workflow below is **executable and testable on staging today** —
  as fenced drafts, prod untouched.
- **Policy / public (S2-19 + D-145 + rail #4):** an AR guide does not go *public*
  until WPML is on **production** (prod is frozen) **and** the Arabic is
  human-reviewed **and** the owner signs off to unfence. Staging twins stay
  fenced meanwhile.

> **S2-19 reconciled (2026-06-29, per Advisor canon):** the AR-public gate is
> **NOT** "WPML on prod" alone. WPML-on-prod is **necessary-but-not-sufficient**;
> current canon gates AR-public on **AR-perfect (D-160) + owner track + the D-157
> cutover + the 7-G flip.** This lane's older S2-19 wording ("AR publishing GATED on
> WPML being on production") is **pre-D-160 drift — incomplete, not a direct
> contradiction**: it under-specifies the gate (implies WPML-on-prod ⇒ publish)
> rather than asserting the opposite of D-160. Patched to canon in role-brief,
> README, calendar, and here. Residual flag to Advisor: this lane holds no S2-19
> *source text*, only the paraphrase — if the central spec literally says
> WPML-on-prod is the *whole* gate, that contradicts D-160 and needs a central
> patch (§9-B).

---

## 3.5. AR Surface Mechanism Map (cross-lane briefing — where guides fit)

> **Shared briefing across all Q8tly lanes; the #1 cause of duplicate/broken AR
> pages is using the wrong mechanism for a surface.** Verified read-only in WPML
> **2026-06-28** (WPML active, EN default + AR, *"different languages in
> directories"* → Arabic under the `/ar/` prefix). Recorded here so Module 8 never
> improvises Arabic on a non-guide surface. **Only listings and (later) guides
> become twin pages — everything else becomes Arabic by translating strings or
> terms, never a second page.**

| # | Surface | Mechanism | Makes a second page? |
|---|---|---|---|
| 1 | **Listings** (`gd_place`) | **A — twin page**, created *only* via WPML (shared `trid`). Never write `icl_translations`/`trid` by hand → orphans `/ar/`. Bulk AR run = this. | **Yes** |
| 2 | **Search page + GD template pages** (`/ar/search/`, GD Archive/Location) | **C — routing, no twin.** Same page served under `/ar/`; labels come from String Translation. 🚫 Never twin a GD-template page (this is the "3 pages" failure). | **No** |
| 3 | **Filter labels + UI chrome** (Price Range, Amenities, Payment, Indoor/Outdoor…) | **B — String Translation** (domains `geodirectory` / `q8tly-core`). Translate the strings; one page, translated copy. | **No** |
| 4 | **Category / taxonomy archives** (`/ar/…/المطاعم/`) | **C — translated term, no twin.** `gd_placecategory` is Translatable; translate the term (D-161 mapping) and WPML/GD generates the archive. 🚫 Never twin an archive. | **No** |
| 5 | **Guides** (`guide_article`) — **our lane** | **No mechanism yet (blocked).** `guide_article` is **Not Translatable** in WPML → no twin button. After Builder flips it Translatable, guides use **mechanism A (twin)** but with **human translation (D-145)** — no DeepL, none of the listings controlled-term machinery. WPML creates the twin; never write `icl_translations` directly. | Yes (after the flip) |

**Module 8 takeaway:** our only twin surface is guides, and it's parked behind
Builder's Translatable flip (§3, §9-A). When it lands, follow §4–§8 (WPML twin,
human-only). For *any* non-guide surface, **do not create a page** — if it shows
only "+ add translation" in WPML and it's a GD-template page or archive, that's
*correct*; translate its strings (mechanism B) or its term (mechanism C) instead.
We don't author AR vocab — that's Pipeline's approved mapping (D-161), and it
doesn't apply to guide prose anyway.

---

## 4. Lifecycle of one guide, EN then AR (imperative — execute in order)

### Phase A — EN original (supported today; this is `guide-kit/README.md`)

1. Assemble the drop folder `guide-kit/guides/<slug>/` (`article.md` with
   frontmatter + **plain** prose body + markers; `images/hero.*` etc.). If Bader
   gave only content + photos + the listing, build the folder from
   `guide.template.md`.
2. `python3 guide-kit/publish_guide.py guide-kit/guides/<slug>` (dry run) →
   review the body + plan.
3. `… --execute`. The kit backs up the DB, uploads images over SSH, creates the
   `guide_article`, sets `deck`/`topic`/`article_type`/hero/meta, does any
   Page→guide 301, touches + flushes cache, and writes `guide-kit/runs/<slug>.md`.
4. **Record the EN `guide_article` ID** (e.g. Anosha = 2189). The AR twin is
   created *from* this post.

### Phase B — AR twin (WPML-gated; execute once §3-A prerequisite is cleared)

> Rail #1: every step here goes **through WPML**. No direct post creation, no
> `icl_translations` writes.

1. **Prepare the human Arabic** in `drafts/<slug>_AR_<date>.md`:
   - **Human translation only** (D-145). No DeepL/MT for the body.
   - **Convert to the kit's plain-body + marker format** (§8). Do **not** keep
     the hand-built `<figure>`/`<picture>`/byline HTML the current AR drafts use —
     the template renders that chrome and it will double-render.
   - AR internal links use the `/ar/...` prefix (§7). Never hardcode `/en/`.
2. **Create the linked twin in WPML (the only sanctioned creation path — §5):**
   open the **EN** guide in wp-admin → in the **Language** box click the **"+"**
   next to **العربية / Arabic**. WPML creates a new `guide_article` **and** the
   `trid` link to the EN original in one action.
3. **Populate the twin** with the reviewed AR title, plain body (markers
   expanded), `deck`, `topic` (translated term), `article_type`, hero + inline
   images, Rank Math title/description. Two ways:
   - **wp-admin paste** (works today): paste the converted body, set meta + the
     AR hero, save.
   - **kit-assisted (future, preferred):** extend `publish_guide.py` with an
     `--into <ar_post_id>` mode that uploads images, builds the body, and runs
     `wp post update <ar_post_id> …` + meta — i.e. **everything except create**.
     It must **never** `wp post create` for AR (that would orphan the twin and
     break rail #1). This is a noted kit gap — see §9-D.
4. **Fence it (rail #4):** set the AR twin's Rank Math robots to **noindex**, and
   keep `post_status` as `draft` (or published-but-noindex) until review. It is
   not "published" in our sense until Phase C clears.
5. **Touch + flush** after any WP-CLI meta write (`wp post update <id>` +
   `rocket_clean_domain()`), or the WordPress.com edge cache serves stale — the
   same gotcha as EN (see `guide-kit/README.md` §3).

### Phase C — review (quality gate; the twin STAYS noindex)

1. **Human review** of the Arabic (accuracy, tone, RTL, links) **on the live fenced
   page**. D-145 means a human signs the translation off — not a machine, not us
   asserting it. Use the per-guide checklist (e.g. `drafts/<slug>_AR_<date>_D145-REVIEW.md`;
   first one: `…anosha…_AR_2026-06-29_D145-REVIEW.md`).
2. **Owner sign-off** (Bader) means *"the Arabic is correct and ready"* — a **quality
   gate, NOT a go-live** (clarified 2026-06-29). The twin **stays `noindex`**. Do
   **not** flip an individual twin to index ahead of the site-wide flip.
3. **Unfence happens later, site-wide, for ALL twins together** — at the AR-public
   flip (**D-160 + owner track + D-157 cutover + 7-G**), Advisor-owned. Only then do
   the Rank Math robots come off noindex.
4. **Update** `calendar/editorial-calendar.md` (AR column → "ready · fenced") and write
   a `/handoffs` note.

> Reminder: never conflate the **quality gate** (D-145, per guide) with the
> **go-live** (site-wide AR-public flip). A guide can be D-145-approved and still
> correctly sit noindex until the site flips.

---

## 5. How the AR twin is created via WPML (proof rail #1 is honored)

**The twin is created by exactly one action: the WPML "+ add translation"
control on the EN post.** That action does two things atomically — creates the
new `guide_article`, and writes the `icl_translations` row sharing the EN post's
`trid`. That shared `trid` is the EN↔AR link, and **WPML is the only thing
allowed to write it.**

**Forbidden (all break rail #1 / orphan `/ar/`):**

- ❌ `wp post create --post_type=guide_article` for the Arabic version (creates an
  **unlinked** post — no `trid` → orphan at `/ar/`, broken switcher).
- ❌ Any `INSERT`/`UPDATE` on `icl_translations` or `icl_translation_status`.
- ❌ Copying the EN post via SQL/duplicate and "pointing" it at Arabic.

**Allowed:**

- ✅ WPML "+" / Translation editor in wp-admin to **create** the twin.
- ✅ `wp post update <existing_ar_id>` + `update_post_meta` to **populate** a twin
  WPML already created and linked (content only — never creation, never linkage).

**Prerequisite for any of this (currently missing — §3/§9-A):** `guide_article`
must be set **Translatable** in WPML → *Post Types Translation*, and `topic` in
*Taxonomies Translation*. No flag, no "+", no twin.

---

## 6. Fallback when a guide's Arabic isn't done yet

**Goal: an Arabic reader never hits a broken or empty page.** With WPML, what
happens at an Arabic URL whose twin doesn't exist is governed by the
`guide_article` translation option (WPML → *Post Types Translation*). The two
choices map **directly** onto the held owner decision below:

| WPML option for `guide_article` | Missing-AR behavior | Maps to launch policy |
|---|---|---|
| **"Only show translated items"** (current house value for `post`/`page` = `1`) | Guide is **hidden** from `/ar/` archives and its `/ar/guide/<slug>` does not resolve to an AR page. No wrong-language content, but no AR entry at all until a twin exists. | **AR-complete gates launch** (Option A) |
| **"Use translation if available, or fall back to default language"** (`2`) | `/ar/guide/<slug>` **shows the EN original** in the AR shell. No broken/empty page — but it is EN content under an AR URL, so it **must be kept noindex (fenced)** to avoid wrong-language indexing. | **EN-fallback behind the fence** (Option B) |

> 🔓 **HELD — RATIFIED VALUE INCOMING (2026-06-29; do NOT set it yourself).**
> *Must guides be Arabic-complete to gate the public launch (Option A), or may they
> ship EN-fallback behind the fence (Option B)?*
> **Per Advisor (2026-06-29): leaning Option A ("only show translated"), consistent
> with D-160 (AR-perfect).** This is a **global WPML display setting affecting ALL
> AR surfaces, not just guides**, so **Bader sets it at the project level** (handed
> to Builder or Blog as a ratified value) — **Blog must NOT set the WPML display
> option itself, and it is NOT a per-guide setting.** Record the ruling in the
> central Decision Log and update this row when it lands.
>
> **This decision does not block twin creation — only fallback behavior.** Until it
> lands, build every AR twin **noindex-fenced** as planned (rail #4); the safe
> default that cannot leak wrong-language content is **Option A** (matches the
> current `post`/`page` house setting `1`).

---

## 7. Routing / URLs for `/ar/` guides — and the `/ar/en/` trap

**Verified live structure:** EN = **no prefix** (`/guide/<slug>/`), AR = **`/ar/`
prefix** (`/ar/guide/<slug>/`); WPML negotiation = **directories**; `/ar/` = 200.

**Rules to keep it correct:**

- **Keep EN as the no-prefix default.** WPML's *"Use directory for default
  language"* must stay **OFF**. If it ever gets turned ON, EN becomes `/en/…` and
  you can get stacked/`malformed` `/ar/en/…` paths in the language switcher,
  sitemaps, and cross-links. This is the documented trap from other lanes —
  guard it.
- **AR body internal links carry `/ar/`.** Write `/ar/place/…`, `/ar/<area>`,
  `/ar/category/…` — exactly as the existing Anosha AR draft already does. **Never
  hardcode `/en/`.** Never write a bare `/guide/…` inside AR prose (it would point
  the Arabic reader at English); use `/ar/guide/…`.
- **Let WPML own the switcher + canonical/hreflang.** Don't hand-build a language
  switcher or hardcode canonical/hreflang in the body — WPML emits them from the
  `trid` link. (This is also why the twin must be WPML-linked, not orphaned.)

> ⚠ **ACTIVE GATE — cross-module check in flight (§9-C, 2026-06-29):** the body
> shortcodes `[q8tly_place]` / `[q8tly_map]` resolve listing URLs **server-side at
> render**. On an `/ar/` page they must emit `/ar/place/…` — not `/place/…` (drops
> the AR prefix) and not `/ar/en/place/…` (double-prefix). Whether they are
> WPML-language-aware is a **Builder / Module 2** property, not Module 8's to fix.
> **Builder is running a read-only check now** (per Advisor); **Blog HOLDS
> twin-building until the finding is relayed.** If already AR-correct → Blog
> verifies on the first twin and closes it; if it drops/doubles the prefix → it's a
> real fix to scope *before* any twins are built.

---

## 8. Plain-body contract for AR (the gotcha that will bite)

The current staged AR drafts (e.g. `drafts/anosha-…_AR_…md`) are written in the
**old hand-built HTML chrome** format — `<figure>`/`<picture>`, a byline
blockquote, an inline hero `<img>`. **That format is incompatible with the guide
template**, which renders kicker / byline / hero / share / related itself.
Publishing it as-is **double-renders**.

**Before any AR twin is populated, convert the Arabic to the kit's contract**
(identical to EN — see `guide.template.md`):

- **Plain prose body**, no kicker/byline/hero/share/related/CTA.
- Images via the `[[image:STEM|caption]]` marker (and an `images/` folder for the
  AR drop if kit-assisted), **not** raw `<figure>`/`<picture>`.
- Listing card / map via `[[place]]` / `[[map]]` markers only.
- The kit's guardrail (`CHROME_FORBIDDEN`) will hard-fail on leftover chrome — a
  feature, not a bug.

> The Arabic *wording* in the existing drafts is good human translation — reuse
> the prose; **discard the HTML scaffolding**.

---

## 9. Open flags routed to Advisor (for the consistency check vs the listings model)

- **A. PREREQUISITE / global-state — RESOLVED 2026-06-29.** `guide_article` +
  `topic` + `guide_tag` are now WPML-Translatable (Builder flipped them via
  `wpml-config.xml` in the plugin root; D-145 guard intact — Translate-Everything
  OFF, no DeepL enrolment; confirmed via Advisor). The "+" twin button renders.
  Was "the one hard blocker"; now cleared — the active gate moved to flag C.
- **B. Stale docs reconcile — DONE 2026-06-29 (per Advisor canon).** S2-19's
  "AR publishing gated on WPML in production" is **pre-D-160 drift: incomplete, not
  a direct contradiction.** Current canon: WPML-on-prod is **necessary-but-not-
  sufficient**; AR-public also needs **AR-perfect (D-160) + owner track + D-157
  cutover + 7-G flip.** Patched in this lane (role-brief, README, calendar, runbook
  §3/§6). **Residual flag to Advisor:** my lane holds no S2-19 *source text* — only
  the paraphrase — so I can't confirm the spec literally says "WPML-on-prod = whole
  gate." If the central S2-19 text does say that, it contradicts D-160 and needs a
  central patch; otherwise this is just lane-doc drift, now fixed.
- **C. Shortcode language-awareness (Module 2 / Builder) — ACTIVE GATE.** Confirm
  `[q8tly_place]` / `[q8tly_map]` emit `/ar/place/…` on AR pages — never `/place/…`
  (dropped prefix) or `/ar/en/…` (doubled). **Builder is running a read-only check
  now (2026-06-29, per Advisor); Blog holds all twin-building until it returns.**
  Was "verify on the first twin"; promoted to a pre-build gate so we never build
  twins against a broken URL emitter (§7).
- **D. Kit gap.** `publish_guide.py` only *creates* (`wp post create`). For AR it
  must instead *populate an existing WPML-created twin* (`--into <ar_id>`,
  update-only). Until built, AR population is manual wp-admin. Worth building once
  §9-A clears. (No code written this pass — definition only.)
- **E. Held owner decision (§6).** AR-complete-to-launch (Option A) vs
  EN-fallback-behind-fence (Option B). Mapped to the concrete WPML setting; slot
  marked. Owner rules; record in the Decision Log.
- **F. Minor — calendar drift.** Two live guides
  (`keif-restaurant-al-kout-mall`, `vibes-coffee-roastery-al-kout-mall`) are not
  in `calendar/editorial-calendar.md`'s Published table. Not AR-related; noted for
  housekeeping.

- **G. RESOLVED-IN-PRACTICE 2026-06-29 (was a cross-module BLOCKER) — site WPML editor is ATE, not the WordPress editor.**
  First twin (2600) was created as a real editable WP draft via the WordPress-editor
  path while global `doc_translation_method` stayed **ATE** (listings keep DeepL).
  → guide twins ARE creatable now. **Open:** confirm with Builder the exact
  per-document/per-type mechanism so each guide repeats it (global is still ATE), or
  default `guide_article` to the WP editor. Original blocker writeup retained below.
  Verified 2026-06-29: `icl_sitepress_settings['translation-management']['doc_translation_method'] = ATE`.
  So clicking the WPML "+" on a guide routes into the **Advanced Translation Editor**:
  it reserves an empty `ar` slot in the trid but creates **no editable `guide_article`
  post** until an ATE translation is "completed" — and ATE owns the content via
  translation memory, which fights this lane's **human-AR-via-SSH populate** (and is
  the DeepL path we must not use for guides, D-145). **But ATE is global and the
  listings lane needs it for DeepL bulk AR**, so Blog must NOT flip
  `doc_translation_method`. **Need from Advisor/Builder:** a way for `guide_article`
  to be translated in the **native WordPress editor** (so "+" makes a real,
  SSH-editable AR draft) **while listings keep ATE/DeepL** — e.g. WPML's
  "translate some content with the WordPress editor" option, scoped to guides.
  Until resolved, **no guide AR twin can be created the rail-#1 way.** First "+"
  attempt on EN 2189 left a dangling empty `ar` slot in trid 4656 — cancel it via
  the WPML UI (Translation Management / the post's Language box), never by hand.

**Consistency note vs the listings model (for Advisor's check):** the listings
lane uses DeepL MT for bodies + controlled-term/area/name machinery; this lane
uses **human translation (D-145) and none of that machinery** — just an item and
its WPML twin (rails #2, #3). The two models are intentionally different; this
runbook does not import listings complexity.

---

## 10. Provenance / changelog

- **2026-06-28** — Created. Authored by Claude Blog (Module 8) on Advisor's
  orientation task. Verified against live staging over SSH:
  - WPML 4.9.5 active; default `en`, active `ar,en`; negotiation = directories;
    `/ar/` = HTTP 200.
  - `guide_article_sync = NOT SET`, `topic` tax `NOT SET`, `post`/`page` = `1`.
  - `anosha` 2189 has no WPML language record.
  - 6 guides live (4 in calendar + `keif-…`, `vibes-…`).
  - **Re-verify these before acting — WPML settings drift.**
- **2026-06-28** — Added §3.5 (AR Surface Mechanism Map): the cross-lane rule for
  which mechanism makes Arabic on each surface (listings/guides = twin via WPML;
  search/GD pages + filters/chrome = String Translation; archives = translated
  term). Recorded so Module 8 never twins a non-guide surface. Verified read-only
  in WPML 2026-06-28 (consistent with the §3/§10 staging audit).
- **2026-06-29** — **Flip landed.** Builder set `guide_article` + `topic` +
  `guide_tag` WPML-Translatable (D-145 guard intact), confirmed via Advisor → the
  AR-twin mechanism is UNBLOCKED and the "+" button renders. Updated §1/§3/§9-A.
  **New active gate = shortcode AR-URL emission check** (Builder, read-only) →
  §7/§9-C; **twin-building HELD until Advisor relays the finding.** S2-19 reconciled
  to current canon (necessary-but-not-sufficient; AR-public = D-160 + owner track +
  D-157 cutover + 7-G) → §3/§9-B, also patched in role-brief/README/calendar.
  Display-mode (§6): leaning Option A, ratified value to be set at project level —
  not by Blog, not per-guide. **No AR twins built this pass (correctly held).**
- **2026-06-29 (later)** — **First "+" attempt surfaced a cross-module BLOCKER (§9-G):**
  site WPML editor is **ATE** (`doc_translation_method=ATE`), so "+" routes to the
  Advanced Translation Editor and makes no editable AR post (only an empty trid slot
  on 2189/trid 4656; no DeepL fired). Can't flip ATE — listings need it. Routed to
  Advisor/Builder: enable WordPress-editor translation for `guide_article` only.
  Built+validated the charset-safe update-only populator `guide-kit/populate_ar_twin.py`
  (uncommitted, pending a clean run) — it correctly refuses while no real twin exists.
- **2026-06-29 (FIRST TWIN LIVE)** — §9-G resolved in practice: shell created
  editable via the WP-editor path (global stays ATE → listings keep DeepL). Populated
  **`guide_article` 2600** (twin of 2189) at `/ar/guide/anosha-beauty-salon-sabah-al-salem/`,
  **publish + noindex (fenced)**, via `populate_ar_twin.py` (now committed — proven
  clean). **First-twin proof PASSED:** guide body = 4 `/ar/places/`, 0 bare `/places/`
  → Builder's shortcode fix v1.14.175 confirmed on real AR content; 0 raw shortcodes;
  zero mojibake; hero+inline media reused (2190/2192/2193/2194); noindex present.
  (§9-D populator gap now filled, update-only.) Bare `/places/` seen only in global
  mega-menu chrome = untranslated category terms (Pipeline/Chrome backlog, not Blog).
  Pending: D-145 human review → owner sign-off → unfence.
- **2026-06-29 (policy + review)** — Bader clarified the unfence model: **per-guide
  unfence does NOT happen.** D-145 review is a **quality gate** (Arabic renders right);
  the twin stays `noindex` and unfences only at the **site-wide flip** (D-160 + owner
  track + D-157 cutover + 7-G). Rail #4 + Phase C corrected accordingly. D-145
  checklist for 2600 staged: `drafts/anosha-…_AR_2026-06-29_D145-REVIEW.md`. Two owner
  decisions pending: AR "Best for" list (prose vs bullets) + the deck line.
