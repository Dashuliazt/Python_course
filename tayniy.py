# # #генератор №1 создание функциями
# # def my_gen(num):
# #     for i in range(num):
# #         yield i
# # # обьект генератора
# # m = my_gen(10)
# # print(m)
# # print(next(m))
# # print(next(m))
# # print(next(m))
# #
# # #генератор №2
# # my_gen1 = (x for x in range(10))
# # print(my_gen1)
# # for i in my_gen1:
# #     print(i)
# #
# #
# # import datetime
# # import time
# #
# # def my_dec(func):
# #     def wrapper(num, p):
# #         with open('log.txt', 'a+') as file:
# #             start = time.time()
# #             result = func(num, p)
# #             finish = time.time()
# #             file.write(f'name func - {func.__name__} '
# #                        f'start - {datetime.datetime.fromtimestamp(start)}'
# #                        f'result func- {result} params{num, p} '
# #                        f'lead time - {finish-start}\n')
# #     return wrapper
# #
# # @my_dec
# # def my_pow(num, p):
# #     return num**p
# #
# # my_pow(2,8)
# # my_pow(12322,22228)
#
# def my_dec(name_dec='dec_1'):
#     def dec_1(func):
#         def wrapper(num, p):
#             return func(num,p)*2
#         return wrapper
#     def dec_2(func):
#         def wrapper(num, p):
#             return list(range(func(num,p)))
#         return wrapper
#     def dec_3(func):
#         def wrapper(num,p):
#             with open('dec3.txt','w') as file:
#                 file.write(f'{func(num,p)}\n')
#         return wrapper
#     if name_dec == dec_1:
#         return dec_1
#     elif name_dec == dec_2:
#         return dec_2
#     elif name_dec == dec_3:
#         return dec_3
#     else:
#         pass
#
#
# @my_dec('dec_2')
# def my_pow(num, p):
#     return num**p
#
# print(my_pow(2, 2))

# def dec_size_prem(perc):
#     def dec_premiya(func):
#         def wrapper(for_hour,hours_for_days, day_foe_week):
#             return func(for_hour,hours_for_days, day_foe_week) * (1 + perc/100)
#         return wrapper
#     return dec_premiya
#
# @dec_size_prem(35)
# def zp(for_hour,hours_for_days, day_foe_week):
#     zp = for_hour*hours_for_days*day_foe_week*4
#     return zp
#
# print(zp(100,8,5))

#task 3
import random


def dec_sum(func):
    def wrapper():
        list = func()
        list.sort(key=lambda x: sum(int(i) for i in str(x)))
        return list
    return wrapper


@dec_sum
def sto():
    return random.sample(range(10,1000),5)

print(sto())















