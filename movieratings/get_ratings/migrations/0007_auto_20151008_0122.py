# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_ratings', '0006_auto_20151007_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='rating',
            new_name='stars',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='rater',
            new_name='user',
        ),
        migrations.AddField(
            model_name='rater',
            name='age',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rater',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rater',
            name='occupation',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rater',
            name='zipcode',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
