from django.db import models
from django.db.models import Model

class Settings(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
