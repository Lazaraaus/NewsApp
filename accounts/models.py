from django.db import models
from django.contrib.auth.models import AbstractUser

# Create a Custom User Class
class CustomUser(AbstractUser):
    # Add an age field, set null and blank properties to True
    # This allows the DB to store an empty field as a NULL value 
    age = models.PositiveIntegerField(null=True, blank=True)

# Create your models here.
