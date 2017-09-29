from django import forms
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    username = forms.CharField(label='Login:', error_messages={'unique': "Login jest już zajęty."})
    email = forms.CharField(label='E-mail:', error_messages={'invalid': "Proszę podać poprawny adres e-mail."})
    # , validators = [EmailValidator(message="Podano błędny adres e-mail")]
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

# class DaneForm(forms.ModelForm):
#     class Meta:
#         model = Document
#         fields = ('name', 'lastname', 'email', 'photo', 'street')