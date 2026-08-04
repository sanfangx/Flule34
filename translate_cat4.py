import csv
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

print("Starting Category 4 technical/language tag translation...", flush=True)

r34_csv = 'assets/tags/rule34video_tags_zh.csv'
with open(r34_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

cat4_map = {
    # Resolutions & Technical Specs
    '4k': '4K超清',
    '8k': '8K极清',
    '1080p': '1080P全高清',
    '720p': '720P高清',
    '60fps': '60帧高帧率',
    '30fps': '30帧帧率',
    '3d': '3D三维动画',
    '2d': '2D二维动画',
    '360 vr': '360度VR全景',
    'vr': 'VR虚拟现实',
    'sfm': 'SFM (Source Filmmaker动画)',
    'mmd': 'MMD (MikuMikuDance动画)',
    'blender': 'Blender3D建模渲染',
    'cgi': 'CGI计算机合成图像',

    # Languages & Subtitles
    'english': '英语',
    'english dialogue': '英文对白',
    'english subtitles': '英文字幕',
    'english voice': '英文配音',
    'japanese': '日语',
    'japanese dialogue': '日文对白',
    'japanese subtitles': '日文字幕',
    'japanese voice acting': '日文声优配音',
    'chinese': '中文',
    'chinese subtitles': '中文字幕',
    'german': '德语',
    'german subtitles': '德文字幕',
    'french': '法语/法式',
    'french accent': '法语口音',
    'french subtitles': '法文字幕',
    'italian': '意大利语',
    'italian subtitles': '意大利文字幕',
    'spanish': '西班牙语',
    'spanish subtitles': '西班牙文字幕',
    'russian': '俄语',
    'russian subtitles': '俄文字幕',
    'brazilian': '巴西/巴西风',
    'brazilian subtitles': '巴西葡萄牙语字幕',
    'british': '英国/英音',
    'american': '美国/美音',
}

fixed_count = 0
for row in rows:
    name = row[1].strip()
    norm = name.lower()

    if norm in cat4_map:
        row[2] = cat4_map[norm]
        fixed_count += 1
    elif norm.endswith(' subtitles'):
        lang = norm.replace(' subtitles', '').strip()
        if lang in cat4_map:
            row[2] = f"{cat4_map[lang]}字幕"
            fixed_count += 1
        else:
            row[2] = f"{lang}字幕"
            fixed_count += 1

print(f"Translated {fixed_count} Category 4 technical & language tags!", flush=True)

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
