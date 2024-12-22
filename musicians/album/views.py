from django.shortcuts import render,redirect
from .forms import AlbumForms

from . models import Album_model

def add_albums(req):
    if req.method=='POST':
        album_form= AlbumForms(req.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('home_page')
    else:
         album_form= AlbumForms()
    return render(req,'add_album.html',{'form':album_form})
     
def edit_albums(req,id):
    editinf=Album_model.objects.get(pk=id)
    album_form= AlbumForms(instance=editinf)
    if req.method=='POST':
        album_form= AlbumForms(req.POST,instance=editinf)
        if album_form.is_valid():
            album_form.save()
            return redirect('home_page')
    
    return render(req,'edit_album.html',{'form':album_form})
 
def del_albums(req,id):
    editinf=Album_model.objects.get(pk=id)
    editinf.delete()
    return redirect('home_page')
    

