from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length = 180)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.name
