# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_dane_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dane',
            name='photo',
            field=models.FileField(default='test', upload_to=''),
        ),
    ]