# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborationship',
            name='is_deleted',
            field=models.BooleanField(default=0),
            preserve_default=True,
        ),
    ]
