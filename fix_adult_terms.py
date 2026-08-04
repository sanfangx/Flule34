import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

csv_path = 'assets/tags/rule34video_tags_zh.csv'
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

fixed_count = 0
for row in rows:
    name = row[1].strip()
    cn = row[2].strip()
    
    # Special manual replacements for adult terms
    if name.lower() == 'titty fuck':
        row[2] = '乳交'
        fixed_count += 1
    elif name.lower() == 'brain fuck':
        row[2] = '脑交'
        fixed_count += 1
    elif name.lower() == 'fuck train':
        row[2] = '轮奸/连续交配'
        fixed_count += 1
    elif name.lower() == 'fuckmeat':
        row[2] = '肉便器'
        fixed_count += 1
    elif name.lower() == 'horse fuck':
        row[2] = '马交'
        fixed_count += 1
    elif name.lower() == 'knot fucking':
        row[2] = '打结交配'
        fixed_count += 1
    elif name.lower() == 'machine fuck':
        row[2] = '机器插穴'
        fixed_count += 1
    elif name.lower() == 'monster fuck':
        row[2] = '怪物交配'
        fixed_count += 1
    elif name.lower() == 'navel fuck':
        row[2] = '肚脐交'
        fixed_count += 1
    elif name.lower() == 'snout fuck':
        row[2] = '兽嘴插穴'
        fixed_count += 1
    elif ' fuck' in name.lower() and ('他妈的' in cn or '该死' in cn):
        # Replace "... fuck" -> "...交" or "...插"
        base = name.lower().replace(' fuck', '').strip()
        row[2] = cn.replace('他妈的', '').replace('该死', '').strip() + '交'
        fixed_count += 1

print(f"Fixed {fixed_count} bad adult translations!")

with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in rows:
        writer.writerow(r)

# Also update the root CSV file
with open('rule34video_tags_zh.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in rows:
        writer.writerow(r)

print("Saved fixes to CSV files!")
