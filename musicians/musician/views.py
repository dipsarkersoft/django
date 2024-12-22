from django.shortcuts import render,redirect
from .forms import MusicianForms
from  . models import Musician_Model

def add_musicians(req):
    if req.method=='POST':
        musician_form= MusicianForms(req.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home_page')
    else:
         musician_form= MusicianForms()
    return render(req,'add_musician.html',{'form':musician_form})
     


def edit_musicians(req,id):
    editinf=Musician_Model.objects.get(pk=id)
    musician_form= MusicianForms(instance=editinf)
    if req.method=='POST':
        musician_form= MusicianForms(req.POST,instance=editinf)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home_page')
    
    return render(req,'edit_musician.html',{'form':musician_form})




