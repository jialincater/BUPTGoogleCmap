# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camper_mng', '0007_camper_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='camper',
            name='GDG',
            field=models.BooleanField(default=False),
        ),
    ]
