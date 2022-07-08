import pymysql
from config import host, port, password, user, db_name
from pymysql import cursors


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
        # Пример сортировки по определенному полю
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `teams`" \
                              "WHERE `City` = 'Лондон'" \
                              "ORDER BY Home_trophies DESC"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
                print('.'*25)

        # Поиск по шаблону
        with connection.cursor() as cursor:
            select_all_rows = "SELECT TeamName FROM `teams`" \
                              "WHERE `TeamName` LIKE '%ма%'"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
                print('.'*25)

        # GROUP BY и HAVING
        with connection.cursor() as cursor:
            select_all_rows = "SELECT City, SUM(Home_trophies) AS sum_trophies FROM `teams`" \
                              "GROUP BY (City)" \
                              "HAVING SUM(Home_trophies) > 25"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
                print('.'*25)

        # Связывание таблиц по определенным полям
        with connection.cursor() as cursor:
            select_all_rows = "SELECT best_coaches.Season AS Season, premier_league.Best_player AS Best_player," \
                              "best_coaches.Name AS Best_coach " \
                              "FROM `premier_league` join `best_coaches`" \
                              "on premier_league.Season = best_coaches.Season"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
                print('.'*25)
    finally:
        connection.close()
        print('Соединение закрыто')

except Exception as ex:
    print('Что-то пошло не так')
    print(ex)
