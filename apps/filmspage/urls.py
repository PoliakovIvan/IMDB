from django.urls import path
from apps.filmspage.views import FilmListView, FilmCreateView, FilmUpdateView, FilmInfoView, genres_view
from django.conf import settings
from django.conf.urls.static import static
from . import views
from apps.watchlist.views import  WatchlistView

app_name = 'filmspage'

urlpatterns = [
    path('', FilmListView.as_view(), name='film-list'),
    path('filmscreate/', FilmCreateView.as_view(), name='film-create'),
    path('filmscreate/<str:pk>/', FilmUpdateView.as_view(), name='film-update'),
    path('filmsinfo/<int:pk>/', FilmInfoView.as_view(), name='film-info'),
    path('genres/', genres_view, name='genres-list'),
    #path('add-to-watchlist/<int:film_id>/', WatchlistView.as_view(), name='add-to-watchlist'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
