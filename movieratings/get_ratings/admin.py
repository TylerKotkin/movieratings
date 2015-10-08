from django.contrib import admin
from .models import Rater, Movie, Rating


class RaterAdmin(admin.ModelAdmin):
    list_display = ['id']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['rater', 'movie', 'stars']

# Register your models here.
admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
