from typing import Any
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout, get_user_model
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.userlogin.forms import RegistrationForm, LoginForm

User = get_user_model()


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'userlogin/login.html'
    success_url = reverse_lazy('auth:account')

    def form_valid(self, form):
        login(self.request, User.objects.get(email=form.cleaned_data['email']))
        return super().form_valid(form)
        

class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'userlogin/register.html'
    success_url = reverse_lazy('auth:login')


class AccountView(LoginRequiredMixin, TemplateView ):
    template_name = 'userlogin/account.html'

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/auth/login')