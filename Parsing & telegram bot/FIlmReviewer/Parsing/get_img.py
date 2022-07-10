import requests
from bs4 import BeautifulSoup


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'}


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


def get_result(url):
    html = get_html(url)
    print(html.status_code)
    if html.status_code == 200:
        save_img('Poster.png', get_image(get_image_url(html.text)))
    else:
        print('Error')



