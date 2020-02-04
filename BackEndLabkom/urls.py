"""BackEndLabkom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('PeminjamanLab/', include('PeminjamanLab.urls', namespace="PeminjamanLab")),
    path('PeminjamanAlat/', include('PeminjamanAlat.urls', namespace="PeminjamanAlat")),
    path('PeminjamanStudio/', include('PeminjamanStudio.urls', namespace="PeminjamanStudio")),
    path('SuratBebasLabkom/', include('SuratBebasLabkom.urls', namespace="SuratBebasLabkom")),
    path('Blog/', include('FrontEndLabkom.urls', namespace="FrontEndLabkom")),
    url(r'^(?P<input>[0-9]+)', views.angka)
]
