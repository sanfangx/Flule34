import sqlite3
import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Starting precise Danbooru Artist category matching...", flush=True)

db_path = r'C:\Users\沙银\.gemini\antigravity\scratch\ffdkj_tags\ffdkj-Danbooru_Tag-Chinese-English-Translation-Table-main\tag.sqlite'
r34_csv = 'assets/tags/rule34video_tags_zh.csv'

# 1. Load exact Danbooru Tag Categories
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Category 1 = Artist tags in Danbooru!
cursor.execute("SELECT name FROM tags WHERE category = 1")
danbooru_artists = set()
for (name,) in cursor:
    n = str(name).strip().lower()
    danbooru_artists.add(n)
    danbooru_artists.add(n.replace('_', ' '))

print(f"Loaded {len(danbooru_artists)} verified artist tags from Danbooru category 1.")

# Category 0, 3, 4, 5 = General, Series, Character, Copyright tags!
cursor.execute("SELECT name, cn_name FROM tags WHERE category != 1 AND cn_name IS NOT NULL AND cn_name != ''")
danbooru_non_artists = {}
for name, cn_name in cursor:
    n = str(name).strip().lower()
    c = str(cn_name).strip()
    danbooru_non_artists[n] = c
    danbooru_non_artists[n.replace('_', ' ')] = c

print(f"Loaded {len(danbooru_non_artists)} non-artist tags from Danbooru.")

conn.close()

with open(r34_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

translated_count = 0
artist_identified = 0

for row in rows:
    if row[1] == row[2]:
        name = row[1].strip()
        norm = name.lower()

        # Check Danbooru verified category
        if norm in danbooru_non_artists:
            row[2] = danbooru_non_artists[norm]
            translated_count += 1
            continue

        if norm in danbooru_artists:
            artist_identified += 1
            continue

        # Check suffixes/infixes that explicitly mean artist
        if norm.endswith(' (artist)') or norm.endswith(' sfm') or norm.endswith(' va') or norm.endswith(' 3d') or ' (peculiart)' in norm or ' (slipperyt)' in norm or ' (slyxxx24)' in norm or ' (woebeeme)' in norm:
            artist_identified += 1
            continue

print(f"Danbooru category check done: Translated {translated_count} tags, verified {artist_identified} artist tags!", flush=True)

with open(r34_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in rows:
        writer.writerow(r)

with open('rule34video_tags_zh.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in rows:
        writer.writerow(r)
