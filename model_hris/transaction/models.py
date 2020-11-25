from django.db import models
from django.db.models import Model
from model_hris.info_profile.models import Profile
from django.contrib.auth.models import User
from django.utils import timezone
leave_type = (
    ('1', 'Sick Leave',),
    ('2', 'Vacation Leave',),
    ('3', 'Special Leave',),
    ('4', 'Offset',),
)

status = (
    ('1', 'Pending',),
    ('2', 'Approved',),
    ('3', 'Rejected',),
)


class Deducted_Transaction(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length = 200)
    leave_type = models.CharField(max_length=50,choices=leave_type)
    status = models.CharField(default=1,max_length=50,choices=status)
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

class Deducted_Action_Transaction(models.Model):
    deducted_transaction = models.OneToOneField(Deducted_Transaction, on_delete=models.CASCADE)
    days = models.DecimalField(default=1,max_digits = 50,decimal_places=3)
    remarks = models.CharField(blank=True,max_length = 200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

class Rejected_Transaction(models.Model):
    deducted_transaction = models.OneToOneField(Deducted_Transaction, on_delete=models.CASCADE)
    remarks = models.CharField(max_length = 200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

class Generated_Transaction(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    remarks = models.CharField(max_length = 200)
    leave_type = models.CharField(max_length=50,choices=leave_type)
    days = models.DecimalField(default=1,max_digits = 50,decimal_places=3)
    is_batch = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

class Batch_Generated_Transaction(models.Model):
    remarks = models.CharField(max_length = 200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
