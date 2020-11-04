from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from app_info_profile.models import Profile

class Voucher(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    voucher = models.CharField(max_length = 200)
    reason = models.CharField(max_length = 200)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.profile.surname) + ' ' + str(self.profile.firstname)
