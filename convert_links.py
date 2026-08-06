"""
Converts old-style wikilinks that point to a heading:
    [[Page Path#Heading Text|Display Text]]
into the new autorefs format:
    [Display Text][slug-id]
and makes sure the target heading is tagged with that id:
    ## Heading Text {#slug-id}

Run this from inside your project folder (the one with mkdocs.yml):
    python convert_links.py

It only touches links that have a '#Heading' part. Plain page links like
[[Page Path|Display Text]] are left alone.
"""

import os
import re

DOCS_DIR = "docs"

WIKI_RE = re.compile(r'\[\[((?:(?!\]\]).)+)\]\]')
HEADING_RE = re.compile(r'^(#{1,6})\s+(.*)$')
EXISTING_ID_RE = re.compile(r'\s*\{#([\w\-]+)\}\s*$')


def normalize(text):
    text = text.replace('\u2013', '-').replace('\u2014', '-')
    text = ' '.join(text.split())
    return text.strip().casefold()


def slugify(text):
    text = text.replace('\u2013', '-').replace('\u2014', '-').lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text).strip('-')
    return text or 'section'


def load_files():
    paths = []
    for root, _, files in os.walk(DOCS_DIR):
        for f in files:
            if f.endswith('.md'):
                paths.append(os.path.join(root, f))
    return paths


def read_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()


def find_target_file(all_files, page_path):
    page_path = page_path.strip()
    direct = os.path.normpath(os.path.join(DOCS_DIR, page_path + '.md'))
    if os.path.exists(direct):
        return direct
    basename = os.path.basename(page_path) + '.md'
    matches = [p for p in all_files if os.path.basename(p).lower() == basename.lower()]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        return ('AMBIGUOUS', matches)
    return None


def main():
    all_files = load_files()
    file_lines = {p: read_lines(p) for p in all_files}
    dirty = set()

    # Pre-scan existing {#id} tags so new slugs never collide with them
    used_slugs = set()
    for p, lines in file_lines.items():
        for line in lines:
            m = HEADING_RE.match(line)
            if m:
                idm = EXISTING_ID_RE.search(m.group(2))
                if idm:
                    used_slugs.add(idm.group(1))

    # Cache: (filepath, line_index) -> assigned slug
    heading_slug_cache = {}

    converted = 0
    tagged = 0
    skipped = []

    for src_path in all_files:
        lines = file_lines[src_path]
        for i, line in enumerate(lines):
            def repl(match):
                nonlocal converted, tagged
                inner = match.group(1)
                if '#' not in inner:
                    return match.group(0)  # plain page link, leave untouched

                page_part, rest = inner.split('#', 1)
                page_part = page_part.strip()
                if '|' in rest:
                    heading_text, display = rest.split('|', 1)
                else:
                    heading_text, display = rest, rest
                heading_text = heading_text.strip()
                display = display.strip()

                target = find_target_file(all_files, page_part)
                if target is None:
                    skipped.append(f"{src_path}: page not found for '[[{inner}]]'")
                    return match.group(0)
                if isinstance(target, tuple):
                    skipped.append(f"{src_path}: ambiguous page '{page_part}' for '[[{inner}]]' -> {target[1]}")
                    return match.group(0)

                target_lines = file_lines[target]
                norm_target_heading = normalize(heading_text)

                found_idx = None
                for j, tline in enumerate(target_lines):
                    hm = HEADING_RE.match(tline)
                    if not hm:
                        continue
                    clean = EXISTING_ID_RE.sub('', hm.group(2)).strip()
                    if normalize(clean) == norm_target_heading:
                        found_idx = j
                        break

                if found_idx is None:
                    skipped.append(f"{src_path}: heading '{heading_text}' not found in {target} (link '[[{inner}]]')")
                    return match.group(0)

                cache_key = (target, found_idx)
                if cache_key in heading_slug_cache:
                    slug = heading_slug_cache[cache_key]
                else:
                    hm = HEADING_RE.match(target_lines[found_idx])
                    existing = EXISTING_ID_RE.search(hm.group(2))
                    if existing:
                        slug = existing.group(1)
                    else:
                        base_slug = slugify(heading_text)
                        slug = base_slug
                        n = 2
                        while slug in used_slugs:
                            slug = f"{base_slug}-{n}"
                            n += 1
                        used_slugs.add(slug)
                        clean_text = EXISTING_ID_RE.sub('', hm.group(2)).strip()
                        target_lines[found_idx] = f"{hm.group(1)} {clean_text} {{#{slug}}}"
                        dirty.add(target)
                        tagged += 1
                    heading_slug_cache[cache_key] = slug

                converted += 1
                return f"[{display}][{slug}]"

            new_line = WIKI_RE.sub(repl, line)
            if new_line != line:
                lines[i] = new_line
                dirty.add(src_path)

    for path in dirty:
        with open(path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(file_lines[path]) + '\n')

    print(f"Converted {converted} link(s).")
    print(f"Tagged {tagged} new heading(s) with an id.")
    print(f"Files changed: {len(dirty)}")
    if skipped:
        print(f"\n{len(skipped)} link(s) skipped (need manual fix):")
        for s in skipped:
            print(f"  - {s}")
    else:
        print("\nNothing skipped.")


if __name__ == '__main__':
    main()
