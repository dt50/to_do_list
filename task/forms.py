from django.forms import ModelForm
from django import forms
from . import models


class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    date = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local'
            }, format='%Y-%m-%dT%H:%M'))

    class Meta:
        model = models.Task
        fields = ('title', 'date')


class TaskFormUpdate(forms.ModelForm):
    title = forms.CharField(max_length=128)
    date = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local'
            }, format='%Y-%m-%dT%H:%M'))
    completed = forms.BooleanField(required=False)

    class Meta:
        model = models.Task
        fields = ('title', 'date', 'completed')
