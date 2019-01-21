from django.contrib import admin
from django.urls import re_path, path, include
from . import views

urlpatterns = [
    re_path(r'^sum/(?P<x>\d+)$', views.mysum),
    re_path(r'^sum/(?P<x>\d+)/(?P<y>\d+)$', views.mysum),
    re_path(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)$', views.mysum),
]
