# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camper_mng', '0004_camper_canruby'),
    ]

    operations = [
        migrations.AddField(
            model_name='camper',
            name='canAe',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='camper',
            name='canAu',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='camper',
            name='canFCP',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='camper',
            name='canPr',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='camper',
            name='canPs',
            field=models.BooleanField(default=False),
        ),
    ]
