from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('task.urls')),
    path('user/', include('users.urls')),
    path('api/', include('api.urls')),
]
