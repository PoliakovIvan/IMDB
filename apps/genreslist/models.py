from django.db import models
from django.utils.translation import gettext_lazy as _


class GenresList(models.Model):
    genres = models.CharField(_('genres'), max_length=255)
