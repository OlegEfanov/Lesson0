class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):                  #новый метод
        cls.houses_history.append(args[0])              #добавление в список
        return object().__new__(cls)                     #возвращать ссылку на экземпляр класса

    def __init__(self, name, number_of_floors):
        self.name = name                                #Название
        self.number_of_floors = number_of_floors        #Количество

    def __del__(self):                                  #удаление названия из класса
        print(f'{self.name} снесён, но он останется в истории.')

    def __len__(self):
        return self.number_of_floors                    #Возвращает кол-во этажей

    def __str__(self):                                  #Возвращает строку
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):                    #other принадлежит ли классу House
            return self.number_of_floors == other.number_of_floors  # Математические методы

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

    def __add__(self, value):                           #метод слажения этажей
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)

    def __iadd__(self, value):
        return self.__add__(value)                      #использование метода __add__

    def __radd__(self, value):
        return self.__add__(value)



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)
