from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from django.contrib.auth.models import User
from django.utils import timezone

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    is_authenticated = models.BooleanField(default=True)
    date_updated = models.DateTimeField(auto_now = True)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.user.profile)

class Settings(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    budget_title = models.CharField(default = "Municipal Budget Officer",max_length=200)
    budget_name = models.CharField(default = "Lymarie A. Malicdem",max_length=200)
    treasury_title = models.CharField(default = "Municipal Treasury Officer",max_length=200)
    treasury_name = models.CharField(default = "Jerry I. Fillalan",max_length=200)
    hr_title = models.CharField(default = "Human Resources Management Officer",max_length=200)
    hr_name = models.CharField(default = "Adonis G. Cuevas",max_length=200)
    mayor_name = models.CharField(default = "Richelle B. Romarate, MSCE",max_length=200)
    from_date = models.DateField(default=timezone.now)
    to_date = models.DateField(default=timezone.now)
