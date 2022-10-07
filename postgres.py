import psycopg2
from psycopg2 import Error


def question_get(question_id):
    try:
        connection = psycopg2.connect(user="marselzakiev",
                                      password="123",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="mars_db")

        cursor = connection.cursor()
        postgresql_select_query = """select * from questions where question_id = %s"""

        cursor.execute(postgresql_select_query, (question_id,))
        row_question = cursor.fetchall()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
        return row_question



        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         "SELECT version ();"
        #     )
        #     print(f"server version: {cursor.fetchone()}")

        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """ CREATE TABLE questions(
        #         question_id serial,
        #         question text,
        #         answer text);"""
        #     )
        #     connection.commit()
        #     print ("[INFO] Table created successfully")

        # # insert data to database
        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """ INSERT INTO questions(question_id, question, answer) VALUES
        #         (1, 'Халявный вопрос (ответ: 1)', '1');"""
        #     )
        #     connection.commit()
        #     print("[INFO] Data was successfully inserted")

        # get data from database
        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """SELECT question FROM questions WHERE question_id = '1';"""
        #     )
        #     print(cursor.fetchone())

    # except Exception as _ex:
    #     print("[INFO] Error while working with PostgreSQL database", _ex)
    # finally:
    #     if connection:
    #         connection.close()
    #         print("[INFO] PostgreSQL connection closed successfully")