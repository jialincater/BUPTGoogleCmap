# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camper_mng', '0008_camper_gdg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camper',
            name='phone',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='camper',
            name='student_id',
            field=models.IntegerField(),
        ),
    ]
