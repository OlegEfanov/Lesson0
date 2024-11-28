class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль.
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

    def check_password(self,password):
        # Проверяем длину пароля
        if len(password) < 8:
            return False
        # Проверяем, есть ли в пароле хотя бы одна латинская буква в верхнем регистре
        if not any(char.isupper() for char in password):
            return False
        # Проверяем, есть ли в пароле хотя бы одна латинская буква в нижнем регистре
        if not any(char.islower() for char in password):
            return False
        # Проверяем, есть ли в пароле хотя бы одна цифра
        if not any(char.isdigit() for char in password):
            return False
        # Если все проверки пройдены успешно, возвращаем True
        return True

    #if check_password(password):
    #    print("Пароль надёжный")
    #else:
    #    print("Пароль ненадёжный")

if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input("Приветствую! Выберите действия: \n1 - Вход\n2 - Регистрация\n"))
        if choice == 1:
            login = input('Введите логин:')
            password = input('Введите пароль:')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен. {login}')
                    break
                else:
                    print('Повторите пароль.')
            else:
                print('Пользователь не найдет.')
        if choice == 2:
            user = User(input('Введите логин:'), password := input('Введите пароль:'),
                        password2 := input('Повторите пароль:'))
            if password != password2:
                print('Пароли не совподают, по пробуйте еще раз.')
                continue
            database.add_user(user.username, user.password)
