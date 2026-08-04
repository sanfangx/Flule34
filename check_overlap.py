import csv

danbooru = {}
with open('assets/tags/danbooru-10w-zh_cn.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 2:
            danbooru[row[0].strip().replace(' ', '_')] = row[1].strip()
            # Also store the space version just in case
            danbooru[row[0].strip().replace('_', ' ')] = row[1].strip()

r34_tags = []
with open('rule34video_tags.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    for row in reader:
        r34_tags.append(row[1].strip())

matched = 0
unmatched = []
for t in r34_tags:
    if t in danbooru or t.replace(' ', '_') in danbooru:
        matched += 1
    else:
        unmatched.append(t)

print(f"Total Rule34Video tags: {len(r34_tags)}")
print(f"Matched with Danbooru: {matched}")
print(f"Unmatched: {len(unmatched)}")
print(f"Sample unmatched: {unmatched[:20]}")
