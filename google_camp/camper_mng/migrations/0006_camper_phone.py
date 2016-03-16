# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camper_mng', '0005_auto_20151013_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='camper',
            name='phone',
            field=models.IntegerField(default=10086),
        ),
    ]
