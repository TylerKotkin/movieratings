# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_ratings', '0005_remove_rating_rater_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie_id',
        ),
        migrations.AddField(
            model_name='rating',
            name='rater',
            field=models.ForeignKey(default=0, to='get_ratings.Rater'),
            preserve_default=False,
        ),
    ]
