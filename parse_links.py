import re
html = open('check_tags.html', 'r', encoding='utf-8').read()
links = re.findall(r'href="([^"]*)"', html)
print([l for l in links if 'tags' in l][:50])
