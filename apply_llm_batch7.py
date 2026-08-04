import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

llm_dict_7 = {
    # Actions & Terms
    'feet on legs': '双脚踩在腿上',
    'feet together': '双脚并拢',
    'felicia': '菲莉西亚 (恶魔战士)',
    'female': '女性',
    'female bodybuilder': '女子健美选手',
    'female domination': '女性主导/女尊/Femdom',
    'female focus': '主视女性/女性焦点',
    'female moaning': '女性呻吟/娇喘',
    'female monster': '女怪物/魔物娘',
    'female on bottom': '女下位',
    'female on futanari': '女性在下/扶他上位',
    'female on male': '女上位/女性压制男性',
    'female only': '全女性/全妹子',
    'female penetrated': '女性被插入',
    'female predator': '女性捕食者/捕猎女兽',
    'female protagonist': '女主角',
    'female rapist': '强暴者女性',
    'female solo': '女性单人/独奏',
    'femboy': '伪娘/伪娘男孩',
    'femboy on female': '伪娘上女性',
    'femshepard (mass effect)': '女薛帕德 (质量效应)',
    'feral': '兽态/野生兽/野性兽人',
    'feral on female': '野兽对女性/兽交',
    'feral on feral': '野兽对野兽',
    'fetish': '恋物/癖好/特化恋癖',
    'ffm': 'FFM/两女一男3P',
    'ffvii remake': '最终幻想7重制版',
    'filled condom': '灌满精液的避孕套',
    'filmmaker': '电影制片人/SFM制作者',
    'finger in mouth': '手指入嘴/咬手指',
    'finger licking': '舔手指',
    'finger on lip': '手指抵唇',
    'fingering pussy': '抠穴/手指插小穴',
    'fingering self': '自慰抠穴/自我安慰',
    'fire emblem awakening | fire emblem kakusei': '火焰之纹章:觉醒',
    'fire emblem three houses': '火焰之纹章:风花雪月',
    'first person perspective': '第一人称视角/POV',
    'fishnet': '渔网/渔网织物',
    'fishnet stockings': '渔网丝袜',
    'fit female': '健美身材女性',
    'fitness': '健身/健美房',
    'fleshlight': '飞机杯/名器杯',
    'fluffy pokemon': '毛茸茸宝可梦',
    'fluids': '体液/爱液喷溅',
    'focus blowjob': '特写口交/口交视角',
    'fondling': '抚摸/爱抚',
    'foot fetish': '恋足癖/足恋',
    'foot in mouth': '塞脚入嘴/吃脚趾',
    'foot juggling': '用脚颠弄',
    'foot lick': '舔脚/舔足',
    'foot licking': '舔足/舔脚心',
    'foot on face': '踩脸/脚踩脸庞',
    'foot smell': '闻脚/脚香',
    'foot smelling': '闻足癖',
    'foot smother': '用脚闷脸/踩脸捂嘴',
    'foot sniffing': '嗅足/嗅脚癖',
    'foot stool': '人肉脚垫/踏脚凳',
    'footwear': '鞋类/鞋饰',
    'forced anal': '强迫爆肛/强行后庭',
    'forced deepthroat': '强行深喉',
    'forced fellatio': '强迫口交',
    'forced oral': '强行口交',
    'forced pleasure': '强迫快感/强制高潮',
    'forced yaoi': '强迫BL/男男强暴',
    'forced yuri': '强迫百合/女女强暴',
    'foreskinjob': '包皮交/包皮手交',
    'fosters home for imaginary friends': '完美友谊/福斯贴之家',
    'four arms': '四条手臂',
    'frame by frame': '逐帧动画/高清逐帧',
    'french': '法语/法国风格',
    'french accent': '法语口音',
    'french kissing': '法式深吻/湿吻',
    'french subtitles': '法文字幕',

    # Characters & Series
    'fin mccloud (stoked)': '芬恩·麦克劳德 (冲浪少年)',
    'finn (starwars)': '芬恩 (星球大战)',
    'fiona (borderlands)': '菲奥娜 (无主之地传说)',
    'fiona (vindictus)': '菲奥纳 (洛奇英雄传)',
    'fn57 (girls frontline)': 'Five-seveN (少女前线)',
    'francesca de santis (hitman)': '弗朗切斯卡·德·圣蒂斯 (杀手47)',
    'francesca findabair (the witcher)': '法兰茜斯卡·芬达贝 (巫师3)',
    'frey holland (forspoken)': '芙蕾·霍兰德 (神领编年史/魔咒之地)',
    'freya (mobile legends bang bang)': '芙蕾雅 (无尽对决)',
    'friday night funkin': '周五夜放克 (FNF)',
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
    if norm in llm_dict_7:
        row[2] = llm_dict_7[norm]
        updated_count += 1

print(f"Applied LLM manual batch 7: Updated {updated_count} tags!")

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
