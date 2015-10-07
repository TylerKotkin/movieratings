from django.db import models

# Create your models here.


class Rater(models.Model):
    pass
    # rater_id = models.PositiveIntegerField()
    #
    # def __str__(self):
    #     return 'Rater ID: {}'.format(self.rater_id)


class Movie(models.Model):
    movie_name = models.CharField(max_length=150)
    movie_id = models.PositiveIntegerField()

    def __str__(self):
        return '{}: {}'.format(self.movie_name, self.movie_id)


class Rating(models.Model):
    rater_id = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.FloatField()

    def __str__(self):
        return self.rating
