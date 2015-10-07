# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_ratings', '0004_remove_rater_rater_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='rater_id',
        ),
    ]
