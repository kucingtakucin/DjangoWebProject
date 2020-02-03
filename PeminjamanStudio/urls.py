from django.urls import path
from . import views
app_name = "PeminjamanStudio"

urlpatterns = [
    path('', views.peminjamanstudio, name="index"),
    path('PeminjamanStudioTambah', views.peminjamanstudiotambah, name="tambahdata")
]
