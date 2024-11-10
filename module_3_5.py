def get_multiplied_digits (number):
    str_number = str(number)                                        #Строковое представление nimber.
    first = int(str_number[0])                                      #Запись первого символа в first.
    if len(str_number) > 1:                                         #Если ДЛИННА str_number>1 то -
        return first * get_multiplied_digits(int(str_number[1:]))   #возвращаем умножаем 1 цифру последовательно на все
    else:
        return first                                                # или вовращаем first первый символ.

result = get_multiplied_digits(40203)
print(result)