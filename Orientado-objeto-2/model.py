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


avengers = Movie('Avengers', 2012, 160)
friends = Series('Friends', 1994, 10)

print(f'Filme: {avengers.name}, Ano: {avengers.year}, Duração: {avengers.duration}')
print(f'Série: {friends.name}, Ano: {friends.year}, Temporadas: {friends.season}')
