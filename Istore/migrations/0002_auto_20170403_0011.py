# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Istore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podlozky',
            name='druh',
        ),
        migrations.AlterField(
            model_name='notebook',
            name='cena',
            field=models.DecimalField(max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notebook',
            name='uhlopriecka',
            field=models.DecimalField(max_digits=3, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='podlozky',
            name='vyrobca',
            field=models.CharField(max_length=24),
            preserve_default=True,
        ),
    ]
