from django.db import models
from django.db.models import Model
from app_info_profile.models import *

class Dtr_Assign(models.Model):
    id = models.IntegerField(primary_key=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

class Dtr(models.Model):
    user_id = models.ForeignKey(Dtr_Assign, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    status = models.CharField(max_length = 1000)
    punch = models.CharField(max_length = 1000)
