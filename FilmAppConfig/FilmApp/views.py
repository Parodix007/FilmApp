from django.shortcuts import render
from django.views import View
from .querys import GetDataFromDB
from django.db import connection


# Create your views here.


class MainView(View):
    template = "base.html"

    query_for_films = "SELECT id, film_title FROM film LIMIT 3"
    query_for_genres = "SELECT id, genre_name FROM genre LIMIT 3"

    getFilms = GetDataFromDB(query_for_films)
    list_with_films = getFilms.get_film()

    getGenres = GetDataFromDB(query_for_genres)
    list_with_genres = getGenres.get_genre()

    def get(self, request):
        return render(
            request,
            self.template,
            {
                "author": "Sebastian Siarczyński",
                "films": self.list_with_films,
                "genres": self.list_with_genres,
            },
        )


class FilmView(View):
    template = "base_film.html"

    def get(self, request):
        return render(request, self.template)
