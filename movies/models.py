from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    cast = models.ManyToManyField('actors.Actor')
