from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField('first name', max_length=30, null=True, blank=True)
    last_name = models.CharField('last name', max_length=150, null=True, blank=True)
    bio = models.TextField(null=True,blank=True)
    last_login = models.DateTimeField(auto_now_add=False, null=True,blank=True)
    last_activity = models.DateTimeField(auto_now_add=False, null=True,blank=True)