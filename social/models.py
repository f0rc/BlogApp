from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class User(AbstractUser):
    pass

class Post(models.Model):
    ACCESS_PUBLIC = 0
    ACCESS_PRIVATE = 1
    ACCESS_LEVEL_CHOICES = [
        (ACCESS_PUBLIC, 'Public'),
        (ACCESS_PRIVATE,'Private'),
    ]
    title = models.CharField(default=date.today().strftime('%m/%d'),max_length=100)
    contents= models.TextField()
    date_posted = models.DateTimeField(default=datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    access_level = models.IntegerField(choices=ACCESS_LEVEL_CHOICES, default=ACCESS_PUBLIC)    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})