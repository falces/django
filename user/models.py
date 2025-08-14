from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    birthDate = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.username