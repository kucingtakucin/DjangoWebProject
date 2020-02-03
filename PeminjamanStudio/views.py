from django.shortcuts import render
from .forms import *

# Create your views here.


def peminjamanstudio(request):
    context = {
        'title': 'Labkom FMIPA UNS | Peminjaman Studio'
    }
    return render(request, 'PeminjamanStudio/PeminjamanStudio.html', context)
    pass


def peminjamanstudiotambah(request):
    data_form = DataForm()
    context = {
        'title': 'Labkom FMIPA UNS | Peminjaman Studio',
        'data_form': data_form
    }
    print(request.POST)
    return render(request, 'PeminjamanStudioTambah/PeminjamanStudioTambah.html', context)
    pass
