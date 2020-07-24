class Program:
    def __init__(self, name, year):
        self.__name = name.title()
        self.year = year
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def give_likes(self):
        self.__likes += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name.title()


class Movie(Program):
    def __init__(self, name, year, duration):
        self.__name = name.title()
        self.year = year
        self.duration = duration
        self.__like = 0


class Series(Program):
    def __init__(self, name, year, season):
        self.name = name.title()
        self.year = year
        self.season = season
        self.__like = 0


avengers = Movie('avengers', 2012, 160)
friends = Series('friends', 1994, 10)

print(f'Filme: {avengers.name}, Ano: {avengers.year}, Duração: {avengers.duration}')
print(f'Série: {friends.name}, Ano: {friends.year}, Temporadas: {friends.season}')
