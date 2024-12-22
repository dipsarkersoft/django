from django.db import models


# Create your models here.

class Task_cate(models.Model):
    category_name=models.CharField(max_length=20)

    def __str__(self):
        return self.category_name
    