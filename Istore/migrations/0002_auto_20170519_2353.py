# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Istore', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zakaznik',
            options={},
        ),
        migrations.AddField(
            model_name='zakaznik',
            name='password_hash',
            field=models.CharField(max_length=32, null=True),
            preserve_default=True,
        ),
    ]
