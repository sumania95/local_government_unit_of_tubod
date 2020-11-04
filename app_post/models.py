from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField

from app_info_profile.models import Profile

class Comment(models.Model):
    description = models.CharField(max_length = 1000)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.description)
        
    class Meta:
        ordering = ('-date_created',)

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length = 1000)

    likes = models.ManyToManyField(Profile , blank = True , related_name = 'post_like')
    comments = models.ManyToManyField(Comment , blank = True)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.description)
