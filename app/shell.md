# Django Setup & Database Population Guide

## Step 0: Create Database Schema

# Create migration files based on model changes (detects changes in models.py)

```python
python manage.py makemigrations
```
This cmd will create files such as app\migrations\0001_initial.py in sequential naming on every run
# Apply migrations to the database (creates tables in SQLite)

```python
python manage.py migrate
```

## Step 1: Open Django Interactive Shell

# Launches an interactive Python shell with Django context configured

```python
python3 manage.py shell
```

## Step 2: Import the Movie Model

# Imports the Movie model class to interact with the movies table

```python
from app.models import Movie
```

## Step 3: Import Movies Data

# Import the movies_data list from the movies.py file containing all movie records

```python
from app.movies import movies_data
```

## Step 4: Populate Database with Movie Records

Loops through each movie in movies_data and creates a Movie object in the database. Each field maps to the corresponding column in the Movie model.

```python
for movie in movies_data:
    Movie.objects.create(
        name=movie["name"],
        genre=movie["genre"],
        releaseYear=movie["releaseYear"],
        rating=movie["rating"],
        duration=movie["duration"],
        director=movie["director"],
        cast=movie["cast"],
        description=movie["description"],
        bannerUrl=movie["bannerUrl"],
        trailer=movie["trailer"],
    )
```

## Step 5: Verify Data in Database

# Retrieve and display all Movie records from the database

```python
Movie.objects.all()
```

# Retrieve specific movies using filters (examples)

Movie.objects.filter(genre="Action") # Get all action movies
Movie.objects.get(id=1) # Get movie with id=1

## Step 6: Display Movies in Views (app/views.py)

```python
from django.shortcuts import render
from .models import Movie

# View function to display all movies on the home page
def home(request):
    # Query all Movie objects from the database using ORM
    movies = Movie.objects.all()

    # Render home.html template with movies data in context
    # The 'movies' list is available in the template as {{ movies }}
    return render(request, 'home.html', {'movies': movies})
```

### Template Usage in home.html

```html
<!-- Loop through movies and display each one -->
{% for movie in movies %}
<div class="movie-card">
  <h3>{{ movie.name }}</h3>
  <p>Genre: {{ movie.genre }}</p>
  <p>{{ movie.description }}</p>
  <img src="{{ movie.bannerUrl }}" alt="{{ movie.name }}" />
  <a href="{{ movie.trailer }}">Watch Trailer</a>
</div>
{% endfor %}
```
