from django.contrib import admin
from django.urls import path,include

from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home_page'),
    path('add_task/',include('task.urls')),
    path('add_task_cat/',include('taskCate.urls')),
]
