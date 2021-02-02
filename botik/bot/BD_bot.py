import mysql.connector
from mysql.connector import Error

def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='127.0.0.1',
                                       database='bot_support',
                                       user='pma',
                                       password='pma')
        if conn.is_connected():
            return conn

    except Error as e:
        return e



def autorithation(id_user):
    cnx = connect()
    isset_id_user = """SELECT * FROM user_auth WHERE id_user = %s"""
    val = [id_user]
    cursor = cnx.cursor()
    cursor.execute(isset_id_user, val)
    present_id_user = cursor.fetchall()
    return present_id_user
    # проверка если номер не существует в БД
    # if present_id_user:
    #     sql = """INSERT INTO user_auth, first_name, last_name (id_user, first_name, last_name) VALUES (%s, %s, %s)"""
    #     val = [id_user, first_name, last_name]
    #     cursor = cnx.cursor()
    #     cursor.execute(sql, val)
    #     cnx.commit()
    #     cursor.close()
    #     cnx.close()
    #     return sql

print(autorithation('2222'))