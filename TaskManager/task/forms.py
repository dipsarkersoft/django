from django import forms
from .models import Task_model



class Add_task_forms(forms.ModelForm):
    class Meta:
        model=Task_model
        fields='__all__'