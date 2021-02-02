# a = tuple((1,2,3))
# s = (3,4,5)
# ol_tup = tuple(set(list(s)).intersection(list(a)))
# c = tuple(set(a).union(s))
# h = tuple(set(a).difference(s))
# k = list(c)
# k.reverse()
# l = tuple(k)
# j = list(l)

#task 2
first_name = input('Введети имя')
last_name = input('Введети фамилию')
size = input('Укажите ваш размер обуви')
file = open('new_file.txt', 'w+')
file.write(first_name + ' ' + last_name + ' - ' + size)
file.close()
l = len(str(file))
p = l-2
file.seek(p)


#
# #task3
# file = open('new_file.txt', 'w')
# str = first_name + '' + last_name + ' -' + size
# str.replace()
# file.write(str)
# file.close()
#
# #task4
#

