import urllib.request
import re
import csv
import concurrent.futures
import threading

base_url = 'https://rule34video.com/tags/?sort_by=tag&from={}'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

all_tags = []
lock = threading.Lock()
max_pages_to_check = 1000
empty_pages_threshold = 5
consecutive_empty = 0

def fetch_page(page_num):
    url = base_url.format(page_num)
    req = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
        
        # Tags are within <a data-action="ajax" href="https://rule34video.com/tags/ID/">
        # Name and count are usually inside the link text like `name\n\n\n count`
        # We can extract all hrefs to tags and their text
        pattern = r'<a[^>]*href="https://rule34video.com/tags/(\d+)/"[^>]*>(.*?)</a>'
        matches = re.findall(pattern, html, re.DOTALL | re.IGNORECASE)
        
        tags_on_page = []
        for tag_id, content in matches:
            # Clean up content
            content_clean = re.sub(r'<[^>]+>', ' ', content) # remove inner HTML if any
            content_clean = content_clean.replace('\r', '').replace('\n', ' ')
            content_clean = re.sub(r'\s+', ' ', content_clean).strip()
            
            # Content usually has name and count. If it's a number at the end, it's count.
            # Example: "4boys 155" or just "4boys"
            match = re.match(r'^(.*?)\s+([\d,]+)$', content_clean)
            if match:
                name = match.group(1).strip()
                count = match.group(2).replace(',', '')
            else:
                name = content_clean
                count = '0'
                
            tags_on_page.append({'id': tag_id, 'name': name, 'count': count})
            
        return tags_on_page
    except Exception as e:
        print(f"Error on page {page_num}: {e}")
        return []

def main():
    print("Starting tag scraper...")
    global consecutive_empty
    
    # We will just fetch pages sequentially or in small batches because we don't know the max page
    # and we don't want to spam the server too hard.
    # Let's do batches of 10 pages concurrently.
    current_page = 1
    batch_size = 10
    total_tags_found = 0
    
    with open('rule34video_tags.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Name', 'VideoCount'])
        
        while current_page <= max_pages_to_check:
            pages = list(range(current_page, current_page + batch_size))
            print(f"Fetching pages {pages[0]} to {pages[-1]}...")
            
            batch_tags = []
            with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                results = list(executor.map(fetch_page, pages))
                
            empty_count = 0
            for tags in results:
                if not tags:
                    empty_count += 1
                else:
                    batch_tags.extend(tags)
            
            # Write batch to CSV
            for t in batch_tags:
                writer.writerow([t['id'], t['name'], t['count']])
            
            total_tags_found += len(batch_tags)
            print(f"  Found {len(batch_tags)} tags in this batch. Total: {total_tags_found}")
            
            if empty_count == batch_size:
                consecutive_empty += 1
            else:
                consecutive_empty = 0
                
            if consecutive_empty >= 2:
                print("No tags found for multiple consecutive batches. Assuming end of pagination.")
                break
                
            current_page += batch_size

    print(f"Done! Scraped {total_tags_found} tags total.")

if __name__ == '__main__':
    main()
