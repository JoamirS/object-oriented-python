class Movie:
    def __init__(self, name, year, duration):
        self.__name = name.title()
        self.year = year
        self.duration = duration
        self.__like = 0

    @property
    def like(self):
        return self.__like

    def give_likes(self):
        self.__like += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


class Series:
    def __init__(self, name, year, season):
        self.name = name.title()
        self.year = year
        self.season = season
        self.__like = 0

    @property
    def like(self):
        return self.__like

    def give_likes(self):
        self.__like += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


avengers = Movie('Avengers', 2012, 160)
friends = Series('Friends', 1994, 10)

print(f'Filme: {avengers.name}, Ano: {avengers.year}, Duração: {avengers.duration}')
print(f'Série: {friends.name}, Ano: {friends.year}, Temporadas: {friends.season}')
