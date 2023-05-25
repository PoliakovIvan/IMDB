
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('i18n/', include('django.conf.urls.i18n')),
    path('auth/', include('apps.userlogin.urls', namespace='auth')),
    path('admin/', admin.site.urls),
    path('', include('apps.mainpage.urls', namespace='mainpage')),
    path('films/', include('apps.filmspage.urls', namespace='filmspage')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

