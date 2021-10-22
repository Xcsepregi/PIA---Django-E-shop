from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('Istore.urls')),
    url(r'^podmienky/$', include('Istore.urls')),
    url(r'^kontakt/$', include('Istore.urls')),
    url(r'^registracia/$', include('Istore.urls')),
    url(r'^prihlasenie/$', include('Istore.urls'))
]
