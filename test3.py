import subprocess
import re

def get_page_info(url):
    cmd = ['curl.exe', '-s', '-b', 'cookies.txt', '-I', '-L', url]
    result = subprocess.run(cmd, capture_output=True)
    headers = result.stdout.decode('utf-8', errors='ignore')
    
    cmd2 = ['curl.exe', '-s', '-b', 'cookies.txt', '-L', url]
    result2 = subprocess.run(cmd2, capture_output=True)
    html = result2.stdout.decode('utf-8', errors='ignore')
    
    title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
    page_title = title_match.group(1) if title_match else "No title"
    return headers, page_title

h1, t1 = get_page_info("https://rule34video.com/my/favourites/videos/")
h2, t2 = get_page_info("https://rule34video.com/my/favourites/videos/2/")
h3, t3 = get_page_info("https://rule34video.com/my/favourites/videos/?from_my_fav_videos=2")

print("=== PAGE 1 ===")
print("Title:", t1)
print("=== PAGE 2 (/2/) ===")
print("Title:", t2)
print("=== PAGE 3 (?from) ===")
print("Title:", t3)
