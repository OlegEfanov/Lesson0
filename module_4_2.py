def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

#inner_function() Ошибка вывода вне функции test_function, т.к. inner_function живет внутри test_function.
test_function()