#!/usr/bin/env python3
r"""
populate_ar_twin.py — populate an EXISTING WPML-created AR twin of a guide_article.

UPDATE-ONLY. This NEVER creates a post (rail #1: the AR twin shell is created only
by WPML's "+ add translation" in wp-admin). It refuses to run unless a linked AR
twin already exists, discovered via WPML from the EN guide id.

Charset-safe for Arabic: body is streamed as UTF-8 bytes to a temp file and read
with file_get_contents(); all meta/title use json.dumps(ensure_ascii=False) so PHP
stores real UTF-8 (the kit's create path uses ensure_ascii=True → \uXXXX mojibake;
that's the CHARSET trap this avoids).

Usage:
  python3 populate_ar_twin.py <ar_draft.md> --en-id 2189 \\
      --media inline-1=2192,inline-2=2193,inline-3=2194,hero=2190 \\
      [--ar-id N] [--draft] [--execute]
Default = DRY RUN (discovers + validates the twin, prints the plan, no writes).
"""
import argparse, html, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import publish_guide as kit  # reuse parse_frontmatter, md_to_blocks, word_count, ssh, load_config


def die(m):
    print(f"\n❌ {m}\n", file=sys.stderr); sys.exit(1)


def jx(s):
    """JSON-encode for embedding in PHP, KEEPING Arabic as real UTF-8 (no \\uXXXX)."""
    return json.dumps(s if s is not None else "", ensure_ascii=False)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--en-id", required=True, help="EN guide_article id (twin source)")
    ap.add_argument("--ar-id", default=None, help="override; else auto-discovered via WPML")
    ap.add_argument("--media", default="", help="stem=attachment,... (e.g. inline-1=2192,hero=2190)")
    ap.add_argument("--draft", dest="keep_draft", action="store_true", help="leave post_status=draft (default: publish + noindex, so the /ar/ page renders for the first-twin proof)")
    ap.add_argument("--execute", action="store_true")
    args = ap.parse_args()

    cfg = kit.load_config()
    host = cfg["SSH_HOST"]
    site = cfg["SITE_URL"].rstrip("/")
    if not host:
        die("no SSH_HOST in config.sh")

    media = {}
    for pair in [p for p in args.media.split(",") if p.strip()]:
        k, v = pair.split("="); media[k.strip()] = v.strip()

    raw = open(args.draft, encoding="utf-8").read()
    raw = re.sub(r"^﻿?\s*<!--.*?-->\s*", "", raw, count=1, flags=re.S)  # allow a leading HTML comment before the frontmatter
    fm, body = kit.parse_frontmatter(raw)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S).strip()  # drop any remaining comments
    if fm.get("lang") != "ar":
        die("draft lang is not 'ar'")
    for bad in kit.CHROME_FORBIDDEN:
        if bad.lower() in body.lower():
            die(f"body contains chrome '{bad}'")

    place_id = fm.get("place_id")
    map_ids = fm.get("map_ids") if isinstance(fm.get("map_ids"), list) else ([fm["map_ids"]] if fm.get("map_ids") else [])
    blocks, body_images = kit.md_to_blocks(body, place_id, map_ids)
    wc = kit.word_count(body)

    # ── discover + HARD-VERIFY the linked AR twin (never touch EN, never an orphan) ──
    en = str(args.en_id)
    if args.ar_id:
        ar = str(args.ar_id)
    else:
        disc = f'<?php echo (int)apply_filters("wpml_object_id",{en},"guide_article",false,"ar");'
        rc, out, err = kit.ssh(host, "wp eval-file -", inp=disc)
        ar = out.strip()
    if not ar.isdigit() or ar == "0":
        die("no AR twin found via WPML. Create it first: wp-admin → EN post → Language box → '+' → العربية. (Never wp post create.)")
    if ar == en:
        die("resolved AR id == EN id — refusing (would overwrite the English original).")
    # verify: ar is a guide_article AND its WPML language is 'ar' AND it points back to EN
    vphp = f"""<?php
$a={ar}; $e={en};
echo "type=".get_post_type($a)."\\n";
echo "status=".get_post_status($a)."\\n";
$ld=apply_filters("wpml_post_language_details",null,$a);
echo "lang=".($ld && isset($ld["language_code"])?$ld["language_code"]:"")."\\n";
echo "en_to_ar=".(int)apply_filters("wpml_object_id",$e,"guide_article",false,"ar")."\\n";
"""
    rc, info, err = kit.ssh(host, "wp eval-file -", inp=vphp)
    d = dict(l.split("=", 1) for l in info.strip().splitlines() if "=" in l)
    print("=== TWIN VERIFY ===", d)
    if d.get("type") != "guide_article": die(f"AR {ar} is not a guide_article (got {d.get('type')!r})")
    if d.get("lang") != "ar":          die(f"AR {ar} language is {d.get('lang')!r}, not 'ar' — not a real twin")
    if d.get("en_to_ar") != ar:        die(f"WPML says EN {en} → AR {d.get('en_to_ar')}, not {ar} — linkage mismatch, refusing")

    # ── build image blocks from EXISTING media (reuse; no upload — repo is text-only) ──
    final = blocks
    for stem, cap in body_images:
        aid = media.get(stem, "")
        if not aid:
            die(f"no --media mapping for image stem '{stem}'")
        rc, url, _ = kit.ssh(host, f"wp post get {aid} --field=guid 2>/dev/null")
        url = url.strip()
        alt = cap or fm["title"]
        cap_html = f'<figcaption class="wp-block-image__caption">{html.escape(cap)}</figcaption>' if cap else ""
        blk = (f'<!-- wp:image {{"id":{aid},"sizeSlug":"large","linkDestination":"none"}} -->\n'
               f'<figure class="wp-block-image size-large"><img src="{url}" alt="{html.escape(alt)}" '
               f'class="wp-image-{aid}"/>{cap_html}</figure>\n<!-- /wp:image -->')
        final = final.replace(f"<!--GUIDEKIT_IMG:{stem}|{cap}-->", blk)

    hero = media.get("hero", "")
    status = "draft" if args.keep_draft else "publish"
    robots = "draft (not public)" if args.keep_draft else "publish + noindex (fenced; page renders for the proof)"

    print(f"\n=== POPULATE AR TWIN {ar}  (twin of EN {en})  [{'EXECUTE' if args.execute else 'DRY RUN'}] ===")
    print(f"title    : {fm['title']}")
    print(f"url      : {site}/ar/guide/{fm['slug']}/")
    print(f"fence    : {robots}")
    print(f"topic    : {fm['topic']}   hero(reuse): {hero or '⚠none'}   words: {wc}")
    print(f"images   : " + ", ".join(f"{s}->{media.get(s,'?')}" for s, _ in body_images))
    print(f"shortcodes: place={place_id} map={map_ids}")

    if not args.execute:
        print("\nDRY RUN — no writes. Re-run with --execute once the twin shell exists.\n")
        return

    # ── backup FIRST (discipline) ──
    rc, ts, _ = kit.ssh(host, "date +%Y%m%d-%H%M%S"); ts = ts.strip()
    bdir = cfg["BACKUP_DIR"]
    if not (bdir and os.path.isdir(bdir)):
        die("BACKUP_DIR missing — no write without a backup")
    dump = os.path.join(bdir, f"staging-{ts}-ar-twin-{fm['slug']}.sql.gz")
    with open(dump, "wb") as f:
        subprocess.run(["ssh", "-o", "BatchMode=yes", host, "wp db export - 2>/dev/null | gzip"], stdout=f)
    size = os.path.getsize(dump) if os.path.exists(dump) else 0
    print(f"\n[1] backup : {os.path.basename(dump)} ({size} B)")
    with open(os.path.join(HERE, "BACKUP_LOG.md"), "a", encoding="utf-8") as lg:
        lg.write(f"| {ts} | populate AR twin `{fm['slug']}` (post {ar}) | `{os.path.basename(dump)}` | {size} B | staging |\n")

    # ── stream body (charset-safe) ──
    bodyfile = f"/tmp/guidekit-ar-{fm['slug']}-body.html"
    subprocess.run(["ssh", "-o", "BatchMode=yes", host, f"cat > {bodyfile}"], input=final.encode("utf-8"), check=True)

    # ── update-only PHP (ensure_ascii=False → real UTF-8) ──
    php = f"""<?php
$id = {ar};
if (get_post_type($id) !== 'guide_article') {{ echo "ERR=not a guide_article\\n"; exit; }}
$r = wp_update_post(array(
  'ID' => $id,
  'post_status'  => {jx(status)},
  'post_title'   => {jx(fm['title'])},
  'post_name'    => {jx(fm['slug'])},
  'post_excerpt' => {jx(fm.get('meta_description',''))},
  'post_content' => file_get_contents({jx(bodyfile)}),
), true);
if (is_wp_error($r)) {{ echo "ERR=".$r->get_error_message()."\\n"; exit; }}
update_post_meta($id,'deck',{jx(fm['deck'])});
update_post_meta($id,'article_type',{jx(fm.get('article_type','guide'))});
update_post_meta($id,'word_count',{int(wc)});
update_post_meta($id,'hero_alt',{jx(fm.get('hero_alt',''))});
update_post_meta($id,'hero_caption',{jx(fm.get('hero_caption',''))});
$t = get_term_by('slug',{jx(fm['topic'])},'topic');
if ($t) {{ wp_set_object_terms($id,array((int)$t->term_id),'topic'); update_post_meta($id,'primary_topic',(int)$t->term_id); echo "TERM=".$t->term_id."\\n"; }}
$h = {int(hero) if str(hero).isdigit() else 0};
if ($h>0) {{ set_post_thumbnail($id,$h); update_post_meta($id,'hero_photo_id',$h); }}
update_post_meta($id,'rank_math_title',{jx(fm.get('seo_title') or fm['title'])});
update_post_meta($id,'rank_math_description',{jx(fm.get('meta_description',''))});
update_post_meta($id,'rank_math_robots',array('noindex'));   // FENCE (rail #4)
echo "OK=".$id."\\n"; echo "URL=".get_permalink($id)."\\n"; echo "ST=".get_post_status($id)."\\n";
"""
    rc, out, err = kit.ssh(host, "wp eval-file -", inp=php)
    print("[2] update :")
    for ln in out.splitlines():
        print("    " + ln)
    if "OK=" not in out:
        die(f"update failed. out={out} err={err}")

    # ── touch + flush (edge cache) ──
    kit.ssh(host, f'wp post update {ar} --post_status={status} >/dev/null 2>&1; '
                  f'wp eval "if(function_exists(\\"rocket_clean_domain\\")){{rocket_clean_domain();}}" >/dev/null 2>&1')
    print("[3] cache  : touched + flushed")

    # ── verify the first-twin proof ──
    print("[4] verify :")
    if args.keep_draft:
        print("    (draft → page not public; skip render check. Re-run without --draft for the /ar/places/ proof.)")
    else:
        import urllib.request
        u = f"{site}/ar/guide/{fm['slug']}/"
        try:
            h = urllib.request.urlopen(u, timeout=25).read().decode("utf-8", "replace")
            title_ok = ("صالون" in h) or (fm["title"][:6] in h)
            ar_places = "/ar/places/" in h
            en_leak = bool(re.search(r'href="/places/', h))
            dbl = "/ar/en/" in h
            single_title = h.count('class="entry-title"') <= 1
            noindex = "noindex" in h
            ok = lambda b: "✓" if b else "✗"
            print(f"    {ok(title_ok)} Arabic title renders (no mojibake)")
            print(f"    {ok(ar_places)} place-card emits /ar/places/  (Builder v1.14.175 proof)")
            print(f"    {'✗ EN leak!' if en_leak else '✓'} no bare /places/ (EN under AR)")
            print(f"    {'✗' if dbl else '✓'} no /ar/en/ double-prefix")
            print(f"    {ok(single_title)} no double title")
            print(f"    {'present ✓' if noindex else '⚠ check'} noindex robots meta (fence)")
        except Exception as e:
            print(f"    ⚠ could not fetch {u}: {e}")
    print(f"\n✅ POPULATED  {site}/ar/guide/{fm['slug']}/  (post {ar}, {status}, noindex-fenced)\n")


if __name__ == "__main__":
    main()
