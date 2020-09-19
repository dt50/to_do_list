from django.db import models
from users.models import MyUser


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        MyUser,
        on_delete=models.SET_NULL,
        null=True
    )
    tag = models.ForeignKey(
        'Tag',
        on_delete=models.SET_NULL,
        null=True
    )

    title = models.CharField(max_length=128)
    date = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag
