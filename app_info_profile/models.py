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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    surname = models.CharField(max_length = 200)
    firstname = models.CharField(max_length = 200)
    middlename = models.CharField(max_length = 200,blank=True)
    ext_name = models.CharField(max_length = 200,blank=True)
    date_of_birth = models.DateField(default=timezone.now())
    place_of_birth = models.CharField(max_length = 200)
    sex = models.CharField(max_length=10,choices=gender)
    civil_status = models.CharField(max_length=10,choices=civil_status)
    height = models.CharField(max_length = 200,blank=True)
    weight = models.CharField(max_length = 200,blank=True)
    blood_type = models.CharField(max_length = 200,blank=True)
    gsis = models.CharField(max_length = 200,blank=True)
    pagibig = models.CharField(max_length = 200,blank=True)
    philhealth = models.CharField(max_length = 200,blank=True)
    sss = models.CharField(max_length = 200,blank=True)
    tin = models.CharField(max_length = 200,blank=True)
    agency_no = models.CharField(max_length = 200,blank=True)
    citizenship = models.CharField(max_length = 200)
    residential_address = models.CharField(max_length = 200,blank=True)
    zipcode_1 = models.CharField(max_length = 200,blank=True)
    permanent_address = models.CharField(max_length = 200,blank=True)
    zipcode_2 = models.CharField(max_length = 200,blank=True)
    telephone = models.CharField(max_length = 200,blank=True)
    mobile = models.CharField(max_length = 200,blank=True)
    email = models.CharField(max_length = 200,blank=True)
    image = models.ImageField(upload_to='images/',default='images/defaultuserprofile.png')

    sl = models.DecimalField(default=0,max_digits = 50,decimal_places=3)
    vl = models.DecimalField(default=0,max_digits = 50,decimal_places=3)
    overtime = models.DecimalField(default=0,max_digits = 50,decimal_places=2)

    is_active = models.BooleanField(default=True)

    date_updated = models.DateTimeField(auto_now = True)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.surname) + ', ' + str(self.firstname) + ' ' + str(self.middlename)
    @property
    def age(self):
        now = timezone.now()
        return int((now.date() - self.date_of_birth).days / 365.25)

    @property
    def primary_key_custom(self):
        return str(self.date_created.year) + str(self.id)

    class Meta:
        ordering = ['surname','firstname','middlename']


class Notification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    detail = models.CharField(max_length = 200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

class Message(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.CharField(max_length = 200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
