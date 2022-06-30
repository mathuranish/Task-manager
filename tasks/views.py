from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Task
from .forms import Taskform
# Create your views here.

def index(request):
    tasks= Task.objects.all()
    form = Taskform()

    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    data = {
        'tasks' : tasks,
        'form' : form,
    }
    #return render(request, "tasks/index.html",data)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = Taskform(instance=task) #for prefilling textfeild when updating

    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    data = {
        'form': form,
    }
    return render(request, "tasks/update_task.html", data)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete() 
        return redirect('/')

    data ={
        'task' : task,
    }
    return render(request, "tasks/delete_task.html",data)


def list(request):
    return render(request, "tasks/list.html")

