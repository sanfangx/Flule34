import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read untranslated or machine-translated tags that need LLM translation
with open('assets/tags/rule34video_tags_zh.csv', 'r', encoding='utf-8') as f:
    rows = list(csv.reader(f))[1:]

print(f"Total tags in dataset: {len(rows)}")
