from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(label='Login:')
    email = forms.CharField(label='E-mail:')
    password = forms.CharField(label='Hasło:', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(label='Login:')
    password = forms.CharField(label='Hasło:', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
