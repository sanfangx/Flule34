import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

llm_dict_12 = {
    # Terms & Actions
    'male': '男性',
    'male domination': '男性主导/男尊/Maledom',
    'male draenei': '德莱尼男性 (魔兽世界)',
    'male human/female anthro': '人类男性对兽人女性',
    'male human/female demon': '人类男性对女魔族',
    'male human/female feral': '人类男性对野生女兽',
    'male human/female humanoid': '人类男性对类人女性',
    'male milking': '榨精/榨干男性',
    'male moaning': '男性呻吟',
    'male molestation victim': '被受害/被性骚扰男性',
    'male on anthro': '男性对兽人',
    'male on bottom': '男下位',
    'male on female': '男对女/异性交配',
    'male on feral': '男性对野兽',
    'male on futanari': '男性对扶他',
    'male on male': '男对男/男同性交',
    'male on top': '男上位',
    'male only': '全男性/纯男',
    'male penetrating': '男性插入',
    'male penetrating female': '男性插入女性',
    'male penetrating male': '男性插入男性',
    'male pov': '男性第一视角/POV',
    'male/male': '男男/GAY',
    'males only': '全男性',
    'malesub': '受虐男/M男',
    'manga': '漫画/日漫',
    'manual': '手动/手控',
    'married couple': '夫妻/已婚夫妇',
    'masked face': '戴面具的脸庞/遮面',
    'mass effect': '质量效应',
    'master roshi': '龟仙人 (龙珠)',
    'masturbating during fellatio': '口交同时自慰',
    'mating': '交配/繁衍',
    'mature anthro': '成熟兽人',
    'mechanical arm': '机械手臂/义肢',
    'mechanical fixation': '机械束缚/固定',
    'medic': '战地医生/医疗兵',
    'medusa': '美杜莎 (蛇发女妖)',
    'metal gear rising': '合金装备崛起:复仇',
    'metal gear solid v': '合金装备5:幻痛',
    'metro: exodus': '地铁:离去',
    'mexican': '墨西哥人/墨西哥风格',
    'micro penis': '微型阴茎/小阴茎',
    'midget': '矮人/侏儒妹',
    'midnight': '午夜/深夜环境',
    'milking': '榨乳/挤奶/榨精',
    'mind flayer (baldurs gate)': '夺心魔 (博德之门3)',
    'mindbreak': '阿黑颜/精神崩溃',
    'mindshift': '心智转变/催眠洗脑',

    # Characters & Series
    'mahiru shiina (otonari no tenshi-sama)': '椎名真昼 (关于我在无意间被隔壁的天使变成废柴这档事)',
    'mai sakurajima': '樱岛麻衣 (青春猪头少年不会梦到兔女郎学姐)',
    'mai valentine (yu-go-oh!)': '孔雀舞 (游戏王)',
    'maid marian (robin hood)': '玛丽安女仆 (罗宾汉)',
    'maki gamou (nagatoro)': '蒲生麻姬 (不要欺负我，长瀞同学)',
    'maki nishikino (love live)': '西木野真姬 (LoveLive!)',
    'mako mankanshoku': '满舰饰真子 (斩服少女)',
    'makoto kino': '木野真琴/水手木星 (美少女战士)',
    'mamako oosuki (do you love your mom)': '大好真真子 (普通攻击是全体二连击，这样的妈妈你喜欢吗？)',
    'mami nanami (kanojo)': '七海麻美 (租借女友)',
    'marian (nikke goddess of victory)': '玛丽安 (胜利女神：妮姬)',
    'marin kitagawa (dress up darling)': '喜多川海梦 (恋上换装娃娃)',
    'maron (dbz)': '玛伦 (龙珠Z)',
    'mary (nikke goddess of victory)': '玛丽 (胜利女神：妮姬)',
    'mashu kyrielight (fate grand order)': '玛修·基列莱特 (Fate/Grand Order)',
    'megara (hercules)': '蜜格拉 (大力士/赫拉克勒斯)',
    'meiko shiraki': '白木芽衣子 (监狱学园)',
    'melia (xenoblade)': '梅莉亚 (异度神剑)',
    'mifuyu (princess connect)': '拜岛美冬 (公主连结)',
    'mika jougasaki (project-imas)': '城崎美嘉 (偶像大师)',
    'mikan tsumiki (danganronpa)': '罪木蜜柑 (弹丸论破)',
    'miko iino (kaguya-sama wa kokurasetai wikia)': '伊井野伊子 (辉夜大小姐想让我告白)',
    'mikoto aketa (shiny colors)': '绯田美琴 (偶像大师)',
    'miku maekawa (the idolmaster)': '前川未来 (偶像大师)',
    'miku nakano (5toubun no hanayome)': '中野三玖 (五等分的新娘)',
    'min min (smash)': '面面 (任天堂明星大乱斗)',
    'minami nitta (the idolmaster)': '新田美波 (偶像大师)',
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
    if norm in llm_dict_12:
        row[2] = llm_dict_12[norm]
        updated_count += 1

print(f"Applied LLM manual batch 12: Updated {updated_count} tags!")

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
