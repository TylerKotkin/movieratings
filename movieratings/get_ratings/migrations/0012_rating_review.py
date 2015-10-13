# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_ratings', '0011_rater_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='review',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
