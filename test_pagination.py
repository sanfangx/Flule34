import subprocess
import re

def fetch_titles(url):
    cmd = ['curl.exe', '-s', '-b', 'cookies.txt', url]
    result = subprocess.run(cmd, capture_output=True)
    html = result.stdout.decode('utf-8', errors='ignore')
    titles = set(re.findall(r'title="([^"]+)"', html))
    return titles

page1 = fetch_titles("https://rule34video.com/my/favourites/videos/")
page2_url1 = "https://rule34video.com/my/favourites/videos/?from_my_fav_videos=2"
page2_url2 = "https://rule34video.com/?mode=async&function=get_block&block_id=list_videos_my_favourite_videos&fav_type=0&playlist_id=0&sort_by=&from_my_fav_videos=2"
page2_url3 = "https://rule34video.com/my/favourites/videos/2/"

p2_titles1 = fetch_titles(page2_url1)
p2_titles2 = fetch_titles(page2_url2)
p2_titles3 = fetch_titles(page2_url3)

print(f"Page 1 titles count: {len(page1)}")
print(f"URL1 (?from_my_fav_videos=2) diff: {len(p2_titles1 - page1)} new titles")
print(f"URL2 (AJAX) diff: {len(p2_titles2 - page1)} new titles")
print(f"URL3 (/2/) diff: {len(p2_titles3 - page1)} new titles")
