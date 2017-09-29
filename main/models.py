from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.

class Dane(models.Model):
    owner = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    name = models.CharField('Imię', max_length=30)
    lastname = models.CharField('Nazwisko', max_length=120)
    email = models.EmailField('E-mail', error_messages={'invalid': "Proszę podać poprawny adres e-mail."})
    photo = models.FileField('Zdjęcie', upload_to='documents/')
    street = models.CharField('Ulica i numer mieszkania', max_length=50)

    def get_absolute_url(self):
        return reverse('cvdispdef', kwargs={'pk': self.pk})


class DaneForm(ModelForm):
    class Meta:
        model = Dane
        exclude = ['owner']