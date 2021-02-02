# age = int(input('Введите ваш возраст'))
# if age > 18:
#     print('Доступ разрешен')
# else:
#     print(f'Просьба подождать {18 - age} лет')
#
# #task2
# a = int(input('Введите число 0-10'))
# g = int(input('Введите число 0-10'))
# e = int(input('Введите число 0-10'))
#
# if a>g and a>e:
#     print(f'Наибольшее число {a}')
# elif g>a and g>e:
#     print(f'Наибольшее число {g}')
# elif e>a and e>g:
#     print(f'Наибольшее число {e}')
#
# #task3
# a = int(input('Введите число 5-15'))
# h = tuple(range(a))
#
# print(*h, sep='\n----\n', end='\nSuccess!')
#
# #task4
#
# a = int(input('\nВведите любое целое число'))
# if a%2 == 0:
#     print('Even number')
# else:
#     print('Odd number')
#
# #task5
# a = int(input('\nВведите год'))
# if a%4 ==0:
#     print('Высокосный год')
# else:
#     print('Не высокосный год')

#task6

# f = open('whitelist.txt', 'r+')
# h = open('blacklist.txt', 'r+')
# a = input('\nВведите ваше имя')
# f = f.read()
# h = h.read()
# if a in f:
#     print('Приветствуем Вас ' + a)
# if a in h:
#     print('Ваше имя ' + a + ' находится в блоке')
# else:
#     j = open('whitelist.txt', 'a+')
#     j.write('\n' + a)
#     j.read()
#     j.close()

#task7
f = open('whitelist.txt', 'r+')
h = open('blacklist.txt', 'r+')
f = f.read()
h = h.read()
f = f.split('\n')
h = h.split('\n')
d = open('all.txt', 'w+')
h.extend(f)
print(*h, sep='\nXXXXXXXXXXXXXXXX\n', end='\nPrint Finished ', file=d)

