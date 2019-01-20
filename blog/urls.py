from django.contrib import admin
from django.urls import path

from . import  views
#현재 폴더에 있는 views를 임포트한다

urlpatterns = {
    path('', views.post_list),
}