# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingress', '0003_agent_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='join',
            field=models.BooleanField(default=False),
        ),
    ]
