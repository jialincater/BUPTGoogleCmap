# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camper_mng', '0003_auto_20151012_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='camper',
            name='canRuby',
            field=models.BooleanField(default=False),
        ),
    ]
