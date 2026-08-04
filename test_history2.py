import subprocess
import re
from bs4 import BeautifulSoup

cmd = ['curl.exe', '-s', '-b', 'cookies.txt', 'https://rule34video.com/my/history/']
result = subprocess.run(cmd, capture_output=True)
html = result.stdout.decode('utf-8', errors='ignore')

soup = BeautifulSoup(html, 'html.parser')
for a in soup.find_all('a', href=True):
    if 'history' in a['href'] or 'page' in a['href'] or 'from' in a.get('data-parameters', ''):
        print("Href:", a['href'], "Params:", a.get('data-parameters', ''))
