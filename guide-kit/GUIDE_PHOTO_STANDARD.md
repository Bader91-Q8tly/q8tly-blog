# Guide-Photo Qualification Standard — D-180 candidate (DRAFT, pending ratification)

> **Owner ruling (2026-07-05):** *A listing only becomes a guide if its photo set fits
> the guide frame cleanly; otherwise the guide is **DEFERRED** (the listing stays live)
> and we move to the next guide-ready business.* **Odachi = reference pass. B+F = the
> composition test case.** Status: DRAFT for ratification (Advisor → Decision Log, D-180).
> **Frame numbers below are Builder's landed values (2026-07-05, template v1.14.220).**

## 0. Intake gate — ASK THIS FIRST (owner rule, 2026-07-05)

**The first question on any guide is "Do the photos QUALIFY for guide/blog?" — NOT
"how do we fix this image?"** Photo qualification is a **gate at intake**, before any guide
is built. Stop opening fix-requests on photos that simply don't qualify.

**Step 1 — measure width FIRST.** The binding number is the **width available for a landscape
7:5 crop**:
- landscape-oriented source → its **long edge**;
- portrait source → its **short edge (width)** — a landscape crop is only ever as wide as the
  source width. *(B+F trap: long edge was 1448–1600 px but usable landscape width was only
  1086 px → it failed. Measure the landscape width, not just the long edge.)*

```bash
# quick screen: usable landscape-crop width for every source in a folder
for f in "<folder>"/*.{jpg,jpeg,png,webp}; do sips -g pixelWidth -g pixelHeight "$f"; done
```

**Step 2 — decide, then act:**
| Landscape width | Verdict | Action |
|---|---|---|
| **≥1520 px**, subject off edges, one ratio achievable | **PASS** | Build the guide; **Canva-fit to 7:5 (1520×1086)** where reframing is needed |
| **1200–1520 px** | **CONDITIONAL** | Canva-fit is fine; **flag if it looks tight** |
| **<1200 px**, or subject edge-to-edge, or portrait-only with no croppable landscape | **FAIL** | **Do NOT force the guide.** Keep the listing live; **DEFER**; move to a business with better photos |

**Canva reframes; it never upscales.** A low-res set is a **re-shoot, not a fix** — flag it and
move on. Do not spend cycles trying to crop, optimize, or Canva-fit a set that lacks the
pixels; that is a sourcing problem to route back, not a Blog framing task.

## 1. The frame numbers (Builder — landed)
- **Ratio:** landscape **1.4–1.6 : 1**. Ideal = **7:5 ≈ 1.407:1** (the frame's box).
- **Resolution:** **≥ 1200 px wide** (1520 px preferred).
- **One ratio per guide** — every photo in a guide (hero + body) shares the *same*
  aspect ratio. No mixing.
- **Portraits are disqualified** — **not for clipping** (v1.14.220 renders portraits
  *whole*), but for **rhythm**: a portrait shows up tall-and-narrow among the landscape
  frames and breaks the guide's visual flow. Guide photos must be landscape.

## 2. What v1.14.220 changed (so the standard targets the right thing)
The old failure mode was **clipping** — the template hard-cropped portraits and sliced the
subject (the Odachi/B+F "weird pictures"). **v1.14.220 fixed the clipping** (portraits now
render whole). So this standard is **no longer about anti-clipping**; it enforces
**landscape rhythm + resolution + one ratio** so the set reads as a clean, consistent
gallery. (The featured-image focal-point work is separately tracked in the 2026-07-05
crop-fix handoff.)

## 3. Qualification checklist (run per guide, BEFORE it publishes)

**A. Ratio & resolution (hard)**
- [ ] Every photo is **landscape 1.4–1.6:1** (ideal 7:5 = 1.407). No portraits.
- [ ] **One ratio across the whole set** (hero + all body photos identical).
- [ ] Every photo is **≥1200 px wide** (1520 preferred) *after* the landscape crop.
      ⚠ A portrait phone source only yields a landscape crop as wide as the source; a
      ~1080–1150 px portrait usually lands **under** 1200 → resolution fail.

**B. Composition (hard — this is the B+F test)**
- [ ] **Storefront/sign:** the business **name is fully legible and sits well** in the
      landscape frame — comfortably placed, not jammed to an edge, not competing with
      clutter. *A correct ratio does not save a badly-composed sign shot.*
- [ ] If no storefront works, a **food/setting hero is allowed only if intentional**,
      landscape-native, and clean (Keif/Vibes precedent).
- [ ] Body subjects (dish/detail) are **whole and intentionally in frame**; no competing
      brand dominating; workable exposure.

**C. Enough of them**
- [ ] ≥1 hero + ≥3 body photos that all clear A and B.

## 4. Outcome
- **All hard boxes tick → guide-ready.**
- **Portrait sources aren't automatically usable:** a landscape re-crop is a valid rescue
  **only if** the crop still clears ratio+resolution (≥1200 px) **and** the subject sits
  well. Note the crop in the ledger.
- **Any hard box fails and no crop rescues it → DEFER.** Listing stays live; guide flagged
  *"deferred pending better photo."* **"Needs a better photo / re-shoot" is a legitimate
  verdict** — a well-composed sign at too-low resolution, or a sign that can't be made to
  sit well, defers the guide. For an **already-published** guide, retire/hold is the
  **owner's** per-case call, not Blog's.

## 5. Quick reference
| Check | Bar |
|---|---|
| Orientation | Landscape only (portraits disqualified — rhythm) |
| Ratio | 1.4–1.6:1, ideal 7:5 (1.407); one ratio per guide |
| Width | ≥1200 px (1520 preferred), measured after the crop |
| Sign | Name legible **and well-composed** in the frame |
| Set size | ≥1 hero + ≥3 body, all clearing the above |
| Fail + no rescue | DEFER (listing stays live); published = owner's retire/hold call |
