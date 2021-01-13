# from faker import Faker
# import csv
# import random
#
# faker = Faker()
# with open('users.csv', 'w') as file:
#     headers = ['id', 'username', 'name', 'sex', 'address', 'mail', 'birthdate', 'salary']
#     writer = csv.DictWriter(file, fieldnames=headers, lineterminator='\n')
#     for i in range(1, 1001):
#         data = {
#             'id': i,
#             'username': faker.user_name(),
#             'name': faker.name(),
#             'sex': faker.simple_profile()['sex'],
#             'address': faker.address().replace('\n', ' '),
#             'mail': faker.ascii_email(),
#             'birthdate': faker.date(),
#             'salary': random.randint(6000, 50000)
#         }
#         writer.writerow(data)
#
#
# # faker = Faker()
# # print(faker.simple_profile())


import psycopg2

