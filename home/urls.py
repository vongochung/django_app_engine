from django.conf.urls import *

urlpatterns = patterns('home.views',
   url(r'^$', 'index'),
   url(r'^create-post/$', 'create_post'),
   url(r'^create-comment/$', 'create_comment'),
   url(r'^get-comment/$', 'get_comment'),
   url(r'^get-posts/$', 'get_posts'),
)
