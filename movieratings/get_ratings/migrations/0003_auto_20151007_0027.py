# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_ratings', '0002_movie_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='rater',
            new_name='rater_id',
        ),
    ]
