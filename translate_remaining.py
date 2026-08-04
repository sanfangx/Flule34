import sqlite3
import csv
import re
import urllib.request
import urllib.parse
import json
import time
from concurrent.futures import ThreadPoolExecutor

db_path = r'C:\Users\沙银\.gemini\antigravity\scratch\ffdkj_tags\ffdkj-Danbooru_Tag-Chinese-English-Translation-Table-main\tag.sqlite'
r34_csv = 'rule34video_tags.csv'
out_csv = 'rule34video_tags_zh.csv'

print("1. Loading Danbooru database...")
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

# Common term mapping for regex rules
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

def translate_gtx(text):
    if not text:
        return ""
    try:
        q = urllib.parse.quote(text)
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t&q={q}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=5).read().decode('utf-8')
        data = json.loads(res)
        translated = "".join([item[0] for item in data[0] if item[0]])
        return translated.strip()
    except Exception as e:
        return text

def solve_tag(row):
    tag_id, tag_name, count = row[0], row[1], row[2]
    norm_name = tag_name.strip().lower()

    # Direct match
    if norm_name in danbooru:
        return (tag_id, tag_name, danbooru[norm_name], count, 'danbooru')
    
    # Combined pattern like 1boy1girl, 3boys1girl, 2animals
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
            return (tag_id, tag_name, "".join(translated_parts), count, 'pattern')

    # Parentheses match (Character (Series))
    if '(' in norm_name and norm_name.endswith(')'):
        parts = norm_name[:-1].split('(')
        base = parts[0].strip()
        series = parts[1].strip()

        base_cn = danbooru.get(base) or danbooru.get(base.replace(' ', '_'))
        series_cn = danbooru.get(series) or danbooru.get(series.replace(' ', '_'))

        if not series_cn:
            series_cn = translate_gtx(series)
        if not base_cn:
            base_cn = translate_gtx(base)

        return (tag_id, tag_name, f"{base_cn} ({series_cn})", count, 'parentheses')

    # Fallback to Google Translate API
    gtx_trans = translate_gtx(tag_name)
    return (tag_id, tag_name, gtx_trans, count, 'gtx')

def main():
    print("2. Reading Rule34Video tags...")
    r34_rows = []
    with open(r34_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        r34_rows = list(reader)

    print(f"3. Processing {len(r34_rows)} tags with parallel translation...")
    
    results = []
    danbooru_count = 0
    pattern_count = 0
    parentheses_count = 0
    gtx_count = 0

    # Process using thread pool
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = executor.map(solve_tag, r34_rows)
        for i, res in enumerate(futures):
            results.append(res)
            source = res[4]
            if source == 'danbooru': danbooru_count += 1
            elif source == 'pattern': pattern_count += 1
            elif source == 'parentheses': parentheses_count += 1
            elif source == 'gtx': gtx_count += 1
            
            if (i + 1) % 1000 == 0 or (i + 1) == len(r34_rows):
                print(f"  Processed {i + 1}/{len(r34_rows)} tags...")

    print(f"\nTranslation Complete!")
    print(f"  - Danbooru Matched: {danbooru_count}")
    print(f"  - Pattern Matched: {pattern_count}")
    print(f"  - Parentheses Combined: {parentheses_count}")
    print(f"  - Online API Translated: {gtx_count}")

    print("4. Saving to rule34video_tags_zh.csv...")
    with open(out_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Name', 'ChineseName', 'VideoCount'])
        for r in results:
            writer.writerow([r[0], r[1], r[2], r[3]])

    print("Done! Output saved to rule34video_tags_zh.csv")

if __name__ == '__main__':
    main()
