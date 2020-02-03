from django.urls import path
from django.conf.urls import url
from . import views
app_name = "FrontEndLabkom"

urlpatterns = [
    path('', views.frontendlabkom, name="index"),
    url(r'^(?P<inputcategory>[\w-]+)', views.categorypost),
    url(r'^post/(?P<inputslug>[\w-]+)', views.slugpost),
]
