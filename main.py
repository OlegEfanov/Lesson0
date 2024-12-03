class Human:
    head = True

    def sey_hello(self):
        print('Здравствуйте')

class Student(Human):
    head = False
    def about(self):
        print('Я студент')


class Teacher(Human):
    pass

#human = Human()
student = Student()
teacher = Teacher()
student.sey_hello()
teacher.sey_hello()
print(student.head)