from django.urls import path
from .views import MainView, FilmView


urlpatterns = [path("", MainView.as_view()), path("films/", FilmView.as_view())]
