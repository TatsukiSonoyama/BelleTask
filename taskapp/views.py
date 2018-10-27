from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm
from django.utils import timezone

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
