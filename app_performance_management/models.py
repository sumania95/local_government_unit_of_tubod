from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from app_info_profile.models import Profile

class Year(models.Model):
    year = models.CharField(max_length = 200)
    is_active = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.year)

class Success_Indicator(models.Model):
    description = models.CharField(max_length = 200)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.description)

    class Meta:
        ordering = ('description',)


class Accomplishment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    core_function_output = models.CharField(max_length = 200)
    indicator = models.ManyToManyField(Success_Indicator,blank = True)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.core_function_output)

#
# class Actual_Accomplishment(models.Model):
#     accomplishment = models.ForeignKey(Accomplishment, on_delete=models.CASCADE)
#     actual_accomplishment = models.CharField(max_length = 200)
#     year = models.ForeignKey(Year, on_delete=models.CASCADE)
#     user = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     date_created = models.DateTimeField(auto_now_add = True)
#     date_updated = models.DateTimeField(auto_now = True)
#
#     def __str__(self):
#         return str(self.actual_accomplishment)

class Rating_Accomplishment(models.Model):
    accomplishment = models.ForeignKey(Accomplishment, on_delete=models.CASCADE)
    actual_accomplishment = models.CharField(max_length = 200)
    ratings = models.FloatField(default=0)
    remarks = models.CharField(max_length = 200,blank=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.remarks)
