from django.db import models

# Create your models here.


class Rater(models.Model):
    rater_id = models.PositiveIntegerField()
    # movies = models.ForeignKey(Movie)
    # rating = models.ForeignKey(Rating)
#
class Movie(models.Model):
    movie_name = models.CharField(max_length=150)
    movie_id = models.PositiveIntegerField()
    # rating = models.ForeignKey(Rating)

class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.FloatField()
