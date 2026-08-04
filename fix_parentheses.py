import sqlite3
import csv
import re
import urllib.request
import urllib.parse
import json
import time

db_path = r'C:\Users\沙银\.gemini\antigravity\scratch\ffdkj_tags\ffdkj-Danbooru_Tag-Chinese-English-Translation-Table-main\tag.sqlite'
out_csv = 'rule34video_tags_zh.csv'

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

series_aliases = {
    'evangelion': '新世纪福音战士',
    'kono subarashii': '为美好的世界献上祝福！',
    'honkai star rail': '崩坏：星穹铁道',
    'honkai impact': '崩坏3',
    'azur lane': '碧蓝航线',
    'genshin impact': '原神',
    'wuthering waves': '鸣潮',
    'blue archive': '蔚蓝档案',
    'league of legends': '英雄联盟',
    'overwatch': '守望先锋',
    'pokemon': '宝可梦',
    'fate': 'Fate系列',
    'rwby': 'RWBY',
    'fnaf': '玩具熊的五夜后宫',
    'uma musume': '赛马娘',
    'oshi no ko': '我推的孩子',
    'vtuber': 'VTuber/虚拟主播',
    'taimanin': '对魔忍',
    'highschool dxd': '恶魔高校D×D',
    'danmachi': '在地下城寻求遭遇是否搞错了什么',
    'kakegurui': '狂赌之渊',
    'kekgurui': '狂赌之渊',
    '100kanojo': '超超超超超喜欢你的100个女朋友',
    'tengoku daimakyou': '天国大魔境',
    'mlp': '小马宝莉',
    'life is strange': '奇异人生',
    'smite': '神之浩劫',
    'helluva boss': '极恶老大',
    'vocaloid': 'VOCALOID',
    'apex legends': 'Apex英雄',
    'death stranding': '死亡搁浅',
    'final fantasy': '最终幻想',
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
    'one piece': '航海王',
    'dragon ball': '龙珠',
    'fairy tail': '妖精的尾巴',
    'demon slayer': '鬼灭之刃',
    'jojo': 'JOJO的奇妙冒险',
    'my hero academia': '我的英雄学院',
    'attack on titan': '进击的巨人',
    'sword art online': '刀剑神域',
    're:zero': 'Re:从零开始的异世界生活',
    'no game no life': '游戏人生',
    'to love-ru': '出包王女',
    'chainsaw man': '电锯人',
    'spy x family': '间谍过家家',
    'arknights': '明日方舟',
    'nikke': '胜利女神：妮姬',
    'zenless zone zero': '绝区零',
    'zzz': '绝区零',
    'fate/grand order': 'Fate/Grand Order',
    'fgo': 'Fate/Grand Order',
    'touhou': '东方Project',
    'paladins': '枪火游侠',
    'fortnite': '堡垒之夜',
    'cyberpunk 2077': '赛博朋克2077',
    'kirby': '星之卡比',
}
for k, v in list(series_aliases.items()):
    series_aliases[k.replace(' ', '_')] = v

def translate_gtx(text):
    if not text:
        return text
    try:
        q = urllib.parse.quote(text)
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t&q={q}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=5).read().decode('utf-8')
        data = json.loads(res)
        translated = "".join([item[0] for item in data[0] if item and item[0]]).strip()
        return translated if translated else text
    except:
        return text

with open(out_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

updated_count = 0
new_rows = []

for row in rows:
    tag_id, name, cn_name, count = row[0], row[1], row[2], row[3]
    norm = name.strip().lower()
    
    if '(' in norm and norm.endswith(')'):
        base = norm[:norm.rfind('(')].strip()
        series = norm[norm.rfind('(')+1:-1].strip()

        # Resolve series
        series_cn = series_aliases.get(series) or series_aliases.get(series.replace(' ', '_'))
        if not series_cn:
            series_cn = danbooru.get(series) or danbooru.get(series.replace(' ', '_'))
        if not series_cn:
            series_cn = translate_gtx(series)

        # Resolve base
        base_cn = danbooru.get(base) or danbooru.get(base.replace(' ', '_'))
        if not base_cn:
            base_cn = translate_gtx(base)

        combined = f"{base_cn} ({series_cn})"
        if combined != cn_name:
            updated_count += 1
            cn_name = combined

    new_rows.append([tag_id, name, cn_name, count])

print(f"Updated {updated_count} parenthetical tags with dual resolution!")

with open(out_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in new_rows:
        writer.writerow(r)

print("Saved fixes to rule34video_tags_zh.csv")
