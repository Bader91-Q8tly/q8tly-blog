# Briefing → Advisor → Builder — systemic featured-image cropping fix (guide/blog posts)

**From:** Claude Blog (Module 8 — Editorial / Guide). **To:** Advisor → relay to Builder
(Module 6, owns q8tly-core + the guide templates/CSS).
**Lane note:** the fix is **template/CSS in q8tly-core = Builder's code** (per
CLAUDE.md + GUIDE_AR_WORKFLOW §0a: "Builder owns the guide-system code; Blog owns content +
injection"; cross-lane code routes Advisor → ratified → Builder). Blog did the site-gate +
full diagnosis + this spec, and did **not** edit q8tly-core. Bader pasted the task into the
Blog session; routing it to its correct owner.

## 0. Site gate — PASS
`wp option get home/siteurl` = `https://staging-e1ff-baderlol44-pwgjm.wpcomstaging.com`,
blogname **Q8tly**. NOT alqurainai.com. Safe to proceed on staging.

## 1. Problem — confirmed, and it's systemic (not one post)
The featured image is cropped **differently in each context and center-anchored**, so the
subject (e.g. a venue sign) drifts to the edge or gets clipped. Verified on MizuMesa (a
guide whose hero was NOT pre-cropped by Blog):
- **Homepage featured card** (`.q8tly-guide-hero__photo`, 16:10): the MizuMesa sign's top is
  clipped — awkward.
- **Guide-single header** (`.q8tly-guide-single__hero-img`, 16:9): the same image crops the
  sign differently again.
(Screenshots in the session scratchpad: `home-desktop.png`, `mizumesa-header.png`.)

## 2. Root cause — a center-anchored DOUBLE crop with no focal point
The same source is cropped twice, both center-anchored:
1. **WP hard-crop at generation** — every registered size is `crop=true`
   (`includes/homepage.php:169-174`): `q8-hero` 1600×900 (16:9), `q8-latest` 800×450 (16:9),
   `q8-feat-tall` 800×1067 (3:4), etc. Hard-crop = center-cropped at upload; a subject that
   isn't dead-center is **already discarded before any CSS runs.**
2. **CSS re-crop at display** — `object-fit: cover` with **no `object-position`** on top,
   and the DISPLAY ratio often differs from the SOURCE ratio, so it crops a second time:
   - Guide-single hero: `guide.css:542-546` `aspect-ratio:16/9` (source q8-hero 16:9 → ok on
     desktop) but **16:10 on mobile** (§10 comment) → second crop.
   - Homepage featured guide hero: `guide.css:117-120` `aspect-ratio:16/10` desktop,
     `:399` `3/2` mobile — from a **16:9** `q8-hero` source → always a second crop.
   - Homepage "Latest" cards: `homepage.css:1054-1058` `--ekg-latest-photo-aspect:16/9`
     desktop / `:70` `3/2` mobile — `q8-latest` 16:9 source → mobile double-crops.
3. **No focal-point / `object-position` anywhere** — `grep -rniE 'object-position|focal|
   focus.?point'` over `assets/ includes/` returns **nothing**. Every crop defaults to
   center. There is no editor control to keep a subject in frame.

## 3. Recommended fix (Builder to implement in q8tly-core)
**A. Add focal-point → `object-position` (the core fix).** Classic theme, so WP's native
focal point isn't auto-applied. Add a per-guide **`hero_focus`** postmeta holding an
`object-position` value (e.g. `center`, `center top`, `50% 30%`); emit it inline on the
hero `<img>` and the card `<img>` in:
   - `includes/guide-single.php` (hero render, ~248-290, `q8tly_guide_responsive_photo`)
   - `includes/home-guide.php` (featured hero + `.q8-latest` card render, ~79/220-235)
   - `includes/guide-hub.php` (hub card, ~142-149)
   Default `center`; fall back gracefully when unset. **Blog↔Builder contract:** once
   `hero_focus` is read, the **guide-kit will set it per guide** (publish_guide.py /
   reinject_en.py frontmatter → meta) so editors nudge framing without touching photos.

**B. Stop the double-crop — align source ratio to display ratio.** Either (i) switch the
hero/card display ratios to **match the registered source** (make the featured hero 16:9 to
match `q8-hero`, not 16:10/3:2), or (ii) add a registered size per display ratio (e.g.
`q8-feat` 16:10) so each context serves a size at its own ratio. Pick one and apply
site-wide; document the chosen ratio per context.

**C. Prefer soft crops + CSS for the framed contexts.** Consider `crop=false` on the
featured sizes so the focal-point `object-position` (A) actually governs the crop, instead
of hard-cropping the subject away at generation. (Keep hard crop only where the ratio is
fixed and focal point is irrelevant.)

**D. Serve the right size per context (mostly already right).** Hero → `q8-hero`; cards →
`q8-latest`. Keep; just don't let a card pull the 1600px hero or stretch a small source.

## 4. QA checklist (Builder — the task's, restated)
- [ ] Correct site (Q8tly staging, not alqurainai.com) — Blog confirmed §0.
- [ ] Featured image correct on the landing-page card AND the blog header.
- [ ] Subject stays in frame (no clip); no stretch/distortion.
- [ ] Template-level — verified on **2–3 different posts**, not just B+F. Use MizuMesa
      (2362), Naranj (2251), Anosha (2189) — their heroes were NOT pre-cropped, so they
      expose the raw behavior. (B+F 2918 and Odachi 2800 are misleading — Blog already
      pre-cropped their heroes to 16:9, so they look fine regardless.)
- [ ] Correct image size served per context; checked desktop + mobile.

## 5. Context: Blog's per-guide pre-crop was a stopgap, not the fix
While shipping Odachi (2800) and B+F (2918), Blog hit this and worked around it in the
**content lane** by pre-cropping those heroes to 16:9 centered on the subject (the task
says "don't change the photos" — that's why it needs the template fix instead). Once Builder
lands A–C: existing pre-cropped guides still render fine, and **future guides won't need
manual pre-cropping** — the guide-kit sets `hero_focus` and the template respects it.

## Routing
Blog repo: this handoff is the record → **Advisor → Builder** (q8tly-core edit; Builder
commits). No code changed by Blog. When Builder lands it, Blog will wire `hero_focus` into
the guide-kit frontmatter as the agreed contract.
