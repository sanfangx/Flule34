import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

llm_dict_8 = {
    # Actions & Terms
    'hana song': '宋哈娜/D.Va (守望先锋)',
    'mario bros': '马里奥兄弟',
    'triple blowjob': '三重口交/三人同时口交',
    'gaping pussy': '穴口扩张/小开大口',
    'gaping urethra': '尿道扩张',
    'gasping': '喘息/倒吸凉气',
    'gay': '男同性恋/GAY',
    'gay domination': '男同主导/男同调教',
    'gender bender': 'TS/性转变身',
    'genital fluids': '生殖体液/爱液喷溅',
    'genitals': '生殖器/下体',
    'german subtitles': '德文字幕',
    'gigantic balls': '巨型睾丸/巨蛋',
    'ginger': '红发妹/金红发',
    'girlfriend': '女友/女朋友',
    'giver pov': '进攻方视角/主导视角',
    'glasses askew': '眼镜歪斜',
    'glistening': '闪烁湿润/爱液光泽',
    'glistening body': '湿漉漉的身体/泛着汗水',
    'gloryhole': '荣耀之洞/墙洞口交',
    'glowing cum': '发光精液/荧光精液',
    'gnomes': '侏儒/地精',
    'goblin female': '女哥布林/哥布林娘',
    'goblins': '哥布林/地魔',
    'goddess': '女神',
    'gold eyes': '金瞳/金黄眼睛',
    'gold toenails': '金色脚趾甲',
    'golden darkness': '金色暗影 (出包王女)',
    'goo girl': '胶水娘/史莱姆娘',
    'good girl': '好女孩/乖孩子',
    'goth': '哥特风/暗黑哥特妹',
    'gotoubun no hanayome | the quintessential quintuplets': '五等分的新娘',
    'grab arms': '抓紧双臂',
    'grabbing balls': '抓握睾丸',
    'grabbing hair': '抓拽头发',
    'grabbing legs': '抓住双腿',
    'granddaughter': '孙女',
    'grandfather': '爷爷/外公',
    'grandmother': '奶奶/外婆',
    'granny': '老奶奶/老妇',
    'gray eyes': '灰瞳/灰色眼睛',
    'green balls': '绿色睾丸',
    'green body': '绿色身体',
    'green lipstick': '绿唇膏',
    'green shadow (plants vs zombies)': '绿影 (植物大战僵尸)',
    'green topwear': '绿色上衣',
    'grey body': '灰色身体',
    'grip': '紧握/抓紧',
    'gritted teeth': '咬紧牙关/忍痛',
    'group': '群交/多人性交',
    'growth': '身体变大/巨大化',
    'grunting': '闷哼/呻吟声',
    'gulp': '咕噜吞下/吞精',
    'guy': '男子/小伙',
    'gym clothes': '体操服/运动服',
    'gymshorts': '运动短裤',
    'gynomorph on bottom': '扶他在下',
    'gynomorph on female': '扶他上女性',
    'gynomorph on top': '扶在上位',
    'gynomorph penetrated': '扶他被插入',
    'gynomorph penetrating female': '扶他插入女性',
    'hades': '哈迪斯',
    'hair': '头发',
    'hair accessory': '发饰/发卡',
    'hair buns': '丸子头/包子头',
    'hair grab': '抓头发',
    'hair pull': '拉扯头发',
    'hair pulling': '拽发调教',
    'hairless pussy': '无毛白虎穴/无毛小穴',
    'hairy armpits': '腋毛/有毛腋下',
    'hairy pussy': '多毛小穴/黑森林',
    'half elf': '半精灵',
    'half naked': '半裸/衣衫不整',
    'half-dressed': '半着装',
    'half-elf': '半精灵族',
    'halo reach': '光环:致远星',
    'hand holding': '牵手/十指相扣',
    'hand on butt': '按住屁股/摸臀',
    'hand on chest': '手抚胸口',
    'hand on chin': '托住下巴',
    'hand on leg': '手摸大腿',
    'hand on mouth': '捂住嘴巴',
    'hand on neck': '掐住脖子/抚摸颈部',

    # Characters & Series
    'gary godspeed (final space)': '加里·高斯比德 (太空终界)',
    'gatomon': '迪路兽 (数码宝贝)',
    'gemma (monster hunter)': '洁玛 (怪物猎人)',
    'geras (mortal kombat)': '杰拉斯 (真人快打)',
    'goba': '高斯/哥巴',
    'gohan (dbz)': '孙悟饭 (龙珠Z)',
    'gojo (dress up darling)': '五条新菜 (恋上换装娃娃)',
    'goku (dbz)': '孙悟空 (龙珠Z)',
    'gondar the bounty hunter (dota)': '赏金猎人刚铎 (DOTA2)',
    'goro (mortal kombat)': '戈洛 (真人快打)',
    'goro akechi': '明智吾郎 (女神异闻录5)',
    'gorou (genhin impact)': '五郎 (原神)',
    'gwen (total drama island)': '格温 (孤岛生存大乱斗)',
    'gwynevere princess of sunlight (dark souls)': '阳光公主葛温艾维亚 (黑暗之魂)',
    'hamakaze (kantai)': '滨风 (舰队Collection)',
    'hana uzaki': '宇崎花 (宇崎学妹想要玩！)',
    'hanabi hyuga': '日向花火 (火影忍者)',
    'hanamaru kunikida (love live)': '国木田花丸 (LoveLive!)',
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
    if norm in llm_dict_8:
        row[2] = llm_dict_8[norm]
        updated_count += 1

print(f"Applied LLM manual batch 8: Updated {updated_count} tags!")

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
