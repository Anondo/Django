from __future__ import unicode_literals

from django.db import models

class Account(models.Model):
    name = models.CharField(max_length = 180)
    type = models.CharField(max_length = 80)
    balance = models.FloatField()


    def __str__(self):
        return self.name
