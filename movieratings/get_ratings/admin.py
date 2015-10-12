from django.contrib import admin
from .models import Rater, Movie, Rating


class RatingAdmin(admin.ModelAdmin):
    list_display = ['rater', 'movie', 'stars']


class RaterAdmin(admin.ModelAdmin):
    list_display = ['id']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

# Register your models here.

admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
