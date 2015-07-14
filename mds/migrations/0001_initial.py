# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemTable',
            fields=[
                ('table_id', models.IntegerField(serialize=False, primary_key=True)),
                ('table_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('create_table_info', models.TextField()),
                ('column_description', models.TextField()),
                ('blood_relation', models.CharField(max_length=200)),
            ],
        ),
    ]
