# my_list = [1, 2, 4]
# iterator
# my_iter = iter(my_list)
# while True:
#     try:
#         print(next(my_iter))
#     except StopIteration:
#         break
#
#генератор №1
# def my_gen():
#     for i in range(10):
#         yield i
# m = my_gen()
# print(next(m))
# print(next(m))
# print(next(m))
#генератор №2
# my_gen1 = (x for x in range(10))
# print(my_gen1)
# for i in my_gen1:
#     print(i)

# import sys
# my_list = [x for x in range(100000000)]
# my_gen = (x for x in range(1000000000))
# print(sys.getsizeof(my_list))
# print(sys.getsizeof(my_gen))

# def count(start = 0):
#     while True:
#         yield start
#         start +=1
#
# c = count()
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

# my = (x for x in range(2))
#
# for i in my:
#     print(i)
#
# my1 = (x for x in range(2))
#
# for j in my1:
#     print(j)



# def foo():
#     print('hello')
# def foo1():
#     pass
# def foo2():
#     pass
#
# list_func = [foo, foo1, foo2]
# my_list = [1, 2]
# for func in my_list:
#     func(my_list)

# def foo():
#     def wraper():
#         print('hi')
#     return wraper
# foo()()

# декораторы
# def foo(func):
#     def wrapper():
#         print('before call func')
#         func()
#         print('after call func')
#     return wrapper
#
# # имя декоратора вызываем @foo
# @foo
# def hello():
#     print('Im code func hello')
#
# hello()
#
# def my_dec(func):
#     def wrapper(s):
#         return [x**2 for x in func(s)]
#     return wrapper
#
# def dec_minus(func):
#     def wrap(s):
#         return [x-1 for x in func(s)]
#     return wrap
#
#
# @dec_minus
# @my_dec
# def res_list(num):
#     return [x for x in range(num)]
#
# print(res_list(10))

def dec_myP(d):
    def dec_my(func):
        def wrap(s):
            return [x for x in func(s) if x%d ==0]
        return wrap
    return dec_my

def dec_mest(func):
    def wraps(s):
        return [str(x)*x for x in func(s)]
    return wraps


@dec_mest
@dec_myP(2)
def my_gen(num):
    return (x for x in range(num))
print(my_gen(10))

