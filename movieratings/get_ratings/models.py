from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Rater(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'


    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    zipcode = models.CharField(max_length=5)
    age = models.PositiveIntegerField()
    occupation = models.CharField(max_length=40)
    user = models.OneToOneField(User, null=True)

    def __str__(self):
        return 'user id: {}.'.format(self.id)
        # return 'user id: {}. {} {} {} {} '.format(self.id, self.gender, self.zipcode, self.age, self.occupation)


class Movie(models.Model):
    title = models.CharField(max_length=150)
    # movie_id = models.PositiveIntegerField()

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('stars')) ['stars__avg']


    def __str__(self):
        return '{}'.format(self.title)


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    stars = models.PositiveIntegerField()

    def __str__(self):
        return 'user {} gave {} {} stars.'.format(self.rater, self.movie, self.stars)
