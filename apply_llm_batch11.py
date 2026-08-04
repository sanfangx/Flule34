import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

llm_dict_11 = {
    # Terms & Actions
    'kunoichi': '女忍者/女忍',
    'labia': '阴唇',
    'labia majora': '大阴唇',
    'lace-trimmed legwear': '蕾丝边袜/蕾丝腿饰',
    'lactation without expressing': '自然喷奶/未挤压出奶',
    'lady': '女士/贵妇',
    'lady bug': '瓢虫/瓢虫少女',
    'large butt': '大臀/大屁股',
    'large filesize': '大文件体积',
    'large tattoo': '大面积纹身',
    'larger dom': '强壮主导者',
    'larger feral': '大型野兽',
    'larger futanari': '高大扶他',
    'larger male': '高大魁梧男性',
    'larger penetrated': '大型受方/高大被插入者',
    'latin': '拉丁风格',
    'latina': '拉丁裔女子',
    'latino': '拉丁裔男子',
    'laugh': '大笑/笑颜',
    'laying back': '仰卧/躺平',
    'leaking cum': '流精/精液外溢',
    'leaves': '树叶/叶子遮挡',
    'leg on table': '腿抬在桌上',
    'leg over head': '单腿抬过头顶',
    'leg over partner\'s shoulder': '单腿挂在同伴肩上',
    'leg over shoulder': '腿挂肩上/扛腿姿势',
    'leg slider position': '滑腿姿势',
    'legendary pokémon': '传说宝可梦/神兽',
    'legs around waist': '双腿夹腰',
    'legs crossed': '二郎腿/双腿交叉',
    'legs held open': '扳开双腿/保持张腿',
    'legwear': '腿饰/袜类',
    'lesbian': '女同性恋/百合',
    'letterbox': '宽银幕黑边/遮幅',
    'lewd': '淫乱/下流',
    'lezdom': '女同主导/百合女王',
    'licking glass': '舔玻璃',
    'licking neck': '舔舐脖子',
    'licking soles': '舔脚心/舔脚底',
    'licking underwear': '舔内裤/品尝内裤',
    'life drain': '吸取生命/精气吸食',
    'lifeline': '生命线 (Apex英雄)',
    'light body': '娇小身材/轻巧体型',
    'light brown hair': '浅棕发',
    'light skin': '白皙肤色/白肉',
    'light skinned female': '白肤女性',
    'light skinned futanari': '白肤扶他',
    'light skinned male': '白肤男性',
    'light-skinned female': '白肤女性',
    'light-skinned male': '白肤男性',
    'lights off': '关灯/暗室环境',
    'lillie': '莉莉艾 (宝可梦)',
    'limp dick after sex': '事后软精/贤者状态阴茎',
    'lip biting': '咬嘴唇',
    'lipstick on balls': '蛋蛋上的唇印',
    'lipstick on penis': '阴茎上的唇印',
    'lipstick smear': '唇膏蹭乱/抹开口红',
    'little mermaid': '小美人鱼',
    'little red riding hood': '小红帽',
    'living sex toy': '活人肉便器/肉玩具',
    'lizard girl': '蜥蜴娘',
    'lizard guy': '蜥蜴人',
    'long ass': '修长翘臀',
    'long breasts': '下垂大乳/长乳',
    'long cock': '长巨根',
    'long ears': '长耳朵',
    'long movie': '长视频/长片',
    'long nails': '长指甲',
    'long playtime': '长时间交配',
    'long socks': '长筒袜',
    'long video': '长视频',
    'looking at partner': '凝视同伴',

    # Characters & Series
    'krillin': '克林 (龙珠Z)',
    'kristoff bjorgman': '克斯托夫 (冰雪奇缘)',
    'kurodate haruna (blue arvhive)': '黑馆羽留奈 (蔚蓝档案)',
    'kurumu kurono (rosario)': '黑乃胡梦 (十字架与吸血鬼)',
    'kyaru back (princess connect)': '凯露后背 (公主连结)',
    'kyoko kirigiri (danganronpa)': '雾切响子 (弹丸论破)',
    'kyouka kudou (my happy marriage)': '久堂清霞 (我的幸福婚约)',
    'launch (dbz)': '兰琪 (龙珠Z)',
    'layla (mobile legends bang bang)': '蕾拉 (无尽对决)',
    'leon scott kennedy': '里昂·S·肯尼迪 (生化危机)',
    'li mei (mortal kombat)': '李梅 (真人快打)',
    'li shang (mulan)': '李翔 (木兰)',
    'lily (spy classroom)': '百合 (间谍教室)',
    'lina': '莉娜 (DOTA2)',
    'lindsay (total drama island)': '林赛 (孤岛生存大乱斗)',
    'lissandra': '丽桑卓 (英雄联盟)',
    'lolita (mobile legends bang bang)': '萝莉塔 (无尽对决)',
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
    if norm in llm_dict_11:
        row[2] = llm_dict_11[norm]
        updated_count += 1

print(f"Applied LLM manual batch 11: Updated {updated_count} tags!")

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
