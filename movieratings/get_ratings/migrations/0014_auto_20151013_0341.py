# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_ratings', '0013_auto_20151013_0338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='review',
        ),
        migrations.AlterField(
            model_name='rating',
            name='stars',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]),
        ),
    ]
