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
                ('name', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('level', models.IntegerField()),
                ('mail', models.EmailField(default=b'hi@hi.hi', max_length=254)),
                ('phone', models.IntegerField(default=10086)),
                ('eat', models.BooleanField(default=False)),
            ],
        ),
    ]
