class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._like = 0

    @property
    def likes(self):
        return self._like

    def give_likes(self):
        self._like += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

    def __str__(self):
        return f'{self._name} - {self.year} - {self._like} Likes'


class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'{self._name} - {self.year} - {self.duration} min - {self._like} Likes'


class Series(Program):
    def __init__(self, name, year, season):
        super().__init__(name, year)
        self.season = season

    def __str__(self):
        return f'{self._name} - {self.year} - {self.season} temporadas - {self._like} Likes'


avengers = Movie('avengers', 2012, 160)
friends = Series('friends', 1994, 10)


movies_and_series = [avengers, friends]

avengers.give_likes()
avengers.give_likes()

friends.give_likes()
friends.give_likes()

for program in movies_and_series:
    print(program)
