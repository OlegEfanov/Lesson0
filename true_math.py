from math import inf        #Импорт бесконечности

def divide(first, second):
    if second == 0:         #Если seconf = 0, то
        return inf          #Вернуть бесконечность
    return first / second   #а если нет то вернуть результат деления
