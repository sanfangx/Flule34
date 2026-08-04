import csv
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

r34_csv = 'assets/tags/rule34video_tags_zh.csv'
with open(r34_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

# Known artist signatures or creator tags
known_artists_set = {
    'arawaraw', '4ere4nik', 'a.lias', 'adriandustred', 'akkoarcade',
    'alexandraus', 'alexia vo', 'allie (slipperyt)', 'almightypatty',
    'alynisa', 'alyxreplace', 'appletin', 'amateurthrowaway', 'ambrosine92',
    'anarchygentleman', 'anaru', 'andrastae', 'anianiboy', 'animmage',
    'annbee (woebeeme)', 'anosluz', 'arnoldthehero', 'audiodude (audio)',
    'audionoob', 'auxtasy', 'awwman', 'ayasz', 'ayyteethreedee', 'azantar',
    'bacn', 'balak', 'baronstrap', 'batesz', 'bayernsfm (aritst)', 'ronin-jelly',
    'jayewilde', 'slipperyt', 'peculiart', 'slyxxx24', 'woebeeme'
}

# General LLM Dictionary for all remaining non-artist words
general_dict = {
    'aid': '援助/辅助',
    'alibi': '不在场证明',
    'amazon': '亚马逊女战士',
    'amazonium': '亚马逊金属',
    'amber': '琥珀',
    'amun': '阿蒙神',
    'anteiku': '安定区 (东京喰种)',
    'aphrodite': '阿弗洛狄忒 (爱神)',
    'ascendant one': '超越者',
    'asaris': '阿萨里族 (质量效应)',
    'bayern': '拜仁',
    'bbm': '大腹便便男',
    'bbw': '丰满大码女性',
    'bdsm': 'BDSM调教',
    'beast': '野兽',
    'beauty': '美女',
    'bed': '床',
    'beer': '啤酒',
    'belt': '腰带',
    'bites': '咬痕',
    'blouse': '衬衫',
    'boots': '靴子',
    'boobs': '乳房',
    'boy': '男孩',
    'bra': '胸罩',
    'breasts': '乳房',
    'brunette': '棕发妹',
    'bunny': '兔女郎',
    'butt': '屁股',
    'cage': '鸟笼/贞操笼',
    'cat': '猫',
    'chain': '锁链',
    'chastity': '贞操',
    'cheating': '出轨',
    'choke': '锁喉',
    'cock': '阴茎',
    'collar': '项圈',
    'condom': '避孕套',
    'couch': '沙发',
    'cowgirl': '牛娘/女上位',
    'cum': '精液',
    'dark': '暗黑',
    'demon': '恶魔',
    'dick': '阴茎',
    'dildo': '假阳具',
    'dog': '狗',
    'dragon': '龙',
    'elf': '精灵',
    'feet': '双脚',
    'female': '女性',
    'futa': '扶他',
    'girl': '女孩',
    'glasses': '眼镜',
    'goddess': '女神',
    'goth': '哥特',
    'hair': '头发',
    'hand': '手',
    'hose': '丝袜',
    'latex': '乳胶',
    'legs': '双腿',
    'male': '男性',
    'milf': '熟女',
    'monster': '怪物',
    'nurse': '护士',
    'oil': '精油',
    'oral': '口交',
    'pussy': '小穴',
    'queen': '女王',
    'rope': '绳索',
    'sex': '性交',
    'skirt': '裙子',
    'slave': '肉奴',
    'stockings': '长筒袜',
    'swimsuit': '泳装',
    'tail': '尾巴',
    'tentacle': '触手',
    'toes': '脚趾',
    'trap': '伪娘',
    'vampire': '吸血鬼',
    'witch': '魔女/女巫',
    'wolf': '狼人',
}

fixed = 0
artist_count = 0

for row in rows:
    if row[1] == row[2]:
        name = row[1].strip()
        norm = name.lower()

        # Check if artist
        is_artist = False
        for a in known_artists_set:
            if a in norm:
                is_artist = True
                break
        if is_artist or norm.endswith(' sfm') or norm.endswith(' va') or norm.endswith(' 3d'):
            artist_count += 1
            continue

        # 1. Dict match
        if norm in general_dict:
            row[2] = general_dict[norm]
            fixed += 1
            continue

        # 2. Parentheses match
        if '(' in name and name.endswith(')'):
            base = name[:name.rfind('(')].strip()
            series = name[name.rfind('(')+1:-1].strip()

            base_cn = general_dict.get(base.lower(), base)
            series_cn = general_dict.get(series.lower(), series)
            row[2] = f"{base_cn} ({series_cn})"
            fixed += 1
            continue

print(f"Sweep done: Translated {fixed} tags, identified {artist_count} artist/studio tags.", flush=True)

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
