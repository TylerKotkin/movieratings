from django.contrib import admin
from .models import Rater, Movie, Rating


class RaterAdmin(admin.ModelAdmin):
    list_display = ['id']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie_name']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['rater', 'movie', 'rating']

# Register your models here.
admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
