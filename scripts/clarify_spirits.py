#!/usr/bin/env python3
import os
import re

BOOKS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "books"))

# Specific verses where "my spirit" / "My spirit" refers to God (Holy Spirit)
GOD_MY_SPIRIT_VERSES = {
    "Genesis 6:3", "Proverbs 1:23", "Isaiah 30:1", "Isaiah 42:1", "Isaiah 44:3", 
    "Isaiah 59:21", "Ezekiel 36:27", "Ezekiel 37:14", "Ezekiel 39:29", "Joel 2:28", 
    "Joel 2:29", "Haggai 2:5", "Zechariah 4:6", "Zechariah 6:8", "Matthew 12:18", 
    "Acts 2:17", "Acts 2:18"
}

# Specific verses where "his spirit" / "His spirit" refers to God (Holy Spirit)
GOD_HIS_SPIRIT_VERSES = {
    "Numbers 11:29", "Nehemiah 9:30", "Isaiah 34:16", "Isaiah 48:16", "Zechariah 7:12",
    "Romans 8:9", "Romans 8:11", "Ephesians 3:16", "1 John 4:13"
}

def preserve_case(old, new):
    if old.isupper():
        return new.upper()
    if old and old[0].isupper():
        return new[0].upper() + new[1:]
    return new

def clarify_spirit_in_line(line, book_name, chapter_num, v_num):
    # Skip comparison blocks or insights
    if "[Operational Insight:" in line or "KJV Skeleton:" in line or "Traditional KJV:" in line or "Classic KJV:" in line:
        return line
        
    # 1. Replace "ghost" with "Holy Spirit"
    line = re.sub(r'\byielded? up the ghost\b', lambda m: preserve_case(m.group(0), 'yielded up the Holy Spirit'), line, flags=re.IGNORECASE)
    line = re.sub(r'\bgaves? up the ghost\b', lambda m: preserve_case(m.group(0), 'gave up the Holy Spirit'), line, flags=re.IGNORECASE)
    line = re.sub(r'\bgiven up the ghost\b', lambda m: preserve_case(m.group(0), 'given up the Holy Spirit'), line, flags=re.IGNORECASE)
    line = re.sub(r'\bgives? up the ghost\b', lambda m: preserve_case(m.group(0), 'gives up the Holy Spirit'), line, flags=re.IGNORECASE)
    line = re.sub(r'\bgiving up of the ghost\b', lambda m: preserve_case(m.group(0), 'giving up of the Holy Spirit'), line, flags=re.IGNORECASE)
    line = re.sub(r'\bghost\b', lambda m: preserve_case(m.group(0), 'Holy Spirit'), line, flags=re.IGNORECASE)

    # 2. Context-aware "spirit" -> "Holy Spirit" or "human spirit"
    verse_key = f"{book_name} {chapter_num}:{v_num}"
    
    # Standard multi-word patterns first
    line = re.sub(r'\bSpirit of God\b', 'Holy Spirit of God', line)
    line = re.sub(r'\bspirit of God\b', 'Holy Spirit of God', line)
    line = re.sub(r'\bSpirit of the Lord\b', 'Holy Spirit of the Lord', line)
    line = re.sub(r'\bspirit of the Lord\b', 'Holy Spirit of the Lord', line)
    line = re.sub(r'\bSpirit of your Father\b', 'Holy Spirit of your Father', line)
    line = re.sub(r'\bSpirit of the living God\b', 'Holy Spirit of the living God', line)
    line = re.sub(r'\bSpirit of truth\b', 'Holy Spirit of truth', line)
    line = re.sub(r'\bSpirit of holiness\b', 'Holy Spirit of holiness', line)
    line = re.sub(r'\bSpirit of life\b', 'Holy Spirit of life', line)
    line = re.sub(r'\bSpirit of Christ\b', 'Holy Spirit of Christ', line)
    line = re.sub(r'\bSpirit of grace\b', 'Holy Spirit of grace', line)
    line = re.sub(r'\bSpirit of glory\b', 'Holy Spirit of glory', line)
    line = re.sub(r'\bSpirit of revelation\b', 'Holy Spirit of revelation', line)
    line = re.sub(r'\bSpirit of adoption\b', 'Holy Spirit of adoption', line)
    line = re.sub(r'\bSpirit of promise\b', 'Holy Spirit of promise', line)
    line = re.sub(r'\bsame Spirit\b', 'same Holy Spirit', line)
    line = re.sub(r'\bone Spirit\b', 'one Holy Spirit', line)
    line = re.sub(r'\bselfsame Spirit\b', 'selfsame Holy Spirit', line)
    line = re.sub(r'\bquickening spirit\b', 'life-giving Holy Spirit', line, flags=re.IGNORECASE)

    # Standard human spirit patterns
    line = re.sub(r'\bpoor in spirit\b', 'poor in their human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bcontrite spirit\b', 'contrite human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bbroken spirit\b', 'broken human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bhumble spirit\b', 'humble human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bhaughty spirit\b', 'haughty human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bright spirit\b', 'right human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bfaithful spirit\b', 'faithful human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bwounded spirit\b', 'wounded human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bexcellent spirit\b', 'excellent human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bpatient in spirit\b', 'patient in human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bproud in spirit\b', 'proud in human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bhasty in spirit\b', 'hasty in human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\banguish of spirit\b', 'anguish of human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bfervent in (?:the )?spirit\b', 'fervent in human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bgrew strong in spirit\b', 'grew strong in human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bwaxed strong in spirit\b', 'grew strong in human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bspirit of man\b', 'human spirit of man', line, flags=re.IGNORECASE)
    line = re.sub(r'\bspirit of a man\b', 'human spirit of a man', line, flags=re.IGNORECASE)
    line = re.sub(r'\bspirit indeed is willing\b', 'human spirit indeed is willing', line, flags=re.IGNORECASE)
    line = re.sub(r'\bspirit truly is ready\b', 'human spirit truly is ready', line, flags=re.IGNORECASE)
    line = re.sub(r'\bbody and spirit\b', 'body and human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bflesh and spirit\b', 'flesh and human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bsoul and spirit\b', 'soul and human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bbody without the spirit\b', 'body without the human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bspirit of the humble\b', 'human spirit of the humble', line, flags=re.IGNORECASE)
    line = re.sub(r'\bspirit and soul and body\b', 'human spirit, soul, and body', line, flags=re.IGNORECASE)
    line = re.sub(r'\bspirits of just men\b', 'human spirits of righteous men', line, flags=re.IGNORECASE)
    line = re.sub(r'\bspirit of Cyrus\b', 'human spirit of Cyrus', line, flags=re.IGNORECASE)
    line = re.sub(r'\bwhose spirit God had raised\b', 'whose human spirit God had raised', line, flags=re.IGNORECASE)
    line = re.sub(r'\bspirit of Jacob\b', 'human spirit of Jacob', line, flags=re.IGNORECASE)
    line = re.sub(r'\bspirit of Elihu\b', 'human spirit of Elihu', line, flags=re.IGNORECASE)
    line = re.sub(r'\bspirit of Joshua\b', 'human spirit of Joshua', line, flags=re.IGNORECASE)
    line = re.sub(r'\bspirit of Elijah\b', 'human spirit of Elijah', line, flags=re.IGNORECASE)
    line = re.sub(r'\bgroaned in the spirit\b', 'groaned in His human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bpurposed in the spirit\b', 'purposed in his human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bbound in the spirit\b', 'bound in my human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bholy both in body and in spirit\b', 'holy both in body and in human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bcleansing from all filthiness of the flesh and spirit\b', 'cleansing from all filthiness of the flesh and human spirit', line, flags=re.IGNORECASE)
    line = re.sub(r'\bmeek and quiet spirit\b', 'meek and quiet human spirit', line, flags=re.IGNORECASE)

    # 3. Handle pronouns (my spirit, his spirit, your spirit, etc.)
    # "my spirit"
    if "my spirit" in line.lower():
        if verse_key in GOD_MY_SPIRIT_VERSES:
            line = re.sub(r'\bmy spirit\b', 'my Holy Spirit', line, flags=re.IGNORECASE)
        else:
            line = re.sub(r'\bmy spirit\b', 'my human spirit', line, flags=re.IGNORECASE)
            
    # "his spirit"
    if "his spirit" in line.lower():
        if verse_key in GOD_HIS_SPIRIT_VERSES:
            line = re.sub(r'\bhis spirit\b', 'His Holy Spirit', line, flags=re.IGNORECASE)
        else:
            line = re.sub(r'\bhis spirit\b', 'his human spirit', line, flags=re.IGNORECASE)
            
    # "your spirit"
    if "your spirit" in line.lower():
        if verse_key == "Psalms 139:7" or verse_key == "Nehemiah 9:30":
            line = re.sub(r'\byour spirit\b', 'your Holy Spirit', line, flags=re.IGNORECASE)
        else:
            line = re.sub(r'\byour spirit\b', 'your human spirit', line, flags=re.IGNORECASE)
            
    # "our spirit"
    line = re.sub(r'\bour spirit\b', 'our human spirit', line, flags=re.IGNORECASE)
    
    # "their spirit"
    line = re.sub(r'\btheir spirit\b', 'their human spirit', line, flags=re.IGNORECASE)

    # 4. Standard general replacements in the New Testament
    # In NT epistles & Acts, "the Spirit" or "the spirit" almost always refers to Holy Spirit
    nt_books = {
        "Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians", "2 Corinthians",
        "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians",
        "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter",
        "1 John", "2 John", "3 John", "Jude", "Revelation"
    }
    
    # Check if this book is in NT
    is_nt = any(nt_b in book_name for nt_b in nt_books)
    if is_nt:
        # Exclude known demon spirits and human spirits in NT
        if not re.search(r'\bunclean spirits?\b|\bevil spirits?\b|\bfamiliar spirits?\b|\blying spirits?\b|\bdeceiving spirits?\b', line, re.I):
            # Replace "the Spirit" / "the spirit" with "the Holy Spirit"
            line = re.sub(r'\bthe Spirit\b', 'the Holy Spirit', line)
            # Make sure we don't accidentally turn "unclean spirit" or similar into "unclean Holy Spirit" if casing was weird
            line = re.sub(r'\bthe spirit\b', 'the Holy Spirit', line)
            
    return line

def process_file(fname):
    fpath = os.path.join(BOOKS_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    
    # Identify book name
    book_match = re.match(r'^#\s+(.*?)\s+-\s+(?:Simple|Based)', content)
    book_name = book_match.group(1).strip() if book_match else fname
    
    lines = content.split('\n')
    new_lines = []
    
    chapter_num = 0
    v_num = 0
    
    for line in lines:
        # Check chapter header
        chap_match = re.match(r'^##\s+.*?\s+Chapter\s+(\d+)', line)
        if chap_match:
            chapter_num = int(chap_match.group(1))
            new_lines.append(line)
            continue
            
        # Check verse line
        verse_match = re.match(r'^(\d+)\s+(.*)$', line)
        if verse_match:
            v_num = int(verse_match.group(1))
            line = clarify_spirit_in_line(line, book_name, chapter_num, v_num)
            
        new_lines.append(line)
        
    new_content = '\n'.join(new_lines)
    if new_content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    files = sorted([f for f in os.listdir(BOOKS_DIR) if f.endswith('.md')])
    print(f"Clarifying 'spirit' / 'ghost' across {len(files)} books...")
    
    modified_count = 0
    for fname in files:
        if process_file(fname):
            print(f"  🔧 {fname}: clarified spirits")
            modified_count += 1
            
    print(f"\nCompleted! Clarified spirits in {modified_count} books.")

if __name__ == "__main__":
    main()
