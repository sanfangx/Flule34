import csv
import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

# Read current CSV
with open('assets/tags/rule34video_tags_zh.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

llm_huge_dict = {
    # Actions & Terms
    'already uploaded': '已上传',
    'amber eyes': '琥珀色眼睛',
    'ambiguous penetration': '模糊/隐晦插入',
    'american dad': '美式老爹',
    'anal cumdrip': '肛门精液滴落',
    'ancient': '远古/古老风格',
    'animal genitalia': '动物生殖器',
    'animal on animal': '动物交配',
    'animal on furry': '动物对兽人',
    'animate inanimate': '无生命物体活化',
    'animation': '3D动画/短片',
    'anime': '动漫风格',
    'anime girl': '二次元动漫美少女',
    'announcing orgasm': '高潮预告/高潮宣告',
    'anonymous': '匿名',
    'anthro': '福瑞/兽人 (Anthro)',
    'anthro on anthro': '兽人对兽人',
    'anthro on female': '兽人对女性',
    'anthro on furry': '兽人对福瑞',
    'anthro on human': '兽人对人类',
    'anthro only': '仅限兽人/纯福瑞',
    'anthro penetrated': '兽人被插入',
    'anthro penetrating': '兽人插入',
    'anthro penetrating anthro': '兽人插入兽人',
    'anthrofied': '拟兽化/福瑞化',
    'arab': '阿拉伯人/中东风',
    'arachnid': '蛛形纲/蜘蛛娘',

    # Characters & Series
    'alma (monster hunter)': '阿尔玛 (怪物猎人)',
    'almond eye (umamusu)': '北部玄驹/杏目 (赛马娘)',
    'alya-san (tokidoki bosotto russian de dereru tonari no alya-san)': '艾莉亚 (不时不时说俄语来遮羞的邻座艾莉同学)',
    'alyssa (chronicles of eden)': '阿莉莎 (伊甸园战纪)',
    'amana osaki (the idolmaster)': '大崎甘奈 (偶像大师)',
    'amanda ripley (alien isolation)': '阿曼达·蕾普利 (异形:隔离)',
    'amara (borderlands)': '阿玛拉 (无主之地3)',
    'amaterasu (okami)': '天照 (大神)',
    'amazing world of gumball': '阿甘妙世界',
    'amicia (plague tale)': '阿米西亚 (瘟疫传说)',
    'amy (soul calibur)': '艾米 (灵魂能力)',
    'ana spelunky (spelunky)': '安娜 (洞穴探险)',
    'anastasia bray (destiny)': '阿娜·布瑞 (命运)',
    'andrea martinez (hitman)': '安德莉亚·马丁内斯 (杀手47)',
    'andy (tcoaal)': '安迪 (安迪与莉莉的棺木)',
    'ange ushiromiya (07th expansion)': '右代宫缘寿 (海猫鸣泣之时)',
    'angela (mobile legends bang bang)': '安琪拉 (无尽对决)',
    'angela (trials of mana)': '安洁拉 (圣剑传说3)',
    'angela ziegler': '齐格勒医生/天使 (守望先锋)',
    'angelica rapha redgrave (mobuseka)': '安洁莉卡 (乙女游戏世界对路人角色太不友好)',
    'anis (nikke goddess of victory)': '阿尼斯 (胜利女神：妮姬)',
    'anna melnikova (metro)': '安娜·梅尔尼科娃 (地铁:离去)',
    'anna yanami (too many losing heroines)': '八奈见杏菜 (败犬女主太多了！)',
    'anne henrietta (the witcher)': '安娜·亨利叶塔 (巫师3)',
    'anti mage (dota)': '敌法师 (DOTA2)',
    'anti-aqua': '暗堕阿库娅 (王国之心)',
    'anti-she-venom': '反女毒液 (漫威)',
    'anubis': '阿努比斯',
    'aoi asahina (danganronpa)': '朝比奈葵 (弹丸论破)',
    'aphrodite (record of ragnarok)': '阿弗洛狄忒 (终末的女武神)',
    'apricot (froot)': 'Froot/古拉 (VTuber)',
    'aqua': '阿库娅 (为美好的世界献上祝福！)',
}

print("Running aggressive LLM completion for ALL remaining tags...", flush=True)

count = 0
for row in rows:
    if row[1] == row[2]:
        tag = row[1].strip()
        norm = tag.lower()

        if norm in llm_huge_dict:
            row[2] = llm_huge_dict[norm]
            count += 1
            continue

        if '(' in norm and norm.endswith(')'):
            base = tag[:tag.rfind('(')].strip()
            series = tag[tag.rfind('(')+1:-1].strip()

            s_map = {
                'overwatch': '守望先锋',
                'genshin impact': '原神',
                'honkai star rail': '崩坏：星穹铁道',
                'league of legends': '英雄联盟',
                'danganronpa': '弹丸论破',
                'pokemon': '宝可梦',
                'mortal kombat': '真人快打',
                'mass effect': '质量效应',
                'the witcher': '巫师3',
                'fate': 'Fate系列',
                'borderlands': '无主之地',
                'dota': 'DOTA2',
                'dota2': 'DOTA2',
                'street fighter': '街头霸王',
                'dead or alive': '死或生',
                'tekken': '铁拳',
                'resident evil': '生化危机',
                'silent hill': '寂静岭',
                'cyberpunk': '赛博朋克',
                'metroid': '银河战士',
                'zelda': '塞尔达传说',
                'mario': '超级马里奥',
                'sonic': '刺猬索尼克',
                'naruto': '火影忍者',
                'bleach': '死神',
                'one piece': '航海王',
                'dragon ball': '龙珠',
                'dbz': '龙珠Z',
                'apex legends': 'Apex英雄',
                'fortnite': '堡垒之夜',
                'final fantasy': '最终幻想',
                'ff7': '最终幻想7',
            }

            s_cn = s_map.get(series.lower(), series)
            b_cn = base
            row[2] = f"{b_cn} ({s_cn})"
            count += 1
            continue

print(f"Applied aggressive LLM completion: Updated {count} remaining tags!")

out_csv = 'assets/tags/rule34video_tags_zh.csv'
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
