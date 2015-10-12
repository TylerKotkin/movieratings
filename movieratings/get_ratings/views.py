from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count, Avg
from .models import Movie, Rater
from django import forms

# Create your views here.


def top_movies(request):
    popular_movies = Movie.objects.annotate(num_ratings=Count('rating')) \
                                  .filter(num_ratings__gte=50)

    movies = popular_movies.annotate(Avg('rating__stars')) \
                           .order_by('-rating__stars__avg')[:20]
    return render(request,
                  'get_ratings/top_movies.html',
                  {'movies': movies})


def movie_view(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    # if request.method == 'POST':
    #     if request.user.is_authenticated():
    #             form = RatingForm(request.POST)
    #             if form.is_valid():
    #                 Rating.create_rating(movie=movie, rater=request.user.rater, stars=request.POST['rating'])
    #
    #     else:
    #         return redirect('user_login')
    return render(request,
                  'get_ratings/movies.html',
                  {'movie': movie})


def rater_view(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    # ratings = rater.rating_set.all()
    # return HttpResponse(rater)
    movie_ratings = []
    for rating in rater.rating_set.all():
        movie_ratings.append({
            'movie': rating.movie,
            'stars': '\u2605' * rating.stars,
        })
    return render(request,
                  'get_ratings/users.html',
                  {'rater': rater,
                   'movie_ratings': movie_ratings})
