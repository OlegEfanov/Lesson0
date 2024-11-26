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

h1 = House('ЖК Горский', 18)    #Исходные данные, название и кол-во этажей
h2 = House('Домик в деревне', 2)

h3 = House('ЖК Эльбрус', 10)
h4 = House('ЖК Акация', 20)

h1.go_to(5)                                         #Вызов метода go_to
h2.go_to(10)
print('')
print('__str__')
print(h3)
print(h4)
print('')
print('__len__')
print(len(h3))
print(len(h4))
