import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read current CSV
with open('assets/tags/rule34video_tags_zh.csv', 'r', encoding='utf-8') as f:
    rows = list(csv.reader(f))[1:]

untranslated = [r[1] for r in rows if r[1] == r[2]]
print(f"Total untranslated tags: {len(untranslated)}")

# Write untranslated tags to text files in batches of 200 for processing
batch_size = 200
for i in range(0, len(untranslated), batch_size):
    batch = untranslated[i:i+batch_size]
    with open(f'scratch/batch_{i//batch_size + 1}.txt', 'w', encoding='utf-8') as f:
        for item in batch:
            f.write(f"{item}\n")

print(f"Created {len(untranslated) // batch_size + 1} batch files in scratch/!")
