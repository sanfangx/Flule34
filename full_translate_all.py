import sqlite3
import csv
import re
import sys
import urllib.request
import urllib.parse
import json
import time

sys.stdout.reconfigure(encoding='utf-8')

db_path = r'C:\Users\沙银\.gemini\antigravity\scratch\ffdkj_tags\ffdkj-Danbooru_Tag-Chinese-English-Translation-Table-main\tag.sqlite'
r34_csv = 'rule34video_tags.csv'
out_csv = 'assets/tags/rule34video_tags_zh.csv'

print("1. Loading Danbooru database...", flush=True)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("SELECT name, cn_name FROM tags WHERE cn_name IS NOT NULL AND cn_name != ''")

danbooru = {}
for name, cn_name in cursor:
    n = str(name).strip().lower()
    c = str(cn_name).strip()
    if n and c:
        danbooru[n] = c
        danbooru[n.replace('_', ' ')] = c
        danbooru[n.replace(' ', '_')] = c
conn.close()

# Expert ACG / Adult dictionary
expert_dict = {
    'adagio dazzle': '艾达琪',
    'aemeath': '埃米斯',
    'titty fuck': '乳交',
    'reverse titty fuck': '反向乳交',
    'brain fuck': '脑交',
    'fuckmeat': '肉便器',
    'monster fuck': '怪物交配',
    'horse fuck': '马交',
    'knot fucking': '打结交配',
    'navel fuck': '肚脐交',
    'snout fuck': '兽嘴插穴',
    'deepthroat': '深喉',
    'paizuri': '乳交',
    'irrumatio': '口交',
    'cunnilingus': '舔阴',
    'fellatio': '口交',
    'anilingus': '舔肛',
    'bukkake': '颜射',
    'creampie': '中出',
    'anal creampie': '肛门中出',
    'gokkun': '饮精',
    'facial': '颜射',
    'handjob': '手交',
    'footjob': '足交',
    'thighjob': '腿交',
    'armpit sex': '腋交',
    'sumata': '素股',
    'ahegao': '阿黑颜',
    'mind break': '精神崩溃',
    'hypnosis': '催眠',
    'tentacles': '触手',
    'bondage': '束缚',
    'shibari': '绳缚',
    'chastity cage': '贞操笼',
    'futa': '扶他', 'futas': '扶他',
    'futanari': '扶他',
    'tomboy': '假小子',
    'milf': '熟女',
    'incest': '乱伦',
    'cuckold': '绿帽',
    'netorare': 'NTR',
    'ntr': 'NTR',
    'pregnant': '孕妇',
    'impregnation': '受孕',
    'lactation': '喷奶',
    'x-ray': '透视',
    'giantess': '女巨人',
    'succubus': '魅魔',
}

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
    'vtuber': 'VTuber',
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

with open(r34_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    r34_rows = list(reader)

new_rows = []
unmatched = []

for row in r34_rows:
    tag_id, name, count = row[0], row[1], row[2]
    norm = name.strip().lower()

    cn = ""

    # 1. Expert dict
    if norm in expert_dict:
        cn = expert_dict[norm]
    # 2. Danbooru DB
    elif norm in danbooru:
        cn = danbooru[norm]
    # 3. Pattern
    else:
        m_combo = re.findall(r'(\d+)\s*([a-zA-Z]+)', norm)
        if m_combo and len("".join([f"{num}{term}" for num, term in m_combo])) == len(norm.replace(' ', '')):
            if all(term in term_map for _, term in m_combo):
                cn = "".join([f"{num}{term_map[term]}" for num, term in m_combo])

    # 4. Parentheses match
    if not cn and '(' in norm and norm.endswith(')'):
        base = norm[:norm.rfind('(')].strip()
        series = norm[norm.rfind('(')+1:-1].strip()

        base_cn = expert_dict.get(base) or danbooru.get(base) or danbooru.get(base.replace(' ', '_'))
        series_cn = series_aliases.get(series) or series_aliases.get(series.replace(' ', '_')) or danbooru.get(series) or danbooru.get(series.replace(' ', '_'))

        if not series_cn:
            series_cn = translate_gtx(series)
        if not base_cn:
            base_cn = translate_gtx(base)

        cn = f"{base_cn} ({series_cn})"

    if not cn:
        unmatched.append((tag_id, name, count))
    else:
        new_rows.append([tag_id, name, cn, count])

print(f"Direct & Pattern & Parentheses matched: {len(new_rows)}")
print(f"Remaining unmatched to translate: {len(unmatched)}")

# Translate remaining using single GTX calls or clean fallback
for idx, (tag_id, name, count) in enumerate(unmatched):
    gtx_res = translate_gtx(name)
    new_rows.append([tag_id, name, gtx_res, count])
    if (idx + 1) % 500 == 0 or (idx + 1) == len(unmatched):
        print(f"  Processed {idx+1}/{len(unmatched)} remaining tags...")

with open(out_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Name', 'ChineseName', 'VideoCount'])
    for r in new_rows:
        writer.writerow(r)

with open('rule34video_tags_zh.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Name', 'ChineseName', 'VideoCount'])
    for r in new_rows:
        writer.writerow(r)

print("Complete! Saved to CSV files.")
