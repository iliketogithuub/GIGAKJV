#!/usr/bin/env python3
import os
import re

BOOKS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "books"))

# Direct mapping for words that do not follow the simple (\w+ed)st -> \w+ed rule
DIRECT_MAP = {
    'thyself': 'yourself',
    'wast': 'were',
    'saidst': 'said',
    'laidst': 'laid',
    'layedst': 'laid',
    'knewst': 'knew',
    'sawst': 'saw',
    'shewedst': 'showed',
    'showedst': 'showed',
}

def preserve_case(old, new):
    if old.isupper():
        return new.upper()
    if old and old[0].isupper():
        return new[0].upper() + new[1:]
    return new

def apply_fixes(text):
    lines = text.split('\n')
    new_lines = []
    
    for line in lines:
        # Skip comparison blocks and insights
        if any(x in line for x in ['[Operational Insight:', 'KJV Skeleton:', 'Traditional KJV:', 'Classic KJV:']):
            new_lines.append(line)
            continue
        
        # Skip headers
        if line.startswith('#'):
            new_lines.append(line)
            continue
            
        # Apply direct replacements first
        for old, new in DIRECT_MAP.items():
            line = re.sub(
                r'\b' + re.escape(old) + r'\b',
                lambda m, n=new: preserve_case(m.group(0), n),
                line,
                flags=re.IGNORECASE
            )
            
        # Apply regex for (\w+ed)st -> \w+ed (e.g. cursedst -> cursed)
        line = re.sub(
            r'\b(\w+ed)st\b',
            lambda m: preserve_case(m.group(0), m.group(1)),
            line,
            flags=re.IGNORECASE
        )
        
        new_lines.append(line)
        
    return '\n'.join(new_lines)

def main():
    files = sorted([f for f in os.listdir(BOOKS_DIR) if f.endswith('.md')])
    print(f"Applying thyself and -st verb fixes across {len(files)} books...")
    
    modified_count = 0
    for fname in files:
        fpath = os.path.join(BOOKS_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = apply_fixes(content)
        if new_content != content:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            modified_count += 1
            print(f"  📖 {fname}: fixed")
            
    print(f"\nCompleted! Fixed pronouns/verbs in {modified_count} books.")

if __name__ == "__main__":
    main()
