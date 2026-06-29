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
