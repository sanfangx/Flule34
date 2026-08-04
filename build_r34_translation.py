import sqlite3
import csv
import re

db_path = r'C:\Users\沙银\.gemini\antigravity\scratch\ffdkj_tags\ffdkj-Danbooru_Tag-Chinese-English-Translation-Table-main\tag.sqlite'
r34_csv = 'rule34video_tags.csv'
out_csv = 'rule34video_tags_zh.csv'
unmatched_csv = 'unmatched_tags.csv'

print("Loading Danbooru database...")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("SELECT name, cn_name FROM tags WHERE cn_name IS NOT NULL AND cn_name != ''")

danbooru = {}
for name, cn_name in cursor:
    name_str = str(name).strip().lower()
    cn_str = str(cn_name).strip()
    if name_str and cn_str:
        danbooru[name_str] = cn_str
        danbooru[name_str.replace('_', ' ')] = cn_str
        danbooru[name_str.replace(' ', '_')] = cn_str

conn.close()
print(f"Loaded {len(danbooru)} Danbooru dictionary entries.")

print("Matching Rule34Video tags...")
matched_count = 0
unmatched_tags = []
results = []

with open(r34_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader) # ID, Name, VideoCount
    
    for row in reader:
        if not row or len(row) < 3:
            continue
        tag_id, tag_name, count = row[0], row[1], row[2]
        norm_name = tag_name.strip().lower()
        
        cn_translation = ""
        
        # 1. Exact match
        if norm_name in danbooru:
            cn_translation = danbooru[norm_name]
        # 2. Try replacing space with underscore or vice versa
        elif norm_name.replace(' ', '_') in danbooru:
            cn_translation = danbooru[norm_name.replace(' ', '_')]
        # 3. Pattern match for Xboys, Xgirls, Xfutas, etc.
        elif re.match(r'^\d+boys$', norm_name):
            cn_translation = f"{norm_name[:-4]}男"
        elif re.match(r'^\d+girls$', norm_name):
            cn_translation = f"{norm_name[:-5]}女"
        elif re.match(r'^\d+futas$', norm_name):
            cn_translation = f"{norm_name[:-5]}扶他"
        # 4. Try base name if contains parenthetical (e.g., "zuko (avatar the last airbender)")
        elif '(' in norm_name:
            parts = norm_name.split('(')
            base = parts[0].strip()
            series = parts[1].replace(')', '').strip()
            
            base_cn = danbooru.get(base) or danbooru.get(base.replace(' ', '_'))
            series_cn = danbooru.get(series) or danbooru.get(series.replace(' ', '_'))
            
            if base_cn and series_cn:
                cn_translation = f"{base_cn} ({series_cn})"
            elif base_cn:
                cn_translation = f"{base_cn} ({series})"
            elif series_cn:
                cn_translation = f"{base} ({series_cn})"

        if cn_translation:
            matched_count += 1
            results.append((tag_id, tag_name, cn_translation, count))
        else:
            unmatched_tags.append((tag_id, tag_name, count))
            results.append((tag_id, tag_name, "", count))

print(f"Total tags: {len(results)}")
print(f"Successfully matched: {matched_count} ({matched_count / len(results) * 100:.2f}%)")
print(f"Unmatched tags: {len(unmatched_tags)}")

# Write current progress
with open(out_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Name', 'ChineseName', 'VideoCount'])
    for r in results:
        writer.writerow(r)

with open(unmatched_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Name', 'VideoCount'])
    for u in unmatched_tags:
        writer.writerow(u)

print("Saved current results to rule34video_tags_zh.csv and unmatched_tags.csv")
