from django.db import models
from users.models import MyUser


# Create your models here.
class UserTg(models.Model):
    external_id = models.IntegerField(
        primary_key=True,
        unique=True,
        verbose_name='Telegram Id profile'
    )
    user_name = models.CharField(
        unique=True,
        max_length=50,
        verbose_name='Telegram user_name'
    )
    user = models.ForeignKey(
        MyUser,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.user_name