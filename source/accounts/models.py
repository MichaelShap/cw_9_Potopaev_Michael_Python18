from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+996 \d{3} \d{3} \d{3}$',
                                 message="Телефонный номер должен соответствовать формату +996 XXX XXX XXX")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False, null=False)

    def __str__(self):
        return self.username