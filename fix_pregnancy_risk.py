import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

r34_csv = 'assets/tags/rule34video_tags_zh.csv'
with open(r34_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

fixes = {
    'pregnancy risk': '怀孕风险/中出怀胎风险',
    'impregnancy risk': '受孕风险/怀孕风险',
    'pregnancyrisk': '怀孕风险/中出怀胎风险',
    'impregnancyrisk': '受孕风险/怀孕风险',
}

count = 0
for row in rows:
    norm = row[1].strip().lower()
    if norm in fixes:
        row[2] = fixes[norm]
        count += 1
    elif 'pregnancy risk' in norm or 'impregnancy risk' in norm:
        row[2] = row[2].replace('pregnancyrisk', '怀孕风险').replace('impregnancyrisk', '受孕风险')
        count += 1

print(f"Fixed {count} pregnancy risk tags!")

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
