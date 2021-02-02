# class Dog:
#     legs = 4
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# # одно нижнее подчёркивание _ - приватный но можно изменить
# # 2 подчеркивания __ - приватный защищённый параметр чтоби его ізменіть можно напісать rename
# # __str __ - короткую справку получим
#     def __str__(self):
#         return f'{self.name} is {self.age} years old.'
#
#     def bark(self):
#         print('Gav')
#
#
# class York(Dog):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color
#
#     def bark(self):
#         print('Woof')
#
# class JachRassel(Dog):
#     def bark(self):
#         print('jasd')
#
#
#
# rex = Dog('Rex',5)
# alma = York('Alma', 2)
# maylo = JackRassel('Maylo, 12')
# rex.bark()
# alma.bark()
# maylo.bark()
#
#
# # переименновать защищённый параметр
#
# class Dog:
#     legs = 4
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# # одно нижнее подчёркивание _ - приватный но можно изменить
# # 2 подчеркивания __ - приватный защищённый параметр чтоби его ізменіть можно напісать rename
# # __str __ - короткую справку получим
#     def __str__(self):
#         return f'{self.name} is {self.age} years old.'
#
#     def sound(self):
#         print('Gav')
#
# class Cat:
#     def sound(self):
#         print('Meow')
#
# class Cow:
#     def sound(self):
#         print('Moo')

# rex = Dog('name', 8)
# tom = Cat()
# burenka = Cow()

# # параметрический полимарфизм
# class SomeClass:
#     def sum(self, a, c):
#         return a+c
#
#
# # параметрический полимарфизм
# cl = SomeClass()
# print(cl.sum(1,9))
# print(cl.sum('1','9'))


# проверка трушности
# print(isinstance('20', int))

# animals = [rex, tom, burenka]
# # полимарфизм
# for animal in animals:
#     animal.sound()
    # вариант без полиморизма больше кода имеет:
    # if isinstance(animal, Dog):
    #     animal.bark()
    # elif isinstance(animal, Cat):
    #     animal.meow()
    # elif isinstance(animal, Cow):
    #     animal.moo()


#
# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#
#     @staticmethod
#     def validate(date_string):
#         year, month, day = list(map(int, date_string.split('-')))
#         res = 1 <= year <= 2020 and 1 <= month <= 12 and 1 <= day <= 30
#         return res, year, month, day
#
#     @classmethod
#     def create_obj(cls, date_string):
#         data = cls.validate(date_string)
#         if data[0]:
#             return cls(data[1], data[2], data[3])
#         else:
#             return None
#
#
# date_str = '2020-10-15'
# # проверка статического метода
# # print(Date.validate(date_str))
# date = Date.create_obj(date_str)
# print(date.year)

import string

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)
    def print(self):
        return self.letters
    def letters_num(self, letters):
        return len(self.letters)

class EngAlphabet(Alphabet):

    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False
        # print(isinstance(letter, Alphabet.print(self.lang)))

    def letters_num(self):
        return EngAlphabet.__letters_num
        # return self.letters_num()

    @staticmethod
    def example():
        print('Hi team!')


if __name__ == '__main__':
    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_en_letter('F'))
    print(eng_alphabet.is_en_letter('Щ'))
    EngAlphabet.example()


