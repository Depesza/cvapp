# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-29 11:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20170929_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dane',
            name='email',
            field=models.EmailField(error_messages={'invalid': 'Proszę podać poprawny adres e-mail.'}, max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='dane',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dane',
            name='photo',
            field=models.FileField(upload_to='documents/', verbose_name='Zdjęcie'),
        ),
        migrations.AlterField(
            model_name='dane',
            name='street',
            field=models.CharField(max_length=50, verbose_name='Ulica i numer mieszkania'),
        ),
    ]