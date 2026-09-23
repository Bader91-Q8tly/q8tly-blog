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
| 20260705-205507 | publish guide `elysee-queue-cafe-mahboula` | `staging-20260705-205507-guide-elysee-queue-cafe-mahboula.sql.gz` | 2622783 B | staging |
| 20260705-224728 | populate AR twin `elysee-queue-cafe-mahboula` (post 3122) | `staging-20260705-224728-ar-twin-elysee-queue-cafe-mahboula.sql.gz` | 2614121 B | staging |
| 20260812-092224 | PRE-WRITE snapshot, prod (canon `q8tly-core/bin/db-snapshot.sh prod`) | `prod-20260812-092224.sql.gz` | 2914576 B | **prod** |
| 20260812-092325 | publish guide `cure-shuwaikh` (post 5025) — FIRST BLOG WRITE TO PROD | `prod-20260812-092325-guide-cure-shuwaikh.sql.gz` | 2928144 B | **prod** |

> ⚠ **Kit bug (found 2026-08-12, first prod run):** `publish_guide.py` hardcodes the `staging`
> label in both the dump filename and this log's env column (`publish_guide.py` §1 backup —
> `f"staging-{ts}-guide-{slug}.sql.gz"` and the literal `| staging |`). On the Cure run it
> wrote a **prod** dump named `staging-…`. Renamed to `prod-20260812-092325-…` and re-verified
> (gzip OK + `Dump completed` marker). **Fix owed:** derive the label from the resolved
> `--ssh-host`/env, not a literal — otherwise every future prod run mislabels its own audit
> trail. Same fix likely needed in `reinject_en.py` / `populate_ar_twin.py`.
| 20260812-094928 | EN caption fix `cure-shuwaikh` (post 5025) — inline-2 "A beef plate" → "Short Ribs Donburi" | `prod-20260812-094928-en-guide-cure-shuwaikh.sql.gz` | 2942117 B | **prod** |

> ⚠ **Same mislabel bug CONFIRMED in `reinject_en.py`** (2026-08-12): it too hardcodes
> `staging-` in the dump filename and `| staging |` in this log. Renamed + re-verified by
> hand again. The fix is one shared helper across all three tools (`publish_guide.py`,
> `reinject_en.py`, `populate_ar_twin.py`) — derive the env label from the resolved SSH host.
| 20260812-031047 | populate AR twin `cure-shuwaikh` (post 5032) | `staging-20260812-031047-ar-twin-cure-shuwaikh.sql.gz` | 2925444 B | staging |
| 20260813-075517 | publish guide `solange-maison-kuwait-city` | `prod-20260813-075517-guide-solange-maison-kuwait-city.sql.gz` | 3040960 B | prod |
| 20260813-081514 | populate AR twin `solange-maison-kuwait-city` (post 5436) | `prod-20260813-081514-ar-twin-solange-maison-kuwait-city.sql.gz` | 3056439 B | prod |
| 20260813-082925 | populate AR twin `solange-maison-kuwait-city` (post 5436) | `prod-20260813-082925-ar-twin-solange-maison-kuwait-city.sql.gz` | 3058849 B | prod |
| 20260813-131544 | EN re-author `cure-shuwaikh` (post 5025) | `prod-20260813-131544-en-guide-cure-shuwaikh.sql.gz` | 3055406 B | prod |
| 20260813-131901 | populate AR twin `cure-shuwaikh` (post 5032) | `prod-20260813-131901-ar-twin-cure-shuwaikh.sql.gz` | 3058384 B | prod |
| 20260813-132128 | populate AR twin `cure-shuwaikh` (post 5032) | `prod-20260813-132128-ar-twin-cure-shuwaikh.sql.gz` | 3060311 B | prod |
| 20260813-132234 | populate AR twin `solange-maison-kuwait-city` (post 5436) | `prod-20260813-132234-ar-twin-solange-maison-kuwait-city.sql.gz` | 3061173 B | prod |
| 20260813-132352 | EN re-author `solange-maison-kuwait-city` (post 5430) | `prod-20260813-132352-en-guide-solange-maison-kuwait-city.sql.gz` | 3061773 B | prod |
| 20260922-145424 | publish guide `best-restaurants-in-kuwait` | `prod-20260922-145424-guide-best-restaurants-in-kuwait.sql.gz` | 3245281 B | prod |
| 20260922-185639 (local UTC+3 = 15:56 server) | pre-write snapshot: create AR twin shell for `best-restaurants-in-kuwait` (EN 6307) | `prod-20260922-185639.sql.gz` | 3.1 MB | prod |
| 20260922-155801 | populate AR twin `best-restaurants-in-kuwait` (post 6309) | `prod-20260922-155801-ar-twin-best-restaurants-in-kuwait.sql.gz` | 3254621 B | prod |
| 20260922-170719 | publish guide `best-italian-restaurants-in-kuwait` | `prod-20260922-170719-guide-best-italian-restaurants-in-kuwait.sql.gz` | 3267309 B | prod |
| 20260922-212041 (local UTC+3) | pre-write snapshot: create AR twin shell for `best-italian-restaurants-in-kuwait` (EN 6313) | `prod-20260922-212041.sql.gz` | 3.1 MB | prod |
| 20260922-182140 | populate AR twin `best-italian-restaurants-in-kuwait` (post 6315) | `prod-20260922-182140-ar-twin-best-italian-restaurants-in-kuwait.sql.gz` | 3278760 B | prod |
| 20260922-183043 | populate AR twin `best-italian-restaurants-in-kuwait` (post 6315) | `prod-20260922-183043-ar-twin-best-italian-restaurants-in-kuwait.sql.gz` | 3291707 B | prod |
| 20260922-183444 | populate AR twin `best-italian-restaurants-in-kuwait` (post 6315) | `prod-20260922-183444-ar-twin-best-italian-restaurants-in-kuwait.sql.gz` | 3293009 B | prod |
| 20260922-190546 | populate AR twin `best-restaurants-in-kuwait` (post 6309) | `prod-20260922-190546-ar-twin-best-restaurants-in-kuwait.sql.gz` | 3293576 B | prod |
| 20260922-192933 | EN re-author `best-restaurants-in-kuwait` (post 6307) | `prod-20260922-192933-en-guide-best-restaurants-in-kuwait.sql.gz` | 3295968 B | prod |
| 20260922-193037 | populate AR twin `best-restaurants-in-kuwait` (post 6309) | `prod-20260922-193037-ar-twin-best-restaurants-in-kuwait.sql.gz` | 3299229 B | prod |
| 20260923-225612 (local UTC+3) | pre-write snapshot: publish EN guide `bar-fres-arraya-centre` + create its AR twin shell | `prod-20260923-225612.sql.gz` | 3.2 MB | prod |
| 20260923-195646 | publish guide `bar-fres-arraya-centre` | `prod-20260923-195646-guide-bar-fres-arraya-centre.sql.gz` | 3367120 B | prod |
| 20260923-225758 (local UTC+3) | pre-write snapshot: create AR twin shell for `bar-fres-arraya-centre` (EN 6589, trid 6699) | `prod-20260923-225758.sql.gz` | 3.2 MB | prod |
| 20260923-195920 | populate AR twin `bar-fres-arraya-centre` (post 6591) | `prod-20260923-195920-ar-twin-bar-fres-arraya-centre.sql.gz` | 3376921 B | prod |
