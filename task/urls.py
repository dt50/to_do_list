from django.urls import path, register_converter

from . import views, converter

app_name = 'task'

register_converter(converter.YearConverter, 'yyyy')

urlpatterns = [
    path('', views.task, name='task'),
    path('filter/<yyyy:start_date>/<yyyy:end_date>', views.task, name='task_date'),
    path('filter/<str:tag>', views.tag_filter, name='tag'),
    path('update/<str:pk>', views.update, name='update'),
    path('delete/<str:pk>', views.delete, name='delete'),
]
