from create_db import *

conn = connect_to_db('users', 'postgres', 'zxcvbnm')
cur = create_cursor(conn)
with open('test_data.csv', 'w') as file:
    cur.copy_expert("""COPY person TO STDOUT DELIMETER ','""", file)


# вывести в список
# cur.execute('SELECT * FROM person;')
# person = cur.fetchall()
# print(person)