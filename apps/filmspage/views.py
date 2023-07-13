from django.urls import reverse_lazy
from .models import Film
from django.views.generic import ListView, CreateView, UpdateView, DetailView



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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()
        genres_list = film.genresfilms_set.all() 
        context['genres_list'] = genres_list
        return context

    
