# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Istore', '0003_auto_20170530_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objednavka',
            name='potvrdena',
        ),
    ]
