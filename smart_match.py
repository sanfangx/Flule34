import sqlite3
import csv
import re

db_path = r'C:\Users\沙银\.gemini\antigravity\scratch\ffdkj_tags\ffdkj-Danbooru_Tag-Chinese-English-Translation-Table-main\tag.sqlite'
r34_csv = 'rule34video_tags.csv'

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

# Also map series aliases
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
    'fate/stay night': 'Fate/stay night',
    'street fighter': '街头霸王',
    'dead or alive': '死或生',
    'tekken': '铁拳',
    'warcraft': '魔兽世界',
    'world of warcraft': '魔兽世界',
    'starcraft': '星际争霸',
    'diablo': '暗黑破坏神',
    'metroid': '银河战士',
    'zelda': '塞尔达传说',
    'the legend of zelda': '塞尔达传说',
    'mario': '超级马里奥',
    'super mario': '超级马里奥',
    'sonic': '刺猬索尼克',
    'naruto': '火影忍者',
    'bleach': '死神',
    'one piece': '海贼王',
    'dragon ball': '龙珠',
    'fairy tail': '妖精的尾巴',
    'demon slayer': '鬼灭之刃',
    'jojo': 'JOJO的奇妙冒险',
    'rwby': 'RWBY',
    'my hero academia': '我的英雄学院',
    'attack on titan': '进击的巨人',
    'sword art online': '刀剑神域',
    're:zero': 'Re:从零开始的异世界生活',
    'no game no life': '游戏人生',
    'to love-ru': '出包王女',
    'chainsaw man': '电锯人',
    'spy x family': '间谍过家家',
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

r34_rows = []
with open(r34_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    r34_rows = list(reader)

matched = 0
unmatched = []

for row in r34_rows:
    tag_name = row[1]
    norm = tag_name.strip().lower()
    
    # 1. Exact Danbooru
    if norm in danbooru:
        matched += 1
        continue
        
    # 2. Pattern
    m_combo = re.findall(r'(\d+)\s*([a-zA-Z]+)', norm)
    if m_combo and len("".join([f"{num}{term}" for num, term in m_combo])) == len(norm.replace(' ', '')):
        if all(term in term_map for _, term in m_combo):
            matched += 1
            continue

    # 3. Parentheses split
    if '(' in norm and norm.endswith(')'):
        base = norm[:norm.rfind('(')].strip()
        series = norm[norm.rfind('(')+1:-1].strip()

        base_cn = danbooru.get(base) or danbooru.get(base.replace(' ', '_'))
        series_cn = aliases.get(series) or danbooru.get(series) or danbooru.get(series.replace(' ', '_'))

        if base_cn or series_cn:
            matched += 1
            continue

    unmatched.append(tag_name)

print(f"Total: {len(r34_rows)}")
print(f"Smart Matched: {matched} ({matched/len(r34_rows)*100:.2f}%)")
print(f"Remaining Unmatched: {len(unmatched)}")
