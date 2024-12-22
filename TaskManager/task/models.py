from django.db import models
from taskCate.models import Task_cate

# Create your models here.

class Task_model(models.Model):
    task_title=models.CharField(max_length=20)
    task_desc=models.CharField(max_length=50)
    is_completed=models.BooleanField(default=False)
    task_assain_date=models.DateTimeField(auto_now=True)
    task_cate=models.ManyToManyField(Task_cate)

    def __str__(self):
        return self.task_title
    


