from django.shortcuts import render
from .models import Album,Musician
from .forms import MusicianForm,AlbumForm
from django.shortcuts import reverse,HttpResponseRedirect
from django.db.models import Avg




def index(request):
    musician_list = Musician.objects.order_by('id')
    context = {'musician_list':musician_list}
    return render(request,'first_app/index.html',context)

def album_list(request,artist_id):
    artist = Musician.objects.get(pk=artist_id)
    albums_list = Album.objects.filter(artist=artist_id).order_by('name','release_date')
    
    ## django aggragate function
    artist_avg_rating = Album.objects.filter(artist=artist_id).aggregate(Avg('num_star'))
    
    context={'artist':artist,'albums_list':albums_list,'artist_avg_rating':artist_avg_rating}
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

