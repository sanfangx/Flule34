import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

llm_dict_4 = {
    # Actions & Terms
    'canon': '原作正统/正史',
    'canon crossdressing': '原作女装/伪娘着装',
    'cap': '帽子/帽子饰品',
    'captain': '队长/船长',
    'captions': '字幕/旁白说明',
    'cartoon': '美漫/卡通style',
    'cat suit': '紧身猫女服/皮衣',
    'cats': '猫咪/猫类',
    'celebrity': '名人/明星',
    'censored penis': '打码阴茎/圣光遮罩',
    'cerebella': '塞雷贝拉 (Skullgirls)',
    'cervix penetration': '子宫颈插入/深插宫颈',
    'cetacean': '鲸豚类/海洋哺乳动物',
    'cetacean penis': '鲸豚类阴茎',
    'cgi': 'CGI/3D计算机动画',
    'chains': '锁链/铁链',
    'changeling': '幻形族/变形怪 (小马宝莉)',
    'chaos': '混沌/混乱',
    'cheek kiss': '亲吻脸颊',
    'cheek tuft': '脸颊毛发/毛茸茸脸庞',
    'chest': '胸部/胸膛',
    'child bearing hips': '好生育的大屁股/宽胯臀',
    'chin grab': '捏住下巴',
    'chinese': '中文/中国',
    'chinese dress': '旗袍/中国传统服饰',
    'chinese subtitles': '中文字幕',
    'chip n dale rescue rangers': '奇蒂大冒险/救难小福星',
    'choke slam': '锁喉抛摔',
    'choke sounds': '窒息/咽哽声',
    'choking': '锁喉/窒息调教',
    'chowder': '巧达/厨神小当家卡通',
    'christmas clothing': '圣诞服装',
    'christmas hat': '圣诞帽',
    'christmas headwear': '圣诞头饰',
    'christmas outfit': '圣诞装',
    'chubby': '微胖/丰满微胖',
    'chuckling': '轻笑/窃笑',
    'cinderella': '灰姑娘',
    'circumcised': '割过包皮的/包皮环切',
    'clamp': '乳头夹/乳夹/夹具',
    'clapping cheeks': '啪啪作响撞击臀部/撞臀声',

    # Characters & Series
    'captain olimar (pikmin)': '欧利玛队长 (皮克敏)',
    'cell (dbz)': '沙鲁 (龙珠Z)',
    'cerys an craite (the witcher)': '凯瑞丝·安·史凯利格 (巫师3)',
    'cetrion (mortal kombat)': '赛崔恩 (真人快打)',
    'chenxing (snowbreak)': '晨星 (尘白禁区)',
    'chi-chi (dbz)': '琪琪 (龙珠Z)',
    'chie hoshinomiya (classroom of the elite)': '星之宫知惠 (欢迎来到实力至上主义的教室)',
    'chieru kazama (princess connect)': '风间千爱瑠 (公主连结)',
    'chihiro fujisaki (danganronpa)': '不二咲千寻 (弹丸论破)',
    'chika fujiwara (kaguya sama)': '藤原千花 (辉夜大小姐想让我告白)',
    'chika takami (love live)': '高海千歌 (LoveLive!)',
    'chiyuki kuwayama (the idolmaster)': '桑山千雪 (偶像大师)',
    'chloe (detroit become human)': '克洛伊 (底特律:变人)',
    'chloe (princess connect)': '克洛伊 (公主连结)',
    'chris yukine (symphogear)': '雪音克里斯 (战姬绝唱)',
    'christina (princess connect)': '克莉丝提娜 (公主连结)',
    'cinderella (nikke goddess of victory)': '辛德瑞拉 (胜利女神：妮姬)',
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
    if norm in llm_dict_4:
        row[2] = llm_dict_4[norm]
        updated_count += 1

print(f"Applied LLM manual batch 4: Updated {updated_count} tags!")

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
