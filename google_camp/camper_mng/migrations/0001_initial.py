# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camper',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('student_id', models.IntegerField(serialize=False, primary_key=True)),
                ('grade', models.CharField(max_length=100)),
            ],
        ),
    ]
