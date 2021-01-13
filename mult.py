import string
import random
import re
# таска 1
x = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
x.reverse()
print(x)
x.insert(0, 21)
x.append(9)
x.remove(20)
del x[2]
x.sort()
k = sum(x)
print(k)
# таска 2
number = int(input('Введите число от 10 до 30'))
letter_abc = list(string.ascii_letters[0:9])
letter_def = list(string.ascii_letters[10::])
digits_012 = list(string.digits)
letter_abc.extend(letter_def)
letter_abc.extend(digits_012)
all_list = '' .join(random.sample(letter_abc, number))
print(all_list)

# таска 3
dtb = input('Введите Вашу дату рождения в формате дд.мм.ГГГГ:')
r = input('Введите ваш рост:')
m = input('введите ваш вес:')
dtb1 = input('Введите дату рождения вашего родственника формате дд-мм-ГГГГ:')
fdf = dtb.split('.', 2)
fdf1 = dtb1.split('-', 2)
list_all = [r, m, fdf]
fdf.extend(fdf1)
list_all = [r, m, fdf]
dtb_all = list_all.pop(2)
list_all, dtb_all = dtb_all, list_all
print(list_all, dtb_all)

# таска 4

rr = int(input('Введите двухзначное число:'))
rrrr = int(input('Введите четырёхзначное число:'))
list_rr = random.sample(range(rr, rrrr), 10)
list_rr_max = list_rr.index(max(list_rr))
list_rr_min = list_rr.index(min(list_rr))
list_rr[list_rr_max],list_rr[list_rr_min] = list_rr[list_rr_min], \
                                            list_rr[list_rr_max]
print(list_rr)

# таска 5

list_first = random.sample(range(10, 100), 10)
list_sec = random.sample(range(10, 100), 10)
list_third = random.sample(range(10, 100), 10)
list_all = [list_first, list_sec, list_third]
list_all[2][7], list_all[2][8], list_all[2][9] = list_all[0][0], list_all[0][1], \
                                               list_all[0][2]
list_all[0][7], list_all[0][8], list_all[0][9] = list_all[2][0], list_all[2][1],\
                                                 list_all[2][2]
print(list_all)
list_all[1][:5] = list_all[0][:5]
list_all[0][5:] = list_all[1][5:]
print(list_all)

list_one_all.extend(list_first)
list_one_all.extend(list_sec)
list_one_all.extend(list_third)
print(list_one_all)