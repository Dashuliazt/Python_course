import random
num = random.sample(range(1,10),1)
while True:
    self = input('Попробуйте угадать, введите значение')
    if self == 'stop':
        print('Have a nice day')
        break
    try:
        if int(self) == num[0]:
            print('Yes it is')
            break
        elif int(self) > num[0]:
            print('Заданое значение меньше Вашего')
        else:
            print('Заданое значение больше Вашего')
        continue
    except ValueError:
        print('Вы ввели не верное значение, просьба ввести цифру')