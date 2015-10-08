from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Rater

# Create your views here.


def movie_view(request):
    movies = Movie.objects.all()
    movie_strings = [str(movie) for movie in movies]
    return HttpResponse('<br>'.join(movie_strings))



def rater_view(request):
    raters = Rater.objects.all()
    rater_strings = [str(rater) for rater in raters]
    return HttpResponse('<br>'.join(rater_strings))
