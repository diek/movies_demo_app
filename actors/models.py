from django.db import models
from movies.models import Movie


class Actor(models.Model):
    name = models.CharField(max_length=255)

    def get_movies(self):
        return Movie.objects.filter(cast=self)