from django.urls import path
from . import views
app_name = "PeminjamanAlat"

urlpatterns = [
    path('', views.peminjamanalat, name="index"),
    path('TambahData', views.peminjamanalattambah, name="tambahdata"),
    path('HapusData/<int:delete_id>', views.peminjamanalathapus, name="hapusdata"),
    path('UbahData/<int:update_id>', views.peminjamanalatubah, name="ubahdata")
]
