from django.db import models
from django.db.models import Model

class Dtr(models.Model):
    user_id = models.IntegerField()
    timestamp = models.DateTimeField()
    status = models.CharField(max_length = 1000)
    punch = models.CharField(max_length = 1000)
