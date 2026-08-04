import csv
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

r34_csv = 'assets/tags/rule34video_tags_zh.csv'
with open(r34_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

# Known artist signatures or creator usernames to strictly keep as original
known_artist_words = {
    'arawaraw', '4ere4nik', 'a.lias', 'adriandustred', 'akkoarcade',
    'alexandraus', 'alexia vo', 'allie (slipperyt)', 'almightypatty',
    'alynisa', 'alyxreplace', 'appletin', 'amateurthrowaway', 'ambrosine92',
    'anarchygentleman', 'anaru', 'andrastae', 'anianiboy', 'animmage',
    'annbee (woebeeme)', 'anosluz', 'arnoldthehero', 'audiodude (audio)',
    'audionoob', 'auxtasy', 'awwman', 'ayasz', 'ayyteethreedee', 'azantar',
    'bacn', 'balak', 'baronstrap', 'batesz', 'bayernsfm (aritst)', 'ronin-jelly',
    'jayewilde', 'slipperyt', 'peculiart', 'slyxxx24', 'woebeeme', 'beastlyjoe',
    'beastsnthings', 'bewyx', 'bia (slipperyt)', 'bellum-art'
}

words_map = {
    'big': '大', 'huge': '巨大', 'giant': '巨人', 'tiny': '微型/娇小',
    'black': '黑色/黑人', 'white': '白人/白色', 'red': '红色', 'blue': '蓝色', 'green': '绿色',
    'pink': '粉色', 'purple': '紫色', 'yellow': '黄色', 'golden': '金色', 'silver': '银色',
    'cock': '阴茎/巨根', 'penis': '阴茎', 'dick': '阴茎', 'balls': '睾丸/蛋蛋',
    'pussy': '小穴/阴道', 'ass': '屁股/臀部', 'butt': '翘臀', 'breasts': '乳房/爆乳',
    'boobs': '奶子', 'tits': '乳房', 'nipples': '乳头', 'areola': '乳晕',
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
}

fixed_count = 0

for row in rows:
    if row[1] == row[2]:
        tag = row[1].strip()
        norm = tag.lower()

        # Skip explicit artist names
        if norm in known_artist_words or norm.endswith(' (artist)') or norm.endswith(' sfm') or norm.endswith(' va'):
            continue

        # Try to translate multi-word phrases using vocab map
        parts = norm.split(' ')
        translated_parts = []
        all_matched = True
        
        for p in parts:
            if p in words_map:
                translated_parts.append(words_map[p])
            else:
                all_matched = False
                break

        if all_matched and len(translated_parts) > 0:
            row[2] = "".join(translated_parts)
            fixed_count += 1

print(f"Deep NLP multi-word translation: Fixed {fixed_count} additional non-artist tags!", flush=True)

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
