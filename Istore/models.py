#coding: utf-8
from django.db import models
from hash_pwd import hash_pwd

class Kategoria(models.Model):
	kategoria=models.CharField(max_length=24)

	def __unicode__(self):
		return u"%s " %(self.kategoria)

	class Meta:
		verbose_name_plural=u"Kategorie"

class Tovar(models.Model):
    popis = models.CharField(max_length=60)
    vyrobca = models.CharField(max_length=25)
    cena = models.DecimalField(max_digits=6, decimal_places=2)
    kategoria=models.ForeignKey(Kategoria)

    class Meta:
        verbose_name = u'Tovar'
        verbose_name_plural = u'Tovary'

    def __unicode__(self):
        return u'%s %s %.2f' %(self.popis,self.vyrobca,self.cena)


class Zakaznik(models.Model):
    meno = models.CharField(max_length=12)
    priezvisko = models.CharField(max_length=16)
    adresa = models.CharField(max_length=40)
    email = models.CharField(max_length=25)
    password_hash=models.CharField(max_length=32,null=True)

    def __unicode__(self):
        return u'%s %s' % (self.meno, self.priezvisko)

    def check_pwd(self,pwd):

        return hash_pwd(pwd)==self.password_hash

class Objednavka(models.Model):
	zakaznik = models.ForeignKey(Zakaznik)
	zaplatenie=models.BooleanField(default=False)

	class Meta:
		verbose_name_plural = u'Objednavky'

class Polozka(models.Model):
    tovar = models.ForeignKey(Tovar)
    pocet = models.PositiveIntegerField(max_length=2)
    objednavka=models.ForeignKey(Objednavka)

    def __unicode__(self):
		return u" %s %d " %(self.tovar,self.pocet)

    class Meta:
        verbose_name_plural = u'Polozky'
