import sqlite3
import csv
import re
import urllib.request
import urllib.parse
import json
import time
import sys
from concurrent.futures import ThreadPoolExecutor

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
print(f"   Loaded {len(danbooru)} Danbooru dictionary entries.", flush=True)

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

def translate_single(text):
    if not text:
        return text
    try:
        q = urllib.parse.quote(text)
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t&q={q}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        res = urllib.request.urlopen(req, timeout=5).read().decode('utf-8')
        data = json.loads(res)
        translated = "".join([item[0] for item in data[0] if item and item[0]]).strip()
        return translated if translated else text
    except:
        return text

def main():
    print("2. Reading Rule34Video tags...", flush=True)
    r34_rows = []
    with open(r34_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        r34_rows = list(reader)

    print(f"3. Processing {len(r34_rows)} tags...", flush=True)
    
    translations = {}
    to_api = []

    for row in r34_rows:
        tag_id, tag_name, count = row[0], row[1], row[2]
        norm_name = tag_name.strip().lower()

        # Direct match
        if norm_name in danbooru:
            translations[tag_name] = danbooru[norm_name]
            continue
        
        # Regex pattern
        m_combo = re.findall(r'(\d+)\s*([a-zA-Z]+)', norm_name)
        if m_combo and len("".join([f"{num}{term}" for num, term in m_combo])) == len(norm_name.replace(' ', '')):
            translated_parts = []
            all_valid = True
            for num, term in m_combo:
                if term in term_map:
                    translated_parts.append(f"{num}{term_map[term]}")
                else:
                    all_valid = False
                    break
            if all_valid and translated_parts:
                translations[tag_name] = "".join(translated_parts)
                continue

        to_api.append(tag_name)

    print(f"   - Directly/Pattern matched: {len(translations)}", flush=True)
    print(f"   - Translating remaining {len(to_api)} tags via multi-threading...", flush=True)

    with ThreadPoolExecutor(max_workers=15) as executor:
        results = executor.map(translate_single, to_api)
        for original, trans in zip(to_api, results):
            translations[original] = trans

    print("\n4. Saving final results to rule34video_tags_zh.csv...", flush=True)
    with open(out_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Name', 'ChineseName', 'VideoCount'])
        for row in r34_rows:
            tag_id, tag_name, count = row[0], row[1], row[2]
            cn_trans = translations.get(tag_name, tag_name)
            writer.writerow([tag_id, tag_name, cn_trans, count])

    print(f"Done! {len(translations)} tags translated successfully!", flush=True)

if __name__ == '__main__':
    main()
