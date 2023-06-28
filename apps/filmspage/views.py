from django.urls import reverse_lazy
from .models import Film
from django.views.generic import ListView, CreateView, UpdateView, DetailView, View
from django.shortcuts import render
from apps.watchlist.models import Watchlist
from apps.genreslist.models import GenresList

class FilmListView(ListView):
    model = Film
    

class FilmCreateView(CreateView):
    model = Film
    success_url = reverse_lazy('filmspage:film-list')
    fields = ['movie', 'date', 'rating', 'description', 'genre', 'photo']

class FilmUpdateView(UpdateView):
    model = Film
    success_url = reverse_lazy('filmspage:film-list')
    fields = ['movie', 'date', 'rating', 'description', 'genre', 'photo']

class FilmInfoView(DetailView):
    model = Film
    success_url = reverse_lazy('filmspage:film-list')
    fields = ['movie', 'date', 'rating', 'description', 'genre', 'photo']


def genres_view(request):
    genres_data = GenresList.objects.all()
    context = {
        'genres_data': genres_data,
    }
    return render(request, 'film_detail.html', context)

