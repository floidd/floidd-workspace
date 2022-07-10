import requests
from bs4 import BeautifulSoup


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'}


def get_html(url):
    response = requests.get(url, headers=HEADERS)
    return response


def get_content(html, url):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='site_content')
    film = {}
    actors = []
    genres = []
    for item in items:
        tmp_actors = item.find_all('span', class_='badgeList_name')
        tmp_genre = item.find_all('a', class_='filmInfo_genreItem button-main')
        for i in tmp_actors:
            if i is not None:
                actor = i.get_text(strip=True)
                actors.append(actor)
        for i in tmp_genre:
            if i is not None:
                genre = i.get_text(strip=True)
                genres.append(genre)
        film = {
            'filmName':
                item.find('h1', class_='trailer_title').get_text(strip=True),
            'review':
                item.find('div', class_='tabs_contentItem js-active').get_text(strip=True),
            'genres':
                genres,
            'actors':
                actors,
            'duration':
                item.find('span', class_='filmInfo_infoData').get_text(strip=True),
            'link':
                url
            }
    return film


def parse(url):
    film = {}
    html = get_html(url)
    print(html.status_code)
    if html.status_code == 200:
        film = get_content(html.text, url)
    else:
        print('Error')
    return film
