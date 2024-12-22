from django import forms
from .models import Task_cate

class Task_Cate_Form(forms.ModelForm):
    class Meta:
        model=Task_cate
        fields='__all__'