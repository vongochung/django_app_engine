from django.conf.urls import *

urlpatterns = patterns('home.views',
   url(r'^$', 'index'),
)
