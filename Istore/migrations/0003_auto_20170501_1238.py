# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Istore', '0002_auto_20170403_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objednavka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cena', models.DecimalField(max_digits=8, decimal_places=2)),
                ('stav', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Polozka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pocet', models.SmallIntegerField(max_length=2)),
                ('cena', models.DecimalField(max_digits=8, decimal_places=2)),
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
                ('parametre', models.CharField(max_length=120)),
                ('cena', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
            options={
                'verbose_name': 'Tovar',
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
                ('objednavky', models.ManyToManyField(to='Istore.Tovar')),
            ],
            options={
                'verbose_name': 'Zakaznik',
                'verbose_name_plural': 'Zakaznici',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Myska',
        ),
        migrations.DeleteModel(
            name='Notebook',
        ),
        migrations.DeleteModel(
            name='Podlozky',
        ),
        migrations.AddField(
            model_name='polozka',
            name='tovar',
            field=models.ForeignKey(related_name='pridany_tovar', to='Istore.Tovar'),
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
            field=models.ManyToManyField(related_name='objednane_polozky', to='Istore.Polozka'),
            preserve_default=True,
        ),
    ]
