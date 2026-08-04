import subprocess
def get_page_info(url):
    cmd = ['curl.exe', '-s', '-b', 'cookies.txt', '-I', '-L', url]
    result = subprocess.run(cmd, capture_output=True)
    return result.stdout.decode('utf-8', errors='ignore')

h1 = get_page_info("https://rule34video.com/my/history/")
h2 = get_page_info("https://rule34video.com/my/history/2/")

print("=== PAGE 1 ===")
print(h1.split('\r\n')[0])
print("=== PAGE 2 ===")
print(h2.split('\r\n')[0])
