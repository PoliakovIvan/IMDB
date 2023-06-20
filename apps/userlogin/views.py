from typing import Any
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login, logout, get_user_model
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, View, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.userlogin.forms import RegistrationForm, LoginForm
import django.contrib.auth.tokens
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
import uuid


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

    def form_valid(self, form):
        user = form.save()

        # Збереження нового користувача
        user.is_active = False  # Обліковий запис неактивний до підтвердження пошти
        
        confirmation_code = str(uuid.uuid4())
        confirmation_link = self.request.build_absolute_uri(reverse('auth:confirm_email', kwargs={'code': confirmation_code}))
        user.confirmation_code = confirmation_code
        user.save()
        # Відправка електронного листа для підтвердження
        html_message = render_to_string('userlogin/confirmation_email.html', {
            'user': user,          
            'confirmation_link': confirmation_link,
        })

        # Створити об'єкт EmailMessage з HTML-повідомленням
        email = EmailMessage(
            'Підтвердження реєстрації',
            html_message,
            'your_email@example.com',
            [user.email],
        )

        # Додати необхідні заголовки для відправлення HTML-повідомлення
        email.content_subtype = 'html'

        # Надіслати електронне повідомлення
        email.send()

        # Перенаправлення на сторінку успішної реєстрації або іншу сторінку
        return self.registration_success(self.request)

    


class AccountView(LoginRequiredMixin, TemplateView ):
    template_name = 'userlogin/account.html'


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/auth/login')
    

class EmailConfirmationView(View):
    def get(self, request, code):
        user = get_object_or_404(User, confirmation_code=code)
        user.is_active = True
        user.is_email_verified = True
        user.save()
        return render(request, 'userlogin/confirmation_success.html')

