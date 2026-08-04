import urllib.request
import re

req = urllib.request.Request('https://rule34video.com/tags/', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')

print("Pagination elements:")
for match in re.findall(r'<a[^>]*class="[^"]*page-link[^"]*"[^>]*>', html, re.I | re.S)[:10]:
    print(match.strip())
