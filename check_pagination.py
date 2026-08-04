import re
html = open('check_tags.html', 'r', encoding='utf-8').read()
pages = re.findall(r'data-parameters="([^"]*)"', html)
print(set(pages))
