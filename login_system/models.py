from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

# Create your models here.

class users(models.Model):
    username = models.CharField(max_length=30)
    fullname = models.CharField(max_length=30)
    dob = models.DateField()
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    Password = models.CharField(max_length=100)
