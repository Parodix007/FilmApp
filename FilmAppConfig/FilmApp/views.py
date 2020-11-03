from django.shortcuts import render
from django.views import View
from .Templates.nav_dropdowns import NavDropdown


# Create your views here.
class RenderDropdowns:
    __nav_dropdowns = NavDropdown()

    def dropdowns(self):
        return {
            "film": f"{self.__nav_dropdowns.nav_film_render()}",
            "genre": f"{self.__nav_dropdowns.nav_genre_render()}",
        }


Dropdowns = RenderDropdowns()


class MainView(View):
    __template = "base.html"

    def get(self, request):
        return render(
            request,
            self.__template,
            Dropdowns.dropdowns(),
        )


class FilmView(View):
    __template = "base_film.html"

    def get(self, request):
        return render(request, self.__template, Dropdowns.dropdowns())
