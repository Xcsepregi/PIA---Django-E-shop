from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', 'Istore.views.front_page'),
    url(r'^podmienky/$', 'Istore.views.podmienky'),
    url(r'^kontakt/$', 'Istore.views.kontakt'),
    url(r'^vyhladavanie/$', 'Istore.views.vyhladavanie'),
    url(r'^prihlasenie/$', 'Istore.views.login'),
    url(r'^registracia/$', 'Istore.views.registracia'),
    url(r'^uspech/$', 'Istore.views.uspech'),
    url(r'^odhlasenie/$', 'Istore.views.logout'),
    url(r'^platba/$','Istore.views.platba'),
    url(r'^kosik/$','Istore.views.kosik'),
    url(r'^profil/$', 'Istore.views.profil'),
    url(r'^vymaz/(?P<polozka>(\d+))','Istore.views.vymaz_polozku'),
    url(r'^kategoria/(?P<kateg>[0-9]+)/$','Istore.views.zoznam_tovaru'),
    url(r'(?P<idcislo>(\d+))','Istore.views.tovar'),
]
