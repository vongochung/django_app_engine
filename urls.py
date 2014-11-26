# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib import admin
import dbindexer
from django.conf.urls import patterns, include, url

handler500 = 'djangotoolbox.errorviews.server_error'

# django admin

admin.site.site_header = u'Tài Khoản'
admin.autodiscover()
# search for dbindexes.py in all INSTALLED_APPS and load them
dbindexer.autodiscover()

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^$', include('home.urls')),
    ('^thongke/', include(admin.site.urls)),
)
