from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^movie/(?P<movie_id>\d+)$', views.movie_view, name='movie_detail'),
    url(r'^profile/(?P<pk>\d+)$', views.RaterDetailView.as_view(), name='profile_view'),
    url(r'^movie/new/(?P<movie_id>\d+)$', views.new_rating, name='new_rating'),
    url(r'^movie/edit/(?P<movie_id>\d+)$', views.edit_rating, name='edit_rating'),
    url(r'^movie/unrate/(?P<movie_id>\d+)$', views.remove_rating, name='remove_rating'),
    url(r'most', views.MostIndexView.as_view(), name='most_rated'),
    url(r'$', views.TopIndexView.as_view(), name='top_movies'),
]
