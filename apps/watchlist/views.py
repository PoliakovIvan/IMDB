from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from requests import request

from apps.filmspage.models import Film
from .models import Watchlist
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

class WatchlistView(LoginRequiredMixin, ListView ):
    model = Watchlist
    template_name = 'watchlist/watchlist_list.html'
    success_url = reverse_lazy('watchlist:watchlist-list')

    def watchlist_view(request):
        watchlist_objects = Watchlist.objects.all()
        context = {'watchlist_objects': watchlist_objects}
        return render(request, 'watchlist.html', context)

    def get_queryset(self):
        user = self.request.user
        return Watchlist.objects.filter(user=user)


    def watchlist(request):
        if request.user.is_authenticated:
            watchlist = Watchlist.objects.filter(user=request.user)
            context = {'watchlist': watchlist}
            return render(request, 'watchlist/watchlist_list.html', context)
        else:
            return render(request, 'watchlist/watchlist_list.html')
        


def add_to_watchlist(request, film_id):
    if request.user.is_authenticated:
        film = get_object_or_404(Film, id=film_id)
        try:
            watchlist = Watchlist.objects.get(user=request.user, film=film)
            watchlist.delete()  # Видаляємо запис, якщо вже існує
        except Watchlist.DoesNotExist:
            watchlist = Watchlist(user=request.user, film=film)
            watchlist.save()
    return redirect('filmspage:film-list')
