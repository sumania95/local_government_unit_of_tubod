from django.db import models
from model_profiling.tips_address.models import (
    Tips_Barangay,
    Tips_City_Municipality,
    Tips_Province,
    Tips_Region,
)
from django.utils import timezone

# MODEL BASIC INFO
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

class Tips_Person(models.Model):
    surname = models.CharField(max_length = 200)
    firstname = models.CharField(max_length = 200)
    middlename = models.CharField(max_length = 200,blank=True)
    ext_name = models.CharField(max_length = 200,blank=True)
    date_of_birth = models.DateField(default=timezone.now)
    place_of_birth = models.CharField(max_length = 200,blank=True)
    sex = models.CharField(max_length=10,choices=gender)
    civil_status = models.CharField(max_length=10,choices=civil_status)
    philhealth = models.CharField(max_length = 200,blank=True)
    religion = models.CharField(max_length = 200,blank=True)
    nationality = models.CharField(max_length = 200,blank=True)
    highest_educational_attainment = models.CharField(max_length = 200,blank=True)
    skills_occupation = models.CharField(max_length = 200,blank=True)
    income = models.DecimalField(default=0,max_digits = 50,decimal_places=2)
    date_updated = models.DateTimeField(auto_now = True)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.surname) + ', ' + str(self.firstname) + ' ' + str(self.middlename)

    @property
    def age(self):
        now = timezone.now()
        return int((now.date() - self.date_of_birth).days / 365.25)

    class Meta:
        ordering = ['surname','firstname','middlename']

class Tips_Address(models.Model):
    person = models.OneToOneField(Tips_Person, on_delete = models.CASCADE)
    barangay = models.ForeignKey(Tips_Barangay, on_delete = models.CASCADE)
    city_municipality = models.ForeignKey(Tips_City_Municipality, on_delete = models.CASCADE)
    province = models.ForeignKey(Tips_Province, on_delete = models.CASCADE)
    region = models.ForeignKey(Tips_Region, on_delete = models.CASCADE)
    purok_street = models.CharField(max_length = 200,blank=True)
    date_updated = models.DateTimeField(auto_now = True)
    date_created = models.DateTimeField(auto_now_add = True)
#
# # BENEFICIARY
# class Tips_Pwd(models.Model):
#     person = models.OneToOneField(Tips_Person, on_delete = models.CASCADE)
#     date_updated = models.DateTimeField(auto_now = True)
#     date_created = models.DateTimeField(auto_now_add = True)
#
# class Tips_Ofw(models.Model):
#     person = models.OneToOneField(Tips_Person, on_delete = models.CASCADE)
#     date_updated = models.DateTimeField(auto_now = True)
#     date_created = models.DateTimeField(auto_now_add = True)
#
# class Tips_Solo_Parent(models.Model):
#     person = models.OneToOneField(Tips_Person, on_delete = models.CASCADE)
#     date_updated = models.DateTimeField(auto_now = True)
#     date_created = models.DateTimeField(auto_now_add = True)
#
# class Tips_Nuclear_Family(models.Model):
#     person = models.OneToOneField(Tips_Person, on_delete = models.CASCADE)
#     date_updated = models.DateTimeField(auto_now = True)
#     date_created = models.DateTimeField(auto_now_add = True)
#
# class Tips_Head_Relationship(models.Model):
#     person = models.OneToOneField(Tips_Person, on_delete = models.CASCADE)
#     date_updated = models.DateTimeField(auto_now = True)
#     date_created = models.DateTimeField(auto_now_add = True)
#
# class Tips_Beneficiary(models.Model):
#     person = models.OneToOneField(Tips_Person, on_delete = models.CASCADE)
#     date_updated = models.DateTimeField(auto_now = True)
#     date_created = models.DateTimeField(auto_now_add = True)
