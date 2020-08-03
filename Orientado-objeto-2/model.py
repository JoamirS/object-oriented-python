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


class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    @property
    def list(self):
        return self._programs

    @property
    def size(self):
        return len(self._programs)


avengers = Movie('avengers', 2012, 160)
friends = Series('friends', 1994, 10)
the_boys = Series('the boys', 2019, 1)
hancok = Movie('hancok', 2008, 150)

the_boys.give_likes()
the_boys.give_likes()

hancok.give_likes()

avengers.give_likes()
avengers.give_likes()

friends.give_likes()
friends.give_likes()

movies_and_series = [avengers, friends, the_boys, hancok]
playlist_weekend = Playlist('fim de semana', movies_and_series)

print(f'Tamanho da minha playlist: {len(playlist_weekend.list)}')

for program in playlist_weekend.list:
    print(program)
