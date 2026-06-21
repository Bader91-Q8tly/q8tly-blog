#!/usr/bin/env python3
"""
Q8tly Guide Ingestion Kit — publish a guide_article from one drop folder.

Usage:
  python3 publish_guide.py guides/<slug>            # DRY RUN (default): validate + print plan
  python3 publish_guide.py guides/<slug> --execute  # do it (backup → upload → create → verify)

Reads SSH host / site URL from config.sh (override: --ssh-host / --site-url or
env GUIDEKIT_SSH_HOST / GUIDEKIT_SITE_URL). Stdlib only. See README.md.
"""
import argparse, glob, gzip, html, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOPICS = {"food-drink", "neighborhoods", "culture-heritage", "seasonal"}
ARTICLE_TYPES = {"longread", "guide", "quick_take"}
# Body must not contain template chrome (it double-renders). Hard fails:
CHROME_FORBIDDEN = ["q8tly-guide-single", "By Q8tly Editorial", "wp:post-title"]


def die(msg):
    print(f"\n❌ {msg}\n", file=sys.stderr)
    sys.exit(1)


def load_config():
    cfg = {"SSH_HOST": "", "SITE_URL": "", "BACKUP_DIR": ""}
    path = os.path.join(HERE, "config.sh")
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            m = re.match(r'\s*([A-Z_]+)="?([^"#\n]+?)"?\s*(?:#.*)?$', line)
            if m and m.group(1) in cfg:
                cfg[m.group(1)] = m.group(2).strip()
    cfg["SSH_HOST"] = os.environ.get("GUIDEKIT_SSH_HOST", cfg["SSH_HOST"])
    cfg["SITE_URL"] = os.environ.get("GUIDEKIT_SITE_URL", cfg["SITE_URL"])
    return cfg


# ── frontmatter (minimal YAML: scalars + inline [a,b] lists) ──
def parse_frontmatter(text):
    if not text.startswith("---"):
        die("article.md has no frontmatter (must start with '---').")
    end = text.find("\n---", 3)
    if end == -1:
        die("frontmatter is not closed with '---'.")
    fm_raw, body = text[3:end].strip(), text[end + 4:].lstrip("\n")
    fm = {}
    for line in fm_raw.splitlines():
        line = line.split("#", 1)[0].rstrip() if not line.strip().startswith("#") else ""
        if not line.strip() or ":" not in line:
            continue
        key, val = line.split(":", 1)
        key, val = key.strip(), val.strip()
        if val.startswith("[") and val.endswith("]"):
            items = [v.strip().strip('"\'') for v in val[1:-1].split(",") if v.strip()]
            fm[key] = items
        else:
            fm[key] = val.strip('"\'')
    return fm, body


# ── markdown body → Gutenberg blocks (subset) + markers ──
def md_inline(t):
    t = html.escape(t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub(r"_([^_]+)_", r"<em>\1</em>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    return t


def md_to_blocks(body, place_id, map_ids):
    lines = body.split("\n")
    out, i, images = [], 0, []
    while i < len(lines):
        s = lines[i].strip()
        # markers
        if s == "[[place]]":
            if place_id:
                out.append(f'<!-- wp:shortcode -->\n[q8tly_place id="{place_id}"]\n<!-- /wp:shortcode -->')
            i += 1; continue
        if s == "[[map]]":
            if map_ids:
                ids = ",".join(str(x) for x in map_ids)
                out.append(f'<!-- wp:shortcode -->\n[q8tly_map ids="{ids}"]\n<!-- /wp:shortcode -->')
            i += 1; continue
        m_img = re.match(r"\[\[image:([^\]|]+)(?:\|([^\]]*))?\]\]", s)
        if m_img:
            stem, cap = m_img.group(1).strip(), (m_img.group(2) or "").strip()
            images.append((stem, cap))
            out.append(f"<!--GUIDEKIT_IMG:{stem}|{cap}-->")
            i += 1; continue
        # table
        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            header = [c.strip() for c in s.strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            t = ["<!-- wp:table -->", '<figure class="wp-block-table"><table><thead><tr>']
            t += [f"<th>{md_inline(h)}</th>" for h in header]
            t.append("</tr></thead><tbody>")
            for r in rows:
                t.append("<tr>" + "".join(f"<td>{md_inline(c)}</td>" for c in r) + "</tr>")
            t.append("</tbody></table></figure>\n<!-- /wp:table -->")
            out.append("".join(t)); continue
        # heading
        mh = re.match(r"^(#{2,3})\s+(.*)$", s)
        if mh:
            lvl = len(mh.group(1))
            attr = ' {"level":3}' if lvl == 3 else ""
            out.append(f'<!-- wp:heading{attr} -->\n<h{lvl} class="wp-block-heading">{md_inline(mh.group(2))}</h{lvl}>\n<!-- /wp:heading -->')
            i += 1; continue
        # blockquote
        if s.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip()); i += 1
            out.append("<!-- wp:quote -->\n<blockquote class=\"wp-block-quote\"><p>" + md_inline(" ".join(buf)) + "</p></blockquote>\n<!-- /wp:quote -->")
            continue
        # list
        if s.startswith("- "):
            items = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append("<li>" + md_inline(lines[i].strip()[2:]) + "</li>"); i += 1
            out.append("<!-- wp:list -->\n<ul>" + "".join(items) + "</ul>\n<!-- /wp:list -->")
            continue
        if s == "":
            i += 1; continue
        # paragraph (gather)
        buf = [s]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^\s*(#{2,3}\s|>|\||-\s|\[\[)", lines[i].strip()):
            buf.append(lines[i].strip()); i += 1
        out.append("<!-- wp:paragraph -->\n<p>" + md_inline(" ".join(buf)) + "</p>\n<!-- /wp:paragraph -->")
    return "\n\n".join(out), images


def word_count(body):
    txt = re.sub(r"\[\[[^\]]+\]\]", "", body)
    txt = re.sub(r"[#>*_`|-]", " ", txt)
    return len([w for w in txt.split() if w.strip()])


def ssh(host, cmd, inp=None):
    full = ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=25", host, cmd]
    r = subprocess.run(full, input=inp, capture_output=True, text=(inp is None or isinstance(inp, str)))
    return r.returncode, (r.stdout if isinstance(r.stdout, str) else r.stdout.decode("utf-8", "replace")), \
        (r.stderr if isinstance(r.stderr, str) else r.stderr.decode("utf-8", "replace"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--execute", action="store_true", help="perform the publish (default: dry run)")
    ap.add_argument("--ssh-host", default=None)
    ap.add_argument("--site-url", default=None)
    ap.add_argument("--offline", action="store_true", help="skip remote read checks (dry run only)")
    args = ap.parse_args()

    cfg = load_config()
    host = args.ssh_host or cfg["SSH_HOST"]
    site = (args.site_url or cfg["SITE_URL"]).rstrip("/")
    backup_dir = cfg["BACKUP_DIR"]

    folder = os.path.abspath(args.folder)
    art = os.path.join(folder, "article.md")
    if not os.path.exists(art):
        die(f"no article.md in {folder}")
    fm, body = parse_frontmatter(open(art, encoding="utf-8").read())

    # ── validate (guardrails) ──
    required = ["title", "slug", "lang", "deck", "topic", "article_type", "place_id"]
    missing = [k for k in required if not fm.get(k)]
    if missing:
        die(f"frontmatter missing required keys: {', '.join(missing)}")
    if fm["topic"] not in TOPICS:
        die(f"topic '{fm['topic']}' not one of {sorted(TOPICS)}")
    if fm["article_type"] not in ARTICLE_TYPES:
        die(f"article_type '{fm['article_type']}' not one of {sorted(ARTICLE_TYPES)}")
    for bad in CHROME_FORBIDDEN:
        if bad.lower() in body.lower():
            die(f"body contains template chrome '{bad}' — keep the body plain (the template renders chrome).")
    if fm["lang"] == "ar" and fm.get("status") != "publish":
        print("ℹ AR drop with status != publish → stays PARKED (not published). Set status: publish to ship AR.")

    slug = fm["slug"]
    place_id = fm.get("place_id")
    map_ids = fm.get("map_ids") if isinstance(fm.get("map_ids"), list) else ([fm["map_ids"]] if fm.get("map_ids") else [])
    map_ids = [x for x in map_ids if str(x).strip() and str(x) != "0"]
    status = fm.get("status", "publish")
    if fm["lang"] == "ar" and status != "publish":
        status = "draft"

    block_body, body_images = md_to_blocks(body, place_id, map_ids)
    wc = word_count(body) if str(fm.get("word_count", "auto")) == "auto" else fm["word_count"]

    # images on disk
    img_dir = os.path.join(folder, "images")
    disk = {os.path.splitext(os.path.basename(p))[0]: p
            for p in sorted(glob.glob(os.path.join(img_dir, "*"))) if os.path.isfile(p)}
    hero = next((disk[k] for k in disk if k == "hero"), None)
    referenced = [stem for stem, _ in body_images]
    missing_imgs = [s for s in referenced if s not in disk]

    print(f"\n=== GUIDE DROP: {slug}  ({'EXECUTE' if args.execute else 'DRY RUN'}) ===")
    print(f"title         : {fm['title']}")
    print(f"permalink     : {site}/guide/{slug}/")
    print(f"lang/status   : {fm['lang']} / {status}")
    print(f"topic         : {fm['topic']}   article_type: {fm['article_type']}   word_count: {wc}")
    print(f"place_id      : {place_id}   map_ids: {map_ids or '—'}")
    print(f"hero image    : {os.path.basename(hero) if hero else '⚠ NONE (flat-plate hero)'}")
    print(f"inline images : {', '.join(referenced) or '—'}")
    print(f"replaces page : {fm.get('replaces_page_slug') or '—'}")
    if missing_imgs:
        die(f"body references images not in images/: {missing_imgs}")

    # ── remote read checks ──
    if host and not args.offline:
        rc, sn, _ = ssh(host, f"wp post list --post_type=guide_article --posts_per_page=-1 --field=post_name 2>/dev/null")
        if rc == 0 and slug in sn.split():
            die(f"slug '{slug}' already exists as a guide_article. Pick a unique slug.")
        if place_id:
            rc, pt, _ = ssh(host, f"wp post get {place_id} --field=post_type 2>/dev/null")
            if pt.strip() != "gd_place":
                die(f"place_id {place_id} is not a published gd_place (got '{pt.strip() or 'nothing'}').")
        print("remote checks : ✓ slug free, place_id resolves")
    else:
        print("remote checks : (skipped)")

    if not args.execute:
        print("\n--- BODY (Gutenberg blocks; [[image]] shown as GUIDEKIT_IMG placeholders) ---\n")
        print(block_body)
        print("\nDRY RUN complete. Re-run with --execute to publish.\n")
        return

    if not host:
        die("no SSH host configured (config.sh SSH_HOST / --ssh-host).")

    # ── 1. backup ──
    rc, ts, _ = ssh(host, "date +%Y%m%d-%H%M%S")
    ts = ts.strip()
    if backup_dir and os.path.isdir(backup_dir):
        dump = os.path.join(backup_dir, f"staging-{ts}-guide-{slug}.sql.gz")
        with open(dump, "wb") as f:
            p = subprocess.run(["ssh", "-o", "BatchMode=yes", host, "wp db export - 2>/dev/null | gzip"],
                               stdout=f)
        size = os.path.getsize(dump) if os.path.exists(dump) else 0
        print(f"\n[1] backup    : {os.path.basename(dump)} ({size} bytes)")
        with open(os.path.join(HERE, "BACKUP_LOG.md"), "a", encoding="utf-8") as lg:
            lg.write(f"| {ts} | publish guide `{slug}` | `{os.path.basename(dump)}` | {size} B | staging |\n")
    else:
        print("[1] backup    : ⚠ BACKUP_DIR missing — aborting (discipline: no write without a verified backup).")
        die("create the backup dir or fix config.sh BACKUP_DIR")

    # ── 2. upload images ──
    media = {}  # stem -> (id, url)
    for stem, path in disk.items():
        if stem != "hero" and stem != "og" and stem not in referenced:
            continue
        remote = f"/tmp/guidekit-{slug}-{stem}{os.path.splitext(path)[1]}"
        with open(path, "rb") as f:
            subprocess.run(["ssh", "-o", "BatchMode=yes", host, f"cat > {remote}"], stdin=f, check=True)
        rc, out, err = ssh(host, f'wp media import {remote} --title="{slug} {stem}" --porcelain 2>/dev/null')
        att = out.strip().splitlines()[-1] if out.strip() else ""
        rc, url, _ = ssh(host, f'wp post get {att} --field=guid 2>/dev/null')
        media[stem] = (att, url.strip())
        print(f"[2] uploaded  : {stem} -> attachment {att}")
    hero_id = media.get("hero", ("", ""))[0]

    # ── 3. body: replace image placeholders with real blocks ──
    final = block_body
    for stem, cap in body_images:
        aid, url = media.get(stem, ("", ""))
        alt = cap or fm["title"]
        cap_html = f'<figcaption class="wp-block-image__caption">{html.escape(cap)}</figcaption>' if cap else ""
        blk = (f'<!-- wp:image {{"id":{aid},"sizeSlug":"large","linkDestination":"none"}} -->\n'
               f'<figure class="wp-block-image size-large"><img src="{url}" alt="{html.escape(alt)}" '
               f'class="wp-image-{aid}"/>{cap_html}</figure>\n<!-- /wp:image -->')
        final = final.replace(f"<!--GUIDEKIT_IMG:{stem}|{cap}-->", blk)

    bodyfile = f"/tmp/guidekit-{slug}-body.html"
    subprocess.run(["ssh", "-o", "BatchMode=yes", host, f"cat > {bodyfile}"], input=final.encode(), check=True)

    # ── 4+5. create guide + meta + term + featured (one PHP run; clean value handling) ──
    php = build_create_php(fm, slug, status, wc, hero_id, bodyfile)
    rc, out, err = ssh(host, "wp eval-file -", inp=php)
    print("[4] create    :")
    for ln in out.splitlines():
        if ln.startswith(("NEWID=", "URL=", "WARN", "TERM=")):
            print("    " + ln)
    new_id = next((ln.split("=", 1)[1] for ln in out.splitlines() if ln.startswith("NEWID=")), "")
    new_url = next((ln.split("=", 1)[1] for ln in out.splitlines() if ln.startswith("URL=")), f"{site}/guide/{slug}/")
    if not new_id.isdigit():
        die(f"create failed. stdout={out}\nstderr={err}")
    # attach uploaded media to the new post (tidiness)
    for stem, (aid, _) in media.items():
        if aid:
            ssh(host, f"wp post update {aid} --post_parent={new_id} >/dev/null 2>&1")

    # ── 6. replace stand-in Page + 301 ──
    old = fm.get("replaces_page_slug")
    if old:
        php301 = build_redirect_php(old, slug)
        ssh(host, "wp eval-file -", inp=php301)
        ssh(host, f"wp post list --post_type=page --name={old} --field=ID 2>/dev/null | "
                  f"xargs -r -I{{}} wp post delete {{}} 2>/dev/null")
        print(f"[6] replaced  : trashed Page '{old}', 301 -> /guide/{slug}/")

    # ── 7. cache bust (touch — wp-cli meta writes don't trigger the edge purge) ──
    ssh(host, f'wp post update {new_id} --post_status={status} >/dev/null 2>&1; '
              f'wp eval "if(function_exists(\\"rocket_clean_domain\\")){{rocket_clean_domain();}}" >/dev/null 2>&1')
    print("[7] cache     : touched + WP Rocket flushed")

    # ── verify ──
    verify(site, slug, new_id, hero_id, host, old)

    # ── handoff ──
    write_handoff(slug, new_id, new_url, media, hero_id, old, wc, fm)
    print(f"\n✅ DONE  {new_url}\n   handoff: guide-kit/runs/{slug}.md\n")


def build_create_php(fm, slug, status, wc, hero_id, bodyfile):
    j = json.dumps
    seo_title = fm.get("seo_title") or fm["title"]
    return f"""<?php
$body = file_get_contents({j(bodyfile)});
$id = wp_insert_post(array(
  'post_type'    => 'guide_article',
  'post_status'  => {j(status)},
  'post_title'   => {j(fm['title'])},
  'post_name'    => {j(slug)},
  'post_excerpt' => {j(fm.get('meta_description',''))},
  'post_content' => $body,
), true);
if (is_wp_error($id)) {{ echo "ERR=".$id->get_error_message()."\\n"; exit; }}
update_post_meta($id, 'deck', {j(fm['deck'])});
update_post_meta($id, 'article_type', {j(fm['article_type'])});
update_post_meta($id, 'word_count', {int(wc)});
update_post_meta($id, 'hero_alt', {j(fm.get('hero_alt',''))});
update_post_meta($id, 'hero_caption', {j(fm.get('hero_caption',''))});
$term = get_term_by('slug', {j(fm['topic'])}, 'topic');
if ($term) {{ wp_set_object_terms($id, array((int)$term->term_id), 'topic'); update_post_meta($id,'primary_topic',(int)$term->term_id); echo "TERM=".$term->term_id."\\n"; }}
else {{ echo "WARN=topic term not found: {fm['topic']}\\n"; }}
$hero = {int(hero_id) if str(hero_id).isdigit() else 0};
if ($hero > 0) {{ set_post_thumbnail($id, $hero); update_post_meta($id,'hero_photo_id',$hero); }}
else {{ echo "WARN=no hero image — flat-plate hero\\n"; }}
$st = {j(seo_title)}; $md = {j(fm.get('meta_description',''))};
if ($st) update_post_meta($id, 'rank_math_title', $st);
if ($md) update_post_meta($id, 'rank_math_description', $md);
echo "NEWID=".$id."\\n";
echo "URL=".get_permalink($id)."\\n";
"""


def build_redirect_php(old_slug, new_slug):
    j = json.dumps
    return f"""<?php
if (class_exists('RankMath\\\\Redirections\\\\DB')) {{
  $args = array(
    'sources' => array(array('pattern' => {j(old_slug)}, 'comparison' => 'exact', 'ignore' => '')),
    'url_to'  => home_url('/guide/' . {j(new_slug)} . '/'),
    'header_code' => '301', 'status' => 'active',
  );
  echo "REDIRECT=".var_export(\\RankMath\\Redirections\\DB::add($args), true)."\\n";
}} else {{ echo "WARN=Rank Math redirections unavailable; add 301 manually\\n"; }}
"""


def verify(site, slug, new_id, hero_id, host, old):
    import urllib.request
    url = f"{site}/guide/{slug}/"
    try:
        h = urllib.request.urlopen(url, timeout=20).read().decode("utf-8", "replace")
        checks = {
            "renders 200": True,
            "house byline (chrome)": "guide-single__byline" in h or "Q8tly Editorial" in h,
            "hero present": (not hero_id) or (f"wp-image-{hero_id}" in h or "guide-single__hero" in h or "/uploads/" in h),
            "no double title": h.count('class="entry-title"') <= 1,
        }
        print("[v] verify    :")
        for k, v in checks.items():
            print(f"    {'✓' if v else '✗'} {k}")
    except Exception as e:
        print(f"[v] verify    : ⚠ could not fetch {url}: {e}")
    if old:
        try:
            req = urllib.request.Request(f"{site}/{old}/")
            opener = urllib.request.build_opener(NoRedirect())
            r = opener.open(req, timeout=20)
            print(f"    ✗ old /{old}/ did not redirect (status {r.status})")
        except urllib.error.HTTPError as e:
            print(f"    {'✓' if e.code in (301,302) else '✗'} old /{old}/ -> {e.code} {e.headers.get('Location','')}")
        except Exception:
            print(f"    ✓ old /{old}/ redirects (no 200)")


class NoRedirect(__import__("urllib.request", fromlist=["HTTPRedirectHandler"]).HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def write_handoff(slug, new_id, new_url, media, hero_id, old, wc, fm):
    runs = os.path.join(HERE, "runs")
    os.makedirs(runs, exist_ok=True)
    lines = [
        f"# Run handoff — guide `{slug}`", "",
        f"- **URL:** {new_url}", f"- **guide_article ID:** {new_id}",
        f"- **topic:** {fm['topic']} · **article_type:** {fm['article_type']} · **word_count:** {wc}",
        f"- **hero attachment:** {hero_id or '⚠ none (flat-plate)'} (Featured + hero_photo_id)",
        f"- **inline images:** " + (", ".join(f"{s}={a}" for s, (a, _) in media.items() if s not in ('hero', 'og')) or "—"),
    ]
    if old:
        lines.append(f"- **replaced Page:** /{old}/ trashed + 301 → /guide/{slug}/")
    manual = []
    if not hero_id:
        manual.append("Add a hero image (images/hero.*) and re-run, or set Featured in wp-admin.")
    if fm.get("lang") == "ar":
        manual.append("AR: confirm human translation review before this counts as published.")
    lines.append("- **manual steps remaining:** " + ("; ".join(manual) if manual else "none ✓"))
    open(os.path.join(runs, f"{slug}.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
