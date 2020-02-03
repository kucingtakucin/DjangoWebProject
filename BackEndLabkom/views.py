from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Labkom FMIPA UNS | Dashboard'
    }
    return render(request, 'index.html', context)
    pass


def angka(request, input):
    Halaman = '<h1> Ini adalah halaman angka <h1>'
    return HttpResponse(Halaman)
    pass
