# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_ratings', '0008_auto_20151008_0206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='user',
            new_name='rater',
        ),
    ]
