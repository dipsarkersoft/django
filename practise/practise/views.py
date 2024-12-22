from django.shortcuts import render
from . forms import PractiseForm

def home(req):
    return render(req,'home.html',{'form':PractiseForm})