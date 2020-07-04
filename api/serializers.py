from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from task.models import Task
from users.models import MyUser


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserSerializer.Meta):
        model = MyUser
        fields = '__all__'