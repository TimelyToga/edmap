from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('edmap.genre.views',
    url(r'^/create$', 'create'),
    url(r'^/view/(?P<genre_name>.*)$', 'view_genre'),
    url(r'^/delete/(?P<genre_key>.*)$', 'delete_genre'),
    url(r'^/all$', 'all'),
)
