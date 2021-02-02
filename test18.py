# class Human:
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname
#         self.__age = None
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if isinstance(value, int) and value>0:
#             self.__age = value
#         else:
#             raise ValueError('Age must be > 0.')
#     @age.deleter
#     def age(self):
#         del self.__age
#
#     @property
#     def fullname(self):
#         return f'{self.name} {self.lastname}'
#
#
#
# me = Human('Alexandr', 'Slipchenko')
# print(me.age)
# me.age = 25
# print(me.age)
# print(me.fullname)
#


# MIXIN methods
# class Radio:
#
#     def set_fm(self, value):
#         print(f'Set FM {value}.')
#
#     def play_song(self):
#         print('Play song!')
#
#     def play_rec(self):
#         print('Start rec')
#
#     def stop_rec(self):
#         print('Stop rec')
#
# # __приватные для того чтобы были доступны только эти методы
# из радио в этом данном классе

# class MixinRadio:
#     def __init__(self):
#         self.__radio = Radio()
#
#     def set_fm_and_play_song(self, value):
#         self.__radio.set_fm(value)
#         self.__radio.play_song()
#
#
#
#
# class Car(MixinRadio):
#
#     def __init__(self, color, brand):
#         super().__init__()
#         self.color = color
#         self.brand = brand
#
#     def start(self):
#         print('Start')
#
#     def stop(self):
#         print('Stop')
#
#     def ride(self):
#         print('Ride')
#
# audi = Car('black', 'Audi')
#
# audi.set_fm_and_play_song(108.1)

# Абстрактные методы нужны для того чтобы
# дочерние классы обязательно использовали методы в абстракте

# from abc import ABC
# from abc import abstractmethod
# class Human(ABC):
#     @abstractmethod
#     def speak(self):
#         print('Hello')
#
# class Jack(Human):
#     def speak(self):
#         print('Hi')
#
# jack = Jack()
# jack.speak()

# from abc import ABC
# from abc import abstractmethod
#
# class PlayerFactory(ABC):
#
#     @abstractmethod
#     def create_player(self, name):
#         pass
#
#     def create_weapon(self):
#         pass
#
# class PoliceFactory(PlayerFactory):
#
#     def create_player(self, name):
#         return Policeman(name)
#     def create_weapon(self):
#         return Colt()
#
# class TerroristFactory(PlayerFactory):
#
#     def create_player(self, name):
#         return Terrorist(name)
#     def create_weapon(self):
#         return Glock()
#
# class Policeman:
#
#     def __init__(self, name):
#         self.name = name
#         self.weapon = None
#
#     def add_weapon(self, weapon):
#         self.weapon = weapon
#
#     def shoot(self):
#         print(f'Policeman {self.name} shoot from {self.weapon.pistol()}')
#
#     def kill(self, name_terrorist):
#         print(f'Policemen {self.name} killed {name_terrorist}')
#
# class Terrorist(Policeman):
#
#     def __init__(self, name):
#         super().__init__(name)
#
#     def shoot(self):
#         print(f'Terrorist {self.name} shoot from {self.weapon.pistol()}')
#
#     def kill(self, name_policeman):
#         print(f'Terrorist {self.name} killed {name_policeman}')
#
# class Colt:
#
#     def pistol(self):
#         return 'Colt'
#
# class Glock:
#
#     def pistol(self):
#         return 'Glock'
#
#
# class Creator:
#     @staticmethod
#     def create_skin(factory, name):
#         player = factory.create_player(name)
#         weapon = factory.create_weapon()
#         player.add_weapon(weapon)
#         return player
#
# if __name__ == '__main__':
#     terrorist = Creator.create_skin(TerroristFactory(), 'Putin')
#     terrorist.shoot()
#     policemen = Creator.create_skin(PoliceFactory(), 'Ivanov')
#     policemen.shoot()
#     policemen.kill(terrorist.name)
#     terrorist.kill(policemen.name)

from abc import ABC
from abc import abstractmethod

class PlayerFactory(ABC):

    @abstractmethod
    def create_player(self, name):
        pass

    def create_skill(self):
        pass


class OrcFactory(PlayerFactory):

    def create_player(self, name):
        return Orc(name)
    def create_skill(self):
        return Ax()

class WizFactory(PlayerFactory):


    def create_player(self, name):
        return Wiz(name)
    def create_skill(self):
        return Magic_wand()

class Orc:

    def __init__(self, name):
        self.name = name
        self.skill = None

    def add_skill(self, skill):
        self.skill = skill

    def damage(self, value):
        print(f'Orc {self.name} received {value} damage with in {self.skill.tool()}')


class Wiz(Orc):
    def __init__(self, name):
        super().__init__(name)

    def heal(self, value):
        print(f'Wiz {self.name} healed with "{self.skill.tool()}" - {value} percent')


class Ax:

    def tool(self):
        return 'Ax'

class Magic_wand:

    def tool(self):
        return 'Magic wand'

class Creator:

    @staticmethod
    def create_person(factory, name):
        player = factory.create_player(name)
        skill = factory.create_skill()
        player.add_skill(skill)
        return player

if __name__ == '__main__':
    wiz = Creator.create_person(WizFactory(), 'MAG')
    wiz.heal(30)
    orc = Creator.create_person(OrcFactory(), 'Greg')
    orc.damage(70)