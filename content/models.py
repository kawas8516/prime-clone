from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    releaseYear = models.IntegerField()
    rating = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    director = models.CharField(max_length=100)
    cast = models.TextField()
    description = models.TextField()
    bannerUrl = models.URLField()
    trailer = models.URLField()

    class Meta:
        # The app was renamed from "app" to "content"; keeping the original
        # table name preserves the existing rows.
        db_table = "app_movie"

    def __str__(self):
        return self.name
