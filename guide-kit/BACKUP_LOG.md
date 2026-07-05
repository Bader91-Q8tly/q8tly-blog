# Backup Verification Log — guide-kit

Every WP write (SQL/SFTP write-class) gets a verified DB snapshot first. Staging
is the same write-class as production, so the discipline applies now.
`publish_guide.py --execute` appends a row automatically before it writes.

| timestamp (server) | action | snapshot file (`q8tly-db-snapshots/`) | size | env |
|---|---|---|---|---|
| 20260621-062135 | guide-kit baseline (post-Anosha state) | `staging-20260621-062135-guidekit-baseline.sql.gz` | 1.6M | staging |

> Note: the first Anosha publish (guide_article 2189 create, Page 2185 trash,
> Rank Math 301, gd_place 2147 photo) was done **before** this kit existed — no
> per-write snapshot was taken at the time (process gap, logged honestly). The
> baseline above captures the resulting good state as the restore point.
| 20260621-235456 | publish guide `naranj-salmiya` | `staging-20260621-235456-guide-naranj-salmiya.sql.gz` | 1678692 B | staging |
| 20260623-203957 | publish guide `south-avenue-salon-sabah-al-salem` | `staging-20260623-203957-guide-south-avenue-salon-sabah-al-salem.sql.gz` | 1725240 B | staging |
| 20260624-165707 | internal-link guides 2189/2251/2339 (district+category) | `staging-20260624-165707-internal-links-guides.sql.gz` | 1683164 B | staging |
| 20260624-182816 | publish guide `mizumesa-sharq` | `staging-20260624-182816-guide-mizumesa-sharq.sql.gz` | 1706283 B | staging |
| 20260629-141843 | populate AR twin `anosha-beauty-salon-sabah-al-salem` (post 2600) | `staging-20260629-141843-ar-twin-anosha-beauty-salon-sabah-al-salem.sql.gz` | 2330238 B | staging |
| 20260629-160503 | populate AR twin `naranj-salmiya` (post 2612) | `staging-20260629-160503-ar-twin-naranj-salmiya.sql.gz` | 2387278 B | staging |
| 20260629-161150 | populate AR twin `mizumesa-sharq` (post 2618) | `staging-20260629-161150-ar-twin-mizumesa-sharq.sql.gz` | 2399728 B | staging |
| 20260629-161624 | populate AR twin `keif-restaurant-al-kout-mall` (post 2630) | `staging-20260629-161624-ar-twin-keif-restaurant-al-kout-mall.sql.gz` | 2406675 B | staging |
| 20260629-195339 | populate AR twin `vibes-coffee-roastery-al-kout-mall` (post 2634) | `staging-20260629-195339-ar-twin-vibes-coffee-roastery-al-kout-mall.sql.gz` | 2399939 B | staging |
| 20260629-195856 | populate AR twin `south-avenue-salon-sabah-al-salem` (post 2619) | `staging-20260629-195856-ar-twin-south-avenue-salon-sabah-al-salem.sql.gz` | 2405034 B | staging |
| 20260630-144914 | populate AR twin `mizumesa-sharq` (post 2618) | `staging-20260630-144914-ar-twin-mizumesa-sharq.sql.gz` | 2418855 B | staging |
| 20260630-152141 | populate AR twin `mizumesa-sharq` (post 2618) | `staging-20260630-152141-ar-twin-mizumesa-sharq.sql.gz` | 2419189 B | staging |
| 20260630-174154 | mizumesa tower fix (KIPCO→Al-Shaheed) PRE-write, EN 2362 + AR 2618 | `staging-20260630-174154-mizumesa-tower-fix-pre.sql.gz` | 2413440 B | staging |
| 20260630-174441 | populate AR twin `mizumesa-sharq` (post 2618) | `staging-20260630-174441-ar-twin-mizumesa-sharq.sql.gz` | 2414762 B | staging |
| 20260701-200653 | EN neutral re-author `naranj-salmiya` (post 2251) — **snapshot taken POST-write** | `staging-20260701-200653-guide-naranj-salmiya-en-reinject-post.sql.gz` | 2412054 B | staging |

> Note: `reinject_en.py` has no built-in pre-write backup step (unlike
> `publish_guide.py` / `populate_ar_twin.py`, which both snapshot automatically).
> The 2026-07-01 Naranj EN reinject ran before this was caught — snapshot above
> was taken immediately after, capturing the resulting state (process gap,
> logged honestly, same pattern as the original Anosha gap above). Restore point
> for pre-reinject state is the prior row (`20260624-165707`, internal-link
> guides snapshot) if a rollback is ever needed. Flagging `reinject_en.py`'s
> missing backup step as a kit gap worth closing.
>
> **CLOSED 2026-07-01.** `reinject_en.py` formalized: it now snapshots
> automatically before every write (`staging-<ts>-en-guide-<slug>.sql.gz`,
> logged here just like `populate_ar_twin.py`), same backup → update → verify
> discipline as the AR tool. No more manual pre-write snapshots needed for EN
> re-authors going forward — see the `20260701-2032xx` row below (auto-logged
> by the tool itself, no manual step).
| 20260701-200804 | populate AR twin `naranj-salmiya` (post 2612) | `staging-20260701-200804-ar-twin-naranj-salmiya.sql.gz` | 2412932 B | staging |
| 20260701-201848 | EN neutral re-author `anosha-beauty-salon-sabah-al-salem` (post 2189) — PRE-write, manual (closes the `reinject_en.py` gap logged above) | `staging-20260701-201848-guide-anosha-en-reinject-pre.sql.gz` | 2416341 B | staging |
| 20260701-202059 | populate AR twin `anosha-beauty-salon-sabah-al-salem` (post 2600) | `staging-20260701-202059-ar-twin-anosha-beauty-salon-sabah-al-salem.sql.gz` | 2410654 B | staging |
| 20260701-202945 | EN re-author `mizumesa-sharq` (post 2362) | `staging-20260701-202945-en-guide-mizumesa-sharq.sql.gz` | 2415136 B | staging |
| 20260701-203207 | EN re-author `mizumesa-sharq` (post 2362) | `staging-20260701-203207-en-guide-mizumesa-sharq.sql.gz` | 2415596 B | staging |
| 20260703-100324 | pillar-card tagging: `menu_feature=1` on `mizumesa-sharq` (2362, food-drink) + `anosha-beauty-salon-sabah-al-salem` (2189, health-beauty-fitness) — PRE-write | `staging-20260703-100324-menu-feature-tagging-pre.sql.gz` | 2456744 B | staging |
| 20260704-183756 | publish guide `odachi-kuwait-city` | `staging-20260704-183756-guide-odachi-kuwait-city.sql.gz` | 2469188 B | staging |
| 20260704-190246 | populate AR twin `odachi-kuwait-city` (post 2808) | `staging-20260704-190246-ar-twin-odachi-kuwait-city.sql.gz` | 2482298 B | staging |
| 20260704-200746 | EN re-author `odachi-kuwait-city` (post 2800) | `staging-20260704-200746-en-guide-odachi-kuwait-city.sql.gz` | 2497965 B | staging |
| 20260704-200917 | populate AR twin `odachi-kuwait-city` (post 2808) | `staging-20260704-200917-ar-twin-odachi-kuwait-city.sql.gz` | 2497796 B | staging |
| 20260704-215916 | publish guide `bandf-360-mall` | `staging-20260704-215916-guide-bandf-360-mall.sql.gz` | 2540755 B | staging |
| 20260704-223255 | populate AR twin `bandf-360-mall` (post 2924) | `staging-20260704-223255-ar-twin-bandf-360-mall.sql.gz` | 2555075 B | staging |
| 20260705-112345 | EN re-author `mizumesa-sharq` (post 2362) | `staging-20260705-112345-en-guide-mizumesa-sharq.sql.gz` | 2594761 B | staging |
| 20260705-112512 | populate AR twin `mizumesa-sharq` (post 2618) | `staging-20260705-112512-ar-twin-mizumesa-sharq.sql.gz` | 2596180 B | staging |
