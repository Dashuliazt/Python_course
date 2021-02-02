class Human:
    default_name = 'Dariia'
    default_age = 25

    def __init__(self, default_name, default_age, money, house):
        self.age = default_age
        self.name = default_name
        self.__money = money
        self.__house = house

    def info(self):
        print(f'Имя - {self.name} \nВозраст {self.age} \nДом - {self.__house} \nДеньги - {self.__money}')

    @staticmethod
    def default_info(default_name, default_age):
        print(f'Имя {default_name} Возраст {default_age}')







hun = Human('Dariia', 12, '1000','Пентхаус')
hun.default_info()