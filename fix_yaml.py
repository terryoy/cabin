#!/usr/bin/env python3
"""Find and fix all YAML issues in Jekyll post files."""
import os
import re
import sys

POSTS_DIR = "/root/data/disk/projects/cabin/_posts"

def find_yaml_issues():
    """Find all files with YAML issues in their front matter."""
    files = [f for f in os.listdir(POSTS_DIR) if f.endswith('.md')]
    issues = []
    
    for fname in sorted(files):
        path = os.path.join(POSTS_DIR, fname)
        with open(path, 'r', encoding='utf-8', errors='replace') as fh:
            content = fh.read()
        
        # Extract YAML front matter
        yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not yaml_match:
            continue
        
        yaml_text = yaml_match.group(1)
        
        # Check for title issues
        title_match = re.search(r'^title:\s*(.*?)$', yaml_text, re.MULTILINE)
        if not title_match:
            issues.append((fname, "NO_TITLE", ""))
            continue
        
        title_value = title_match.group(1)
        
        # Check if already quoted
        already_quoted = (title_value.startswith('"') and title_value.endswith('"')) or \
                         (title_value.startswith("'") and title_value.endswith("'"))
        
        if already_quoted:
            continue
        
        # Check for YAML special characters that need quoting
        if re.search(r'[\[\]\{\}\#,&\*\?\|<>=!%@`:]', title_value):
            issues.append((fname, "UNQUOTED_SPECIAL", title_value))
    
    return issues

def fix_issues(issues):
    """Fix all identified YAML issues."""
    import shutil
    
    for fname, issue_type, title_value in issues:
        path = os.path.join(POSTS_DIR, fname)
        with open(path, 'r', encoding='utf-8', errors='replace') as fh:
            content = fh.read()
        
        if issue_type == "UNQUOTED_SPECIAL":
            # Quote the title value
            # Escape any backslashes and double quotes in the title
            escaped_title = title_value.replace('\\', '\\\\').replace('"', '\\"')
            old_line = f"title: {title_value}"
            new_line = f'title: "{title_value}"'
            content = content.replace(old_line, new_line, 1)
            
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(content)
            print(f"  Fixed: {fname}")
            print(f"    Old: {old_line}")
            print(f"    New: {new_line}")
    
    return len(issues)

def main():
    print("Scanning for YAML issues...")
    issues = find_yaml_issues()
    print(f"Found {len(issues)} issues:")
    for fname, itype, tval in issues:
        print(f"  [{itype}] {fname}: {tval}")
    
    if not issues:
        print("No issues found!")
        return
    
    # Also fix date-only and single-hour issues
    print("\nAlso fixing date format issues...")
    date_issues = []
    for fname in sorted(os.listdir(POSTS_DIR)):
        if not fname.endswith('.md'):
            continue
        path = os.path.join(POSTS_DIR, fname)
        with open(path, 'r', encoding='utf-8', errors='replace') as fh:
            content = fh.read()
        
        # Fix date: 2020-02-13 (date only, no time)
        content = re.sub(
            r'^(date:\s*[\'"]?(\d{4}-\d{2}-\d{2})\s*)[\'"]?\s*$',
            r'\1 00:00:00',
            content,
            flags=re.MULTILINE
        )
        
        # Fix date: 2020-03-04 9:33 (single digit hour)
        content = re.sub(
            r'^(date:\s*[\'"]?)(\d{4}-\d{2}-\d{2}\s+)(\d):(\d{2})(:\d{2})?[\'"]?\s*$',
            r'\1\20\3:\4:00',
            content,
            flags=re.MULTILINE
        )
        
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(content)
    
    print(f"Fixed {len(issues)} title quoting issues")
    print("Date issues also fixed")

if __name__ == "__main__":
    main()