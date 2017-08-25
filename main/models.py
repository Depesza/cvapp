from django.db import models
# Create your models here.

class Dane(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=120)
    email = models.EmailField()
    # telefon = models.IntegerField()
