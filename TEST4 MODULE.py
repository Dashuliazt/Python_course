import datetime
#
# date = datetime.date(2020, 12, 13)
# print(date)
# d = datetime.datetime(2013, 12, 3, 12)
# print(d)
# dd = datetime.datetime.fromtimestamp(122220120)
# print(dd)
# frd = datetime.datetime.now().strftime('%d.%m.%Y')
# print(frd)
# delta = datetime.timedelta()
# print(delta)
# print(datetime.datetime.now()+delta)
# frad = datetime.datetime.now().strftime('%a')
# print(frad)
# import sys
# print(sys.argv)


import os
import datetime

#task 1
# def my_gen(dirname):
#     for el in os.listdir(dirname):
#         obj = os.path.join(dirname, el)
#         create = datetime.datetime.fromtimestamp(os.path.getctime(obj))
#         change = datetime.datetime.fromtimestamp(os.path.getmtime(obj))
#         yield f'{create} и была изменена {change}'
#
# for el in my_gen('Задание'):
#     print(el)

#task 2
# def NY():
#     now = datetime.datetime.today()
#     NY = datetime.datetime(2021,1,1)
#     d = NY-now
#     print('До нового года осталось: {} дней'.format(d.days))
#
# NY()

#task 3
import sys

# for el in sys.argv:
#     if el == '-t':
#         print(datetime.datetime.now().time())
#     elif el == '-d':
#         print(datetime.datetime.now().date())
#     elif el == '-dt':
#         print(datetime.datetime.now())
#     else:
#         pass

#task 4

# def dated(YEAr):
#
#     return datetime.datetime(YEAr, 1, 1).strftime('%A')
#
# print(dated(2021))

#task 5
# def dated(dbay_date, year_choice):
#     day, month, year = dbay_date.split('.')
#     return datetime.datetime(int(year_choice), int(month), int(day)).strftime('%A')
#
# print(dated('01.04.1995', '2021'))

#task 6
import date
def datedi(now):
    nofw = date(now).timetuple()
    return nofw

datedi()