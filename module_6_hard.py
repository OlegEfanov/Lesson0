import math

class Figure:
    sides_count = 0
    def __init__(self, color, sides, filled):
        self.__sides = sides    #список сторон
        self.__color = color    #список цветов
        self.filled = filled    #закрашенный

    def get_color(self):
        return self.__color     #возвращает список RGB цветов

    def __is_valid_color(self, r, g, b):        #принимает параметры r, g, b
        if 0 <= r <= 255 and  0 <= g <= 255 and 0 <= b <= 255:      #проверяет корректность переданных значений
            return True
        else:
            return False

    def set_color(self, r ,g, b):       #принимает параметры r, g, b
        result = self.__is_valid_color(r, g, b)
        if result == True:              #проверив их на корректность
            self.__color = [r, g, b]    #изменяет атрибут __color на соответствующие значения
        else:
            print('Цвет остаётся прежним.')

    def  __is_valid_sides(self, sides):
        for elem in sides:
            if not isinstance(elem, int) or not elem > 0:
                return False
        if len(self.__sides) == len(sides):
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def  set_sides(self, *new_sides):
        resultat = self.__is_valid_sides(new_sides)
        if resultat == True:
            self.__sides = new_sides
        else:
            print('Стороны остались прежними.')

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides, filled, radius):
        super().__init__(color, sides, filled)
        self.radius = sides[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides, filled):
        super().__init__(color, sides, filled)

    def get_square(self, a, b, c):
        a, b, c = self.get_sides()  # Получаем стороны треугольника
        s = (a + b + c) / 2  # Полупериметр
        return math.sqrt(s * (s - a) * (s - b) * (s - c))  # Площадь по формуле Герона

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides, filled):
        super().__init__([sides] * 12, color, filled)
        self.__sides = [sides] * self.sides_count

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())