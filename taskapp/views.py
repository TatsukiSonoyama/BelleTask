from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic
from .forms import LoginForm

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'taskapp/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'taskapp/task_list.html'

# Create your views here.
def task_list(request):
    tasks = Task.objects.all().order_by("limit_date")
    return render(request,"taskapp/task_list.html",{"tasks":tasks})

def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'taskapp/task_edit.html', {'form': form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.created_date = timezone.now()
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'taskapp/task_edit.html', {'form': form})

def task_uncompleted(request):
    tasks = Task.objects.filter(is_completed=False).order_by("limit_date")
    return render(request,"taskapp/task_uncompleted.html",{"tasks":tasks})
