from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def frontendlabkom(request):
    postingan = Post.objects.all()
    context = {
        'title': 'Labkom FMIPA UNS | Blog',
        'post': postingan
    }
    return render(request, 'FrontEndLabkom/FrontEndLabkom.html', context)
    pass


def categorypost(request, inputcategory):
    posts = Post.objects.filter(kategori=inputcategory)
    return HttpResponse(posts)
    pass


def slugpost(request, inputslug):
    posts = Post.objects.get(slug=inputslug)
    judul = "<h1>{}<h1>".format(posts.title)
    body = "<h1>{}<h1>".format(posts.body)
    kategory = "<h1>{}<h1>".format(posts.kategori)
    email = "<h1>{}<h1>".format(posts.email)
    alamat = "<h1>{}<h1>".format(posts.alamat)
    return HttpResponse(judul, body, kategory, email, alamat)
    pass
