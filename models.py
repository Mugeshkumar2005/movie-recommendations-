from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    actor = models.CharField(max_length=200, blank=True, null=True)
    director = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title