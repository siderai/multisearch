from pyexpat import model
import django
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=255, verbose_name="email")
    paid = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
