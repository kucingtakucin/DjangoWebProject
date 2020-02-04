from django.urls import path
from . import views
app_name = "PeminjamanLab"

urlpatterns = [
    path('', views.peminjamanlab, name="index"),
    path('DidalamJam', views.peminjamanlabdidalam, name="didalam"),
    path('DiluarJam', views.peminjamanlabdiluar, name="diluar"),
]
