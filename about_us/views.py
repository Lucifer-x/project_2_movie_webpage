from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, ComingMovie


# Create your views here.
def index(request):
    return render(request, 'about-us.html')


def movies(request):
    movie_all = Movie.objects.all()
    coming_movie_all = ComingMovie.objects.all()
    return render(request, 'movies.html', {'Movies': movie_all, 'ComingMovies': coming_movie_all})
