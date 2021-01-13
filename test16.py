import shutil

# копирование файла
# shutil.copy('test.py', 'ders')
# скопирование папки со всем содержимым в другую папку
# shutil.copytree('Задание', 'Task')
# переместить файл с текущей папки в папку
# shutil.move('all.txt', 'Task')
# удаление папки целиком
# shutil.rmtree('Task')
# проверка места на диске
# shutil.disk_usage('C:')

# import sys
#
# def my_sum(x,y):
#     return x+y
# params = sys.argv
# print(my_sum(params[1],params[2]))

#
# import argparse
# def my_sum(x,y):
#     return x+y
# parser = argparse.ArgumentParser(description='First my app')
# parser.add_argument('a', type=int, help='first digit')
# parser.add_argument('b', type=int, help='second digit')
# parser.add_argument('-s', '--sum', action='store')
# # parser.add_argument('-s', '--sum', action='count') # считает кол-во -s
# args = parser.parse_args()
# print(my_sum(args.a, args.b))
# if args.sum:
#   print(my_sum(args.a,args.b))
# else:
#     print('OOps')

# nargs - in nargs - write count elem, if =* nothing ograni4eniy
# choice = [] - пропісиваем возможние варіанти ввода
# dest='summa' - переименование мени обьекта -
# но прописывает только в не обязат параметрах,
# те которые имеют тире перед переменной

# import argparse
# def my_sum(x,y):
#     return x+y
# parser = argparse.ArgumentParser(description='First my app')
# # parser.add_argument('digits', nargs=2, help='please enter 2 element')
# parser.add_argument('digits', choices=[1, 2, 3], type=int)
# parser.add_argument('-s', '--sum', action='count', dest='summa')
# args = parser.parse_args()
# print(args)

# import requests
# import argparse
# def get(url):
#     return requests.get(url)
#
# def save(filename, text):
#     with open(f'{filename}.html', 'w') as file:
#         file.write(text)
#
# def save_picture(filename, content, extension):
#     with open(f'{filename}.{extension}', 'wb') as file:
#         file.write(content)
#
#
#
# def check_url(url):
#     if 'png'==url[-3:]:
#         return True, 'png'
#     else:
#         return False, None
#
#
# def main():
#     parser = argparse.ArgumentParser(description='My first console app')
#     parser.add_argument('url', type=str, help='url for get')
#     parser.add_argument('-s', '--status', action='store_true')
#     parser.add_argument('-t', '--text',  action='store_true')
#     parser.add_argument('-S', '--save_html', nargs=1, type=str, action='store')
#     parser.add_argument('-p', '--picture', nargs=1, action='store')
#     args = parser.parse_args()
#     response=get(args.url)
#     check = check_url(args.url)
#     if args.status:
#         print(response.status_code)
#     elif args.text:
#         print(response.text)
#     elif args.save_html:
#         save(args.save_html[0], response.text)
#     elif check[0]:
#         save_picture(args.picture, response.content, check[1])
#
# main()
import shutil
import argparse
def copy_file(filename_copy, filename_new):
    shutil.copy(filename_copy, filename_new)


def move_file(filename_new):
    shutil.move(filename_new, 'Задание')


def main():
    parser = argparse.ArgumentParser(description='Second my console app')
    parser.add_argument('-s', '--save', nargs=2, action='store')
    args = parser.parse_args()
    copy_file(args.save[0], args.save[1])
    move_file(args.save[1])


main()