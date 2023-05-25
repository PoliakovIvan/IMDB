
from django.urls import path

from apps.filmspage.views import FilmListView, FilmCreateView, FilmUpdateView



app_name = 'filmspage'

urlpatterns = [
    path('', FilmListView.as_view(), name='film-list'),
    path('filmscreate/', FilmCreateView.as_view(), name='film-create'),
    path('filmscreate/<str:pk>/', FilmUpdateView.as_view(), name='film-update'),

]