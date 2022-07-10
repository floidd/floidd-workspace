import requests
from bs4 import BeautifulSoup



URL = 'https://www.kinoafisha.info/rating/movies/?ysclid=l4gpyyqjwx845203721'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'}


def get_html_ps(url):
    response = requests.get(url, headers=HEADERS)
    return response


def get_pages_count_ps(html):
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find_all('nav', class_='ratings_pagination bricks bricks-unite swipe outer-mobile inner-mobile')
    numbs = []
    for page in pages:
        tmp_numb = page.find_all('a', class_='bricks_item')
        for i in tmp_numb:
            if i is not None:
                numb_text = i.get_text(strip=True)
                numb_link = i.get('href')
                if numb_text != 'Вперед':
                    numbs.append(numb_link)
    return numbs


def get_content_ps(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='movieItem_info')
    films = []
    for item in items:
        films.append({
            'filmName':
                item.find('a', class_='movieItem_title').get_text(strip=True),
            'link':
                item.find('a', class_='movieItem_title').get('href')
            })
    return films


def parse_ps():
    films = []
    html = get_html_ps(URL)
    urls = get_pages_count_ps(html.text)
    for url in urls:
        html = get_html_ps(url)
        print(html.status_code)
        if html.status_code == 200:
            films.extend(get_content_ps(html.text))
        else:
            print('Error')
    return films


