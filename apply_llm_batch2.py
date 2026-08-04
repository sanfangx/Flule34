import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

llm_dict_2 = {
    # Actions & Anatomy & Clothing & Quality
    'archer': '弓箭手/弓兵',
    'areola': '乳晕',
    'arm grab': '抓住手臂',
    'arm sleeves': '袖套',
    'armpit licking': '舔腋下',
    'arms tied': '捆绑双手',
    'armwear': '手臂佩饰',
    'artificial intelligence': '人工智能/AI',
    'moral support': '精神支持',
    'platinum blonde hair': '白金发/银发',
    'source': '来源/出处',
    'female on bottom': '女下位/女在下方',
    'clothed': '穿衣/着装',
    'ash': '灰烬/小智/小灰',
    'ashen blight': '灰烬病',
    'asian female': '亚裔女性',
    'ass gape': '肛门扩展/扩肛',
    'ass grab': '抓屁股/摸臀',
    'ass juice': '肠液/爱液',
    'ass to ass': '臀对臀',
    'ass to mouth': '转口交/ATM',
    'ass up': '翘臀/抬高屁股',
    'assassins creed': '刺客信条',
    'assertive': '强势/主导',
    'assistant sam': '助手萨姆',
    'assjob': '臀交/夹臀',
    'asylum': '精神病院/避难所',
    'atheltic': '健美/运动型',
    'athletic female': '健美女性',
    'athletic futanari': '健美扶他',
    'athletic male': '健美男性',
    'atlantis the lost empire': '亚特兰蒂斯:失落的帝国',
    'attack on titan': '进击的巨人',
    'audible creampie': '有声中出/中出水声',
    'audio cake': '音频蛋糕',
    'audio only': '纯音频',
    'autodesk maya': 'Autodesk Maya软件',
    'avatar the last airbender': '降世神通:最后的气宗',
    'avengers': '复仇者联盟',
    'avian': '鸟类人/羽人',
    'babe': '辣妹/宝贝',
    'babes': '美女/辣妹们',
    'back view': '后视视角/背影',
    'background music': '背景音乐/BGM',
    'background noise': '背景杂音',
    'backshots': '后入视角/后背撞击',
    'backside': '后背/背面',
    'bad dragon dildo': '坏龙假阳具 (Bad Dragon)',
    'ball caress': '抚摸睾丸',
    'ball clenching': '揉捏蛋蛋',
    'ball expansion': '睾丸膨胀',
    'ball fondling': '玩弄睾丸',
    'ball grab': '抓住蛋蛋',
    'ball inflation': '睾丸充气膨胀',
    'ball lick': '舔舐睾丸',
    'ball slap': '拍打睾丸',
    'ball sucking': '吮吸睾丸',

    # Characters & Series
    'ariel (the little mermaid)': '爱丽儿 (小美人鱼)',
    'arisha (vindictus)': '艾丽莎 (洛奇英雄传)',
    'asahi serizawa (the idolmaster)': '芹泽朝日 (偶像大师)',
    'shizuru hoshino (princess connect)': '藤野静流 (公主连结)',
    'chai (hifi rush)': '阿柴 (完美音浪)',
    'ashley baker (silent hill)': '阿什莉·贝克 (寂静岭)',
    'ashley brown (untill dawn)': '阿什莉·布朗 (直到黎明)',
    'asuka (wwe diva)': '明日华 (WWE女子选手)',
    'athena (king of fighters)': '麻宫雅典娜 (拳皇)',
    'audrey ii (little shop of horrors)': '奥德丽二世 (恐怖小店)',
    'aura the guillotine (frieren beyond journeys end)': '断头台阿乌拉 (葬送的芙莉莲)',
    'ava (borderlands)': '阿瓦 (无主之地)',
    'aya maruyama (bang dream)': '丸山彩 (BanG Dream!)',
    'aya shameimaru': '射命丸文 (东方Project)',
    'aylin (baldurs gate)': '艾林女士 (博德之门3)',
    'azuma haruka (saint dorei gakuen)': '东遥 (圣奴隶学园)',
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
    if norm in llm_dict_2:
        row[2] = llm_dict_2[norm]
        updated_count += 1

print(f"Applied LLM manual batch 2: Updated {updated_count} tags!")

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
