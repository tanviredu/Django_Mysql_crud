from django.urls import path
from . import views
app_name="TEST"

urlpatterns = [
    
        path('',views.index,name='index'),
        path('album_form',views.album_form,name='album_form'),
        path('album_list',views.album_list,name='album_list'),
        path('musician_form',views.musician_form,name='musician_form'),
    
]