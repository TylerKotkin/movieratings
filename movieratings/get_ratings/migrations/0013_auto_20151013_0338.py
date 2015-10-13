# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_ratings', '0012_rating_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='stars',
            field=models.IntegerField(max_length=1, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]),
        ),
    ]
