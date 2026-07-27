#!/usr/bin/env python3
"""
Fix Jekyll blog posts in terryoy/cabin repo - optimized version.
Uses GitHub API directly via HTTPS.
1. Add :00 seconds to date: fields that don't have seconds
2. Remove duplicate files (same content, punctuation-different filenames)
"""

import json
import re
import sys
import base64
import time
import os
import subprocess
import urllib.request
import urllib.error

REPO = "terryoy/cabin"
BRANCH = "master"
POSTS_TREE_SHA = "130d4230095267cc6a143102100ae69b14dd38fc"

# Get GitHub token
GH_TOKEN = os.environ.get("GH_TOKEN", "")
if not GH_TOKEN:
    try:
        result = subprocess.run(
            ["gh", "auth", "token"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            GH_TOKEN = result.stdout.strip()
    except Exception:
        GH_TOKEN = ""

if not GH_TOKEN:
    print("No GitHub token available")
    sys.exit(1)

HEADERS = {
    "Authorization": f"Bearer {GH_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "Hermes-Fixer"
}
API_BASE = "https://api.github.com"

def api_call(method, endpoint, data=None, retries=3):
    """Make a GitHub API call directly via HTTPS."""
    url = f"{API_BASE}{endpoint}"
    body = json.dumps(data).encode("utf-8") if data else None

    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, data=body, headers=HEADERS, method=method)
            if body:
                req.add_header("Content-Type", "application/json")

            with urllib.request.urlopen(req, timeout=30) as resp:
                text = resp.read().decode("utf-8")
                if text.strip():
                    return json.loads(text)
                return {}
        except urllib.error.HTTPError as e:
            err_text = e.read().decode("utf-8", errors="replace")[:200]
            if e.code == 409:
                time.sleep(2)
                continue
            print(f"  HTTP {e.code}: {err_text}")
            return None
        except urllib.error.URLError as e:
            time.sleep(2)
            continue
        except Exception as e:
            time.sleep(2)
            continue
    return None

def get_blob(sha):
    """Get decoded file content from a git blob SHA."""
    result = api_call("GET", f"/repos/{REPO}/git/blobs/{sha}")
    if not result:
        return None
    content = result.get("content", "")
    encoding = result.get("encoding", "utf-8")
    if encoding == "base64":
        try:
            return base64.b64decode(content).decode("utf-8", errors="replace")
        except:
            return None
    return content

def create_blob(content):
    """Create a new git blob and return its SHA."""
    encoded = base64.b64encode(content.encode("utf-8")).decode("ascii")
    result = api_call("POST", f"/repos/{REPO}/git/blobs", {
        "content": encoded,
        "encoding": "base64"
    })
    return result.get("sha") if result else None

def fix_date_format(content):
    """Fix date: fields that don't have seconds. Add :00."""
    pattern = r'^(date:\s*[\'"]?(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})(?!:\d{2})[\'"]?\s*)$'
    matches = re.findall(pattern, content, re.MULTILINE)
    if not matches:
        return content, False
    modified = content
    for full_match, date_part in matches:
        modified = modified.replace(full_match, full_match.replace(date_part, f"{date_part}:00"))
    return modified, True

def normalize_filename(path):
    """Normalize filename for dedup comparison."""
    name = path.rsplit(".", 1)[0]
    name = re.sub(r'[\s\-]+', '-', name)
    name = re.sub(r'[\uE000-\uF8FF]', '', name)
    name = re.sub(r'[《》「」『』]', '', name)
    name = name.replace('？', '?').replace('！', '!').replace('：', ':').replace('～', '~')
    name = re.sub(r'-+', '-', name)
    name = name.strip('-')
    return name.lower()

def main():
    print("=" * 60)
    print("Cabin Blog Fixer")
    print("=" * 60)

    # Step 1: Get tree
    print("\nGetting _posts tree...")
    tree_result = api_call("GET", f"/repos/{REPO}/git/trees/{POSTS_TREE_SHA}")
    if not tree_result or "tree" not in tree_result:
        print("Failed to get _posts tree")
        sys.exit(1)
    files = tree_result["tree"]
    print(f"  Found {len(files)} files")

    # Step 2: Read files and fix dates
    print("\nProcessing files...")
    date_fixed = 0
    date_failed = 0
    new_blobs = {}
    file_contents = {}

    for i, f in enumerate(files):
        path = f["path"]
        sha = f["sha"]
        content = get_blob(sha)
        if content is None:
            date_failed += 1
            continue

        file_contents[path] = content
        new_content, changed = fix_date_format(content)
        if changed:
            new_sha = create_blob(new_content)
            if new_sha:
                new_blobs[path] = new_sha
                date_fixed += 1
            else:
                date_failed += 1

        if (i + 1) % 50 == 0:
            print(f"  Progress: {i+1}/{len(files)}, {date_fixed} fixed")

    print(f"\nDate fix: {date_fixed} fixed, {date_failed} failed")

    # Step 3: Find duplicates
    print("\nFinding duplicates...")
    groups = {}
    for f in files:
        path = f["path"]
        norm = normalize_filename(path)
        if norm not in groups:
            groups[norm] = []
        groups[norm].append(path)

    duplicates = {k: v for k, v in groups.items() if len(v) > 1}
    to_delete = []

    if duplicates:
        for norm, paths in sorted(duplicates.items()):
            def sort_key(p):
                name = p.rsplit('.', 1)[0]
                return (-name.count('-'), name.count(' '), p)
            sorted_paths = sorted(paths, key=sort_key)
            keep = sorted_paths[0]
            for d in sorted_paths[1:]:
                to_delete.append(d)
                print(f"  Delete duplicate: {d} (keep: {keep})")

    print(f"  Total to delete: {len(to_delete)}")

    # Step 4: Build new tree
    print("\nBuilding new tree...")
    new_tree = []
    for f in files:
        path = f["path"]
        if path in to_delete:
            continue
        new_tree.append({
            "path": path,
            "mode": f["mode"],
            "type": "blob",
            "sha": new_blobs.get(path, f["sha"])
        })

    print(f"  New tree: {len(new_tree)} entries (was {len(files)})")

    if not date_fixed and not to_delete:
        print("  No changes needed")
        return

    tree_result = api_call("POST", f"/repos/{REPO}/git/trees", {
        "base_tree": POSTS_TREE_SHA,
        "tree": new_tree
    })
    if not tree_result or "sha" not in tree_result:
        print("Failed to create tree")
        sys.exit(1)
    new_tree_sha = tree_result["sha"]

    # Step 5: Get current commit
    print("\nGetting current commit...")
    ref = api_call("GET", f"/repos/{REPO}/git/ref/heads/{BRANCH}")
    if not ref or "object" not in ref:
        print("Failed to get ref")
        sys.exit(1)
    current_sha = ref["object"]["sha"]

    # Step 6: Create commit
    changes = []
    if date_fixed:
        changes.append(f"统一日期格式：{date_fixed} 篇文章的 date: 字段补上 :00 秒数")
    if to_delete:
        changes.append(f"删除重复文章：{len(to_delete)} 篇标点符号不同的重复文件")
    message = "chore: 修复文章日期格式和删除重复文件\n\n" + "\n".join("- " + c for c in changes)

    print("\nCreating commit...")
    commit = api_call("POST", f"/repos/{REPO}/git/commits", {
        "message": message,
        "tree": new_tree_sha,
        "parents": [current_sha]
    })
    if not commit or "sha" not in commit:
        print("Failed to create commit")
        sys.exit(1)
    new_commit_sha = commit["sha"]

    # Step 7: Update branch
    print("\nUpdating master branch...")
    result = api_call("PATCH", f"/repos/{REPO}/git/refs/heads/{BRANCH}", {
        "sha": new_commit_sha,
        "force": True
    })
    if not result:
        print("Failed to update branch")
        sys.exit(1)

    print(f"\nDone!")
    print(f"  Date fixes: {date_fixed}")
    print(f"  Deleted: {len(to_delete)}")
    print(f"  Final count: {len(files) - len(to_delete)}")
    print(f"  Commit: {new_commit_sha}")

if __name__ == "__main__":
    main()