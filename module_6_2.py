class Vehicle:                                                                     #Любой транспорт

    def __init__(self, owner:str, __model:str, __color:str, __engine_power:int):
        self.owner = owner                                                          #Владец транспорта
        self.__model = __model                                                      #Модель
        self.__engine_power = __engine_power                                        #Мощность двигателя
        self.__color = __color                                                      #Цвет

    __COLOR_VARIANTS = ['blue', 'gray', 'white', 'black', 'green','red']

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return  f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):                                   #распечатывает результаты методов в том же порядке
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color:str):         #принимает аргумент new_color(str), меняет цвет __color
        if new_color.lower in self.__COLOR_VARIANTS:        #на new_color, если он есть в списке
            self.__color = new_color
        else:
            print(f'Нельзя поменять цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5          #в седан может поместиться только 5 пассажиров

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()