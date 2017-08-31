from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your models here.

class Dane(models.Model):
    username = User.username
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=120)
    email = models.EmailField()
    photo = models.FileField(default='test')
    street = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('cvpers', kwargs={'pk': self.pk})
#