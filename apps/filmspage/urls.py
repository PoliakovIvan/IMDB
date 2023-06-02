
from django.urls import path

from apps.filmspage.views import FilmListView, FilmCreateView, FilmUpdateView, FilmInfoView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


app_name = 'filmspage'

urlpatterns = [
    path('', FilmListView.as_view(), name='film-list'),
    path('filmscreate/', FilmCreateView.as_view(), name='film-create'),
    path('filmscreate/<str:pk>/', FilmUpdateView.as_view(), name='film-update'),
    path('filmsinfo/<int:pk>/', FilmInfoView.as_view(), name='film-info'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)