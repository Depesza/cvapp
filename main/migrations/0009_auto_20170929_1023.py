# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-29 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20170929_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dane',
            name='photo',
            field=models.FileField(upload_to='media'),
        ),
    ]