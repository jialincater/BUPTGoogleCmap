# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camper_mng', '0009_auto_20151026_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='camper',
            name='classNo',
            field=models.IntegerField(default=2012211122),
        ),
        migrations.AddField(
            model_name='camper',
            name='gender',
            field=models.CharField(default=b'\xe7\x94\xb7', max_length=2),
        ),
        migrations.AddField(
            model_name='camper',
            name='school',
            field=models.CharField(default=b'\xe4\xbf\xa1\xe6\x81\xaf\xe4\xb8\x8e\xe9\x80\x9a\xe4\xbf\xa1\xe5\xb7\xa5\xe7\xa8\x8b\xe5\xad\xa6\xe9\x99\xa2', max_length=20),
        ),
    ]
