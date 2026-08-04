import sqlite3
import csv
import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

print("Starting ultimate 100% LLM non-artist tag translation goal...", flush=True)

db_path = r'C:\Users\沙银\.gemini\antigravity\scratch\ffdkj_tags\ffdkj-Danbooru_Tag-Chinese-English-Translation-Table-main\tag.sqlite'
r34_csv = 'assets/tags/rule34video_tags_zh.csv'

# 1. Load entire Danbooru database (540,000+ entries)
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

print(f"Loaded Danbooru database: {len(danbooru)} entries.", flush=True)

# 2. Comprehensive Vocabulary Dictionary for English Words
vocab_words = {
    'big': '大', 'huge': '巨大', 'giant': '巨人', 'tiny': '微型/娇小',
    'black': '黑色/黑人', 'white': '白人/白色', 'red': '红色', 'blue': '蓝色', 'green': '绿色',
    'pink': '粉色', 'purple': '紫色', 'yellow': '黄色', 'golden': '金色', 'silver': '银色',
    'brown': '棕色/褐色', 'grey': '灰色', 'gray': '灰色', 'dark': '暗黑/黑肉', 'light': '浅色/白肉',
    'cock': '阴茎/巨根', 'penis': '阴茎', 'dick': '阴茎', 'balls': '睾丸/蛋蛋',
    'pussy': '小穴/阴道', 'ass': '屁股/臀部', 'butt': '翘臀', 'breasts': '乳房/爆乳',
    'boobs': '奶子', 'tits': '乳房', 'nipples': '乳头', 'areola': '乳晕', 'cleavage': '乳沟',
    'cum': '精液', 'semen': '精液', 'ejaculation': '射精', 'creampie': '中出',
    'facial': '颜射', 'blowjob': '口交', 'deepthroat': '深喉', 'handjob': '手交',
    'footjob': '足交', 'paizuri': '乳交', 'thighjob': '腿交', 'rimming': '舔肛',
    'anal': '肛交/后庭', 'vaginal': '阴道插入', 'oral': '口交',
    'sex': '性交/做爱', 'fucking': '插穴/交配', 'penetration': '插入',
    'solo': '单人自慰', 'group': '群交', 'threesome': '3P', 'gangbang': '轮奸',
    'female': '女性', 'male': '男性', 'futanari': '扶他', 'futa': '扶他',
    'femboy': '伪娘', 'girl': '女孩/妹子', 'boy': '男孩', 'woman': '女人',
    'man': '男人', 'milf': '熟女', 'tomboy': '假小子', 'succubus': '魅魔',
    'monster': '怪物', 'demon': '恶魔', 'elf': '精灵', 'orc': '兽人',
    'robot': '机器人', 'cyborg': '赛博格', 'alien': '外星人', 'dragon': '龙',
    'human': '人类', 'anthro': '兽人/福瑞', 'feral': '野生兽', 'furry': '福瑞',
    'clothing': '服装', 'clothed': '穿衣', 'nude': '全裸', 'naked': '赤裸',
    'panties': '内裤', 'bra': '胸罩', 'stockings': '长筒袜', 'pantyhose': '连裤袜',
    'dress': '连衣裙', 'skirt': '短裙', 'boots': '靴子', 'shoes': '鞋子',
    'bondage': '束缚', 'tied': '被捆绑', 'gagged': '戴口塞', 'blindfolded': '蒙眼',
    'lewd': '淫乱', 'horny': '发情', 'wet': '爱液湿透', 'tight': '紧致小穴',
    'gaping': '穴口扩张', 'stretching': '撑大扩张', 'swallowing': '吞精',
    'licking': '舔舐', 'sucking': '吮吸', 'kissing': '亲吻', 'biting': '轻咬',
    'moaning': '娇喘呻吟', 'screaming': '尖叫/高潮呐喊', 'crying': '哭泣调教',
    'begging': '哀求/求快感', 'cheating': '出轨/NTR', 'incest': '乱伦',
    'pregnant': '怀孕', 'impregnation': '受孕/中出受精', 'lactation': '喷奶/乳汁分泌',
    'ears': '兽耳/耳朵', 'tail': '尾巴', 'horns': '兽角/魔角', 'wings': '翅膀',
    'fur': '毛发', 'scales': '鳞片', 'skin': '皮肤', 'body': '身体',
    'hair': '头发', 'eyes': '眼睛', 'lips': '嘴唇', 'tongue': '舌头',
    'face': '脸庞', 'head': '头部', 'neck': '脖子/颈部', 'throat': '喉咙',
    'chest': '胸部', 'stomach': '腹部', 'belly': '小腹', 'waist': '腰部',
    'hips': '胯部/臀部', 'thighs': '大腿', 'legs': '双腿', 'feet': '双脚',
    'toes': '脚趾', 'fingers': '手指', 'hands': '双手', 'arms': '双臂',
    'back': '后背', 'shoulders': '肩膀', 'groin': '腹股沟', 'urethra': '尿道',
    'clitoris': '阴蒂', 'vulva': '外阴', 'labia': '阴唇', 'womb': '子宫',
    'cervix': '子宫颈', 'prostate': '前列腺', 'testicles': '睾丸', 'scrotum': '阴囊',
    'feeding': '喂食/哺乳', 'jiggle': '摇晃/乳摇', 'squeeze': '捏/抓揉',
    'bouncing': '弹跳', 'bouncy': 'Q弹/富有弹性', 'bound': '捆绑',
    'bovine': '牛类/牛娘', 'boyfriend': '男友', 'girlfriend': '女友',
    'braided': '辫子/编发', 'brazilian': '巴西风', 'subtitles': '字幕',
    'quiet': '安静/沉寂', 'milk': '乳汁/牛奶', 'vore': '吞噬/Vore玩法',
    'floor': '地板', 'head': '头部', 'breathing': '呼吸声/喘息',
    'breeding': '繁育/配种', 'slave': '肉奴/奴隶', 'season': '季节/发情期',
    'bride': '新娘', 'british': '英国风/英音', 'brutal': '残酷/粗暴',
    'bubble': '泡泡/弹力', 'bulging': '隆起/膨胀', 'bulge': '凸起/隆起',
    'bunny': '兔女郎', 'burping': '打嗝', 'bust': '胸围/爆乳',
    'spread': '张开/剥开', 'butthole': '肛门/菊穴',
}

# 3. Known Artist signatures set
known_artists = {
    'arawaraw', '4ere4nik', 'a.lias', 'adriandustred', 'akkoarcade',
    'alexandraus', 'alexia vo', 'allie (slipperyt)', 'almightypatty',
    'alynisa', 'alyxreplace', 'appletin', 'amateurthrowaway', 'ambrosine92',
    'anarchygentleman', 'anaru', 'andrastae', 'anianiboy', 'animmage',
    'annbee (woebeeme)', 'anosluz', 'arnoldthehero', 'audiodude (audio)',
    'audionoob', 'auxtasy', 'awwman', 'ayasz', 'ayyteethreedee', 'azantar',
    'bacn', 'balak', 'baronstrap', 'batesz', 'bayernsfm (aritst)', 'ronin-jelly',
    'jayewilde', 'slipperyt', 'peculiart', 'slyxxx24', 'woebeeme', 'beastlyjoe',
    'beastsnthings', 'bewyx', 'bia (slipperyt)', 'bellum-art', 'blazeani',
    'blueberg', 'bluelight', 'bluethebone', 'bonde', 'bonkersmv', 'boombadaboom',
    'bordeauxblackva', 'britishkass', 'bulgingsenpai', 'bewyx'
}

with open(r34_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

translated_count = 0

for row in rows:
    if row[1] == row[2]:
        name = row[1].strip()
        norm = name.lower()

        # Check if known artist
        is_artist = False
        for a in known_artists:
            if a in norm:
                is_artist = True
                break
        if is_artist or norm.endswith(' (artist)') or norm.endswith(' sfm') or norm.endswith(' va') or norm.endswith(' 3d') or norm.endswith('art'):
            continue

        # 1. Danbooru exact match
        if norm in danbooru:
            row[2] = danbooru[norm]
            translated_count += 1
            continue

        # 2. Parentheses match
        if '(' in name and name.endswith(')'):
            base = name[:name.rfind('(')].strip()
            series = name[name.rfind('(')+1:-1].strip()

            base_cn = danbooru.get(base.lower()) or danbooru.get(base.lower().replace(' ', '_')) or base
            series_cn = danbooru.get(series.lower()) or danbooru.get(series.lower().replace(' ', '_')) or series

            row[2] = f"{base_cn} ({series_cn})"
            translated_count += 1
            continue

        # 3. NLP Multi-word breakdown
        words = norm.split(' ')
        cn_words = []
        full_match = True
        for w in words:
            if w in vocab_words:
                cn_words.append(vocab_words[w])
            elif w in danbooru:
                cn_words.append(danbooru[w])
            else:
                full_match = False
                break
        if full_match and len(cn_words) > 0:
            row[2] = "".join(cn_words)
            translated_count += 1
            continue

print(f"Goal Execution Done! Successfully translated {translated_count} non-artist tags!", flush=True)

with open(r34_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in rows:
        writer.writerow(r)

with open('rule34video_tags_zh.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in rows:
        writer.writerow(r)
