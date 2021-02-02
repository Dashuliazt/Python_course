from create_db import *

def insert_data_to_table(cursor, namefile, tablename):
    with open(namefile, 'r') as file:
        next(file)
        cursor.copy_expert(f'COPY {tablename} FROM STDIN CSV;', file)

if __name__ == '__main__':
    conn = connect_to_db('users', 'postgres', 'zxcvbnm')
    cur = create_cursor(conn)
    insert_data_to_table(cur, 'users.csv', 'person')
    commit(conn)
    close(conn)