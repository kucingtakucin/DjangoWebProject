from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.


def peminjamanalat(request):
    data_model = DataPeminjamanAlat.objects.all()
    context = {
        'title': 'Labkom FMIPA UNS | Peminjaman Alat',
        'data_model': data_model
    }
    return render(request, 'PeminjamanAlat/PeminjamanAlat.html', context)
    pass


def peminjamanalattambah(request):
    data_form = DataForm(request.POST or None)
    if request.method == "POST":
        if data_form.is_valid():
            data_form.save()
            return redirect('PeminjamanAlat:index')
            pass
        pass
    pass

    context = {
        'title': 'Labkom FMIPA UNS | Peminjaman Alat',
        'data_form': data_form
    }
    print(request.POST)
    return render(request, 'PeminjamanAlatTambah/PeminjamanAlatTambah.html', context)
    pass


def peminjamanalathapus(request, delete_id):
    DataPeminjamanAlat.objects.filter(id=delete_id).delete()
    return redirect('PeminjamanAlat:index')
    pass


def peminjamanalatubah(request, update_id):
    data_id = DataPeminjamanAlat.objects.get(id=update_id)
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
        'alat': data_id.alat,
        'jumlah': data_id.jumlah,
        'lama_peminjaman': data_id.lama_peminjaman,
        'harga': data_id.harga,
        'keperluan': data_id.keperluan,
    }
    data_form = DataForm(request.POST or None, initial=elemen, instance=data_id)
    if request.method == "POST":
        if data_form.is_valid():
            data_form.save()
            return redirect('PeminjamanAlat:index')
            pass
        pass
    pass

    context = {
        'title': 'Labkom FMIPA UNS | Peminjaman Alat',
        'data_form': data_form
    }
    print(request.POST)
    return render(request, 'PeminjamanAlatTambah/PeminjamanAlatTambah.html', context)
    pass
