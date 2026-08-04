import subprocess
import re

def fetch_titles(url):
    cmd = ['curl.exe', '-s', '-b', 'cookies.txt', url]
    result = subprocess.run(cmd, capture_output=True)
    html = result.stdout.decode('utf-8', errors='ignore')
    titles = []
    # Match the thumbnail title
    for match in re.finditer(r'<a[^>]+href="https://rule34video.com/videos/\d+/[^>]+title="([^"]+)"', html):
        titles.append(match.group(1))
    return titles

page1 = fetch_titles("https://rule34video.com/my/favourites/videos/")
page2 = fetch_titles("https://rule34video.com/my/favourites/videos/2/")

print("Page 1:")
for t in page1[:3]: print(t)
print("\nPage 2 (/2/):")
for t in page2[:3]: print(t)

print(f"\nPage 1 count: {len(page1)}")
print(f"Page 2 count: {len(page2)}")
