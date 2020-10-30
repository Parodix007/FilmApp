from django.db import models

# Create your models here.


class Film(models.Model):
    id = models.IntegerField(primary_key=True)
    film_name = models.CharField(max_length=50)

    def str(self):
        return self.film_name


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    genre_name = models.CharField(max_length=50)

    def str(self):
        return self.genre_name
