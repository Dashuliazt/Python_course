import psycopg2
from create_db import *



def create_table(cursor, table_name, **kwargs):


    columns = ''
    for key, value in kwargs.items():
        columns += f'{key} {value} NOT NULL,'
    query = f'CREATE TABLE {table_name} ({columns});'
    query = f'{query[:-3]});'
    cursor.execute(query)

conn = connect_to_db('users', 'postgres', 'zxcvbnm')
cur = create_cursor(conn)
create_table(cur, 'person',
             id='Serial',
             username='VARCHAR(30)',
             name = 'VARCHAR(30)',
             sex = 'VARCHAR(1)',
             address = 'VARCHAR(30)',
             birthdate = 'DATE',
             salary = 'DECIMAL(11,2)'
             )

commit(conn)
close(conn)
