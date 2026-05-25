#!/usr/bin/env python3
import os
import re

BOOKS_DIR = "/home/charlie/Desktop/Websites/BKJV/books"

# Whitelist of modern words ending in st (including plurals and possessives if any)
WHITELIST = {
    'first', 'must', 'just', 'trust', 'least', 'lost', 'most', 'beast', 'beasts',
    'priest', 'priests', 'west', 'rest', 'worst', 'guest', 'guests', 'nest', 'nests',
    'chest', 'chests', 'dust', 'east', 'last', 'past', 'fast', 'cast', 'post', 'posts',
    'cost', 'costs', 'list', 'lists', 'fist', 'fists', 'mist', 'mists', 'jest', 'jests',
    'wrest', 'wrests', 'forest', 'forests', 'tempest', 'tempests', 'request', 'requests',
    'honest', 'earnest', 'manifest', 'manifests', 'harvest', 'harvests', 'protest', 'protests',
    'contest', 'contests', 'digest', 'digests', 'suggest', 'suggests', 'invest', 'invests',
    'arrest', 'arrests', 'nearest', 'dearest', 'poorest', 'smallest', 'largest', 'hardest',
    'softest', 'richest', 'wisest', 'fastest', 'slowest', 'fairest', 'purest', 'interest',
    'interests', 'modest', 'closest', 'finest', 'bravest', 'truest', 'fullest', 'test', 'tests',
    'greatest', 'highest', 'lowest', 'deepest', 'strongest', 'longest', 'oldest', 'youngest',
    'sweetest', 'latest', 'chiefest', 'holiest', 'straitest', 'mightiest', 'eldest', 'goodliest',
    'valiantest', 'meetest', 'basest', 'choicest', 'faintest', 'fewest', 'detest', 'detests',
    'exist', 'exists', 'assist', 'assists', 'resist', 'resists', 'consist', 'consists',
    'insist', 'insists', 'persist', 'persists', 'christ', 'christs', 'midst', 'whilst', 'against',
    'amongst', 'boast', 'boasts', 'roast', 'roasts', 'blast', 'blasts', 'crest', 'crests',
    'frost', 'frosts', 'ghost', 'ghosts', 'host', 'hosts', 'post', 'posts', 'rust', 'crust', 'crusts',
    'thrust', 'thrusts', 'twist', 'twists', 'yeast', 'harvested', 'harvesting', 'manifested',
    'manifesting', 'protested', 'protesting', 'requested', 'requesting', 'trusted', 'trusting',
    'interested', 'interesting', 'exhaust', 'exhausts', 'forecast', 'forecasts', 'broadcast',
    'broadcasts', 'adjust', 'adjusts', 'boastful', 'robust', 'earnestness', 'priestly', 'priesthood',
    'restless', 'restoration', 'fasting', 'fasted',
}

def main():
    words = {}
    for filename in sorted(os.listdir(BOOKS_DIR)):
        if not filename.endswith('.md'):
            continue
        filepath = os.path.join(BOOKS_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all words ending in st (case-insensitive)
        for match in re.finditer(r'\b\w+st\b', content, re.IGNORECASE):
            word = match.group(0).lower()
            if word not in WHITELIST:
                # Exclude comparison lines
                line = content[:match.start()].count('\n') + 1
                line_text = content.split('\n')[line - 1]
                if any(x in line_text for x in ['[Operational Insight:', 'KJV Skeleton:', 'Traditional KJV:', 'Classic KJV:']):
                    continue
                words[word] = words.get(word, 0) + 1
                
    print("Found non-whitelisted words ending in -st:")
    for w, count in sorted(words.items(), key=lambda x: x[1], reverse=True):
        print(f"  {w}: {count} occurrences")

if __name__ == "__main__":
    main()
