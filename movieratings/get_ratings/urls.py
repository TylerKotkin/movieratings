from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^movie/(?P<movie_id>\d+)$', views.movie_view, name='movie_view'),
    url(r'^rater/(?P<rater_id>\d+)$', views.rater_view, name='rater_view'),
    url(r'^profile/(?P<rater_id>\d+)$', views.profile_view, name='profile_view'),
    url(r'^movie/new/(?P<movie_id>\d+)$', views.new_rating, name='new_rating'),
    url(r'^movie/edit/(?P<movie_id>\d+)$', views.edit_rating, name='edit_rating'),
    url(r'^movie/unrate/(?P<movie_id>\d+)$', views.remove_rating, name='remove_rating'),
    url(r'most', views.MostIndexView.as_view(), name='most_rated'),
    url(r'$', views.TopIndexView.as_view(), name='top_movies'),
]
