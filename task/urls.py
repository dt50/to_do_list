from django.urls import path

from . import views

app_name = 'task'

urlpatterns = [
    path('', views.task, name='task'),
    path('<str:start_date>/<str:end_date>', views.task, name='task_date'),
    path('update/<str:pk>', views.update, name='update'),
    path('delete/<str:pk>', views.delete, name='delete'),
]
