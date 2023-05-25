from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(label=_('Email Address'))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)

    def clean(self):
        user = User.objects.filter(email=self.cleaned_data['email']).first()

        if user is None:
            raise forms.ValidationError("Unknown user or password")

        if not user.check_password(self.cleaned_data['password']):
            raise forms.ValidationError("Unknown user or password")


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password2 != password:
            raise forms.ValidationError('Password mismath')
        return password2
    
    def save(self, is_commit=True):
        user = super().save(is_commit)
        if is_commit:
            user.set_password(self.cleaned_data['password'])
            user.save()
        return user

