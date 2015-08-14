__author__ = 'atik'

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_app import views

urlpatterns = [
    url(r'^$', 'rest_app.views.index', name='index'),
    url(r'^(?P<value>[0-9]+)/$', 'rest_app.views.get', name='get'),
    url(r'^api/$', views.ZipList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.ZipDetails.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)