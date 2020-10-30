from django.shortcuts import render
from django.views import View
from django.db import connection
from .models import Film, Genre

# Create your views here.


class MainView(View):
    template = "base.html"

    query_for_films = "SELECT id, film_title FROM film LIMIT 3"
    query_for_genres = "SELECT id, genre_name FROM genre LIMIT 3"

    list_with_films = []
    list_with_genres = []

    for item in Film.objects.raw(query_for_films):
        list_with_films.append({"id": f"{item.id}", "title": f"{item.film_title}"})

    for item in Genre.objects.raw(query_for_genres):
        list_with_genres.append({"id": f"{item.id}", "name": f"{item.genre_name}"})
    # with connection.cursor() as cursor:
    #    cursor.execute("SELECT film_title FROM film")
    #    film = cursor.fetchone()
    #    print(film)

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
