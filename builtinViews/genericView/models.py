from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Books(models.Model):
    name = models.CharField(max_length = 180)
    author = models.CharField(max_length = 150)
    genre = models.CharField(max_length = 120)
    price = models.IntegerField()

    def get_absolute_url(self):
        return reverse("books")

    def __str__(self):
        return self.name
