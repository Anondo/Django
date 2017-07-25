from __future__ import unicode_literals

from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    name = models.CharField(max_length = 150)
    age = models.IntegerField()
    institution = models.CharField(max_length = 150)
    program = models.CharField(max_length = 150)
    bio = models.TextField(null = True)

    def __str__(self):
        return self.name
