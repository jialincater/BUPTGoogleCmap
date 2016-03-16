# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camper_mng', '0002_auto_20151012_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='camper',
            name='canC',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='camper',
            name='canHTML',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='camper',
            name='canJAVA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='camper',
            name='canJS',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='camper',
            name='canPHP',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='camper',
            name='canPython',
            field=models.BooleanField(default=False),
        ),
    ]
