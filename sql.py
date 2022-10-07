import psycopg2

try:
    connection = psycopg2.connect(user="marselzakiev",
                                  password="123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="mars_db")





    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version ();"
        )
        print(f"server version: {cursor.fetchone()}")

# with connection.cursor() as cursor:
#     cursor.execute(
#         """ CREATE TABLE questions(
#         question_id serial,
#         question text,
#         answer text);"""
#     )
#     connection.commit()
#     print ("[INFO] Table created successfully")

# insert data to database
    with connection.cursor() as cursor:
        cursor.execute(
            """ INSERT INTO questions(question_id, question, correct_answer, incorrect_answer_1, incorrect_answer_2, incorrect_answer_3) VALUES
            (1, 'Укажите, какие спецификаторы доступа не существуют', 'open', 'public', 'protected', 'private');"""
        )
        connection.commit()
        print("[INFO] Data was successfully inserted")

    # get data from database
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT question FROM questions WHERE question_id = '1';"""
    #     )
    #     print(cursor.fetchone())

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE questions; """
    #     )
    #     print("[INFO] TABLE WAS DELETED successfully")


except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL database", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed successfully")