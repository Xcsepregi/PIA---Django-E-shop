# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Istore', '0002_auto_20170529_1623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='objednavka',
            options={'verbose_name_plural': 'Objednavky'},
        ),
        migrations.RenameField(
            model_name='objednavka',
            old_name='stav',
            new_name='potvrdena',
        ),
        migrations.AddField(
            model_name='objednavka',
            name='zaplatenie',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
