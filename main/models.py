from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your models here.

class Dane(models.Model):
    owner = models.ForeignKey(User, unique=False, default='', on_delete=models.CASCADE)
    name = models.CharField(u'Imię', max_length=30)
    lastname = models.CharField(u'Nazwisko', max_length=120)
    email = models.EmailField()
    photo = models.FileField(default='')
    street = models.CharField(u'Ulica i numer mieszkania', max_length=50, default='')


    def get_absolute_url(self):
        return reverse('cvpers', kwargs={'pk': self.pk})
#