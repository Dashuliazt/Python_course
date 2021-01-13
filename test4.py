import string
l = string.ascii_letters + string.digits
age = int(input('Ваш возраст'))
name = input('Ваше имя')
h = random.randint(len(name), age)
print(l[h])


