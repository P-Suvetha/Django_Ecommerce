from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # role = models.CharField(max_length=50, default='user')
    age=models.IntegerField(default=0)
    role_choices = (
        (0, 'Admin'),
        (1, 'Manager'),
        (2, 'Employee'),         
    )
    role = models.IntegerField(choices=role_choices, default=0)
