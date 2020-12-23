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

# # BENEFICIARY
class Tips_Person_Category(models.Model):
    person = models.OneToOneField(Tips_Person, on_delete = models.CASCADE)
    cnsp = models.BooleanField(default=False)
    ynsp = models.BooleanField(default=False)
    wedc = models.BooleanField(default=False)
    pwd = models.BooleanField(default=False)
    fhona = models.BooleanField(default=False)
    solo_parent = models.BooleanField(default=False)
    ip = models.BooleanField(default=False)

    date_updated = models.DateTimeField(auto_now = True)
    date_created = models.DateTimeField(auto_now_add = True)


class Tips_Farmer(models.Model):
    person = models.OneToOneField(Tips_Person, on_delete=models.CASCADE)
    is_rice = models.BooleanField(default=False)
    is_corn = models.BooleanField(default=False)
    other_crops = models.CharField(max_length = 200,blank=True)
    livestock = models.CharField(max_length = 200,blank=True)
    poultry = models.CharField(max_length = 200,blank=True)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.person.surname) + ', ' + str(self.person.firstname) + ' ' + str(self.person.middlename)

class Tips_Farmerworker(models.Model):
    person = models.OneToOneField(Tips_Person, on_delete=models.CASCADE)
    is_land_preparation = models.BooleanField(default=False)
    is_planting_or_transplanting = models.BooleanField(default=False)
    is_cultivation = models.BooleanField(default=False)
    is_harvesting = models.BooleanField(default=False)
    others = models.CharField(max_length = 200,blank=True)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.person.surname) + ', ' + str(self.person.firstname) + ' ' + str(self.person.middlename)

class Tips_Fisherfolk(models.Model):
    person = models.OneToOneField(Tips_Person, on_delete=models.CASCADE)
    is_fish_capture = models.BooleanField(default=False)
    is_aquaculture = models.BooleanField(default=False)
    is_gleaning = models.BooleanField(default=False)
    is_fish_processing = models.BooleanField(default=False)
    is_fish_vending = models.BooleanField(default=False)
    others = models.CharField(max_length = 200,blank=True)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.person.surname) + ', ' + str(self.person.firstname) + ' ' + str(self.person.middlename)
