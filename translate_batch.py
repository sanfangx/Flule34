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
print(f"   Loaded {len(danbooru)} Danbooru dictionary entries.")

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

def translate_batch_gtx(text_list):
    if not text_list:
        return []
    text_payload = "\n".join(text_list)
    q = urllib.parse.quote(text_payload)
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t&q={q}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    
    try:
        res = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
        data = json.loads(res)
        full_text = "".join([item[0] for item in data[0] if item and item[0]])
        lines = full_text.split('\n')
        if len(lines) == len(text_list):
            return [l.strip() for l in lines]
    except Exception as e:
        print(f"Batch translation error: {e}")
        
    # Fallback to item-by-item if batch alignment failed
    results = []
    for item in text_list:
        try:
            q_single = urllib.parse.quote(item)
            u_single = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t&q={q_single}"
            r_single = urllib.request.urlopen(urllib.request.Request(u_single, headers={'User-Agent': 'Mozilla/5.0'}), timeout=5).read().decode('utf-8')
            d_single = json.loads(r_single)
            results.append("".join([x[0] for x in d_single[0] if x and x[0]]).strip())
        except:
            results.append(item)
        time.sleep(0.05)
    return results

def main():
    print("2. Reading Rule34Video tags...")
    r34_rows = []
    with open(r34_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        r34_rows = list(reader)

    print(f"3. Matching and processing {len(r34_rows)} tags...")
    
    translations = {}
    unmatched = []

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

        unmatched.append(tag_name)

    print(f"   - Directly/Pattern matched: {len(translations)}")
    print(f"   - Remaining unmatched to translate via batch API: {len(unmatched)}")

    batch_size = 40
    for i in range(0, len(unmatched), batch_size):
        chunk = unmatched[i:i + batch_size]
        print(f"   Translating batch {i//batch_size + 1} / {(len(unmatched) + batch_size - 1)//batch_size} ({len(chunk)} items)...")
        translated_chunk = translate_batch_gtx(chunk)
        for original, trans in zip(chunk, translated_chunk):
            translations[original] = trans
        time.sleep(0.2)

    print("\n4. Saving final results to rule34video_tags_zh.csv...")
    with open(out_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Name', 'ChineseName', 'VideoCount'])
        for row in r34_rows:
            tag_id, tag_name, count = row[0], row[1], row[2]
            cn_trans = translations.get(tag_name, tag_name)
            writer.writerow([tag_id, tag_name, cn_trans, count])

    print("Done! All tags translated successfully!")

if __name__ == '__main__':
    main()
