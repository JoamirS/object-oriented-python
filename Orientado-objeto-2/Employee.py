class Employee:
    def __init__(self, name):
        self.name = name

    def register_time(self, time):
        print('Horas registradas...')

    def show_task(self):
        print('Fez muita coisa...')


class Caelum(Employee):
    def show_task(self):
        print('Fez muita coisa, Caelumer')

    def search_courses_of_month(self, month=None):
        print(f'Mostrando cursos - {month}' if month else 'Mostrando cursos desse mês')


class Alura(Employee):
    def show_task(self):
        print('Fez muita coisa, Alurete!')

    def search_question_without_answer(self):
        print('Mostrando questões não respondidas no fórum.')


class Hipster:
    def __str__(self):
        return f'Hipster, {self.name}'


class Junior(Alura):
    pass


class Pleno(Alura, Caelum):
    pass


class Senior(Alura, Caelum, Hipster):
    pass


jose = Junior()
jose.search_question_without_answer()

luan = Senior('Luan')
print(luan)
