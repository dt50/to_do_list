from django.urls import path, include
from . import views
urlpatterns = [
    path('reg/', views.registration, name='reg'),
    path('login/', views.Login, name='log'),
    path('change/', views.Change, name='change'),
    path('change_p/', views.Change_p, name='change_p'),
    path('logout/', views.Logout, name='logout'),
]