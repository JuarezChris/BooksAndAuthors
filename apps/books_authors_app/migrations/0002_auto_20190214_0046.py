# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-14 00:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='books', to='books_authors_app.Author'),
        ),
    ]
