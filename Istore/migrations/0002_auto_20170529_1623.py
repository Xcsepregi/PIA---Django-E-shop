# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Istore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kategoria', models.CharField(max_length=24)),
            ],
            options={
                'verbose_name_plural': 'Kategorie',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='polozka',
            options={'verbose_name_plural': 'Polozky'},
        ),
        migrations.AlterModelOptions(
            name='zakaznik',
            options={},
        ),
        migrations.RemoveField(
            model_name='objednavka',
            name='zoznam_poloziek',
        ),
        migrations.AddField(
            model_name='polozka',
            name='objednavka',
            field=models.ForeignKey(default=0, to='Istore.Objednavka'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tovar',
            name='kategoria',
            field=models.ForeignKey(default=2, to='Istore.Kategoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zakaznik',
            name='password_hash',
            field=models.CharField(max_length=32, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='polozka',
            name='tovar',
            field=models.ForeignKey(to='Istore.Tovar'),
            preserve_default=True,
        ),
    ]
