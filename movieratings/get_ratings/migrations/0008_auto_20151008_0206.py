# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_ratings', '0007_auto_20151008_0122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='movie_name',
            new_name='title',
        ),
    ]
