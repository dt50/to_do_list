from django.shortcuts import render, redirect

from . import models
from . import forms


def task(request):
    tasks = models.Task.objects.all()
    form = forms.TaskForm()
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/task')
    return render(request, 'task/task.html', {'form': form, 'tasks': tasks})


def update(request, pk):
    task = models.Task.objects.get(id=pk)
    form = forms.TaskFormUpdate(instance=task)
    if request.method == 'POST':
        form = forms.TaskFormUpdate(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/task')

    return render(request, 'task/update.html', context={'form': form})


def delete(request, pk):
    task = models.Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/task')
    return render(request, 'task/delete.html', context={'task': task})
