from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# TODO register on admin!

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE) # another way to import

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='post/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by @{self.user.username}'