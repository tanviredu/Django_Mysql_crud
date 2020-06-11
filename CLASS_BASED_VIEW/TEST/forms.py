from django import forms
from .models import Musician,Album


class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = "__all__"
        

class AlbumForm(forms.ModelForm):
    
    ## form override
    ## to add widget
    release_date = forms.DateField(widget = forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Album
        fields = "__all__"