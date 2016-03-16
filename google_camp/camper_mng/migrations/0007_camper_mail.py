# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camper_mng', '0006_camper_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='camper',
            name='mail',
            field=models.EmailField(default=b'hi@hi.hi', max_length=254),
        ),
    ]
