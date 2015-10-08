from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^movies/', views.movie_view),
    url(r'^raters/', views.rater_view),
]
