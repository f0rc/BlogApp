from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


class User(AbstractUser):
    pass

class Post(models.Model):
    # make it public or private
    ACCESS_PUBLIC = 0
    ACCESS_PRIVATE = 1
    ACCESS_LEVEL_CHOICES = [
        (ACCESS_PUBLIC, 'Public'),
        (ACCESS_PRIVATE,'Private'),
    ]
    #the input places in admin site/make post thing

    title = models.CharField(default=datetime.today().strftime('%m/%d'),max_length=100)
    contents= models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    access_level = models.IntegerField(choices=ACCESS_LEVEL_CHOICES, default=ACCESS_PUBLIC)    

    #to create custom links to the posts(create detail post vies. )
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    #created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    #created_at = models.DateTimeField(auto_now_add=True)

#<p><em>@{{ post.author.username }}</em> {{ post.contents }} <em>{{ post.created_at|date:"SHORT_DATETIME_FORMAT" }}</em></p>