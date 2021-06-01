class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.name_class = __class__.__name__

    def speak(self):
        print(f'{self.name_class} falando...')


class Client(Person):
    def buy(self):
        print(f'{self.name_class} falando...')


class Student(Person):
    def study(self):
        print(f'{self.name_class} estudando...')