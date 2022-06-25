import time
import requests
from bs4 import BeautifulSoup
import csv


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'}


def get_filmname(number):
    with open("Parsing\Film base.csv", 'r', newline='') as r_file:
        file_reader = list(csv.reader(r_file, delimiter=";"))
        film = file_reader[number][0]
        return film


def get_link(film):
    with open("Parsing\Film base.csv", 'r', newline='') as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        link = ''
        for row in file_reader:
            if row[0].lower() == film.lower():
                link = row[1]
    return link


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


def save_film_info(items):
    for film in items['genres']:
        check = 0
        if str(film) == 'детский' or str(film) == 'музыка' or str(film) == 'короткометражный' or str(film) == 'сказка'\
                or str(film) == 'документальный':
            pass
        elif str(film) == 'фантастика' or str(film) == 'фэнтези':
            try:
                with open('фэнтези.csv', 'r', newline='') as file:
                    reader = csv.reader(file, delimiter=';')
                    for row in reader:
                        if items['filmName'] == row[0]:
                            check = 1
                if check == 0:
                    with open('фэнтези.csv', 'a', newline='') as file:
                        writer = csv.writer(file, delimiter=';')
                        writer.writerow([items['filmName'], items['review'], items['actors'], items['genres'], items['duration'],
                                        items['link']])
            except FileNotFoundError:
                with open('фэнтези.csv', 'a', newline='') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerow(
                        [items['filmName'], items['review'], items['actors'], items['genres'], items['duration'],
                         items['link']])
        elif str(film) == 'анимация':
            with open('мультфильм.csv', 'a', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow([items['filmName'], items['review'], items['actors'], items['genres'], items['duration'],
                                items['link']])
        else:
            with open(str(film)+'.csv', 'a', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow([items['filmName'], items['review'], items['actors'], items['genres'], items['duration'],
                                items['link']])


def parse():
    numbers = list(range(151, 201))
    for number in numbers:
        url = get_link(get_filmname(number))
        html = get_html(url)
        print(html.status_code)
        if html.status_code == 200:
            film = get_content(html.text, url)
            save_film_info(film)
        else:
            print('Error')
        time.sleep(5)

