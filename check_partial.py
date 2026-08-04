import csv
import re

out_csv = 'rule34video_tags_zh.csv'

with open(out_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

untranslated_base = []
untranslated_series = []
untranslated_both = []

for row in rows:
    tag_id, name, cn_name, count = row[0], row[1], row[2], row[3]
    
    # Check if original name has parenthetical: "name (series)"
    if '(' in name and name.endswith(')'):
        # Check if Chinese translation still has English in the base part before '('
        if '(' in cn_name and cn_name.endswith(')'):
            base_cn = cn_name[:cn_name.rfind('(')].strip()
            series_cn = cn_cn = cn_name[cn_name.rfind('(')+1:-1].strip()
            
            # Check if base contains English letters (e.g., Aemeath)
            has_eng_base = bool(re.search(r'[a-zA-Z]{2,}', base_cn))
            has_eng_series = bool(re.search(r'[a-zA-Z]{2,}', series_cn))
            
            if has_eng_base and not has_eng_series:
                untranslated_base.append((name, cn_name))
            elif has_eng_series and not has_eng_base:
                untranslated_series.append((name, cn_name))
            elif has_eng_base and has_eng_series:
                untranslated_both.append((name, cn_name))

print(f"Total parenthetical tags checked.")
print(f"1. Base is still English (Series is Chinese): {len(untranslated_base)}")
print(f"   Sample: {untranslated_base[:15]}")
print(f"\n2. Series is still English (Base is Chinese): {len(untranslated_series)}")
print(f"   Sample: {untranslated_series[:15]}")
print(f"\n3. Both Base and Series still English: {len(untranslated_both)}")
print(f"   Sample: {untranslated_both[:15]}")
