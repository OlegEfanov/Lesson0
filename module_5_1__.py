class House:                                        #Создание класса House.
    # определяем метод __init__ и передаем название и кол-во этажей.
    def __init__(self, name, number_of_floors):
        self.name = name                            #Объект - имя
        self.number_of_floors = number_of_floors    #Объект - количество

    def go_to(self, new_floor):                     #Метод go_to
        if new_floor > self.number_of_floors or new_floor < 1:  #Если №этажа > кол-ву этажей или <1, то
            print('')
            print("Такого этажа не существует")
        else:                                       #иначе
            for i in range(1, new_floor + 1):       #перебрать с 1 этажа +1 до заданного
                print(i,'- этаж')

    def __len__(self):
        return self.number_of_floors                #Возвращает кол-во этажей

    def __str__(self):                              #Возвращает строку
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):                #other принадлежит ли классу House
            return self.number_of_floors == other.number_of_floors  #Математические методы

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):                       #метод слажения этажей
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)

    def __iadd__(self, value):
        return self.__add__(value)                  #использование метода __add__

    def __radd__(self, value):
        return self.__add__(value)

h1 = House('ЖК Горский', 18)    #Исходные данные, название и кол-во этажей
h2 = House('Домик в деревне', 2)

h3 = House('ЖК Эльбрус', 10)
h4 = House('ЖК Акация', 20)

print('')
print(h3)
print(h4)

print(h3 == h4)  #__eq__

h3 = h3 + 10     #__add__
print(h3)
print(h3 == h4)

h3 += 10         #__iadd__
print(h3)

h4 = 10 + h4     #__radd__
print(h4)

print(h3 > h4)   #__gt__
print(h3 >= h4)  #__ge__
print(h3 < h4)   #__lt__
print(h3 <= h4)  #__le__
print(h3 != h4)  #__ne__

