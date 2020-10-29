from django.shortcuts import render
from django.views import View
from django.db import connection

# Create your views here.


class MainView(View):
    template = "MainPage.html"

    with connection.cursor() as cursor:
        cursor.execute("SELECT film_title FROM film")
        film = cursor.fetchone()
        print(film)

    def get(self, request):
        return render(request, self.template, {"author": "Sebastian Siarczyński"})
