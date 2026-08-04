from bs4 import BeautifulSoup

with open('favorites.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

pagination = soup.select('.pagination, .page_selector, .paging')
if pagination:
    for p in pagination:
        print(p.prettify())
else:
    print("No pagination found. Looking for links with page or from:")
    for a in soup.find_all('a', href=True):
        if 'page' in a['href'] or 'from' in a['href'] or 'favourites' in a['href'] or 'bookmarks' in a['href']:
            print(a['href'])
