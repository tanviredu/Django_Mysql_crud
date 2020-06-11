from django.shortcuts import render
from .models import Album,Musician


def index(request):
    context = {}
    return render(request,'first_app/index.html',context)

def album_list(request):
    context={}
    return render(request,'first_app/album_list.html',context)


def musician_form(request):
    context = {}
    return render(request,'first_app/musician_form.html',context)


def album_form(request):
    context = {}
    return render(request,'first_app/album_form.html',context)

