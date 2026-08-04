import sqlite3
import csv
import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

print("Starting ultimate goal resolution script for Rule34Video tags...", flush=True)

db_path = r'C:\Users\沙银\.gemini\antigravity\scratch\ffdkj_tags\ffdkj-Danbooru_Tag-Chinese-English-Translation-Table-main\tag.sqlite'
r34_csv = 'assets/tags/rule34video_tags_zh.csv'

# 1. Load entire Danbooru database
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

print(f"Loaded {len(danbooru)} entries from Danbooru database.")

# 2. Comprehensive ACG/Adult/General Translation Dictionary
dict_override = {
    'arcade machine': '街机/游戏机',
    'artorias': '亚尔特留斯 (黑暗之魂)',
    'ashley': '阿什莉',
    'ball tugging': '拉扯睾丸',
    'ball worship': '蛋蛋崇拜/膜拜睾丸',
    'ballbusting': '碎蛋/击打睾丸',
    'ballcaress': '抚摸睾丸',
    'balls deep': '全根没入/阴囊贴臀',
    'balls expansion': '睾丸膨胀',
    'balls fondle': '抚弄蛋蛋',
    'balls inflation': '睾丸充气膨胀',
    'balls touching': '睾丸碰撞',
    'bandage': '绷带/绷带缚体',
    'bāozi': '包子',
    'barbed penis': '倒钩阴茎',
    'bare calves': '赤裸小腿',
    'bare thighs': '裸露大腿',
    'barefeet': '赤脚/裸足',
    'barely clothed': '衣不蔽体/极其微少着装',
    'baron (doom)': '地狱男爵 (毁灭战士)',
    'bat': '蝙蝠/球棒',
    'bat pony': '蝠翼小马 (小马宝莉)',
    'bathroom stall': '厕所隔间',
    'bbm': 'BBM/大腹便便男',
    'bbw': 'BBW/丰满大码女性',
    'bdsm hardcore': '硬核BDSM/重度调教',
    'beach sex': '海滩性交/海边做爱',
    'beachside bunnies': '海滩兔女郎',
    'bear humanoid': '熊人/熊兽人',
    'beast': '野兽/巨兽',
    'beauty': '美女/绝色佳人',
    'bed sex': '床上做爱',
    'behind the back': '在背后/背手姿势',
    'belching': '打嗝',
    'belly bulge': '小腹隆起/小腹微凸',
    'belly button': '肚脐',
    'belt': '腰带/皮带',
    'bent over': '弯腰/俯身姿势',
    'bestiality': '兽交',
    'big ass': '大臀/巨臀',
    'big belly': '大肚腩/大肚子',
    'big breasts': '大胸/爆乳',
    'big clitoris': '大阴蒂/阴蒂肥大',
    'big cock': '大巨根',
    'big penis': '大阴茎',
    'bites': '咬痕',
    'biting': '咬/轻咬调教',
    'black hair': '黑发',
    'black pantyhose': '黑丝/黑色连裤袜',
    'black skin': '黑肤/黑肉',
    'blindfold': '眼罩/蒙眼调教',
    'blonde hair': '金发',
    'blood': '血液/流血',
    'blood dripping': '血液滴落',
    'blue hair': '蓝发',
    'blur': '动态模糊',
    'blushing': '脸红/害羞',
    'bondage': '束缚/调教',
    'boobs': '巨乳/胸部',
    'boots': '靴子',
    'bound': '被捆绑',
    'boy': '男孩',
    'bra': '胸罩',
    'breast expansion': '丰胸/胸部膨胀',
    'breast grab': '抓揉乳房',
    'breast smother': '乳房闷脸/洗面奶',
    'breasts': '乳房',
    'brother and sister': '兄妹/姐弟',
    'brunette': '棕发妹',
    'bunny ears': '兔耳',
    'bunny suit': '兔女郎服',
    'butt': '屁股/臀部',
    'butt cheek': '臀瓣',
    'butt plug': '肛塞',
    'cameltoe': '骆驼趾/紧身裤显痕',
    'cat ears': '猫耳',
    'catgirl': '猫娘',
    'cervix': '子宫颈',
    'chain': '锁链',
    'champion': '冠军/英雄',
    'cheating': '出轨/NTR',
    'cheerleader': '拉拉队服/拉拉队长',
    'chest hair': '胸毛',
    'choke': '窒息/锁喉',
    'clothed sex': '穿衣性交',
    'clothes': '衣服',
    'clothing': '服饰',
    'cock': '阴茎/巨根',
    'cock ring': '贞操环/锁精环',
    'collar': '项圈/颈圈',
    'condom': '避孕套',
    'cowgirl': '牛娘/女上位',
    'creampie': '中出',
    'cum': '精液',
    'cum in ass': '肠内中出/射在屁股里',
    'cum in pussy': '阴道中出/小穴中出',
    'cum inside': '体内中出',
    'cum drip': '精液滴落',
    'cumshot': '射精特写',
    'cunnilingus': '舔阴',
    'dark skin': '黑肉/深色皮肤',
    'deepthroat': '深喉',
    'demon': '恶魔',
    'demon girl': '恶魔娘',
    'dick': '阴茎',
    'dildo': '假阳具',
    'doggy style': '后入式/狗刨式',
    'domination': '主导/调教',
    'double penetration': '双重插入',
    'dragon': '龙/巨龙',
    'ejaculation': '射精',
    'elf': '精灵',
    'erection': '勃起',
    'exhibitionism': '暴露癖',
    'facial': '颜射',
    'fellatio': '口交',
    'female': '女性',
    'femboy': '伪娘',
    'fingering': '抠穴/手交',
    'footjob': '足交',
    'furry': '福瑞/兽人',
    'futanari': '扶他',
    'gangbang': '轮奸/多人性交',
    'giantess': '女巨人',
    'glasses': '眼镜',
    'group sex': '群交',
    'handjob': '手交',
    'harem': '后宫',
    'hentai': 'Hentai',
    'high heels': '高跟鞋',
    'humiliation': '羞辱/耻辱',
    'incest': '乱伦',
    'lactation': '喷奶/乳汁分泌',
    'lesbian': '百合/女同',
    'lingerie': '情趣内衣',
    'lolita': '萝莉/洛丽塔',
    'male': '男性',
    'masturbation': '自慰',
    'milf': '熟女',
    'mind break': '精神崩溃/阿黑颜',
    'monster': '怪物',
    'monster girl': '魔物娘',
    'nakadashi': '中出',
    'nipples': '乳头',
    'nude': '全裸',
    'orgasm': '高潮',
    'paizuri': '乳交',
    'panties': '内裤',
    'pantyhose': '丝袜/连裤袜',
    'penetration': '插入',
    'pov': '第一人称视角',
    'pregnant': '怀孕',
    'pussy': '小穴',
    'rimming': '舔肛',
    'scat': '黄金',
    'schoolgirl': '女子高中生/校服',
    'sex': '性交',
    'shemale': '伪娘/扶他',
    'solo': '单人自慰',
    'stockings': '长筒袜',
    'succubus': '魅魔',
    'swimsuit': '泳装',
    'tentacles': '触手',
    'threesome': '3P',
    'tits': '乳房',
    'uncensored': '无码/无遮挡',
    'vibrator': '跳蛋',
    'virgin': '处女/处男',
    'voyeur': '偷窥',
    'x-ray': '透视',
    'yuri': '百合',
}

# Known Artists / Studio creators to leave as-is
known_artists = {
    'arawaraw', '4ere4nik', 'a.lias', 'adriandustred', 'akkoarcade',
    'alexandraus', 'alexia vo', 'allie (slipperyt)', 'almightypatty',
    'alynisa', 'alyxreplace', 'appletin', 'amateurthrowaway', 'ambrosine92',
    'anarchygentleman', 'anaru', 'andrastae', 'anianiboy', 'animmage',
    'annbee (woebeeme)', 'anosluz', 'arnoldthehero', 'audiodude (audio)',
    'audionoob', 'auxtasy', 'awwman', 'ayasz', 'ayyteethreedee', 'azantar',
    'bacn', 'balak', 'baronstrap', 'batesz', 'bayernsfm (aritst)', 'ronin-jelly',
    'jayewilde'
}

with open(r34_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

fixed = 0
for row in rows:
    tag_id, name, cn_name, count = row[0], row[1], row[2], row[3]
    
    # Check if untranslated
    if name == cn_name:
        norm = name.strip().lower()
        
        # Skip if known artist
        if norm in known_artists or (norm.endswith(' (artist)') or norm.endswith(' sfm') or norm.endswith('va')):
            continue

        # 1. Override dictionary
        if norm in dict_override:
            row[2] = dict_override[norm]
            fixed += 1
            continue

        # 2. Danbooru DB
        if norm in danbooru:
            row[2] = danbooru[norm]
            fixed += 1
            continue

        # 3. Parentheses auto resolution
        if '(' in name and name.endswith(')'):
            base = name[:name.rfind('(')].strip()
            series = name[name.rfind('(')+1:-1].strip()

            base_cn = danbooru.get(base.lower()) or danbooru.get(base.lower().replace(' ', '_')) or base
            series_cn = danbooru.get(series.lower()) or danbooru.get(series.lower().replace(' ', '_')) or series

            row[2] = f"{base_cn} ({series_cn})"
            fixed += 1
            continue

print(f"Goal sweep completed! Translated {fixed} additional non-artist tags.", flush=True)

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
