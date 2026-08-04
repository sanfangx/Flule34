import csv
import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

print("Executing full LLM dictionary sweep to completion...", flush=True)

# 1. Master translation mappings for remaining words
master_llm_dict = {
    # Actions, NSFW attributes, Body Parts, Positions
    'nipple biting': '咬乳头',
    'nipple clamp': '乳头夹/乳夹',
    'nipple erection': '乳头勃起/凸起',
    'nipple expansion': '乳头膨胀',
    'nipple fondling': '抚摸乳头',
    'nipple fuck': '乳头交/插乳头',
    'nipple lick': '舔乳头',
    'nipple licking': '舔舐乳头',
    'nipple penetration': '乳头插入',
    'nipple pinching': '捏乳头',
    'nipple play': '玩弄乳头',
    'nipple pulling': '拉扯乳头',
    'nipple rings': '乳环',
    'nipple slip': '露乳头/走光',
    'nipple stimulation': '刺激乳头',
    'nipple sucking': '吮吸乳头',
    'nipple torment': '折磨乳头/乳痛调教',
    'nipple tweaking': '拧捏乳头',
    'nipple-to-nipple': '乳头贴乳头',
    'no bra': '无胸罩/真空着装',
    'no condoms': '无套/无避孕套',
    'no panties': '无内裤/下体真空',
    'no panties under dress': '连衣裙下无内裤',
    'non-humanoid': '非人形生物',
    'non-humanoid feral': '非人形野兽',
    'nude': '全裸/赤裸',
    'nudity': '裸体/全裸状态',
    'oil': '润滑油/精油',
    'oiled breasts': '抹油爆乳',
    'oiled skin': '涂油肌肤/光泽皮肤',
    'oiling': '涂油/涂抹润滑油',
    'on bed': '在床上',
    'on couch': '在沙发上',
    'on desk': '在书桌上',
    'on floor': '在地板上',
    'on knees': '跪地姿势',
    'on side': '侧卧姿势',
    'on stomach': '趴着/俯卧姿势',
    'on table': '在桌子上',
    'one-piece swimsuit': '连体泳衣',
    'oral': '口交/口部性行为',
    'oral creampie': '口内射精/口爆',
    'oral cumshot': '口交射精特写',
    'orgasm': '高潮',
    'orgasm denial': '高潮控制/控精剥夺',
    'orgasm facial': '高潮颜射',
    'outdoor sex': '野外性交/打野战',
    'outdoors': '户外/野外',
    'overalls': '工装裤/吊带裤',
    'overhead': '头顶视角/俯瞰',
    'oviposition': '排卵/产卵调教',
    'paizuri': '乳交',
    'paizuri cumshot': '乳交射精特写',
    'panties': '内裤',
    'panties down': '褪下内裤',
    'panties aside': '内裤拉到一旁/拉开内裤',
    'pantyhose': '连裤袜/丝袜',
    'penetration': '插入',
    'penis': '阴茎/巨根',
    'penis in mouth': '阴茎在口中',
    'penis pump': '阴茎泵/抽吸增长器',
    'penis shadow': '阴茎投影/巨根影子',
    'pegging': '逆插/女用假阳具插入男性',
    'pet play': '宠物调教/人宠玩法',
    'piercing': '穿孔/穿环',
    'piggyback': '背着/背负姿势',
    'piss': '尿液/圣水',
    'pissing': '排尿/圣水调教',
    'pixiv': 'Pixiv/P站',
    'plap': '啪啪声/撞击声',
    'plapping': '激烈撞击/啪啪水声',
    'plug': '肛塞/塞子',
    'poh': 'POV/第一人称',
    'pony': '小马/马驹',
    'position': '体位/姿势',
    'possessive': '占有欲强/霸道强上',
    'pov': '第一人称视角/POV',
    'pregnant': '怀孕/孕妇',
    'preservation': '封存/保持姿势',
    'princess carry': '公主抱',
    'public sex': '公共场所性交/露癖性交',
    'pussy': '小穴/阴道',
    'pussy juice': '爱液/阴道分泌物',
    'pussy licking': '舔阴/舔穴',
    'pussy rub': '磨穴/阴部摩擦',
    'pussy stretch': '小穴扩张/撑大穴口',
    'pussy worship': '舔穴膜拜/小穴崇拜',
    'queen': '女王',
    'quicky': '快餐/速战速决',
    'rimming': '舔肛/毒龙钻',
    'rope bondage': '绳缚调教',
    'scat': '黄金/排泄调教',
    'seduction': '勾引/诱惑',
    'sex': '做爱/性交',
    'shemale': '伪娘/扶他',
    'shibari': '日式绳缚',
    'shower sex': '洗澡性交/淋浴性交',
    'sideways': '侧向体位',
    'slave': '奴隶/肉奴',
    'solo': '单人自慰/独奏',
    'spanking': '打屁股/打臀调教',
    'squirting': '喷水/潮吹',
    'stealth': '潜行/偷摸做爱',
    'straddling': '跨坐姿势',
    'strapon': '佩戴式假阳具/假阳具逆插',
    'succubus': '魅魔',
    'tentacles': '触手',
    'threesome': '3P/三人交配',
    'tied up': '捆绑/系紧',
    'titfuck': '乳交',
    'titty': '乳房/奶子',
    'topless': '半裸/上身赤裸',
    'tribadism': '磨豆腐/女同阴部摩擦',
    'uncircumcised': '包茎/未割包皮',
    'undressing': '脱衣服/解衣',
    'upskirt': '窥视裙底/偷拍裙底',
    'urethra penetration': '尿道插入',
    'vaginal penetration': '阴道插入',
    'vaginal sex': '阴道性交',
    'vibrator': '跳蛋/按摩棒',
    'voyeurism': '偷窥癖',
    'wet': '湿透/爱液泛滥',
    'whip': '皮鞭/鞭打调教',
    'x-ray': '透视/X光内视',
    'yiff': 'Furry性交/兽人交配',

    # Major Anime / Game Characters
    'nami (one piece)': '娜美 (航海王)',
    'nico robin (one piece)': '妮可·罗宾 (航海王)',
    'nezuko kamado (demon slayer)': '灶门祢豆子 (鬼灭之刃)',
    'nier automata': '尼尔:自动人形',
    'overwatch': '守望先锋',
    'pokemon': '宝可梦',
    'power (chainsaw man)': '帕瓦 (电锯人)',
    'pyra (xenoblade)': '焰 (异度神剑2)',
    'raiden shogun (genshin impact)': '雷电将军 (原神)',
    'remi (touhou)': '蕾米莉亚 (东方Project)',
    'reymu (touhou)': '博丽灵梦 (东方Project)',
    'rinn tohsaka (fate)': '远坂凛 (Fate)',
    'samus aran (metroid)': '萨姆丝·阿兰 (银河战士)',
    'saber (fate)': '阿尔托莉雅/Saber (Fate)',
    'shadowheart (baldurs gate)': '影心 (博德之门3)',
    'tifa lockhart (ff7)': '蒂法·洛克哈特 (最终幻想7)',
    'tracer (overwatch)': '猎空 (守望先锋)',
    'tsunade (naruto)': '纲手 (火影忍者)',
    'velma (scooby doo)': '韦尔玛 (叔比狗)',
    'yelan (genshin impact)': '夜兰 (原神)',
    'yor forger (spy x family)': '约尔·福杰 (间谍过家家)',
    'zelda (legend of zelda)': '塞尔达公主 (塞尔达传说)',
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
    if norm in master_llm_dict:
        row[2] = master_llm_dict[norm]
        updated_count += 1

print(f"Applied final master LLM dictionary: Updated {updated_count} tags!", flush=True)

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

print("Saved final translations to CSV!", flush=True)
