from django.db import models

# Create your models here.

class User(models.Model):
    """User model"""

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=101)

    first_name = models.CharField(max_length=100)
    las_name = models.CharField(max_length=100)

    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True) #includes hour
    modified = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)