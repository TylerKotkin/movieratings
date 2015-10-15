from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count, Avg
from .models import Movie, Rater, Rating

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import RatingForm, EditForm
from django.views import generic



# Create your views here.


class TopIndexView(generic.ListView):
    template_name = 'get_ratings/top_movies.html'
    context_object_name = 'movies'
    paginate_by = 20

    def get_queryset(self):
        movies = Movie.objects.annotate(num_ratings=Count('rating')) \
                                      .filter(num_ratings__gte=50)
        return movies.annotate(Avg('rating__stars')) \
                               .order_by('-rating__stars__avg')


class MostIndexView(generic.ListView):
    template_name = 'get_ratings/most_movies.html'
    context_object_name = 'most_movies'
    paginate_by = 20

    def get_queryset(self):
        return Movie.objects.annotate(num_ratings=Count('rating')).order_by('-num_ratings')


class RaterDetailView(generic.DetailView):
    model = Rater
    template = 'get_ratings/profile_detail.html'


def movie_view(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    try:
        rater_stars = request.user.rater.rating_set.filter(movie_id=movie_id)[0].stars
    except:
        rater_stars = ''
    return render(request,
                  'get_ratings/movie_detail.html',
                  {'movie': movie,
                   'rater_stars': rater_stars,
                   })


@login_required
def new_rating(request, movie_id):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.rater = request.user.rater
            rating.movie = Movie.objects.get(pk=movie_id)
            rating.posted_at = datetime.now()
            rating.save()
            messages.add_message(request, messages.SUCCESS, 'Your rating has been saved')
            return redirect('movie_detail', rating.movie.pk)

    else:
        form = RatingForm()
    return render(request,
                  'get_ratings/new.html',
                  {'form': form, 'movie': Movie.objects.get(pk=movie_id)})


@login_required
def edit_rating(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.rating_set.filter(rater=request.user.rater).delete()
    return redirect('new_rating', movie_id)


@login_required
def remove_rating(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.rating_set.filter(rater=request.user.rater).delete()
    messages.add_message(request, messages.SUCCESS, 'Your rating has been deleted')
    return redirect('movie_detail', movie_id)
