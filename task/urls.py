from django.urls import path
from users import views as UsersView

from . import views

urlpatterns = [
    path('task/', views.task, name='task'),
    path('update/<str:pk>', views.update, name='update'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('reg', UsersView.register, name='registration')
]
