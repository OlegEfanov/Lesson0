# i = int(input('Вве  дите число: '))
# try:
#     result = 10 * (1/i)
# except ZeroDivisionError as exc:
#     print('нельзя делить на ноль!', exc)
# else:
#     print('Ура! Мы не делим на ноль.', result)
# finally:
#     print('файнали мы закончили выполнение :)')

#   Пример 1
# def greet_person(person_name):
#     if person_name == 'ВоланДеМорт':
#         raise Exception('Мы не любим тебя, ВоланДеМорт!')
#     print(f'Привет, {person_name}')
#
# greet_person('Дорогой ученик')
# greet_person('ВоланДеМорт')

#   Пример 2
# try:
#     raise NameError('Привет Там')
# except NameError as exc:
#     print(f'Исключение типа {type(exc)} пролетело мимо! его параметр {exc.args}')
#     raise

#   Пример 3
#class ProZero(Exception):
#     pass
#
#def f(a, b):
#     if b == 0:
#         raise ProZero('Деление на ноль не возможно.')
#     return  a / b
#
#print(f(10,0))

#   Пример 4
class ProZero(Exception):
    def __init__(self, massege, extra_info):
        self.massege = massege
        self.extra_info = extra_info

def f(a, b):
    if b == 0:
        raise ProZero("Деление на ноль не возможно.", {"a": a, "b": b})
    return a / b

try:
    result = f(10, 1)
    print(result)
except ProZero as e:
    print('Не очень хороший день, мы словили ошибку.')
    print(f'Сообщение об ошибке: {e.massege}')
    print(f'Дополнительная информация {e.extra_info}')
