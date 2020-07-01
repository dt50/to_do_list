from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
# Create your views here.


def register(request):
    form = forms.CreateUser()
    if request.method == 'POST':
        form = forms.CreateUser(request.POST)
        if form.is_valid():
            print('yes')
            messages.success(request, f'Пользователь {form.cleaned_data.get("username")} успешно зарегистрировался!')
            form.save()
        return redirect('task')
    return render(request, 'users/register.html', context={'form': form})
