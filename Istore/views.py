# coding:utf-8
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import RequestContext,Context,loader
from django import forms
from models import *
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from functools import wraps
from django.contrib import messages

class IstoreContext(RequestContext):

    def __init__(self,request,d={}):

        if "prihlaseny_email" in request.session:
            d["prihlaseny_email"]=Zakaznik.objects.get(
                meno=request.session["prihlaseny_email"]
                )
        RequestContext.__init__(self,request,d)

def kontrola_prihlasenosti(view):

    @wraps(view)
    def view_ret(request,*args,**kwargs):
        if "prihlaseny_email" not in request.session:
            return HttpResponseRedirect(reverse("Istore.views.front_page"))
        else:
            return view(request,*args,**kwargs)

    return view_ret

class RegForm(forms.Form):
    meno=forms.CharField(max_length=12)
    priezvisko=forms.CharField(max_length=16)
    adresa=forms.CharField(max_length=40)
    email=forms.CharField(max_length=30)
    heslo=forms.CharField(max_length=32,widget=forms.PasswordInput)
    heslo2=forms.CharField(max_length=32,widget=forms.PasswordInput)

class LoginForm(forms.Form):
    email=forms.CharField(max_length=30)
    heslo=forms.CharField(max_length=32,widget=forms.PasswordInput)

class KosikForm(forms.Form):
    pocet=forms.IntegerField(min_value=1)

class SearchForm(forms.Form):
    retazec=forms.CharField(max_length=60)

def front_page(request):
    kat=Kategoria.objects.all()
    t = loader.get_template("front_page.html")
    c=IstoreContext(request,{'kat':kat})
    return HttpResponse(t.render(c))

def podmienky(request):
    t = loader.get_template("podmienky.html")
    c=IstoreContext(request,{})
    return HttpResponse(t.render(c))

def kontakt(request):
    t = loader.get_template("kontakt.html")
    c=IstoreContext(request,{})
    return HttpResponse(t.render(c))

def registracia(request):
	error=None
	if request.method=='POST':
		form=RegForm(request.POST)
		if form.is_valid():
			meno= form.cleaned_data["meno"]
			priezvisko= form.cleaned_data["priezvisko"]
			adresa= form.cleaned_data["adresa"]
			email= form.cleaned_data["email"]
			heslo = hash_pwd(form.cleaned_data["heslo"])
			heslo2 = hash_pwd(form.cleaned_data["heslo2"])
			if heslo == heslo2 :
				if Zakaznik.objects.filter(email = email).count() == 0:
					u=Zakaznik(meno=meno,priezvisko=priezvisko,adresa=adresa,email=email,password_hash=heslo)
					u.save()
					return HttpResponseRedirect(reverse("Istore.views.uspech"))
				else:
					error="Email je už obsadený!"
			else:
				error="Hesla nie sú zhodné!"
	else:
		form=RegForm()
	t=loader.get_template("registracia.html")
	c=RequestContext(request,{"form":form,"error":error})
	return HttpResponse(t.render(c))

def login(request):
    if "objednavka" in request.session:
        del request.session["objednavka"]
    error=None
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            try:
                u=Zakaznik.objects.get(email=form.cleaned_data["email"])
                if u.check_pwd(form.cleaned_data["heslo"]):
                    request.session["prihlaseny_email"]=u.meno
                    return HttpResponseRedirect(reverse("Istore.views.front_page"))
                else:
                    error=u'Chybné meno alebo heslo!'
            except Zakaznik.DoesNotExist:
                error=u'Chybné meno alebo heslo!'
    else:
        form=LoginForm()
    t=loader.get_template("login.html")
    c=IstoreContext(request,{"form":form,"error":error})
    return HttpResponse(t.render(c))

def logout(request):
    if "prihlaseny_email" in request.session:
        del request.session["prihlaseny_email"]
    if "objednavka" in request.session:
        del request.session["objednavka"]
    return HttpResponseRedirect(reverse("Istore.views.front_page"))

def kategorie(request):
    kat=Kategoria.objects.all()
    t=loader.get_template("front_page.html")
    c=IstoreContext(request,{"kat":kat})
    html=t.render(c)
    return HttpResponse(html)

def zoznam_tovaru(request,kateg):
    tov=Tovar.objects.filter(kategoria_id=int(kateg))
    kat=Kategoria.objects.get(id=int(kateg))
    t=loader.get_template("zoznam.html")
    c=IstoreContext(request,{"tov":tov,"kat":kat})
    html=t.render(c)
    return HttpResponse(html)

def tovar(request,idcislo):
    tov=Tovar.objects.get(id=idcislo)
    kat=tov.kategoria
    error = None
    if request.method == "POST":
        form = KosikForm(request.POST)
        if form.is_valid():
            poc=form.cleaned_data["pocet"]
            if "objednavka" not in request.session:
                o=Objednavka(zakaznik=Zakaznik.objects.get(meno=request.session["prihlaseny_email"]))
                o.save()
                request.session["objednavka"]=o.id
            u=Polozka(tovar=tov,pocet=poc,objednavka_id=request.session["objednavka"])
            u.save()

            return HttpResponseRedirect(reverse('Istore.views.kosik'))
    else:
        form=KosikForm()
    t=loader.get_template("tovar.html")
    c=IstoreContext(request,{"form":form,"tov":tov, "kat":kat})
    html=t.render(c)
    return HttpResponse(html)

def kosik(request):
    if "prihlaseny_email" not in request.session:
        return HttpResponseRedirect(reverse('Istore.views.front_page'))
    if "objednavka" not in request.session:
        return HttpResponseRedirect(reverse('Istore.views.kosik'))
    pol=Polozka.objects.filter(objednavka_id=request.session["objednavka"])
    suma=0
    for polozka in pol:
        suma=suma+polozka.tovar.cena*polozka.pocet

    c=IstoreContext(request,{"pol":pol, "suma":suma})
    t=loader.get_template("kosik.html")
    html=t.render(c)
    return HttpResponse(html)

def platba(request):
   obj=Objednavka.objects.get(id=request.session["objednavka"])
   obj.zaplatenie=True
   obj.save()
   if "objednavka" in request.session:
       del request.session["objednavka"]
   t=loader.get_template("platba.html")
   c=IstoreContext(request,{})
   html=t.render(c)
   return HttpResponse(html)

def vymaz_polozku(request,polozka):
   pol=Polozka.objects.get(id=int(polozka))
   pol.delete()
   polozky=Polozka.objects.filter(objednavka_id=request.session["objednavka"])
   return HttpResponseRedirect(reverse('Istore.views.kosik'))

def profil(request):
   zak=Zakaznik.objects.get(meno=request.session["prihlaseny_email"])
   obj=Objednavka.objects.filter(zakaznik=Zakaznik.objects.get(meno=request.session["prihlaseny_email"]))
   pol=Polozka.objects.filter(objednavka=obj)
   t=loader.get_template("profil.html")
   c=IstoreContext(request,{"pol":pol,"zak":zak})
   html=t.render(c)
   return HttpResponse(html)

def uspech(request):
    t=loader.get_template("reguspech.html")
    c=IstoreContext(request,{})
    html=t.render(c)
    return HttpResponse(html)

def vyhladavanie(request):
    error=None
    if request.method=='POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            ret=form.cleaned_data["retazec"]
            tov=Tovar.objects.filter(popis__icontains=ret)
            t=loader.get_template("vysledky.html")
            c=IstoreContext(request,{"tov":tov,"ret":ret})
            html=t.render(c)
            return HttpResponse(html)
        else:
            form=SearchForm()
    else:
        form=SearchForm()
    t=loader.get_template("vyhladavanie.html")
    c=IstoreContext(request,{"form":form})
    return HttpResponse(t.render(c))
