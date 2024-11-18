import fake_math as f_m                     #Импорт всего модуля и его переименование
import true_math as t_m                     #Импорт всего модуля и его переименование

result1 = f_m.divide(69, 3)     #Исходные данные
result2 = f_m.divide(3, 0)
result3 = t_m.divide(49, 7)
result4 = t_m.divide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)