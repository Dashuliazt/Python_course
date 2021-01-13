import psycopg2

def connect_to_db(dbname, username, passwd):
    conn = psycopg2.connect(dbname=dbname, user=username, password=passwd)
    return conn

def create_cursor(connector):
    return connector.cursor() # передача sql запроса

def commit(connector):
    connector.commit()

def close(connector):
    connector.close()



# def create_new_db(dbname, username, passwd, namedb):
#     conn = psycopg2.connect(dbname=dbname, user=username, password=passwd)
#     conn.autocommit = True
#     cur = conn.cursor()
#     cur.execute(f'CREATE DATABASE {namedb};') #передача запроса
#     conn.commit() #сохранить наши изменения
#     conn.close()


def create_new_db(connector, cursor, namedb):
    connector.autocommit = True
    cursor.execute(f'CREATE DATABASE {namedb};')



conn = connect_to_db('postgres', 'postgres', 'zxcvbnm')
cur = create_cursor(conn)
create_new_db(conn, cur, 'users')
commit(conn)
close(conn)
