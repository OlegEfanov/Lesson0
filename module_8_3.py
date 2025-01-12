def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:                               #перебор чисел в numbers
        try:
            result += i                             #увеличивать переменную result
        except TypeError as exc:                    #обработать исключение TypeError
            incorrect_data += 1                     #увеличив счётчик  incorrect_data
            print(f'Некорекктный тип данных для подсчёта суммы - {i})')
    return result, incorrect_data

def calculate_average(numbers):
    try:
        result_1 = personal_sum(numbers)                        #используйте функцию personal_sum
        return result_1[0] / (len(numbers) - result_1[1])       #среднее арифметическое всех чисел
    except ZeroDivisionError:                                   #обработать исключение ZeroDivisionError
        return 0                                                #верните 0
    except TypeError:                                           #обработать исключение TypeError
        return print(f'В numbers записан некорректный тип данных')
    if isinstance(numbers, int):                                #проверка типа данных
        return None                                             #просто вернёт None

print(f'Результат 1: {calculate_average("1, 2, 3")}')           # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')                 # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')    # Всё должно работать