import csv
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

r34_csv = 'assets/tags/rule34video_tags_zh.csv'
with open(r34_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

# Known artist signatures (STRICT LIST, ONLY TRUE ARTIST USERNAMES)
strict_artists = {
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
    'bordeauxblackva', 'britishkass', 'bulgingsenpai'
}

# Extensive Vocabulary & Grammar Map for all position, species, action and state tags
phrase_dict = {
    'doggystyle position': '后入式姿势/后背位',
    'standing doggystyle position': '站立后入式姿势',
    'canine': '犬科/犬类',
    'canine on female': '犬交/犬科动物对女性',
    'canine on male': '犬科动物对男性',
    'futanari on canine': '扶他对犬科动物',
    'from front position': '前入式姿势/正面体位',
    'kneeling oral position': '跪姿口交',
    'missionary position': '正常位/传教士体位',
    'multiple positions': '多种体位/换姿势交配',
    'prison guard position': '狱警体位/压制体位',
    'reverse piledriver position': '反向打桩机体位',
    'side saddle position': '侧骑体位/侧面姿势',
    'stand and carry position': '站立抱起体位/抱立交配',
    'table lotus position': '桌上观音坐莲体位',
}

# Words parser for dynamic assembly
words_db = {
    'canine': '犬科/犬类', 'feline': '猫科', 'equine': '马科', 'bovine': '牛科',
    'porcine': '猪科', 'vulpine': '狐科', 'lupine': '狼科', 'reptilian': '爬行类',
    'dragon': '龙', 'monster': '怪物', 'demon': '恶魔', 'human': '人类',
    'anthro': '兽人', 'feral': '野兽', 'furry': '福瑞', 'female': '女性',
    'male': '男性', 'futanari': '扶他', 'femboy': '伪娘', 'girl': '女孩',
    'doggystyle': '后入式', 'missionary': '正常位', 'cowgirl': '女上位',
    'reverse': '反向', 'standing': '站立式', 'kneeling': '跪姿',
    'lying': '躺姿', 'sitting': '坐姿', 'carrying': '抱起',
    'position': '体位/姿势', 'pose': '姿势', 'sex': '性交', 'mating': '交配',
    'penetration': '插入', 'oral': '口交', 'anal': '后庭', 'vaginal': '小穴插入',
}

fixed_count = 0

for row in rows:
    if row[1] == row[2]:
        name = row[1].strip()
        norm = name.lower()

        # Check explicit phrase dict
        if norm in phrase_dict:
            row[2] = phrase_dict[norm]
            fixed_count += 1
            continue

        # Check X on Y
        if ' on ' in norm:
            parts = norm.split(' on ')
            if len(parts) == 2:
                p1, p2 = parts[0].strip(), parts[1].strip()
                t1 = words_db.get(p1, p1)
                t2 = words_db.get(p2, p2)
                if t1 != p1 or t2 != p2:
                    row[2] = f"{t1}压制{t2}/{t1}对{t2}"
                    fixed_count += 1
                    continue

        # Check "... position"
        if norm.endswith(' position'):
            base_p = norm[:-9].strip()
            # Try to build base
            base_words = base_p.split(' ')
            mapped_b = [words_db.get(w, w) for w in base_words]
            row[2] = f"{''.join(mapped_b)}姿势/体位"
            fixed_count += 1
            continue

print(f"Fixed position & species tags: Updated {fixed_count} tags!", flush=True)

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
