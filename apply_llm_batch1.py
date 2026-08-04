import csv
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# Comprehensive LLM translation dictionary mapping built by AI reasoning
llm_dict = {
    # Numerical / Compositional
    '1animal': '1只动物',
    '1boy1girl': '1男1女',
    '1boys': '1男',
    '1elf': '1精灵',
    '1female': '1女性',
    '1femboy': '1伪娘',
    '1human': '1人类',
    '1monster': '1怪物',
    '1orc': '1兽人',
    '1robot': '1机器人',
    '2animals': '2只动物',
    '2d': '2D/二维',
    '2futas': '2扶他',
    '2monsters': '2只怪物',
    '360 vr': '360度VR全景',
    '3boys1girl': '3男1女',
    '3futas': '3扶他',
    '3toes': '3脚趾',
    '4fingers': '4手指',
    '4futas': '4扶他',
    '4k': '4K超清',
    '4th wall breaking': '打破第四面墙',
    '4toes': '4脚趾',
    '5toes': '5脚趾',
    '60fps': '60帧高帧率',
    '69 position': '69式姿势',
    '6boys': '6男',
    '6girls': '6女',
    '7futas': '7扶他',

    # Descriptive / Features / Actions
    'german': '德语/德国',
    'nurse redheart': '红心护士 (小马宝莉)',
    'no panties under skirt': '裙下无内裤/空挡',
    'princessleia': '莱娅公主',
    'abnormal': '异常/变态',
    'above view': '俯视视角',
    'absorption': '吸收/融合',
    'absurd res': '超高分辨率',
    'academia': '学院/学术',
    'accent': '口音/口音特色',
    'accessory': '饰品/配件',
    'activision': '动视',
    'adeptus steve': '史蒂夫大能 (Minecraft)',
    'adult female': '成年女性',
    'advertisement': '广告',
    'aegis': '宙斯盾',
    'after orgasm': '高潮之后/余韵',
    'against the glass': '贴在玻璃上',
    'aggressive': '强攻/粗暴',
    'aggretsuko': '冲吧烈子',
    'airtight': '气密/完全堵塞',
    'akari': '明/朱莉',
    'aladdin': '阿拉丁',
    'alien cock': '外星人巨根',
    'alien creature': '外星生物',
    'alien genitalia': '外星人生殖器',
    'alienabduction': '外星人绑架',
    'aliens': '外星人',
    'all grown up': '长大成人',
    'all the way to the base': '直插到底/全根没入',
    'alliance': '联盟',
    'allsex': '全套性交',

    # Characters & Series
    'serath (paragon)': '塞拉丝 (虚幻争霸)',
    '808 (hifi rush)': '808 (完美音浪)',
    'abby (the last of us 2)': '艾比 (美末2)',
    'abigail blyg (the quarry)': '阿比盖尔 (采石场惊魂)',
    'acht (splatoon)': '8号/阿八 (喷射战士)',
    'ada-1 (destiny)': '艾达-1 (命运)',
    'adam (record of ragnarok)': '亚当 (终末的女武神)',
    'ai hayasaka (love is war)': '早坂爱 (辉夜大小姐想让我告白)',
    'akane shinjou (gridman)': '新条茜 (SSSS.GRIDMAN)',
    'akane tendo (ranma 12)': '天道茜 (乱马1/2)',
    'akari kazemiya (princess connect)': '风宫爱理 (公主连结)',
    'akasha (gmod)': '阿卡莎 (盖瑞模组)',
    'akeha (nier automata)': '明羽 (尼尔:自动人形)',
    'akiha tohno (type moon)': '远野秋叶 (月姬/Type-Moon)',
    'akira tendo (zombie 100)': '天道辉 (僵尸100)',
    'akiza izinski (yu-gi-oh)': '十六夜咲夜/十六夜秋 (游戏王)',
    'alexis rhodes (yu-gi-oh)': '天上院明日香 (游戏王)',
    'alice (nikke goddess of victory)': '爱丽丝 (胜利女神：妮姬)',
    'alice liddell': '爱丽丝·利德尔 (爱丽丝疯狂回归)',
    'alicia acorn': '艾莉西亚松鼠 (刺猬索尼克)',
    'alina grey (the puella magi)': '阿莉娜·格雷 (魔法少女小圆外传)',
}

# Update function for full CSV
out_csv = 'assets/tags/rule34video_tags_zh.csv'
with open(out_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

updated_count = 0
for row in rows:
    name = row[1].strip()
    norm = name.lower()
    if norm in llm_dict:
        row[2] = llm_dict[norm]
        updated_count += 1

print(f"Applied LLM manual batch 1: Updated {updated_count} tags!")

with open(out_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in rows:
        writer.writerow(r)

with open('rule34video_tags_zh.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in rows:
        writer.writerow(r)
