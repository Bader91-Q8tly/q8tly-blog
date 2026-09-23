# → PIPELINE (via Advisor): listing 6443/6444 edited by Blog (2026-09-23): "Barfres" → "Bar Frès", Casual Dining + Upscale, non-smoking

**Heads-up: Blog wrote listing (`gd_place`) data, which is Pipeline's lane.** Done on Bader's explicit instruction
(same evening as the Bar Frès guides, 6589/6591), under the shared publish lock (`/tmp/q8tly-publish.lock`, taken
23:09:39 right after `-01` released it from Freej, released after verify). Same precedent as the Solange Maison rename
(`handoffs/2026-09-22-to-pipeline-solange-rename.md`).

## ⚖ Owner overrides of P-285 rulings (his later, specific instruction governs)
- **Title:** P-285 ruled `Barfres` ("their site's spelling"). Bader now: **`Bar Frès`**, slug kept `barfres`.
- **Subcategory:** P-285 ruled `Fine Dining` over the Casual lean. Bader now: **`Casual Dining` "for now"**, plus the
  **Upscale** tag ("the room is upscale, the format is casual").

## What changed (both twins, AR written first, EN last; guarded on the exact pre-state)
| | EN 6443 | AR 6444 |
|---|---|---|
| `post_title` + detail `post_title` | Barfres → **Bar Frès** (`C3A8` verified) | Barfres → **Bar Frès** (Latin, house rule) |
| detail `_search_title` | → `bar fres` (GD's `geodir_sanitize_keyword`) | → `bar fres` |
| `post_name` | **unchanged** `barfres` (passed explicitly) | **unchanged** `barfres` |
| `post_content`, name mention only | "Barfres is a…" → "Bar Frès is a…" | «Barfres مطعم…» → «Bar Frès مطعم…» |
| categories | 1487 + **1494 Casual Dining** (was 1488 Fine Dining) | 1894 + **1703 مطاعم عائلية بسيطة** (was 2028) |
| detail `post_category` | `,1487,1494,` (default 1487 kept) | `,1894,1703,` (default 1894 kept) |
| tags | −1675 Family-Friendly, **+1862 Upscale** | −2019 مناسب للعائلات, **+1920 فاخر** |
| detail `post_tags` | `Japanese,French,Date Night,Group-Friendly,Upscale` | `ياباني,فرنسي,أجواء رومانسية,مناسب للمجموعات,فاخر` |
| `smoking` (field 97, per-side) | null → **`non-smoking`** | null → **`non-smoking`** |
| gallery titles (alt text + JSON-LD image names) | 8 gd rows + 8 WP attachments "Barfres N" → "Bar Frès N" | 1 gd row, same |

- **Fields-win-over-tags respected:** "No smoking" went into the Smoking **field** (`non-smoking`), not a tag. Upscale
  and Family-Friendly are registered tag pairs (register pairs[251], [74]), so there's **no NEW-VOCAB**.
- **Not touched:** hours (EN `business_hours` byte-identical before and after; still Mo–Su 11:00–22:00, Bader is
  confirming the close with the restaurant), photos, badge, amenities, price, payment, seating, location,
  website/IG/phone, statuses.
- Written with `wp_update_post` + `wp_set_object_terms`/`wp_remove_object_terms` + a direct `$wpdb->update` of the
  detail row (GD's save path NOT used, per your rule 7).

## Verified
Read-back of all columns on both twins · **`publish_check.py 6443` = 13 PASS / 0 WARN / 0 FAIL** (T8 status parity
both twins, T7 AR side-table 7 = EN 7) · served 200 on both URLs (unchanged) · H1 "Bar Frès", `<title>` «Bar Frès —
Kuwait City | Restaurants» / «Bar Frès، مدينة الكويت | مطاعم» · "Smoking: Non-smoking" / «التدخين: ممنوع التدخين» ·
Upscale/فاخر shown, Family-Friendly/مناسب للعائلات gone · **0 "Barfres" left** outside file/slug paths · term counts moved
by exactly one: Fine Dining 12→11, Casual Dining 39→40, Family-Friendly 30→29, Upscale 1→2. Purged: cache flush +
Rocket + edge `--domain`.

## For Pipeline to sync (Blog did NOT touch your repo)
- **MASTER_LISTINGS.xlsx / register:** title, subcategory, tags and smoking for this pair. If anything re-syncs 6443/6444
  from source, it will **revert** these unless the source is updated. Register tag counts (`n`) for 1675/2019 and 1862/1920
  moved.
- **Photo provenance correction (Bader, 2026-09-23):** the storefront `AC25D4FA…` is **our blogger's own photo, with
  people removed by AI for privacy**. That's allowed under the photo rule: *people may be removed or blurred; the venue itself
  must not be changed*. P-285 excluded it as "screenshot crop + Apple Clean Up edit" and P-292 recorded its use as an owner
  override. Per Bader it was never a violation, so please correct the P-285/P-292 wording. The XMP
  (`compositeWithTrainedAlgorithmicMedia`, `Credit=Apple Photos Clean Up`) is what a privacy removal leaves behind, so
  it isn't evidence against a photo on its own.

## Provenance
Backup `prod-20260923-230939.sql.gz` (canon `db-snapshot.sh`, gzip-tested, dump-complete), taken under the lock, before
the write. Logged in `guide-kit/BACKUP_LOG.md`.
