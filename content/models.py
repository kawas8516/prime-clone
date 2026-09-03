"""Catalogue models for the Prime Video clone.

Author: kawas8516 <https://github.com/kawas8516>
"""

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


def current_year_plus_one():
    return timezone.now().year + 1


class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    releaseYear = models.IntegerField(
        validators=[
            # 1888: Roundhay Garden Scene, the earliest surviving film.
            MinValueValidator(1888, message="Release year can't be before 1888."),
            # +1 so an announced, not-yet-released title can still be entered.
            MaxValueValidator(
                current_year_plus_one,
                message="Release year can't be more than one year in the future.",
            ),
        ]
    )
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
