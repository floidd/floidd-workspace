import pymysql
from config import host, port, password, user, db_name
from pymysql import cursors
import csv

try:
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=db_name,
        cursorclass=cursors.DictCursor
    )
    print('Успешное соединение')
    print('.'*25)

    try:
        with connection.cursor() as cursor:
            create_table_query = "CREATE TABLE `best_coaches` (id INT AUTO_INCREMENT, Season VARCHAR(10)," \
                                 " Name VARCHAR(50)," \
                                 "TeamName VARCHAR(50), PRIMARY KEY(id))"
            cursor.execute(create_table_query)
            print('Таблица успешно создана')
            print('.' * 25)

        with connection.cursor() as cursor:
            with open("coaches.csv", 'r', newline='') as r_file:
                file_reader = csv.reader(r_file, delimiter=";")
                for row in file_reader:
                    insert_data_query = "INSERT INTO `best_coaches`(Season, Name, TeamName) VALUES (%s, %s, %s)"
                    cursor.execute(insert_data_query, row)
                    connection.commit()
                    print('Данные добавлены')
                    print('.' * 25)
    finally:
        connection.close()
        print('Соединение закрыто')

except Exception as ex:
    print('Что-то пошло не так')
    print(ex)
