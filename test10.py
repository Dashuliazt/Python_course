# def column(g):
#     for i in range(g):
#         print(i)
# column(20)


# task 2
# def pow2(l):
#     h = l ** (1/2)
#     print(h)
# pow2(25)
#
#
# # task 3
# def longnum():
#     num = input('Просьба ввести цисло больше 5 цифр')
#     if len(num) >= 5:
#         for i in num:
#             print(i)
#     else:
#         print('Просьба ввести число более 5 символов')
# longnum()


# # task 4
# def nonefile(s):
#     name = s + '.txt'
#     f = open (name, 'w')
# nonefile(input('Просьба ввести имя файла'))

# task 5


#
# def key(n, name):
#     file_name = name + '.txt'
#     f = open(file_name, 'w')
#     letter_abc = list(string.ascii_letters)
#     digits_012 = list(string.digits)
#     letter_abc.extend(digits_012)
#     all_list = ''.join(random.sample(letter_abc, n))
#     f.write(all_list)
# key(11, 'keys')


# # task 6
# def only_list(d):
#     print(d)
#     if type(d) is list:
#         print(set(d))
#     else:
#         print('None')
#
# only_list(list('ABCDDSA'))


#task 7
# def tuple_list(i, j):
#     a =[]
#     if type(j) is list or type(i) is list or type(j) is tuple or type(i) is tuple:
#         a = list(set(i) - set(j))
#         a.extend(list(set(j) - set(i)))
#         print(a)
#     else:
#         print('Error on your type')
#
# tuple_list(tuple('asaas'),list('far'))

# task 8
random_string='zxccvbnm'
def counter(string):
    result = {el:0 for el in string}
    for i in string:
        result[i] +=1
    return result

print(counter(random_string))


# task 9
def max_word(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            words = file.read().replace(',', '').replace('.','').lower().split()
            counter_dict = counter(words)
            max_index = list(counter_dict.values()).index(max(counter_dict.values()))
            max_word = list(counter_dict.keys())[max_index]
            return max_word
    except FileNotFoundError:
        return None
print(max_word('NEW.txt'))



