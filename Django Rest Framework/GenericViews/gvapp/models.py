from __future__ import unicode_literals

from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length = 180)
    body = models.TextField()
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
