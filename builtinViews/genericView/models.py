from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Books(models.Model):
    name = models.CharField(max_length = 180)
    author = models.CharField(max_length = 150)
    genre = models.CharField(max_length = 120)
    price = models.IntegerField()

    def __str__(self):
        return self.name
