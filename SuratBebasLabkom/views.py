from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.


def suratbebaslabkom(request):
    data_model = DataSuratBebasLabkom.objects.all()
    context = {
        'title': 'Labkom FMIPA UNS | Surat Bebas Labkom',
        'data_model': data_model
    }
    return render(request, 'SuratBebasLabkom/SuratBebasLabkom.html', context)
    pass


def suratbebaslabkomtambah(request):
    data_form = DataForm(request.POST or None)
    if request.method == "POST":
        if data_form.is_valid():
            data_form.save()
            return redirect('SuratBebasLabkom:index')
            pass
        pass
    pass

    context = {
        'title': 'Labkom FMIPA UNS | Surat Bebas Labkom',
        'data_form': data_form
    }
    print(request.POST)
    return render(request, 'SuratBebasLabkomCRUD/SuratBebasLabkomCRUD.html', context)
    pass


def suratbebaslabkomhapus(request, delete_id):
    DataSuratBebasLabkom.objects.filter(id=delete_id).delete()
    return redirect('SuratBebasLabkom:index')
    pass


def suratbebaslabkomubah(request, update_id):
    data_id = DataSuratBebasLabkom.objects.get(id=update_id)
    elemen = {
        'nama': data_id.nama,
        'nim': data_id.nim,
        'jenis_kelamin': data_id.jenis_kelamin,
        'program_studi': data_id.program_studi,
        'angkatan': data_id.angkatan,
        'hari': data_id.hari,
        'tanggal': data_id.tanggal,
    }
    data_form = DataForm(request.POST or None, initial=elemen, instance=data_id)
    if request.method == "POST":
        if data_form.is_valid():
            data_form.save()
            return redirect('SuratBebasLabkom:index')
            pass
        pass
    pass

    context = {
        'title': 'Labkom FMIPA UNS | Surat Bebas Labkom',
        'data_form': data_form
    }
    print(request.POST)
    return render(request, 'SuratBebasLabkomCRUD/SuratBebasLabkomCRUD.html', context)
    pass
