from django.shortcuts import render,redirect
from .forms import Task_Cate_Form 

# Create your views here.
def add_taskCate(req):
    if req.method=='POST':
        task_cate_form=Task_Cate_Form(req.POST)
        if task_cate_form.is_valid():
            task_cate_form.save()
            return redirect('home_page')
    else:
        task_cate_form=Task_Cate_Form()
    return render(req,'add_task_cate.html',{'form':task_cate_form})
    
