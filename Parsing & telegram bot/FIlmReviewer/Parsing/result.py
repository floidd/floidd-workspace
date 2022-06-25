import requests
from bs4 import BeautifulSoup
import csv
import random


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'}


def get_film(path):
    with open(path, 'r', newline='') as rFile:
        info = list(csv.reader(rFile, delimiter=';'))
        borders = list(enumerate(info))
        counter = random.randrange(borders[0][0], borders[-1][0]+1)
        print(counter)
        filmname = info[counter][0]
        review = info[counter][1]
        actors = info[counter][2].replace("'",'')
        genres = info[counter][3].replace("'",'')
        duration = info[counter][4]
        link = info[counter][5]
    return filmname, review, actors, genres, duration, link


def get_html(url):
    response = requests.get(url, headers=HEADERS)
    return response


def get_image_url(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='filmInfo_poster')
    imgurl = ''
    for item in items:
        imgurl = item.find('a', class_='filmInfo_posterLink').get('href')
    return imgurl


def get_image(url):
    response = requests.get(url, stream=True)
    return response


def save_img(name, file_data):
    file = open(name, 'bw')
    for chunk in file_data.iter_content(4096):
        file.write(chunk)


def get_result(path):
    filmname, review, actors, genres, duration, link = get_film(path)
    print(link)
    html = get_html(link)
    print(html.status_code)
    if html.status_code == 200:
        save_img('Parsing\Poster.png', get_image(get_image_url(html.text)))
    else:
        print('Error')
    return filmname, review, actors, genres, duration


