from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    custom_field = models.CharField(max_length=20, blank=True, null=True, verbose_name="Some test field")

    def __str__(self):
        return self.username