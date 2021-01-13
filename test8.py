# #task 1
# for soten in range(101):
#     print(soten)
#
# #task 2
# n = 0
# for soten in range(101):
#     n+=soten
# print(n)
# #while
# soten = 0
# while soten < 101:
#     l += soten
#     soten +=1
# print(l)
#
# #task 3
# n = int(input('Введите число от 1 до 10'))
# t = int(input('Введите число от 100 до 1000'))
# list_all = []
# for p in range(n, t):
#     if p % 2 == 0:
#         list_all.append(p)
# print(list_all)
#
# list_all1 = [p for p in range(n, t) if p % 2 == 0]
# print(list_all1)
#
# #task 4
#
# for h in range(11):
#     j = '0'
#     print(str(h) + '-' + j*10)
#
#
# #task 5

n = int(input('Введите любое число'))
t = int(input('Введите любое число'))
k = int(input('Введите любое число'))
list_all = [n, t, k]
for same in range(len(list_all)):
    if list_all[same] == list_all[same]:
        print('SUPER')
    print('Not the same')
#
# #task 6
#
# n = int(input('Введите любое число'))
# j=1
# for fact in range(1,n+1):
#     j = j*fact
# print(j)

# #task 7
# n = int(input('Введите любое число'))
# D = {x:pow(x,2) for x in range(2,n+1)}
# print(D)

#task 8

import string

h = string.ascii_lowercase
dict_abc={}
p = 0
for j in h:
    dict_abc[h.index(j)+1]=j
dict_abc1 = {h.index(j)+1: j for j in h}
dict_cba = {value: key for key, value in dict_abc1.items()}

#task 9
import random
cities = ['Kiev', 'Odessa', 'Lviv', 'Chernihiv', 'Kharkiv']
temper = []
dict_city={}
for temp in random.sample(range(100, 1000), 7):
    temper.append(temp)
for j in range(len(cities)):
    dict_city[cities[j]] = temper
print(dict_city)

temper = [temp for temp in random.sample(range(100, 1000), 7)]
dict_city1 = {cities[j]: temper for j in range(len(cities))}
