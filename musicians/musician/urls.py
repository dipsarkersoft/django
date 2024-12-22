from django.urls import path,include
from .views import add_musicians,edit_musicians

urlpatterns = [
   
   path('add/',add_musicians,name='add_musicians'),
   path('edit/<int:id>',edit_musicians,name='edit_musicians')
  
   

]
