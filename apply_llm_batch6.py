import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

llm_dict_6 = {
    # Actions & Terms
    'dripping semen': '滴落精液/精水顺流',
    'dubbed': '配音版/译制配音',
    'dubious consent': '半推半就/模糊同意/违抗感',
    'dungeons and dragons': '龙与地下城 (D&D)',
    'duo': '双人组合/两人',
    'dwarf female': '矮人女性',
    'dwarfs': '矮人/地精',
    'dynasty warriors': '真·三国无双',
    'ear penetration': '耳孔插入',
    'ear rub': '抚摸耳朵/捏耳朵',
    'ear twitch': '抖动耳朵',
    'earring': '耳环/耳饰',
    'ears': '兽耳/耳朵',
    'earth pony': '陆马 (小马宝莉)',
    'earthbending': '御土术 (降世神通)',
    'ebony': '黑人/黑肉妹',
    'echidna': '针鼹/艾奇多娜',
    'edging': '边缘控精/憋精调教',
    'edging blowjob': '边缘控精口交',
    'eeveelution': '伊布进化形态 (宝可梦)',
    'egg insertion': '塞入排卵/塞蛋调教',
    'eggs': '排卵/兽卵/虫卵',
    'egirl': 'E-Girl/网红辣妹',
    'egyptian': '埃及风格/埃及',
    'egyptian princess': '埃及公主',
    'eldritch': '克苏鲁/古神异形',
    'electric shocks': '电击调教',
    'elevator sex': '电梯性交',
    'elf ears': '精灵尖耳',
    'elven': '精灵族的',
    'elves': '精灵/精灵族',
    'emo': '哥特暗黑/EMO风格',
    'endless': '无休止/连续不断',
    'endured face': '忍耐表情/忍受折磨',
    'english': '英语/英文',
    'english dialogue': '英文对白',
    'english subtitles': '英文字幕',
    'english voice': '英文配音',
    'enjoying': '享受其中/沉愉',
    'enthusiastic': '热情主导/主动拉客',
    'equestria girls': '小马宝莉:女孩系列',
    'equine': '马类/马科',
    'equine cock': '马巨根/马交根',
    'erotic': '色情/情色风',
    'european': '欧洲人/白人风',
    'evil': '邪恶化/堕落化',
    'excessive bestiality': '过度兽交',
    'excessive creampie': '海量中出/注入过度',
    'excessive cum in pussy': '大量精液填满小穴',
    'excessive cum inside': '体内注入巨量精液',
    'excessive impregnation': '多次受孕/深度受精',
    'exhibition': '裸露展示/露癖',
    'exhibitionist': '暴露狂/户外露出癖',
    'exposed': '露出/袒胸露乳',
    'exposed anus': '露出肛门',
    'exposed ass': '露出翘臀',
    'exposed breasts': '露出胸部/爆乳',
    'exposed nipples': '露乳头/凸起',

    # Characters & Series
    'dsr-50 (girls frontline)': 'DSR-50 (少女前线)',
    'edith (mobile legends bang bang)': '伊迪丝 (无尽对决)',
    'eida (boruto)': '艾达 (博人传)',
    'elegg (nikke: goddess of victory)': '埃莱格 (胜利女神：妮姬)',
    'eli ayase (love live)': '绚濑绘里 (LoveLive!)',
    'elizabeth (bioshock)': '伊丽莎白 (生化奇兵:无限)',
    'ellie (the last of us 2)': '艾莉 (美末2)',
    'emilia (rezero)': '爱蜜莉雅 (Re:从零开始的异世界生活)',
    'emma (the quarry)': '艾玛 (采石场惊魂)',
    'enya (snowbreak)': '恩雅 (尘白禁区)',
    'erasa (dbz)': '伊拉莎 (龙珠Z)',
    'erina nakiri (shokugeki no soma)': '薙切绘理奈 (食戟之灵)',
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
    if norm in llm_dict_6:
        row[2] = llm_dict_6[norm]
        updated_count += 1

print(f"Applied LLM manual batch 6: Updated {updated_count} tags!")

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
