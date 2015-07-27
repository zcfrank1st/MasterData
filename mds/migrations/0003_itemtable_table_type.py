# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mds', '0002_auto_20150714_0543'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtable',
            name='table_type',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
