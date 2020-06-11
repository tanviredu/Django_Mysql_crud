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


def edit_artist(request,artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = MusicianForm(instance=artist_info)
    if request.method == "POST":
        ## this is the most important part
        ## for edit you need to provide the 
        ## instance too that you want to edit
        form = MusicianForm(request.POST,instance=artist_info)
        if form.is_valid():
            form.save()
            ## this is new way of redirection
            return album_list(request,artist_info.id) 
    
    return render(request,'first_app/edit_artist.html',{'form':form})


def edit_album(request,album_id):
    album_info = Album.objects.get(pk=album_id)
    form = AlbumForm(instance=album_info)
    if request.method == "POST":
        form = AlbumForm(request.POST,instance=album_info)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('TEST:index'))
    return render(request,'first_app/edit_album.html',{'form':form})


def delete_album(request,album_id):
    album = Album.objects.get(pk=album_id).delete()
    return HttpResponseRedirect(reverse('TEST:index'))
    


