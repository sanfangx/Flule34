import sqlite3
import csv
import re
import sys
import urllib.request
import urllib.parse
import json

sys.stdout.reconfigure(encoding='utf-8')

db_path = r'C:\Users\沙银\.gemini\antigravity\scratch\ffdkj_tags\ffdkj-Danbooru_Tag-Chinese-English-Translation-Table-main\tag.sqlite'
r34_csv = 'rule34video_tags.csv'
out_csv = 'assets/tags/rule34video_tags_zh.csv'

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
        pass
    
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
    return res_list

with open(r34_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    r34_rows = list(reader)

translations = {}
unmatched = []

for row in r34_rows:
    tag_name = row[1]
    norm = tag_name.strip().lower()

    if norm in expert_dict:
        translations[tag_name] = expert_dict[norm]
    elif norm in danbooru:
        translations[tag_name] = danbooru[norm]
    else:
        m_combo = re.findall(r'(\d+)\s*([a-zA-Z]+)', norm)
        if m_combo and len("".join([f"{num}{term}" for num, term in m_combo])) == len(norm.replace(' ', '')):
            if all(term in term_map for _, term in m_combo):
                translations[tag_name] = "".join([f"{num}{term_map[term]}" for num, term in m_combo])
                continue

        if '(' in norm and norm.endswith(')'):
            base = norm[:norm.rfind('(')].strip()
            series = norm[norm.rfind('(')+1:-1].strip()

            base_cn = expert_dict.get(base) or danbooru.get(base) or danbooru.get(base.replace(' ', '_'))
            series_cn = series_aliases.get(series) or series_aliases.get(series.replace(' ', '_')) or danbooru.get(series) or danbooru.get(series.replace(' ', '_'))

            if base_cn and series_cn:
                translations[tag_name] = f"{base_cn} ({series_cn})"
                continue

        unmatched.append(tag_name)

print(f"Matched {len(translations)} tags natively.", flush=True)
print(f"Translating remaining {len(unmatched)} tags in 40-item batches...", flush=True)

batch_size = 40
for i in range(0, len(unmatched), batch_size):
    chunk = unmatched[i:i + batch_size]
    translated_chunk = translate_batch(chunk)
    for original, trans in zip(chunk, translated_chunk):
        translations[original] = trans

print("Saving to CSV files...", flush=True)
with open(out_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Name', 'ChineseName', 'VideoCount'])
    for row in r34_rows:
        tag_id, tag_name, count = row[0], row[1], row[2]
        cn_trans = translations.get(tag_name, tag_name)
        writer.writerow([tag_id, tag_name, cn_trans, count])

with open('rule34video_tags_zh.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Name', 'ChineseName', 'VideoCount'])
    for row in r34_rows:
        tag_id, tag_name, count = row[0], row[1], row[2]
        cn_trans = translations.get(tag_name, tag_name)
        writer.writerow([tag_id, tag_name, cn_trans, count])

print("ALL DONE!", flush=True)
