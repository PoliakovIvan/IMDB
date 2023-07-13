from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator



class Film(models.Model):
    movie = models.CharField(_('movie'), max_length=255)
    date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    description = models.CharField(_('Description'), max_length=1000)
    photo = models.ImageField(upload_to='D:/python_hilel/python_pro/Projects/IMDB/media/photo/')
    trailer = models.URLField()




