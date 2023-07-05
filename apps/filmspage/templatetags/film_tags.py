from django import template

register = template.Library()

@register.filter
def has_genre_fantasy(film):
    return film.genresfilms_set.filter(genres_id=6).exists()