from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.utils import timezone

gender = (
    ('1', 'Male',),
    ('2', 'Female',),
)

civil_status = (
    ('1', 'Single',),
    ('2', 'Married',),
    ('3', 'Widowed',),
    ('4', 'Separated',),
    ('5', 'Annulled',),
)

class Profiling(models.Model):
    surname = models.CharField(max_length = 200)
    firstname = models.CharField(max_length = 200)
    middlename = models.CharField(max_length = 200,blank=True)
    ext_name = models.CharField(max_length = 200,blank=True)
    date_of_birth = models.DateField(default=timezone.now)
    sex = models.CharField(max_length=10,choices=gender)
    civil_status = models.CharField(max_length=10,choices=civil_status)

    date_updated = models.DateTimeField(auto_now = True)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.surname) + ', ' + str(self.firstname) + ' ' + str(self.middlename)
    @property
    def age(self):
        now = timezone.now()
        return int((now.date() - self.date_of_birth).days / 365.25)

class Address(models.Model):
    profiling = models.OneToOneField(Profiling, on_delete=models.CASCADE)
    region = models.CharField(max_length = 200)
    city_municipality = models.CharField(max_length = 200)
    barangay = models.CharField(max_length = 200)
    street = models.CharField(max_length = 200)

class Religion_Nationality(models.Model):
    profiling = models.OneToOneField(Profiling, on_delete=models.CASCADE)
    religion = models.CharField(max_length = 200)
    nationality = models.CharField(max_length = 200)
