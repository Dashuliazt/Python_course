# import random
#
# # task 1
#
# bubbles = [i for i in random.sample(range(0,100), 10)]
# print(bubbles)
# for bubble in range(len(bubbles)-1):
#     for j in range(len(bubbles)-bubble-1):
#         print('before:', bubbles)
#         if bubbles[j] > bubbles[j+1]:
#             bubbles[j], bubbles[j+1] = bubbles[j+1], bubbles[j]
#         print('after', bubbles)
#     print(bubbles)

# task 2

for i in range(10):
    try:
        num = int(input('Введите Ваше любимое число: '))
        print('Спасибо Вам за сотрудничество')
        break
    except ValueError:
        i = i + 1
        if i < 3:
            print('Просьба быть внимательнее и ввести число')
        elif i < 5:
            print('Вы ввели не число')
        elif i < 6:
            print('У Вас осталась последняя попытка для ввода числа')
        elif i > 5:
            print('Вы исчерпали все попытки')
            break
    continue