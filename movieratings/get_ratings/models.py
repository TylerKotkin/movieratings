from django.db import models

# Create your models here.


class Rater(models.Model):
    pass
    # rater_id = models.PositiveIntegerField()
    #
    def __str__(self):
        return 'user id: {}'.format(self.id)


class Movie(models.Model):
    movie_name = models.CharField(max_length=150)
    # movie_id = models.PositiveIntegerField()

    def __str__(self):
        return self.movie_name


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.FloatField()

    def __str__(self):
        return 'user {} gave {} {} stars.'.format(self.rater, self.movie, self.rating)
