from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "genre", "releaseYear", "rating", "director")
    search_fields = ("name", "genre", "director")
