from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import TextChoices
from common.models import LogsMixin
# Create your models here.
class UserTypeChoices(TextChoices):
    VENDOR = 1
    CLIENT = 2

class User(AbstractUser):
    user_type = models.CharField(max_length=10, null=True, blank=True, choices=UserTypeChoices.choices)
    email = models.EmailField(null=True, blank=True, unique=True)
    username = models.CharField(max_length=300, null=True, blank=True)
    password = models.CharField(max_length=1000, null=True, blank=True)
    login_token = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=10000, null=True, blank=True)
    contact = models.CharField(max_length=10000, null=True, blank=True)
    bio = models.CharField(max_length=10000, null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
