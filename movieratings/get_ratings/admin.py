from django.contrib import admin
from .models import Rater, Movie, Rating


class RaterAdmin(admin.ModelAdmin):
    list_display = ['rater_id']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie_name', 'movie_id']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['rater_id', 'movie', 'rating']

# Register your models here.
admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
