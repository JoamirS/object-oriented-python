class Client:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print("chamando @property nome()")
        return self.name.title()
