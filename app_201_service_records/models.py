from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from app_info_profile.models import Profile
from django.utils import timezone

class Service_Record(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    designate = models.CharField(max_length = 200, blank=True)
    status = models.CharField(max_length = 200)
    salary = models.DecimalField(default= 0,max_digits = 50,decimal_places=2)
    station = models.CharField(max_length = 200)
    branch = models.CharField(max_length = 200)
    lwabs = models.CharField(max_length = 200)
    separtion_date = models.CharField(max_length = 200)
    date_from = models.DateField()
    date_to = models.DateField()

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.profile.surname) + ' ' + str(self.profile.firstname)

    @property
    def is_todate(self):
        now = timezone.now()
        return now.date() < self.date_to
