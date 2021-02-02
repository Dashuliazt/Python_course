import re

names = input('Ваше имя')
age = str(input('Ваш возраст'))
w_m = input('Ваш пол')
tx = str('Hello! My name is' + names + '. I\'m' + age + '. I\'m a' + w_m + '.')
print(tx)
another_string = 'Hello! My name is %s. I\'m %s. I\'m a %s.' % (names, age, w_m)
print(another_string)
another_string1 = 'Hello! My name is {0}. I\'m {1}. I\'m a {2}.'.format("Den",
                                                                        "28",
                                                                        "men")
print(another_string1)
about_me_fstring = f'Hello! My name is {names}. I\'m {age}. I\'m a {w_m}.'
print(about_me_fstring)
s = re.split('\.|\!', about_me_fstring)
s1 = s[0]; s2 = s[1]; s3 = s[2]; s4 = s[3]
print(s1); print(s2); print(s3); print(s4)
about_me_fstring = about_me_fstring.replace(names, 'Raise')
about_me_fstring = about_me_fstring.replace(age, '24')
about_me_fstring = about_me_fstring.replace(w_m, 'woman')
print(about_me_fstring)
list_from_str = re.split('\.|\!', about_me_fstring)
print(type(list_from_str))
str_from_list ='. '.join(list_from_str)
print(str_from_list)
me_string = about_me_fstring.swapcase()
print(me_string)





