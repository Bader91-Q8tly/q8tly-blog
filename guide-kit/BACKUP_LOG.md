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
