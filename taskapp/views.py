from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

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
