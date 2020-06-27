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
        redirect('/')
    return render(request, 'task/task.html', {'form': form, 'tasks': tasks})
