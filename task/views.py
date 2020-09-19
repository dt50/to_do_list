from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from . import models
from . import forms


@login_required(login_url='/user/login/')
def task(request, start_date=None, end_date=None):
    task_form = forms.TaskForm()
    if start_date and end_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        tasks = models.Task.objects.all().filter(user=request.user, date__range=[start_date, end_date]).order_by('date')
    else:
        tasks = models.Task.objects.all().filter(user=request.user).order_by('date')

    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            obj = task_form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, 'Your task created successfully')

        return redirect('task:task')

    return render(request, 'task/task.html', {'form': task_form, 'tasks': tasks})


@login_required(login_url='/user/login/')
def tag_filter(request, tag):
    task_form = forms.TaskForm()

    tag_object = models.Tag.objects.get(tag=tag)
    tasks_tag = models.Task.objects.all().filter(tag=tag_object)

    return render(request, 'task/task.html', {'form': task_form, 'tasks': tasks_tag})


@login_required(login_url='/user/login/')
def update(request, pk):
    task = models.Task.objects.get(id=pk)
    form = forms.TaskFormUpdate(instance=task)
    if request.method == 'POST':
        form = forms.TaskFormUpdate(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('task:task')

    return render(request, 'task/update.html', context={'form': form})


@login_required(login_url='/user/login/')
def delete(request, pk):
    task = models.Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task:task')
    return render(request, 'task/delete.html', context={'task': task})
