from django.urls import path

from apps.userlogin.views import LoginView, AccountView, LogoutView, RegisterView

app_name = 'userlogin'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('account/', AccountView.as_view(), name='account'),
    path('register/', RegisterView.as_view(), name='register'),
]