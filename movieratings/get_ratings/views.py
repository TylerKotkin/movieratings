from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count, Avg
from .models import Movie, Rater

# Create your views here.


def movie_view(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    # ratings = '{}: Average Rating: {}'.format(movie.title, movie.average_rating())
    # return HttpResponse(ratings)
    return render(request,
                  'get_ratings/movies.html',
                  {'movie': movie})




def top_movies(request):
    # movies = Movie.objects.annotate(Avg('rating__stars')).order_by('-rating__stars__avg')[:20]
    # movies = Movie.objects.order_by('-rating')[:20]
    # top_20 = [str(movie) for movie in movies]
    # return HttpResponse('<br>'.join(top_20))
    popular_movies = Movie.objects.annotate(num_ratings=Count('rating')) \
                                  .filter(num_ratings__gte=50)

    movies = popular_movies.annotate(Avg('rating__stars')) \
                           .order_by('-rating__stars__avg')[:20]

    most_movies = Movie.objects.annotate(num_ratings=Count('rating')).order_by('-num_ratings')[:20]

    return render(request,
                  'get_ratings/top_movies.html',
                  {'movies': movies,
                  'most_movies': most_movies})


# def most_movies(request):
#     # most_movies = Movie.objects.annotate(num_ratings=Count('rating')).order_by('-rating')[:20]
#     most_movies = Movie.objects.order_by('-rating')[:20]
#     return render(request,
#                   'get_ratings/top_movies.html',
#                   {'most_movies': most_movies})


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
