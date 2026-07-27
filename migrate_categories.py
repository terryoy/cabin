#!/usr/bin/env python3
"""Migrate categories to tags in Jekyll posts."""
import os
import re

POSTS_DIR = "/root/data/disk/projects/cabin/_posts"

def main():
    files = sorted([f for f in os.listdir(POSTS_DIR) if f.endswith('.md')])
    print(f"Total files: {len(files)}")
    
    changes = 0
    for fname in files:
        path = os.path.join(POSTS_DIR, fname)
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        # Check if file has categories
        cat_match = re.search(r'^categories:\s*(.*?)$', content, re.MULTILINE)
        if not cat_match:
            continue
        
        cat_value = cat_match.group(1).strip()
        cat_line = cat_match.group(0)
        
        # Skip empty categories
        if cat_value == '[]' or not cat_value:
            new_content = content.replace(cat_line + '\n', '')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            changes += 1
            print(f"  Removed empty categories: {fname}")
            continue
        
        # Parse categories value
        if cat_value.startswith('[') and cat_value.endswith(']'):
            cats = [c.strip().strip("'\"") for c in cat_value[1:-1].split(',')]
        else:
            cats = [cat_value.strip().strip("'\"")]
        
        # Get current tags
        tags_match = re.search(r'^tags:\s*(.*?)$', content, re.MULTILINE)
        current_tags = []
        
        if tags_match:
            tags_value = tags_match.group(1).strip()
            if tags_value.startswith('[') and tags_value.endswith(']'):
                current_tags = [t.strip().strip("'\"") for t in tags_value[1:-1].split(',')]
            elif tags_value.startswith('- '):
                # Multi-line list format
                tag_lines = re.findall(r'^\s*-\s*(.*?)$', content[tags_match.start():], re.MULTILINE)
                current_tags = [t.strip().strip("'\"") for t in tag_lines]
            elif tags_value:
                current_tags = [tags_value.strip().strip("'\"")]
        
        # Merge categories into tags (avoid duplicates)
        for c in cats:
            if c not in current_tags:
                current_tags.append(c)
        
        # Build new tags line
        if len(current_tags) == 1:
            new_tags_line = f"tags: {current_tags[0]}"
        else:
            new_tags_line = "tags: [" + ", ".join(current_tags) + "]"
        
        # Remove old categories line and replace tags line
        new_content = content.replace(cat_line + '\n', '')
        if tags_match:
            new_content = new_content.replace(tags_match.group(0), new_tags_line)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        changes += 1
        print(f"  Merged: {fname}")
        print(f"    categories: {cats} -> tags: {current_tags}")
    
    print(f"\nTotal files modified: {changes}")

if __name__ == "__main__":
    main()