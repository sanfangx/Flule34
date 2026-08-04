import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

llm_dict_9 = {
    # Actions & NSFW Terms
    'helpless': '无助/任人宰割',
    'hentai': 'Hentai/变态色情动画',
    'hercules': '大力神赫拉克勒斯',
    'hero': '英雄/主角',
    'heterosexual': '异性恋/BG',
    'hidden sex': '隐蔽性交/偷偷做爱',
    'high heel': '高跟鞋',
    'high resolution': '超高清/高分辨率',
    'highmountain tauren': '至高岭牛头人 (魔兽世界)',
    'hip grab': '抓住胯部/抓臀',
    'hispanic': '拉丁裔/西班牙裔',
    'hitman': '杀手47 (Hitman)',
    'holding arm': '挽住手臂',
    'holding arms': '抓握双臂',
    'holding breast': '抓揉乳房',
    'holding face': '捧着脸庞',
    'holding hair': '抓拽头发',
    'holding head': '按住头部',
    'holding hips': '按住胯部/抓臀',
    'holding object': '手持物品',
    'holding penis': '握住阴茎/手交',
    'holding thigh': '按住大腿',
    'holidays': '节日/假期风',
    'horde': '部落 (魔兽世界)',
    'horde domination': '部落主导',
    'horny': '发情/发春/渴求快感',
    'horny female': '发情女性/欲望妹子',
    'horror': '恐怖/惊悚风格',
    'horse sex': '马交/兽交',
    'horsecock dildo': '马交巨根假阳具',
    'hot dogging': '夹腿/腿缝摩擦',
    'hotpants': '热裤/超短裤',
    'hotwife': '人妻出轨/绿帽娇妻',
    'hourglass figure': '沙漏型身材/完美S曲线',
    'huge': '巨大/超大号',
    'huge areolae': '巨大乳晕',
    'huge balls': '巨型睾丸/巨蛋',
    'huge belly': '大肚子/隆起腹部',
    'huge cumshot': '海量射精/巨量喷精',
    'huge filesize': '超大文件体积',
    'huge insertion': '巨大物品/巨物插入',
    'huge load': '巨量浓精',
    'huge monster': '巨型怪物',
    'hugging': '拥抱/抱紧',
    'human': '人类',
    'human on alien': '人类对外星人',
    'human on anthro': '人类对兽人',
    'human on feral': '人类对野兽',
    'human on furry': '人类对福瑞/毛茸茸',
    'human on humanoid': '人类对类人生物',
    'human on machine': '人类对机械',
    'human on robot': '人类对机器人',
    'human penetrating': '人类插入',
    'human pet': '人类宠物/人宠调教',
    'human pov': '人类第一视角',
    'humanized': '拟人化/娘化',
    'humanoid': '类人生物/人形',
    'humanoid genitalia': '类人生殖器',
    'humanoid penis': '类人阴茎',
    'humilation': '羞辱/耻辱调教',
    'humor': '搞笑/幽默风',
    'hunter': '猎人',
    'hyper': '超巨大/Hyper特化',
    'hyper ass': 'Hyper巨臀',
    'hyper balls': 'Hyper巨蛋/超大睾丸',
    'hyper hips': 'Hyper夸张宽胯',
    'hyper inflation': 'Hyper膨胀',
    'hyper penis': 'Hyper巨根',
    'hyper testicles': 'Hyper超大睾丸',
    'hyperdimension neptunia | choujigen game neptune': '超次元游戏:海王星',
    'ignoring': '视而不见/冷落无视',

    # Characters & Series
    'hestia': '赫斯缇雅 (在地下城寻求遭遇是否搞错了什么)',
    'hifumi takimoto': '泷本日富美 (NEW GAME!)',
    'hifumi yamada (danganronpa)': '山田一二三 (弹丸论破)',
    'hikari (xenoblade)': '光 (异度神剑2)',
    'himawari uzumaki': '漩涡向日葵 (博人传)',
    'himiko agari (komi-san)': '上理卑弥呼 (古见同学有交流障碍症)',
    'himmel (frieren beyond journeys end)': '辛美尔 (葬送的芙莉莲)',
    'hina hikawa (bang dream)': '冰川日菜 (BanG Dream!)',
    'hina ichikawa (the idolmaster)': '市川雏菜 (偶像大师)',
    'hitori gotoh (bocchi the rock)': '后藤一里/波奇酱 (孤独摇滚!)',
    'hiyoko saionji (danganronpa)': '西园寺日寄子 (弹丸论破)',
    'hizuru minakata (summer time rendering)': '南方日鹤 (夏日重现)',
    'hk416 (girls frontline)': 'HK416 (少女前线)',
    'holly forrester (back 4 blood)': '霍莉·福雷斯特 (喋血复仇)',
    'honami ichinose (classroom of the elite)': '一之濑帆波 (欢迎来到实力至上主义的教室)',
    'hoodwink (dota2)': '森海飞霞 (DOTA2)',
    'hsien ko (dark stalkers)': '泪泪/泪泪僵尸 (恶魔战士)',
    'ibuki mioda (danganronpa)': '澪田唯吹 (弹丸论破)',
    'ichika nakano (5Toubun no Hanayome)': '中野一花 (五等分的新娘)',
    'ikkitousen | battle vixens': '一骑当千',
    'ikuyo kita (bocchi the rock)': '喜多郁代 (孤独摇滚!)',
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
    if norm in llm_dict_9:
        row[2] = llm_dict_9[norm]
        updated_count += 1

print(f"Applied LLM manual batch 9: Updated {updated_count} tags!")

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
