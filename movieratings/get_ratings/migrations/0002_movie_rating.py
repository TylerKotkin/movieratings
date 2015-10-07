# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_ratings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('movie_name', models.CharField(max_length=150)),
                ('movie_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('rating', models.FloatField()),
                ('movie', models.ForeignKey(to='get_ratings.Movie')),
                ('rater', models.ForeignKey(to='get_ratings.Rater')),
            ],
        ),
    ]
