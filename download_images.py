"""
Scans all .md files inside the 'docs' folder, finds images that are
hosted on an external website (http:// or https://), downloads each
one into docs/assets/, and rewrites the markdown to point to the
local copy instead.

Run this from inside your project folder (the one with mkdocs.yml):
    python download_images.py
"""

import os
import re
import hashlib
from urllib.parse import urlparse
import requests

DOCS_DIR = "docs"
ASSETS_DIR = os.path.join(DOCS_DIR, "assets")

# Matches both markdown images ![alt](url) and raw <img src="url">
MD_IMG = re.compile(r'!\[([^\]]*)\]\((https?://[^\)\s]+)\)')
HTML_IMG = re.compile(r'<img\s+[^>]*src=["\'](https?://[^"\']+)["\']')

os.makedirs(ASSETS_DIR, exist_ok=True)

def safe_filename(url):
    parsed = urlparse(url)
    name = os.path.basename(parsed.path)
    if not name or "." not in name:
        # no usable filename in the URL, make one up
        ext_guess = ".png"
        name = hashlib.md5(url.encode()).hexdigest()[:10] + ext_guess
    return name

def download(url):
    filename = safe_filename(url)
    local_path = os.path.join(ASSETS_DIR, filename)

    # avoid overwriting a different image that happens to share a filename
    if os.path.exists(local_path):
        with open(local_path, "rb") as f:
            existing_hash = hashlib.md5(f.read()).hexdigest()
        try:
            resp = requests.get(url, timeout=15)
            new_hash = hashlib.md5(resp.content).hexdigest()
        except Exception as e:
            print(f"  FAILED: {url} ({e})")
            return None
        if existing_hash != new_hash:
            base, ext = os.path.splitext(filename)
            filename = f"{base}_{hashlib.md5(url.encode()).hexdigest()[:6]}{ext}"
            local_path = os.path.join(ASSETS_DIR, filename)
            with open(local_path, "wb") as f:
                f.write(resp.content)
    else:
        try:
            resp = requests.get(url, timeout=15)
            resp.raise_for_status()
        except Exception as e:
            print(f"  FAILED: {url} ({e})")
            return None
        with open(local_path, "wb") as f:
            f.write(resp.content)

    return filename

processed_urls = {}

for root, _, files in os.walk(DOCS_DIR):
    for fname in files:
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        urls = set(MD_IMG.findall(content))
        urls = {u for (_, u) in urls} | set(HTML_IMG.findall(content))

        if not urls:
            continue

        print(f"{fpath}: found {len(urls)} external image(s)")
        new_content = content

        for url in urls:
            if url not in processed_urls:
                print(f"  downloading {url}")
                filename = download(url)
                processed_urls[url] = filename
            filename = processed_urls[url]
            if filename:
                # relative path from a docs subfolder back to assets/
                rel_depth = os.path.relpath(DOCS_DIR, root)
                local_ref = os.path.join(rel_depth, "assets", filename).replace("\\", "/")
                new_content = new_content.replace(url, local_ref)

        if new_content != content:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"  updated {fpath}")

print("Done. Images saved in docs/assets/")
