# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_ratings', '0014_auto_20151013_0341'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='review',
            field=models.CharField(null=True, blank=True, max_length=400),
        ),
    ]
