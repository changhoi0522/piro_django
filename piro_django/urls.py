"""piro_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import re_path, include
from django.conf import settings
urlpatterns = [
    re_path(r'^$', lambda r: redirect('blog:post_list'), name='root'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^blog/', include('blog.urls')),
    re_path(r'^dojo/', include('dojo.urls')),
    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^shop/', include('shop.urls')),
    
]

if settings.DEBUG:
    import  debug_toolbar
    urlpatterns += [
        re_path(r'__debug__/', include(debug_toolbar.urls))
    ]
