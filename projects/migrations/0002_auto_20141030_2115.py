# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_private',
            field=models.BooleanField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_deleted',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='is_deleted',
            field=models.BooleanField(default=0),
        ),
    ]
