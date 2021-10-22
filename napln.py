#!/usr/bin/env python2
# coding:utf-8

import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path=[os.path.realpath('.')]+sys.path
os.environ['DJANGO_SETTINGS_MODULE']='InternetStore.settings'
application=get_wsgi_application()

from Istore.models import Tovar
from Istore.models import Kategoria

Kategoria.objects.all().delete()
Tovar.objects.all().delete()

f=open('kategorie.dat')
for line in f:
	kat=line[:-1]
	t=Kategoria.objects.create(kategoria=kat)
	t.save()

k=Kategoria.objects.get(kategoria="Elektro")

f1=open('elektro.dat')
for line in f1:
    line=line.strip()
    p,v,c=line.split(',')
    tovar=Tovar(popis=p, vyrobca=v, cena=c,kategoria=k)
    tovar.save()
f1.close()

k=Kategoria.objects.get(kategoria="Oblečenie")

f2=open('saty.dat')
for line in f2:
    line=line.strip()
    p,v,c=line.split(',')
    tovar=Tovar(popis=p, vyrobca=v, cena=c,kategoria=k)
    tovar.save()
f2.close()

k=Kategoria.objects.get(kategoria="Školské potreby")

f3=open('skola.dat')
for line in f3:
    line=line.strip()
    p,v,c=line.split(',')
    tovar=Tovar(popis=p, vyrobca=v, cena=c,kategoria=k)
    tovar.save()
f3.close()
