from django.template import Template, Context
from ..querys import GetDataFromDB

query_for_films = "SELECT id, film_title FROM film LIMIT 3"
query_for_genres = "SELECT id, genre_name FROM genre LIMIT 3"

getFilms = GetDataFromDB(query_for_films)
list_with_films = getFilms.get_film()

getGenres = GetDataFromDB(query_for_genres)
list_with_genres = getGenres.get_genre()


class NavDropdown:
    __nav_film_template = Template(
        "{% for film in films %}"
        '<a class="navbar-item" href="film?film={{ film.title }}"> {{ film.title }} </a>'
        "{% endfor %}"
    )

    __nav_genre_template = Template(
        "{% for genre in genres %}"
        '<a class="navbar-item" href="genre?genre={{ genre.name }}"> {{ genre.name }} </a>'
        "{% endfor %}"
    )

    def __init__(self):
        self.__film = list_with_films
        self.__genre = list_with_genres

    def nav_film_render(self):
        __nav_films_context = Context({"films": self.__film})
        return self.__nav_film_template.render(__nav_films_context)

    def nav_genre_render(self):
        __nav_genre_context = Context({"genres": self.__genre})
        return self.__nav_genre_template.render(__nav_genre_context)
