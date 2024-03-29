from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    """Proxy class from auth user"""

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    website = models.URLField(max_length=200,blank=True)
    biography = models.TextField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True,
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        """toString"""
        return f'{self.user.username}'
