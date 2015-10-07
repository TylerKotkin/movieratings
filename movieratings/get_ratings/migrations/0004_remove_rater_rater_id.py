# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_ratings', '0003_auto_20151007_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rater',
            name='rater_id',
        ),
    ]
