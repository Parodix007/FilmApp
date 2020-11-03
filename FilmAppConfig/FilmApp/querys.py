from django.db import connection


class GetDataFromDB:
    def __init__(self, query):
        self.__query = query

    def get_film(self):
        __list_of_films = []

        try:
            from .models import Film
        except ImportError:
            return ImportError("Could not import database")

        try:
            for item in Film.objects.raw(self.__query):
                __list_of_films.append(
                    {"id": f"{item.id}", "title": f"{item.film_title}"}
                )

            return __list_of_films
        except SyntaxError:
            return False

    def get_genre(self):
        __list_of_genres = []

        try:
            from .models import Genre
        except ImportError:
            raise ImportError

        try:
            for item in Genre.objects.raw(self.__query):
                __list_of_genres.append(
                    {"id": f"{item.id}", "name": f"{item.genre_name}"}
                )
            return __list_of_genres
        except SyntaxError:
            return False
