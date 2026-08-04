import urllib.request
import re

def get_tags(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        links = re.findall(r'href="https://rule34video.com/tags/([^"/]+)/"', html)
        return list(set(links))
    except Exception as e:
        return [str(e)]

print("Base:", get_tags('https://rule34video.com/tags/')[:5])
print("?from=2:", get_tags('https://rule34video.com/tags/?from=2')[:5])
print("?from=02:", get_tags('https://rule34video.com/tags/?from=02')[:5])
print("?from_tags=2:", get_tags('https://rule34video.com/tags/?from_tags=2')[:5])
print("/2/:", get_tags('https://rule34video.com/tags/2/')[:5])
