from django.db import models
from model_profiling.tips_person.models import (
    Tips_Person,
)
from django.utils import timezone


class Tips_Category(models.Model):
    name = models.CharField(max_length = 200)
    date_updated = models.DateTimeField(auto_now = True)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.name)

class Tips_Sub_Category(models.Model):
    category = models.ForeignKey(Tips_Category, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    date_updated = models.DateTimeField(auto_now = True)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.name)

services_assistance = (
    ('1', 'Counseling',),
    ('2', 'Legal Assistance (Retainer Lawyer/Others)',),
    ('3', 'Referral',),
    ('4', 'Other Services Assistance',),
)

class Tips_Recommended_Services(models.Model):
    person = models.ForeignKey(Tips_Person, on_delete = models.CASCADE)
    services_assistance = models.CharField(max_length=50,choices=services_assistance)
    specify = models.CharField(max_length = 200)
    date = models.DateField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now = True)
    date_created = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return str(self.person.surname) + ', ' + str(self.person.firstname)

mode_assistance = (
    ('1', 'Cash',),
    ('2', 'Check',),
)

class Tips_Recommended_Services_Action(models.Model):
    recommended_services = models.OneToOneField(Tips_Recommended_Services, on_delete = models.CASCADE)
    category = models.ForeignKey(Tips_Category, on_delete = models.CASCADE)
    sub_category = models.ForeignKey(Tips_Sub_Category, on_delete = models.CASCADE)
    amount = models.IntegerField(default=0)
    mode_assistance = models.CharField(max_length=50,choices=mode_assistance)
    date_updated = models.DateTimeField(auto_now = True)
    date_created = models.DateTimeField(auto_now_add = True)
