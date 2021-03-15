class People:
    def __init__(self, name, age, eating=False, speaking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.eating = eating

    def __str__(self):
        return self.name

    def eat(self, food):
        if self.eating:
            print(f'{self.name} já está comendo.')
            return

        print(f'{self.name} já está comendo {food}')
        self.eating = True

    def stop_eat(self):
        if not self.eating:
            print(f'{self.name} não está comendo.')
            return
