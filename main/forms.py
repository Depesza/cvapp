from django import forms
from .models import Dane


class DaneFrom(forms.ModelForm):
    class Meta:
        model = Dane
        fields = ['name', 'lastname', 'email']
