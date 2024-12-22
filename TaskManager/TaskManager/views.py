from django.shortcuts import redirect,render
from task.models import Task_model

def home(req):
    res=Task_model.objects.all()
    return render(req,'home.html',{'data':res})



