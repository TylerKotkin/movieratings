# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_ratings', '0009_auto_20151008_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='stars',
            field=models.PositiveIntegerField(),
        ),
    ]
