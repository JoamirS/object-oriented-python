class Client:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print("chamando @property nome()")
        return self.__name.title()

    @name.setter
    def name(self, new_name):
        print("Chamando setter nome()")
        self.__name = new_name

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, new_limit):
        self.__limit = new_limit
