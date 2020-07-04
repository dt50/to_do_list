from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from . import forms


def registration(request):
    form = forms.CustomUserCreationForm()

    if request.method == 'POST':
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Успешная регистрация пользователя {form.username}')
        return redirect('task:task')

    return render(request, 'users/register.html', context={'form': form})


def Login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('email'),
            password=request.POST.get('password')
        )
        if user is not None:
            login(request, user)
            messages.success(request, f'Пользователь с почтой {request.POST.get("email")} успешно авторизировался')
            return redirect('task:task')
        else:
            messages.error(request, f'Не удалось аторизироваться, вы ввели неправильные данные!')
    return render(request, 'users/login.html')


@login_required
def Change(request):
    form = forms.CustomUserChangeForm()
    if request.method == 'POST':
        form = forms.CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('task:task')
    return render(request, 'users/change.html', context={'form': form})


@login_required
def Change_p(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
        return redirect('task:task')
    return render(request, 'users/change_password.html', context={'form': form})


@login_required
def Logout(request):
    logout(request)
    return redirect('task:task')
