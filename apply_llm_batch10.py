import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

llm_dict_10 = {
    # Terms & Actions
    'irish': '爱尔兰人/爱尔兰风格',
    'iron golem': '铁傀儡 (Minecraft)',
    'iron man | tony stark': '钢铁侠 / 托尼·斯塔克',
    'italian': '意大利人/意大利语',
    'italian subtitles': '意大利文字幕',
    'iwara': 'Iwara/站',
    'izanami': '伊邪那美',
    'izuku': '绿谷出久 (我的英雄学院)',
    'izuocha': '出茶CP (绿谷出久x丽日御茶子)',
    'jacket only': '仅穿外套/空档外套',
    'jacko challenge': 'Jack-O姿势挑战',
    'japanese': '日语/日本',
    'japanese dialogue': '对白',
    'japanese subtitles': '日文字幕',
    'japanese voice acting': '日文配音/声优配音',
    'jedi padawan': '绝地学徒 (星球大战)',
    'jiggle': '抖动/乳摇/臀摇',
    'jiggling': '剧烈摇晃/抖动',
    'jiggling ass': '巨臀摇晃/摇臀',
    'jiggling breasts': '爆乳摇晃/乳摇',
    'jiggly ass': '弹性臀部/摇摆翘臀',
    'jiggly butt': 'Q弹臀部',
    'job': '手交/口交/工作',
    'joi countdown': 'JOI倒计时/指示高潮',
    'jojos bizarre adventure': 'JOJO的奇妙冒险',
    'k/da series': 'K/DA女团系列 (英雄联盟)',

    # Characters & Series
    'iruma suzuki (mairimashita!)': '铃木入间 (魔入间)',
    'irumi miu (danganronpa)': '入间美兔 (弹丸论破)',
    'isobel (baldurs gate)': '伊索贝尔 (博人门3)',
    'itsuki nakano (5toubun no hanayome)': '中野五月 (五等分的新娘)',
    'jabba the hut (starwars)': '贾巴 (星球大战)',
    'jacob (the quarry)': '杰客布 (采石场惊魂)',
    'jacqui briggs (mortal kombat)': '杰奎·布里格斯 (真人快打)',
    'jane shepard (mass effect)': '简·薛帕德 (质量效应)',
    'jasmine (aladdin)': '茉莉公主 (阿拉丁)',
    'jesse faden (control)': '杰西·法登 (控制/Control)',
    'jessica riley (until dawn)': '杰西卡·莱利 (直到黎明)',
    'jodie holmes (beyond two souls)': '祖迪·霍姆斯 (超凡双生)',
    'jotaro (jojo\'s)': '空条承太郎 (JOJO的奇妙冒险)',
    'junko enoshima (danganronpa)': '江之岛盾子 (弹丸论破)',
    'kaede takagaki (the idolmaster)': '高垣枫 (偶像大师)',
    'kaguya shinomiya (character)': '四宫辉夜 (辉夜大小姐想让我告白)',
    'kaho hinata (blend-s)': '日向夏帆 (调教咖啡厅)',
    'kale (dbz)': '开尔 (龙珠超)',
    'kalifa': '卡莉法 (航海王)',
    'kalina (girls frontline)': '格林娜 (少女前线)',
    'kallen kozuki (code geas)': '红月卡莲 (叛逆的鲁路修)',
    'karlee (back 4 blood)': '卡莉 (喋血复仇)',
    'karyl (princess connect)': '凯露/臭鼬 (公主连结)',
    'kassandra (assassins creed)': '卡珊德拉 (刺客信条:奥德赛)',
    'kaveh (genhin impact)': '卡维 (原神)',
    'kawatake (kantai)': '川风 (舰队Collection)',
    'kazuma satou': '佐藤和真 (为美好的世界献上祝福！)',
    'kefla (dbz)': '开芙拉 (龙珠超)',
    'kei karuizawa (classroom of the elite)': '轻井泽惠 (欢迎来到实力至上主义的教室)',
    'kei shirogane (kaguya sama)': '白银圭 (辉夜大小姐想让我告白)',
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
    if norm in llm_dict_10:
        row[2] = llm_dict_10[norm]
        updated_count += 1

print(f"Applied LLM manual batch 10: Updated {updated_count} tags!")

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
