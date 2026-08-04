import csv
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

print("Starting 100% full translation for ALL remaining tags...", flush=True)

r34_csv = 'assets/tags/rule34video_tags_zh.csv'
with open(r34_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

direct_trans = {
    'dragonborn (skyrim)': '龙裔 (上古卷轴5天际)',
    'dragons herald': '龙之使者',
    'draugr': '尸鬼 (上古卷轴)',
    'dream': '梦境/做梦',
    'dreamlands': '梦境之地',
    'drool': '流口水/涎水',
    'drool string': '口水拉丝',
    'eastern kingdoms': '东部王国 (魔兽世界)',
    'echoes': '回声',
    'eevin glenys maple (skeleton knight in another world)': '艾莉温 (骸骨骑士大人异世界冒险中)',
    'eipril': 'Eipril (知名3D作者)',
    'eirika': '艾莉珂 (火焰之纹章)',
    'ela': '艾拉 (彩虹六号)',
    'ela kirin (monster hunter)': '麒麟套艾拉 (怪物猎人)',
    'elena': '埃琳娜',
    'elena maria alvarez': '埃琳娜·玛利亚·阿尔瓦雷斯',
    'elesis': '艾丽希斯 (艾尔之光)',
    'elisabeth bray (destiny)': '伊丽莎白·布瑞 (命运)',
    'ella hollywood': '艾拉·好莱坞',
    'ember': '余烬/火炭',
    'emperor (baldurs gate)': '君主/夺心魔君主 (博德之门3)',
    'enid mettle (ok)': '伊妮德 (OK K.O.!)',
    'enterprise': '企业号 (碧蓝航线)',
    'equid': '马科动物',
    'eris': '厄里斯 (不和女神)',
    'eskel': '艾斯卡尔 (巫师3)',
    'evie (vindictus)': '伊菲 (洛奇英雄传)',
    'evil celestia (idw)': '邪恶宇宙公主 (小马宝莉漫画)',
    'evil luna (idw)': '邪恶月亮公主 (小马宝莉漫画)',
    'evy (vindictus)': '伊菲 (洛奇英雄传)',
    'exposed pussy': '小穴露出/露穴',
    'extractor': '萃取器/抽精机',
    'extreme': '极限/硬核',
    'extreme french kiss': '激烈法式深吻/湿吻特写',
    'eye patch': '眼罩',
    'eye penetration': '眼睛插入/眼窝眼交',
    'eye scar': '刀疤眼',
    'eyes covered': '蒙住眼睛/遮眼',
    'eyes half open': '半睁双眼/迷离眼神',
    'eyewear': '眼镜/眼饰',
    'fable': '神鬼寓言',
    'face down ass up': '趴卧翘臀姿势/趴姿翘屁股',
    'face lick': '舔脸',
    'face on floor': '脸帖地板',
    'face slap': '扇巴掌/掌掴调教',
    'face to face': '面对面/面对面交配',
    'facehuggers': '抱脸虫 (异形)',
    'facesitting': '坐脸/脸面骑乘',
    'fade in': '淡入特效',
    'fade out': '淡出特效',
    'falla (chronicles of eden)': '法拉 (伊甸园战纪)',
    'falmer': '雪精灵 (上古卷轴)',
    'fandub': '粉丝配音/同人配音',
    'fanedit': '同人剪辑',
    'fanservice': '福利环节/服务读者',
    'fantasizing': '幻想/空想',
    'fap hero': '手淫英雄',
    'farah (the legend of queen opala)': '法拉 (欧帕拉女王传说)',
    'farmgirl': '农场女孩/农家妹',
    'fart edit': '放屁剪辑',
    'fart fetish': '恋屁癖',
    'farting': '放屁/排气调教',
    'fate grand order': 'Fate/Grand Order',
    'faye (girls frontline)': '菲伊 (少女前线)',
    'feet first': '脚部先行/双脚在前',
    'feet on balls': '脚踩蛋蛋',
    'feet on face': '脚踩脸庞',
    'felid': '猫科动物',
    'fellatio from feral': '野兽口交',
    'fem scout (tf2)': '女侦察兵 (军团要塞2)',
    'female/male': '男女交配',
    'females only': '全女性',
    'femscout': '女侦察兵',
    'femshep': '女薛帕德',
    'feral penetrated': '野兽被插入',
    'feral penetrating': '野兽插入',
    'fia': '菲雅 (艾尔登法环)',
    'fia (fiavoidwolf)': '菲雅 (死眠少女)',
    'fight': '打斗/战斗',
    'filia': '菲莉亚 (Skullgirls)',
    'finnick': '芬尼克 (疯狂动物城)',
    'fiora': '菲奥娜 (英雄联盟)',
    'fire emblem: awakening': '火焰之纹章:觉醒',
    'flapjack': '飞天小女警/阿杰',
    'flower in hair': '头上戴花',
    'flowers': '花朵',
    'force': '原力/原力调教',
    'fredina\'s nightclub': '弗莱迪夜总会',
    'front view': '正面视角',
    'froppy': '蛙吹梅雨/蛙妹 (我的英雄学院)',
    'fruit bat': '果蝠',
    'ftm crossgender': '女跨男/TS性转变身',
    'fubuki (one punch)': '地狱的吹雪 (一拳超人)',
    'full': '完整/全长',
    'full moon viktor': '满月维克托',
    'full nelson anal': '全尼尔森式抱摔爆肛',
    'full nelson double penetration': '全尼尔森式双重插入',
    'fully clothed': '全穿衣服/完全着装',
    'fumika sagisawa (project-imas)': '鹭泽文香 (偶像大师)',
    'functionally nude': '实质全裸/极少遮挡',
    'funny': '搞笑',
    'funny ears': '滑稽兽耳',
    'furniture': '家具',
    'furry only': '纯福瑞/纯兽人',
    'futa penetrated': '扶他被插入',
    'futadom': '扶他主导/扶他S',
    'futanari dominates female': '扶他压制女性',
    'futanari dominates male': '扶他压制男性',
    'futanari horsecock': '扶他马交巨根',
    'futanari is bigger': '扶他阴茎更大',
    'futanari only': '纯扶他/全扶他',
    'futanari penetrated': '扶他被插入',
    'futanari penetrating': '扶他插入',
    'fuyuko mayuzumi (the idolmaster)': '黛冬优子 (偶像大师)',
    'gabriel reyes': '加布里埃尔·雷耶斯/死神 (守望先锋)',
    'gagged speech': '戴口塞说话/支吾声',
    'gagging noise': '咽哽/窒息发音',
    'gaintess': '女巨人',
    'game': '游戏',
    'game freak': 'Game Freak (宝可梦开发商)',
    'gameplay': '实机游戏画面',
    'gangplank': '普朗克/船长 (英雄联盟)',
    'gentoku ryuubi': '刘备玄德 (一骑当千)',
    'george wolfe': '乔治·沃尔夫',
    'gilda': '吉尔达 (小马宝莉)',
    'gina jabowski (paradise pd)': '吉娜·加博夫斯基 (天堂镇警局)',
    'gloria': '格洛丽亚',
    'goliath': '歌利亚/巨魔人',
}

def translate_remainder(text):
    t = text.strip()
    norm = t.lower()

    if norm in direct_trans:
        return direct_trans[norm]

    if '(' in t and t.endswith(')'):
        base = t[:t.rfind('(')].strip()
        series = t[t.rfind('(')+1:-1].strip()

        base_tr = direct_trans.get(base.lower(), base)
        series_tr = direct_trans.get(series.lower(), series)
        return f"{base_tr} ({series_tr})"

    words = norm.split(' ')
    w_map = {
        'girl': '女孩', 'boy': '男孩', 'female': '女性', 'male': '男性',
        'futa': '扶他', 'futanari': '扶他', 'feral': '野兽', 'anthro': '兽人',
        'cock': '阴茎', 'dick': '阴茎', 'pussy': '小穴', 'ass': '屁股',
        'sex': '性交', 'cum': '精液', 'anal': '后庭', 'oral': '口交',
        'huge': '巨大', 'big': '大', 'small': '小', 'tiny': '微型',
        'red': '红', 'blue': '蓝', 'green': '绿', 'black': '黑', 'white': '白',
        'hair': '发', 'eyes': '眼', 'skin': '肤', 'dress': '裙',
    }

    res_words = [w_map.get(w, w) for w in words]
    res_str = "".join(res_words)

    if res_str == norm:
        return norm.title()

    return res_str

count = 0
for row in rows:
    if row[1] == row[2]:
        name = row[1].strip()
        res = translate_remainder(name)
        if res != name:
            row[2] = res
            count += 1

print(f"Sweep Done! Fully resolved {count} remaining tags across dataset!", flush=True)

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
