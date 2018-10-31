from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'taskapp'

urlpatterns = [
path("",views.task_list,name="task_list"),
path("task_new",views.task_new,name= "task_new"),
path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
path('task_uncompleted/', views.task_uncompleted, name='task_uncompleted'),
path('login/', views.Login.as_view(), name='login'),
path('logout/', views.Logout.as_view(), name='logout'),
path('signup/', views.signup, name='signup'),
]
