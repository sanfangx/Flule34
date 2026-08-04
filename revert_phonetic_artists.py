import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

r34_csv = 'assets/tags/rule34video_tags_zh.csv'
with open(r34_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

# List of forced phonetic translations that should be restored to raw English (since they are artist IDs)
phonetic_artist_reversals = {
    '阿拉瓦拉': 'arawaraw',
    '切列普尼克': '4ere4nik',
    '别名/艾利亚斯': 'a.lias',
    '阿比盖尔 (PeculiArt)': 'abigail (peculiart)',
    '阿德里安尘红': 'adriandustred',
    '阿柯街机': 'akkoarcade',
    '亚历山德拉': 'alexandraus',
    '亚历克西娅配音': 'alexia vo',
    '艾莉 (SlipperyT)': 'allie (slipperyt)',
    '全能帕蒂': 'almightypatty',
    '艾琳妮萨': 'alynisa',
    '艾莉克丝替代': 'alyxreplace',
    '苹果汀': 'appletin',
    '业余抛弃': 'amateurthrowaway',
    '安布罗辛92': 'ambrosine92',
    '无政府绅士': 'anarchygentleman',
    '安娜鲁': 'anaru',
    '安德拉斯蒂': 'andrastae',
    '阿尼阿尼男孩': 'anianiboy',
    '动漫法师': 'animmage',
    '安蜂 (WoeBeeMe)': 'annbee (woebeeme)',
    '阿利亚 (Slyxxx24)': 'aria (slyxxx24)',
    '英雄阿诺德': 'arnoldthehero',
    '魅魔阿什莉': 'ashley succubi',
    '音频大佬': 'audiodude (audio)',
    '音频菜鸟': 'audionoob',
    '辅助迷幻': 'auxtasy',
    '嗷曼': 'awwman',
    '阿亚兹': 'ayasz',
    '艾特3D': 'ayyteethreedee',
    '阿赞塔尔': 'azantar',
    '培根': 'bacn',
    '巴拉克': 'balak',
    '男爵绑带': 'baronstrap',
    '贝茨': 'batesz',
    '拜仁SFM (画师)': 'bayernsfm (aritst)',
    '浪人果冻': 'ronin-jelly',
    '杰伊怀尔德': 'jayewilde',
    '野兽与万物': 'beastsnthings',
    '贝伦艺术': 'bellum-art',
    '贝威克斯': 'bewyx',
    '烈焰动画': 'blazeani',
    '蓝冰山': 'blueberg',
    '蓝光': 'bluelight',
    '蓝骨': 'bluethebone',
    '邦德': 'bonde',
    '疯狂MV': 'bonkersmv',
    '轰巴达轰': 'boombadaboom',
    '波尔多黑配音': 'bordeauxblackva',
    '英国卡斯': 'britishkass',
    '膨胀S': 'BulgingS',
    '膨胀学长': 'bulgingsenpai',
    '凯莉3D': 'cally3d',
    '追逐尼禄': 'chasingnero',
    '切洛多伊': 'chelodoy',
    '切洛蒂': 'chelody',
    '雪莉 (HexVoid)': 'cheri (hexvoid)',
    '灰烬树精': 'cinderdryadva',
    '班级宅男': 'class sweeb',
    '科巴特艺术': 'cobatsart',
    '优波上校': 'colonelyobo',
    '雷金指挥官': 'comandorekin',
    '水鸡27': 'coot27',
    '棉尾兔配音': 'cottontailva',
    '计数器SFM': 'countersfm',
    '飞天小女警队长': 'cpt-flapjack',
    '奶油肉汁': 'creamygravy',
    '赛博独特': 'cyberunique',
    '红气旋': 'cyclonered',
    '达卡德': 'dacad',
    '大哥': 'dage',
    '达鲨鱼': 'dahsharky',
    '达西·瑞德': 'darcy redd',
    '暗黑梦境VR': 'darkdreamsvr',
    '黑洞工坊': 'darkholestuff',
    '龙之屁': 'datdragonfart',
    '丹丹多': 'dendendo',
    '丹尼斯M': 'denisem',
    '丹托尔': 'dentol',
    '迪奥吉': 'deoggy',
    '渴望现实': 'desire reality',
    '戴斯蒂奈': 'destinnae',
    '恶魔之泣': 'devilscry',
    '德兹商场': 'dezmall',
    'D发生器': 'dgenerator',
    '狄维斯': 'diives',
    '迪米普隆': 'dimipron',
    '德米特里': 'dmitrys',
    'DMT': 'dmt',
    '车管所': 'dmv',
    '紫博士2K': 'doctorpurple2k',
    '多米诺猫咪': 'dominokotya',
    '多恩配音': 'dornva',
    '多布': 'doub',
    '面团室': 'doughroom',
    '偏离博士': 'dr deviant',
    '自攻螺丝/自钻SMS': 'Selfdrillingsms'
}

reverted_count = 0
for row in rows:
    if row[2] in phonetic_artist_reversals:
        row[2] = phonetic_artist_reversals[row[2]]
        reverted_count += 1
    elif row[2].istitle() and not (' (' in row[1] or ' ' in row[1]): # restore pure capitalized fallback IDs
        # If it was fallback Title Case from raw ID
        if row[2].lower() == row[1].lower():
            row[2] = row[1]
            reverted_count += 1

print(f"Reverted {reverted_count} forced phonetic artist names back to clean original English!")

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
