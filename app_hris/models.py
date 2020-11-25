from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from django.contrib.auth.models import User

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    is_authenticated = models.BooleanField(default=True)
    date_updated = models.DateTimeField(auto_now = True)
    date_created = models.DateTimeField(auto_now_add = True)

class Settings(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
