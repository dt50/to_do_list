from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),

    path('list/', views.apiOverview, name="api-overview"),
    path('test/', views.test, name='test'),

    path('task-list/', views.taskList, name="task-list"),
    path('task-create/', views.taskCreate, name="task-create"),

    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),

]
