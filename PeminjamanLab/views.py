from django.shortcuts import render

# Create your views here.


def peminjamanlab(request):
    context = {
        'title': 'Labkom FMIPA UNS | Peminjaman Lab'
    }
    return render(request, "PeminjamanLab/PeminjamanLab.html", context)
    pass


def peminjamanlabdidalam(request):
    context = {
        'title': 'Labkom FMIPA UNS | Peminjaman Lab'
    }
    return render(request, "PeminjamanLabDidalamJam/PeminjamanLabDidalam.html", context)
    pass


def peminjamanlabdiluar(request):
    context = {
        'title': 'Labkom FMIPA UNS | Peminjaman Lab'
    }
    return render(request, "PeminjamanLabDiluarJam/PeminjamanLabDiluar.html", context)