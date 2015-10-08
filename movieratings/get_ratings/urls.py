from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^movies/(?P<movie_id>\d+)$', views.movie_view),
    url(r'^raters/(?P<user_id>\d+)$', views.rater_view),
    url(r'^top/', views.top_movies),
]
