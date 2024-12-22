from django.urls import path,include
from .views import add_taskCate



urlpatterns = [
    path('',add_taskCate,name='add_taskCate'),

   
]
