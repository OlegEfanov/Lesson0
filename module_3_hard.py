def calculate_structure_sum(data_structure):
    summa = 0                                           #Создаем нулевое значение, что бы в него потом складывать сумму
    if isinstance(data_structure, (list, set, tuple)):  #Если тип данных список, множество, картеж, то
        for i in data_structure:                        #перебираем все элементы из data_structure
            summa += calculate_structure_sum(i)         #и суммируем в summa
    elif isinstance(data_structure, dict):              #иначе если тип данных словарь
        for key, value in data_structure.items():       #перебираем ключ и его значение
            summa += calculate_structure_sum(key)       #суммируем ключи в summa
            summa += calculate_structure_sum(value)     #суммируем значения в summa
    elif isinstance(data_structure, str):               #иначе если тип данных строка
        summa += len(data_structure)                    #суммируем количество букв в summa
    elif isinstance(data_structure, int):               #иначе если тип данных число
        summa += data_structure                         #суммируем числа в summa
    return summa                                        #возвращаем summa


data_structure = [                                      #данные для подсчета
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)