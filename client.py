class Client:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.name.title()
