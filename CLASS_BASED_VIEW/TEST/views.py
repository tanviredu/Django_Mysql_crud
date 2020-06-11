from django.shortcuts import render
from .models import Album,Musician
from .forms import MusicianForm,AlbumForm
from django.shortcuts import reverse,HttpResponseRedirect
def index(request):
    musician_list = Musician.objects.order_by('id')
    context = {'musician_list':musician_list}
    return render(request,'first_app/index.html',context)

def album_list(request):
    context={}
    return render(request,'first_app/album_list.html',context)


def musician_form(request):
    form = MusicianForm()
    if request.method == "POST":
        form = MusicianForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('TEST:index'))
            
    
    
    return render(request,'first_app/musician_form.html',{"form":form})


def album_form(request):
    form = AlbumForm()
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("TEST:index"))    
    
    return render(request,'first_app/album_form.html',{"form":form})

