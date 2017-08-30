from __future__ import unicode_literals

from django.db import models


class Student(models.Model):
    name = models.CharField(max_length = 180)
    program = models.CharField(max_length = 80)
    year = models.IntegerField()
    cgpa = models.FloatField()

    def __str__(self):
        return self.name
