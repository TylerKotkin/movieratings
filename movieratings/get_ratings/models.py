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

    def __str__(self):
        return 'user id: {}'.format(self.id)


class Movie(models.Model):
    movie_name = models.CharField(max_length=150)
    # movie_id = models.PositiveIntegerField()

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']

    def __str__(self):
        return self.movie_name


class Rating(models.Model):
    user = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    stars = models.FloatField()

    def __str__(self):
        return 'user {} gave {} {} stars.'.format(self.user, self.movie, self.stars)


def load_ml_data():
    import csv
    import json
    import re

    users = []

    with open('ml-1m/users.dat') as f:
        reader = csv.DictReader(f,
                                filednames='',
                                delimiter='')
        for row in reader:
            user = {
                'fields': {
                    'gender': row['Gender'],
                    'age': row['Age'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code'],
                },
                'model': 'get_ratings.Rater',
                'pk': int(row['UserID']),
            }

            users.append(user)

    with open('users.json', 'w') as f:
        f.write(json.dumps(users))

    # print(json.dumps(users, sort_keys=True, indent=4, separators=(',', ': ')))
