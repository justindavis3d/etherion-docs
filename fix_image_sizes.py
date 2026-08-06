"""
Scans all .md files inside 'docs' for Obsidian-style resized image
embeds, e.g.:
    ![[image.png|300]]
    ![[image.png|300x200]]
    ![alt text](image.png|300)

...and rewrites them as HTML <img> tags with real width/height
attributes, which render correctly on the built website.

Run from inside your project folder (the one with mkdocs.yml):
    python fix_image_sizes.py
"""

import os
import re

DOCS_DIR = "docs"

# ![[image.png|300]]  or  ![[image.png|300x200]]
WIKI_EMBED = re.compile(r'!\[\[([^\|\]]+\.(?:png|jpe?g|gif|svg|webp))\|(\d+)(?:x(\d+))?\]\]', re.IGNORECASE)

# ![alt](image.png|300)  or  ![alt](image.png|300x200)
MD_EMBED = re.compile(r'!\[([^\]]*)\]\(([^\|\)]+\.(?:png|jpe?g|gif|svg|webp))\|(\d+)(?:x(\d+))?\)', re.IGNORECASE)

changed_files = 0
changed_images = 0

for root, _, files in os.walk(DOCS_DIR):
    for fname in files:
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        original = content

        def wiki_replace(m):
            global changed_images
            changed_images += 1
            path, w, h = m.group(1), m.group(2), m.group(3)
            if h:
                return f'<img src="{path}" width="{w}" height="{h}">'
            return f'<img src="{path}" width="{w}">'

        def md_replace(m):
            global changed_images
            changed_images += 1
            alt, path, w, h = m.group(1), m.group(2), m.group(3), m.group(4)
            if h:
                return f'<img src="{path}" alt="{alt}" width="{w}" height="{h}">'
            return f'<img src="{path}" alt="{alt}" width="{w}">'

        content = WIKI_EMBED.sub(wiki_replace, content)
        content = MD_EMBED.sub(md_replace, content)

        if content != original:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            changed_files += 1
            print(f"updated: {fpath}")

print(f"\nDone. {changed_images} image(s) fixed across {changed_files} file(s).")
