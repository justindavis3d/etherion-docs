"""
Renames top-level folders inside docs/ from "1  Foliage Physics" style
names to plain names like "Foliage Physics" (strips leading numbers and
all the spaces after them). Page filenames are left untouched.

Then scans every .md file for wikilinks/markdown links that reference
the OLD folder name in their path and updates them to the new folder
name, so links keep working after the rename.

Run this from inside your project folder (the one with mkdocs.yml):
    python rename_folders.py

BACK UP your docs folder before running this.
"""

import os
import re

DOCS_DIR = "docs"

FOLDER_PREFIX_RE = re.compile(r'^\d+\s*(.*)$')


def main():
    entries = [d for d in os.listdir(DOCS_DIR)
               if os.path.isdir(os.path.join(DOCS_DIR, d))]

    renames = {}
    for old_name in entries:
        m = FOLDER_PREFIX_RE.match(old_name)
        if not m:
            continue
        new_name = m.group(1).strip()
        if new_name and new_name != old_name:
            renames[old_name] = new_name

    if not renames:
        print("No numbered folders found to rename.")
        return

    print("Planned renames:")
    for old, new in renames.items():
        print(f"  '{old}'  ->  '{new}'")

    # Do the actual folder renames
    for old_name, new_name in renames.items():
        old_path = os.path.join(DOCS_DIR, old_name)
        new_path = os.path.join(DOCS_DIR, new_name)
        if os.path.exists(new_path):
            print(f"SKIPPED rename of '{old_name}': '{new_name}' already exists.")
            continue
        os.rename(old_path, new_path)
        print(f"Renamed '{old_name}' -> '{new_name}'")

    # Now fix any links that reference the old folder names
    md_files = []
    for root, _, files in os.walk(DOCS_DIR):
        for f in files:
            if f.endswith('.md'):
                md_files.append(os.path.join(root, f))

    changed_files = 0
    total_replacements = 0

    for path in md_files:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        original = content
        for old_name, new_name in renames.items():
            if os.path.exists(os.path.join(DOCS_DIR, new_name)):
                pattern = re.escape(old_name) + r'/'
                new_content, count = re.subn(pattern, new_name + '/', content)
                if count:
                    content = new_content
                    total_replacements += count
        if content != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            changed_files += 1

    print(f"\nUpdated {total_replacements} link reference(s) across {changed_files} file(s).")


if __name__ == '__main__':
    main()
