from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('edmap.genre.views',
    url(r'^/create$', 'create'),
)
