from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Dane(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=120)
    email = models.EmailField()
    photo = models.FileField(default='44')

    def get_absolute_url(self):
        return reverse('cvpers', kwargs={'pk': self.pk})
