"""Lançamos o seguinte desafio: para ajudar na formatação de datas você deve criar uma nova classe auxiliar. Essa classe
 deve representar uma Data (sem hora) que sabe imprimir uma data formatada. Ela deve funcionar dessa forma:
    from datas import Data
    d = Data(21,11,2007)
    d.formatada()
    Imprime:
    21/11/2007
 """
from time import sleep


class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def formatted(self):
        print("Formatando a data...")
        sleep(2)
        print(f"A data é {self.day}/{self.month}/{self.year}")
