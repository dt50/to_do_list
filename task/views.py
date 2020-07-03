from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import models
from . import forms


@login_required(login_url='/user/login/')
def task(request):
    form = forms.TaskForm()
    tasks = models.Task.objects.all().filter(user=request.user).order_by('date')
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, 'Your task created successfully')
        return redirect('/task')
    return render(request, 'task/task.html', {'form': form, 'tasks': tasks})


@login_required(login_url='/user/login/')
def update(request, pk):
    task = models.Task.objects.get(id=pk)
    form = forms.TaskFormUpdate(instance=task)
    if request.method == 'POST':
        form = forms.TaskFormUpdate(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/task')

    return render(request, 'task/update.html', context={'form': form})


@login_required(login_url='/user/login/')
def delete(request, pk):
    task = models.Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/task')
    return render(request, 'task/delete.html', context={'task': task})
