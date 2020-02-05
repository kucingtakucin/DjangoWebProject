from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.


def peminjamanlab(request):
    context = {
        'title': 'Labkom FMIPA UNS | Peminjaman Lab',
    }
    return render(request, "PeminjamanLab/PeminjamanLab.html", context)
    pass


def peminjamanlabdidalam(request):
    data_model = DataPeminjamanLab.objects.all()
    context = {
        'title': 'Labkom FMIPA UNS | Peminjaman Lab',
        'data_model': data_model
    }

    return render(request, "PeminjamanLabDidalamJam/PeminjamanLabDidalam.html", context)
    pass


def peminjamanlabdiluar(request):
    context = {
        'title': 'Labkom FMIPA UNS | Peminjaman Lab'
    }
    return render(request, "PeminjamanLabDiluarJam/PeminjamanLabDiluar.html", context)

def tambahdata(request):
    data_forms = DataForm(request.POST or None)
    if request.method == "POST":
        pass
    pass