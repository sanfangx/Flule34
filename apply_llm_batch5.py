import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

llm_dict_5 = {
    # Batch 5: Actions, Cum, D-F Terms & Characters
    'cum everywhere': '精液满地/到处是精',
    'cum explosion': '精液爆发/大喷精',
    'cum filled condom': '装满精液的避孕套',
    'cum from nose': '精液从鼻孔流出',
    'cum in own mouth': '射进自己嘴里/自饮精液',
    'cum in penis': '精液射入阴茎',
    'cum inside balls': '精液射进睾丸',
    'cum leaking': '精液流出/精液外溢',
    'cum multiple times': '多次射精/连续高潮',
    'cum on abs': '射在腹肌上',
    'cum on balls': '射在蛋蛋上',
    'cum on eye': '射在眼睛上/颜射入眼',
    'cum on glass': '射在玻璃上',
    'cum on hand': '射在手心',
    'cum on own face': '射在自己脸上/自颜射',
    'cum on panties': '射在内裤上',
    'cum on thighs': '射在大腿上',
    'cum on upper body': '射在上半身',
    'cum on viewer': '射向观众/视角射精',
    'cum out ass': '精液从肛门流出/肠内排出精液',
    'cum out mouth': '精液从口中溢出',
    'cum outside': '体外射精',
    'cum over breasts': '射在乳房上/胸射',
    'cum puke': '吐精/反胃吐精',
    'cum ring': '精液环/精圈',
    'cum share': '共享精液/品尝精液',
    'cum splatter': '精液飞溅',
    'cum stain': '精渍/精液印记',
    'cum swallow': '吞精',
    'cum through': '精液穿透/射穿',
    'cum twice': '射精两次/二次射精',
    'cum vomit': '吐出精液',
    'cum while penetrated': '被插入时高潮射精',
    'cumshot': '射精特写/射精',
    'cumshot in mouth': '口中射精/口射特写',
    'cuntbusting': '踢阴/猛撞小穴',
    'cupping balls': '托住睾丸',
    'curvy body': 'S型身材/丰满曲线身材',
    'curvy female': '丰满女性',
    'curvy figure': '身材婀娜/丰满轮廓',
    'customization': '自定义/捏人角色',
    'cut': '切削/剪辑',
    'cute': '可爱/萌',
    'cute fangs': '可爱小虎牙',
    'cutegirls': '萌妹子/可爱女孩',
    'cyan light': '青色灯光/蓝绿光',
    'cyber': '赛博/赛博朋克风格',
    'd vorah (mortal kombat)': '迪沃拉 (真人快打)',
    'daddy kink': '爸爸癖好/恋父调教',
    'daisy chain': '接龙性交/多人连锁性交',
    'daiyan (girls frontline)': '黛烟 (少女前线)',
    'dalia margolis (hitman)': '达莉亚·玛格丽斯 (杀手47)',
    'damaged clothes': '破衣/战损服装',
    'damsel': '受难少女/落难女子',
    'danah (vindictus)': '丹雅 (洛奇英雄传)',
    'danganronpa': '弹丸论破',
    'danger girl': '危险女孩',
    'dangling testicles': '垂悬的睾丸/摇晃蛋蛋',
    'dani nakamura (the callisto protocol)': '丹尼·中村 (木卫四协议)',
    'dante (dmc)': '但丁 (鬼泣)',
    'dark areola': '深色乳晕',
    'dark body': '暗黑身体/黑肤',
    'dark environment': '昏暗环境/暗室',
    'dark hair': '黑发/深色头发',
    'dark skinned female': '黑肉女性/深色肤色女性',
    'dark skinned futanari': '黑肉扶他',
    'dark skinned male': '黑肉男性/深色肤色男性',
    'death by penis': '精尽人亡/巨根致死',
    'death by snoo snoo': 'Snoo Snoo致死/强上做死',
    'death prophet': '死亡先知 (DOTA2)',
    'death trooper': '死亡死亡冲锋队 (星球大战)',
    'deep': '深层/深插',
    'deep blowjob': '深喉口交',
    'deep rimming': '深层舔肛',
    'deep sea king (one punch)': '深海王 (一拳超人)',
    'deepthroat request': '深喉要求/深喉点播',
    'deertaur': '鹿人/鹿半人马',
    'defeated': '战败/被征服',
    'deformation': '形变/肢体异化',
    'delia (vindictus)': '蒂莉亚 (洛奇英雄传)',
    'delta (the eminence in shadow)': '德尔塔/Delta (想要成为影之实力者)',
    'demon hunter sombra': '恶魔猎手黑影 (守望先锋)',
    'desdemona (fornite)': '黛斯德蒙娜 (堡垒之夜)',
    'detailed background': '精细背景',
    'devil girl': '恶魔娘/恶魔女子',
    'devil may cry': '鬼泣',
    'dexters laboratory': '德克斯特的实验室',
    'dexters mom (dexter\'s lab)': '德克斯特妈妈 (德克斯特的实验室)',
    'diablo': '暗黑破坏神',
    'diana allers (mass effect)': '戴安娜·阿勒斯 (质量效应)',
    'diana burnwood (hitman)': '戴安娜·伯恩伍德 (杀手47)',
    'diaochan (dynasty warriors)': '貂蝉 (真三国无双)',
    'dick growth': '巨根增长/阴茎变大',
    'dicks touching': '阴茎碰撞/击剑',
    'digital media (artwork)': '数字艺术/CG作品',
    'dildo in pussy': '假阳具插穴',
    'dildo machine': '自动假阳具打桩机',
    'dildo penetration': '假阳具插入',
    'dildo sitting': '坐假阳具/坐骑假阳具',
    'dipstick ears': '沾墨耳/斑点耳',
    'disgaea | makai senki disgaea': '魔界战记Disgaea',
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
    if norm in llm_dict_5:
        row[2] = llm_dict_5[norm]
        updated_count += 1

print(f"Applied LLM manual batch 5: Updated {updated_count} tags!")

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
