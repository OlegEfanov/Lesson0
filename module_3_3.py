#Функция с параметрами по умолчанию:
def print_params (a=1, b='string', c=True):
    print (a, b, c)

print_params(11, 22)
print_params()
print_params(b=25)
print_params(c=[1,2,3])

print()#2.Распаковка параметров:
values_list = [1, 2.2, 'python']
values_dict = {'a':'Oleg', 'b':2, 'c':False}

print_params(*values_list)
print_params(**values_dict)

print()#Распаковка + отдельные параметры:
values_list2 = ['string', 147]

print_params(*values_list2, 42)
