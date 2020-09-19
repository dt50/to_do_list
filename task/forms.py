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

    tag = forms.ModelChoiceField(queryset=models.Tag.objects.all(),
                                 empty_label="(Choose tag)",
                                 to_field_name='tag')

    class Meta:
        model = models.Task
        fields = ('title', 'date', 'tag')


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
