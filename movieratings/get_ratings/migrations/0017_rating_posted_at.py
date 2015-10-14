# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_ratings', '0016_auto_20151013_0348'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='posted_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
