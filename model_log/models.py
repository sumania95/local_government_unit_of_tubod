from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from django.contrib.auth.models import User
from app_info_profile.models import Profile

log_result = (
    ('1', 'Single',),
    ('2', 'Married',),
    ('3', 'Widowed',),
    ('4', 'Separated',),
    ('5', 'Annulled',),
)

class User_Logs(models.Model):
    remarks = models.CharField(max_length=200,choices = log_result)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    date_updated = models.DateTimeField(auto_now = True)
    date_created = models.DateTimeField(auto_now_add = True)



admin_log_result = (
    ('1', 'New employee created',),
    ('2', 'Update information',),
    ('3', 'Designated assigned',),
    ('4', 'Designated removed',),
    ('5', 'Contractual assigned',),
    ('6', 'Reward created',),
    ('7', 'Reward updated',),
    ('8', 'Applied leave',),
    ('9', 'Approved leave',),
    ('10', 'Rejected leave',),
    ('11', 'Generated leave',),
    ('11', 'Change settings',),
)

class Admin_Logs(models.Model):
    remarks = models.CharField(max_length=200,choices = admin_log_result)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    date_updated = models.DateTimeField(auto_now = True)
    date_created = models.DateTimeField(auto_now_add = True)
