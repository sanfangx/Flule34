import sqlite3
import csv
import re
import urllib.request
import urllib.parse
import json
import time

db_path = r'C:\Users\沙银\.gemini\antigravity\scratch\ffdkj_tags\ffdkj-Danbooru_Tag-Chinese-English-Translation-Table-main\tag.sqlite'
r34_csv = 'rule34video_tags.csv'
out_csv = 'rule34video_tags_zh.csv'

print("1. Loading Danbooru database...", flush=True)
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

aliases = {
    'evangelion': '新世纪福音战士',
    'kono subarashii': '为美好的世界献上祝福！',
    'honkai star rail': '崩坏：星穹铁道',
    'honkai impact': '崩坏3',
    'azur lane': '碧蓝航线',
    'genshin impact': '原神',
    'blue archive': '蔚蓝档案',
    'league of legends': '英雄联盟',
    'overwatch': '守望先锋',
    'pokemon': '宝可梦',
    'fate': 'Fate系列',
    'rwby': 'RWBY',
    'fnaf': '玩具熊的五夜后宫',
}
for k, v in list(aliases.items()):
    aliases[k.replace(' ', '_')] = v

term_map = {
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

def translate_batch(text_list):
    if not text_list:
        return []
    payload = " ||| ".join(text_list)
    try:
        q = urllib.parse.quote(payload)
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t&q={q}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        res = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
        data = json.loads(res)
        full = "".join([item[0] for item in data[0] if item and item[0]])
        parts = [p.strip() for p in full.split('|||')]
        if len(parts) == len(text_list):
            return parts
    except Exception as e:
        print(f"  Batch error: {e}", flush=True)
    
    # Fallback to single requests
    res_list = []
    for item in text_list:
        try:
            q = urllib.parse.quote(item)
            url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t&q={q}"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            res = urllib.request.urlopen(req, timeout=5).read().decode('utf-8')
            data = json.loads(res)
            res_list.append("".join([x[0] for x in data[0] if x and x[0]]).strip())
        except:
            res_list.append(item)
        time.sleep(0.05)
    return res_list

def main():
    r34_rows = []
    with open(r34_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        r34_rows = list(reader)

    translations = {}
    unmatched = []

    for row in r34_rows:
        tag_name = row[1]
        norm = tag_name.strip().lower()

        # 1. Exact Danbooru
        if norm in danbooru:
            translations[tag_name] = danbooru[norm]
            continue
            
        # 2. Pattern
        m_combo = re.findall(r'(\d+)\s*([a-zA-Z]+)', norm)
        if m_combo and len("".join([f"{num}{term}" for num, term in m_combo])) == len(norm.replace(' ', '')):
            if all(term in term_map for _, term in m_combo):
                translations[tag_name] = "".join([f"{num}{term_map[term]}" for num, term in m_combo])
                continue

        # 3. Parentheses split
        if '(' in norm and norm.endswith(')'):
            base = norm[:norm.rfind('(')].strip()
            series = norm[norm.rfind('(')+1:-1].strip()

            base_cn = danbooru.get(base) or danbooru.get(base.replace(' ', '_'))
            series_cn = aliases.get(series) or danbooru.get(series) or danbooru.get(series.replace(' ', '_'))

            if base_cn and series_cn:
                translations[tag_name] = f"{base_cn} ({series_cn})"
                continue

        unmatched.append(tag_name)

    print(f"Matched {len(translations)} tags via DB & patterns.", flush=True)
    print(f"Translating remaining {len(unmatched)} tags via batch API...", flush=True)

    batch_size = 40
    for i in range(0, len(unmatched), batch_size):
        chunk = unmatched[i:i + batch_size]
        print(f"Batch {i//batch_size + 1}/{(len(unmatched) + batch_size - 1)//batch_size}...", flush=True)
        translated_chunk = translate_batch(chunk)
        for original, trans in zip(chunk, translated_chunk):
            translations[original] = trans
        time.sleep(0.1)

    print("Saving to rule34video_tags_zh.csv...", flush=True)
    with open(out_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Name', 'ChineseName', 'VideoCount'])
        for row in r34_rows:
            tag_id, tag_name, count = row[0], row[1], row[2]
            cn_trans = translations.get(tag_name, tag_name)
            writer.writerow([tag_id, tag_name, cn_trans, count])

    print("All done!", flush=True)

if __name__ == '__main__':
    main()
