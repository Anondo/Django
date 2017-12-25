from __future__ import unicode_literals

from django.db import models

class Subscriber(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    email = models.EmailField(max_length = 100)

    def __str__(self):
        return self.name
