import pymysql
import Parsing
from database import config
from pymysql import cursors
import random


def create_table():
    try:
        connection = pymysql.connect(
            host=config.host,
            port=config.port,
            user=config.user,
            password=config.password,
            database=config.db_name,
            cursorclass=cursors.DictCursor
        )
        print('Успешное соединение')
        print('.' * 25)

        try:
            with connection.cursor() as cursor:
                create_table_query = "CREATE TABLE `all_films` (id INT AUTO_INCREMENT, filmname VARCHAR(75)," \
                                     "link TEXT, PRIMARY KEY(id))"
                cursor.execute(create_table_query)
                print('Таблица успешно создана')
                print('.' * 25)
        finally:
            connection.close()
            print('Соединение закрыто')

    except Exception as ex:
        print('Что-то пошло не так')
        print(ex)


def insert_data():
    try:
        connection = pymysql.connect(
            host=config.host,
            port=config.port,
            user=config.user,
            password=config.password,
            database=config.db_name,
            cursorclass=cursors.DictCursor
        )
        print('Успешное соединение')
        print('.'*25)
        try:
            films = Parsing.parse_ps()
            with connection.cursor() as cursor:
                for film in films:
                    insert_data_query = "INSERT INTO `all_films`(filmname, link) VALUES (%s, %s)"
                    cursor.execute(insert_data_query, (film['filmName'], film['link']))
                    connection.commit()
                print('Данные добавлены')
                print('.' * 25)
        finally:
            connection.close()
            print('Соединение закрыто')

    except Exception as ex:
        print('Что-то пошло не так')
        print(ex)


def get_film():
    try:
        connection = pymysql.connect(
            host=config.host,
            port=config.port,
            user=config.user,
            password=config.password,
            database=config.db_name,
            cursorclass=cursors.DictCursor
        )
        print('Успешное соединение')
        print('.'*25)
        try:
            number = random.randrange(1, 1001)
            with connection.cursor() as cursor:
                select_all_rows = "SELECT link FROM `all_films` Where id = %s"
                cursor.execute(select_all_rows, number)
                row = cursor.fetchall()
                url = row[0]['link']
                film = Parsing.parse(url)
        finally:
            connection.close()
            print('Соединение закрыто')
            return film

    except Exception as ex:
        print('Что-то пошло не так')
        print(ex)


def processing(film):
    filmname = film['filmName']
    review = film['review'][:-10]
    actors = ", ".join(film['actors'])
    genres = ", ".join(film['genres'])
    duration = film['duration']
    link = film['link']
    Parsing.get_result(link)
    return filmname, review, actors, genres, duration
