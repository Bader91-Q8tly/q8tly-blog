#!/usr/bin/env python3
# One-off EN guide body re-inject (existing post; NO fence — EN stays indexable).
# Handles inline media + hero, like populate_ar_twin.py, but targets an explicit EN post.
# Usage: reinject_en.py <md> <post_id> --media inline-1=2359,...,hero=2358 [--execute]
import re, sys, json, html, subprocess
HERE = "/Users/baderalbussarah/Desktop/Q8tly Blog/guide-kit"
sys.path.insert(0, HERE)
import publish_guide as kit

def jx(s): return json.dumps(s if s is not None else "", ensure_ascii=False)

md, post_id = sys.argv[1], sys.argv[2]
execute = "--execute" in sys.argv
media = {}
for a in sys.argv:
    if a.startswith("--media="): a = a.split("=",1)[1]
mi = sys.argv.index("--media")+1 if "--media" in sys.argv else -1
if mi > 0:
    for pair in sys.argv[mi].split(","):
        if "=" in pair: k,v = pair.split("="); media[k.strip()] = v.strip()
cfg = kit.load_config(); host = cfg["SSH_HOST"]

raw = open(md, encoding="utf-8").read()
raw = re.sub(r"^﻿?\s*<!--.*?-->\s*", "", raw, count=1, flags=re.S)
fm, body = kit.parse_frontmatter(raw)
body = re.sub(r"<!--.*?-->", "", body, flags=re.S).strip()
map_ids = fm.get("map_ids") if isinstance(fm.get("map_ids"), list) else []
blocks, body_images = kit.md_to_blocks(body, fm.get("place_id"), map_ids)
wc = kit.word_count(body)

# HARD-VERIFY target = EN guide_article
vphp = (f"<?php $p={post_id};\n"
        'echo "type=".get_post_type($p)."\\n";\n'
        '$ld=apply_filters("wpml_post_language_details",null,$p);\n'
        'echo "lang=".($ld && isset($ld["language_code"])?$ld["language_code"]:"")."\\n";\n')
rc, info, err = kit.ssh(host, "wp eval-file -", inp=vphp)
d = dict(l.split("=", 1) for l in info.strip().splitlines() if "=" in l)
print("TARGET VERIFY:", d)
if d.get("type") != "guide_article": sys.exit(f"target {post_id} not a guide_article")
if d.get("lang") not in ("en", ""): sys.exit(f"target {post_id} lang={d.get('lang')} (want en)")

# Build inline image blocks from existing media (reuse; no upload)
final = blocks
for stem, cap in body_images:
    aid = media.get(stem, "")
    if not aid: sys.exit(f"no --media mapping for image stem '{stem}'")
    rc, url, _ = kit.ssh(host, f"wp post get {aid} --field=guid 2>/dev/null"); url = url.strip()
    alt = cap or fm["title"]
    cap_html = f'<figcaption class="wp-block-image__caption">{html.escape(cap)}</figcaption>' if cap else ""
    blk = (f'<!-- wp:image {{"id":{aid},"sizeSlug":"large","linkDestination":"none"}} -->\n'
           f'<figure class="wp-block-image size-large"><img src="{url}" alt="{html.escape(alt)}" '
           f'class="wp-image-{aid}"/>{cap_html}</figure>\n<!-- /wp:image -->')
    final = final.replace(f"<!--GUIDEKIT_IMG:{stem}|{cap}-->", blk)

hero = media.get("hero", "")
print(f"\n=== EN RE-INJECT post {post_id}  [{'EXECUTE' if execute else 'DRY RUN'}] ===")
print(f"title: {fm.get('title')}  place_id: {fm.get('place_id')}  words: {wc}  hero(reuse): {hero}")
print(f"images: {[(s,media.get(s)) for s,_ in body_images]}  | NO fence (EN indexable)")
if not execute:
    print("DRY RUN — no writes."); sys.exit(0)

bodyfile = f"/tmp/guidekit-en-{fm['slug']}-body.html"
subprocess.run(["ssh", "-o", "BatchMode=yes", host, f"cat > {bodyfile}"], input=final.encode("utf-8"), check=True)
php = f"""<?php
$id = {post_id};
if (get_post_type($id) !== 'guide_article') {{ echo "ERR=not a guide_article\\n"; exit; }}
$r = wp_update_post(array(
  'ID' => $id, 'post_status' => 'publish',
  'post_title' => {jx(fm['title'])}, 'post_name' => {jx(fm['slug'])},
  'post_excerpt' => '',
  'post_content' => file_get_contents({jx(bodyfile)}),
), true);
if (is_wp_error($r)) {{ echo "ERR=".$r->get_error_message()."\\n"; exit; }}
update_post_meta($id,'deck',{jx(fm.get('deck',''))});
update_post_meta($id,'word_count',{int(wc)});
update_post_meta($id,'hero_alt',{jx(fm.get('hero_alt',''))});
update_post_meta($id,'hero_caption',{jx(fm.get('hero_caption',''))});
$h = {int(hero) if str(hero).isdigit() else 0};
if ($h>0) {{ set_post_thumbnail($id,$h); update_post_meta($id,'hero_photo_id',$h); }}
echo "OK=".$id."\\n"; echo "URL=".get_permalink($id)."\\n"; echo "ST=".get_post_status($id)."\\n";
"""
rc, out, err = kit.ssh(host, "wp eval-file -", inp=php)
print(out.strip())
if "OK=" not in out: sys.exit(f"update failed: {err}")
kit.ssh(host, f'wp post update {post_id} --post_status=publish >/dev/null 2>&1; '
              f'wp eval "if(function_exists(\\"rocket_clean_domain\\")){{rocket_clean_domain();}}" >/dev/null 2>&1')
print("cache: touched + flushed")
