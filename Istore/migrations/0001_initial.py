# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objednavka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stav', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Objednavka',
                'verbose_name_plural': 'Objednavky',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Polozka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pocet', models.PositiveIntegerField(max_length=2)),
            ],
            options={
                'verbose_name': 'Polozka',
                'verbose_name_plural': 'Polozky',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('popis', models.CharField(max_length=60)),
                ('vyrobca', models.CharField(max_length=25)),
                ('cena', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
            options={
                'verbose_name': 'Tovar',
                'verbose_name_plural': 'Tovary',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zakaznik',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meno', models.CharField(max_length=12)),
                ('priezvisko', models.CharField(max_length=16)),
                ('adresa', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Zakaznik',
                'verbose_name_plural': 'Zakaznici',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='polozka',
            name='tovar',
            field=models.ForeignKey(related_name='tovary', to='Istore.Tovar'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objednavka',
            name='zakaznik',
            field=models.ForeignKey(to='Istore.Zakaznik'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objednavka',
            name='zoznam_poloziek',
            field=models.ForeignKey(related_name='polozky', to='Istore.Polozka'),
            preserve_default=True,
        ),
    ]
