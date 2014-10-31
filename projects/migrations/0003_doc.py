# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20141030_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('people', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('organization', models.CharField(max_length=200)),
                ('misc', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=200)),
                ('dataset', models.ForeignKey(to='projects.DataSet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
