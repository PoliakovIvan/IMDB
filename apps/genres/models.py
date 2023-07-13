from django.db import models
from apps.filmspage.models import Film
from apps.genreslist.models import GenresList


class GenresFilms(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    genre = models.ForeignKey(GenresList, on_delete=models.CASCADE)