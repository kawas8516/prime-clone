from urllib import request

from django.shortcuts import render
from .movies import movies_data
from app import movies
from .models import Movie

# Create your views here.
# define home function


def home(request):
    movies=Movie.objects.all()
    print(len(movies))
    context = {
        'movies': movies
    }
    return render(request, 'index.html', context)