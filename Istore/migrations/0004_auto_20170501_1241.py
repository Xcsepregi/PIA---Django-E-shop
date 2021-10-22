# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Istore', '0003_auto_20170501_1238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='objednavka',
            options={'verbose_name': 'Objednavka', 'verbose_name_plural': 'Objednavky'},
        ),
        migrations.AlterModelOptions(
            name='tovar',
            options={'verbose_name': 'Tovar', 'verbose_name_plural': 'Tovary'},
        ),
    ]
