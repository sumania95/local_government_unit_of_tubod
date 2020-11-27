from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.utils import timezone

legal_assistance = (
    ('1', 'Financial Assistance',),
    ('2', 'Material Assistance',),
)

class Legal_Assistance(models.Model):
    description = models.CharField(max_length = 200)
    legal_assistance = models.CharField(max_length=10,choices=legal_assistance)

    date_updated = models.DateTimeField(auto_now = True)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.description)
