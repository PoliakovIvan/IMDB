from apps.watchlist.views import *
from django.urls import path
from apps.filmspage.views import FilmInfoView
from apps.watchlist.views import  WatchlistView
from django.conf import settings
from django.conf.urls.static import static



app_name = 'genrelist'

urlpatterns = [
    path('', WatchlistView.as_view(), name='watchlist-list'),
    path('filmsinfo/<int:pk>/', FilmInfoView.as_view(), name='film-info'),
    path('add-to-watchlist/<int:film_id>/', add_to_watchlist, name='add-to-watchlist'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)