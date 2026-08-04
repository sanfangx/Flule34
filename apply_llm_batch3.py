import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

llm_dict_3 = {
    # NSFW Actions / Body Parts / Features
    'big tits': '大巨乳/大胸',
    'big white cock': '白人大巨根',
    'biggreen': '大绿/绿色巨物',
    'bigjohnson': '大约翰逊',
    'biker': '机车骑手/骑士装',
    'bikini bottom': '比基尼泳裤',
    'bikini top': '比基尼泳胸',
    'bimbo': '大胸丰满辣妹/呆萌辣妹',
    'biohazard': '生化危机/生物危害',
    'birdway': '鸟路/鸟人形态',
    'birth': '分娩/生育',
    'birthing': '生产/生育过程',
    'bisexual': '双性恋',
    'bite': '咬/轻咬',
    'biting lip': '咬嘴唇',
    'bitting finger': '咬手指',
    'bitting lip': '咬唇',
    'black': '黑色/黑人',
    'black and white': '黑白风格/单色',
    'black balls': '黑色睾丸',
    'black bars': '黑条遮挡/遮罩',
    'black body': '黑色身体',
    'black cock': '黑人大巨根',
    'black legwear': '黑色腿饰/黑袜',
    'black lipstick': '黑色唇膏/黑唇',
    'black male only': '仅黑人男性',
    'black nail polish': '黑色指甲油',
    'black penis': '黑色阴茎',
    'black screen roulette': '黑屏轮盘',
    'black spleen lotus': '黑脾莲花',
    'black stockings': '黑丝/黑色长统袜',
    'black toenails': '黑色脚趾甲',
    'black-framed glasses': '黑框眼镜',
    'blacked': 'Blacked品牌/黑人征服',
    'blackedweasel': 'Blacked黄鼠狼',
    'blank thumbnail': '空白缩略图',
    'bleached': '漂白/白发/金发',
    'blender': 'Blender3D建模软件',
    'blenderknight': 'Blender骑士',
    'blendy': 'Blender渲染风',
    'blinds': '百叶窗',
    'blood elf rogue': '血精灵盗贼 (魔兽世界)',
    'blood elf warlock': '血精灵术士 (魔兽世界)',
    'bloodhound (apex legend)': '寻血猎犬 (Apex英雄)',
    'bloodrayne': '吸血莱恩',
    'blowjob': '口交',
    'blowjob after ejaculation': '射精后口交/清理口交',
    'blowjob face': '口交表情/阿黑颜',
    'blue balls': '憋精/蛋疼',
    'blue body': '蓝色身体',
    'blue clothing': '蓝色衣服',
    'blue diamond': '蓝钻石',
    'blue eye': '蓝眼睛',
    'blue lipstick': '蓝唇膏',
    'bob': '波波头/短发',
    'bocchi the rock': '孤独摇滚!',
    'bodily fluids': '体液',
    'body distension': '身体胀大/膨胀',
    'body paint': '人体彩绘',
    'body part in ass': '肢体入臀/爆肛',
    'body swap': '灵魂互换/身体交换',
    'body tattoo': '全身纹身/刺青',
    'bodybuilding': '健美/健身',
    'bog rat': '沼泽老鼠',
    'bonnie': '邦尼 (玩具熊)',
    'boo': '害羞幽灵 (马里奥)',
    'boob and book': '巨乳与书本',
    'boosette': '幽灵姬 (马里奥姬化)',
    'boots only': '仅穿靴子/全身赤裸穿靴',
    'booty shorts': '热裤/超短裤',
    'bordeaux black': '波尔多黑',
    'boruto': '博人传',
    'boruto uzumaki (boruto)': '漩涡博人 (博人传)',
    'botchling': '妖灵/尸婴 (巫师3)',
    'bottom heavy': '下半身丰满/下身宽大',
    'bounce': '弹跳/乳摇',
    'bouncing butt': '臀摇/屁股弹跳',

    # Characters & Series
    'blanc (nikke goddess of victory)': '布兰儿 (胜利女神：妮姬)',
}

out_csv = 'assets/tags/rule34video_tags_zh.csv'
with open(out_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

updated_count = 0
for row in rows:
    name = row[1].strip()
    norm = name.lower()
    if norm in llm_dict_3:
        row[2] = llm_dict_3[norm]
        updated_count += 1

print(f"Applied LLM manual batch 3: Updated {updated_count} tags!")

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
