from django.urls import path
from . import views

urlpatterns = [
    path('', views.peminjamanlab),
    path('PeminjamanLabDidalamJam', views.peminjamanlabdidalam),
    path('PeminjamanLabDiluarJam', views.peminjamanlabdiluar),
]
