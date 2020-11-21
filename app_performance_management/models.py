from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from app_info_profile.models import Profile

class Accomplishment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    core_function_output = models.CharField(max_length = 200)
    indicator = models.ManyToManyField(Indicator, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.profile.surname) + ' ' + str(self.profile.firstname)

class Indicator(models.Model):
    description = models.CharField(max_length = 200)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.description)

class Rating(models.Model):
    individual = models.ForeignKey(Individual, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    ratings = models.CharField(max_length = 200)
    remarks = models.CharField(max_length = 200)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.description)

class Year(models.Model):
    year = models.CharField(max_length = 200)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.description)
