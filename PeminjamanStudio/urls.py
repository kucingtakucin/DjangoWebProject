from django.urls import path
from . import views
app_name = "PeminjamanStudio"

urlpatterns = [
    path('', views.peminjamanstudio, name="index"),
    path('TambahData', views.peminjamanstudiotambah, name="tambahdata"),
    path('HapusData/<int:delete_id>', views.peminjamanstudiohapus, name="hapusdata"),
    path('UpdateData/<int:update_id>', views.peminjamanstudioubah, name="ubahdata")
]
