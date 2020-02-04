from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.


def peminjamanstudio(request):
    data_model = DataPeminjamanStudio.objects.all()
    context = {
        'title': 'Labkom FMIPA UNS | Peminjaman Studio',
        'data_model': data_model
    }
    return render(request, 'PeminjamanStudio/PeminjamanStudio.html', context)
    pass


def peminjamanstudiotambah(request):
    data_form = DataForm(request.POST or None)
    if request.method == "POST":
        if data_form.is_valid():
            data_form.save()
            return redirect('PeminjamanStudio:index')
            pass
        pass
    pass
    context = {
        'title': 'Labkom FMIPA UNS | Peminjaman Studio',
        'data_form': data_form
    }
    print(request.POST)
    return render(request, 'PeminjamanStudioCRUD/PeminjamanStudioCRUD.html', context)
    pass


def peminjamanstudiohapus(request, delete_id):
    DataPeminjamanStudio.objects.filter(id=delete_id).delete()
    pass


def peminjamanstudioubah(request, update_id):
    data_id = DataPeminjamanStudio.objects.get(id=update_id)
    elemen = {
        'nama': data_id.nama,
        'nim': data_id.nim,
        'jenis_kelamin': data_id.jenis_kelamin,
        'program_studi': data_id.program_studi,
        'angkatan': data_id.angkatan,
        'hari': data_id.hari,
        'tanggal': data_id.tanggal,
        'tempat': data_id.tempat,
        'waktu': data_id.waktu,
    }
    data_form = DataForm(request.POST or None, initial=elemen, instance=data_id)
    if request.method == "POST":
        if data_form.is_valid():
            return redirect('PeminjamanStudio:index')
            pass
        pass
    pass
    context = {
        'title': 'Labkom FMIPA UNS | Peminjaman Studio',
        'data_form': data_form
    }
    print(request.POST)
    return render(request, 'PeminjamanStudioCRUD/PeminjamanStudioCRUD.html', context)
    pass
