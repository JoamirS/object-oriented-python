from datetime import date


class People:
    current_year = int(date.today().year)

    def __init__(self, name, age, eating=False, speaking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.speaking = speaking

    def __str__(self):
        return self.name

    def speak(self, subject):
        if self.eating:
            print(f'{self.name} não pode falar comendo.')
            return

        if self.speaking:
            print(f'{self.name} já está falando.')
            return

        print(f'{self.name} está falando sobre {subject}.')
        self.speaking = True

    def stop_speak(self):
        if not self.speaking:
            print(f'{self.name} não está falando.')
            return

        print(f'{self.name} parou de falar.')
        self.speaking = False

    def eat(self, food):
        if self.eating:
            print(f'{self.name} já está comendo.')
            return

        if self.speaking:
            print(f'{self.name} não pode comer falando.')
            return

        print(f'{self.name} está comendo {food}')
        self.eating = True

    def stop_eat(self):
        if self.eating:
            self.eating = False
            print(f'{self.name} parou de comer')
            return

        if not self.eating:
            print(f'{self.name} não está comendo.')
            return
