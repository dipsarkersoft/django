from django.urls import path,include
from .views import add_albums,edit_albums,del_albums

urlpatterns = [
   
   path('add/',add_albums,name='add_albums'),
   path('edit/<int:id>',edit_albums,name='edit_albums'),
   path('del/<int:id>',del_albums,name='del_albums')
   

]