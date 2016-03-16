# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingress', '0002_auto_20151024_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='password',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
