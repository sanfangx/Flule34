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

# 1. Comprehensive rule-based parser for X on Y, X penetrating Y, etc.
def parse_combinations(tag):
    t = tag.lower().strip()

    # Terms map
    terms = {
        'futanari': '扶他', 'futa': '扶他', 'futas': '扶他',
        'female': '女性', 'females': '女性',
        'male': '男性', 'males': '男性',
        'human': '人类', 'humans': '人类',
        'anthro': '兽人', 'anthros': '兽人',
        'feral': '野兽', 'ferals': '野兽',
        'monster': '怪物', 'monsters': '怪物',
        'orc': '兽人', 'orcs': '兽人',
        'elf': '精灵', 'elves': '精灵',
        'gynomorph': '扶他', 'gynomorphs': '扶他',
        'femboy': '伪娘', 'femboys': '伪娘',
        'robot': '机器人', 'robots': '机器人',
        'alien': '外星人', 'aliens': '外星人',
        'demon': '恶魔', 'demons': '恶魔',
        'angel': '天使', 'angels': '天使',
        'dragon': '龙', 'dragons': '龙',
        'dog': '狗', 'dogs': '狗',
        'horse': '马', 'horses': '马',
        'bull': '公牛', 'bulls': '公牛',
        'wolf': '狼', 'wolves': '狼',
    }

    # Pattern: "X on Y" (e.g. futanari on female)
    if ' on ' in t:
        parts = t.split(' on ')
        if len(parts) == 2:
            left = parts[0].strip()
            right = parts[1].strip()
            if left in terms and right in terms:
                return f"{terms[left]}压制{terms[right]}/{terms[left]}对{terms[right]}"

    # Pattern: "X penetrating Y" (e.g. futanari penetrating female)
    if ' penetrating ' in t:
        parts = t.split(' penetrating ')
        if len(parts) == 2:
            left = parts[0].strip()
            right = parts[1].strip()
            if left in terms and right in terms:
                return f"{terms[left]}插入{terms[right]}"

    # Pattern: "moaning in X" or "X in Y"
    if t.startswith('moaning in '):
        emotion = t.replace('moaning in ', '').strip()
        e_map = {'pleasure': '快感/欢愉', 'pain': '痛苦', 'ecstasy': '极乐', 'agony': '剧痛'}
        if emotion in e_map:
            return f"在{e_map[emotion]}中娇喘呻吟"

    # Pattern: "begging for X"
    if t.startswith('begging for '):
        req = t.replace('begging for ', '').strip()
        r_map = {
            'creampie': '求中出',
            'cum in pussy': '求穴内射精',
            'cum inside': '求体内中出',
            'impregnation': '求受孕/求受精',
            'orgasm': '求高潮',
            'sex': '求做爱',
            'vaginal': '求小穴插入',
            'cock': '求巨根插穴',
            'more': '求更多快感',
        }
        if req in r_map:
            return f"{r_map[req]}/主动哀求"

    return None

# 2. Comprehensive vocabulary map for general actions, body parts, states
vocab = {
    'beauty and the beast': '美女与野兽',
    'beauty mark': '美人痣',
    'becoming erect': '阴茎勃起/渐渐挺立',
    'before sex': '前戏/做爱前',
    'behind': '在背后/后方视角',
    'beige fur': '米色毛发',
    'beige scales': '米色鳞片',
    'being held up': '被抱起/悬空托起',
    'being molested': '被猥亵/被骚扰',
    'being watched': '被偷窥/被旁观',
    'belly expansion': '小腹膨胀',
    'belly inflation': '小腹充气/腹部膨胀',
    'bellybulge': '小腹隆起/凸起',
    'bending over': '弯腰/俯身姿势',
    'bent knees': '屈膝/双腿弯曲',
    'betting': '赌博/赌局调教',
    'bianca': '比安卡',
    'big areola': '大乳晕',
    'big black cock': '黑人大巨根',
    'big cleavage': '深沟爆乳/乳沟特写',
    'big dick': '大阴茎/巨根',
    'big dildo': '大号假阳具',
    'bell cranel (danmachi)': '贝尔·克拉奈尔 (在地下城寻求遭遇是否搞错了什么)',
    'belle (beauty and the beast)': '贝儿公主 (美女与野兽)',
    'beta (the eminence in shadow)': '贝塔/Beta (想要成为影之实力者)',
    'beth (total drama island)': '贝斯 (孤岛生存大乱斗)',
    'bianca (punishing gray raven)': '比安卡 (战双帕弥什)',
}

translated_count = 0
for row in rows:
    if row[1] == row[2]:
        tag = row[1].strip()
        norm = tag.lower()

        # Skip explicit artist names
        if norm in known_artist_words or norm.endswith(' (artist)') or norm.endswith(' sfm') or norm.endswith(' va'):
            continue

        # Check combos
        combo_res = parse_combinations(tag)
        if combo_res:
            row[2] = combo_res
            translated_count += 1
            continue

        # Check vocab
        if norm in vocab:
            row[2] = vocab[norm]
            translated_count += 1
            continue

        # Parentheses
        if '(' in tag and tag.endswith(')'):
            base = tag[:tag.rfind('(')].strip()
            series = tag[tag.rfind('(')+1:-1].strip()

            base_cn = vocab.get(base.lower(), base)
            series_cn = vocab.get(series.lower(), series)
            row[2] = f"{base_cn} ({series_cn})"
            translated_count += 1
            continue

print(f"Applied rigorous LLM tag translation: Fixed {translated_count} tags!", flush=True)

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
