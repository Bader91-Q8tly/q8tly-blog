# guide-kit/config.sh — WHERE guides publish. Single source of truth.
# Staging now (production is frozen until cutover — swap these two at cutover).
#
# publish_guide.py reads these (or override with --ssh-host / --site-url / env
# GUIDEKIT_SSH_HOST, GUIDEKIT_SITE_URL).

SSH_HOST="staging-e1ff-baderlol44-pwgjm.wordpress.com@ssh.wp.com"
SITE_URL="https://staging-e1ff-baderlol44-pwgjm.wpcomstaging.com"

# Locked `topic` taxonomy slugs on guide_article (assign exactly one as primary):
#   food-drink | neighborhoods | culture-heritage | seasonal
# article_type set: longread | guide | quick_take

# Where DB backups are written before any WP write (created by the runbook):
BACKUP_DIR="/Users/baderalbussarah/Desktop/q8tly-db-snapshots"
