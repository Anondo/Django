# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-23 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180)),
                ('author', models.CharField(max_length=120)),
                ('genre', models.CharField(max_length=30)),
                ('price', models.FloatField()),
            ],
        ),
    ]
