from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Film
from django.views.generic import ListView, CreateView, UpdateView, DetailView, View

from django.shortcuts import redirect, get_object_or_404
from apps.watchlist.models import Watchlist

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

