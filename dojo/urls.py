from django.contrib import admin
from django.urls import re_path, path, include
from . import views

urlpatterns = [
    re_path(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
]
