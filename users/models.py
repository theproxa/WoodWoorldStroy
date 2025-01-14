from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    phone = models.IntegerField(null = True)
    adress = models.CharField(max_length = 256)

    def __str__(self) -> str:
        return self.username