from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name

    introduce = models.TextField(max_length=500, null=True)
    genre = models.TextField(max_length=1000, blank=True)
