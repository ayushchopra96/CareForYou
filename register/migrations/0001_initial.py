# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-12 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fbUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fbid', models.CharField(blank=True, max_length=40)),
                ('username', models.CharField(max_length=40, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]