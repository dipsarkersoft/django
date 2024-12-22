from django.urls import path,include
from .views import create_task,edit_task,del_task


urlpatterns = [
   path('',create_task,name='create_task'),
   path('edit/<int:id>',edit_task,name='edit_task'),
   path('del/<int:id>',del_task,name='del_task')
   
]