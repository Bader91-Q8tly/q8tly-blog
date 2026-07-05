# Briefing → Advisor → Pipeline — listing gaps for Elysee Beauty Lounge + Queue Café

**From:** Claude Blog (Module 8). **To:** Advisor → relay to **Pipeline** (owns `gd_place`).
**Why routed:** these are **listing (gd_place) data gaps**, not guide/Blog scope. The combined
guide is live and unaffected (EN `guide_article` **3115**, AR fenced **3122**; both place cards
resolve to the listings). This is about completing the two **listings** the cards point to.
**Not a Blog task** — Blog can't invent listing data (no-fabrication rule); Pipeline sources it.

## Queue Café — `gd_place` 3067 (`/places/mahboula/queue-cafe/`)
- **⚠ No phone.** The intake's phone field held "10am–8pm" (visitor put hours there) → no
  actual number. Needed.
- **⚠ Coordinates / Maps pin missing.** "24th floor, Park Inn by Radisson, Mahboula" is the
  display address only; the stored pin / Directions button needs lat-long.
- **Hours to confirm.** 10:00 AM – 8:00 PM is staff-stated (recovered from the phone field);
  the raw daypart ticks (Breakfast + Late-night = Yes, Lunch/Dinner = No) don't square with
  10–8. Reconcile.
- **AR business name** — "Queue Café" renders Latin (كيو كافيه in title only). Confirm.
- **New-vocab tags to register** (stored labels): `Women-Only`, `Sea View`, `Rooftop`.
- **Hotel/venue composer** treatment to confirm (venue displayed as "Park Inn by Radisson,
  Mahboula — 24th floor").

## Elysee Beauty Lounge — `gd_place` 3066 (`/places/mahboula/elysee-beauty-lounge/`)
**Thin listing — the intake was ~90% café.** Has the shared-premises facts (women-only, valet,
24th floor, the café pairing) but **no salon-specific data at all:**
- **⚠ Services / treatments — none.** The core of any Beauty listing. Blocker for a full listing.
- **⚠ Salon hours / price / phone — unknown** (the 10–8 and 10 KD are café-side, not the salon's).
- **`price_range $$`** was set to match the café (a per-person café figure, not a treatment
  price) — reconfirm at salon intake.
- **AR business name** — إليزيه likely; confirm official branding.
- `Sea View` / `Rooftop` deliberately withheld for the salon (café-specific unless Pipeline
  confirms the salon shares the view).
- **Needs its own salon Quick Visit Pack** to become a full listing.

## Priority
- **Blocks a full listing:** Queue's phone + coordinates; Elysee's services/hours/price/phone.
- **Confirm/register (non-blocking):** hours-daypart reconcile, AR names, the new-vocab tags,
  the salon price/view questions.
- **Not blocking the guide** — 3115/3122 stay live either way; this only improves the listings.

## Routing
Blog repo: this handoff is the record → **Advisor → Pipeline**. No `gd_place` writes by Blog.
