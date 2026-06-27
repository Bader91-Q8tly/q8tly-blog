# Guide → Arabic (AR) Twin — Standing Workflow Runbook

> **Module 8 (Editorial / Guide).** The single, repeatable procedure for giving
> any guide its Arabic version. **Read this FIRST** whenever Bader hands over a
> new guide or says "add Arabic." It pairs with **`guide-kit/README.md`** (the
> EN publishing kit) — that one ships English; this one defines the EN→AR
> lifecycle and how the Arabic twin is made.
>
> Source of truth for the AR side. Last verified against live staging:
> **2026-06-28** (see §10). When you act, re-verify the WPML state — settings
> drift.

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
  4. PREREQUISITE (one-time, currently MISSING): guide_article + topic must be
     WPML-Translatable.  -> NOT set yet. Route to Advisor (§3, §9-A). Until done,
     there is no "+" twin button and AR cannot be created the sanctioned way.
  5. Stage the human Arabic in drafts/<slug>_AR_<date>.md, converted to the
     kit's PLAIN-body + markers format (§8 — current AR drafts are old HTML chrome).
  6. In wp-admin, on the EN guide, click WPML "+" next to Arabic to create the
     LINKED AR twin (§5). NEVER `wp post create` an AR guide. NEVER touch icl_*.
  7. Paste/populate the reviewed AR body + meta into that twin; keep it noindex
     (fenced). Human review (D-145) -> owner sign-off -> unfence (§ Phase C).

If unsure which step you're at: EN is unblocked; AR is blocked on step 4.
```

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
4. **Arabic stays fenced (noindex) until signed off, then unfenced on owner
   review.** An AR twin does not go public the moment it exists. It is created
   noindex/draft → human review → **owner sign-off flips it to indexable**. The
   site-wide fence (prod `blog_public=0` / noindex) is a separate, higher launch
   gate owned by Advisor; the per-twin fence (Rank Math robots on the AR post) is
   ours.

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
| `guide_article` translatable in WPML | **NO — `guide_article_sync = NOT SET`** ⛔ |
| `topic` taxonomy translatable | **NO — `NOT SET`** |
| `post` / `page` translatable | yes, both = `1` ("only show translated items") |
| `anosha` (2189) language record | **none** — WPML doesn't track it (because the CPT isn't translatable) |

**The real blocker is NOT "WPML isn't installed." It is: the `guide_article` CPT
(and the `topic` taxonomy) are not set Translatable in WPML.** Until that flag is
flipped, **the WPML "+" twin button does not appear on guides** and there is no
rail-#1-honoring way to create an AR guide. Enabling EN→AR on `post` does nothing
for us — translatability is per post type (§0).

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

> Note for Advisor: because WPML *is* on staging (contradicting the handoff), the
> exact current scope of S2-19 should be reconciled centrally — is the gate
> "WPML on prod" only, or also "guide_article made translatable"? See §9.

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

### Phase C — review → unfence (owner-gated)

1. **Human review** of the Arabic (accuracy, tone, RTL, links). D-145 means a
   human signs the translation off — not a machine, not us asserting it.
2. **Owner sign-off** (Bader). Only then:
3. **Unfence:** flip the AR twin's Rank Math robots from noindex to **index**,
   set `post_status=publish`, touch + flush.
4. **Update** `calendar/editorial-calendar.md` (AR column → live) and write a
   `/handoffs` note.

> Reminder: the **site-wide** public flip (prod `blog_public`/noindex off,
> production WPML) is Advisor/launch territory and is a *higher* gate than this
> per-twin unfence. Don't conflate them.

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

> 🔓 **HELD — OWNER DECISION PENDING (do not decide here; Advisor/Bader rule).**
> *Must guides be Arabic-complete to gate the public launch, or may they ship
> EN-fallback behind the fence at launch?*
> **→ When the owner rules, implement it by setting the `guide_article`
> translation option above (Option A = "only show translated", Option B =
> "fallback to default + keep fenced/noindex").** Record the ruling in the
> central Decision Log and update this row.
>
> Until the ruling lands, the safe default that cannot leak wrong-language
> content is **Option A** (hide untranslated) — matching the current `post`/`page`
> house setting (`1`). Whatever is chosen, rail #4 (fenced until sign-off) still
> applies to every individual AR twin.

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

> ⚠ **Cross-module flag (§9-C):** the body shortcodes `[q8tly_place]` /
> `[q8tly_map]` resolve listing URLs **server-side at render**. On an `/ar/` page
> they must emit `/ar/place/…` — not `/place/…` (English under an AR page) and
> not a malformed `/ar/en/place/…`. Whether they are WPML-language-aware is a
> **Builder / Module 2** property, not Module 8's to fix. **Verify on the first
> real AR twin** and route any malformation to Advisor.

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

- **A. PREREQUISITE / global-state — `guide_article` + `topic` are not WPML
  Translatable.** This is the one hard blocker for AR guide twins. Flipping it is
  a WPML/site-config change (cross-module). **Decision/owner needed:** who flips
  it and when (Builder/Module 6?). Nothing AR can proceed until then.
- **B. Stale docs reconcile.** The role-brief / calendar / Anosha handoff say
  "WPML not active on staging" / "gated on WPML in production." **Reality: WPML
  4.9.5 is live on staging** (EN no-prefix, AR `/ar/` = 200). Please reconcile
  **S2-19's exact current meaning** centrally (is the gate "WPML on prod," or
  also "guide_article made translatable," or "+ human review + unfence"?). I have
  written this runbook to ground truth and flagged, not silently rewritten, the
  decision IDs.
- **C. Shortcode language-awareness (Module 2 / Builder).** Confirm
  `[q8tly_place]` / `[q8tly_map]` emit `/ar/place/…` on AR pages and never
  `/ar/en/…`. Verify on the first AR twin (§7).
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
