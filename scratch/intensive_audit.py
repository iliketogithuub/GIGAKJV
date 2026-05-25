#!/usr/bin/env python3
import os
import re
import sys

BOOKS_DIR = "/home/charlie/Desktop/Websites/SKJV/books"

# Helper verbs (second person singular, etc.)
ARCHAIC_HELPERS = {
    'didst': r'\bdidst\b',
    'hadst': r'\bhadst\b',
    'wouldst': r'\bwouldst\b',
    'couldst': r'\bcouldst\b',
    'shouldst': r'\bshouldst\b',
    'shalt': r'\bshalt\b',
    'wilt': r'\bwilt\b',
    'art': r'\bart\b',
    'wert': r'\bwert\b',
    'canst': r'\bcanst\b',
    'hast': r'\bhast\b',
    'dost': r'\bdost\b',
}

# General KJV vocabulary archaisms
ARCHAIC_VOCAB = {
    'spake': r'\bspake\b',
    'slew': r'\bslew\b',
    'smote': r'\bsmote\b',
    'brake': r'\bbrake\b',
    'gat': r'\bgat\b',
    'begat': r'\bbegat\b',
    'holpen': r'\bholpen\b',
    'waxed': r'\bwaxed\b',
    'trow': r'\btrow\b',
    'wist': r'\bwist\b',
    'wot': r'\bwot\b',
    'twain': r'\btwain\b',
    'anon': r'\banon\b',
    'damsel': r'\bdamsel\b',
    'heretofore': r'\bheretofore\b',
    'hitherto': r'\bhitherto\b',
    'henceforth': r'\bhenceforth\b',
    'thenceforth': r'\bthenceforth\b',
    'thence': r'\bthence\b',
    'hence': r'\bhence\b',
    'whence': r'\bwhence\b',
    'whither': r'\bwhither\b',
    'thither': r'\bthither\b',
    'hither': r'\bhither\b',
    'eschew': r'\beschew\b',
    'peradventure': r'\bperadventure\b',
    'seemly': r'\bseemly\b',
    'unseemly': r'\bunseemly\b',
    'travail': r'\btravail\b',
    'subtilty': r'\bsubtilty\b',
    'divers': r'\bdivers\b',
    'oft': r'\boft\b',
    'ofttimes': r'\bofttimes\b',
    'shew': r'\bshew\b',
    'shewed': r'\bshewed\b',
    'shewing': r'\bshewing\b',
    'clave': r'\bclave\b',
    'superfluity': r'\bsuperfluity\b',
    'nought': r'\bnought\b',
    'naught': r'\bnaught\b',
    'matrix': r'\bmatrix\b',
    'concupiscence': r'\bconcupiscence\b',
    'froward': r'\bfroward\b',
    'goodman': r'\bgoodman\b',
    'howbeit': r'\bhowbeit\b',
    'similitude': r'\bsimilitude\b',
    'dearth': r'\bdearth\b',
    'afore': r'\bafore\b',
    'aforetime': r'\baforetime\b',
    'verily': r'\bverily\b',
    'wroth': r'\bwroth\b',
    'coms': r'\bcoms\b',
    'drivs': r'\bdrivs\b',
    'becoms': r'\bbecoms\b',
    'taks': r'\btaks\b',
    'maks': r'\bmaks\b',
    'defils': r'\bdefils\b',
    'ses': r'\bses\b',
    'gos': r'\bgos\b',
    'dos': r'\bdos\b',
    'givs': r'\bgivs\b',
    'livs': r'\blivs\b',
}

# Words that end in -eth / -est that are forbidden (general search)
# We exclude the whitelists from verify_translation.py
ETH_WHITELIST = {
    'teeth', 'seth', 'japheth', 'nazareth', 'bethlehem', 'shibboleth',
    'seventh', 'twentieth', 'thirtieth', 'fortieth', 'fiftieth',
    'sixtieth', 'seventieth', 'eightieth', 'ninetieth', 'hundredth',
    'elizabeth', 'hazareth', 'neth', 'beth', 'meth',
}

EST_WHITELIST = {
    'greatest', 'highest', 'lowest', 'deepest', 'strongest', 'longest',
    'oldest', 'youngest', 'sweetest', 'latest', 'chiefest', 'least',
    'best', 'west', 'rest', 'priest', 'forest', 'tempest', 'request',
    'honest', 'earnest', 'manifest', 'harvest', 'guest', 'nest', 'test',
    'chest', 'crest', 'jest', 'protest', 'contest', 'digest', 'suggest',
    'invest', 'arrest', 'nearest', 'dearest', 'poorest', 'smallest',
    'largest', 'hardest', 'softest', 'richest', 'wisest', 'fastest',
    'slowest', 'fairest', 'purest', 'worst', 'first', 'interest',
    'modest', 'closest', 'finest', 'bravest', 'truest', 'fullest',
    'lightest', 'detest', 'holiest', 'straitest', 'mightiest', 'eldest',
    'goodliest', 'valiantest', 'meetest', 'basest', 'choicest', 'faintest',
    'fewest', 'wrest', 'dishonest'
}

def check_file(fname):
    fpath = os.path.join(BOOKS_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Strip operational insights and translation skeletons for clean auditing of translated scripture text
    cleaned = re.sub(r'\[Operational Insight:[^\]]*\]', '', content)
    cleaned = re.sub(r'Traditional KJV:[^\n]*', '', cleaned)
    cleaned = re.sub(r'KJV Skeleton:[^\n]*', '', cleaned)
    
    lines = cleaned.split('\n')
    
    issues = []
    
    # Check header
    if not re.match(r'^#\s+.*?\s+-\s+Simple\s+King\s+James\s+Version\s+\(SKJV\)', content):
        issues.append(("HEADER", "Missing or invalid book header at line 1"))
        
    # Check eof marker
    if "## eof" not in content.lower():
        issues.append(("EOF", "Missing '## eof' marker at the end of the file"))
        
    # Scan line by line for specific archaisms
    for idx, line in enumerate(lines, 1):
        # Scan helpers
        for word, pattern in ARCHAIC_HELPERS.items():
            if re.search(pattern, line, re.IGNORECASE):
                issues.append(("ARCHAIC_HELPER", f"Line {idx}: Found helper '{word}' in \"{line.strip()}\""))
                
        # Scan vocab
        for word, pattern in ARCHAIC_VOCAB.items():
            if re.search(pattern, line, re.IGNORECASE):
                issues.append(("ARCHAIC_VOCAB", f"Line {idx}: Found word '{word}' in \"{line.strip()}\""))
                
        # Scan general -eth endings
        for match in re.finditer(r'\b\w+eth\b', line, re.IGNORECASE):
            word = match.group(0).lower()
            if word not in ETH_WHITELIST:
                issues.append(("ETH_ENDING", f"Line {idx}: Found suspect -eth word '{word}' in \"{line.strip()}\""))
                
        # Scan general -est endings
        for match in re.finditer(r'\b\w+est\b', line, re.IGNORECASE):
            word = match.group(0).lower()
            if word not in EST_WHITELIST:
                # Extra check to ensure it doesn't end in typical suffixes like -ist, -est superlatives we might have missed
                issues.append(("EST_ENDING", f"Line {idx}: Found suspect -est word '{word}' in \"{line.strip()}\""))
                
        # Check for duplicate punctuation or formatting weirdness
        if "  " in line:
            issues.append(("DOUBLE_SPACE", f"Line {idx}: Double space in \"{line.strip()}\""))
        if re.search(r'[,.;:?!][,.;:?!]', line):
            # Allow "..." or similar if deliberate, but check for things like ",," or ".."
            if "..." not in line:
                issues.append(("DOUBLE_PUNCTUATION", f"Line {idx}: Double punctuation in \"{line.strip()}\""))
                
    return issues

def main():
    files = sorted([f for f in os.listdir(BOOKS_DIR) if f.endswith('.md')])
    log_path = "/home/charlie/Desktop/Websites/SKJV/scratch/audit_details.log"
    
    total_issues = 0
    by_category = {}
    
    with open(log_path, 'w', encoding='utf-8') as log_file:
        log_file.write("=== SKJV INTENSIVE AUDIT DETAILS ===\n\n")
        log_file.write(f"Auditing {len(files)} files in {BOOKS_DIR}...\n")
        
        for fname in files:
            issues = check_file(fname)
            if issues:
                log_file.write(f"\n📂 {fname}:\n")
                for cat, desc in issues:
                    log_file.write(f"  [{cat}] {desc}\n")
                    total_issues += 1
                    by_category[cat] = by_category.get(cat, 0) + 1
                    
        log_file.write("\n" + "="*40 + "\n")
        log_file.write("AUDIT SUMMARY\n")
        log_file.write("="*40 + "\n")
        log_file.write(f"Total issues found: {total_issues}\n")
        for cat, count in by_category.items():
            log_file.write(f"  {cat}: {count}\n")
            
    print(f"Intensive audit complete. Detailed log written to: {log_path}")
    print("\n" + "="*40)
    print("AUDIT SUMMARY")
    print("="*40)
    print(f"Total issues found: {total_issues}")
    for cat, count in by_category.items():
        print(f"  {cat}: {count}")

if __name__ == "__main__":
    main()
