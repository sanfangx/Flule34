import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')
conn = sqlite3.connect(r'C:\Users\沙银\.gemini\antigravity\scratch\ffdkj_tags\ffdkj-Danbooru_Tag-Chinese-English-Translation-Table-main\tag.sqlite')
cursor = conn.cursor()
cursor.execute("SELECT name, cn_name FROM tags WHERE name LIKE '%adagio%'")
rows = cursor.fetchall()
print("Found in Danbooru:", rows)
