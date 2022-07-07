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

        # создание таблицы
        with connection.cursor() as cursor:
            create_table_query = "CREATE TABLE `people` (id INT AUTO_INCREMENT, name VARCHAR(50)," \
                                 "profession VARCHAR(50), PRIMARY KEY(id))"
            cursor.execute(create_table_query)
            print('Таблица успешно создана')
            print('.' * 25)

        # добавление данных
        with connection.cursor() as cursor:
            insert_data_query = "INSERT INTO `people`(name, profession) VALUES" \
                                "('Владимир', 'Доктор'), ('Олег', 'Учитель')," \
                                "('Ольга', 'Инженер'), ('Максим', 'Автомеханик')"
            cursor.execute(insert_data_query)
            connection.commit()
            print('Данные добавлены')
            print('.' * 25)

        # Обновление данных
        with connection.cursor() as cursor:
            update_data_query = "UPDATE `people` SET profession = 'Спортсмен' WHERE id = 2"
            cursor.execute(update_data_query)
            connection.commit()
            print('Данные обновлены')
            print('.' * 25)

        # Удаление данных
        with connection.cursor() as cursor:
            delete_data_query = "DELETE FROM `people` WHERE profession = 'Спортсмен'"
            cursor.execute(delete_data_query)
            connection.commit()
            print('Данные удалены')
            print('.' * 25)

        # Вывод данных
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `PEOPLE`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
                print('.'*25)

        #Удаление таблицы
        with connection.cursor() as cursor:
            delete_table_query = "DROP TABLE `people`"
            cursor.execute(delete_table_query)
            print('Таблица успешно удалена')
            print('.'*25)
    finally:
        connection.close()
        print('Соединение закрыто')
except Exception as ex:
    print('Что-то пошло не так')
    print(ex)





