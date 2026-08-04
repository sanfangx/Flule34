import csv
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

r34_csv = 'assets/tags/rule34video_tags_zh.csv'
with open(r34_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

untranslated = [row[1] for row in rows if row[1] == row[2]]
print(f"Exporting {len(untranslated)} untranslated tags to chunks for 100% LLM inspection...", flush=True)

chunk_size = 300
for i in range(0, len(untranslated), chunk_size):
    chunk = untranslated[i:i+chunk_size]
    with open(f'scratch/full_untranslated_{i//chunk_size + 1}.txt', 'w', encoding='utf-8') as f:
        for t in chunk:
            f.write(f"{t}\n")

print(f"Created {len(untranslated) // chunk_size + 1} chunk files in scratch/!")
