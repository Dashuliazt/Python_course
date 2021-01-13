# class Dog:
#     legs = 4
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def bark(self, voice):
#         print(voice)
#
#
#
#
# alma = Dog('Alma', 8)
# alma.bark('Wooh')
# print(alma.legs)
# rex = Dog('Rex',4)
# rex.bark('Gaw')
# print(rex)

class Human:
    arms = 2
    legs = 2
    head = 1
    body = 1

    def __init__(self, firstname, lastname, sex, age):
     self.firstname = firstname
     self.lastname = lastname
     self.age = age
     self.sex = sex

    def greeting(self, firstname1):
        print(f'Hi, {firstname1}')
    def introduce_himself(self):
        print(f'My name is {self.firstname} {self.lastname}. I\'m {self.age}')
    def to_take(self, staff):
        print(f'I took {staff}')

    def sex_check(self, gender):
        if gender == 'woman':
            print('I love him.')
        elif gender == 'man':
            print('I love her.')
        else:
            print('I love it.')


Dar = Human('Dariia', 'Liashko', 'woman', 25)
Den = Human('Den', 'Green', 'man', 26)

Dar.greeting(Den.firstname)
Dar.introduce_himself()
Dar.to_take('tea')
Dar.sex_check(Den.sex)
Den.sex_check(Dar.sex)
