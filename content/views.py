from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MovieForm
from .models import Movie


def staff_required(view):
    """Allow only staff/superusers past this point.

    Anonymous users are sent to the login page; a logged-in non-staff user
    gets a 403 rather than being bounced back to a login form they have
    already completed.
    """

    @wraps(view)
    @login_required
    def wrapper(request, *args, **kwargs):
        if not (request.user.is_staff or request.user.is_superuser):
            raise PermissionDenied
        return view(request, *args, **kwargs)

    return wrapper


@login_required
def home(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {"movies": movies})


@staff_required
def addMovie(request):
    form = MovieForm()
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manage_movies")
    return render(request, "add_movie.html", {"form": form, "title": "Add Title"})


@staff_required
def manageMovies(request):
    movies = Movie.objects.all().order_by("-releaseYear")
    return render(request, "manage_movies.html", {"movies": movies})


@staff_required
def editMovie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    form = MovieForm(instance=movie)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect("manage_movies")
    return render(request, "add_movie.html", {"form": form, "title": "Edit Title"})


@staff_required
def deleteMovie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        movie.delete()
        return redirect("manage_movies")
    return render(request, "delete_movie.html", {"movie": movie})
