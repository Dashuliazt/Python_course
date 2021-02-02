import string

shfr = input('Вы хотите зашифровать(Z) либо расшифровать(R) Ваш файл').upper()


def file_for_work():
    while True:
        try:
            name_file = input('Введите имя исходного файла')
            with open(name_file + '.txt') as file:
                lines_file = file.readlines()
            return lines_file
        except FileNotFoundError:
            print('Ошибка: Просьба ввести существующий файл')
            break


def work_with_ans(shfr):
    while True:
        try:
            if shfr == 'Z':
                key_z = int(input('Ключ сдвига'))
            elif shfr == 'R':
                key_z = int(input('Ключ сдвига'))
                key_z = - key_z
            else:
                print('Ошибка: Введите верное значение')
                break
        except ValueError:
            print('Ошибка: Просьба ввести цифру')
            break
        return key_z


def caesar_shifr():
    lines_file = file_for_work()
    key_z = work_with_ans(shfr)
    shifr_after = []
    for i in range(len(lines_file[0])):
        # проверка буква ли это
        if lines_file[0][i].isalpha():
            # проверка большая буква или маленькая
            if lines_file[0][i].isupper():
                abc = string.ascii_uppercase
            else:
                abc = string.ascii_lowercase
            j = abc.find(lines_file[0][i])
            k = j + int(key_z)
            # проверка или не выходит за кол-во букв в алфавите
            if k >= len(string.ascii_lowercase):
                g = abc[k - len(string.ascii_lowercase)]
            else:
                g = abc[k]
        else:
            g = lines_file[0][i]
        shifr_after.append(g)
    shifrs = ''.join(shifr_after)
    name_file_z = input('Введите имя файла для вывода результата')
    with open(name_file_z + '.txt', 'w+') as file:
        file.write(shifrs)
    return file


caesar_shifr()
