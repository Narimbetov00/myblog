from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

#Birinshi config dir ge kirip settings.py ga AUTH_USER_MODEL = 'accounts.CustomUser' dep jaziwimiz kerek

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True)
