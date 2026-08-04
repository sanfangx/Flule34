import csv
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Regular expressions and smart LLM transformation rules for remaining untranslated tags
def llm_smart_translate(name):
    norm = name.strip().lower()

    # Numbers + terms (e.g. 1boy1girl, 3boys1girl, 2animals, 4fingers, 5toes)
    m = re.findall(r'(\d+)\s*([a-zA-Z]+)', norm)
    if m and len("".join([f"{n}{t}" for n, t in m])) == len(norm.replace(' ', '')):
        t_map = {
            'boy': '男', 'boys': '男',
            'girl': '女', 'girls': '女',
            'futa': '扶他', 'futas': '扶他',
            'female': '女性', 'females': '女性',
            'male': '男性', 'males': '男性',
            'human': '人类', 'humans': '人类',
            'elf': '精灵', 'elves': '精灵',
            'monster': '怪物', 'monsters': '怪物',
            'orc': '兽人', 'orcs': '兽人',
            'robot': '机器人', 'robots': '机器人',
            'animal': '动物', 'animals': '动物',
            'toe': '脚趾', 'toes': '脚趾',
            'finger': '手指', 'fingers': '手指',
        }
        if all(t in t_map for _, t in m):
            return "".join([f"{n}{t_map[t]}" for n, t in m])

    # NSFW Descriptor Rules
    if 'fuck' in norm and not '(' in norm:
        clean = norm.replace(' fuck', '').replace('fuck ', '').replace('fuck', '')
        if clean:
            return f"{clean}交"

    if norm.endswith(' job'):
        clean = norm[:-4].strip()
        return f"{clean}交"

    return None

out_csv = 'assets/tags/rule34video_tags_zh.csv'
with open(out_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

updated_count = 0
for row in rows:
    if row[1] == row[2]:
        smart_res = llm_smart_translate(row[1])
        if smart_res:
            row[2] = smart_res
            updated_count += 1

print(f"Applied LLM smart transformation rules: Updated {updated_count} tags!")

with open(out_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in rows:
        writer.writerow(r)

with open('rule34video_tags_zh.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in rows:
        writer.writerow(r)
