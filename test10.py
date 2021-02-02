# a =[]
# def my_sum(s,c,k):
#     for i in range(c):
#         a.append(k)
#     for j in range(s):
#         print (a)
# my_sum(3,5,1)

# task 2
# a =[]
# def my_sum(s,c,k=0):
#     for i in range(c):
#         a.append(k)
#     for j in range(s):
#         print (a)
# my_sum(3,5)

# # task 3
#
# upper = lambda x: x.upper()
# print(upper('dddd'))
#
# # task 4
# import string
# k =[]
# for i in string.ascii_lowercase:
#     k.append(i)
# print(list(map(upper, k)))

# task 5

# import string
# import random
# def low_up():
#     k = random.sample(string.ascii_letters, 10)
#     print(k)
#     for i in range(len(k)):
#          if str(k[i]).isupper():
#             k[i] = str(k[i]).replace(k[i],str(k[i]).lower())
#     print(k)
#
# low_up()
# task 5 - 2
# import string
# import random
# print(list(map(lambda x: str(x).replace(x, str(x).lower()),
#                 random.sample(string.ascii_letters, 10))))
# task 6


print(list((map(lambda x : x if x%3 == 0 else 0, [i for i in range(-20,20)]))))
