from django.shortcuts import render,redirect
from .forms import Add_task_forms
from .models import Task_model
# Create your views here.


def create_task(req):
    if req.method=='POST':
        task_create=Add_task_forms(req.POST)
        if task_create.is_valid():
            task_create.save()
            return redirect('home_page')
    else:
        task_create=Add_task_forms()
    return render(req,'add_task.html',{'form':task_create})   

def edit_task(req,id):
    data=Task_model.objects.get(pk=id)
    task_form=Add_task_forms(instance=data)
    if req.method=='POST':
         task_form=Add_task_forms(req.POST,instance=data)
         if task_form.is_valid():
             task_form.save()
             return redirect('home_page')
    return render(req,'edit_task.html',{'form':task_form})   


def del_task(req,id):
     data=Task_model.objects.get(pk=id)
     data.delete()
     return redirect('home_page')


