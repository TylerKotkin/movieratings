from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Rater

# Create your views here.


def movie_view(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    ratings = '{}: Average Rating: {}'.format(movie.title, movie.average_rating())
    return HttpResponse(ratings)
    # movies = Movie.objects.all()
    # movie_strings = [str(movie) for movie in movies]
    # return HttpResponse('<br>'.join(movie_strings))




def top_movies(request):
    movies = Movie.objects.order_by('-rating')[:20]
    top_20 = [str(movie) for movie in movies]
    return HttpResponse('<br>'.join(top_20))



def rater_view(request, user_id):
    rater = Rater.objects.get(pk=user_id)
    # ratings = rater.rating_set.all()
    return HttpResponse(rater)

    # raters = Rater.objects.all()
    # rater_strings = [str(rater) for rater in raters]
    # return HttpResponse('<br>'.join(rater_strings))
