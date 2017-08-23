from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length = 180)
    author = models.CharField(max_length = 120)
    genre = models.CharField(max_length = 120)
    price = models.FloatField()

    def __str__(self):
        return self.name
