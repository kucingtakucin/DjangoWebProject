from django.urls import path
from . import views
app_name = "SuratBebasLabkom"

urlpatterns = [
    path('', views.suratbebaslabkom, name="index"),
    path('TambahData', views.suratbebaslabkomtambah, name="tambahdata"),
    path('HapusData/<int:delete_id>', views.suratbebaslabkomhapus, name="hapusdata"),
    path('UbahData/<int:update_id>', views.suratbebaslabkomubah, name="ubahdata"),
]
